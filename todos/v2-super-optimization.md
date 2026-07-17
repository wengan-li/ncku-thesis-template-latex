# V2 Super Optimization and Simplification

Status: implementation complete; full and hosted validation in progress
Owner: Leon / Tachikoma
Date: 2026-07-17

## Intent

### Goal

Reduce the active dependency and maintenance cost of the v2 template and improve
measured cold-build performance without changing the public template contract or
the default NCKU document.

### Constraints

- Keep XeLaTeX, direct student `latexmk`, Overleaf, and root `just` workflows.
- Preserve the complete v1 API manifest and compatible argument shapes.
- Preserve the canonical 271-page NCKU text, geometry, and representative pixels.
- Prefer current LaTeX-kernel primitives and lighter existing package modes over
  introducing replacement libraries.
- Keep required clean CI and release builds deterministic; do not cache auxiliary
  state into correctness gates.

### Failure Conditions

The optimization fails if any slice:

- changes a protected v1 declaration/signature or student-owned pinned input;
- changes canonical page count, normalized text/bbox tuples, or reviewed raster
  output without a separately approved visible correction;
- removes required `G{...}` xparse compatibility, XeLaTeX, direct student builds,
  or exact release packaging;
- increases the focused student cold-build median, or claims performance from a
  single noisy timing;
- adds a dependency or abstraction without removing measured cost or duplication.

## Expectations

### Done Means

- At least one active package/dependency path is removed or materially lightened.
- The optimized path is exercised by a focused fixture and the complete gate.
- Before/after timings use the same host, command, run count, and clean-state
  procedure and are recorded as evidence rather than a universal guarantee.
- Final source, docs, and todo are committed and pushed to `feat/v2.x`; exact-SHA
  push and pull-request Test runs pass; `main` remains unchanged.

### Success Scenarios

1. A package used for trivial arithmetic is replaced by deterministic integer
   primitives while year and modulo public behavior remains exact.
2. A heavy rendering backend is replaced by a lighter supported mode only when
   complete canonical text/bbox and representative raster output stay identical.
3. Current tools that are already latest and appropriate remain unchanged rather
   than receiving version churn.
4. No-op builds remain near-instant and student builds remain the primary user
   performance measure; the 271-page teaching corpus remains integration coverage.

### Recovery Plan

- Revert an experimental slice immediately when output or API evidence changes.
- Keep a simplification with statistically noisy timing only when it removes a
  real dependency and does not worsen the student median; describe it as
  maintenance/dependency reduction, not a speed claim.
- Stop after the first useful slice if later candidates require broad public API
  rewrites or visible-layout retuning.

### Validation

Focused:

```bash
python3 scripts/test/check-v1-api.py
just _test-helper-values
just _test-float-contract
just _test-student-mode
```

Complete:

```bash
just test
just ci
just release review
```

Artifact checks include `pdfinfo`, complete `pdftotext -layout`, normalized
`pdftotext -bbox-layout` tuples, fixed-DPI representative rasters, `.fls` package
presence/absence, `git diff --check`, exact student ZIP tree/direct build, and
local/remote/PR exact-SHA parity.

## Context

### Current Evidence

Toolchain on the benchmark host:

```text
XeTeX 0.999998 / TeX Live 2026 Homebrew
latexmk 4.87
just 1.56.0
```

Current GitHub Actions are already their official latest stable majors as of this
review: `actions/checkout@v7`, `actions/upload-artifact@v7`,
`actions/download-artifact@v8`, and `xu-cheng/texlive-action@v3`. The JavaScript
actions use Node 24; no action-version churn is justified.

Baseline at `c9d30b5e60ecc09ec61548d03f317662a2e15c9e`, measured with three clean
runs and five no-change runs on the same host:

```text
canonical cold: 30.708s, 29.473s, 30.365s; median 30.365s
canonical no-op: 0.149s, 0.144s, 0.138s, 0.139s, 0.140s; median 0.140s
student cold:   7.644s, 6.861s, 6.724s; median 6.861s
```

Convergence work:

```text
canonical: 4 XeLaTeX + 3 BibTeX + 1 xdvipdfmx
student:   3 XeLaTeX + 2 BibTeX + 1 xdvipdfmx
```

The no-op result proves that latexmk dependency tracking is already effective.
The normal student path is much smaller than the 271-page teaching corpus, so
optimizations must report both audiences separately.

The canonical `.fls` currently contains 112 unique package/class/definition
inputs totaling about 2.26 MB of source. Relevant active paths include:

- `fp` 2.1d: 12 files / about 117 KB, used by only three integer calculations;
- `mdframed` 1.9b with `framemethod=tikz`: one core file plus the TikZ/PGF
  frontend; only float wrappers, `DescriptionFrame`, and extended-summary boxes
  use it;
- `ifthen`: 208 calls; broad replacement is high-risk and not a first slice;
- `xparse`: required because protected public commands still use deprecated
  `G{...}` arguments that the LaTeX kernel deliberately does not provide.

Official LaTeX evidence:

- Document-command APIs entered the kernel in LaTeX 2020-10-01, but `g/G`, `l`,
  and `u` remain available only through explicit `xparse` compatibility.
- `xfp` is itself deprecated because `\fpeval` entered the kernel in 2022-06-01;
  adding `xfp` is therefore not modernization.
- `mdframed` officially supports a default LaTeX-rule renderer in addition to
  TikZ and PSTricks; only the backend mode should change in the first rendering
  experiment.
- latexmk 4.87 already provides the correct dependency/convergence and `-pvc`
  workflow; replacing it is not justified.

### Candidate Ranking

1. **TikZ-backed `mdframed` to its default renderer — rejected.** The experiment
   removed TikZ from the active graph but changed the canonical document from 271
   to 270 pages and introduced a new `mdframed` bad-break warning. The three
   source edits were fully rolled back rather than retuning visible layout.
2. **Remove `fp` for three numeric operations — completed.** The existing LaTeX
   programming layer now preserves integer, decimal, truncation, and TeX group
   semantics without adding `xfp`; all 12 `fp` files (about 117 KB) leave the
   active graph.
3. **Simplify month lookup — completed.** One native 12-way branch table replaces
   21 sequential `ifthenelse` calls while preserving `1`/`01` through `12` and
   empty output for invalid numeric ranges. The repository now has 187 remaining
   calls; no broad rewrite is justified.
4. **Keep and explicitly declare `xparse` — completed.** Protected `G{...}`
   signatures require it, so source ownership no longer depends on fontspec's
   transitive load.
5. **Do not update GitHub Action majors.** They are already current and Node 24.

### Measured Result

The retained arithmetic/package slice produced these same-host medians:

```text
single-pass preamble: 0.690s -> 0.673s (-2.37%, 8 alternating runs each)
student cold:         6.861s -> 6.685s (-2.56%, 3 runs each)
canonical no-op:      0.140s -> 0.141s (effectively unchanged)
```

The three-run 271-page canonical cold median was noisy and increased from
30.365s to 33.694s while the machine was under changing background load. It is
not evidence of a full-corpus speedup and is not presented as one. The retained
claim is narrower: fewer active dependencies, simpler month dispatch, a small
isolated preamble/student improvement, and unchanged output.

## Progress

- [x] Verified clean local/remote/PR starting head and unchanged `origin/main`.
- [x] Recorded toolchain, package graph, convergence passes, and baseline timings.
- [x] Checked official LaTeX/CTAN/latexmk and GitHub Action evidence.
- [x] Rejected and fully rolled back the lighter mdframed backend after the page
      count changed from 271 to 270 and a new bad-break warning appeared.
- [x] Removed `fp`, added decimal/negative semantic fixtures, and verified zero
      active `fp` records.
- [x] Replaced 21 month comparisons with a 12-way branch and made `xparse`
      ownership explicit.
- [x] Verified canonical 271-page layout text, 40,823 normalized bbox tuples, and
      raster pages 1, 2, 82, and 258--261 are identical to
      `c9d30b5e60ecc09ec61548d03f317662a2e15c9e`.
- [ ] Run complete compatibility/release/output/hosted gates and record results.
