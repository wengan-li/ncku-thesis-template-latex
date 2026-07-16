# V2 Local Float Hardening

Status: complete; promoted to `feat/v2.x`
Owner: Leon / Tachikoma

## Intent

### Goal

Reduce duplicated figure/multi-figure/table framing internals without changing any public API, option semantics, float placement, caption/label behavior, or visible canonical output.

### Constraints

- Work only on local `feat/v2-local-hardening`.
- Do not push, merge to `main`, tag, release, publish, or update Overleaf.
- Preserve every v1 declaration and direct XeLaTeX path.
- Keep `InsertFigure` and `InsertFigures` `pos`/`align` compatibility keys accepted but behaviorally inactive; all three parent floats remain forced `[H]`.
- Extract only the exact minipage/mdframed/opacity wrapper shared by figure, multi-figure, and table paths.

### Failure Conditions

- Any public figure/table command or signature disappears.
- A caption, label, subcaption, reference, table caption position, image transform, or table scaling value changes.
- A compatibility key begins changing placement/alignment.
- Focused float text, normalized word coordinates, image inventory, or rendered pixels change after extraction.
- Canonical thesis text/bbox/raster evidence changes.
- Any remote, release, or Overleaf state changes.

## Expectations

### Done Means

- A focused pre-refactor float contract freezes single figure, multi-figure, subfigure, top/bottom/starred table, key-state, label/reference, asset, page, and rendered behavior.
- One private helper owns only the identical `minipage` + zero-line `mdframed` + opacity wrapper.
- Public wrappers and table content helper retain their established declarations and signatures.
- Focused/full validation and exact before/after artifact comparisons pass.
- Learning and implementation are committed locally with no upstream.

### Success Scenarios

- Figure and multi-figure captions/references remain numbered and subfigure labels resolve.
- Table captions remain above/below according to `pos`; `nomtitle` remains unnumbered.
- Scale, angle, opacity, tab spacing, row stretch, and compatibility key state are preserved.
- Canonical 271-page thesis output remains unchanged.

### Recovery Plan

If any focused or canonical artifact differs, revert only the uncommitted helper extraction and retain the fixture as evidence. Do not weaken exact comparisons to make a refactor pass.

### Validation

```text
just _test-float-contract
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just ci
git diff --check
pdftotext -layout and normalized bbox word tuples
fixed-DPI focused/canonical raster comparisons
visual inspection of focused float pages
```

## Context

### Current Evidence

- `cmd-figure.tex`, `cmd-figures.tex`, and `cmd-table.tex` repeat the same full-width minipage and zero-line `mdframed` wrapper with only opacity/content varying.
- Figure and multi-figure `pos`/`align` keys are documented compatibility no-ops; implementations force `[H]`.
- Table `pos=top|bottom` is active caption placement and must remain independent from float placement.
- Existing canonical teaching pages provide integration coverage but no focused exact float contract existed.
- The focused contract reproduced `Undefined control sequence: \TmpMISubValueCaption` when `\nameref` read subfigure metadata after scope exit; other names retained mutable `\TmpValueCaption`/`\TmpMIValueCaption` tokens.
- Caption wrappers now freeze literal current-label names before labels. The one-page contract passes with eight names, four images/four masks, no box/reference warnings, and exact top/bottom/star order.
- The corrected pre-refactor baseline is `/tmp/ncku-float-contract-fixed-baseline.pdf`; canonical text/bbox and float pages 82/258--261 remain identical.
- One two-argument private helper now owns the three exact minipage/mdframed/opacity wrappers. Combined source size is 773 to 770 lines; the small net reduction is secondary to having one framing policy.
- Post-extraction focused text, bbox word tuples, and raster are identical to the corrected baseline. `just ci`, the then-current 612-entry scanner gate (later corrected to 597 runtime declarations plus 22 audited comment-environment declarations), 102 v2 additions, unchanged 18-file v1 migration input, canonical 271-page text/bbox, and selected float-page rasters all pass.

## Progress

- [x] Record theorem closeout learning before continuing.
- [x] Inventory float implementations and public API boundary.
- [x] Add and baseline the focused float contract.
- [x] Extract the shared private framed-content helper.
- [x] Run focused/full artifact validation.
- [x] Write durable lessons and create the local-only implementation commit.

## Promotion Decision

On 2026-07-17 the owner lifted the local-only publication boundary for the
completed hardening commits. The slice was fast-forwarded to `feat/v2.x` at
implementation head `ce5c4943e9ce71029219590883eea090d1c022b5`; both the exact-SHA
push and pull-request Test workflows passed. The original no-merge, no-tag,
no-Release, and no-Overleaf boundaries remain in force.
