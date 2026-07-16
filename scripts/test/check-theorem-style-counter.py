#!/usr/bin/env python3
"""Verify custom theorem environment, counter, and style behavior."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from xml.etree import ElementTree


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Theorem style/counter matrix FAIL: {message}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()

    stem = args.build_dir / "theorem-style-counter"
    log = stem.with_suffix(".log").read_text(errors="replace")
    text = stem.with_suffix(".txt").read_text(errors="replace")
    pdfinfo = stem.with_suffix(".pdfinfo").read_text(errors="replace")
    xml_path = stem.with_suffix(".xml")

    numbered_plain = (
        "Theorem",
        "Lemma",
        "Corollary",
        "Proposition",
        "Conjecture",
        "Criterion",
        "Assertion",
    )
    numbered_definition = (
        "Definition",
        "Condition",
        "Problem",
        "Example",
        "Question",
        "Hypothesis",
    )
    unnumbered_definition = (
        "Proof",
        "Note",
        "Annotation",
        "Claim",
        "Case",
        "Acknowledgment",
        "Conclusion",
        "Summary",
    )
    theorem_types = numbered_plain + numbered_definition + unnumbered_definition

    require(log.count("NCKU-TEST-MATRIX-") == len(theorem_types), "unexpected matrix marker count")
    for theorem_type in theorem_types:
        follow = "section" if theorem_type == "Condition" else ""
        marker = f"NCKU-TEST-MATRIX-{theorem_type}: EnvMatrix{theorem_type}/Matrix {theorem_type}/{follow}"
        require(marker in log, f"missing or incorrect matrix marker: {theorem_type}")
    require(
        "NCKU-TEST-PASS: custom theorem style/counter matrix compiled" in log,
        "missing pass marker",
    )

    forbidden_warnings = (
        "undefined references",
        "Rerun to get (cross-references|outlines) right",
        "destination with the same identifier",
        "Token not allowed in a PDF string",
        "No counter .* defined",
    )
    for warning in forbidden_warnings:
        require(re.search(warning, log, re.IGNORECASE) is None, f"log contains {warning}")

    require(re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None, "PDF is not exactly one page")
    require(re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None, "PDF is not A4")

    expected_first = {
        "Definition": "1",
        "Theorem": "1",
        "Condition": "I.1",
        "Problem": "1",
        "Example": "1",
        "Lemma": "1",
        "Corollary": "1",
        "Proposition": "1",
        "Conjecture": "1",
        "Criterion": "1",
        "Assertion": "1",
        "Question": "1",
        "Hypothesis": "1",
    }
    normalized_text = " ".join(text.split())
    for theorem_type, number in expected_first.items():
        fragment = f"Matrix {theorem_type} {number}. MATRIX{theorem_type.upper()}BODYONE"
        require(fragment in normalized_text, f"missing numbered output: {fragment}")
    for theorem_type in unnumbered_definition:
        fragment = f"Matrix {theorem_type}. MATRIX{theorem_type.upper()}BODYONE"
        require(fragment in normalized_text, f"missing unnumbered output: {fragment}")
    for fragment in (
        "Matrix Definition 2. MATRIXDEFINITIONBODYTWO",
        "Matrix Theorem 2. MATRIXTHEOREMBODYTWO",
        "Matrix Condition II.1. MATRIXCONDITIONBODYTWO",
    ):
        require(fragment in normalized_text, f"missing second-section output: {fragment}")
    require("MATRIXPROOFBODYONE ■" in normalized_text, "proof marker is missing")

    root = ElementTree.parse(xml_path).getroot()
    styled: dict[str, bool] = {}
    for element in root.iter("text"):
        value = "".join(element.itertext())
        match = re.search(r"MATRIX([A-Z]+)BODY(?:ONE|TWO)", value)
        if match:
            styled[match.group(0)] = any(child.tag == "i" for child in element.iter())

    for theorem_type in numbered_plain:
        marker = f"MATRIX{theorem_type.upper()}BODYONE"
        require(marker in styled, f"missing XML style token: {marker}")
        require(styled[marker], f"plain theorem body is not italic: {theorem_type}")
    for theorem_type in numbered_definition + unnumbered_definition:
        marker = f"MATRIX{theorem_type.upper()}BODYONE"
        require(marker in styled, f"missing XML style token: {marker}")
        require(not styled[marker], f"definition theorem body became italic: {theorem_type}")

    print(
        "Theorem style/counter matrix PASS: 21 custom environments, "
        "plain/definition styles, global/scoped/chained-empty counters"
    )


if __name__ == "__main__":
    main()
