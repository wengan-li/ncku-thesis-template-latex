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
    source = Path("thesis/template/command/cmd-theorem.tex").read_text(errors="replace")

    require(
        r"\keys_define:nn { ncku / insert-theorem }" in source,
        "theorem-content parser is not defined through l3keys",
    )
    require(
        source.count(r".tl_set_e:N") == 2,
        "theorem-content parser does not use exactly two expanded tl properties",
    )
    require(
        r"/InsertTheoremOptions/.is family" not in source,
        "legacy theorem-content pgfkeys family remains active",
    )
    require(
        r"\NCKUPrivateSetInsertTheoremKeys{#1}" in source,
        "theorem-content insertion bypasses the private parser",
    )
    require(
        r"/Theorem#1Format/.is family" in source,
        "dynamic theorem-format pgfkeys registry was changed by this slice",
    )

    require(
        "NCKU-TEST-PASS: all 21 public theorem insertion helpers compiled" in log,
        "missing theorem pass marker",
    )
    compact_log = "".join(log.split())
    for marker in (
        "NCKU-THEOREM-KEY-DEFAULTS:/",
        "NCKU-THEOREM-KEY-EXPANDED:ExpandedTheoremTitle/ncku:theorem-expanded",
        "NCKU-THEOREM-KEY-RESET:/",
    ):
        require(marker in compact_log, f"missing theorem key-state marker: {marker}")

    theorem_types = (
        "Definition",
        "Condition",
        "Problem",
        "Example",
        "Theorem",
        "Lemma",
        "Corollary",
        "Proposition",
        "Conjecture",
        "Proof",
        "Note",
        "Annotation",
        "Claim",
        "Case",
        "Acknowledgment",
        "Conclusion",
        "Criterion",
        "Assertion",
        "Question",
        "Hypothesis",
        "Summary",
    )
    numbered_types = {
        "Definition",
        "Condition",
        "Problem",
        "Example",
        "Theorem",
        "Lemma",
        "Corollary",
        "Proposition",
        "Conjecture",
        "Criterion",
        "Assertion",
        "Question",
        "Hypothesis",
    }
    require(log.count("NCKU-TEST-DEFAULT-") == len(theorem_types), "unexpected default metadata count")
    for theorem_type in theorem_types:
        follow = "section" if theorem_type in numbered_types else ""
        marker = f"NCKU-TEST-DEFAULT-{theorem_type}: Env{theorem_type}/{theorem_type}/{follow}"
        require(marker in log, f"missing default metadata marker: {theorem_type}")

    require(log.count("NCKU-TEST-ROUTE-") == len(theorem_types), "unexpected setter route count")
    for theorem_type in theorem_types:
        marker = f"NCKU-TEST-ROUTE-{theorem_type}: Registry{theorem_type}"
        require(marker in log, f"missing setter route marker: {theorem_type}")
    require("NCKU-TEST-UNKNOWN-ROUTE: no-op" in log, "unknown theorem type is not a no-op")
    require("NCKU-TEST-EMPTY-ROUTE: no-op" in log, "empty theorem type is not a no-op")
    require("NCKU-TEST-UNKNOWN-ROUTE: FAIL" not in log, "unknown theorem type created state")
    require("NCKU-TEST-EMPTY-ROUTE: FAIL" not in log, "empty theorem type created state")

    require(
        log.count("NCKU-TEST-COUNTER-ROUTE-") == len(theorem_types) + 1,
        "unexpected counter target route count",
    )
    for theorem_type in theorem_types:
        follow = "section" if theorem_type in numbered_types else ""
        source = theorem_type if theorem_type == "Definition" else "Definition"
        marker = f"NCKU-TEST-COUNTER-ROUTE-{theorem_type}: {source}/{follow}"
        require(marker in log, f"missing counter target route: {theorem_type}")
    require(
        "NCKU-TEST-COUNTER-ROUTE-Section: Definition/section" in log,
        "Section counter target did not normalize",
    )
    require("NCKU-TEST-COUNTER-UNKNOWN: Section" in log, "unknown counter target is not a no-op")
    require("NCKU-TEST-COUNTER-EMPTY: Section" in log, "empty counter target is not a no-op")
    require("NCKU-TEST-COUNTER-CHAIN: " in log, "multi-hop empty counter chain did not resolve")

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

    print(
        f"Theorem contract PASS: {len(theorem_types)} defaults/insertion/setter/counter routes, "
        f"{len(labels)} labels, self/unknown/empty, multi-hop, title/ref/nameref, section reset, proof marker"
    )


if __name__ == "__main__":
    main()
