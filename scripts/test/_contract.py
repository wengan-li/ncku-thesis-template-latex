"""Shared helpers for the fixture contract checkers.

Each checker binds ``require = require_for("<label>")`` so failure messages
keep their per-checker prefix while the assertion mechanics live here.
Warning allowlists intentionally stay in each checker: which log patterns a
fixture rejects is per-contract policy, not shared mechanics.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]

Require = Callable[[bool, str], None]


def require_for(prefix: str) -> Require:
    def require(condition: bool, message: str) -> None:
        if not condition:
            raise SystemExit(f"{prefix} FAIL: {message}")

    return require


def compact(text: str) -> str:
    """Remove all whitespace (log lines wrap at arbitrary columns)."""

    return "".join(text.split())


def normalized(text: str) -> str:
    """Collapse all whitespace runs to single spaces."""

    return " ".join(text.split())


def require_single_a4_page(require: Require, pdfinfo: str) -> None:
    require(
        re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None,
        "PDF is not exactly one page",
    )
    require(
        re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None,
        "PDF is not A4",
    )


def l3keys_block(source: str, keys_path: str, setter: str) -> str | None:
    """Return the text between an l3keys family definition and its setter.

    ``keys_path`` is the literal key tree ("ncku / font-options"); ``setter``
    is the ``\\cs_new_protected:Npn`` function name that follows the block.
    Returns None when the boundaries cannot be found.
    """

    match = re.search(
        rf"\\keys_define:nn \{{ {re.escape(keys_path)} \}}"
        rf"(.*?)\\cs_new_protected:Npn \\{re.escape(setter)}",
        source,
        re.DOTALL,
    )
    return None if match is None else match.group(1)
