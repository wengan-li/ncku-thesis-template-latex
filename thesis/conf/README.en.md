<!-- doc-pair: student-config; lang: en; topics: usage-and-compatibility-boundary,content-doi-and-line-spacing,cover-language-titles-and-names,draft-and-three-watermark-layers,degree-and-dates,department-and-advisors,defense-certificate-and-committee,keywords-indexes-and-float-names,bibliography,section-numbering-and-theorems,other-institution-profiles,build-and-troubleshoot -->

[繁體中文](README.md) | [English](README.en.md)

# Thesis-configuration guide

`conf/conf.tex` is the thesis configuration file. This guide walks through it in file order and says, for each section, whether to change it, on which line, and to what; the must-change table and the common errors are in [`../README.en.md`](../README.en.md).

## Usage and compatibility boundary

Every item in `conf/conf.tex` carries a Chinese comment; this guide is its English companion. Change only the values: do not rename commands or add other configuration files. When the same setting appears more than once, the last one wins; keep one deliberate choice in each group and build after small changes.

A thesis started with a 1.x release can bring its `conf/conf.tex` over unchanged. The template keeps every 1.x command throughout 2.x.

## Content, DOI, and line spacing

**Must change**: line 13 `\ExampleMode`. **Optional**: line 20 DOI (not needed in the current workflow), line 29 line spacing.

Enabling `\ExampleMode` builds the complete teaching document from `example/context.tex`. Comment it out for your own thesis so the project uses `context/context.tex`. The current ETDS workflow does not require a student-added DOI, watermark, or PDF security setting; use the legacy/custom `\ShowDOI{...}` only when another explicit requirement applies. `\SetLineStretch{...}` adjusts line spacing and defaults to `1.2`.

```tex
% \ExampleMode
% \ShowDOI{doi:example}
% \SetLineStretch{1.2}
```

## Cover language, titles, and names

**Required**: lines 44–45 cover language and name display, lines 71–73 title, line 111 name.

Cover language only decides whether the cover is in Chinese or English; it is independent of the language of the thesis body. Select one of `\DisplayCoverInChi` or `\DisplayCoverInEng`; `\DisplayCoverPeoplesBothNames` displays both Chinese and English names on the cover.

The library workflow normally expects both Chinese and English titles, so prefer `\SetTitle{中文題目}{English Title}`. Likewise, `\SetMyName{中文姓名}{English Name}` sets both student names; use the separate Chinese/English setters only when one form is genuinely unavailable.

```tex
\DisplayCoverInEng
\DisplayCoverPeoplesBothNames
\SetTitle{中文題目}{English Title}
\SetMyName{中文姓名}{English Name}
```

For forced title line breaks, use `\\` deliberately and keep PDF metadata behavior in mind.

## Draft and three watermark layers

**Optional**: lines 80, 84, 89; keep all three commented out for final output.

Three states are independent: `\DisplayDraft` controls the `(初稿)` / `(Draft)` cover marker, `\SetWatermarkText{...}` controls the diagonal text layer, and `\UseWatermarkFigureStyle` controls the institution-logo/image layer. Final output defaults to all three being off. Enable a layer only when deliberately needed during writing or review, then disable it and re-check current university rules before submission.

```tex
% \DisplayDraft
% \SetWatermarkText{DRAFT}
% \UseWatermarkFigureStyle
```

The official system may apply its own watermark after approval; do not add one merely because the template retains an API.

## Degree and dates

**Required**: line 99 degree, line 125 oral exam date. NCKU students leave line 138 (cover date) unchanged.

Select one of `\MasterDegree` or `\PhdDegree`. `\SetOralDate{year}{month}{day}` sets the oral-defense date; `\SetCoverDate{year}{month}` stores only a cover year and month. For NCKU the cover date (including the Taiwan year) is derived from the oral date, so line 138 needs no change. Students from other institutions define a different date rule in their own school's style.

```tex
\MasterDegree
\SetOralDate{2026}{6}{30}
% \SetCoverDate{2026}{6}
```

Use Gregorian numeric input. Do not manually pre-convert the year to the Taiwan calendar.

## Department and advisors

**Required**: line 148 department, lines 166–168 advisors; with one advisor delete the B and C lines.

The template has built-in commands for 9 NCKU colleges and 110 departments; a shortcut such as `\SetDeptCSIE` sets both the department and its college. See [`../template/style/ncku/README.en.md`](../template/style/ncku/README.en.md) for every command, Chinese name, English abbreviation, English full name, and college; the fastest way to find yours is to search that page for the Chinese department name and copy the command from the left column. Students from other institutions use the generic `\SetUniversityName`, `\SetCollName`, and `\SetDeptName{Chinese name}{English abbreviation}{English full name}`, or define commands in their own school's style.

The cover holds up to three advisors. `\SetAdvisorNameA` is the first; the shipped file already fills in placeholder names for B and C, so with one advisor delete those two lines or they are printed on the cover. The Chinese honorific suffix and the English "Dr." prefix are added by the template; do not type them.

```tex
\SetDeptCSIE
\SetAdvisorNameA{指導教授姓名}{Advisor Name}
% \SetAdvisorNameB{共同指導姓名}{Co-advisor Name}
```

## Defense certificate and committee

**Required**: lines 204–206 certificate file names. Lines 176–193 matter only with the legacy example certificate.

For final submission, prefer certificate images produced by the official degree-examination system. Use `\DisplayOralImage` with `\SetOralImageChi` / `\SetOralImageEng` to load files from `context/oral/`. The version produced by `\DisplayOralTemplate` is only a legacy/example and regression output, not an official document.

`\SetCommitteeSize{n}` includes the advisors. NCKU allows 3–5 members for a master's degree and 5–9 for a doctoral degree, and the template clamps to that range by degree, so set the degree before the size. The size only matters with the legacy example certificate.

```tex
\DisplayOralImage
\SetOralImageChi{official-certificate-chi.pdf}
\SetOralImageEng{official-certificate-eng.pdf}
\SetCommitteeSize{5}
```

## Keywords, indexes, and float names

**Required**: line 224 PDF keywords, lines 246–248 abstract keywords. **Optional**: lines 264–265 index language, lines 273–279 index titles, lines 288 and 297 figure/table names.

`\SetKeywords` sets PDF metadata keywords. Chinese, English, and extended-English abstracts have separate `\SetAbstractChiKeywords`, `\SetAbstractEngKeywords`, and `\SetAbstractExtKeywords` calls; omit a call when that abstract does not exist. `\IndexChiMode` / `\IndexEngMode` select default table-of-contents, list-of-figures, and list-of-tables title language, while the corresponding title setters override wording. Use `\SetCustomFigureName` and `\SetCustomTableName` only when a custom label is required.

```tex
\SetKeywords{thesis template}{XeLaTeX}{NCKU}
\SetAbstractChiKeywords{論文範本}{成大}{XeLaTeX}
\SetAbstractEngKeywords{thesis template}{NCKU}{XeLaTeX}
\IndexEngMode
```

## Bibliography

**Optional**: lines 362–365; keep the default unless a format is required.

`\SetupReference` sets the bibliography title and BibTeX style. Keep the default when no special format is required. When switching from `abbrv` / `plain` to `apacite`, old `.aux`, `.bbl`, and related intermediates may be incompatible; run `latexmk -C thesis.tex` before rebuilding. Bibliography data belongs under `context/references/` and is selected by the existing context files.

```tex
\SetupReference{
  Title = {\TextDefaultTitleReferenceEng},
  BibStyle = {plain},
}
```

## Section numbering and theorems

**Optional**: section numbering from line 564, theorems from line 629; ignore unless a format is required.

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

`conf/conf.tex` stores thesis data; it must not own institution geometry, names, date policy, wording, or assets. `template/style/custom/` is a neutral skeleton, not a formal profile for any named institution. This repository currently has no NTU profile; students from other institutions can follow the illustrative NTU wiring in [`../template/style/Customization.en.md`](../template/style/Customization.en.md) to create an independent profile. After the profile defines a reusable catalogue, replace the original NCKU `\SetDept...` selection in `conf/conf.tex` with the new institution-prefixed command. Documentation or cover language never selects an institution profile automatically.

Exactly one profile is loaded by `template/style/style.tex`; the default remains `ncku`.

## Build and troubleshoot

After each small configuration change, run the direct build from the directory containing `thesis.tex`. Inspect the log when references or bibliography fail to converge; clean and rebuild when changing BibTeX style or stale intermediates are involved. Do not replace `latexmk` with a guessed manual count of XeLaTeX/BibTeX runs. Common error messages and fixes are listed under "Common errors" in [`../README.en.md`](../README.en.md).

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Before submission:

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Confirm no unresolved references/citations, unexpected Draft marker, text watermark, or institution-logo watermark.
