# V2 Modernization IDSD Brief

Status: Implementation complete on `feat/v2.x`; review pending
Owner: Wen-Gan Li

## Intent

### Goal

Deliver one v2 development line that improves helper correctness and restores a
real non-NCKU style-port boundary while preserving the established NCKU output,
student project shape, and 1.x public command surface.

### Constraints

- Preserve the visible NCKU cover, front matter, body layout, and direct XeLaTeX
  workflow unless a focused fixture proves a bug requires a documented change.
- Keep `thesis.tex`, `conf/conf.tex`, and the packaged top-level student
  structure stable.
- Keep all explicitly declared 1.x commands and environments available through
  the complete 2.x line.
- Keep student thesis data in `conf/`; keep institution-level ports under
  `template/style/`, matching the v1.5.0 `Customization.md` intent.
- Keep standard XeLaTeX and Overleaf builds independent of maintainer tooling.

### Failure Conditions

The outcome fails if any of these occur:

- an entry in `tests/v1-public-api.json` disappears or changes argument shape;
- the default NCKU build changes required text, page dimensions, or visible
  layout without a recorded bug and focused evidence;
- the custom profile must first load NCKU style policy in order to work;
- a v1 project cannot build on v2 through the documented compatibility path;
- migration steps omit a changed behavior or require repository-only tooling.

## Expectations

### Done Means

- The v1 API manifest and unchanged-project migration manifest are enforced by
  `just test`.
- Known helper defects are covered by exact focused fixtures before correction.
- Generic helper/state mechanisms no longer own NCKU college/department data or
  NCKU date policy.
- `template/style/style.tex` loads exactly one selected institution profile.
- The default `ncku` profile reproduces the established NCKU output.
- A neutral `custom` profile compiles without NCKU names, labels, or watermark
  assets in its visible output.
- `thesis/MIGRATION-1.x-TO-2.x.md` covers unchanged-project and native-v2 paths.

### Success Scenarios

1. An existing NCKU student project builds on v2 without renaming its helpers.
2. A corrected helper keeps its public signature and produces the documented
   corrected value.
3. A template maintainer copies or edits a profile under `template/style/` and
   does not need to undo NCKU setter overrides.
4. The canonical NCKU example and focused fixtures pass the same `just ci` gate.

### Recovery Plan

- If a public API gate fails, restore an adapter before continuing the refactor.
- If NCKU output changes unexpectedly, revert the output-sensitive slice and
  reduce it to a focused fixture plus one ownership change.
- If the custom profile leaks NCKU policy, move the dependency behind the NCKU
  profile or explicitly classify it as a temporary v1 compatibility adapter.

### Validation

```bash
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
git status --short
```

For output-sensitive changes, also compare PDF metadata/text and render the
cover plus affected pages.

## Context

### Implemented Evidence

- The immutable pre-v2 tree has 597 runtime-visible LaTeX/xparse
  command/environment declarations plus 65 literal `\def`-style declarations
  captured and enforced by `tests/v1-public-api.json`; 22 declarations found
  inside LaTeX `comment` environments are recorded separately as audit artifacts.
- `tests/v1-project-migration.json` pins 18 student-owned files byte-for-byte to
  v1.8.2. Runtime evidence is split between the unchanged entry/configuration
  build and exact StudentMode content/BibTeX dependency assertions.
- `template/command/command.tex` loads `template/compat/v1.tex`; historical NCKU
  catalogue helpers remain available while their data is owned by
  `template/style/ncku/`. The same adapter loads `template/compat/deprecated.tex`,
  which owns 23 literal zero-argument tombstones and their exact migration
  diagnostics without reviving the commented-out zero-argument `\RefTo` form;
  the active one-argument `\RefTo` remains in `cmd-ref.tex`.
- `template/style/style.tex` dynamically loads exactly one registered profile.
- `template/style/ncku/ncku.tex` implements cover/oral and Chinese-year policy
  through hooks/getters instead of overriding public setters.
- Generic watermark storage is empty; the selected profile owns any text style
  or figure asset.
- Committee-size validation is profile-owned: NCKU enforces Master 3--5 and
  Doctoral 5--9, while the neutral/custom policy retains renderer capacity 2--9.
- `template/style/custom/custom.tex` builds Chinese and English cover/oral pages
  with Gregorian Chinese dates and without NCKU visible policy or watermark
  assets.
- `thesis/template/style/Customization.md` and the v1.5.0 changelog keep
  `template/style/` as the non-NCKU port boundary.

### Open Questions

Open decisions discovered during implementation must be recorded here or in the
migration guide before changing an observable contract. The accepted defaults
are full v1 API compatibility, one selected profile, and no separate v1.9 line.

## Final Validation Evidence

The completed v2 slice plus the full-review repair batch was validated from a
clean committed worktree:

- review-repair implementation head
  `4e036df6dc3a648bf3136a0ea90ecaf75d860dc5` passed exact-SHA Push Test
  `29557691733` and Pull-request Test `29557693565` after four focused commits
  hardened the API scanner, corrected packaged migration commands, required
  exact migration dependency records, and removed duplicate release-test
  execution;
- optimization implementation/docs head
  `b02570d7df37032e86a081e0ac775a299cade203` passed exact-SHA Push Test
  `29559890805` and Pull-request Test `29559892766`; the retained slice removes
  the 12-file legacy `fp` runtime path, uses the already-loaded LaTeX programming
  layer for numeric evaluation, replaces 21 sequential month comparisons with
  one 12-way branch, and declares the required xparse-only `G{...}` dependency
  explicitly;

- `just ci`: pass, including canonical build and all focused fixtures;
- `just release review`: pass after the optimization from a clean committed
  worktree, including the exact student archive and all generated examples;
- v1 API gate: 597/597 LaTeX/xparse declarations and 65/65 literal `\def`-style
  declarations preserved, with 22 audited comment-environment declarations,
  105 primary v2 additions, and 7 literal-def v2 additions;
- API-scanner mutation probes: nested xparse defaults remain brace-balanced,
  optional-first defaults are part of the signature, parity-aware `%` comments
  do not expose dead declarations, dynamic `\def\csname` forms are excluded
  from the literal audit, and baseline regeneration refuses any source other
  than immutable pre-v2 commit `f80a2649232dd25761276ccf7043cf3f3a79e031`;
- deprecated-command contract: all 23 literal zero-argument tombstones are
  compatibility-owned and preserve their exact diagnostics plus `\stop`; the
  live one-argument `\RefTo` keeps its original path/signature while its
  comment-only zero-argument tombstone remains excluded;
- migration source gate: 18 student-owned files (296,726 bytes) match v1.8.2
  exactly;
- migration runtime gates: unchanged entry/configuration plus active StudentMode
  content and all three BibTeX databases pass through v2;
- student-package gate: the ZIP regular-file list exactly matches the tracked
  `HEAD:thesis` tree, including migration/compatibility/profile files; deleting
  the migration guide from a temporary ZIP is detected;
- direct unpacked student ZIP build: all 18 pinned v1 files retain exact
  SHA-256/size and `latexmk -xelatex thesis.tex` produces 271 A4 pages through
  the v1 adapter plus base/NCKU profiles without Draft or template watermark;
- packaged migration/customization instructions distinguish student-project
  root commands from full-repository-only `just`/`scripts`/`tests` tooling and
  verify the direct output at `thesis.pdf` rather than a nonexistent
  `../build/thesis.pdf`;
- migration runtime assertions require complete `.fls`/`.blg` records, so a
  suffix such as `conf.tex.bak` cannot satisfy a declared dependency;
- `just release review`: pass, proving `just release` alone executes its
  declared `test` dependency once and then verifies the two ZIP packages plus
  six generated example PDFs; the Release workflow no longer invokes the same
  full test gate twice;
- canonical NCKU PDF: 271 A4 pages;
- diagnostic budgets: all pass, including zero empty-hyperlink and zero unknown
  CJK-family warnings;
- profile-extraction comparison: canonical extracted text identical, cover word
  count/bounding boxes identical, and 150-DPI cover raster RMSE `0 (0)`;
- custom profile: six A4 pages covering Chinese/English Master cover, Chinese
  oral, both Master/Doctoral English oral branches, and the Doctoral English
  cover; Gregorian Chinese years, distinct `July 2024` cover and
  `31 December 2023` oral dates, no oral-day leakage into the Doctoral cover,
  custom degree display/submission wording, no NCKU visible policy or watermark
  asset, generic committee capacity 2--9, and no clipping or overlap on rendered
  inspection;
- committee policy fixture: six NCKU boundary/interior cases prove Master 3--5
  and Doctoral 5--9 clamping from numeric degree state;
- theorem contract fixture: all 21 public insertion and setter routes compile with
  exact default metadata, numbered/unnumbered text, 15 labels,
  `\ref`/`\nameref`, section reset, proof-marker assertions, and unknown/empty
  setter no-op coverage; the label option no longer leaks into visible text and
  titled labels retain stable nameref metadata;
- theorem registry: one 21-row source owns order, style/numbering policy,
  defaults, key-family declarations, membership, aggregate initialization, and
  default application while literal v1 public adapters remain;
- theorem style/counter matrix: all 21 custom environment/text routes preserve
  plain-versus-definition styles and cover global, Section, custom-counter,
  forward/multi-hop, chained-empty, and optional-type numbering; all 21
  default/setter/counter routes plus self/unknown/empty behavior are asserted;
- theorem cycle fixture: cyclic parents fail with a deterministic package error
  and never reach recursive TeX-capacity overflow;
- float caption contract: single/multi/subfigure and top/bottom/star table paths
  preserve key state, numbering, visible order, and eight literal nameref titles;
  caption wrappers freeze `\@currentlabelname` before writing labels so later
  pgf parses and subfigure scope exit cannot corrupt auxiliary metadata; one
  private framed-content helper now owns the identical figure/multi/table
  minipage and zero-line `mdframed` wrapper with exact focused/canonical output;
- numbering state contract: all eight general/appendix selectors, seven styles,
  dynamic counter mutation, fallback references, F/T/E output, and unknown/empty
  no-ops pass; parsed prefixes/separators/counter names are frozen, counter values
  remain dynamic, and repeated appendix equation setup stays `2.8` instead of
  accumulating `2.82.8`;
- generated NCKU English oral comparison: extracted text, word coordinates, and
  150-DPI raster remain identical after submission-text token extraction.

## Progress

- [x] Create and enforce the v1 command/environment baseline.
- [x] Pin and build the unchanged v1.8.2 student-project inputs on v2.
- [x] Add exact helper contract fixtures.
- [x] Correct the first verified helper defects.
- [x] Add the v1 compatibility adapter and style profile contract.
- [x] Consolidate the 23 deprecated public-command tombstones behind a focused compatibility contract.
- [x] Extract NCKU policy/data and add a neutral custom profile.
- [x] Complete migration and customization documentation.
- [x] Run final compatibility, PDF, and rendered-page validation.
