#!/usr/bin/env python3
"""Verify deprecated public commands stay literal and compatibility-owned."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import cast

ROOT = Path(__file__).resolve().parents[2]
API_CHECKER = ROOT / "scripts" / "test" / "check-v1-api.py"
EXPECTED_LOCATION = "thesis/template/compat/deprecated.tex"
EXPECTED_NAMES = {
    "AppendixChapterTitleNumFormat",
    "AppendixSectionTitleNumFormat",
    "AppendixSubSectionTitleNumFormat",
    "AppendixSubSubSectionTitleNumFormat",
    "BibStyleUseAbbrv",
    "BibStyleUseAlpha",
    "BibStyleUseApacite",
    "BibStyleUsePlain",
    "ChapterReferenceTitleInChi",
    "ChapterReferenceTitleInEng",
    "ChapterSectionTitleInChi",
    "ChapterTitleInChi",
    "ChapterTitleNumFormat",
    "ChapterTitleNumInChi",
    "EndChiAbstract",
    "InsertCenterImage",
    "InsertImage",
    "InsertMultiImages",
    "SectionTitleNumFormat",
    "SetChapterReferenceTitle",
    "SubSectionTitleNumFormat",
    "SubSubSectionTitleNumFormat",
    "ThesisWroteInChi",
}


def load_api_checker() -> ModuleType:
    spec = importlib.util.spec_from_file_location("ncku_check_v1_api", API_CHECKER)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Could not load {API_CHECKER.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_api_checker()
    entries = cast(dict[str, dict[str, list[str]]], module.collect_api())
    failures: list[str] = []

    for name in sorted(EXPECTED_NAMES):
        entry = entries.get(name)
        if entry is None:
            failures.append(f"missing deprecated command: {name}")
            continue
        if entry["signatures"] != ["latex:0"]:
            failures.append(
                f"signature drift for {name}: expected ['latex:0'], "
                f"found {entry['signatures']}"
            )
        if entry["defined_in"] != [EXPECTED_LOCATION]:
            failures.append(
                f"ownership drift for {name}: expected {EXPECTED_LOCATION}, "
                f"found {entry['defined_in']}"
            )

    ref_to = entries.get("RefTo")
    expected_ref_to = {
        "signatures": ["latex:1"],
        "defined_in": ["thesis/template/command/cmd-ref.tex"],
    }
    if ref_to != expected_ref_to:
        failures.append(
            "live RefTo helper drifted: expected the original one-argument "
            f"project declaration, found {ref_to}"
        )

    deprecated_source = ROOT / EXPECTED_LOCATION
    text = deprecated_source.read_text(encoding="utf-8")
    if text.count("\\errmessage{") != len(EXPECTED_NAMES):
        failures.append(
            "deprecated module must contain exactly one error diagnostic for each "
            f"of the {len(EXPECTED_NAMES)} commands"
        )
    if text.count("\\stop}") != len(EXPECTED_NAMES):
        failures.append(
            "deprecated module must contain exactly one stop token for each "
            f"of the {len(EXPECTED_NAMES)} commands"
        )

    if failures:
        print("Deprecated command compatibility FAIL:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(
        "Deprecated command compatibility PASS: "
        f"{len(EXPECTED_NAMES)} literal zero-argument tombstones owned by "
        f"{EXPECTED_LOCATION}; live one-argument RefTo preserved and "
        "comment-only zero-argument tombstone excluded"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
