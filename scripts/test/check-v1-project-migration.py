#!/usr/bin/env python3
"""Verify the unchanged v1.8.2 student-project inputs used by v2.

The committed manifest is generated from the immutable v1.8.2 release tag.  It
covers student-owned configuration, content, bibliography, oral-certificate
assets, and the root thesis entry point.  This source-integrity gate is paired
with two runtime checks: the unchanged canonical entry/configuration build and
a StudentMode build that asserts its active content and bibliography inputs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tests" / "v1-project-migration.json"

ManifestEntry = dict[str, object]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if not MANIFEST.is_file():
        raise SystemExit(f"Missing migration manifest: {MANIFEST.relative_to(ROOT)}")

    payload = cast(dict[str, object], json.loads(MANIFEST.read_text(encoding="utf-8")))
    if payload.get("schema") != 1:
        raise SystemExit(f"Unsupported migration manifest schema: {payload.get('schema')!r}")

    source = cast(dict[str, str], payload.get("source"))
    entries = cast(dict[str, ManifestEntry], payload.get("entries"))
    if not source or not entries:
        raise SystemExit("Migration manifest must define source provenance and entries")

    failures: list[str] = []
    total_bytes = 0

    for relative, expected in sorted(entries.items()):
        relative_path = Path(relative)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            failures.append(f"unsafe manifest path: {relative}")
            continue

        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing: {relative}")
            continue

        expected_size = int(cast(int, expected["size"]))
        expected_sha256 = str(expected["sha256"])
        actual_size = path.stat().st_size
        actual_sha256 = file_sha256(path)
        total_bytes += actual_size

        if actual_size != expected_size:
            failures.append(
                f"size mismatch: {relative}: expected {expected_size}, found {actual_size}"
            )
        if actual_sha256 != expected_sha256:
            failures.append(
                f"SHA-256 mismatch: {relative}: expected {expected_sha256}, "
                f"found {actual_sha256}"
            )

    if failures:
        print("V1 project migration source FAIL:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(
        "V1 project migration source PASS: "
        f"{len(entries)} unchanged files ({total_bytes} bytes) from "
        f"{source['tag']} at {source['commit']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
