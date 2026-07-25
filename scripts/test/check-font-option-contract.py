#!/usr/bin/env python3
"""Verify font-option parser state, rendered fonts, and source boundary."""

from __future__ import annotations

import argparse
from pathlib import Path

from _contract import ROOT, l3keys_block, normalized, require_for, require_single_a4_page

require = require_for("Font option contract")

parser = argparse.ArgumentParser()
parser.add_argument("build_dir", type=Path)
args = parser.parse_args()

build = args.build_dir
log = (build / "font-option-contract.log").read_text(errors="replace")
text = (build / "font-option-contract.txt").read_text(errors="replace")
pdfinfo = (build / "font-option-contract.pdfinfo").read_text(errors="replace")
fonts = (build / "font-option-contract.fonts").read_text(errors="replace")
source = (ROOT / "thesis/template/command/cmd-font.tex").read_text()
normalized_log = normalized(log)

markers = [
    "NCKU-FONT-OPTION-FULL: times.ttf|timesi.ttf|timesbd.ttf|timesbi.ttf",
    "NCKU-FONT-OPTION-PARTIAL: ||timesbd.ttf|",
    "NCKU-FONT-OPTION-OMITTED: |||",
    "NCKU-TEST-PASS: font option parser and English/CJK loading routes",
]
for marker in markers:
    require(marker in normalized_log, f"missing font-option marker: {marker}")
require("NCKU-TEST-FAIL:" not in log, "font-option fixture emitted failure marker")

for phrase in [
    "Normal English and 中文普通字型。",
    "Italic English and 中文斜體字型。",
    "Bold English and 中文粗體字型。",
    "Bold italic English and 中文粗斜體字型。",
]:
    require(phrase in text, f"missing rendered font-option text: {phrase}")

require_single_a4_page(require, pdfinfo)
for font_name in [
    "TimesNewRomanPSMT",
    "TimesNewRomanPS-ItalicMT",
    "TimesNewRomanPS-BoldMT",
    "TimesNewRomanPS-BoldItalicMT",
]:
    require(font_name in fonts, f"focused PDF missing expected font: {font_name}")
require(
    fonts.count("DFKaiShu-SB-Estd-BF") == 4,
    "focused PDF must contain KaiU normal/fake-bold/fake-slant/fake-bold-slant subsets",
)

require(
    r"\cs_new_protected:Npn \NCKUPrivateSetFontOptionKeys #1" in source,
    "font-option private parser seam is missing",
)
require(
    source.count(r"\NCKUPrivateSetFontOptionKeys{#1}") == 2,
    "English and CJK setters do not both route through the private seam",
)
require(
    r"\keys_define:nn { ncku / font-options }" in source,
    "font-option l3keys family is missing",
)
require(
    r"\keys_set:nn { ncku / font-options } {#1}" in source,
    "font-option private seam does not route through l3keys",
)
font_block = l3keys_block(source, "ncku / font-options", "ncku_font_options_set_keys:n")
require(font_block is not None, "cannot isolate font-option l3keys block")
require(
    font_block is not None and font_block.count(".tl_set_e:N") == 4,
    "font-option parser must preserve expanded storage for exactly four keys",
)
require(
    r"/ParseFontOption/.is family" not in source,
    "legacy font-option pgfkeys family remains after migration",
)
require(
    r"\keys_define:nn { ncku / custom-font-files }" in source,
    "completed custom-font filename l3keys family changed unexpectedly",
)
require("l3keys2e" not in source, "font source must not use l3keys2e")

print("Font option contract PASS: l3keys expanded state, reset, English/CJK rendering, fonts, and source boundary")
