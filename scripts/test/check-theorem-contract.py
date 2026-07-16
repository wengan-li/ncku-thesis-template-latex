#!/usr/bin/env python3
"""Verify the focused theorem helper PDF, labels, and references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Theorem contract FAIL: {message}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()

    stem = args.build_dir / "theorem-contract"
    log = stem.with_suffix(".log").read_text(errors="replace")
    aux = stem.with_suffix(".aux").read_text(errors="replace")
    text = stem.with_suffix(".txt").read_text(errors="replace")
    pdfinfo = stem.with_suffix(".pdfinfo").read_text(errors="replace")

    markers = (
        "NCKU-TEST-THEOREM-DEFAULT: EnvTheorem/Theorem/section",
        "NCKU-TEST-DEFINITION-DEFAULT: EnvDefinition/Definition/section",
        "NCKU-TEST-PROOF-DEFAULT: EnvProof/Proof/",
        "NCKU-TEST-PASS: all 21 public theorem insertion helpers compiled",
    )
    for marker in markers:
        require(marker in log, f"missing log marker: {marker}")

    forbidden_warnings = (
        "undefined references",
        "Rerun to get (cross-references|outlines) right",
        "destination with the same identifier",
        "Token not allowed in a PDF string",
    )
    for warning in forbidden_warnings:
        require(re.search(warning, log, re.IGNORECASE) is None, f"log contains {warning}")

    require(re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None, "PDF is not exactly one page")
    require(re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None, "PDF is not A4")

    expected_text = (
        "Definition I.1. NCKU Definition Body.",
        "Condition I.1. NCKU Condition Body.",
        "Problem I.1. NCKU Problem Body.",
        "Example I.1. NCKU Example Body.",
        "Theorem I.1 (Named Theorem). NCKU Theorem Body One.",
        "Lemma I.1. NCKU Lemma Body.",
        "Corollary I.1. NCKU Corollary Body.",
        "Proposition I.1. NCKU Proposition Body.",
        "Conjecture I.1. NCKU Conjecture Body.",
        "Criterion I.1. NCKU Criterion Body.",
        "Assertion I.1. NCKU Assertion Body.",
        "Question I.1. NCKU Question Body.",
        "Hypothesis I.1. NCKU Hypothesis Body.",
        "Theorem I.2. NCKU Theorem Body Two.",
        "Proof. NCKU Proof Body. ■",
        "Note. NCKU Note Body.",
        "Annotation. NCKU Annotation Body.",
        "Claim. NCKU Claim Body.",
        "Case. NCKU Case Body.",
        "Acknowledgment. NCKU Acknowledgment Body.",
        "Conclusion. NCKU Conclusion Body.",
        "Summary. NCKU Summary Body.",
        "Theorem II.1. NCKU Theorem Reset Body.",
        "References: I.1, I.1, I.2, II.1. Named reference: Named Theorem.",
    )
    normalized_text = " ".join(text.split())
    for fragment in expected_text:
        require(" ".join(fragment.split()) in normalized_text, f"missing PDF text: {fragment}")
    require("ncku:test:" not in text, "label key leaked into visible PDF text")

    labels = {
        "definition": "I.1",
        "condition": "I.1",
        "problem": "I.1",
        "example": "I.1",
        "theorem-first": "I.1",
        "lemma": "I.1",
        "corollary": "I.1",
        "proposition": "I.1",
        "conjecture": "I.1",
        "criterion": "I.1",
        "assertion": "I.1",
        "question": "I.1",
        "hypothesis": "I.1",
        "theorem-second": "I.2",
        "theorem-reset": "II.1",
    }
    require(aux.count(r"\newlabel{ncku:test:") == len(labels), "unexpected theorem label count")
    for name, value in labels.items():
        pattern = rf"\\newlabel\{{ncku:test:{re.escape(name)}\}}\{{\{{{re.escape(value)}\}}"
        require(re.search(pattern, aux) is not None, f"label {name} is not {value}")
    require(
        r"\newlabel{ncku:test:theorem-first}{{I.1}{i}{Named Theorem}" in aux,
        "titled theorem did not freeze nameref metadata",
    )

    print(f"Theorem contract PASS: 21 insertion helpers, {len(labels)} labels, title/ref/nameref, section reset, proof marker")


if __name__ == "__main__":
    main()
