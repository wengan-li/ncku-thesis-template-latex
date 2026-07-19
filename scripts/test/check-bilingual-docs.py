#!/usr/bin/env python3
"""Validate bilingual documentation structure and first-party Markdown links.

This checker proves only deterministic structure. It cannot prove translation
quality or semantic parity; those remain human review requirements.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

COMPLETE_BILINGUAL: dict[str, int] = {
    "README.md": 7,
    "thesis/README.md": 7,
    "thesis/conf/README.md": 8,
    "docs/README.md": 4,
    "docs/v1-to-v2-migration.md": 8,
    "docs/features/README.md": 2,
    "thesis/template/style/Customization.md": 7,
}

SUMMARY_PLUS_ENGLISH = (
    "docs/features/v2-modernization.md",
    "docs/features/validation-and-performance.md",
    "docs/features/release-and-distribution.md",
)

USER_FACING = tuple(COMPLETE_BILINGUAL)
CANTONESE_ONLY = ("呢個", "只係", "唔", "嘅", "喺", "咁樣")
WRONG_PRODUCT_CASING = re.compile(r"\b(?:LaTex|Latex|XeLatex|Xelatex)\b")
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$", re.MULTILINE)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


def fail(message: str) -> None:
    raise AssertionError(message)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing bilingual documentation file: {relative}")
    return path.read_text(encoding="utf-8")


def strip_fenced_blocks(text: str) -> str:
    output: list[str] = []
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = (token[0], len(token))
                output.append("")
                continue
            if token[0] == fence[0] and len(token) >= fence[1] and not match.group(2).strip():
                fence = None
                output.append("")
                continue
        output.append("" if fence else line)
    if fence is not None:
        fail("unclosed Markdown fence while checking bilingual docs")
    return "\n".join(output)


def h2_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*#*$", text, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[match.end() : end]))
    return sections


def github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading.strip().lower())
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^\w\-\s\u3400-\u9fff]", "", heading)
    return re.sub(r"[\s\-]+", "-", heading).strip("-")


def anchors(path: Path) -> set[str]:
    text = strip_fenced_blocks(path.read_text(encoding="utf-8"))
    return {github_slug(match.group(2)) for match in HEADING.finditer(text)}


def check_complete_bilingual(relative: str, minimum_sections: int) -> None:
    text = read(relative)
    if "<!-- bilingual:complete -->" not in text:
        fail(f"{relative}: missing bilingual:complete marker")
    sections = h2_sections(text)
    bilingual = 0
    for title, body in sections:
        if " / " not in title:
            fail(f"{relative}: H2 is not bilingual: {title}")
        if "**繁體中文**" not in body:
            fail(f"{relative}: missing Traditional-Chinese block in H2: {title}")
        if "**English**" not in body:
            fail(f"{relative}: missing English block in H2: {title}")
        bilingual += 1
    if bilingual < minimum_sections:
        fail(
            f"{relative}: expected at least {minimum_sections} bilingual H2 sections, "
            f"found {bilingual}"
        )


def check_summary_record(relative: str) -> None:
    text = read(relative)
    if "<!-- bilingual:summary-plus-english -->" not in text:
        fail(f"{relative}: missing summary-plus-English marker")
    chinese = text.find("## 繁體中文摘要")
    english = text.find("## English technical record")
    if chinese < 0 or english < 0 or chinese > english:
        fail(f"{relative}: invalid Chinese-summary/English-body order")
    summary = text[chinese:english]
    if len(re.findall(r"^- ", summary, re.MULTILINE)) < 5:
        fail(f"{relative}: Chinese executive summary needs at least five bullets")


def check_language_hygiene() -> None:
    for relative in USER_FACING:
        text = strip_fenced_blocks(read(relative))
        bad_case = sorted(set(WRONG_PRODUCT_CASING.findall(text)))
        if bad_case:
            fail(f"{relative}: incorrect product casing: {', '.join(bad_case)}")
        present = [token for token in CANTONESE_ONLY if token in text]
        if present:
            fail(f"{relative}: Cantonese-only prose tokens: {', '.join(present)}")


def check_changelog() -> None:
    text = read("CHANGELOG.md")
    if "<!-- bilingual:changelog-v2 -->" not in text:
        fail("CHANGELOG.md: missing bilingual V2 marker")
    region = text.split("## 1.8.x", 1)[0]
    releases = re.split(r"(?=^### \[v2\.)", region, flags=re.MULTILINE)[1:]
    if len(releases) < 2:
        fail("CHANGELOG.md: expected both current V2 release entries")
    for release in releases:
        title = release.splitlines()[0]
        if "**繁體中文**" not in release or "**English**" not in release:
            fail(f"CHANGELOG.md: incomplete bilingual V2 entry: {title}")


def check_package_routes() -> None:
    student = read("thesis/README.md")
    config = read("thesis/conf/README.md")
    if "conf/README.md" not in student:
        fail("thesis/README.md: missing packaged configuration-guide link")
    if "docs/v1-to-v2-migration.md" not in student:
        fail("thesis/README.md: missing canonical full migration link")
    if "../README.md" not in config:
        fail("thesis/conf/README.md: missing packaged student-guide backlink")
    if "../template/style/Customization.md" not in config:
        fail("thesis/conf/README.md: missing customization-guide link")


def check_links() -> int:
    issues: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "build"} for part in path.parts):
            continue
        text = strip_fenced_blocks(path.read_text(encoding="utf-8"))
        for raw in INLINE_LINK.findall(text):
            target = raw.strip().strip("<>")
            checked += 1
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                if target[1:] not in anchors(path):
                    issues.append(f"{path.relative_to(ROOT)}: missing {target}")
                continue
            file_part, _, fragment = target.partition("#")
            destination = (path.parent / urllib.parse.unquote(file_part)).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                issues.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                issues.append(f"{path.relative_to(ROOT)}: missing {target}")
            elif fragment and destination.is_file() and fragment not in anchors(destination):
                issues.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    if issues:
        fail("Markdown link failures:\n  - " + "\n  - ".join(issues))
    return checked


def main() -> int:
    try:
        for relative, minimum in COMPLETE_BILINGUAL.items():
            check_complete_bilingual(relative, minimum)
        for relative in SUMMARY_PLUS_ENGLISH:
            check_summary_record(relative)
        check_language_hygiene()
        check_changelog()
        check_package_routes()
        links = check_links()
    except AssertionError as error:
        print(f"Bilingual documentation FAIL: {error}", file=sys.stderr)
        return 1

    print(
        "Bilingual documentation PASS: "
        f"{len(COMPLETE_BILINGUAL)} complete guides, "
        f"{len(SUMMARY_PLUS_ENGLISH)} summary records, {links} Markdown links"
    )
    print("Semantic translation parity remains a human review gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
