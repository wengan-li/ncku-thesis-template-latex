#!/usr/bin/env python3
"""Deterministic Markdown traversal and live-source validation regressions."""

from __future__ import annotations

import importlib.util
import os
import shutil
import tempfile
import unittest
from contextlib import ExitStack, contextmanager
from pathlib import Path
from unittest.mock import patch

CHECKER = Path(__file__).resolve().parents[1] / "scripts/test/check-bilingual-docs.py"
spec = importlib.util.spec_from_file_location("bilingual_docs", CHECKER)
docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docs)


@contextmanager
def intercept_scandir(replacement):
    with ExitStack() as stack:
        stack.enter_context(patch("os.scandir", side_effect=replacement))
        # Python 3.9 pathlib caches scandir on its accessor at import time.
        if hasattr(Path(), "_accessor"):
            stack.enter_context(patch.object(Path()._accessor, "scandir", replacement))
        yield


class MarkdownDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.root_patch = patch.object(docs, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.write("docs/live.md", "# Live\n")
        self.write("thesis/live.md", "# Live\n")

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_excluded_subtrees_are_never_entered(self):
        # Remove the subtree exactly when scandir enters it: no timing or thread
        # scheduling is needed to reproduce the concurrent package-cleanup race.
        checks = (
            docs.check_no_legacy_locale_suffixes,
            docs.check_no_repeated_language_labels,
            docs.check_links,
            docs.check_no_mutable_release_labels,
            docs.public_markdown_paths,
            docs.check_current_docs,
        )
        for check in checks:
            for relative in ("build/tests/overleaf-gallery", ".git/objects",
                             "docs/build/generated", "thesis/.git/objects"):
                with self.subTest(check=check.__name__, subtree=relative):
                    self.write(relative + "/ignored.md", "# English\n[bad](missing)\n")
                    entered = []
                    scandir = os.scandir

                    def remove_excluded(path):
                        if isinstance(path, int):  # shutil.rmtree's descriptor walk
                            return scandir(path)
                        candidate = Path(path)
                        relative_path = candidate.relative_to(self.root)
                        if any(part in {"build", ".git"} for part in relative_path.parts):
                            entered.append(relative_path.as_posix())
                            shutil.rmtree(candidate)
                            raise FileNotFoundError(str(candidate))
                        return scandir(path)

                    try:
                        with intercept_scandir(remove_excluded):
                            check()
                        self.assertEqual(entered, [], "discovery entered an excluded subtree")
                    finally:
                        # Each subtest gets its own excluded tree, including RED.
                        parts = Path(relative).parts
                        stop = next(i for i, part in enumerate(parts) if part in {"build", ".git"})
                        subtree = self.root.joinpath(*parts[:stop + 1])
                        if subtree.exists():
                            shutil.rmtree(subtree)

    def test_live_markdown_negatives_are_still_rejected(self):
        cases = (
            ("docs/untracked.zh-TW.md", "# Live\n",
             docs.check_no_legacy_locale_suffixes, "legacy .zh-TW.md paths remain"),
            (".agents/skills/live.md", "**English**\n",
             docs.check_no_repeated_language_labels, "visible per-section language labels remain"),
            ("thesis/context/.agents/live.md", "[bad](missing.md)\n",
             docs.check_links, "Markdown link failures"),
            ("docs/untracked.md", "Latest production release: v9.0.0\n",
             docs.check_no_mutable_release_labels, "mutable current/latest release labels remain"),
        )
        for relative, text, check, diagnostic in cases:
            with self.subTest(path=relative):
                path = self.write(relative, text)
                try:
                    with self.assertRaisesRegex(AssertionError, diagnostic):
                        check()
                finally:
                    path.unlink()

    def test_symlinks_are_excluded_and_hidden_source_is_checked(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside)
            (external / "bad.md").write_text("**English**\n[bad](missing)\n", encoding="utf-8")
            (self.root / "docs/alias.md").symlink_to(external / "bad.md")
            (self.root / "docs/alias-directory").symlink_to(external, target_is_directory=True)
            (self.root / "docs/broken.md").symlink_to(external / "missing.md")
            self.write("thesis/context/.agents/skills/reference.md", "[live](../../../live.md)\n")
            docs.check_no_repeated_language_labels()
            self.assertEqual(docs.check_links(), 1)
            public = {path.relative_to(self.root).as_posix() for path in docs.public_markdown_paths()}
            self.assertEqual(public, {"docs/live.md", "thesis/live.md",
                                     "thesis/context/.agents/skills/reference.md"})

    def test_source_traversal_errors_are_not_swallowed(self):
        scandir = os.scandir

        def deny_live_source(path):
            if Path(path) == self.root / "docs":
                raise PermissionError("live source denied")
            return scandir(path)

        with intercept_scandir(deny_live_source):
            with self.assertRaisesRegex(PermissionError, "live source denied"):
                docs.check_links()

    def test_disappearing_live_markdown_is_not_ignored(self):
        read_text = Path.read_text

        def remove_live_source(path, *args, **kwargs):
            if path == self.root / "docs/live.md":
                path.unlink()
            return read_text(path, *args, **kwargs)

        with patch.object(Path, "read_text", remove_live_source):
            with self.assertRaises(FileNotFoundError):
                docs.check_links()


if __name__ == "__main__":
    unittest.main()
