#!/usr/bin/env python3
"""Capture and verify the v1 public TeX compatibility surface.

The v2.x line preserves every supported LaTeX/xparse declaration captured from
the immutable pre-v2 source. Literal ``\\def``-style declarations are audited in
a separate section because dynamically generated definitions require a different
parser and compatibility judgement.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Iterable, cast

ApiEntry = dict[str, list[str]]
SourceText = tuple[str, str]

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = ROOT / "thesis" / "template"
BASELINE = ROOT / "tests" / "100-v1-public-api.json"
COMMENT_ARTIFACTS = ROOT / "tests" / "101-v1-comment-environment-artifacts.json"
PRE_V2_SOURCE_COMMIT = "f80a2649232dd25761276ccf7043cf3f3a79e031"

LATEX_COMMENT_ENVIRONMENT = re.compile(
    r"\\begin\s*\{comment\}.*?\\end\s*\{comment\}", re.DOTALL
)
LATEX_COMMAND_START = re.compile(
    r"\\(?P<kind>newcommand|renewcommand|providecommand)\*?"
    r"\s*(?:\{\s*)?\\(?P<name>[A-Za-z@]+)(?:\s*\})?"
)
LATEX_ENVIRONMENT_START = re.compile(
    r"\\(?P<kind>newenvironment|renewenvironment)\*?"
    r"\s*\{(?P<name>[^}]+)\}"
)
XPARSE_COMMAND_START = re.compile(
    r"\\(?P<kind>DeclareDocumentCommand|NewDocumentCommand|"
    r"RenewDocumentCommand|ProvideDocumentCommand)\s*"
)
XPARSE_ENVIRONMENT_START = re.compile(
    r"\\(?P<kind>NewDocumentEnvironment|RenewDocumentEnvironment|"
    r"DeclareDocumentEnvironment|ProvideDocumentEnvironment)\s*"
)
TEX_DEF_START = re.compile(
    r"\\(?P<kind>def|gdef|xdef|edef)\s*\\(?P<name>[A-Za-z@]+)"
)


def is_escaped(text: str, index: int) -> bool:
    """Return whether the character at index has an odd backslash prefix."""

    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def strip_line_comments(text: str) -> str:
    """Strip TeX comments while preserving an escaped ``\\%`` token."""

    cleaned: list[str] = []
    for line in text.splitlines():
        comment_at = None
        for index, character in enumerate(line):
            if character == "%" and not is_escaped(line, index):
                comment_at = index
                break
        cleaned.append(line[:comment_at] if comment_at is not None else line)
    return "\n".join(cleaned)


def strip_comments(text: str) -> str:
    # Remove line comments first so a commented-out ``\\begin{comment}`` cannot
    # consume later live source through a real ``\\end{comment}``.
    return LATEX_COMMENT_ENVIRONMENT.sub("", strip_line_comments(text))


def normalize_spec(spec: str) -> str:
    return " ".join(spec.split())


def skip_whitespace(text: str, position: int) -> int:
    while position < len(text) and text[position].isspace():
        position += 1
    return position


def read_balanced_group(
    text: str, position: int, opener: str = "{", closer: str = "}"
) -> tuple[str, int] | None:
    """Read one balanced TeX group, allowing braces inside bracket groups."""

    position = skip_whitespace(text, position)
    if position >= len(text) or text[position] != opener:
        return None

    depth = 0
    brace_depth = 0
    start = position + 1
    for index in range(position, len(text)):
        character = text[index]
        if is_escaped(text, index):
            continue

        if opener == "[":
            if character == "{":
                brace_depth += 1
            elif character == "}" and brace_depth:
                brace_depth -= 1
            elif brace_depth == 0 and character == opener:
                depth += 1
            elif brace_depth == 0 and character == closer:
                depth -= 1
                if depth == 0:
                    return text[start:index], index + 1
        else:
            if character == opener:
                depth += 1
            elif character == closer:
                depth -= 1
                if depth == 0:
                    return text[start:index], index + 1

    raise ValueError(f"Unterminated {opener}{closer} group near offset {position}")


def latex_signature(text: str, position: int) -> str:
    arity = 0
    arity_group = read_balanced_group(text, position, "[", "]")
    if arity_group is None:
        return "latex:0"

    arity_text, position = arity_group
    if not arity_text.strip().isdigit():
        raise ValueError(f"Invalid LaTeX command arity: {arity_text!r}")
    arity = int(arity_text.strip())

    default_group = read_balanced_group(text, position, "[", "]")
    if default_group is None:
        return f"latex:{arity}"

    default_text, _ = default_group
    return f"latex:{arity}:optional-first={normalize_spec(default_text)}"


def add_definition(
    definitions: dict[str, set[tuple[str, str]]],
    name: str,
    signature: str,
    relative: str,
) -> None:
    definitions[name].add((signature, relative))


def collect_source_declarations(
    relative: str,
    source: str,
    definitions: dict[str, set[tuple[str, str]]],
    literal_defs: dict[str, set[tuple[str, str]]],
) -> None:
    text = strip_comments(source)

    for match in LATEX_COMMAND_START.finditer(text):
        add_definition(
            definitions,
            match.group("name"),
            latex_signature(text, match.end()),
            relative,
        )

    for match in LATEX_ENVIRONMENT_START.finditer(text):
        add_definition(
            definitions,
            f"environment:{match.group('name').strip()}",
            latex_signature(text, match.end()),
            relative,
        )

    for match in XPARSE_COMMAND_START.finditer(text):
        name_group = read_balanced_group(text, match.end())
        if name_group is None:
            continue
        name_text, position = name_group
        spec_group = read_balanced_group(text, position)
        if spec_group is None:
            continue
        spec_text, _ = spec_group
        name = name_text.strip()
        if name.startswith("\\"):
            name = name[1:]
        add_definition(
            definitions,
            name,
            f"xparse:{normalize_spec(spec_text)}",
            relative,
        )

    for match in XPARSE_ENVIRONMENT_START.finditer(text):
        name_group = read_balanced_group(text, match.end())
        if name_group is None:
            continue
        name_text, position = name_group
        spec_group = read_balanced_group(text, position)
        if spec_group is None:
            continue
        spec_text, _ = spec_group
        add_definition(
            definitions,
            f"environment:{name_text.strip()}",
            f"xparse:{normalize_spec(spec_text)}",
            relative,
        )

    for match in TEX_DEF_START.finditer(text):
        name = match.group("name")
        # ``\\expandafter\\def\\csname ...\\endcsname`` is dynamic and cannot be
        # represented as the literal command named ``csname``.
        if name == "csname":
            continue
        replacement_at = match.end()
        while replacement_at < len(text):
            if text[replacement_at] == "{" and not is_escaped(text, replacement_at):
                break
            replacement_at += 1
        if replacement_at >= len(text):
            continue
        parameters = text[match.end() : replacement_at]
        arity = max((int(value) for value in re.findall(r"#([1-9])", parameters)), default=0)
        add_definition(
            literal_defs,
            name,
            f"texdef:{match.group('kind')}:{arity}",
            relative,
        )


def finalize_entries(
    definitions: dict[str, set[tuple[str, str]]],
) -> dict[str, ApiEntry]:
    entries: dict[str, ApiEntry] = {}
    for name in sorted(definitions):
        values = sorted(definitions[name])
        entries[name] = {
            "signatures": sorted({signature for signature, _ in values}),
            "defined_in": sorted({path for _, path in values}),
        }
    return entries


def collect_from_sources(
    sources: Iterable[SourceText],
) -> tuple[dict[str, ApiEntry], dict[str, ApiEntry]]:
    definitions: dict[str, set[tuple[str, str]]] = defaultdict(set)
    literal_defs: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for relative, text in sources:
        collect_source_declarations(relative, text, definitions, literal_defs)
    return finalize_entries(definitions), finalize_entries(literal_defs)


def current_sources() -> list[SourceText]:
    return [
        (
            path.relative_to(ROOT).as_posix(),
            path.read_text(encoding="utf-8"),
        )
        for path in sorted(TEMPLATE_ROOT.rglob("*.tex"))
    ]


def git_sources(commit: str) -> list[SourceText]:
    names = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", commit, "thesis/template"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    sources: list[SourceText] = []
    for relative in sorted(name for name in names if name.endswith(".tex")):
        text = subprocess.check_output(
            ["git", "show", f"{commit}:{relative}"],
            cwd=ROOT,
            text=True,
        )
        sources.append((relative, text))
    return sources


def collect_api() -> dict[str, ApiEntry]:
    """Return the current LaTeX/xparse API (used by focused ownership checks)."""

    entries, _ = collect_from_sources(current_sources())
    return entries


def run_scanner_self_test() -> list[str]:
    failures: list[str] = []
    probe = r"""
\newcommand{\RuntimeVisible}{}
\begin{comment}
\newcommand{\CommentOnly}{}
\end{comment}
\newcommand{\EscapedPercentVisible}{} \% \newcommand{\AfterEscapedPercent}{}
\newcommand{\BeforeRealComment}{} \\% \newcommand{\AfterRealComment}{}
\newcommand{\MandatoryProbe}[2]{}
\newcommand{\OptionalProbe}[2][old default]{}
\DeclareDocumentCommand{\NestedOne}{+O{\empty} +m +G{\empty}}{}
\DeclareDocumentCommand{\NestedTwo}{+O{\empty} +m}{}
\def\LiteralDefProbe#1#2{}
\expandafter\def\csname DynamicProbe\endcsname{}
"""
    entries, literal_defs = collect_from_sources([("scanner-probe.tex", probe)])

    expected_present = {
        "RuntimeVisible",
        "EscapedPercentVisible",
        "AfterEscapedPercent",
        "BeforeRealComment",
        "MandatoryProbe",
        "OptionalProbe",
        "NestedOne",
        "NestedTwo",
    }
    for name in sorted(expected_present):
        if name not in entries:
            failures.append(f"scanner self-test lost live declaration: {name}")
    for name in ("CommentOnly", "AfterRealComment"):
        if name in entries:
            failures.append(f"scanner self-test retained commented declaration: {name}")

    expected_signatures = {
        "MandatoryProbe": ["latex:2"],
        "OptionalProbe": ["latex:2:optional-first=old default"],
        "NestedOne": [r"xparse:+O{\empty} +m +G{\empty}"],
        "NestedTwo": [r"xparse:+O{\empty} +m"],
    }
    for name, signatures in expected_signatures.items():
        actual = entries.get(name, {}).get("signatures")
        if actual != signatures:
            failures.append(
                f"scanner self-test signature mismatch for {name}: "
                f"expected {signatures}, found {actual}"
            )

    literal_signature = literal_defs.get("LiteralDefProbe", {}).get("signatures")
    if literal_signature != ["texdef:def:2"]:
        failures.append(
            "scanner self-test literal def mismatch: "
            f"expected ['texdef:def:2'], found {literal_signature}"
        )
    if "csname" in literal_defs:
        failures.append("scanner self-test treated dynamic \\def\\csname as literal")

    return failures


def write_baseline(source_ref: str) -> int:
    commit = subprocess.check_output(
        ["git", "rev-parse", f"{source_ref}^{{commit}}"],
        cwd=ROOT,
        text=True,
    ).strip()
    if commit != PRE_V2_SOURCE_COMMIT:
        raise SystemExit(
            "Refusing to regenerate the v1 baseline from a non-canonical ref: "
            f"expected {PRE_V2_SOURCE_COMMIT}, resolved {commit}"
        )

    api, literal_defs = collect_from_sources(git_sources(commit))
    payload = {
        "schema": 2,
        "source": {
            "commit": commit,
            "description": "immutable pre-v2 feat/v2.x parent",
        },
        "policy": (
            "Every runtime-visible pre-v2 LaTeX/xparse declaration remains "
            "available with a compatible argument shape throughout v2.x; literal "
            "def-style declarations and comment-environment artifacts are audited "
            "separately."
        ),
        "entries": api,
        "literal_def_entries": literal_defs,
    }
    BASELINE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(api)} v1 API entries and {len(literal_defs)} literal def "
        f"entries from {commit} to {BASELINE.relative_to(ROOT)}"
    )
    return 0


def compare_expected(
    label: str,
    expected_entries: dict[str, ApiEntry],
    current_entries: dict[str, ApiEntry],
) -> list[str]:
    failures: list[str] = []
    for name, expected in expected_entries.items():
        if name not in current_entries:
            failures.append(f"missing {label}: {name}")
            continue
        expected_signatures = set(expected["signatures"])
        current_signatures = set(current_entries[name]["signatures"])
        if not expected_signatures.issubset(current_signatures):
            failures.append(
                f"incompatible {label} {name}: expected "
                f"{sorted(expected_signatures)}, found {sorted(current_signatures)}"
            )
    return failures


def check_baseline() -> int:
    if not BASELINE.exists():
        raise SystemExit(f"Missing {BASELINE.relative_to(ROOT)}")
    if not COMMENT_ARTIFACTS.exists():
        raise SystemExit(f"Missing {COMMENT_ARTIFACTS.relative_to(ROOT)}")

    failures = run_scanner_self_test()
    payload = cast(dict[str, object], json.loads(BASELINE.read_text(encoding="utf-8")))
    if payload.get("schema") != 2:
        failures.append(f"unsupported v1 API baseline schema: {payload.get('schema')!r}")
    source = cast(dict[str, str], payload.get("source", {}))
    if source.get("commit") != PRE_V2_SOURCE_COMMIT:
        failures.append(
            "v1 API baseline source drift: expected "
            f"{PRE_V2_SOURCE_COMMIT}, found {source.get('commit')!r}"
        )

    baseline = cast(dict[str, ApiEntry], payload.get("entries", {}))
    baseline_defs = cast(dict[str, ApiEntry], payload.get("literal_def_entries", {}))
    if not baseline or not baseline_defs:
        failures.append("v1 API baseline must contain primary and literal-def entries")

    artifact_doc = json.loads(COMMENT_ARTIFACTS.read_text(encoding="utf-8"))
    artifacts = cast(dict[str, ApiEntry], artifact_doc["entries"])
    overlapping_artifacts = cast(
        dict[str, object], artifact_doc["overlapping_runtime_entries"]
    )
    overlap = sorted(set(baseline) & set(artifacts))
    if overlap:
        failures.append(
            "comment-only names remain in runtime baseline: " + ", ".join(overlap)
        )
    if len(artifacts) != 15 or len(overlapping_artifacts) != 7:
        failures.append(
            "expected 15 comment-only names and 7 overlapping comment "
            f"declarations, got {len(artifacts)} and {len(overlapping_artifacts)}"
        )

    current, current_defs = collect_from_sources(current_sources())
    failures.extend(compare_expected("v1 API entry", baseline, current))
    failures.extend(compare_expected("v1 literal-def entry", baseline_defs, current_defs))

    if failures:
        print("V1 API compatibility FAIL:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    added = sorted(set(current) - set(baseline))
    added_defs = sorted(set(current_defs) - set(baseline_defs))
    audited_declarations = len(artifacts) + len(overlapping_artifacts)
    print(
        f"V1 API compatibility PASS: {len(baseline)} LaTeX/xparse declarations "
        f"and {len(baseline_defs)} literal def-style declarations preserved; "
        f"{audited_declarations} audited comment-environment declarations; "
        f"{len(added)} primary and {len(added_defs)} literal-def v2 additions"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-baseline-from-ref",
        metavar="GIT_REF",
        help=(
            "rewrite the v1 baseline only when GIT_REF resolves to the immutable "
            f"pre-v2 commit {PRE_V2_SOURCE_COMMIT}"
        ),
    )
    args = parser.parse_args()
    if args.write_baseline_from_ref:
        return write_baseline(args.write_baseline_from_ref)
    return check_baseline()


if __name__ == "__main__":
    raise SystemExit(main())
