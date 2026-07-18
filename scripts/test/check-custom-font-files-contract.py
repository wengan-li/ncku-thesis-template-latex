#!/usr/bin/env python3
"""Verify custom-font filename parser state and its bounded source contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def normalized(text: str) -> str:
    return re.sub(r"\s+", "", text)


parser = argparse.ArgumentParser()
parser.add_argument("build_dir", type=Path)
args = parser.parse_args()

root = Path(__file__).resolve().parents[2]
source_path = root / "thesis/template/command/cmd-font.tex"
source = source_path.read_text(errors="replace")
log = (args.build_dir / "custom-font-files-contract.log").read_text(errors="replace")
text = (args.build_dir / "custom-font-files-contract.txt").read_text(errors="replace")
pdfinfo = (args.build_dir / "custom-font-files-contract.pdfinfo").read_text(errors="replace")
compact = normalized(log)

markers = [
    "NCKU-CFONT-INITIAL-ENG:times.ttf|timesi.ttf|timesbd.ttf|timesbi.ttf",
    "NCKU-CFONT-INITIAL-CHI:kaiu.ttf|||",
    "NCKU-CFONT-SCRATCH-ONE:scratch-normal.ttf|||",
    "NCKU-CFONT-SCRATCH-RESET:|||",
    "NCKU-CFONT-OMITTED-TYPE:10",
    "NCKU-CFONT-OMITTED-ENG:times.ttf|timesi.ttf|timesbd.ttf|timesbi.ttf",
    "NCKU-CFONT-ENG-EXPANDED:eng-normal-a.ttf|eng-italic-a.ttf|eng-bold-a.ttf|eng-bi-a.ttf",
    "NCKU-CFONT-ENG-PARTIAL-ALIAS:||eng-bold-b.ttf|",
    "NCKU-CFONT-ENG-AFTER-CHI:chi-normal.ttf|chi-italic.ttf|chi-bold.ttf|chi-bi.ttf",
    "NCKU-CFONT-CHI-FULL:chi-normal.ttf|chi-italic.ttf|chi-bold.ttf|chi-bi.ttf",
    "NCKU-CFONT-ALIASES-AFTER-OMITTED:|||/|||",
    "NCKU-TEST-PASS:customfontfilenameparsercontract",
]
for marker in markers:
    require(normalized(marker) in compact, f"missing custom-font marker: {marker}")

require("NCKU-TEST-FAIL" not in log, "custom-font contract emitted failure marker")
require("Custom font filename parser contract." in text, "focused PDF text missing")
require(re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None, "focused PDF is not one page")
require(re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None, "focused PDF is not A4")

require(
    r"\cs_new_protected:Npn \NCKUPrivateSetCustomFontFileKeys #1" in source,
    "custom-font private parser seam is missing",
)
require(
    source.count(r"\NCKUPrivateSetCustomFontFileKeys{#1}") == 2,
    "public custom-font setters do not both route through the private seam",
)
require(
    r"\keys_define:nn { ncku / custom-font-files }" in source,
    "custom-font l3keys family is missing",
)
require(
    r"\keys_set:nn { ncku / custom-font-files } {#1}" in source,
    "custom-font private seam does not route through l3keys",
)
custom_block_match = re.search(
    r"\\keys_define:nn \{ ncku / custom-font-files \}(.*?)\\cs_new_protected:Npn \\ncku_custom_font_files_set_keys:n",
    source,
    re.DOTALL,
)
if custom_block_match is None:
    raise SystemExit("cannot isolate custom-font filename l3keys block")
require(
    custom_block_match.group(1).count(".tl_set_e:N") == 4,
    "custom-font parser must preserve expanded storage for exactly four keys",
)
require(
    r"/ParseCustomFontFiles/.is family" not in source,
    "legacy custom-font pgfkeys family remains after migration",
)
require(
    r"\keys_define:nn { ncku / font-options }" in source,
    "adjacent font-option l3keys family is missing",
)
require("l3keys2e" not in source, "custom-font source must not use l3keys2e")

print("Custom font filename contract PASS: l3keys defaults, expansion, aliases, routes, and source boundary")
