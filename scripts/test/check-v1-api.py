#!/usr/bin/env python3
"""Capture and verify the v1 public TeX command compatibility surface.

The v2.x line intentionally preserves every explicitly declared v1 command and
environment.  The baseline is generated once before the v2 refactor.  Normal
checks only read the committed baseline and fail when a name or argument shape
disappears.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import cast

ApiEntry = dict[str, list[str]]

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = ROOT / "thesis" / "template"
BASELINE = ROOT / "tests" / "v1-public-api.json"

LATEX_COMMAND = re.compile(
    r"\\(?P<kind>newcommand|renewcommand|providecommand)\*?"
    r"\s*(?:\{\s*)?\\(?P<name>[A-Za-z@]+)(?:\s*\})?"
    r"\s*(?:\[(?P<arity>\d+)\])?"
)
XPARSE_COMMAND = re.compile(
    r"\\(?P<kind>DeclareDocumentCommand|NewDocumentCommand|"
    r"RenewDocumentCommand|ProvideDocumentCommand)"
    r"\s*\{\s*\\(?P<name>[A-Za-z@]+)\s*\}"
    r"\s*\{(?P<spec>[^}]*)\}"
)
LATEX_ENVIRONMENT = re.compile(
    r"\\(?P<kind>newenvironment|renewenvironment)\*?"
    r"\s*\{(?P<name>[^}]+)\}"
    r"\s*(?:\[(?P<arity>\d+)\])?"
)
XPARSE_ENVIRONMENT = re.compile(
    r"\\(?P<kind>NewDocumentEnvironment|RenewDocumentEnvironment|"
    r"DeclareDocumentEnvironment|ProvideDocumentEnvironment)"
    r"\s*\{(?P<name>[^}]+)\}"
    r"\s*\{(?P<spec>[^}]*)\}"
)


def strip_comments(text: str) -> str:
    cleaned: list[str] = []
    for line in text.splitlines():
        match = re.search(r"(?<!\\)%", line)
        cleaned.append(line[: match.start()] if match else line)
    return "\n".join(cleaned)


def normalize_spec(spec: str) -> str:
    return " ".join(spec.split())


def collect_api() -> dict[str, ApiEntry]:
    entries: dict[str, ApiEntry] = {}
    definitions: dict[str, set[tuple[str, str]]] = defaultdict(set)

    for path in sorted(TEMPLATE_ROOT.rglob("*.tex")):
        relative = path.relative_to(ROOT).as_posix()
        text = strip_comments(path.read_text(encoding="utf-8"))

        for match in LATEX_COMMAND.finditer(text):
            name = match.group("name")
            signature = f"latex:{int(match.group('arity') or 0)}"
            definitions[name].add((signature, relative))

        for match in XPARSE_COMMAND.finditer(text):
            name = match.group("name")
            signature = f"xparse:{normalize_spec(match.group('spec'))}"
            definitions[name].add((signature, relative))

        for match in LATEX_ENVIRONMENT.finditer(text):
            name = f"environment:{match.group('name').strip()}"
            signature = f"latex:{int(match.group('arity') or 0)}"
            definitions[name].add((signature, relative))

        for match in XPARSE_ENVIRONMENT.finditer(text):
            name = f"environment:{match.group('name').strip()}"
            signature = f"xparse:{normalize_spec(match.group('spec'))}"
            definitions[name].add((signature, relative))

    for name in sorted(definitions):
        values = sorted(definitions[name])
        entries[name] = {
            "signatures": sorted({signature for signature, _ in values}),
            "defined_in": sorted({path for _, path in values}),
        }
    return entries


def write_baseline() -> int:
    api = collect_api()
    payload = {
        "schema": 1,
        "policy": (
            "Every explicitly declared v1 command and environment remains "
            "available with a compatible argument shape throughout v2.x."
        ),
        "entries": api,
    }
    BASELINE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(api)} v1 API entries to {BASELINE.relative_to(ROOT)}")
    return 0


def check_baseline() -> int:
    if not BASELINE.exists():
        raise SystemExit(
            f"Missing {BASELINE.relative_to(ROOT)}; generate it before v2 changes"
        )

    baseline = cast(
        dict[str, ApiEntry],
        json.loads(BASELINE.read_text(encoding="utf-8"))["entries"],
    )
    current = collect_api()
    missing: list[str] = []
    incompatible: list[str] = []

    for name, expected in baseline.items():
        if name not in current:
            missing.append(name)
            continue
        expected_signatures = set(expected["signatures"])
        current_signatures = set(current[name]["signatures"])
        if not expected_signatures.issubset(current_signatures):
            incompatible.append(
                f"{name}: expected {sorted(expected_signatures)}, "
                f"found {sorted(current_signatures)}"
            )

    if missing or incompatible:
        if missing:
            print("Missing v1 API entries:")
            for name in missing:
                print(f"  - {name}")
        if incompatible:
            print("Incompatible v1 API signatures:")
            for message in incompatible:
                print(f"  - {message}")
        return 1

    added = sorted(set(current) - set(baseline))
    print(
        f"V1 API compatibility PASS: {len(baseline)} preserved; "
        f"{len(added)} v2 additions"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="write the one-time v1 API baseline before v2 implementation",
    )
    args = parser.parse_args()
    return write_baseline() if args.write_baseline else check_baseline()


if __name__ == "__main__":
    raise SystemExit(main())
