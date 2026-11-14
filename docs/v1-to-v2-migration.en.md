<!-- doc-pair: v1-v2-migration; lang: en; topics: before-you-start,compatibility-first-path,new-project-path,stable-project-boundaries,current-helper-behavior,date-configuration,institution-port,build-and-compare,compatibility-boundary,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# NCKU thesis template 1.x-to-2.x migration guide

The automatically loaded compatibility layer preserves declared 1.x public command names and argument shapes throughout 2.x. Upgrade the template, verify output, then adopt institution profiles gradually. A source-wide thesis rewrite is not required.

## Before you start

Keep a complete buildable 1.x project and PDF. Record XeLaTeX version, paper size, page count, cover/oral dates and deliberately enabled watermarks. Separate data from template implementation rather than overwriting the only thesis copy. Back up official school-system certificates and locally added fonts too.

```text
Student-owned:
  conf/conf.tex
  context/
  local figures, bibliography and official certificate files
  locally added fonts under template/fonts/

Template-owned:
  template/ (merge locally added fonts deliberately)
  packaged examples and build configuration

Root document:
  thesis.tex (merge local edits deliberately)
```

## Compatibility-first path

For an NCKU thesis in progress, preserve student data, figures, bibliography and certificates. Update template-owned files from the 2.x student package, deliberately merge `thesis.tex` edits and locally added fonts, and keep existing helper calls. `template/compat/v1.tex` loads automatically. Build after each small step and compare with the saved PDF.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

In Overleaf select XeLaTeX and main document `thesis.tex`. Editors use the same root and a XeLaTeX/BibTeX latexmk chain.

## New-project path

Start from the 2.x student package, copy content, figures, bibliography and certificates, then deliberately merge `conf/conf.tex` data. NCKU projects retain default ncku; students from other institutions create/select one profile using the [customization guide](../thesis/template/style/Customization.en.md). Compatibility helpers remain available throughout 2.x. Copy `context/` with hidden files and relative aliases; see the [writing guide](../thesis/context/README.en.md).

## Stable project boundaries

conf/ holds student thesis data only. Institution geometry, catalogues, dates and assets belong under `template/style/`, never `conf/style.tex`. Documentation language, institution profile, cover language, degree and content mode are independent.

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

| Axis | Choices |
| --- | --- |
| Institution | ncku, custom or another registered profile |
| Cover language | `\DisplayCoverInChi`, `\DisplayCoverInEng` |
| Degree | `\MasterDegree`, `\PhdDegree` |
| Content | own `context/` or the `\ExampleMode` teaching example |

## Current helper behavior

Check these current behaviors and actions after upgrading. Public argument shapes remain compatible; do not rely on incorrect output or effects that an accepted option does not implement.

| Command or feature | Current behavior | Migration check |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}` | Labels retain a stable hierarchy even when the heading hides its number. | Keep calls and rebuild references. |
| `\GetOralYearInTaiwanYear`, `\SetOralEngDate` | Oral state does not mutate thesis-year state; English date input synchronizes oral Taiwan-year state. | Check both oral and cover dates. |
| `\SetDeptName{chi}{short}{full}` | `\GetDeptEngShortName` returns the abbreviation; `\GetDeptEngName` returns the full name. `\SetDeptDPS` uses Department of Photonics. | Check custom metadata and cover output. |
| English oral-certificate date | Uses oral day, month and year. | Do not substitute cover data; students use official system files. |
| English cover date | Generic profiles use cover month/year; NCKU supplies oral-date policy explicitly. | Other institutions customize policy without borrowing unrelated data. |
| `\SetCommitteeSize` | NCKU Master 3–5, Doctoral 5–9; generic/custom 2–9. | Select `\MasterDegree` or `\PhdDegree` first. |
| Theorem title and label | Option signatures remain stable; labels and nameref metadata are retained. | Keep calls and rebuild. |
| Figure, subfigure and table captions | Labels store actual caption text independently of later setup. | Rerun until auxiliary data converges. |
| Custom numbering | Prefixes/separators are fixed while counter values stay dynamic; repeated setup is idempotent. | Rebuild labels and contents. |
| Theorem FollowCounter | Resolves forward/multi-hop chains; cycles stop with an explicit error. | Remove cycles rather than relying on initializer order. |
| `\SetCustomEngFontFiles`, `\SetCustomChiFontFiles` | Configured files are loaded; a missing file produces a fontspec error. | Put fonts in `template/fonts/` or remove custom setters to retain defaults. |

## Date configuration

`\GetRequestedCoverYear`/`\GetRequestedCoverMonth` expose raw input; `\GetThesisYear`/`\GetThesisMonth` expose profile-resolved cover values. Oral state remains independent. NCKU derives the cover from the oral date; generic profiles use explicit cover month/year.

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Profiles use `\ApplyOralDatePolicy`, `\ApplyCoverDatePolicy` and degree date tokens instead of replacing public setters.

## Port another institution's style

1. Start from `template/style/custom/`; do not load NCKU merely to undo it.
2. Put institution geometry, names, watermarks, dates and certificate wording in `<profile>/<profile>.tex`.
3. Call `\RegisterTemplateStyle{<profile>}` exactly once and select it with `\TemplateStyleName` in `template/style/style.tex`.
4. Use policy hooks for dates and degree-specific committee ranges; preserve public `\SetOralDate`, `\SetCoverDate` and `\SetCommitteeSize` signatures.
5. Use generic `\SetCollName`/`\SetDeptName` or an institution-prefixed catalogue. Profiles define entries before student configuration selects one.
6. Test distinct oral/cover dates across languages and degrees. Require a nonempty `.fls` before asserting that unintended institution assets are absent.

Neither custom nor the NTU wiring example guarantees a ready-to-submit profile. Follow the [customization guide](../thesis/template/style/Customization.en.md); current official rules override the template.

## Build and compare

Build from the student project root containing `thesis.tex`. Check A4, expected pages, names, department, advisors, dates, contents, references, bibliography and watermark state. Inspect cover, front matter, body and final pages against the saved 1.x PDF. File creation alone is insufficient.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Overleaf and editors use the same XeLaTeX root and BibTeX workflow; recompile from scratch when necessary.

## Compatibility boundary

Declared 1.x public command/environment names and argument shapes remain available throughout 2.x. Deprecated commands have explicit diagnostics; `\RefTo{label}` remains active. Default ncku preserves existing NCKU presets; other profiles load only the generic metadata contract.

Current output is untagged, without PDF/UA or institution-compliance claims. [Architecture](features/v2-modernization.en.md) explains runtime responsibilities and [validation](features/validation-and-performance.en.md) explains repository checks; student migration does not require repository test tooling.

## Recovery and troubleshooting

If output differs unexpectedly, stop adding changes and preserve the original project/PDF. Identify whether the problem is student data, template files or the `thesis.tex` merge. Return to a buildable version and reapply one change at a time. For stale auxiliary data or a BibTeX style change, run `latexmk -C thesis.tex` before rebuilding. Supply missing custom fonts or remove the custom settings rather than hiding errors. Use the [student troubleshooting guide](../thesis/README.en.md) for other failures.
