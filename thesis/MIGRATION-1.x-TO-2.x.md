# Migrating NCKU Thesis Template Projects from 1.x to 2.x

This guide is maintained alongside v2 implementation. V2 preserves every
explicitly declared 1.x command/environment through the 2.x line, so an
existing project can migrate first and adopt native v2 structure gradually.

## Migration Paths

### Path A: Existing Project, Compatibility First

Use this path when completing a current NCKU thesis:

1. Keep your thesis content, bibliography, figures, and current `conf/conf.tex`.
2. Replace template implementation files with the v2 package while retaining
   your user-owned data/content.
3. Build directly with XeLaTeX/latexmk.
4. Resolve only behavior corrections listed below.
5. Compare cover, front matter, references, page dimensions, and final pages.

The v1 compatibility adapter is loaded by default in v2; helper renaming is not
required.

### Path B: Native V2 Project

Use this path for a new project or a maintained institutional fork:

1. Start from the packaged v2 student project.
2. Copy user content, bibliography entries, and figures.
3. Reapply thesis metadata in `conf/conf.tex`.
4. For a non-NCKU institutional port, create/select a profile under
   `template/style/` following `template/style/Customization.md`.
5. Replace compatibility-only calls gradually using the mapping recorded in
   this guide.
6. Keep the direct XeLaTeX build passing after each migration step.

## Stable Project Boundaries

These paths remain stable in v2:

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

`conf/` remains student thesis data. Institution-level style ports remain under
`template/style/`; v2 does not introduce `conf/style.tex`.

## Public Helper Compatibility

All names and argument shapes recorded in `tests/v1-public-api.json` remain
available throughout 2.x. Native v2 code may delegate those helpers to new
internal mechanisms or profile hooks.

## Corrected Behaviors

This section is normative and must be updated with every observable helper fix.

| 1.x behavior | 2.x behavior | Required user action |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}` wrote an empty reference when the default heading intentionally hid its number. | The heading remains visually unnumbered, while the label records the stable hierarchical value such as `1.1.1.1`; empty-link warnings are rejected. | None; existing references become usable. |
| `\GetOralYearInTaiwanYear` recalculated through thesis state and could change `\GetThesisYearInTaiwanYear`. | The getter reads oral-year state without modifying thesis-year state; `\SetOralEngDate` keeps oral Taiwan-year state synchronized. | None. |
| The second argument of `\SetDeptName{chi}{short}{full}` was discarded. | The short name is stored and available through `\GetDeptEngShortName`; `\GetDeptEngName` still returns the full name. | None; code may optionally use the new getter. |
| `\SetDeptDPS` produced `Departmment of Photonics`. | The visible catalogue value is corrected to `Department of Photonics`. | Rebuild to receive the corrected text. |

## Style-Port Migration

The v1.5.0 intent remains authoritative: a non-NCKU port lives under
`template/style/`. V2 changes the loader so exactly one institution profile is
active, rather than loading NCKU and then layering a custom file over it.

Detailed profile hooks and the custom skeleton will be documented in
`template/style/Customization.md` as implementation lands.

## Verification Checklist

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Then verify:

- A4 page dimensions and expected page count;
- cover/university/college/department/title/author/advisor text;
- oral and cover dates;
- table of contents and all references;
- bibliography convergence;
- no unexpected Draft text or institutional watermark;
- representative rendered cover, front-matter, body, and final pages.

Repository maintainers should additionally run `just ci` and the v1 API gate.
