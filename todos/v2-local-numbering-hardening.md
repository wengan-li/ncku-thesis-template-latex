# V2 Local Numbering Hardening

Status: complete, local-only
Owner: Leon / Tachikoma

## Intent

### Goal

Make general/appendix numbering initialization repeatable and establish a focused compatibility contract before any numbering-registry experiment.

### Constraints

- Work only on local `feat/v2-local-hardening`.
- Do not push, merge to `main`, tag, release, publish, or update Overleaf.
- Preserve every v1 command/signature, selector/key name, default/custom title format, reference value, and canonical visible output.
- Do not remove `comment`-environment blocks merely because they are runtime-dead: the current source manifest incorrectly discovers 15 declarations inside them.
- Do not start a full declarative numbering registry until the focused general/appendix matrix passes.

### Failure Conditions

- Repeating a setup command changes its output.
- Any default/custom general or appendix title/reference/figure/table/equation format changes unexpectedly.
- Unknown or empty selectors stop being no-ops.
- Any of the seven supported counter styles changes.
- V1 API, unchanged-project migration, focused artifact, or canonical PDF evidence regresses.
- Any remote, release, or Overleaf state changes.

## Expectations

### Done Means

- A focused runtime contract covers eight title selectors, seven counter styles, default/custom general and appendix titles, fallback subsubsection references, general/appendix figure/table/equation formats, unknown/empty selectors, and repeated setup.
- The reproduced appendix-equation accumulation defect is corrected without changing first-call output.
- Only clearly disabled implementation blocks may be considered for removal, and only if the source manifest remains truthful; otherwise they remain documented debt.
- Focused/full validation and exact canonical comparisons pass.
- Learning and implementation are committed locally without an upstream.

### Recovery Plan

If the focused matrix or canonical artifact changes, revert only the uncommitted numbering correction and retain the fixture as evidence. Do not weaken expected values or alter the v1 baseline to make the change pass.

### Validation

```text
just _test-numbering-contract
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just ci
git diff --check
normalized layout text and bbox word tuples
fixed-DPI focused and canonical raster comparisons
```

## Context

### Current Evidence

- `cmd-numbering.tex` is 1,132 lines and mixes active title/counter setup with three disabled `comment` blocks.
- The current source scanner sees 714 declarations, while stripping `comment` environments leaves 699: 15 scanner-only declarations, including two disabled FTE helpers and 13 bibliography names.
- Therefore dead-block deletion is not a safe mechanical cleanup until the manifest/runtime boundary is repaired deliberately.
- `\SetupAppendixEquationNumberFormatString` uses `\appto...{}` where sibling initializers use `\renewcommand...{}`.
- A direct probe reproduced first call `2.8` and second call `2.82.8`.
- The focused matrix also reproduced prefix/separator/counter-name contamination: defaults collapsed to `2/23/234`, and all custom titles followed the final `ASSS[...]` setup.
- Three private append helpers now freeze parsed values/counter names while leaving counter formatter commands dynamic; first/second appendix F/T/E values are both `2.6/2.7/2.8`.
- Focused output covers eight selectors, seven styles, default/custom and dynamic general/appendix values on one A4 page with no box/reference warnings.
- `just ci`, 612/612 v1 declarations with 105 v2 additions, unchanged 18-file migration input, canonical 271-page text/bbox, and pages 40/44/143/144 rasters all pass.
- The three disabled numbering blocks remain because manifest-visible runtime-dead declarations require a separate policy correction before removal.

## Progress

- [x] Inventory numbering and source-manifest boundaries.
- [x] Reproduce appendix-equation accumulation.
- [x] Add the focused numbering matrix.
- [x] Correct the repeatability defect.
- [x] Run focused/full artifact validation.
- [x] Write durable lessons and create local-only commit(s).
