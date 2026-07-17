# V2 Full-Review Repairs

Status: implementation complete and hosted validation passed on `feat/v2.x`
Owner: Leon / Tachikoma
Date: 2026-07-17

## Intent

Close the four actionable findings from the read-only `origin/main...feat/v2.x`
review without changing TeX runtime behavior, visible NCKU output, release
assets, or the no-merge boundary for `main`.

## Completed Slices

1. `26e8237c2fa0e9b6896d60932699cfcffa7275b2` — harden the v1 API signature
   audit with balanced xparse groups, optional-first defaults, parity-aware TeX
   comments, immutable source provenance, mutation self-tests, and a 65-name
   literal `\def` audit alongside the 597-name LaTeX/xparse surface.
2. `0116a259882abdc8d90249189a3159d68f1b35c6` — separate student-ZIP direct
   build instructions from full-repository maintainer tooling and correct the
   portable PDF path to `thesis.pdf`.
3. `14cbccb15cda3b5ca2baa5c4bc439f0675398810` — require exact `.fls` and `.blg`
   dependency records instead of substring matches.
4. `4e036df6dc3a648bf3136a0ea90ecaf75d860dc5` — remove the Release workflow's
   redundant explicit `just test`; `just release` retains the required `test`
   dependency.

## Validation

- Scanner gate: 597/597 LaTeX/xparse declarations and 65/65 literal
  `\def`-style declarations preserved; 22 comment-environment declarations
  audited; 105 primary and 4 literal-def v2 additions.
- Immutable baseline regeneration rejects refs other than
  `f80a2649232dd25761276ccf7043cf3f3a79e031`.
- V1 migration source: 18 files / 296,726 bytes match v1.8.2 exactly.
- `just ci`: pass.
- `just release review`: pass; two ZIP packages and six generated example PDFs
  verified.
- Extracted student ZIP: direct `latexmk -xelatex thesis.tex` produces
  `thesis.pdf`, 271 A4 pages, SyncTeX, and preserves all 18 pinned files.
- Canonical d13-to-current comparison: complete layout text identical, 40,823
  normalized bbox word tuples identical, zero bbox differences, and raster
  pages 1, 82, and 258--261 identical.
- `git diff --check`, Python/shell/JSON/YAML syntax, Markdown relative links,
  and generated-artifact checks pass.
- Implementation Push Test `29557691733`: success.
- Implementation Pull-request Test `29557693565`: success.

## Boundary

PR #76 remains an open review record. Do not merge `main`, create/move tags,
publish a release, or update Overleaf as part of this repair batch.