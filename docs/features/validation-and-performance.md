<!-- language: en; summary: validation-and-performance.zh-TW.md -->

[繁體中文摘要](validation-and-performance.zh-TW.md) | [English technical record](validation-and-performance.md)

# Validation and performance

Status: production evidence consolidated through
[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

This record distinguishes current deterministic gates from dated benchmark and
release evidence. Current tests and source win if a historical number drifts.

## Canonical repository gates

Run from the repository root:

```bash
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
git status --short
```

For a clean committed release candidate:

```bash
just release <version>
```

For an extracted student project, run from the directory containing `thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

The portable package path intentionally does not depend on repository `justfile`,
root tests, scripts, or build directories.

The tracked test-source inventory is flat and numerically grouped under `tests/`;
[`tests/000-test-suite.md`](../../tests/000-test-suite.md) defines the sparse ranges
and distinguishes executable fixtures from `900`-series historical references.
`scripts/test/check-test-layout.py` rejects unnumbered files, nested test paths,
duplicate numbers, empty reserved groups, and missing layout anchors.

## What the gate protects

| Boundary | Deterministic evidence |
| --- | --- |
| 1.x declarations | 597 LaTeX/xparse plus 65 literal `\def` entries; 22 runtime-dead comment-environment declarations audited separately |
| Unchanged 1.x project | 18 student-owned files / 296,726 bytes pinned to v1.8.2; unchanged entry/config and active StudentMode runtime paths |
| Canonical integration document | 271 A4 pages, converged references/citations, expected text and dependency records |
| Student package | regular-file list equals tracked `HEAD:thesis`; direct extracted XeLaTeX build; no repository-only tooling or redundant `thesis/` wrapper |
| Profiles | default NCKU output plus six-page neutral/custom cover/oral matrix with no NCKU visible policy or watermark asset |
| Numbering | all general/appendix selectors, seven counter styles, dynamic values, repeatability, unknown/empty no-ops |
| Theorems | 21 public routes, labels, `ref`/`nameref`, styles, counter chains, optional numbering, and deterministic cycles |
| Floats | single/multi/subfigure and table paths, caption order, labels/names, assets, scale/opacity, and compatibility key behavior |
| Metadata and fonts | Unicode metadata/bookmarks, CJK/Latin routes, exact meaningful `pdffonts` rows for output-neutral refactors |
| Draft/watermark | all three default-off layers plus explicit opt-in fixture and Gallery package defence in depth |
| Diagnostics | bounded final-log budgets; zero unresolved references/citations and zero rerun-required state |

Output-sensitive work requires layered proof. Page count and extracted text are not
sufficient on their own; use normalized `pdftotext -bbox-layout` word tuples,
`pdffonts`, fixed-DPI rasters, and visual inspection of affected pages. Raw bbox
HTML is not byte-stable because PDF metadata such as creation time changes.

## Current production release read-back

The immutable tag `v2.0.1.260719010734` points to source commit
`76b5262af9a4494fcdbff3139f5dfa6eb1317325`. Release workflow
[`29668523151`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/29668523151)
built and promoted exactly two public assets.

Public re-download checks recorded:

```text
ncku-thesis-template-latex-v2.0.1.260719010734.zip
SHA-256 c4bd107485f6f920a469c1b8a892f0844f27a43f6004c6a6fedef360cf15cbf7

ncku-thesis-template-latex-examples-v2.0.1.260719010734.zip
SHA-256 6921930adb3281623d01a877d287488bacf869a2387f160916a219fa60cf5613
```

The public bytes matched the successful workflow artifact. The downloaded
student ZIP matched the tagged `thesis/` tree exactly and built directly to a
271-page A4 PDF with SyncTeX and resolved references/citations. The examples ZIP
contained exactly its README plus six expected A4 PDFs:

| PDF | Pages |
| --- | ---: |
| `cover.pdf` | 1 |
| `thesis-chi.pdf` | 17 |
| `thesis-eng.pdf` | 17 |
| `thesis-full.pdf` | 271 |
| `defense-certificate-master.pdf` | 1 |
| `defense-certificate-phd.pdf` | 1 |

Generated defense certificates are template demonstrations and regression
outputs, not official school-system documents.

## Output-identity evidence

The V2 profile extraction and bounded internal refactors retained:

- canonical 271-page A4 output;
- complete extracted-text identity where output-neutrality was required;
- normalized word-coordinate identity for focused and canonical comparisons;
- fixed-DPI raster identity for all 271 pages during the final command-parser
  migration, plus higher-DPI representative cover, float, theorem, and final
  pages during focused slices;
- meaningful font-table identity for the dependency/performance slice;
- exact student archive tree and direct-build behavior.

The custom profile proof covers Chinese/English Master covers, Chinese oral,
Master/Doctoral English oral branches, and the Doctoral English cover. It keeps
Gregorian custom dates distinct, does not borrow oral day into a generic cover,
uses custom degree wording without changing numeric degree semantics, and loads
no NCKU watermark asset or college/department catalogue. The gate requires each
`.fls` recorder file to exist before asserting that those paths are absent.

## Dated performance evidence

Benchmarks describe their tested host and workload; they are not universal speed
promises.

### Initial modernization review

```text
271-page clean build:             31.34 s
271-page warm no-change build:     0.10–0.33 s
271-page real dependency edit:    12.51–12.93 s
11-page student clean build:       3.84 s
11-page student no-change build:   0.07 s
11-page student chapter edit:      1.45 s
```

`latexmk` was already doing correct dependency tracking. The full-corpus edit
cost was XeLaTeX layout and PDF generation, not unnecessary bibliography runs.
StudentMode with teaching examples disabled is the primary writing optimization;
`latexmk -pvc` adds automatic rebuild/viewer refresh without weakening final
build semantics.

### Dependency simplification measurement

A later same-host experiment compared three student clean runs, five no-change
runs, and alternating isolated preamble runs:

```text
single-pass preamble median: 0.690 s -> 0.673 s (-2.37%)
student cold median:         6.861 s -> 6.685 s (-2.56%)
canonical no-op median:      0.140 s -> 0.141 s (unchanged)
```

The three-run 271-page cold median moved from 30.365 s to 33.694 s under changing
background load. That is noisy and is not presented as a full-corpus speedup.
The retained claim is narrower: fewer dependencies, simpler bounded dispatch,
small isolated/student improvements, and unchanged output.

## Accepted, rejected, and deferred decisions

### Accepted

- Remove the legacy `fp` path for three numeric operations using the already
  loaded LaTeX programming layer. All 12 `fp` inputs (about 117 KB) leave the
  active graph while decimal, negative-modulo, expansion, and group semantics
  remain fixture-protected.
- Replace 21 sequential month comparisons with one native 12-way branch while
  preserving `1`/`01` through `12` and invalid-range empty output.
- Keep `xparse` as an explicit dependency because protected `G{...}` signatures
  are not supplied by the kernel document-command surface.
- Move nineteen repository-owned command parser families to `l3keys` through
  bounded baseline-first slices.
- Keep required Test and Release lanes clean rather than caching auxiliary TeX
  state into correctness gates.

### Measured and rejected

- The default non-TikZ `mdframed` renderer removed TikZ from the active graph but
  changed 271 pages to 270 and added a bad-break warning. It was fully rolled back
  rather than retuning visible layout for a benchmark.
- A separate chapter-preview entry point was rejected because the measured
  student chapter edit was about 1.45 seconds and another mode would add
  numbering/reference risk.
- GitHub Actions cache for `build/` was rejected because the dominant hosted cost
  was the TeX container pull and clean convergence is part of the required proof.
- Changing the runner to Arm was rejected because the selected TeX container did
  not provide a native Arm64 image; architecture labels alone do not prove a
  speedup.
- Replacing retained transitive packages or all remaining `ifthen` calls was
  rejected without a bounded behavior and output contract.

### Deferred and inactive

Class/package redesign, `l3build`, `latex-dev`, engine migration, broad control-flow
rewrites, and tagged-PDF/PDF-UA work are not active requirements. Each needs a
new owner-approved Intent, representative fixtures, and its own release boundary.

## Maintenance rule

For every future output-sensitive slice:

1. add or extend the focused fixture before the source change;
2. preserve public declarations and student-owned migration inputs;
3. run focused checks and `just test`/`just ci`;
4. compare page count, text, normalized geometry, fonts, relevant rasters,
   diagnostics, references, and dependencies;
5. verify the exact extracted student package when its surface is touched;
6. keep generated artifacts outside source Git.
