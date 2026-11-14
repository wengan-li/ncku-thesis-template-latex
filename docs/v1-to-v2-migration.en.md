<!-- doc-pair: v1-v2-migration; lang: en; topics: before-you-start,compatibility-first-path,build-and-compare,new-project-path,stable-project-boundaries,current-helper-behavior,date-configuration,institution-port,compatibility-boundary,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# NCKU thesis template 1.x-to-2.x migration guide

A thesis started with 1.x can move to 2.x without rewriting its content. Keep the original project, upgrade in a new directory, and compare with the old PDF. Version 2.x still uses XeLaTeX.

## Before you start

Back up the complete 1.x project and its latest PDF, including your figures, bibliography, added fonts and official certificates. Record the XeLaTeX version, page count, cover and oral dates, and any enabled watermarks for comparison. Do not overwrite your only thesis copy.

## Upgrade with your existing configuration

1. Download the 2.x student package from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) and extract it into a new directory.
2. Copy in your old `conf/conf.tex`, `context/` content, figures, bibliography and official certificates, replacing sample files with your own files of the same name.
3. Copy your added fonts into `template/fonts/`. Do not replace the new `template/` directory with the old one.
4. If you edited `thesis.tex` or `cover.tex`, merge those edits into the new files instead of overwriting them.

Build and compare as described below before continuing to edit the thesis.

## Build and compare

Build from the directory containing `thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

In Overleaf, select XeLaTeX and set `thesis.tex` as the main document. Editors use the same main document and XeLaTeX/BibTeX workflow.

Compare with the old PDF: A4 paper, page count, cover data and dates, certificate, contents, figures, citations, bibliography and final page. Resolve undefined references and unexpected watermarks. Producing a PDF alone does not complete the upgrade.

## Start with the new configuration

To reorganize your settings, keep the 2.x `conf/conf.tex` and enter your data using the [configuration guide](../thesis/conf/README.en.md). Comment out `\ExampleMode` to build your own thesis rather than the tutorial.

When moving the complete project, preserve its hidden `.agents/`, `.claude/` and relative links. See the [content and writing guide](../thesis/context/README.en.md) for writing assistance.

## Where files belong

- `conf/conf.tex` contains thesis data; `context/` contains your chapters.
- `template/` contains the template implementation; `example/` contains the tutorial.
- University layout and rules belong in `template/style/`, not a new `conf/style.tex`.

NCKU students keep the default `ncku` setting. Cover language, degree and tutorial mode are separate choices. An English cover does not require a different university style.

## Changes to check after upgrading

| Item | What to check |
| --- | --- |
| Section references | With `\StartSubSubSection{title}{label}`, references still get the section number when the heading hides it. Rebuild and check those references. |
| English department names | With `\SetDeptName{chi}{short}{full}`, check the abbreviation and full name. `\SetDeptDPS` uses Department of Photonics. |
| Committee size | Select `\MasterDegree` or `\PhdDegree` before calling `\SetCommitteeSize`. NCKU uses 3–5 members for Master's and 5–9 for doctoral degrees; generic settings allow 2–9. |
| Theorem and caption references | Rebuild and check `\ref` and `\nameref`. Figure and table labels are no longer overwritten by later caption settings. |
| Custom numbering | Check prefixes, separators and contents. Repeated setup should not accumulate prefixes; counter values still update. |
| Theorem `FollowCounter` | References may point forward or follow several counters. Remove circular dependencies if a cycle error appears. |
| Custom fonts | `\SetCustomEngFontFiles` and `\SetCustomChiFontFiles` now load the specified files. Supply missing files in `template/fonts/`, or remove custom settings to use the defaults. |

## Date settings

NCKU derives the cover date from the oral date. Generic settings for other institutions use the cover month and year you enter. Keep the two dates distinct:

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Check both dates after upgrading. `\GetOralYearInTaiwanYear` no longer changes the thesis year, and `\SetOralEngDate` updates the oral Taiwan-year value too. English certificate examples use the oral day, month and year. Use the official university-system certificate for submission.

To change a university's date rules, follow the [customization guide](../thesis/template/style/Customization.en.md) rather than redefining `\SetOralDate` or `\SetCoverDate`.

## Students from other institutions

Start with `template/style/custom/` rather than loading NCKU settings and undoing them. Set university names, departments, layout, dates, watermarks and certificate wording in the school style. Keep student data in `conf/conf.tex`.

Use the [customization guide](../thesis/template/style/Customization.en.md) to register and select the style. Replace NCKU department calls with generic `\SetCollName` and `\SetDeptName` calls or your university's commands. Test different oral and cover dates, both languages and both degrees, and check that no NCKU names or assets remain.

Neither `custom` nor the NTU wiring example is a ready-to-submit format. Check your university's and department's current requirements.

## Old commands and limitations

Version 2.x preserves declared 1.x public command and environment names and their arguments. `template/compat/v1.tex` loads automatically. Deprecated commands still report errors; `\RefTo{label}` remains usable. NCKU department shortcuts are available under the default `ncku` setting only.

The PDF is untagged, with no PDF/UA or university-approval claim. See [architecture](features/v2-modernization.en.md) and [validation](features/validation-and-performance.en.md) for technical details. Normal migration does not require repository test tools.

## Recovery and troubleshooting

If output differs unexpectedly, stop editing and keep the failing version for comparison. Return to a buildable backup, then check copied data, fonts and merged `thesis.tex` edits one at a time.

For stale auxiliary files or errors after changing BibTeX styles, clean and rebuild:

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Supply missing custom fonts or remove the custom settings rather than ignoring errors. See the [student troubleshooting guide](../thesis/README.en.md) for other failures.
