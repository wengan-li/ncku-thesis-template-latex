# Incremental `expl3` Internal Modernization

Status: first bounded slice implemented and validated; pending review

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

### Deferred: `pgfkeys` to `l3keys`

The seven key families expose different defaulting, storage, repeated-setup, and
unknown-key behaviors. Migrating one family is justified only after freezing its
complete parse and error contract. This slice does not change key parsing.

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
8. 271-page A4 canonical output, text, bounding boxes, fonts, and representative
   rasters;
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
- identical 150-DPI rasters for pages 1, 2, 82, and 258--261;
- active-graph assertions: `expl3`, `ifthen`, `pgfkeys`, and `xparse` active;
  `fp` and `apptools` absent.

The local source delta is seven fewer `\ifthenelse` calls in
`cmd-numbering.tex` (15 to 8), one new bounded `expl3` string case, no public API
change, and no PDF-output change.

## Next research slice

Do not continue by count alone. Rank candidates by removable dependency cost,
finite semantics, existing fixture coverage, and output risk. A small isolated
`pgfkeys` family may be the next research target only after its default,
macro-expansion, unknown-key, and repeated-setup contract is captured; otherwise
prefer another finite `ifthen` dispatcher. Keep each slice independently
revertible.
