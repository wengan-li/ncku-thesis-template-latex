#!/usr/bin/env python3
"""Verify expansion, reset, and omission for remaining numbering families."""
from __future__ import annotations
import argparse
from pathlib import Path

# (family, expanded key count, OMITTED-state field values). The EXPANDED row
# is always `<family>-X` repeated per key, and the PARTIAL row is the OMITTED
# row with its first field replaced by the literal `PARTIAL`.
FAMILIES = (
    ("SetupTitleNumberFormatString", 14, "|" * 13),
    ("STitleNumberFormat", 7, "||Left|Arabic|Arabic|.|."),
    ("SSTitleNumberFormat", 9, "||Left|Arabic|Arabic|Arabic|.|.|."),
    ("SSSTitleNumberFormat", 11, "||Left|Arabic|Arabic|Arabic|Arabic|.|.|.|."),
    ("AppendixCTitleNumberFormat", 5, "Appendix||Left|UpperAlph|."),
    ("AppendixSTitleNumberFormat", 7, "||Left|UpperAlph|Arabic|.|."),
    ("AppendixSSTitleNumberFormat", 9, "||Left|UpperAlph|Arabic|Arabic|.|.|."),
    ("AppendixSSSTitleNumberFormat", 11, "||Left|UpperAlph|Arabic|Arabic|Arabic|.|.|.|."),
    ("SetupGeneralAppendixNumberFormatString", 20, "|" * 12 + "|.|||.|||."),
)


def family_markers(family: str, key_count: int, omitted: str) -> tuple[str, str, str]:
    prefix = f"NCKU-NUMBERING-FAMILY-{family.upper()}"
    partial = "PARTIAL|" + omitted.split("|", 1)[1]
    return (
        f"{prefix}-EXPANDED:" + "|".join([f"{family}-X"] * key_count),
        f"{prefix}-PARTIAL:{partial}",
        f"{prefix}-OMITTED:{omitted}",
    )


EXPECTED = tuple(
    marker
    for family, key_count, omitted in FAMILIES
    for marker in family_markers(family, key_count, omitted)
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()
    log = (args.build_dir / "numbering-family-contract.log").read_text(errors="replace")
    compact = "".join(log.split())
    if log.count("NCKU-NUMBERING-FAMILY-") != len(EXPECTED):
        raise SystemExit("Numbering family contract FAIL: unexpected marker count")
    for marker in EXPECTED:
        if marker not in compact:
            raise SystemExit(f"Numbering family contract FAIL: {marker}")
    if "NCKU-TEST-PASS:remainingnumberingfamilyparsercontract" not in compact:
        raise SystemExit("Numbering family contract FAIL: missing pass marker")
    print("Numbering family contract PASS: 9 families, expanded/partial/omitted")

if __name__ == "__main__":
    main()
