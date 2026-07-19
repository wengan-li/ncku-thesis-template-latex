#!/usr/bin/env python3
"""Validate language-separated documentation pairs and first-party Markdown links.

This checker proves deterministic structure only. Translation quality and semantic
parity remain manual review requirements.
"""

from __future__ import annotations

import os
import re
import sys
import urllib.parse
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[2]

GUIDE_PAIRS: tuple[tuple[str, str, str, int], ...] = (
    ("README.md", "README.en.md", "root-readme", 7),
    ("thesis/README.md", "thesis/README.en.md", "student-readme", 7),
    ("thesis/conf/README.md", "thesis/conf/README.en.md", "student-config", 8),
    ("docs/README.md", "docs/README.en.md", "project-index", 4),
    (
        "docs/v1-to-v2-migration.md",
        "docs/v1-to-v2-migration.en.md",
        "v1-v2-migration",
        8,
    ),
    ("docs/features/README.md", "docs/features/README.en.md", "feature-index", 2),
    (
        "thesis/template/style/Customization.md",
        "thesis/template/style/Customization.en.md",
        "style-customization",
        7,
    ),
    (
        "thesis/template/style/ncku/README.md",
        "thesis/template/style/ncku/README.en.md",
        "ncku-department-catalogue",
        5,
    ),
)

SUMMARY_PAIRS: tuple[tuple[str, str], ...] = (
    (
        "docs/features/v2-modernization.md",
        "docs/features/v2-modernization.en.md",
    ),
    (
        "docs/features/validation-and-performance.md",
        "docs/features/validation-and-performance.en.md",
    ),
    (
        "docs/features/release-and-distribution.md",
        "docs/features/release-and-distribution.en.md",
    ),
)

CHINESE_USER_DOCS = tuple(pair[0] for pair in GUIDE_PAIRS + SUMMARY_PAIRS) + (
    "CHANGELOG.md",
)
ENGLISH_USER_DOCS = tuple(pair[1] for pair in GUIDE_PAIRS + SUMMARY_PAIRS)
CANTONESE_ONLY = ("呢個", "只係", "唔", "嘅", "喺", "咁樣")
WRONG_PRODUCT_CASING = re.compile(r"\b(?:LaTex|Latex|XeLatex|Xelatex)\b")
MUTABLE_RELEASE_LABEL = re.compile(
    r"目前正式release|最新immutable release|正式目標|最新production release|"
    r"Current production release|latest immutable release|Production target|"
    r"Latest production release"
)
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$", re.MULTILINE)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
PAIR_META = re.compile(
    r"<!-- doc-pair: ([^;]+); lang: ([^;]+); topics: ([a-z0-9,-]+) -->"
)
CJK = re.compile(r"[\u3400-\u9fff]")
VISIBLE_LANGUAGE_LABEL = re.compile(r"\*\*(?:繁體中文|English)\*\*")
FORBIDDEN_PUBLIC_VOICE = re.compile(
    r"我|維護者|非本校|非成大|非NCKU|非 NCKU|非本維護者|外校|"
    r"不要從讀者語言推斷學校profile|"
    r"\bI\b|\b[Mm]aintainers?\b|[Nn]on-NCKU|"
    r"Do not infer an institution profile from the reader's language"
)


def fail(message: str) -> NoReturn:
    raise AssertionError(message)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing documentation file: {relative}")
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
        fail("unclosed Markdown fence while checking documentation")
    return "\n".join(output)


def fenced_blocks(text: str) -> tuple[str, ...]:
    blocks: list[str] = []
    current: list[str] | None = None
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if fence is None:
            if match:
                token = match.group(1)
                fence = (token[0], len(token))
                current = [line]
            continue
        assert current is not None
        current.append(line)
        if match:
            token = match.group(1)
            if token[0] == fence[0] and len(token) >= fence[1] and not match.group(2).strip():
                blocks.append("\n".join(current))
                current = None
                fence = None
    if fence is not None:
        fail("unclosed Markdown fence while comparing paired guides")
    return tuple(blocks)


def h2_count(text: str) -> int:
    return len(re.findall(r"^##\s+", text, re.MULTILINE))


def github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading.strip().lower())
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^\w\-\s\u3400-\u9fff]", "", heading)
    return re.sub(r"[\s\-]+", "-", heading).strip("-")


def anchors(path: Path) -> set[str]:
    text = strip_fenced_blocks(path.read_text(encoding="utf-8"))
    return {github_slug(match.group(2)) for match in HEADING.finditer(text)}


def check_guide_pair(zh_relative: str, en_relative: str, pair_id: str, minimum: int) -> None:
    zh = read(zh_relative)
    en = read(en_relative)
    zh_meta = PAIR_META.search(zh)
    en_meta = PAIR_META.search(en)
    if not zh_meta or not en_meta:
        fail(f"{pair_id}: missing doc-pair metadata")
    if zh_meta.group(1) != pair_id or en_meta.group(1) != pair_id:
        fail(f"{pair_id}: metadata pair identifier drift")
    if zh_meta.group(2) != "zh-Hant-TW" or en_meta.group(2) != "en":
        fail(f"{pair_id}: language metadata drift")
    if zh_meta.group(3) != en_meta.group(3):
        fail(f"{pair_id}: stable topic IDs differ")
    topics = zh_meta.group(3).split(",")
    if len(topics) < minimum:
        fail(f"{pair_id}: expected at least {minimum} stable topics, found {len(topics)}")
    if h2_count(zh) != len(topics) or h2_count(en) != len(topics):
        fail(f"{pair_id}: H2 count does not match stable topic count")

    zh_name = Path(zh_relative).name
    en_name = Path(en_relative).name
    switcher = f"[繁體中文]({zh_name}) | [English]({en_name})"
    if switcher not in zh or switcher not in en:
        fail(f"{pair_id}: missing reciprocal top language switcher")
    if fenced_blocks(zh) != fenced_blocks(en):
        fail(f"{pair_id}: paired fenced code blocks differ")


def check_summary_pair(zh_relative: str, en_relative: str) -> None:
    zh = read(zh_relative)
    en = read(en_relative)
    zh_name = Path(zh_relative).name
    en_name = Path(en_relative).name
    if f"<!-- language: en; summary: {zh_name} -->" not in en:
        fail(f"{en_relative}: missing English summary metadata")
    if f"<!-- language: zh-Hant-TW; summary-of: {en_name} -->" not in zh:
        fail(f"{zh_relative}: missing Chinese summary metadata")
    switcher = f"[繁體中文摘要]({zh_name}) | [English technical record]({en_name})"
    if switcher not in en or switcher not in zh:
        fail(f"{en_relative}: missing reciprocal summary switcher")
    if len(re.findall(r"^- ", zh, re.MULTILINE)) < 5:
        fail(f"{zh_relative}: executive summary needs at least five bullets")
    if "## 繁體中文摘要" in en or "## English technical record" in en:
        fail(f"{en_relative}: old inline-language section survived")


def check_no_legacy_locale_suffixes() -> None:
    failures = sorted(
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*.zh-TW.md")
        if not any(part in {".git", "build"} for part in path.parts)
        and not path.is_symlink()
    )
    if failures:
        fail("legacy .zh-TW.md paths remain: " + ", ".join(failures))


def check_no_repeated_language_labels() -> None:
    failures: list[str] = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "build"} for part in path.parts) or path.is_symlink():
            continue
        if VISIBLE_LANGUAGE_LABEL.search(path.read_text(encoding="utf-8")):
            failures.append(str(path.relative_to(ROOT)))
    if failures:
        fail("visible per-section language labels remain: " + ", ".join(failures))


def check_language_hygiene() -> None:
    for relative in CHINESE_USER_DOCS + ENGLISH_USER_DOCS:
        plain = strip_fenced_blocks(read(relative))
        if relative == "CHANGELOG.md":
            plain = plain.split("## 1.8.x", 1)[0]
        bad_case = sorted(set(WRONG_PRODUCT_CASING.findall(plain)))
        if bad_case:
            fail(f"{relative}: incorrect product casing: {', '.join(bad_case)}")

    for relative in CHINESE_USER_DOCS:
        plain = strip_fenced_blocks(read(relative))
        if relative == "CHANGELOG.md":
            plain = plain.split("## 1.8.x", 1)[0]
        present = [token for token in CANTONESE_ONLY if token in plain]
        if present:
            fail(f"{relative}: Cantonese-only prose tokens: {', '.join(present)}")

    for relative in ENGLISH_USER_DOCS:
        plain = strip_fenced_blocks(read(relative))
        plain = re.sub(r"<!--.*?-->", "", plain, flags=re.DOTALL)
        plain = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", plain)
        plain = re.sub(r"`[^`]*`", "", plain)
        plain = re.sub(r"^(?:\[)?繁體中文[^\n]*$", "", plain, flags=re.MULTILINE)
        if CJK.search(plain):
            lines = [line for line in plain.splitlines() if CJK.search(line)]
            fail(f"{relative}: CJK prose outside code/switcher: {lines[0]}")


def check_no_mutable_release_labels() -> None:
    failures: list[str] = []
    for path in (ROOT / "docs").rglob("*.md"):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if MUTABLE_RELEASE_LABEL.search(line):
                failures.append(f"{path.relative_to(ROOT)}:{number}")
    if failures:
        fail("mutable current/latest release labels remain: " + ", ".join(failures))


def public_markdown_paths() -> tuple[Path, ...]:
    paths = [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CHANGELOG.en.md",
    ]
    paths.extend((ROOT / "docs").rglob("*.md"))
    paths.extend((ROOT / "thesis").rglob("*.md"))
    return tuple(sorted(set(path for path in paths if path.is_file())))


def check_public_voice() -> None:
    failures: list[str] = []
    for path in public_markdown_paths():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if FORBIDDEN_PUBLIC_VOICE.search(line):
                failures.append(f"{path.relative_to(ROOT)}:{number}")
    if failures:
        fail("public owner-voice or cross-school wording drift: " + ", ".join(failures))

    required_third_person = {
        "README.md": (
            "本模版以XeLaTeX建置",
            "本模版將共用renderer",
        ),
        "README.en.md": (
            "This XeLaTeX template supports",
            "The template separates shared rendering",
        ),
        "docs/README.md": ("本目錄記錄",),
        "docs/README.en.md": ("This directory records",),
        "thesis/conf/README.md": ("repository baseline及migration hash不會",),
        "thesis/conf/README.en.md": (
            "the repository baseline and migration hash remain unchanged",
        ),
    }
    for relative, markers in required_third_person.items():
        text = read(relative)
        missing = [marker for marker in markers if marker not in text]
        if missing:
            fail(f"{relative}: missing third-person project voice: {', '.join(missing)}")

    internal_root_status = {
        "README.md": ("發行與Overleaf狀態", "本模版的V2已上載"),
        "README.en.md": ("Release and Overleaf status", "V2 has been uploaded"),
    }
    for relative, markers in internal_root_status.items():
        text = read(relative)
        leaked = [marker for marker in markers if marker in text]
        if leaked:
            fail(f"{relative}: internal release status leaked into public README: {', '.join(leaked)}")


def check_project_index_scope() -> None:
    internal_terms = (
        "docs/requirements",
        "todos/",
        ".gitkeep",
        "owner-approved",
        "文件生命週期",
        "Documentation lifecycle",
        "Source of truth",
        "source-of-truth",
        "feat/<short-name>",
        "branch checklist",
    )
    for relative in ("docs/README.md", "docs/README.en.md"):
        text = read(relative)
        leaked = [term for term in internal_terms if term in text]
        if leaked:
            fail(
                f"{relative}: internal repository-governance content leaked "
                f"into public index: {', '.join(leaked)}"
            )


def check_language_local_routes() -> None:
    required = {
        "README.en.md": (
            "docs/features/release-and-distribution.en.md",
            "CHANGELOG.en.md",
        ),
        "docs/README.md": (
            "../CHANGELOG.md",
            "features/v2-modernization.md",
            "features/validation-and-performance.md",
            "features/release-and-distribution.md",
        ),
        "docs/README.en.md": (
            "../CHANGELOG.en.md",
            "features/v2-modernization.en.md",
            "features/validation-and-performance.en.md",
            "features/release-and-distribution.en.md",
        ),
        "docs/features/README.md": (
            "v2-modernization.md",
            "validation-and-performance.md",
            "release-and-distribution.md",
        ),
        "docs/features/README.en.md": (
            "v2-modernization.en.md",
            "validation-and-performance.en.md",
            "release-and-distribution.en.md",
        ),
    }
    for relative, routes in required.items():
        text = read(relative)
        missing = [route for route in routes if route not in text]
        if missing:
            fail(f"{relative}: missing language-local routes: {', '.join(missing)}")


def check_institution_profile_docs() -> None:
    department_source = read("thesis/template/style/ncku/department.tex")
    college_source = read("thesis/template/style/ncku/college.tex")
    ncku_profile = read("thesis/template/style/ncku/ncku.tex")
    compat = read("thesis/template/compat/v1.tex")
    configure = read("thesis/template/configure.tex")
    custom_fixture = read("tests/603-custom-institution-api.tex")

    catalogue_inputs = (
        "\\input{./template/style/ncku/college}",
        "\\input{./template/style/ncku/department}",
    )
    missing_inputs = [item for item in catalogue_inputs if item not in ncku_profile]
    if missing_inputs:
        fail("NCKU profile no longer owns its catalogue inputs: " + ", ".join(missing_inputs))
    forbidden_compat_inputs = (
        "template/command/cmd-college",
        "template/command/cmd-department",
        "template/style/ncku/college",
        "template/style/ncku/department",
    )
    leaked_inputs = [item for item in forbidden_compat_inputs if item in compat]
    if leaked_inputs:
        fail("V1 adapter leaked NCKU catalogue inputs: " + ", ".join(leaked_inputs))
    if "\\providecommand{\\TemplateConfigurationFile}{./conf/conf}" not in configure:
        fail("configure: missing default-preserving profile-fixture config seam")
    load_order_markers = (
        "\\input{./template/command/command}",
        "\\input{./template/style/style}",
        "\\input{\\TemplateConfigurationFile}",
        "\\FillInPDFData",
    )
    load_positions = [configure.find(marker) for marker in load_order_markers]
    if -1 in load_positions or load_positions != sorted(load_positions):
        fail(
            "configure: load order must remain command -> selected profile -> "
            "student configuration -> PDF metadata initialization"
        )
    for marker in (
        "custom profile excludes NCKU department presets",
        "custom profile excludes NCKU college presets",
    ):
        if marker not in custom_fixture:
            fail(f"custom institution fixture missing profile-isolation marker: {marker}")

    def compact(value: str) -> str:
        return re.sub(r"\s+", " ", value.strip())

    colleges: list[tuple[str, str, str]] = []
    for command, body in re.findall(
        r"\\newcommand\{\\(SetCollege\w+)\}\s*\{(.*?)\}\s*% End of \\newcommand\{\}",
        college_source,
        re.DOTALL,
    ):
        values = re.search(r"\\SetCollName\{([^{}]*)\}\{([^{}]*)\}", body)
        if values is None:
            fail(f"unparsed NCKU college preset: {command}")
        colleges.append((command, compact(values.group(1)), compact(values.group(2))))

    departments: list[tuple[str, str, str, str, str]] = []
    for command, body in re.findall(
        r"\\newcommand\{\\(SetDept\w+)\}\s*\{(.*?)\}\s*% End of \\newcommand\{\}",
        department_source,
        re.DOTALL,
    ):
        values = re.search(
            r"\\SetDeptName\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}", body
        )
        college = re.search(r"\\(SetCollege\w+)", body)
        if values is None or college is None:
            fail(f"unparsed NCKU department preset: {command}")
        departments.append(
            (
                command,
                compact(values.group(1)),
                compact(values.group(2)),
                compact(values.group(3)),
                college.group(1),
            )
        )

    if len(colleges) != 9 or len(departments) != 110:
        fail(
            "NCKU catalogue count changed; review source, public catalogue, "
            f"and repository skill together: colleges={len(colleges)}, "
            f"departments={len(departments)}"
        )

    zh = read("thesis/template/style/ncku/README.md")
    en = read("thesis/template/style/ncku/README.en.md")
    college_names = {command: (zh_name, en_name) for command, zh_name, en_name in colleges}
    grouped: dict[str, list[tuple[str, str, str, str]]] = {
        command: [] for command, _, _ in colleges
    }
    for command, zh_name, short_name, en_name, college in departments:
        if college not in grouped:
            fail(f"{command}: unknown NCKU college preset {college}")
        grouped[college].append((command, zh_name, short_name, en_name))

    for text, language in ((zh, "zh"), (en, "en")):
        for command, zh_name, en_name in colleges:
            row = f"| `\\{command}` | `{zh_name}` | `{en_name}` |"
            if row not in text:
                fail(f"NCKU {language} catalogue missing college row: {command}")
        for college, rows in grouped.items():
            zh_college, en_college = college_names[college]
            heading = (
                f"### {zh_college}（`\\{college}`）— {len(rows)}個"
                if language == "zh"
                else f"### {en_college} (`\\{college}`) — {len(rows)} presets"
            )
            if heading not in text:
                fail(f"NCKU {language} catalogue missing group heading: {college}")
            section = text.split(heading, 1)[1].split("\n### ", 1)[0]
            for command, zh_name, short_name, en_name in rows:
                row = (
                    f"| `\\{command}` | `{zh_name}` | `{short_name}` | "
                    f"`{en_name}` |"
                )
                if row not in section:
                    fail(
                        f"NCKU {language} catalogue row/value/college drift: {command}"
                    )

    generic_markers = (
        "\\SetUniversityName",
        "\\SetCollName",
        "\\SetDeptName",
        "\\GetDeptEngShortName",
    )
    for relative in (
        "thesis/template/style/ncku/README.md",
        "thesis/template/style/ncku/README.en.md",
    ):
        text = read(relative)
        missing = [marker for marker in generic_markers if marker not in text]
        if missing:
            fail(f"{relative}: generic institution API missing: {', '.join(missing)}")

    if (ROOT / "thesis/template/style/ntu").exists():
        fail("NTU profile now exists; replace the illustrative-only documentation claim")
    ntu_markers = (
        "\\SetNTUDeptCSIE",
        "https://www.lib.ntu.edu.tw/doc/cl/THESISSAMPLE.pdf",
        "https://www.lib.ntu.edu.tw/doc/CL/thesissample_en.pdf",
        "https://www.csie.ntu.edu.tw/en/AboutUs",
        "2026-07-19",
        "% conf/conf.tex: replace the existing NCKU department selection.",
    )
    for relative in (
        "thesis/template/style/Customization.md",
        "thesis/template/style/Customization.en.md",
    ):
        text = read(relative)
        missing = [marker for marker in ntu_markers if marker not in text]
        if missing:
            fail(f"{relative}: illustrative NTU boundary missing: {', '.join(missing)}")
        load_order_doc_markers = (
            "template/configure.tex",
            "template/command/command.tex",
            "template/style/style.tex",
            "\\TemplateConfigurationFile (default: ./conf/conf)",
            "\\FillInPDFData and remaining metadata/render initialization",
        )
        missing_order = [marker for marker in load_order_doc_markers if marker not in text]
        if missing_order:
            fail(f"{relative}: customization load-order contract missing: {', '.join(missing_order)}")

    skill = read(".agents/skills/repo-maintenance/SKILL.md")
    if "9 college presets and 110 department presets" not in skill:
        fail("repo-maintenance skill: NCKU catalogue inventory drift")


def check_changelog() -> None:
    zh = read("CHANGELOG.md")
    en = read("CHANGELOG.en.md")
    switcher = "[繁體中文](CHANGELOG.md) | [English](CHANGELOG.en.md)"
    if switcher not in en or switcher not in zh:
        fail("changelog: missing reciprocal language switcher")
    if "<!-- language: en; companion: CHANGELOG.md -->" not in en:
        fail("CHANGELOG.en.md: missing language metadata")
    if "<!-- language: zh-Hant-TW; companion: CHANGELOG.en.md -->" not in zh:
        fail("CHANGELOG.md: missing language metadata")
    if "# 變更記錄" not in zh or "V2變更記錄" in zh:
        fail("CHANGELOG.md: generic changelog heading is missing")
    marker = "## 1.8.x"
    if marker not in en or marker not in zh:
        fail("changelog: complete V1 history is missing")
    en_current, en_history = en.split(marker, 1)
    zh_current, zh_history = zh.split(marker, 1)
    if en_history != zh_history:
        fail("CHANGELOG.md: V1 history differs from the complete English companion")
    bad_case = sorted(set(WRONG_PRODUCT_CASING.findall(strip_fenced_blocks(en_current))))
    if bad_case:
        fail(f"CHANGELOG.en.md: incorrect current-release product casing: {', '.join(bad_case)}")
    en_releases = re.findall(r"^### \[(v2\.[^]]+)\]", en_current, re.MULTILINE)
    zh_releases = re.findall(r"^### \[(v2\.[^]]+)\]", zh_current, re.MULTILINE)
    if len(en_releases) < 2 or en_releases != zh_releases:
        fail("changelog: current V2 release entries differ between languages")
    if VISIBLE_LANGUAGE_LABEL.search(en_current) or VISIBLE_LANGUAGE_LABEL.search(zh_current):
        fail("changelog: old inline-language labels survived")


def check_package_routes() -> None:
    required = {
        "thesis/README.md": ("conf/README.md", "docs/v1-to-v2-migration.md"),
        "thesis/README.en.md": ("conf/README.en.md", "docs/v1-to-v2-migration.en.md"),
        "thesis/conf/README.md": (
            "../README.md",
            "../template/style/Customization.md",
            "../template/style/ncku/README.md",
        ),
        "thesis/conf/README.en.md": (
            "../README.en.md",
            "../template/style/Customization.en.md",
            "../template/style/ncku/README.en.md",
        ),
    }
    for relative, needles in required.items():
        text = read(relative)
        for needle in needles:
            if needle not in text:
                fail(f"{relative}: missing package route {needle}")


def check_instruction_alias() -> None:
    alias = ROOT / "CLAUDE.md"
    if not alias.is_symlink():
        fail("CLAUDE.md must be a symlink")
    if os.readlink(alias) != "AGENTS.md":
        fail("CLAUDE.md must point directly to relative AGENTS.md")
    if alias.resolve() != (ROOT / "AGENTS.md").resolve():
        fail("CLAUDE.md does not resolve to AGENTS.md")


def check_requirements_directory() -> None:
    entries = sorted(path.name for path in (ROOT / "docs/requirements").iterdir())
    if entries != [".gitkeep"]:
        fail(f"docs/requirements must contain only .gitkeep, found: {entries}")


def check_links() -> int:
    issues: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "build"} for part in path.parts) or path.is_symlink():
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
        for pair in GUIDE_PAIRS:
            check_guide_pair(*pair)
        for pair in SUMMARY_PAIRS:
            check_summary_pair(*pair)
        check_no_legacy_locale_suffixes()
        check_no_repeated_language_labels()
        check_language_hygiene()
        check_no_mutable_release_labels()
        check_public_voice()
        check_project_index_scope()
        check_language_local_routes()
        check_institution_profile_docs()
        check_changelog()
        check_package_routes()
        check_instruction_alias()
        check_requirements_directory()
        links = check_links()
    except AssertionError as error:
        print(f"Language-separated documentation FAIL: {error}", file=sys.stderr)
        return 1

    print(
        "Language-separated documentation PASS: "
        f"{len(GUIDE_PAIRS)} complete guide pairs, "
        f"{len(SUMMARY_PAIRS)} summary pairs, {links} Markdown links"
    )
    print("Semantic translation parity remains a manual review gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
