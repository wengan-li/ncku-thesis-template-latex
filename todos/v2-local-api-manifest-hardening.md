# V2 Local API Manifest Hardening

Status: complete, local-only
Owner: Leon / Tachikoma

## Intent

Correct the v1 API compatibility gate so it represents runtime-visible LaTeX declarations rather than declarations inside `comment` environments, then remove only the audited runtime-dead blocks.

## Constraints

- Work only on local `feat/v2-local-hardening`.
- Do not push, merge `main`, tag, release, publish, or update Overleaf.
- Do not drop a real v1 runtime name or compatible signature.
- Do not weaken the baseline merely to make dead-code deletion pass.
- Preserve a durable audit of every comment-only or runtime-overlapping declaration.
- Require unchanged v1 student files and identical canonical thesis artifacts.

## Evidence

- Original name-set comparison found 15 names visible only because `%`-comment stripping did not handle `\begin{comment}...\end{comment}`.
- Signature comparison found seven additional dead declarations overlapping live tombstones. Six had the same signature; dead `\SetChapterReferenceTitle[1]` added a false `latex:1` signature to the live zero-argument tombstone.
- `tests/v1-public-api.json` now contains 597 runtime-visible v1 names.
- `tests/v1-comment-environment-artifacts.json` records 22 dead declarations: 15 comment-only names and seven runtime overlaps.
- The scanner has a self-test proving that a visible command survives while a command inside a LaTeX `comment` environment is ignored.
- Three numbering comment blocks and one obsolete bibliography block were removed only after the corrected gate passed with the blocks still present.
- Current gate: 597/597 runtime declarations, 22 audited comment-environment declarations, 105 additive v2 declarations.
- Unchanged migration input: 18 files, 296,726 bytes.
- `just ci` passes.
- Canonical comparison: 271 pages, no normalized layout-text changes, identical bbox word tuples, and raster-identical pages 40, 44, 125, 143, and 144.

## Validation

```text
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just _test-numbering-contract
just _test-custom-style
just ci
git diff --check
normalized canonical text/bbox and selected rasters
```

## Recovery

If a runtime declaration disappears or canonical output changes, revert the dead-block deletion and retain the scanner/audit correction for diagnosis. Do not restore the incorrect 612 count without proving those declarations existed at runtime.

## Progress

- [x] Compare old scanner output with comment-aware output by name.
- [x] Compare per-name signatures and identify runtime overlaps.
- [x] Preserve the 22-declaration audit artifact.
- [x] Correct the runtime baseline to 597 names.
- [x] Add the scanner self-test.
- [x] Remove only audited runtime-dead blocks.
- [x] Update all current compatibility documentation and annotate historical checkpoints.
- [x] Run focused/full/canonical validation.
- [x] Create the local-only commit and verify remote immutability.
