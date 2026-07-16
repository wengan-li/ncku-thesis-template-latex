# V2 Local Theorem Hardening

Status: complete, local-only
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

- One private ordered registry owns theorem type order, default environment/text/counter metadata, style policy, key-family declaration, membership, aggregate initialization, and default setter dispatch.
- Existing per-type public insertion helpers and initializers remain explicitly declared with their established signatures; their bodies delegate to registry-backed internals.
- Counter routing resolves registered targets dynamically, freezes effective values, handles self-reference without recursive aliases, preserves unknown/empty no-op behavior, and supports optional types becoming numbered.
- Focused fixtures exercise all defaults, known setter/counter routes, self/unknown/empty sentinels, styles, labels, and counter policies.
- Focused checks, v1 compatibility, `just ci`, and output comparisons pass.
- All work remains in reviewable local commits.

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
4. Start registry work with only membership/order/dispatch; promote metadata, key declarations, and initialization into the registry only after focused custom/default/counter fixtures pass.
5. Preserve old unknown-type no-op behavior explicitly; direct construction of `/Theorem<Type>Format` for arbitrary input would create a new pgfkeys error path.
6. Resolve and freeze an effective parent counter before redefining the source getter. Storing a getter alias can create recursive self-follow definitions or later state coupling.
7. Historically unnumbered helpers expose `FollowCounter`; an empty value keeps the starred form, while an explicitly configured parent must create a numbered global/scoped form after resolution.
8. Generic initializer scratch macros must be frozen into each `\newtheorem` declaration; otherwise every environment can render the final registry row's heading.

### Current Evidence

- Local base fix commit: `0e98dcb`.
- Theorem fixture covers all 21 insertion helpers, 15 labels, title/ref/nameref, section reset, and proof marker.
- Full v1 declaration gate preserves 612 entries with 100 additive v2 declarations.
- Canonical 271-page output has zero layout-text or normalized bbox word-tuple changes; theorem pages 50, 51, and 269 remain raster-identical, and the theorem contract raster matches the pre-registry fixture.
- The custom matrix now renders 26 entries covering all 21 custom environment/text routes, plain/definition styles, global/Section/arbitrary-custom/forward/multi-hop/chained-empty counters, and optional-type numbering.
- The negative cycle fixture produces the package diagnostic without recursive TeX-capacity overflow.
- `cmd-theorem.tex` is 574 lines, 505 lines (46.8%) smaller than the 1,079-line pre-consolidation source.

## Progress

- [x] Correct theorem label-key leakage and mutable title metadata.
- [x] Add focused theorem runtime contract.
- [x] Record reusable optional-argument/title-state lessons.
- [x] Extend registry routing/no-op fixture coverage.
- [x] Introduce private ordered theorem type registry.
- [x] Validate and create a local-only implementation commit.
- [x] Add custom theorem style/counter matrix coverage.
- [x] Correct chained-to-unscoped numbered initialization.
- [x] Validate and create the next local-only commit.
- [x] Freeze all 21 default metadata and counter-routing contracts.
- [x] Make one registry own key declarations, style/policy metadata, and defaults.
- [x] Consolidate all numbered/optional initializer branches and counter mapping.
- [x] Run final local compatibility/output proof and commit the completed theorem cleanup.
