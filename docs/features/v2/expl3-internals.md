# Incremental `expl3` Internal Modernization

Status: first six bounded slices implemented and validated; pending review

## Intent

Modernize legacy internal control flow only where the behavior is finite, already
fixture-protected, and output-neutral. Preserve the complete audited 1.x public
API through the 2.x line, direct XeLaTeX student builds, TeX Live 2026,
Overleaf compatibility, and canonical PDF output.

This is not approval for a repository-wide rewrite, a class/package redesign,
LuaLaTeX migration, or a blanket `pgfkeys`/`ifthen` conversion.

## Starting evidence

The first audit used immutable baseline
`a7950358b017e2dc813d137c1a8a193a3d1f5704` and found:

- 187 literal `\ifthenelse` calls across 24 active template files;
- 58 `\pgfkeys`/`\pgfkeysvalueof` references across seven files;
- 49 document-command declarations, including protected 2.x compatibility
  signatures that still require explicit `xparse` for `G{...}` arguments;
- direct `etoolbox` helpers in numbering code, while `mdframed` also keeps
  `etoolbox` in the active package graph transitively;
- `expl3`, `ifthen`, `pgfkeys`, `xparse`, and `etoolbox` active in the canonical
  `.fls`; legacy `fp` and vendored `apptools` absent.

The LaTeX Project's [`interface3` reference](https://mirror.math.princeton.edu/pub/CTAN/macros/latex/required/l3kernel/interface3.pdf),
released 2026-06-18, defines `\str_case_e:nn` as a fully expanding string-case
dispatch that does nothing when no case matches. Those semantics match the
existing counter-style dispatcher: style names can arrive through pgf-stored
macros, while unknown or empty styles are deliberate no-ops.

## Candidate decisions

### Selected: bounded counter-style dispatch

`\AppendCounterStringToFormatString` had seven sequential
`\ifthenelse{\equal{...}{...}}` branches for:

```text
ChiNum / Tiangan / Arabic / LowerRoman / UpperRoman / LowerAlph / UpperAlph
```

The implementation now uses one `\str_case_e:nn` table. The public command name,
three-argument LaTeX signature, formatter helpers, dynamic counter behavior, and
unknown-style no-op are unchanged. The focused test also rejects a return to
sequential `ifthen` dispatch.

### Selected follow-up: single-figure key parsing

The seven-key `/InsertFigure` family was the smallest independently reversible
`pgfkeys` candidate. Before changing its implementation, the float fixture froze
all literal defaults, expanded macro-valued storage, reset-on-repeat behavior,
and unknown-key hard-error behavior behind one private parser seam.

The family now uses `\keys_define:nn`, `\keys_set:nn`, and seven
`.tl_set_e:N` properties. This preserves the original `.estore in` expansion
semantics and existing `\TmpValue...` scratch macros. The public
`\InsertFigure` name, `[2][\empty]` signature, key names, fixed `[H]` placement,
caption/label rendering, and deliberately inactive `pos`/`align` compatibility
keys are unchanged.

### Selected follow-up: single-table key parsing

The eight-key `/InsertTable` family was selected only after the same parser-first
method froze literal defaults, expanded macro-valued storage, reset-on-repeat,
and unknown-key hard-error behavior under `pgfkeys`. Existing float coverage
already protected top and bottom captions, unnumbered nomenclature titles,
scaled and unscaled content, labels, references, and fixed `[H]` placement.

The parser now uses a separate `ncku / insert-table` `l3keys` family with eight
`.tl_set_e:N` properties. The public `\InsertTable` name, `[2][\empty]`
signature, all key names/defaults, `\TmpValue...` scratch macros, caption and
`nomtitle` ordering, table dimensions, and rendering branches are unchanged.

### Selected follow-up: theorem-content key parsing

The two-key `/InsertTheoremOptions` family was selected instead of the more
coupled multi-figure parser. The existing theorem fixture already exercises all
21 public insertion helpers, named and unnamed forms, numbered and unnumbered
environments, labels, references, `nameref`, section resets, styles, and counter
routing. A private seam first froze literal defaults, expanded macro-valued
storage, reset-on-repeat, and unknown-key hard-error behavior under `pgfkeys`.

The content parser now uses a separate `ncku / insert-theorem` `l3keys` family
with two `.tl_set_e:N` properties. Public insertion commands, optional argument
signatures, `title` and `label` names/defaults, `\TmpValueTitle` and
`\TmpValueLabel`, title metadata freezing, proof markers, and rendering are
unchanged. The dynamic theorem-format registry and counter-routing families
remain on `pgfkeys`; this slice does not combine those independent state
machines.

### Selected follow-up: reference setup key parsing

The two-key `/SetupReference` family was selected after repository and runtime
audits confirmed that no active source or generated `.fls` loads deprecated
`l3keys2e`. Before replacement, a private seam froze the default English
`References` title, `plain` style, expanded macro-valued storage,
reset-on-repeat, and unknown-key hard-error behavior under `pgfkeys`.

The parser now uses a separate `ncku / setup-reference` `l3keys` family with
`Title` and `BibStyle` `.tl_set_e:N` properties. The public
`\SetupReference` signature, `\GetReferenceTitle` and
`\GetReferenceBibStyle` storage, `\ReferencesFiles` renderer, BibTeX resource
handling, and `BibStyle=apacite` preamble side effect remain unchanged. A
dedicated fixture proves that `apacite` still loads with `notocbib`.

This command-level parser uses `l3keys` directly. It does not use or require
`l3keys2e`; current LaTeX package/class option processing would instead use the
kernel `\DeclareKeys`, `\ProcessKeyOptions`, and `\SetKeys` surface when that
becomes relevant.

### Selected follow-up: custom-font filename key parsing

The four-key `/ParseCustomFontFiles` family was selected separately from the
font-loading `/ParseFontOption` family. Before replacement, a private seam and
focused fixture froze empty defaults, expanded macro-valued filenames, both
English and Chinese public setter routes, custom-type selection, repeated calls,
and unknown-key hard errors.

The legacy public filename macros deliberately retain references to the four
shared scratch values rather than snapshots. Consequently, a later partial,
Chinese, or omitted setter call can change values previously exposed through an
English setter. This surprising alias behavior is preserved by this parser-only
slice; correcting it requires a separate behavior-change intent and migration
contract.

The parser now uses `ncku / custom-font-files` with four `.tl_set_e:N` keys and
explicit per-call scratch clearing. `\SetCustomEngFontFiles`,
`\SetCustomChiFontFiles`, `\SetFontUseType`, every custom filename macro, and
the font initialization/rendering path remain unchanged. `/ParseFontOption`
continues to use `pgfkeys` and is outside this slice.

### Retained: explicit `xparse`

The LaTeX kernel provides modern document-command interfaces, but it deliberately
does not provide all legacy `xparse` argument types. Protected 2.x commands still
use `G{...}` signatures, so removing explicit `xparse` would make compatibility
transitive and fragile rather than modern.

### Deferred: broad `ifthen` conversion

After this slice, 180 literal `\ifthenelse` calls remain across independent
cover, chapter, float, bibliography, font, theorem, oral, and style behavior.
They do not form one bounded state machine. Each future conversion needs its own
fixture and visible-output proof; a mechanical global rewrite is rejected.

### Deferred: remaining `pgfkeys` families

Only the single-figure, single-table, theorem-content, reference-setup, and
custom-font filename families moved. The remaining 42 literal
`\pgfkeys`/`\pgfkeysvalueof`
references span four files and expose different defaulting, storage,
repeated-setup, rendering, and unknown-key behavior. No multi-figure, dynamic
theorem-format, remaining font-loading, or numbering key family is approved for
conversion without its own frozen contract and output proof.

### Retained: `etoolbox`

Replacing one direct helper would not remove the package because `mdframed`
loads it transitively, and numbering still uses its append and boolean-expression
helpers. No dependency-removal benefit is claimed.

## Compatibility expectations

The slice must preserve:

1. the audited public declaration and three-argument signature;
2. all seven counter styles;
3. full expansion of macro-valued style names;
4. unknown and empty style no-ops;
5. dynamic counter values and frozen counter names;
6. default/custom general and appendix title/getter output;
7. figure/table/equation numbering idempotence;
8. 271-page A4 canonical output, text, bounding boxes, fonts, and all-page
   fixed-DPI raster output;
9. V1 API and unchanged-project migration contracts;
10. the existing package graph boundary: `ifthen` remains active and no new
    package is added.

## Validation result

The retained implementation passed:

- focused one-page numbering contract;
- all seven style markers, macro-valued styles, unknown no-op, dynamic counters,
  repeated setup, and figure/table/equation idempotence;
- focused text, normalized bounding boxes, font table, and 200-DPI raster
  identity against the baseline;
- fresh `just ci`, including V1 API, unchanged-project migration, diagnostics,
  student archive, engine, metadata, font/CJK, student-mode, watermark, float,
  theorem, and custom-style gates;
- canonical 271-page A4 text identity;
- canonical normalized bounding-box and font-table identity;
- identical 120-DPI raster output for all 271 canonical pages, plus identical
  150-DPI representative rasters for pages 1, 2, 82, and 258--261;
- active-graph assertions: `expl3`, `ifthen`, `pgfkeys`, and `xparse` active;
  `fp` and `apptools` absent.

The local source delta is seven fewer `\ifthenelse` calls in
`cmd-numbering.tex` (15 to 8), one new bounded `expl3` string case, no public API
change, and no PDF-output change.

### Follow-up `l3keys` validation result

The single-figure parser replacement passed:

- the existing custom-value float contract plus new default, macro-expansion,
  reset-on-repeat, and unknown-key hard-error contracts;
- focused one-page text, normalized bounding-box, font-table, and 200-DPI raster
  identity against the same fixture running the original `pgfkeys` parser;
- fresh exact-HEAD `just ci`, including the V1 API, unchanged-project migration,
  diagnostics, negative-key, student archive, float, theorem, font/CJK,
  student-mode, watermark, and custom-style gates;
- canonical 271-page A4 text, normalized bounding-box, and font-table identity;
- identical 120-DPI raster output for all 271 canonical pages;
- successful `just release review` package generation and verification;
- a repo-external build of the generated student ZIP using the documented
  `latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex` command,
  producing 271 A4 pages, SyncTeX, and resolved references.

`pgfkeys` remains intentionally active because other template files still use it
and PGF/TikZ also remains part of the rendering stack. This slice claims one
bounded family migration, not package removal.

### Single-table `l3keys` validation result

The table parser replacement passed:

- original-implementation defaults, macro-expansion, reset-on-repeat, and
  unknown-key hard-error baseline contracts;
- top, bottom, numbered-caption, unnumbered-`nomtitle`, scaled/unscaled,
  label/reference, spacing, and opacity float contracts;
- focused one-page text, normalized bounding-box, font-table, and 200-DPI raster
  identity against the same fixture using the original `pgfkeys` parser;
- fresh exact-HEAD `just ci`, including V1 API, unchanged-project migration,
  diagnostics, negative-key, student archive, float, theorem, font/CJK,
  student-mode, watermark, and custom-style gates;
- canonical 271-page A4 text, normalized bounding-box, and font-table identity;
- identical 120-DPI raster output for all 271 canonical pages;
- successful `just release review` package generation and verification;
- a repo-external documented `latexmk -xelatex` build of the generated student
  ZIP, producing 271 A4 pages, SyncTeX, and resolved references.

After the two key-family slices, 52 literal `pgfkeys` references remain across
five active template files. No package-removal claim is made.

### Theorem-content `l3keys` validation result

The theorem-content parser replacement passed:

- original-implementation defaults, macro-expansion, reset-on-repeat, and
  unknown-key hard-error baseline contracts;
- all 21 public insertion helpers, named/unnamed and numbered/unnumbered forms,
  15 labels, references, `nameref`, section reset, proof marker, setter routes,
  custom styles, counter chains, and deterministic cycle diagnostics;
- focused one-page text, normalized bounding-box, font-table, and 200-DPI raster
  identity against the same fixture using the original `pgfkeys` parser;
- fresh exact-HEAD `just ci`, including V1 API, unchanged-project migration,
  diagnostics, all negative-key gates, student archive, float, theorem matrix,
  font/CJK, student-mode, watermark, and custom-style gates;
- canonical 271-page A4 text, normalized bounding-box, and font-table identity;
- identical 120-DPI raster output for all 271 canonical pages;
- successful `just release review` package generation and verification;
- a repo-external documented `latexmk -xelatex` build of the generated student
  ZIP, producing 271 A4 pages, SyncTeX, and resolved references.

After the three key-family slices, 49 literal `pgfkeys` references remain across
five active template files. The two dynamic theorem-registry references remain
intentionally active. No package-removal claim is made.

### Reference-setup `l3keys` validation result

The reference parser replacement passed:

- original-implementation defaults, macro-expansion, reset-on-repeat, and
  unknown-key hard-error baseline contracts;
- public custom title/style state and a rendered BibTeX bibliography;
- a separate `apacite[notocbib]` package-load and state contract;
- focused one-page text, normalized bounding-box, font-table, and 200-DPI
  raster identity for both the BibTeX and `apacite` fixtures;
- fresh exact-HEAD `just ci`, including V1 API, unchanged-project migration,
  diagnostics, all negative-key gates, student archive, float, theorem matrix,
  font/CJK, student-mode, watermark, and custom-style gates;
- canonical 271-page A4 text, 40,823 normalized bounding-box words, and
  font-table identity;
- identical 120-DPI raster output for all 271 canonical pages;
- successful `just release review` package generation and verification;
- a repo-external `latexmk -xelatex` build of the generated student ZIP,
  producing 271 A4 pages, SyncTeX, and resolved references;
- zero `l3keys2e` references in active student source and zero `l3keys2e`
  runtime loads across generated `.fls` files.

After the four key-family slices, 46 literal `pgfkeys` references remain across
four active template files. PGF/TikZ still loads `pgfkeys` at runtime, so no
package-removal claim is made.

### Custom-font filename `l3keys` validation result

The custom-font filename parser replacement passed:

- original-implementation empty defaults, macro expansion, custom-type
  selection, both public setter routes, repeated calls, shared-scratch alias
  behavior, and unknown-key hard-error contracts;
- focused one-page text, bounding-box XML, font-table, and 200-DPI raster
  identity against the same fixture using the original `pgfkeys` parser;
- fresh exact-HEAD `just ci`, including V1 API, unchanged-project migration,
  diagnostics, all negative-key gates, student archive, float, theorem matrix,
  font/CJK, student-mode, watermark, and custom-style gates;
- canonical 271-page A4 text, 40,823 normalized bounding-box words, and
  font-table identity;
- identical 120-DPI raster output for all 271 canonical pages;
- successful `just release review` package generation and verification;
- a repo-external `latexmk -xelatex -synctex=1` build of the generated student
  ZIP, producing 271 A4 pages, SyncTeX, and resolved references;
- zero `l3keys2e` references in active student source and zero `l3keys2e`
  runtime loads across generated `.fls` files.

After the five key-family slices, 42 literal `pgfkeys` references remain across
four active template files. The separate `/ParseFontOption` font-loading family
and all other deferred families remain unchanged.

## Next research slice

Do not continue by count alone. Rank candidates by removable dependency cost,
finite semantics, existing fixture coverage, and output risk. Before another key
family moves, capture its default, macro-expansion, unknown-key, repeated-setup,
and rendering contract under the current implementation. Otherwise prefer
another finite `ifthen` dispatcher. `/ParseFontOption` is the adjacent candidate,
but it must remain separate because it directly configures `fontspec` and
`xeCJK`; require explicit English/CJK optional-face and font-table coverage
before considering implementation. Keep every slice independently revertible.
