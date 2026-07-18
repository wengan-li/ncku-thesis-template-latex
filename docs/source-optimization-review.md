# XeLaTeX source optimization and modernization review

Status: completed and shipped in [`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231); P3 experiments are deferred and inactive

Checked: 2026-07-18

## Closure

The compatibility-bounded P0--P2 work from this review is complete and its
maintained implementation record now lives under [`features/v2/`](features/v2/).
This document remains the evidence and prioritization record for the measured
modernization work. The P3 ideas below are not active requirements, todos, or
authorization to change the class/package structure, engine, public API, or PDF
accessibility claims; each would require a separate owner-approved Intent and
validation boundary.

The original public Overleaf Gallery template remains published. The V2 update
was submitted through the original project and is still pending Gallery review;
GitHub Releases remains the canonical V2 package until the public Gallery copy
is approved and independently read back.

## Implementation status

- Complete: sectioning/star behavior fixture and fix; core numbering/reference fixture; explicit oral default state; final-log diagnostics baseline; Unicode metadata/bookmark and font/CJK fixtures; continuous preview and student-mode guidance; versioned student/examples release packages; CI cache/runner decision; `iftex`/kernel document-command cleanup with an explicit minimum LaTeX format.
- Complete in v1.8.2: the cover Draft marker, diagonal text watermark, and institutional-logo watermark defaults now match the final-submission guidance; all three layers remain explicit opt-ins with default-off and opt-in regression coverage. Historical evidence and the distribution boundary are recorded in [`draft-watermark-history.md`](draft-watermark-history.md).
- Complete safe P2 simplification: shared figure/table caption-label implementation, shared optional-keyword appending, and removal of commented-out caption/column experiments. Public wrappers and argument signatures remain unchanged.
- Complete theorem hardening and registry consolidation: one 21-row registry owns order, style/numbering policy, default metadata, key families, membership, aggregate initialization, and default application. Literal v1 public insertion/initializer adapters remain. Focused contracts cover all defaults/setters/counter targets, self/unknown/empty behavior, multi-hop and forward chains, optional-type numbering, deterministic cycle rejection, labels/`\ref`/`\nameref`, proof marker, and plain/definition styles. `cmd-theorem.tex` falls from 1,079 to 574 lines (46.8%) with canonical output unchanged.
- Rejected after measurement: a separate chapter-preview entry point, because a real student-mode chapter edit rebuilt in approximately 1.45 seconds and another document mode would add numbering/reference risk.
- Complete: Overleaf publication research/verification, v1.8.1 release, and integration into `main`; the public Gallery template was approved on 2026-07-15.
- Complete in v1.8.2: post-v1.8.1 visible-overflow diagnostics cleanup and final-ready Draft/watermark safe defaults.
- Complete after v1.8.2: all repository-owned GitHub Actions references use their latest stable major versions checked on 2026-07-15 (`actions/checkout@v7`, `actions/upload-artifact@v7`, `actions/download-artifact@v8`, and the already-current `xu-cheng/texlive-action@v3`). The JavaScript actions declare Node.js 24 and remove the runner's Node.js 20 compatibility warning.
- Deferred to later major-version experiments: numbering-format registry rewrites outside theorem handling, class/package redesign, broad `expl3` conversion, `l3build`, engine migration, and tagged-PDF/PDF-UA work. The theorem registry cleanup is complete; its remaining repeated lines are deliberate literal public adapters.

## Intent

Review the complete template for correctness, rewrite-preview performance, maintainability, modern LaTeX practice, and student usability without changing the v1.x contract:

- XeLaTeX remains the required production engine.
- Existing public commands and visible layout remain compatible.
- `thesis.tex` and `conf/conf.tex` remain the student entry points.
- `just test` and `just release` remain the canonical repository gates.
- Final and release builds remain deterministic even if a faster non-final preview path is added.

No official XeLaTeX AI-agent skill is published by the LaTeX Project, XeTeX maintainers, TUG, or CTAN. Third-party prompt packs are not treated as standards. This review uses maintainer-backed documentation from the LaTeX Project, TUG/XeTeX, CTAN package maintainers, and Overleaf.

## Measured baseline

Repository inventory under `thesis/`:

```text
Files:                  203
TeX files:              103
TeX lines:              15,221
Loaded packages:        41
\newcommand:             861
\renewcommand:           151
\def:                     97
\RenewDocumentCommand:     8
\NewDocumentCommand:       0
```

Isolated and local benchmarks agree:

| Scenario | Wall time | Work performed |
|---|---:|---|
| Clean build | 31.34 s | XeLaTeX ×4, BibTeX ×3, xdvipdfmx ×1 |
| Warm build without changes | 0.10–0.33 s | No compiler run |
| Edit to a real dependency in the 271-page example | 12.51–12.93 s | XeLaTeX ×1, xdvipdfmx ×1, BibTeX ×0 |

`latexmk` dependency tracking is working correctly. The rewrite bottleneck in the integration document is full-document XeLaTeX layout and PDF generation, not unnecessary BibTeX runs.

A separate student-facing benchmark used an isolated copy containing only `thesis/`, disabled the standalone `\ExampleMode` command, and invoked `latexmk -xelatex` directly without the repository `justfile` or root `latexmkrc`:

| Student scenario | Wall time | Work performed |
|---|---:|---|
| Clean 11-page thesis build | 3.84 s | XeLaTeX ×3, BibTeX ×2 |
| Warm build without changes | 0.07 s | No compiler run |
| Edit to `context/introduction/introduction.tex` | 1.45 s | XeLaTeX ×1, BibTeX ×0 |

This validates the intended student workflow: disabling `\ExampleMode` is the primary build-time optimization, and continuous `latexmk -pvc` removes manual rebuild steps. A separate chapter-preview entry point is not currently justified because a real student-mode edit already rebuilds in approximately 1.5 seconds; adding another document mode would increase student complexity for little demonstrated benefit.

The full teaching example is intentionally heavy:

```text
Pages:       271
PDF size:    approximately 24.3 MB
Largest embedded example PDF:
             example/appendix/pdf/2012050003-short-a.pdf
             approximately 24.7 MiB
```

Normal students should write with `\ExampleMode` disabled so `context/context.tex` is used instead of the complete teaching and appendix integration document.

## Current strengths

- `template/configure.tex` correctly enforces XeLaTeX and uses `fontspec` plus `xeCJK` for Unicode/OpenType/CJK support.
- Bundled font paths make the student ZIP reproducible across machines.
- `latexmkrc` provides output-directory-safe `TEXINPUTS` and `BIBINPUTS`, SyncTeX, BibTeX orchestration, and bounded reruns.
- The root `justfile` gives local development and GitHub Actions one shared build contract.
- The release workflow builds maintained TeX case entry points rather than copying old PDFs.
- The custom student ZIP contains only the tracked `thesis/` contents and compiles through the direct XeLaTeX/`latexmk` path.
- Command files are already separated by feature even though they are not yet a formal class/package.

## CI cache and runner architecture decision

Status: documented issue; no migration

The required GitHub Actions jobs currently use:

```yaml
runs-on: ubuntu-24.04
```

GitHub documents this standard public-repository label as a four-CPU, 16 GB **x64** runner. Arm64 would require an explicit label such as `ubuntu-24.04-arm`; the workflow is not currently running on Arm.

The repository has no Actions cache entries and does not use `actions/cache`. A measured successful test run took approximately 4 minutes 19 seconds; the TeX action occupied approximately 4 minutes 10 seconds, including approximately 2 minutes to pull `ghcr.io/xu-cheng/texlive-alpine:latest`. The dominant repeat cost is therefore the full TeX Live container pull, not `latexmk` dependency analysis.

Caching `build/` auxiliary files could reduce a clean or edited LaTeX build by tens of seconds, but it would not remove the dominant image pull and would weaken the required proof that a fresh checkout converges without stale `.aux`, `.bbl`, `.toc`, `.fdb_latexmk`, or `.fls` state. The required test and release lanes must remain clean and reproducible, so no LaTeX-output cache migration is planned.

Caching the full Docker image through `actions/cache` is also not adopted: the image is large, cache upload/download and `docker load` can offset the network saving, and it adds storage and invalidation complexity. The small Alpine packages installed by the job take only seconds and are not a meaningful cache target.

An Arm migration is not currently viable with the selected container. Its live image manifest exposes `linux/amd64` and no native `linux/arm64` image. Merely changing `runs-on` would therefore create an architecture mismatch or require emulation; Arm is not assumed to be faster for XeLaTeX.

Revisit this decision only if a smaller, digest-pinned TeX Live 2026 image can be built with both `linux/amd64` and `linux/arm64` variants. Benchmark cold image pull plus `just test` and `just release`, and migrate only if all release gates pass and the total workflow time improves materially enough to justify maintaining the custom image.

Maintainer references:

- GitHub-hosted runner architectures: <https://docs.github.com/en/actions/reference/runners/github-hosted-runners>
- GitHub dependency caching: <https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching>
- `xu-cheng/texlive-action`: <https://github.com/xu-cheng/texlive-action>

## P0 — correctness and regression protection

Do these before simplifying core macros.

### 1. Protect sectioning behavior

`template/command/cmd-chapter.tex` directly replaces `\chapter`, `\section`, `\subsection`, and `\subsubsection` while also managing counters, TOC entries, labels, appendix state, and page numbering.

The starred branches for `\section*`, `\subsection*`, and `\subsubsection*` currently contain no output implementation, so starred headings can disappear silently.

Add focused fixtures before changing behavior:

- starred and non-starred headings;
- TOC inclusion/exclusion;
- `\label` / `\ref` targets;
- appendix numbering;
- page-number transitions;
- duplicate PDF destination detection.

The 271-page example remains an integration test but is not a sufficient macro regression test.

### 2. Protect numbering and references

`template/command/cmd-numbering.tex` contains several coupled parsers/renderers and old disabled implementations. Add exact-output fixtures for chapter, appendix, figure, table, equation, and reference labels before internal consolidation.

### 3. Make oral-certificate state explicit

`template/command/cmd-oral.tex` initializes the document-type flag with a token that is not one of the normal numeric state values. Current `conf.tex` and release entry points overwrite it, masking the state problem.

Add a fixture for the default external-image/no-document path and each explicit legacy template mode, then replace the implicit state with a defined constant without changing public commands.

### 4. Baseline diagnostics

Current builds succeed but report known font/CJK/hyperref/layout warnings, including CJK mono-family and substituted font-shape diagnostics. Record an allowlist/budget first, then reject newly introduced warnings without suddenly treating every historical teaching-example underfull box as fatal.

Add focused fixtures for:

- CJK main, mono, bold, italic, and small-caps fallback behavior;
- Unicode PDF metadata and bookmarks;
- Chinese and English covers;
- external oral-certificate PDF inclusion;
- bibliography path/style;
- long CJK captions and table/figure anchors.

## P1 — safe, high-value improvements

### 1. Add continuous preview UX

Add a repository `just watch` recipe based on the official `latexmk` preview-continuous mode and document equivalent Texmaker/TeXstudio configuration:

```text
latexmk -pvc -synctex=1 -interaction=nonstopmode thesis.tex
```

This does not reduce the measured 12.5-second XeLaTeX work, but it removes manual rebuild/viewer switching and preserves incremental dependency behavior. Final submission still uses `just thesis` / `just test`.

### 2. Keep the teaching example out of normal writing loops

Documentation should clearly tell students to disable `\ExampleMode` when writing their own thesis. The normal `context/context.tex` path is substantially smaller than the 271-page teaching/release integration document.

### 3. Prototype a non-final chapter preview

If normal student documents still rebuild too slowly, prototype a clearly named non-final preview entry point that loads the common preamble and one selected chapter while omitting cover, oral certificate, TOC/lists, bibliography, teaching appendix, and content tests.

The preview must warn that numbering, cross-references, citations, and total pagination can differ. It must never replace final or release gates. Benchmark the fixture before promising a speedup.

### 4. Low-risk platform cleanup

In isolated commits with fixtures and PDF comparison:

- evaluate `ifxetex` → kernel-maintained `iftex` while retaining the XeLaTeX-only contract;
- define a supported minimum LaTeX/TeX Live version, then evaluate removal of the explicit `xparse` package because modern document-command APIs are in the kernel;
- separate display titles containing line breaks from PDF metadata strings;
- define the CJK mono-font policy instead of relying on an unknown family fallback.

## P2 — internal simplification after fixtures

These changes preserve public commands and belong in separate, reviewable commits.

### 1. Numbering registry

`cmd-numbering.tex` has near-duplicate generic and appendix title builders, repeated key families/dispatch, repeated figure/table/equation formatting, and disabled legacy code in the loaded runtime path.

A focused one-page contract now freezes all eight title selectors, default/custom general and appendix titles/getters, fallback subsubsection references, seven counter styles, dynamic counter mutation, general/appendix figure-table-equation output, unknown/empty selector no-ops, and repeated setup. It reproduced two existing state defects: earlier getters retained the final pgf scratch prefix/separator/counter-name aliases, and `\SetupAppendixEquationNumberFormatString` appended without resetting (`2.8` became `2.82.8`). Parsed configuration and counter names are now frozen while counter values remain dynamic; every repeated setup is stable.

The source API scanner strips LaTeX `comment` environments and parity-aware `%` comments, parses nested xparse groups without truncating `O{...}`/`G{...}` specs, and records optional-first LaTeX defaults. Its immutable pre-v2 baseline contains 597 runtime-visible LaTeX/xparse names plus a separate 65-name literal `\def` audit, while `tests/v1-comment-environment-artifacts.json` preserves an explicit audit of 22 dead declarations: 15 comment-only names plus 7 overlaps with live tombstones, including one false extra signature. The three numbering comment blocks and obsolete bibliography block were removed only after this boundary was established. Full registry generation remains deferred; the numbering correction and dead-code cleanup are compatibility-bounded and fixture-backed.

### 2. Theorem registry

`cmd-theorem.tex` now has one declarative 21-row source for type order, `plain`/`definition` style, numbered/optional policy, default environment/display/counter metadata, pgf key-family declaration, membership, aggregate initialization, and default application. Counter routing resolves Section, registered forward references, and multi-hop chains recursively to a frozen terminal value while preserving arbitrary existing LaTeX counters; cycles produce a deterministic package error. Optional types stay starred when empty and become global/scoped numbered forms when configured.

All established public insertion and initializer commands remain literally declared as compatibility adapters, including the 13 v1 counter getters required by the source-level API manifest. Those getters were historically discoverable only through repeated literal `\renewcommand` branches, so registry generation alone was not source-compatible. Runtime gates cover all 21 defaults, setter routes, counter targets, self/unknown/empty behavior, multi-hop chains, optional numbering, labels/references, styles, and cycle rejection. The file is 505 lines smaller while canonical thesis text, normalized bbox word tuples, theorem-page rasters, and the pre-registry contract raster remain identical. No further theorem-internal consolidation is planned.

### 3. Shared float internals

`cmd-figure.tex`, `cmd-figures.tex`, and `cmd-table.tex` repeat float/minipage/frame/opacity behavior and currently force `[H]` while retaining compatibility keys that do not affect placement.

A focused one-page contract now covers single/multi/subfigure paths, all numbered labels and names, top/bottom/star table forms, key-state/no-op placement, four embedded images, and visual order. It reproduced an existing caption-metadata defect: mutable pgf caption tokens were written to `\@currentlabelname`, so later parsing changed names and a closed subfigure scope made `\nameref` fail with an undefined `\TmpMISubValueCaption`. Caption wrappers now freeze the title after `\caption`/`\caption*` and before `\label`; the auxiliary file contains literal names.

The identical full-width minipage plus zero-line `mdframed`/opacity wrapper is now owned by one private helper and reused by `\InsertFigure`, `\InsertFigures`, and the public `\DisplayTableContent` adapter. The public float commands and signatures, forced `[H]` placement, inactive `pos`/`align` compatibility keys, row dispatch, transforms, table scaling/spacing, and caption order remain unchanged. Against the corrected pre-refactor fixture, layout text, normalized bbox word tuples, four-image inventory, and 180-DPI raster are identical; canonical text/bbox and float pages 82/258--261 are also unchanged.

### 4. Small duplicate helpers

- Completed: repeated keyword accumulation now routes through one private helper while preserving append-not-replace semantics.
- Completed: 23 deprecated zero-argument public-command tombstones now live literally in `template/compat/deprecated.tex`; the focused contract preserves every diagnostic and `\stop`, while the active one-argument `\RefTo` remains in `cmd-ref.tex`.
- Completed: the three `fp` calculations now use the LaTeX programming layer
  already loaded by the template. Decimal Taiwan-year and negative-modulo
  semantics are fixture-protected, all 12 `fp` package inputs leave the active
  graph, and no replacement package is added. `\GetMonthInEng` now uses one
  native 12-way branch table instead of 21 sequential `ifthen` comparisons;
  leading-zero months, invalid ranges, canonical text/bbox, and reviewed rasters
  remain identical.
- Completed: `\SetDeptName{chi}{short}{full}` stores the second argument, `\GetDeptEngShortName` exposes it, and `\GetDeptEngName` continues to return the full name.
- Completed on the v2 profile branch: committee-size validation is profile-owned;
  NCKU uses Master 3--5 and Doctoral 5--9, while neutral/custom keeps the generic
  2--9 renderer capacity. A focused boundary fixture rejects future drift.

## P3 — inactive major-version experiments

These are research directions, not active requirements or todos. Do not mix
them into v2 maintenance; each requires a separate owner-approved experiment.

### 1. Formal class/package structure

Evaluate a future `nckuthesis.cls` that loads `report` and separates layout policy, metadata, optional feature packages, and a v1 compatibility adapter. Keep the direct student workflow and old commands for at least one major compatibility cycle.

### 2. Typed modern internals

For new major-version internals, evaluate `expl3`, `l3keys`, and structured messages instead of global temporary macros, `pgfkeys`, long `ifthen` state machines, and raw `\errmessage` tombstones.

### 3. `l3build` regression harness

The LaTeX Project's `l3build` is suitable for `.lvt/.tlg` macro regression and PDF-based tests. Pilot it behind `just test`; do not replace the student build command or force package-development tooling into the student ZIP.

Add a scheduled/non-blocking `latex-dev` lane to observe upcoming kernel compatibility while keeping pinned TeX Live 2026 as the required release lane.

### 4. Tagged PDF and accessibility

Current output is untagged. Do not claim PDF/UA compliance.

A future isolated experiment may evaluate LuaLaTeX plus `\DocumentMetadata` before `\documentclass`, representative cover/TOC/abstract/table/figure/bibliography fixtures, alt-text semantics, structural validation, and assistive-technology review. External/scanned PDFs do not become accessible merely because the parent PDF is tagged.

## Changes not recommended for rewrite speed

- Do not change the production engine solely for speed without font/layout compatibility evidence.
- Do not disable BibTeX or reduce `latexmk` rerun limits; that creates stale references.
- Do not convert every `\input` to `\include`/`\includeonly` without a chapter-boundary and auxiliary-reference migration design.
- Do not treat graphics draft mode as a final build.
- Do not precompile the preamble before measuring whether its complexity and cache invalidation are worth the maintenance cost.
- Do not rewrite all legacy commands to `expl3` in one change.

## Completed execution order and deferred boundary

1. Completed: sectioning, numbering/reference, oral-state, metadata, and
   font/CJK fixtures.
2. Completed: `just watch` and editor documentation.
3. Measured and rejected: an optional non-final chapter preview did not justify
   its additional numbering/reference risk.
4. Completed: isolated low-risk engine/metadata/font cleanup.
5. Completed: small-helper consolidation and dead private-code removal.
6. Completed: bounded numbering, theorem, and float hardening with PDF/text
   baselines.
7. Deferred and inactive: class/package, `l3build`, `latex-dev`, and tagged-PDF
   experiments.

## Acceptance gates for every implementation slice

- Preserve public command signatures unless a major-version migration explicitly says otherwise.
- Run focused fixtures and `just test`.
- Run `just release` when release-facing code is touched.
- Compare page count, A4 dimensions, extracted text, relevant rendered pages, warnings, references, and PDF destinations.
- Test the direct student ZIP/compiler path when student-facing files change.
- Keep the worktree clean and the branch diff free of generated artifacts.

## Maintainer-backed references

- XeTeX / TUG: <https://tug.org/xetex/>
- `fontspec` / CTAN: <https://ctan.org/pkg/fontspec>
- `latexmk` / CTAN: <https://ctan.org/pkg/latexmk/>
- `l3build` / LaTeX Project: <https://ctan.org/pkg/l3build>
- LaTeX Project, package/class author guide: <https://www.latex-project.org/help/documentation/clsguide.pdf>
- LaTeX Project, hook management: <https://www.latex-project.org/help/documentation/lthooks-doc.pdf>
- LaTeX Project, tagged PDF guidance: <https://www.latex-project.org/news/2024/07/08/tagging/>
- Overleaf compile-time guidance: <https://docs.overleaf.com/troubleshooting-and-support/fixing-and-preventing-compile-timeouts>
