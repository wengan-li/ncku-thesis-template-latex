#!/usr/bin/env python3
"""Keep the conf/conf.tex line numbers cited in the student guides truthful.

`thesis/README.md` (must-change table) and `thesis/conf/README.md` (the
required/optional line at the top of each section), with their English
companions, tell students which line of `conf/conf.tex` to edit. Those numbers
were stable while the file was byte-pinned to v1.8.2; since the pin moved onto
a tag-materialized fixture on 2026-08-23, this check is what keeps them honest.

Two directions are checked:

1. every line number in EXPECTED still holds the command the guides describe;
2. every line number cited in the four guides is one of the EXPECTED lines, so
   a new citation cannot point at an unchecked line.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONF = ROOT / "thesis" / "conf" / "conf.tex"
GUIDES = (
    "thesis/README.md",
    "thesis/README.en.md",
    "thesis/conf/README.md",
    "thesis/conf/README.en.md",
)

# line number -> text that line must contain
EXPECTED: dict[int, str] = {
    13: r"\ExampleMode",
    20: r"\ShowDOI",
    29: r"\SetLineStretch",
    44: r"\DisplayCoverInEng",
    45: r"\DisplayCoverPeoplesBothNames",
    71: r"\SetTitle",
    73: "Thesis/Dissertation Template",
    80: r"\DisplayDraft",
    84: r"\SetWatermarkText",
    89: r"\UseWatermarkFigureStyle",
    99: r"\PhdDegree",
    111: r"\SetMyName",
    125: r"\SetOralDate",
    138: r"\SetCoverDate",
    148: r"\SetDeptCSIE",
    166: r"\SetAdvisorNameA",
    167: r"\SetAdvisorNameB",
    168: r"\SetAdvisorNameC",
    176: r"\DisplayOralTemplate",
    193: r"\SetCommitteeSize",
    204: r"\DisplayOralImage",
    205: r"\SetOralImageChi",
    206: r"\SetOralImageEng",
    224: r"\SetKeywords",
    246: r"\SetAbstractChiKeywords",
    248: r"\SetAbstractExtKeywords",
    264: r"\IndexChiMode",
    265: r"\IndexEngMode",
    273: r"\SetIndexTitleText",
    279: r"\SetFiguresIndexTitleText",
    288: r"\SetCustomFigureName",
    297: r"\SetCustomTableName",
    362: r"\SetupReference",
    365: r"End of \SetupReference",
    564: r"\SetNumberingFormat[Chapter]",
    629: "Theorems",
}

# Chinese guides: 第13行, 第44–45行, 第80、84、89行, 第564行起
ZH_CITATION = re.compile(r"第([0-9]+(?:[–、][0-9]+)*)行")
# English guides: line 13, lines 44–45, lines 80, 84, 89, line 564
EN_CITATION = re.compile(r"\blines? ([0-9]+(?:(?:–|, )[0-9]+)*)")
# must-change tables: the second cell holds only numbers, ranges, and separators
TABLE_LINE_CELL = re.compile(r"^\| [^|]+ \| ([0-9]+(?:[–、,][ ]?[0-9]+)*) \| ")


def cited_numbers(text: str) -> set[int]:
    numbers: set[int] = set()
    for pattern in (ZH_CITATION, EN_CITATION):
        for group in pattern.findall(text):
            numbers.update(int(n) for n in re.findall(r"[0-9]+", group))
    for line in text.splitlines():
        match = TABLE_LINE_CELL.match(line)
        if match:
            numbers.update(int(n) for n in re.findall(r"[0-9]+", match.group(1)))
    return numbers


def main() -> int:
    failures: list[str] = []
    conf_lines = CONF.read_text(encoding="utf-8").splitlines()
    for number, needle in sorted(EXPECTED.items()):
        if number > len(conf_lines):
            failures.append(f"conf.tex has no line {number} (expected {needle!r})")
        elif needle not in conf_lines[number - 1]:
            failures.append(
                f"conf.tex line {number} no longer contains {needle!r}: {conf_lines[number - 1].strip()!r}"
            )

    cited_total = 0
    for relative in GUIDES:
        cited = cited_numbers((ROOT / relative).read_text(encoding="utf-8"))
        cited_total += len(cited)
        for number in sorted(cited):
            if number not in EXPECTED:
                failures.append(f"{relative} cites conf.tex line {number}, which this check does not cover")

    if failures:
        print("conf.tex line references FAIL:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print(
        f"conf.tex line references PASS: {len(EXPECTED)} checked lines, "
        f"{cited_total} citations across {len(GUIDES)} guides"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
