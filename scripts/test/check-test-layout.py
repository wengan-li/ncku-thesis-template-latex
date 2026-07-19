#!/usr/bin/env python3
"""Validate the flat, numerically grouped tests/ source inventory."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAME = re.compile(r"^(\d{3})-[a-z0-9][a-z0-9.-]*$")
EXPECTED_ANCHORS = {
    "000-test-suite.md",
    "100-v1-public-api.json",
    "102-v1-project-migration.json",
    "900-reference-fixtures.md",
    "910-reference-ieeetran.tex",
    "920-reference-page-orientation-lscape.tex",
    "921-reference-page-orientation-pdflscape.tex",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def tracked_test_paths() -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z", "--", "tests"], cwd=ROOT
    )
    return [item.decode("utf-8") for item in output.split(b"\0") if item]


def main() -> int:
    try:
        paths = tracked_test_paths()
        if not paths:
            fail("tests/ has no tracked files")

        names: list[str] = []
        numbers: list[int] = []
        for relative in paths:
            parts = Path(relative).parts
            if len(parts) != 2 or parts[0] != "tests":
                fail(f"test inventory must be flat: {relative}")
            name = parts[1]
            match = NAME.fullmatch(name)
            if not match:
                fail(f"test filename is not numerically prefixed: {relative}")
            assert match is not None
            names.append(name)
            numbers.append(int(match.group(1)))

        duplicates = sorted(number for number, count in Counter(numbers).items() if count > 1)
        if duplicates:
            fail("duplicate test numbers: " + ", ".join(f"{number:03d}" for number in duplicates))

        missing = sorted(EXPECTED_ANCHORS.difference(names))
        if missing:
            fail("missing required test-layout anchors: " + ", ".join(missing))

        groups = Counter(number // 100 for number in numbers)
        absent_groups = [group for group in range(10) if groups[group] == 0]
        if absent_groups:
            fail("empty reserved test groups: " + ", ".join(str(group) for group in absent_groups))

    except (AssertionError, subprocess.CalledProcessError) as error:
        print(f"Test layout FAIL: {error}", file=sys.stderr)
        return 1

    group_text = ", ".join(
        f"{group}xx={groups[group]}" for group in sorted(groups)
    )
    print(f"Test layout PASS: {len(paths)} flat numbered files ({group_text})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
