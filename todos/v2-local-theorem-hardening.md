# V2 Local Theorem Hardening

Status: active, local-only
Owner: Leon / Tachikoma

## Intent

### Goal

Make theorem internals safer to maintain without changing the public 1.x/2.x command surface or visible NCKU output.

### Constraints

- Work only on the local `feat/v2-local-hardening` branch.
- Do not push, merge to `main`, tag, publish a Release, or update Overleaf.
- Preserve all entries in `tests/v1-public-api.json` and the direct XeLaTeX path.
- Keep each theorem refactor independently reviewable and output-neutral.
- Record reusable findings in the class-level LaTeX skill and repository-local maintenance sources before continuing implementation.

### Failure Conditions

- Any public theorem command, argument shape, key family, type, style, or counter behavior disappears.
- An unknown `\SetTheoremFormat[...]` type stops being a silent no-op.
- The theorem fixture loses working labels, `\ref`, `\nameref`, section reset, or proof marker behavior.
- Canonical extracted text/word coordinates or representative theorem-page rasters change.
- Work is pushed, merged, released, or sent to Overleaf without a new explicit owner decision.

## Expectations

### Done Means

- One private ordered registry drives only aggregate theorem initialization and `\SetTheoremFormat` dispatch.
- Existing per-type public insertion helpers, initializers, key families, styles, and counter implementations remain intact.
- The focused fixture exercises every registered setter route and an unknown-type no-op sentinel.
- Focused checks, v1 compatibility, `just ci`, and output comparisons pass.
- Learning and implementation are separate local commits.

### Success Scenarios

- All 21 theorem types initialize in the established order and still render through their existing wrappers.
- Each known type can be routed by `\SetTheoremFormat` through the registry.
- Unknown and empty type selectors remain no-ops.
- The local branch stays ahead of `origin/feat/v2.x` with no upstream or remote mutation.

### Recovery Plan

If a fixture, compatibility gate, or output comparison changes unexpectedly, revert only the uncommitted registry slice and keep the completed theorem label/title fix plus learning checkpoint.

### Validation

```text
just _test-theorem-contract
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just ci
git diff --check
pdfinfo build/thesis.pdf
pdftotext/pdftotext -bbox normalized comparison
150-DPI raster comparison for theorem integration pages
```

## Context

### Learned Constraints

1. Optional-call syntax is semantic in TeX: braces passed to an optional helper become document input instead of the optional argument.
2. Reusable pgf key state must not be written by name to label metadata; freeze the current title before `\label` so later insertions cannot blank `\nameref`.
3. Declaration compatibility alone does not protect runtime behavior; the focused theorem contract must remain in `just test`.
4. A first registry slice should centralize only type membership/order and dispatch. Combining declaration generation, counter mapping, styles, and rendering in one rewrite would hide regressions.
5. Preserve old unknown-type no-op behavior explicitly; direct construction of `/Theorem<Type>Format` for arbitrary input would create a new pgfkeys error path.

### Current Evidence

- Local base fix commit: `0e98dcb`.
- Theorem fixture covers all 21 insertion helpers, 15 labels, title/ref/nameref, section reset, and proof marker.
- Full v1 declaration gate preserves 612 entries with 93 additive v2 declarations.
- Canonical 271-page output has zero text or normalized bbox changes; theorem pages 50, 51, and 269 remain raster-identical after the registry slice.

## Progress

- [x] Correct theorem label-key leakage and mutable title metadata.
- [x] Add focused theorem runtime contract.
- [x] Record reusable optional-argument/title-state lessons.
- [x] Extend registry routing/no-op fixture coverage.
- [x] Introduce private ordered theorem type registry.
- [x] Validate and create a local-only implementation commit.
