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
        "NCKU-CHAPTER-PARSER-EXPANDED:Macro[|]|Center|UpperRoman|:",
        "NCKU-CHAPTER-PARSER-PARTIAL:Chapter|!|Left|Arabic|.",
        "NCKU-CHAPTER-PARSER-OMITTED:Chapter||Left|Arabic|.",
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
    require(log.count("NCKU-NUMBERING-") == len(markers) - 3, "unexpected numbering marker count")
    require(log.count("NCKU-CHAPTER-PARSER-") == 3, "unexpected Chapter parser marker count")
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
        r"\cs_new_protected:Npn \NCKUPrivateSetChapterTitleFormatKeys #1" in source,
        "Chapter title-format private seam is missing",
    )
    require(
        source.count(r"\NCKUPrivateSetChapterTitleFormatKeys{#2}") == 1,
        "Chapter selector does not route through the private seam exactly once",
    )
    require(
        r"\keys_define:nn { ncku / chapter-title-format }" in source,
        "Chapter title-format l3keys family is missing",
    )
    chapter_block_match = re.search(
        r"\\keys_define:nn \{ ncku / chapter-title-format \}(.*?)\\cs_new_protected:Npn \\ncku_chapter_title_format_set_keys:n",
        source,
        re.DOTALL,
    )
    require(chapter_block_match is not None, "cannot isolate Chapter title-format l3keys block")
    if chapter_block_match is None:
        raise SystemExit("Numbering contract FAIL: cannot isolate Chapter title-format l3keys block")
    require(
        chapter_block_match.group(1).count(".tl_set_e:N") == 5,
        "Chapter parser must preserve expanded storage for exactly five keys",
    )
    require(
        r"/CTitleNumberFormat/.is family" not in source,
        "legacy Chapter title-format pgfkeys family remains after migration",
    )
    require(
        r"\appto\GetAppendixEquationNumberFormatString{}" not in source,
        "appendix equation initializer still appends instead of resetting",
    )
    require(
        re.search(r"\\appto#3\{\\TmpValue", source) is None,
        "numbering output retains mutable pgf scratch value",
    )
    require(
        source.count(r"\begin{comment}") == 0,
        "runtime-dead numbering comment blocks reappeared",
    )
    dispatcher = source.split(r"\newcommand\AppendCounterStringToFormatString", 1)[1].split(
        r"\newcommand\SetupTitleNumberFormatString", 1
    )[0]
    require(r"\str_case_e:nn" in dispatcher, "counter-style dispatch is not an expl3 string case")
    require(r"\ifthenelse" not in dispatcher, "counter-style dispatch regained sequential ifthen tests")
    for style in (
        "ChiNum",
        "Tiangan",
        "Arabic",
        "LowerRoman",
        "UpperRoman",
        "LowerAlph",
        "UpperAlph",
    ):
        require(dispatcher.count(f"{{{style}}}") == 1, f"counter-style case changed: {style}")

    print(
        "Numbering contract PASS: default/custom general+appendix titles/getters, "
        "dynamic counters, 7-style expl3 dispatch, F/T/E idempotence, "
        "unknown/empty no-op, A4 single page"
    )


if __name__ == "__main__":
    main()
