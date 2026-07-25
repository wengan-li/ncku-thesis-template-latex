#!/usr/bin/env python3
"""Require hard errors for top-level and nested multi-figure unknown keys."""
from __future__ import annotations
import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()
    build_dir = args.build_dir.resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    source_dir = ROOT / "thesis"

    def check_level(level: str) -> str | None:
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
            return f"{level} compiled"
        log = (build_dir / f"{job}.log").read_text(errors="replace")
        if "unsupported" not in log or "NCKU-TEST-FAIL" in log:
            return f"{level} diagnostic"
        return None

    with ThreadPoolExecutor(max_workers=2) as pool:
        failures = [message for message in pool.map(check_level, ("top", "sub")) if message]
    if failures:
        raise SystemExit("Multi-figure unknown-key FAIL: " + "; ".join(failures))
    print("Multi-figure unknown-key PASS: 2/2 deterministic hard errors")


if __name__ == "__main__":
    main()
