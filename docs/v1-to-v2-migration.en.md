<!-- doc-pair: v1-v2-migration; lang: en; topics: before-you-start,compatibility-first-path,native-v2-path,stable-project-boundaries,corrected-behaviors,date-migration,migrate-another-institution-style-port,portable-verification,compatibility-evidence,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# NCKU Thesis Template 1.x-to-2.x Migration Guide

V2 keeps every declared 1.x command working through a compatibility layer, so
an existing thesis can upgrade the template implementation first, confirm the
output, and adopt the V2 profile architecture at its own pace. This guide is
written for a student mid-migration; how the compatibility promise is
machine-verified is summarized under [Compatibility evidence](#compatibility-evidence)
at the end.

## Before you start

1. Commit or archive the complete working 1.x project.
2. Build the 1.x PDF once more and keep it as the text and visual reference.
3. Record the XeLaTeX version, page count, paper size, cover/oral dates, and
   every deliberately enabled Draft/watermark option.
4. Separate the three kinds of files below; do not overwrite an uncommitted
   thesis directory and expect Git to reconstruct it later.

```text
Student-owned / 學生資料:
  conf/conf.tex
  context/
  figures/
  bibliography data
  local certificate files

Template-owned / 範本實作:
  template/
  fonts/
  build configuration
  packaged examples

Root document / 主文件:
  thesis.tex (merge local edits deliberately / 有意識地merge本地修改)
```

## Compatibility-first path

Use this path for an NCKU thesis already in progress. Preserve `conf/conf.tex`,
content, figures, bibliography data, and local certificate files; replace
template-owned files with the V2 student package and manually merge local
changes to `thesis.tex`. Keep existing helper calls — the V1 adapter loads
automatically and no command needs renaming. Build after each small step and
compare the result with the saved 1.x PDF at the end.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

## Native V2 path

Use this path for a new thesis or a maintained institutional fork. Start from
the V2 student package, copy content, figures, bibliography data, and
certificate files, then re-enter or deliberately merge thesis information in
`conf/conf.tex`. Keep the default `ncku` profile for NCKU work; students from
other institutions create and select exactly one profile by following
[`thesis/template/style/Customization.en.md`](../thesis/template/style/Customization.en.md).
Compatibility helpers may remain throughout 2.x — a source-wide rewrite is
optional. Build after every migration step.

## Stable project boundaries

The following student-facing paths remain stable in 2.x. `conf/` stores
student thesis data only; institution geometry, wording, catalogues, date
rules, and assets live under `template/style/`, and V2 does not introduce
`conf/style.tex`. Documentation language, institution profile, cover language,
degree, and content mode are independent decisions.

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

| Axis | Choices |
| --- | --- |
| Institution | `ncku`, `custom`, or another maintained profile |
| Cover language | `\DisplayCoverInChi`, `\DisplayCoverInEng` |
| Degree | `\MasterDegree`, `\PhdDegree` |
| Content | own context or `\ExampleMode` teaching example |

## Corrected behaviors

This table is the normative migration contract and must be updated in both
languages for every observable helper correction. Compatibility preserves
public APIs, not verified defects.

| 1.x behavior | 2.x behavior | User action |
| --- | --- | --- |
|It wrote an empty reference when the default heading hid its number. |The heading remains visually unnumbered while the label records a stable hierarchy such as `1.1.1.1`; empty-link warnings are rejected. |No source change; existing references become usable. |
|The oral-year getter could mutate thesis-year state. |The getter reads oral state without mutating thesis state; `\SetOralEngDate` keeps oral Taiwan-year state synchronized. | None. |
|The English abbreviation was discarded. |The abbreviation is available through `\GetDeptEngShortName`; the full-name getter is unchanged. |Optionally adopt the new getter. |
|The catalogue contained a spelling error. |The catalogue value is corrected. | Rebuild. |
|The English certificate mixed oral day with cover month/year. |English oral output consistently uses oral metadata. | Students from other institutions automatically receive the correct oral date when using distinct dates. |
|The Doctoral English cover borrowed an oral day not owned by `\SetCoverDate`. |Date tokens are profile-owned; generic/custom uses cover-owned month/year while NCKU explicitly retains its oral-day policy. |No NCKU action; other profiles may customize date tokens. |
|Every degree accepted the generic 2–9 range. |Profile policy clamps NCKU Master to 3–5 and Doctoral to 5–9; neutral/custom remains 2–9. |Select degree before committee size. |
|The theorem label option leaked into visible text and mutable title metadata became blank. |The optional signature is preserved, labels are written correctly, and title metadata is frozen. |No source change; rebuild. |
|Captions wrote mutable temporary tokens to metadata. |Rendered captions are frozen before labels; reference numbers remain unchanged. |Rebuild until auxiliary files converge. |
|Reusable scratch aliases let later setup rewrite earlier numbering and repeated setup appended state. |Configuration is frozen while counter values remain dynamic; repeated setup is idempotent. | Custom numbering users should rebuild generated labels/lists. |
|Counter chains depended on initializer order and cycles could overflow recursively. |Chains resolve to frozen terminals and cycles stop with a deterministic package error. |No source change; rebuild. |
|The two-digit custom font-type value never matched in single-token `\if` dispatch, so font initialization after `\SetCustomEngFontFiles`/`\SetCustomChiFontFiles` was silently skipped and output fell back to engine default fonts. |Font-type dispatch compares complete numeric values with `\ifnum`; the custom type actually loads the configured files from `template/fonts/` and a missing file stops with a deterministic fontspec error. |Projects that call the custom font setters place the font files in `template/fonts/`, or remove those setters to keep default fonts. |

## Date migration

Public setters are unchanged. V2 separates raw input from profile-resolved
display policy: `\GetRequestedCoverYear` / `\GetRequestedCoverMonth` expose
raw `\SetCoverDate` input, `\GetThesisYear` / `\GetThesisMonth` expose
profile-resolved cover values, and oral getters remain independent. NCKU still
makes the oral date authoritative for the cover, preserving NCKU output; a
profile for another institution uses explicit cover year/month and does not
borrow an oral day.

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Institutional forks override `\ApplyOralDatePolicy`, `\ApplyCoverDatePolicy`,
and profile-owned Master/Doctoral date tokens — not the public setters.

## Migrate a style port for another institution

1. Start from `template/style/custom/`; do not copy/load NCKU merely to undo it.
2. Move institution geometry, names, watermark, and date behavior from the old
   custom file into `<profile>/<profile>.tex`.
3. Call exactly one `\RegisterTemplateStyle{<profile>}`.
4. Select the profile with `\TemplateStyleName` in `template/style/style.tex`.
5. Replace old `\SetOralDate` / `\SetCoverDate` overrides with policy hooks.
6. Override `\ApplyCommitteeSizePolicy` only for degree-specific institution
   ranges; keep `\SetCommitteeSize` unchanged.
7. Move cover/oral wording and English cover-date formats to profile token
   setters.
8. Use `\SetCollName` / `\SetDeptName`, or maintain an institution catalogue
   inside the profile.
9. Build cover/certificate cases with deliberately different oral and cover
   dates to prove policy separation.
10. Confirm through `.fls` that no unintended institution asset is loaded.

Detailed guide:
[`thesis/template/style/Customization.en.md`](../thesis/template/style/Customization.en.md)

## Portable verification

Run these commands from an extracted student ZIP or any migrated project root
containing `thesis.tex`. Verify A4 and expected pages; university, college,
department, title, author, and advisor text; cover/oral dates; contents and
references; bibliography convergence; Draft/watermark state; and
representative cover, front-matter, body, and final pages.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Use the saved 1.x PDF as the comparison reference.

## Compatibility evidence

Nothing in this section is required during a migration; it explains how the
compatibility promise is machine-checked in the full Git repository. Three
manifests pin the 1.x public surface and student files:

```text
tests/100-v1-public-api.json                     597 LaTeX/xparse + 65 literal \def declarations
tests/101-v1-comment-environment-artifacts.json  22 declarations from dead comment environments
tests/102-v1-project-migration.json              18 byte-pinned v1.8.2 student files
```

An unchanged 1.x project keeps selecting the default `ncku` profile and
therefore retains the historical NCKU college/department presets, while
`custom` and other institution profiles receive only the generic institution
API. The compatibility layer loads like this:

```text
template/compat/v1.tex
  template/compat/deprecated.tex        23 deprecated-command tombstones
template/style/ncku/ncku.tex            selected NCKU profile
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
template/command/cmd-college.tex        dormant direct-path wrapper
template/command/cmd-department.tex     dormant direct-path wrapper
```

The full repository builds the unchanged v1.8.2 project into the canonical
271-page A4 output, and a StudentMode fixture proves the active content and
all three bibliography databases through `.fls`/`.blg` records. These checks
and manifests are intentionally absent from the student ZIP:

```bash
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
```

The complete gate list and output-identity evidence live in the
[validation and performance record](features/validation-and-performance.en.md).

## Recovery and troubleshooting

If migrated output differs unexpectedly, stop adding changes and keep the old
project and baseline PDF. Classify the change as student data, template-owned
files, or a local `thesis.tex` merge; return to the last buildable commit and
reapply one change at a time. When changing BibTeX style or encountering stale
intermediates, run `latexmk -C thesis.tex` before rebuilding. Do not edit
compatibility manifests, lower expected counts, or disable tests to hide a
difference; a verified behavior correction belongs in the normative table
above.
