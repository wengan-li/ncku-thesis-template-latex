#!/usr/bin/env python3
"""Verify SetupReference parser, bibliography output, and dependency boundary."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from _contract import ROOT, compact, normalized, require_for, require_single_a4_page

require = require_for("Reference contract")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()

    stem = args.build_dir / "reference-contract"
    log = stem.with_suffix(".log").read_text(errors="replace")
    text = stem.with_suffix(".txt").read_text(errors="replace")
    pdfinfo = stem.with_suffix(".pdfinfo").read_text(errors="replace")
    source_path = ROOT / "thesis/template/command/cmd-bibliography.tex"
    source = source_path.read_text(errors="replace")

    require(
        r"\NCKUPrivateSetReferenceKeys{#1}" in source,
        "public SetupReference bypasses the private parser seam",
    )
    require(
        r"\keys_define:nn { ncku / setup-reference }" in source,
        "reference parser is not defined through l3keys",
    )
    require(
        source.count(r".tl_set_e:N") == 2,
        "reference parser does not use exactly two expanded tl properties",
    )
    require(
        r"\keys_set:nn { ncku / setup-reference } { #1 }" in source,
        "reference private seam does not apply the l3keys family",
    )
    require(
        r"/SetupReference/.is family" not in source,
        "legacy SetupReference pgfkeys family remains active",
    )
    active_sources = [
        path
        for path in (ROOT / "thesis").rglob("*")
        if path.is_file() and path.suffix in {".tex", ".sty", ".cls"}
    ]
    require(
        all("l3keys2e" not in path.read_text(errors="replace") for path in active_sources),
        "active thesis source introduced deprecated l3keys2e",
    )

    compact_log = compact(log)
    expected_markers = (
        "NCKU-REFERENCE-INITIAL:References/plain",
        "NCKU-REFERENCE-KEY-DEFAULTS:References/plain",
        "NCKU-REFERENCE-KEY-EXPANDED:ExpandedReferenceTitle/abbrv",
        "NCKU-REFERENCE-KEY-RESET:References/plain",
        "NCKU-REFERENCE-PUBLIC:NCKUContractReferences/plain",
        "NCKU-TEST-PASS:SetupReferenceparserandrenderedbibliographycontract",
    )
    for marker in expected_markers:
        require(marker in compact_log, f"missing state marker: {marker}")

    for warning in (
        "undefined references",
        "undefined citations",
        "Rerun to get (cross-references|outlines) right",
    ):
        require(re.search(warning, log, re.IGNORECASE) is None, f"log contains {warning}")

    require_single_a4_page(require, pdfinfo)
    normalized_text = normalized(text)
    require("NCKU Contract References" in normalized_text, "custom bibliography title is missing")
    require("Google - Homepage" in normalized_text, "expected bibliography entry is missing")

    print("Reference contract PASS: defaults, expansion, reset, public title/style, BibTeX output, no l3keys2e")


if __name__ == "__main__":
    main()
