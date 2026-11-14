<!-- language: en; summary: validation-and-performance.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# Validation and performance

The validation system checks public compatibility, output, student portability and packaging. Current source, fixtures and `justfile` define the executable contracts.

## Run the checks

From the repository root:

```bash
python3 scripts/test/check-bilingual-docs.py
python3 scripts/test/check-test-layout.py
python3 scripts/test/check-v1-api.py
just test
just ci
git diff --check
```

`just test` builds the canonical thesis and runs focused fixtures. `just ci` includes that gate and repository hygiene checks. CI runs `just test`; a local pass does not establish a hosted run or publication.

The [test inventory](../../tests/000-test-suite.md) groups flat, uniquely numbered sources under `tests/`. Focused fixtures are the normal fast gate; the complete teaching document supplies integration coverage.

## Protected behavior

| Concern | Current contract |
| --- | --- |
| Public API and migration | Declared 1.x names/argument shapes, explicit deprecated-command diagnostics, and an unchanged v1.8.2 fixture built through the current runtime |
| Student configuration | Cited conf/conf.tex line numbers still point to the documented commands |
| Canonical output | 261 A4 pages, PDF plus SyncTeX, expected text and dependencies, converged references/citations |
| Institution profiles | Correct load order, one selected profile, independent oral/cover dates, degree-specific policy, no NCKU data/assets in custom output |
| Helpers | Numbering state, theorem counter chains/cycles, reference metadata, float captions/options, fonts, keywords and PDF metadata |
| Diagnostics | Reviewed warning budgets in `scripts/test/check-diagnostics.py`; no unresolved references/citations or rerun-required state |
| Student knowledge | Published guide snippets, English-only agent payload, bounded links, aliases, root discovery and copied-context builds in `scripts/test/check-student-agent-skills.py` |
| Packages | Exact HEAD:thesis inventory and bytes, required members, safe symlink extraction, generated examples and Overleaf cold builds |

Negative cases must fail for their intended reason. Missing recorder files cannot prove dependency absence: require a nonempty `.fls` before testing that an institution asset or teaching file was not loaded. Keep API, archive and page-count assertions meaningful when changing source or fixtures.

Markdown discovery prunes `build/`, `.git/` and symlink directories before descent,
and excludes symlink files. Hidden source documentation remains checked. The
documentation gate tests excluded-directory removal during discovery alongside
live-source validation and error propagation, so parallel package cleanup cannot
race traversal of generated output.

## Check output and portability

For output-sensitive changes, compare page count, text, normalized word coordinates from `pdftotext -bbox-layout`, meaningful `pdffonts` rows and fixed-DPI page renders. Inspect affected covers, front matter, figures and pagination. Raw PDF bytes and unnormalized metadata are not portable identity guarantees across operating systems, TeX Live versions or fonts.

From an extracted student project containing `thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Overleaf uses XeLaTeX and `thesis.tex` as the main document. Editors use the same root and XeLaTeX/BibTeX build chain. Repository `just`, tests and scripts are not student prerequisites. Check the final log and expected content; a PDF alone does not prove convergence.

Archive gates read committed `HEAD:thesis`. If student sources are uncommitted, those gates describe committed package bytes, while working-tree checks describe the edits. [Distribution](release-and-distribution.en.md) defines release and public verification.

## Performance characteristics

Own-thesis mode avoids rebuilding the teaching corpus: comment out `\ExampleMode` and write under `context/`. `latexmk` tracks dependencies and reruns XeLaTeX/BibTeX as needed; `just watch` uses continuous rebuilding. A warm no-change build does less work than a clean build, but its time is not a clean-build benchmark.

Build times depend on document size, figures, bibliography, fonts, hardware, TeX installation and concurrent load. Hosted container startup and Overleaf timeout limits are separate costs. Local timing cannot promise hosted completion or a universal speedup. Preserve clean convergence in required test/release lanes; generated auxiliary state must not substitute for cold-build proof. `JUST_JOBS=1` permits serial execution when diagnosing interleaved fixture failures.

See [student writing and agent skills](student-writing-and-agent-skills.en.md) for the writing-contract coverage and [architecture](v2-modernization.en.md) for runtime responsibilities.
