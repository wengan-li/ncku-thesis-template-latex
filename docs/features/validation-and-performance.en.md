<!-- language: en; summary: validation-and-performance.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# Validation and performance

Status: production evidence consolidated

This record explains how the template is tested, what the canonical outputs
must look like, and which performance decisions were measured rather than
assumed. Deterministic gates come first; dated benchmark and release evidence
follows. When a historical number drifts, current tests and source win.

## How to check a change

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

For an extracted student project, run from the directory containing
`thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

The packaged student project deliberately works without the repository
`justfile`, root tests, scripts, or build directories.

Test sources sit flat under `tests/` with three-digit sparse prefixes.
[`tests/000-test-suite.md`](../../tests/000-test-suite.md) defines the ranges
and separates executable fixtures from `900`-series historical references,
and `scripts/test/check-test-layout.py` rejects unnumbered files, nested test
paths, duplicate numbers, empty reserved groups, and missing layout anchors.

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

## How output identity is proven

Page count and extracted text alone cannot show that a layout stayed
identical, so output-sensitive work layers its proof: normalized
`pdftotext -bbox-layout` word tuples, `pdffonts` tables, fixed-DPI page
rasters, and rendered inspection of the affected pages. Raw bbox HTML is not
byte-stable because PDF metadata such as the creation time changes between
runs.

The V2 profile extraction and the bounded internal refactors retained:

- the canonical 271-page A4 output;
- complete extracted-text identity where output-neutrality was required;
- normalized word-coordinate identity for focused and canonical comparisons;
- fixed-DPI raster identity for all 271 pages during the final command-parser
  migration, plus higher-DPI representative cover, float, theorem, and final
  pages during focused slices;
- meaningful font-table identity for the dependency/performance slice;
- the exact student archive tree and direct-build behavior.

The custom-profile proof covers Chinese/English Master covers, the Chinese
oral certificate, Master/Doctoral English oral branches, and the Doctoral
English cover. It keeps Gregorian custom dates distinct, does not borrow an
oral day into a generic cover, uses custom degree wording without changing
numeric degree semantics, and loads no NCKU watermark asset or
college/department catalogue. The gate requires each `.fls` recorder file to
exist before asserting that those paths are absent.

## v2.0.2 production release read-back

The immutable tag `v2.0.2.260719120024` points to source commit
`077323b1af173cfb564859dd360b959dd58ffaa5`. The exact merged-main Test run
[`29687020022`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/29687020022)
passed before Release workflow
[`29687321505`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/29687321505)
built and promoted exactly two public assets.

Public re-download checks recorded:

```text
ncku-thesis-template-latex-v2.0.2.260719120024.zip
SHA-256 5ddc1e32680c596090a25d1c028abdabd5dd653f754fe03819b64fbc90447079

ncku-thesis-template-latex-examples-v2.0.2.260719120024.zip
SHA-256 fe094390317bdeb23c5d55371e3c263cec06285cd01af4601e60158cd464b108
```

The public bytes matched the successful workflow artifact. The downloaded
student ZIP matched the tagged `thesis/` tree exactly and built with the
packaged canonical `latexmk` command to a 271-page A4 PDF with SyncTeX and
resolved references/citations. The examples ZIP contained exactly its README
plus six expected A4 PDFs:

| PDF | Pages |
| --- | ---: |
| `cover.pdf` | 2 |
| `thesis-chi.pdf` | 11 |
| `thesis-eng.pdf` | 11 |
| `thesis-full.pdf` | 271 |
| `defense-certificate-master.pdf` | 6 |
| `defense-certificate-phd.pdf` | 10 |

Generated defense certificates are template demonstrations and regression
outputs, not official school-system documents.

## v2.0.5 production release read-back

The immutable tag `v2.0.5.260821154358` points to source commit
`9350d1d35e501b20153f293f9057da09576d6643`. The merged-main Test run
[`32499614687`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/32499614687)
passed before Release workflow
[`32499622823`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/32499622823)
built and promoted exactly two public assets. An earlier tag string for this
release failed the merge-aware whitespace gate before packaging (the packaged
licence copy carried the root file's historical trailing whitespace), produced
no release, and was removed; the fix landed through a separate pull request
before the tag above was cut.

Public re-download checks recorded on 2026-08-21:

```text
ncku-thesis-template-latex-v2.0.5.260821154358.zip  (33,372,825 bytes)
SHA-256 116336d4928ed074506b352110deee0150bcf11920eb89e49202760035fe790a

ncku-thesis-template-latex-examples-v2.0.5.260821154358.zip  (20,770,699 bytes)
SHA-256 8d3e7d73c8fda73ba15af5d5556fd1df627910e2fecd8e3d45cb34bf13062b98
```

The public bytes matched the promoted workflow artifact. The downloaded
student ZIP matched the tagged `thesis/` tree exactly, carried the 18 pinned
v1.8.2 student inputs (296,726 bytes, zero mismatches) and the licence text,
and built with the packaged canonical `latexmk` command to a 271-page A4 PDF
with SyncTeX, resolved references/citations, no Draft marker, and no
institutional watermark asset. The examples ZIP contained exactly its README,
`LICENSE`, and six A4 PDFs:

| PDF | Pages |
| --- | ---: |
| `cover.pdf` | 2 |
| `thesis-chi.pdf` | 11 |
| `thesis-eng.pdf` | 11 |
| `thesis-full.pdf` | 271 |
| `defense-certificate-master.pdf` | 6 |
| `defense-certificate-phd.pdf` | 10 |

## Dated performance evidence

Benchmarks describe the host and workload they were measured on; they are not
universal speed promises.

### Initial modernization review

```text
271-page clean build:             31.34 s
271-page warm no-change build:     0.10–0.33 s
271-page real dependency edit:    12.51–12.93 s
11-page student clean build:       3.84 s
11-page student no-change build:   0.07 s
11-page student chapter edit:      1.45 s
```

`latexmk` was already doing correct dependency tracking: the full-corpus edit
cost was XeLaTeX layout and PDF generation, not unnecessary bibliography
runs. Writing with StudentMode (teaching examples disabled) is the primary
speed optimization for a normal thesis, and `latexmk -pvc` adds automatic
rebuilds without weakening final build semantics.

### Dependency simplification measurement

A later same-host experiment compared three student clean runs, five
no-change runs, and alternating isolated preamble runs:

```text
single-pass preamble median: 0.690 s -> 0.673 s (-2.37%)
student cold median:         6.861 s -> 6.685 s (-2.56%)
canonical no-op median:      0.140 s -> 0.141 s (unchanged)
```

The three-run 271-page cold median moved from 30.365 s to 33.694 s under
changing background load — too noisy to claim as a full-corpus speedup. The
retained claim is narrower: fewer dependencies, simpler bounded dispatch,
small isolated/student improvements, and unchanged output.

## Accepted, rejected, and deferred decisions

### Accepted

- Remove the legacy `fp` path for three numeric operations using the already
  loaded LaTeX programming layer. All 12 `fp` inputs (about 117 KB) leave the
  active graph while decimal, negative-modulo, expansion, and group semantics
  remain fixture-protected.
- Replace 21 sequential month comparisons with one native 12-way branch while
  preserving `1`/`01` through `12` and invalid-range empty output.
- Keep `xparse` as an explicit dependency because protected `G{...}`
  signatures are not supplied by the kernel document-command surface.
- Move nineteen repository-owned command parser families to `l3keys` through
  bounded baseline-first slices.
- Keep required Test and Release lanes clean rather than caching auxiliary TeX
  state into correctness gates.
- Build the five standalone release example PDFs concurrently. Each case
  writes only its own jobname files inside the release staging directory, the
  measured cold segment dropped from 24.7 to 15.1 seconds on the reference
  host, and `JUST_JOBS=1` restores serial execution.

### Measured and rejected

- The default non-TikZ `mdframed` renderer removed TikZ from the active graph
  but changed 271 pages to 270 and added a bad-break warning. It was fully
  rolled back rather than retuning visible layout for a benchmark.
- A separate chapter-preview entry point was rejected because the measured
  student chapter edit was about 1.45 seconds and another mode would add
  numbering/reference risk.
- GitHub Actions cache for `build/` was rejected because the dominant hosted
  cost was the TeX container pull and clean convergence is part of the
  required proof.
- Changing the runner to Arm was rejected because the selected TeX container
  did not provide a native Arm64 image; architecture labels alone do not
  prove a speedup.
- Replacing retained transitive packages or all remaining `ifthen` calls was
  rejected without a bounded behavior and output contract.
- Caching the hosted TeX container image was rejected after measuring Test run
  [`32492812318`](https://github.com/wengan-li/ncku-thesis-template-latex/actions/runs/32492812318):
  the `ghcr.io/xu-cheng/texlive-alpine` pull took about 79 seconds of the
  3-minute-51-second job, while an actions/cache round trip for the multi-GB
  image tar plus `docker load` costs comparable time on a hit, pays a
  save/upload penalty whenever the upstream image moves, and would move
  environment plumbing into workflow YAML that deliberately owns environment
  selection and promotion only. A repository-owned slim pinned image remains a
  possible separate Intent.

### Deferred and inactive

Class/package redesign, `l3build`, `latex-dev`, engine migration, broad
control-flow rewrites, and tagged-PDF/PDF-UA work are not active
requirements. Each needs a new owner-approved Intent, representative
fixtures, and its own release boundary.

## Maintenance rule

For every future output-sensitive slice:

1. add or extend the focused fixture before the source change;
2. preserve public declarations and student-owned migration inputs;
3. run focused checks and `just test`/`just ci`;
4. compare page count, text, normalized geometry, fonts, relevant rasters,
   diagnostics, references, and dependencies;
5. verify the exact extracted student package when its surface is touched;
6. keep generated artifacts outside source Git.
