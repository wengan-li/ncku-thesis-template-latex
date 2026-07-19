#!/usr/bin/env python3
"""Require hard errors for top-level and nested multi-figure unknown keys."""
from __future__ import annotations
import argparse
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()
    build_dir = args.build_dir.resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    source_dir = Path("thesis").resolve()
    for level in ("top", "sub"):
        job = f"multi-figure-key-unknown-{level}"
        for old in build_dir.glob(f"{job}.*"):
            old.unlink()
        tex_input = (
            rf"\def\NCKUTestMultiParser{{{level}}}"
            r"\input{../tests/402-multi-figure-key-unknown.tex}"
        )
        result = subprocess.run(
            ("xelatex", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={build_dir}", f"-jobname={job}", tex_input),
            cwd=source_dir, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode == 0:
            raise SystemExit(f"Multi-figure unknown-key FAIL: {level} compiled")
        log = (build_dir / f"{job}.log").read_text(errors="replace")
        if "unsupported" not in log or "NCKU-TEST-FAIL" in log:
            raise SystemExit(f"Multi-figure unknown-key FAIL: {level} diagnostic")
    print("Multi-figure unknown-key PASS: 2/2 deterministic hard errors")


if __name__ == "__main__":
    main()
