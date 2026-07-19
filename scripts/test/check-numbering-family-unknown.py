#!/usr/bin/env python3
"""Require unknown-key hard errors for every remaining numbering family."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

FAMILIES = (
    "SetupTitleNumberFormatString",
    "STitleNumberFormat",
    "SSTitleNumberFormat",
    "SSSTitleNumberFormat",
    "AppendixCTitleNumberFormat",
    "AppendixSTitleNumberFormat",
    "AppendixSSTitleNumberFormat",
    "AppendixSSSTitleNumberFormat",
    "SetupGeneralAppendixNumberFormatString",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()
    build_dir = args.build_dir.resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    source_dir = Path("thesis").resolve()

    for family in FAMILIES:
        job = f"numbering-family-key-unknown-{family}"
        for old in build_dir.glob(f"{job}.*"):
            old.unlink()
        tex_input = (
            rf"\def\NCKUTestFamily{{{family}}}"
            r"\input{../tests/202-numbering-family-key-unknown.tex}"
        )
        result = subprocess.run(
            (
                "xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                f"-jobname={job}",
                tex_input,
            ),
            cwd=source_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode == 0:
            raise SystemExit(
                f"Numbering family unknown-key FAIL: {family} unexpectedly compiled"
            )
        log = (build_dir / f"{job}.log").read_text(errors="replace")
        if "unsupported" not in log:
            raise SystemExit(
                f"Numbering family unknown-key FAIL: {family} missing unsupported diagnostic"
            )
        if "NCKU-TEST-FAIL" in log:
            raise SystemExit(
                f"Numbering family unknown-key FAIL: {family} reached failure marker"
            )

    print(
        "Numbering family unknown-key PASS: 9/9 deterministic hard errors"
    )


if __name__ == "__main__":
    main()
