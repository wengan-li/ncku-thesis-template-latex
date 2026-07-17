# V2 Deprecated Command Compatibility Consolidation

Status: complete on `feat/v2.x`; pending commit/push and exact-SHA hosted verification
Owner: Leon / Tachikoma
Date: 2026-07-17

## Intent

### Goal

Move the runtime deprecated public-command tombstones out of generic command modules and into one v1 compatibility module without changing their names, signatures, diagnostics, stop behavior, load timing, or canonical output.

### Constraints

- Preserve all 597 runtime-visible v1 declarations and compatible signatures.
- Keep every deprecated command as a literal declaration; do not hide public names behind generated definitions.
- Preserve each existing `\errmessage` text and trailing `\stop` behavior exactly.
- Move only runtime deprecated declarations. Preserve the live one-argument `\RefTo` helper in `cmd-ref.tex`; do not revive or move its commented-out zero-argument tombstone.
- Do not merge `main`, tag, release, or update Overleaf.
- Keep CodeGraph's `.codegraph/` index local and outside Git.

### Failure Conditions

- Any of the 23 runtime tombstones disappears, changes signature, changes diagnostic text, or no longer stops.
- The live one-argument `\RefTo` helper disappears, changes signature/path, or gains the commented-out zero-argument deprecated tombstone as a second project declaration.
- A tombstone remains duplicated in a generic command module.
- V1 API, unchanged-project migration, focused behavior, canonical text/layout, or hosted tests regress.
- Any `.codegraph/` path becomes tracked, staged, committed, or pushed.

## Expectations

### Done Means

- One `template/compat/deprecated.tex` file owns all 23 literal deprecated public declarations.
- `template/compat/v1.tex` loads the deprecated compatibility module after the generic command modules.
- A focused fixture invokes every tombstone under an intercepted `\errmessage`/`\stop` pair and asserts the complete ordered diagnostic contract.
- The v1 API gate reports 597/597 runtime declarations and the existing 22 comment-environment audit declarations.
- Documentation distinguishes the previously corrected `\SetDeptName` short-name behavior from the actual pending tombstone consolidation.

### Success Scenarios

1. Existing projects still find every old command and receive the same migration diagnostic.
2. Maintainers can inspect deprecated public compatibility in one file instead of seven generic modules.
3. Generic command modules contain active mechanisms rather than 1.x migration tombstones.
4. The canonical NCKU thesis remains output-identical.

### Recovery Plan

If the focused contract, API gate, or canonical comparison changes, restore the 23 literal declarations to their original modules and keep the fixture/todo as diagnostic evidence. Do not weaken the expected diagnostics or add the comment-only `\RefTo` command.

### Validation

```text
just _test-deprecated-command-contract
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
canonical page/text/bbox and selected raster comparison
git ls-files '.codegraph/**'  # empty
```

## Context

### Current Evidence

- Runtime inventory: 23 zero-argument commands declared with `\newcommand{...}{\errmessage{...}\stop}` across abstract, bibliography, chapter, figure, multi-figure, numbering, and spacing modules.
- The live `\RefTo` remains `latex:1` in `cmd-ref.tex`; its historical commented zero-argument tombstone remains excluded.
- The current API checker enforces names/signatures but intentionally does not require declarations to remain in their v1 source paths.
- `\SetDeptName{chi}{short}{full}` is not pending debt: v2 already stores `short`, exposes `\GetDeptEngShortName`, and tests it in `tests/helper-values.tex`. The optimization review wording is stale.
- CodeGraph v1.2.0 indexes this repository's Python/YAML validation tooling but not TeX structure; TeX declaration inventory therefore uses direct source search plus runtime/API fixtures.

### Runtime Tombstones

```text
EndChiAbstract
SetChapterReferenceTitle
ChapterReferenceTitleInChi
ChapterReferenceTitleInEng
BibStyleUseAbbrv
BibStyleUsePlain
BibStyleUseAlpha
BibStyleUseApacite
ChapterTitleNumInChi
ChapterTitleInChi
ChapterSectionTitleInChi
InsertCenterImage
InsertImage
InsertMultiImages
ChapterTitleNumFormat
SectionTitleNumFormat
SubSectionTitleNumFormat
SubSubSectionTitleNumFormat
AppendixChapterTitleNumFormat
AppendixSectionTitleNumFormat
AppendixSubSectionTitleNumFormat
AppendixSubSubSectionTitleNumFormat
ThesisWroteInChi
```

## Progress

- [x] Recover the live runtime and comment-only boundaries.
- [x] Add the focused pre-move runtime contract.
- [x] Move the 23 literal declarations into the compatibility module.
- [x] Synchronize current documentation.
- [x] Run local/full/canonical validation.
- [ ] Commit, push, and verify exact-SHA hosted tests.

## Local Validation Result

- Focused contract: 23 exact diagnostic matches and 23 intercepted `\stop` calls.
- Ownership contract: all 23 literal zero-argument tombstones are owned only by `template/compat/deprecated.tex`; live `\RefTo` remains `latex:1` in `cmd-ref.tex`.
- V1 API: 597 runtime declarations preserved, 22 audited comment-environment declarations, 105 v2 additions.
- Unchanged v1 project: 18 files / 296,726 bytes source-identical.
- `just test`: pass.
- `just ci`: pass.
- Canonical PDF: 271 pages; complete layout text identical; all 40,820 normalized bbox word tuples identical; page 1, 82, and 258--261 rasters identical at 150 DPI.
- CodeGraph safety: `.codegraph/` remains local via `.git/info/exclude` and is not tracked or staged.
