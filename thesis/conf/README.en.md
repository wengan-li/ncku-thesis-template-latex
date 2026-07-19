<!-- doc-pair: student-config; lang: en; topics: usage-and-compatibility-boundary,content-doi-and-line-spacing,cover-language-titles-and-names,draft-and-three-watermark-layers,degree-and-dates,department-and-advisors,defense-certificate-and-committee,keywords-indexes-and-float-names,bibliography,section-numbering-and-theorems,other-institution-profiles,build-and-troubleshoot -->

[繁體中文](README.md) | [English](README.en.md)

# Thesis-configuration guide

`conf/conf.tex` is the student project's main configuration file. This guide explains its editable sections in file order without replacing the file itself. Return to [`../README.en.md`](../README.en.md) for the complete student workflow.

## Usage and compatibility boundary

`conf/conf.tex` has been byte-pinned from `v1.8.2.260715154703` throughout 2.x to prove that existing student configuration can migrate unchanged. Its original Chinese comments and repository bytes are therefore not rewritten for translation. Enter values in your own thesis copy; the repository baseline and migration hash remain unchanged for translation.

When the same setting is called more than once, the last call normally wins. Keep one deliberate choice in each group and build after small changes.

Do not add `conf/style.tex`. Student metadata belongs in `conf/`; institution policy belongs under `template/style/`.

## Content, DOI, and line spacing

Enabling `\ExampleMode` builds the complete teaching document from `example/context.tex`. Comment it out for your own thesis so the project uses `context/context.tex`. The current ETDS workflow does not require a student-added DOI, watermark, or PDF security setting; use the legacy/custom `\ShowDOI{...}` only when another explicit requirement applies. `\SetLineStretch{...}` adjusts line spacing and defaults to `1.2`.

```tex
% \ExampleMode
% \ShowDOI{doi:example}
% \SetLineStretch{1.2}
```

## Cover language, titles, and names

Cover language is independent of the institution profile. Select one of `\DisplayCoverInChi` or `\DisplayCoverInEng`; `\DisplayCoverPeoplesBothNames` displays both Chinese and English names on the cover. NCKU students retain the `ncku` profile regardless of documentation language.

The library workflow normally expects both Chinese and English titles, so prefer `\SetTitle{中文題目}{English Title}`. Likewise, `\SetMyName{中文姓名}{English Name}` sets both student names; use the separate Chinese/English setters only when one form is genuinely unavailable.

```tex
\DisplayCoverInEng
\DisplayCoverPeoplesBothNames
\SetTitle{中文題目}{English Title}
\SetMyName{中文姓名}{English Name}
```

For forced title line breaks, use `\\` deliberately and keep PDF metadata behavior in mind.

## Draft and three watermark layers

Three states are independent: `\DisplayDraft` controls the `(初稿)` / `(Draft)` cover marker, `\SetWatermarkText{...}` controls the diagonal text layer, and `\UseWatermarkFigureStyle` controls the institution-logo/image layer. Final output defaults to all three being off. Enable a layer only when deliberately needed during writing or review, then disable it and re-check current university rules before submission.

```tex
% \DisplayDraft
% \SetWatermarkText{DRAFT}
% \UseWatermarkFigureStyle
```

The official system may apply its own watermark after approval; do not add one merely because the template retains an API.

## Degree and dates

Select one of `\MasterDegree` or `\PhdDegree`. `\SetOralDate{year}{month}{day}` sets the oral-defense date; `\SetCoverDate{year}{month}` stores only a cover year and month. The NCKU profile derives the cover date and Taiwan-year display from the oral date under NCKU policy, so NCKU students normally do not rely on a separate cover date. Another institution's date policy belongs in its profile.

```tex
\MasterDegree
\SetOralDate{2026}{6}{30}
% \SetCoverDate{2026}{6}
```

Use Gregorian numeric input. Do not manually pre-convert the year to the Taiwan calendar.

## Department and advisors

NCKU projects may use department presets such as `\SetDeptCSIE`; inspect `template/style/ncku/department.tex` for available commands. Other institutions must not use NCKU presets. Provide institution data in the selected profile or use the generic `\SetDeptName{Chinese name}{English abbreviation}{English full name}`.

The cover reserves space for up to three advisors. `\SetAdvisorNameA` is the first advisor; add `B` and `C` only when needed. Both language forms may be supplied together, while Chinese suffixes and English prefixes are profile policy.

```tex
\SetDeptCSIE
\SetAdvisorNameA{指導教授姓名}{Advisor Name}
% \SetAdvisorNameB{共同指導姓名}{Co-advisor Name}
```

## Defense certificate and committee

For final submission, prefer certificate images produced by the official degree-examination system. Use `\DisplayOralImage` with `\SetOralImageChi` / `\SetOralImageEng` to load files from `context/oral/`. The version produced by `\DisplayOralTemplate` is only a legacy/example and regression output, not an official document.

`\SetCommitteeSize{n}` includes advisors. The NCKU profile applies semantic degree policy: 3–5 members for a master's degree and 5–9 for a doctoral degree. The neutral/custom generic renderer supports 2–9. Set the degree before the committee size.

```tex
\DisplayOralImage
\SetOralImageChi{official-certificate-chi.pdf}
\SetOralImageEng{official-certificate-eng.pdf}
\SetCommitteeSize{5}
```

## Keywords, indexes, and float names

`\SetKeywords` sets PDF metadata keywords. Chinese, English, and extended-English abstracts have separate `\SetAbstractChiKeywords`, `\SetAbstractEngKeywords`, and `\SetAbstractExtKeywords` calls; omit a call when that abstract does not exist. `\IndexChiMode` / `\IndexEngMode` select default table-of-contents, list-of-figures, and list-of-tables title language, while the corresponding title setters override wording. Use `\SetCustomFigureName` and `\SetCustomTableName` only when a custom label is required.

```tex
\SetKeywords{thesis template}{XeLaTeX}{NCKU}
\SetAbstractChiKeywords{論文範本}{成大}{XeLaTeX}
\SetAbstractEngKeywords{thesis template}{NCKU}{XeLaTeX}
\IndexEngMode
```

## Bibliography

`\SetupReference` sets the bibliography title and BibTeX style. Keep the default when no special format is required. When switching from `abbrv` / `plain` to `apacite`, old `.aux`, `.bbl`, and related intermediates may be incompatible; run `latexmk -C thesis.tex` before rebuilding. Bibliography data belongs under `context/references/` and is selected by the existing context files.

```tex
\SetupReference{
  Title = {\TextDefaultTitleReferenceEng},
  BibStyle = {plain},
}
```

## Section numbering and theorems

Keep the default numbering and theorem styles unless an explicit requirement says otherwise. `\SetNumberingFormat[<type>]{...}` independently configures normal/appendix Chapter, Section, SubSection, and SubSubSection formats, with Arabic, Roman, alphabetic, `ChiNum`, and `Tiangan` styles. `\SetTheoremFormat[<type>]{...}` sets visible text and counter relationships. Unknown keys fail hard, so change one family at a time and build immediately.

```tex
\SetNumberingFormat[Chapter]{
  BeginText = {Chapter },
  CNumStyle = {Arabic},
  SepAtIndex = {.},
}
\SetTheoremFormat[Theorem]{ShowText = {Theorem}}
```

Do not rename public commands during 2.x; the compatibility adapter preserves existing projects.

## Other institution profiles

`conf/conf.tex` stores thesis data; it must not own institution geometry, names, date policy, wording, or assets. Students from other institutions should start from `template/style/custom/` and follow [`../template/style/Customization.en.md`](../template/style/Customization.en.md). Documentation or cover language never selects an institution profile automatically.

Exactly one profile is loaded by `template/style/style.tex`; the default remains `ncku`.

## Build and troubleshoot

After each small configuration change, run the direct build from the directory containing `thesis.tex`. Inspect the log when references or bibliography fail to converge; clean and rebuild when changing BibTeX style or stale intermediates are involved. Do not replace `latexmk` with a guessed manual count of XeLaTeX/BibTeX runs.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Before submission:

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Confirm no unresolved references/citations, unexpected Draft marker, text watermark, or institution-logo watermark.
