# V2 Modernization IDSD Brief

Status: Active on `v2.x`
Owner: Wen-Gan Li

## Intent

### Goal

Deliver one v2 development line that improves helper correctness and restores a
real non-NCKU style-port boundary while preserving the established NCKU output,
student project shape, and 1.x public command surface.

### Constraints

- Preserve the visible NCKU cover, front matter, body layout, and direct XeLaTeX
  workflow unless a focused fixture proves a bug requires a documented change.
- Keep `thesis.tex`, `conf/conf.tex`, and the packaged top-level student
  structure stable.
- Keep all explicitly declared 1.x commands and environments available through
  the complete 2.x line.
- Keep student thesis data in `conf/`; keep institution-level ports under
  `template/style/`, matching the v1.5.0 `Customization.md` intent.
- Keep standard XeLaTeX and Overleaf builds independent of maintainer tooling.

### Failure Conditions

The outcome fails if any of these occur:

- an entry in `tests/v1-public-api.json` disappears or changes argument shape;
- the default NCKU build changes required text, page dimensions, or visible
  layout without a recorded bug and focused evidence;
- the custom profile must first load NCKU style policy in order to work;
- a v1 project cannot build on v2 through the documented compatibility path;
- migration steps omit a changed behavior or require repository-only tooling.

## Expectations

### Done Means

- The v1 API manifest is enforced by `just test`.
- Known helper defects are covered by exact focused fixtures before correction.
- Generic helper/state mechanisms no longer own NCKU college/department data or
  NCKU date policy.
- `template/style/style.tex` loads exactly one selected institution profile.
- The default `ncku` profile reproduces the established NCKU output.
- A neutral `custom` profile compiles without NCKU names, labels, or watermark
  assets in its visible output.
- `thesis/MIGRATION-1.x-TO-2.x.md` covers unchanged-project and native-v2 paths.

### Success Scenarios

1. An existing NCKU student project builds on v2 without renaming its helpers.
2. A corrected helper keeps its public signature and produces the documented
   corrected value.
3. A template maintainer copies or edits a profile under `template/style/` and
   does not need to undo NCKU setter overrides.
4. The canonical NCKU example and focused fixtures pass the same `just ci` gate.

### Recovery Plan

- If a public API gate fails, restore an adapter before continuing the refactor.
- If NCKU output changes unexpectedly, revert the output-sensitive slice and
  reduce it to a focused fixture plus one ownership change.
- If the custom profile leaks NCKU policy, move the dependency behind the NCKU
  profile or explicitly classify it as a temporary v1 compatibility adapter.

### Validation

```bash
python3 scripts/test/check-v1-api.py
just test
just ci
git diff --check
git status --short
```

For output-sensitive changes, also compare PDF metadata/text and render the
cover plus affected pages.

## Context

### Implemented Evidence

- The v1 tree declares 612 commands/environments captured and enforced by
  `tests/v1-public-api.json`.
- `template/command/command.tex` loads `template/compat/v1.tex`; historical NCKU
  catalogue helpers remain available while their data is owned by
  `template/style/ncku/`.
- `template/style/style.tex` dynamically loads exactly one registered profile.
- `template/style/ncku/ncku.tex` implements date policy through hooks instead of
  overriding public setters.
- `template/style/custom/custom.tex` builds an English cover and oral
  certificate without NCKU visible policy or watermark assets.
- `thesis/template/style/Customization.md` and the v1.5.0 changelog keep
  `template/style/` as the non-NCKU port boundary.

### Open Questions

Open decisions discovered during implementation must be recorded here or in the
migration guide before changing an observable contract. The accepted defaults
are full v1 API compatibility, one selected profile, and no separate v1.9 line.

## Progress

- [x] Create and enforce the v1 command/environment baseline.
- [x] Add exact helper contract fixtures.
- [x] Correct the first verified helper defects.
- [x] Add the v1 compatibility adapter and style profile contract.
- [x] Extract NCKU policy/data and add a neutral custom profile.
- [x] Complete migration and customization documentation.
- [ ] Run final compatibility, PDF, and rendered-page validation.
