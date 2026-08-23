#!/usr/bin/env python3
"""Materialize the v1.8.2 student-project inputs for the migration build.

The manifest lists the student-owned files of the v1.8.2 release (root entry
point, configuration, content, bibliography, oral-certificate assets) with the
bytes they had at the immutable tag. This checker proves the tag still carries
exactly those bytes, then writes them into a fixture directory next to symlinks
to the current template and teaching example, so `just test` can build an
unchanged 1.x project through the current V2 template.

The live `thesis/` files are free to evolve: they matched the tag byte for byte
until 2026-08-23, when the owner moved the pin onto this tag-materialized
fixture so that placeholders and typos in the packaged files could be fixed.

Usage: check-v1-project-migration.py <fixture-dir>
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tests" / "102-v1-project-migration.json"
PACKAGE_PREFIX = "thesis/"
SHARED_DIRECTORIES = ("template", "example")

ManifestEntry = dict[str, object]


def tag_bytes(tag: str, relative: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{tag}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def replace_symlink(link: Path, target: Path) -> None:
    if link.is_symlink() or link.exists():
        if link.is_dir() and not link.is_symlink():
            raise SystemExit(f"refusing to replace a real directory: {link}")
        link.unlink()
    link.symlink_to(os.path.relpath(target, link.parent), target_is_directory=True)


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__.strip().splitlines()[-1])
    fixture_dir = Path(sys.argv[1]).resolve()
    if ROOT not in fixture_dir.parents:
        raise SystemExit(f"fixture directory must live inside the repository: {fixture_dir}")

    if not MANIFEST.is_file():
        raise SystemExit(f"Missing migration manifest: {MANIFEST.relative_to(ROOT)}")
    payload = cast(dict[str, object], json.loads(MANIFEST.read_text(encoding="utf-8")))
    if payload.get("schema") != 1:
        raise SystemExit(f"Unsupported migration manifest schema: {payload.get('schema')!r}")
    source = cast(dict[str, str], payload.get("source"))
    entries = cast(dict[str, ManifestEntry], payload.get("entries"))
    if not source or not entries:
        raise SystemExit("Migration manifest must define source provenance and entries")
    for required in ("thesis/thesis.tex", "thesis/conf/conf.tex", "thesis/context/context.tex"):
        if required not in entries:
            raise SystemExit(f"Migration manifest must list {required}")

    tag = source["tag"]
    lookup = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{tag}^{{commit}}"], cwd=ROOT, capture_output=True, text=True
    )
    if lookup.returncode != 0:
        raise SystemExit(
            f"tag {tag} is not available in this clone; fetch tags first "
            "(the Test workflow checks out with fetch-tags: true)"
        )
    resolved = lookup.stdout.strip()
    failures: list[str] = []
    if resolved != source["commit"]:
        failures.append(f"tag {tag} resolves to {resolved}, manifest expects {source['commit']}")

    total_bytes = 0
    fixture_dir.mkdir(parents=True, exist_ok=True)
    for relative, expected in sorted(entries.items()):
        relative_path = Path(relative)
        if relative_path.is_absolute() or ".." in relative_path.parts or not relative.startswith(PACKAGE_PREFIX):
            failures.append(f"unsafe or non-package manifest path: {relative}")
            continue
        try:
            content = tag_bytes(tag, relative)
        except subprocess.CalledProcessError:
            failures.append(f"missing at {tag}: {relative}")
            continue
        expected_size = int(cast(int, expected["size"]))
        expected_sha256 = str(expected["sha256"])
        actual_sha256 = hashlib.sha256(content).hexdigest()
        total_bytes += len(content)
        if len(content) != expected_size:
            failures.append(f"size mismatch at {tag}: {relative}: expected {expected_size}, found {len(content)}")
        if actual_sha256 != expected_sha256:
            failures.append(f"SHA-256 mismatch at {tag}: {relative}: expected {expected_sha256}, found {actual_sha256}")
        destination = fixture_dir / relative[len(PACKAGE_PREFIX):]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)

    for name in SHARED_DIRECTORIES:
        replace_symlink(fixture_dir / name, ROOT / "thesis" / name)

    if failures:
        print("V1 project migration source FAIL:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(
        "V1 project migration source PASS: "
        f"{len(entries)} files ({total_bytes} bytes) materialized from {tag} at "
        f"{source['commit']} into {fixture_dir.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
