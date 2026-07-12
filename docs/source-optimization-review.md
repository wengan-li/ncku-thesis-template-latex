# XeLaTeX source optimization and modernization review

Status: reviewed; implementation not started

Checked: 2026-07-12

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

Keep `\SetNumberingFormat[...]` and all existing key names, but drive the internals from one type-to-counter/format schema.

### 2. Theorem registry

`cmd-theorem.tex` duplicates setup, key parsing, initialization, and dispatch across approximately 21 theorem types. Replace the internal repetition with a declarative registry containing name, style, counter, and numbered/un-numbered policy. Preserve public aliases such as `\InsertTheorem` and `\InsertDefinition`.

### 3. Shared float internals

`cmd-figure.tex`, `cmd-figures.tex`, and `cmd-table.tex` repeat float/minipage/frame/opacity behavior and currently force `[H]` while retaining compatibility keys that do not affect placement.

Extract a private framed-content helper. Preserve all public signatures. Keep historical no-op keys documented as compatibility behavior; making placement keys active is a separate visible-layout change.

### 4. Small duplicate helpers

- Consolidate repeated keyword accumulation behind one private helper while preserving append-not-replace semantics.
- Move deprecated public-command tombstones into one compatibility module; remove only truly unreachable private dead blocks.
- Replace isolated `fp`/long `ifthen` calculations only when exact-output fixtures exist.
- Document that the second abbreviation argument to `\SetDeptName` is currently ignored rather than silently changing the public signature.
- Reconcile the committee-size implementation range with the teaching text.

## P3 — major-version experiments

Do not mix these into v1.x maintenance.

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

## Recommended implementation order

1. Add sectioning, numbering/reference, oral-state, metadata, and font/CJK fixtures.
2. Add `just watch` and editor documentation.
3. Benchmark an optional non-final chapter preview.
4. Apply isolated low-risk engine/metadata/font cleanup.
5. Consolidate small helpers and dead private code.
6. Refactor numbering, theorem, and float internals one subsystem at a time with PDF/text baselines.
7. Evaluate class/package, `l3build`, `latex-dev`, and tagged-PDF work only on a major-version experiment line.

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
