#!/usr/bin/env python3
"""Compose GitHub Release notes for one version from both changelogs.

The notes tell a student which asset to download, then reproduce the
Traditional Chinese and English changelog entries for the version. A release
version without an entry in both changelogs is an error, so a tag cannot be
promoted with notes that say nothing.

Usage:
    release-notes.py <version> [--output FILE]
    release-notes.py --newest [--output FILE]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHANGELOGS = (("zh", "CHANGELOG.md"), ("en", "CHANGELOG.en.md"))
REPOSITORY = "https://github.com/wengan-li/ncku-thesis-template-latex"
VERSION = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{12}$")
ENTRY_HEADING = re.compile(r"^### \[(v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{12})\]\(")
ANY_HEADING = re.compile(r"^#{2,3} ")

DOWNLOAD = {
    "zh": (
        "## 下載",
        "",
        "- 撰寫論文：下載`ncku-thesis-template-latex-{version}.zip`，解壓後先閱讀其中的`README.md`。",
        "- 預覽成品：`ncku-thesis-template-latex-examples-{version}.zip`只包含已建置的範例PDF。",
        "- 學校及系所的現行規定永遠優先於本範本。",
        "",
        "## 本版變更",
        "",
    ),
    "en": (
        "## Download",
        "",
        "- To write a thesis: download `ncku-thesis-template-latex-{version}.zip` and read its `README.md` first.",
        "- To preview the output: `ncku-thesis-template-latex-examples-{version}.zip` contains only the generated example PDFs.",
        "- Current university and department rules take precedence over the template.",
        "",
        "## Changes in this release",
        "",
    ),
}


def fail(message: str) -> None:
    print(f"release-notes: {message}", file=sys.stderr)
    raise SystemExit(1)


def entry_body(text: str, version: str, name: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        match = ENTRY_HEADING.match(line)
        if match and match.group(1) == version:
            start = index + 1
            break
    if start is None:
        fail(f"{name} has no entry for {version}")
    body: list[str] = []
    for line in lines[start:]:
        if ANY_HEADING.match(line):
            break
        body.append(line.rstrip())
    while body and not body[0]:
        body.pop(0)
    while body and not body[-1]:
        body.pop()
    if not any(line.startswith("- ") for line in body):
        fail(f"{name} entry for {version} has no bullet points")
    return body


def newest_version(text: str, name: str) -> str:
    for line in text.splitlines():
        match = ENTRY_HEADING.match(line)
        if match:
            return match.group(1)
    fail(f"{name} has no release entries")
    raise AssertionError("unreachable")


def compose(version: str) -> str:
    sections: list[str] = []
    for lang, name in CHANGELOGS:
        text = (ROOT / name).read_text(encoding="utf-8")
        header = [line.format(version=version) for line in DOWNLOAD[lang]]
        sections.append("\n".join(header + entry_body(text, version, name)))
    sections.append(
        "\n".join(
            (
                "---",
                "",
                f"完整變更記錄 / Full changelog: [`CHANGELOG.md`]({REPOSITORY}/blob/{version}/CHANGELOG.md)"
                f" · [`CHANGELOG.en.md`]({REPOSITORY}/blob/{version}/CHANGELOG.en.md)",
            )
        )
    )
    return "\n\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("version", nargs="?", help="release version, e.g. v2.0.6.260822064417")
    target.add_argument("--newest", action="store_true", help="use the newest entry in CHANGELOG.md")
    parser.add_argument("--output", type=Path, help="write the notes here instead of stdout")
    args = parser.parse_args()

    if args.newest:
        version = newest_version((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), "CHANGELOG.md")
    else:
        version = args.version
        if not VERSION.match(version):
            fail(f"not a release version: {version} (expected vMAJOR.MINOR.PATCH.YYMMDDhhmmss)")

    notes = compose(version)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(notes, encoding="utf-8")
        print(f"release-notes: wrote {version} notes to {args.output}")
    else:
        sys.stdout.write(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
