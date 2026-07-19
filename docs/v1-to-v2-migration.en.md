<!-- doc-pair: v1-v2-migration; lang: en; topics: before-you-start,compatibility-first-path,native-v2-path,stable-project-boundaries,public-helper-compatibility,byte-identical-v1-project-gate,v1-adapter-layout,corrected-behaviors,date-migration,migrate-another-institution-style-port,portable-verification,repository-verification,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# NCKU Thesis Template 1.x-to-2.x Migration Guide

Production target：[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

V2 preserves the machine-audited 1.x LaTeX/xparse and literal `\def` declaration surfaces through the complete 2.x line. Existing projects can migrate template implementation first, verify NCKU output, and adopt native V2 profiles gradually.

## Before you start

1. Commit or archive the complete working 1.x project.
2. Build the 1.x PDF once more and retain it as a text/visual reference.
3. Record the XeLaTeX version, page count, paper size, cover/oral dates, and every deliberately enabled Draft/watermark option.
4. Separate student data, template implementation, and the root document. Do not overwrite an uncommitted thesis directory and expect Git to reconstruct it later.

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

Use this path for an NCKU thesis already in progress. Preserve `conf/conf.tex`, content, figures, bibliography data, and local certificate files; replace template-owned files with the V2 student package and manually merge local changes to `thesis.tex`. Keep existing helper calls; the V1 adapter loads automatically. Build after each small step and compare the result with the saved 1.x PDF.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

No helper rename is required.

## Native V2 path

Use this path for a new thesis or a maintained institutional fork. Start from the V2 student package, copy content, figures, bibliography data, and certificate files, then re-enter or deliberately merge metadata in `conf/conf.tex`. Keep the default `ncku` profile for NCKU work; another institution creates and selects exactly one profile by following [`thesis/template/style/Customization.en.md`](../thesis/template/style/Customization.en.md). Compatibility helpers may remain throughout 2.x; a source-wide rewrite is optional.

Build after every migration step.

## Stable project boundaries

The following student-facing paths remain stable in 2.x. `conf/` stores student thesis data only. Institution geometry, wording, catalogues, date rules, and assets remain under `template/style/`; V2 does not introduce `conf/style.tex`. Documentation language, institution profile, cover language, degree, and content mode are independent decisions.

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

## Public helper compatibility

The full Git repository's `tests/100-v1-public-api.json` records 597 runtime-visible 1.x LaTeX/xparse commands/environments plus 65 literal `\def`-style declarations. Their names and complete argument shapes remain available throughout 2.x. A separate audit records 22 declarations found only inside runtime-dead LaTeX `comment` environments; they are not removed public APIs. Native V2 internals may delegate old helpers to profile hooks, but compatibility preserves correct contracts rather than verified defects.

Full-repository check:

```bash
python3 scripts/test/check-v1-api.py
```

The checker and manifest are intentionally absent from the student ZIP.

## Byte-identical V1 project gate

`tests/102-v1-project-migration.json` pins 18 student-owned files totalling 296,726 bytes to immutable release `v1.8.2.260715154703`. It covers `thesis.tex`, `conf/conf.tex`, student content, bibliography data, and oral-certificate assets. Runtime evidence is split: the unchanged entry/configuration builds a 271-page A4 canonical result through the V2 adapter, base contract, and NCKU profile; the StudentMode fixture uses `.fls` and `.blg` records to prove active content and all three bibliography databases.

Alternate abstracts and external certificate PDFs disabled by that V1 configuration remain source-pinned but are not falsely claimed as runtime-loaded.

```text
tests/102-v1-project-migration.json
scripts/test/check-v1-project-migration.py
```

## V1 adapter layout

The V1 adapter loads even for a custom profile so old NCKU college/department presets remain defined. `template/compat/deprecated.tex` preserves 23 commands already unsupported during 1.x with the same names, diagnostics, and `\stop` behavior instead of undefined-control-sequence failures. The active one-argument `\RefTo{label}` remains available; its historical comment-only zero-argument tombstone is not public API. A custom profile does not load NCKU geometry, date policy, or watermark assets; only the intentional source-level compatibility cost remains.

```text
template/compat/v1.tex
  template/command/cmd-college.tex      compatibility wrapper
  template/command/cmd-department.tex   compatibility wrapper
  template/compat/deprecated.tex        23 deprecated-command tombstones
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
```

## Corrected behaviors

This table is the normative migration contract and must be updated in both languages for every observable helper correction. Compatibility preserves public APIs, not verified defects.

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

## Date migration

Public setters are unchanged. V2 separates raw input from profile-resolved display policy: `\GetRequestedCoverYear` / `\GetRequestedCoverMonth` expose raw `\SetCoverDate` input, `\GetThesisYear` / `\GetThesisMonth` expose profile-resolved cover values, and oral getters remain independent. NCKU still makes the oral date authoritative for the cover, preserving NCKU output. A profile for another institution uses explicit cover year/month and does not borrow an oral day.

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Institutional forks override `\ApplyOralDatePolicy`, `\ApplyCoverDatePolicy`, and profile-owned Master/Doctoral date tokens—not the public setters.

## Migrate a style port for another institution

1. Start from `template/style/custom/`; do not copy/load NCKU merely to undo it.
2. Move institution geometry, names, watermark, and date behavior from the old custom file into `<profile>/<profile>.tex`.
3. Call exactly one `\RegisterTemplateStyle{<profile>}`.
4. Select the profile with `\TemplateStyleName` in `template/style/style.tex`.
5. Replace old `\SetOralDate` / `\SetCoverDate` overrides with policy hooks.
6. Override `\ApplyCommitteeSizePolicy` only for degree-specific institution ranges; keep `\SetCommitteeSize` unchanged.
7. Move cover/oral wording and English cover-date formats to profile token setters.
8. Use `\SetCollName` / `\SetDeptName`, or maintain an institution catalogue inside the profile.
9. Build cover/certificate cases with deliberately different oral and cover dates to prove policy separation.
10. Confirm through `.fls` that no unintended institution asset is loaded.

Detailed guide: [`thesis/template/style/Customization.en.md`](../thesis/template/style/Customization.en.md)

The executable `tests/600-custom-style.tex` fixture exists only in the full repository and is intentionally absent from the student ZIP.

## Portable verification

Run these commands from an extracted student ZIP or any migrated project root containing `thesis.tex`. Verify A4 and expected pages; university, college, department, title, author, and advisor text; cover/oral dates; contents and references; bibliography convergence; Draft/watermark state; and representative cover, front-matter, body, and final pages.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Use the saved 1.x PDF as the comparison reference.

## Full-repository verification

The following commands require the complete Git checkout and run from the repository root; they are unavailable in the student ZIP. Acceptance evidence includes 597/597 runtime-visible declarations, 65/65 literal-def declarations, 22 dead-comment audit entries, 18 byte-identical student inputs, exact-tree student archive, direct build, the six-page neutral/custom fixture, and canonical 271-page NCKU output identity.

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
```

Current canonical contract:

```text
pages:                 271
paper:                 A4
normalized bbox words: 40823
text:                  identical
fonts:                 identical
raster:                271/271 identical at 120 DPI
```

## Recovery and troubleshooting

If migrated output differs unexpectedly, stop adding changes and retain the old project and baseline PDF. Classify the change as student data, template-owned files, or a local `thesis.tex` merge; return to the last buildable commit and reapply one change at a time. When changing BibTeX style or encountering stale intermediates, run `latexmk -C thesis.tex` before rebuilding. Do not edit compatibility manifests, lower expected counts, or disable tests to hide a difference.

A verified behavior correction belongs in the normative table above; an undocumented output change is a blocker.
