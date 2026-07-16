#!/usr/bin/env python3
"""Verify general/appendix numbering state, selectors, and repeatability."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Numbering contract FAIL: {message}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()

    stem = args.build_dir / "numbering-contract"
    log = stem.with_suffix(".log").read_text(errors="replace")
    text = stem.with_suffix(".txt").read_text(errors="replace")
    pdfinfo = stem.with_suffix(".pdfinfo").read_text(errors="replace")
    compact_log = "".join(log.split())
    normalized_text = " ".join(text.split())

    markers = (
        "NCKU-NUMBERING-DEFAULT-GENERAL:Chapter2/2.3/2.3.4//2.3.4.5",
        "NCKU-NUMBERING-DEFAULT-APPENDIX:AppendixB/B.3/B.3.4//B.3.4.5",
        "NCKU-NUMBERING-DEFAULT-GENERAL-GETTERS:2/2.3/2.3.4/",
        "NCKU-NUMBERING-DEFAULT-APPENDIX-GETTERS:B/B.3/B.3.4/",
        "NCKU-NUMBERING-GENERAL-FTE:2.6/2.7/2.8",
        "NCKU-NUMBERING-APPENDIX-FTE-FIRST:2.6/2.7/2.8",
        "NCKU-NUMBERING-APPENDIX-FTE-SECOND:2.6/2.7/2.8",
        "NCKU-NUMBERING-STYLES:四/丁/4/iv/IV/d/D/",
        "NCKU-NUMBERING-DYNAMIC-GENERAL:Chapter4/4.3/4.3.2/4/4.3/4.3.2",
        "NCKU-NUMBERING-DYNAMIC-APPENDIX:AppendixC/C.4/C.4.2/C/C.4/C.4.2",
        "NCKU-NUMBERING-CUSTOM-GENERAL:GC[4]/GS[4-3]/GSS[4-3-2]/GSSS[4-3-2-1]",
        "NCKU-NUMBERING-CUSTOM-APPENDIX:AC[B]/AS[B-3]/ASS[B-3-2]/ASSS[B-3-2-1]",
        "NCKU-NUMBERING-NOOP-SELECTOR:GC[",
    )
    require(log.count("NCKU-NUMBERING-") == len(markers), "unexpected marker count")
    for marker in markers:
        require(marker in compact_log, f"missing or incorrect marker: {marker}")
    require(
        "NCKU-TEST-PASS:focusednumberingcontractcompiled" in compact_log,
        "missing pass marker",
    )

    forbidden = (
        r"undefined references",
        r"Rerun to get (cross-references|outlines) right",
        r"Undefined control sequence",
        r"destination with the same identifier",
        r"Token not allowed in a PDF string",
        r"Overfull \\hbox",
        r"Underfull \\hbox",
    )
    for warning in forbidden:
        require(re.search(warning, log, re.IGNORECASE) is None, f"log contains {warning}")

    require(re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None, "PDF is not one page")
    require(re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None, "PDF is not A4")

    visible = (
        "Default general: Chapter 2/ 2.3/ 2.3.4/ / 2.3.4.5.",
        "Default appendix: Appendix B/ B.3/ B.3.4/ / B.3.4.5.",
        "General F/T/E: 2.6/2.7/2.8.",
        "Appendix F/T/E first: 2.6/2.7/2.8.",
        "Appendix F/T/E second: 2.6/2.7/2.8.",
        "Styles: 四, 丁, 4, iv, IV, d, D, empty=[].",
        "Dynamic general: Chapter 4/ 4.3/ 4.3.2/ 4/ 4.3/ 4.3.2.",
        "Dynamic appendix: Appendix C/ C.4/ C.4.2/ C/ C.4/ C.4.2.",
        "Custom general: GC[4]/ GS[4-3]/ GSS[4-3-2]/ GSSS[4-3-2-1].",
        "Custom appendix: AC[B]/ AS[B-3]/ ASS[B-3-2]/ ASSS[B-3-2-1].",
        "Unknown/empty selector preserved: GC[.",
    )
    for fragment in visible:
        require(fragment in normalized_text, f"missing visible fragment: {fragment}")

    source = Path("thesis/template/command/cmd-numbering.tex").read_text()
    require(
        r"\appto\GetAppendixEquationNumberFormatString{}" not in source,
        "appendix equation initializer still appends instead of resetting",
    )
    require(
        re.search(r"\\appto#3\{\\TmpValue", source) is None,
        "numbering output retains mutable pgf scratch value",
    )
    require(
        source.count(r"\begin{comment}") == 3,
        "disabled blocks changed before source-manifest boundary was repaired",
    )

    print(
        "Numbering contract PASS: default/custom general+appendix titles/getters, "
        "dynamic counters, 7 styles, F/T/E idempotence, unknown/empty no-op, A4 single page"
    )


if __name__ == "__main__":
    main()
