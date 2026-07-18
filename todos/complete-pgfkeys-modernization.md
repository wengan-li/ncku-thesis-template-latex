# Complete command-parser `pgfkeys` modernization

Status: active
Owner: Leon
Started: 2026-07-18

## Intent

### Goal

Complete the compatibility-preserving migration of repository-owned command parsers away from direct `pgfkeys`, while retaining `pgfkeys` wherever PGF/TikZ naturally owns it.

### Constraints

- Preserve all public commands, signatures, selectors, and XeLaTeX/Overleaf paths.
- Keep each subsystem independently reviewable and reversible.
- Preserve canonical visible output, pagination, coordinates, fonts, and extracted student-package behavior.
- Do not tag, release, or update Overleaf as part of parser modernization.

### Failure conditions

- A default, macro-valued key, repeated/partial setup, omitted input, unknown key, selector, counter, label, caption, or rendered route changes unexpectedly.
- Canonical text, normalized bounding boxes, font metadata, or any fixed-DPI page raster changes.
- The extracted exact-HEAD student ZIP does not direct-build with XeLaTeX and resolved references.
- Direct `pgfkeys` references remain in repository-owned generic command parsers without an evidence-backed retention decision.

## Expectations

### Done means

- Remaining numbering, multi-figure, and dynamic-theorem parser families are migrated through frozen contracts, or an audited family is explicitly retained because it uses native PGF/TikZ semantics.
- Source inventory and shipped modernization records match the final implementation.
- Every subsystem PR and the final merged-main SHA pass local and hosted gates.

### Success scenarios

1. Nine remaining numbering families preserve default/custom general and appendix title/counter output.
2. Top-level and nested multi-figure options preserve row dispatch, captions, labels, opacity, subfigure rendering, and failure behavior.
3. Dynamic theorem style/counter setup preserves all registry types, chaining, unknown-type behavior, labels, and cycle diagnostics.
4. Final source audit reaches zero repository-owned command-parser `pgfkeys` references, or lists only justified PGF/TikZ-native retention.

### Recovery plan

- Stop and revert the current family commit when focused or canonical identity fails.
- Improve the legacy fixture before retrying if behavior is not fully characterized.
- Do not weaken an identity or unknown-key gate to make a migration pass.

### Review checkpoints

- Normal-merge only PRs whose exact head has successful push and pull-request checks and `mergeStateStatus=CLEAN`.
- Keep release, tag, and Overleaf publication outside this brief.

### Validation

- Focused positive and negative parser contracts per subsystem.
- `just ci` from clean committed heads.
- Full canonical text, normalized bbox word tuples, `pdffonts`, and all 271 fixed-DPI rasters.
- `just release review` and repo-external direct build of the generated student ZIP.
- Exact-SHA hosted push and pull-request checks; merged-main local and hosted read-back.

## Context

### Current evidence

At merged-main `650a6d9c89a56250e57d6ff652b83a1324d5c541`:

- 35 direct `pgfkeys`/`pgfkeysvalueof` references remain across three files.
- `cmd-numbering.tex` owns 27 references across nine families.
- `cmd-figures.tex` owns six references across top-level and nested multi-figure families.
- `cmd-theorem.tex` owns two dynamic-registry references.
- Seven command families already use `l3keys`; active student source has zero `l3keys2e` references.
- Exact merged-main `just ci` and hosted push run 29664936529 pass.

## Progress

- [x] Merge validated Chapter title-format PR #87.
- [ ] Migrate the remaining nine numbering families.
- [ ] Migrate top-level and nested multi-figure families.
- [ ] Migrate or explicitly retain dynamic theorem parsing from evidence.
- [ ] Run final zero-reference/retention audit and graduate this brief into `docs/features/v2/`.
