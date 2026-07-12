#!/usr/bin/env python3
"""Check the final canonical XeLaTeX log against the reviewed warning budget."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


log_path = Path(sys.argv[1] if len(sys.argv) > 1 else "build/thesis.log")
text = log_path.read_text(encoding="utf-8", errors="replace")

forbidden = {
    "undefined references": r"undefined references?",
    "undefined citations": r"undefined citations?",
    "rerun required": r"Rerun to get (?:cross-references|outlines) right",
    "duplicate PDF destinations": r"already defined|destination with the same identifier",
    "hyperref PDF-string token leakage": r"Token not allowed in a PDF string",
}

failures: list[str] = []
for label, pattern in forbidden.items():
    count = len(re.findall(pattern, text, flags=re.IGNORECASE))
    if count:
        failures.append(f"{label}: {count}")

warning_lines = [
    line.strip()
    for line in text.splitlines()
    if re.match(r"^(?:Package \S+ Warning:|LaTeX(?: Font)? Warning:)", line)
]


def classify(line: str) -> str:
    if line.startswith("Package xeCJK Warning: Unknown CJK family"):
        return "xecjk-unknown-family"
    if line.startswith("Package hyperref Warning: Suppressing empty link"):
        return "hyperref-empty-link"
    if line.startswith("LaTeX Font Warning:"):
        return "font-shape"
    if re.match(r"LaTeX Warning: `h' float specifier changed to `ht'", line):
        return "float-placement-adjustment"
    return f"unknown:{line}"


warning_counts = Counter(classify(line) for line in warning_lines)
warning_budget = {
    "xecjk-unknown-family": 0,
    "hyperref-empty-link": 1,
    "font-shape": 2,
    "float-placement-adjustment": 5,
}

for label, count in warning_counts.items():
    maximum = warning_budget.get(label)
    if maximum is None:
        failures.append(f"unreviewed warning class ({count}): {label}")
    elif count > maximum:
        failures.append(f"warning budget exceeded for {label}: {count} > {maximum}")

layout_counts = {
    "underfull-hbox": len(re.findall(r"Underfull \\hbox", text)),
    "overfull-hbox": len(re.findall(r"Overfull \\hbox", text)),
    "underfull-vbox": len(re.findall(r"Underfull \\vbox", text)),
    "overfull-vbox": len(re.findall(r"Overfull \\vbox", text)),
}
layout_budget = {
    "underfull-hbox": 130,
    "overfull-hbox": 21,
    "underfull-vbox": 0,
    "overfull-vbox": 0,
}
for label, count in layout_counts.items():
    maximum = layout_budget[label]
    if count > maximum:
        failures.append(f"layout warning budget exceeded for {label}: {count} > {maximum}")

if failures:
    print(f"Diagnostics check failed for {log_path}:", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    raise SystemExit(1)

print(f"Diagnostics check passed for {log_path}")
for label in sorted(warning_budget):
    print(f"  {label}: {warning_counts.get(label, 0)}/{warning_budget[label]}")
for label in sorted(layout_budget):
    print(f"  {label}: {layout_counts[label]}/{layout_budget[label]}")
