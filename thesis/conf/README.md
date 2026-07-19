<!-- bilingual:complete -->

# 論文設定雙語指南 / Bilingual thesis-configuration guide

`conf/conf.tex`是學生專案的主要設定檔。本指南按該檔案的順序解釋可調整項目，但不取代檔案本身。回到[`../README.md`](../README.md)查看完整student workflow。

`conf/conf.tex` is the student project's main configuration file. This guide explains its editable sections in file order without replacing the file itself. Return to [`../README.md`](../README.md) for the complete student workflow.

## 使用原則與相容邊界 / Usage and compatibility boundary

**繁體中文**

`conf/conf.tex`從`v1.8.2.260715154703`開始在2.x被byte-pinned，用來證明既有學生設定可原封不動地升級。因此它原有的中文註解及檔案bytes不會為雙語文件而改寫。請在自己的論文副本內填寫值；範本維護者不可改動repository baseline或更新migration hash來配合翻譯。

同一類設定如呼叫多次，通常以最後一次呼叫為準。每一組只保留你真正選擇的一項，並在小步修改後立即build。

**English**

`conf/conf.tex` has been byte-pinned from `v1.8.2.260715154703` throughout 2.x to prove that existing student configuration can migrate unchanged. Its original Chinese comments and repository bytes are therefore not rewritten for bilingual documentation. Enter values in your own thesis copy; maintainers must not change the repository baseline or migration hash merely to translate comments.

When the same setting is called more than once, the last call normally wins. Keep one deliberate choice in each group and build after small changes.

Do not add `conf/style.tex`. Student metadata belongs in `conf/`; institution policy belongs under `template/style/`.

## 論文內容、DOI與行距 / Content, DOI, and line spacing

**繁體中文**

啟用`\ExampleMode`會使用`example/context.tex`編譯完整教學文件。撰寫自己的論文時，請將該行註解，專案便會使用`context/context.tex`。現行ETDS流程不需要自行加入DOI、浮水印或PDF保全；只有其他明確規定要求時才使用legacy/custom `\ShowDOI{...}`。`\SetLineStretch{...}`可調整行距，預設為`1.2`。

**English**

Enabling `\ExampleMode` builds the complete teaching document from `example/context.tex`. Comment it out for your own thesis so the project uses `context/context.tex`. The current ETDS workflow does not require a student-added DOI, watermark, or PDF security setting; use the legacy/custom `\ShowDOI{...}` only when another explicit requirement applies. `\SetLineStretch{...}` adjusts line spacing and defaults to `1.2`.

```tex
% \ExampleMode
% \ShowDOI{doi:example}
% \SetLineStretch{1.2}
```

## 封面語言、題目與姓名 / Cover language, titles, and names

**繁體中文**

封面語言與學校profile互相獨立。使用`\DisplayCoverInChi`或`\DisplayCoverInEng`選擇一項；`\DisplayCoverPeoplesBothNames`可讓封面同時顯示中英文姓名。成大學生無論閱讀哪種文件語言，均保留`ncku` profile。

圖書館流程通常要求中英文題目都存在，建議使用`\SetTitle{中文題目}{English Title}`。姓名亦可用`\SetMyName{中文姓名}{English Name}`一次設定兩種語言；只有一種資料時才使用分開的Chinese/English setter。

**English**

Cover language is independent of the institution profile. Select one of `\DisplayCoverInChi` or `\DisplayCoverInEng`; `\DisplayCoverPeoplesBothNames` displays both Chinese and English names on the cover. NCKU students retain the `ncku` profile regardless of documentation language.

The library workflow normally expects both Chinese and English titles, so prefer `\SetTitle{中文題目}{English Title}`. Likewise, `\SetMyName{中文姓名}{English Name}` sets both student names; use the separate Chinese/English setters only when one form is genuinely unavailable.

```tex
\DisplayCoverInEng
\DisplayCoverPeoplesBothNames
\SetTitle{中文題目}{English Title}
\SetMyName{中文姓名}{English Name}
```

For forced title line breaks, use `\\` deliberately and keep PDF metadata behavior in mind.

## 初稿與三層浮水印 / Draft and three watermark layers

**繁體中文**

三個狀態互相獨立：`\DisplayDraft`控制封面`(初稿)`／`(Draft)`標記；`\SetWatermarkText{...}`控制斜向文字層；`\UseWatermarkFigureStyle`控制學校logo／圖片層。正式輸出預設全部關閉。只有在撰寫或審閱階段確實需要時才啟用，提交前再次關閉並核對學校規定。

**English**

Three states are independent: `\DisplayDraft` controls the `(初稿)` / `(Draft)` cover marker, `\SetWatermarkText{...}` controls the diagonal text layer, and `\UseWatermarkFigureStyle` controls the institution-logo/image layer. Final output defaults to all three being off. Enable a layer only when deliberately needed during writing or review, then disable it and re-check current university rules before submission.

```tex
% \DisplayDraft
% \SetWatermarkText{DRAFT}
% \UseWatermarkFigureStyle
```

The official system may apply its own watermark after approval; do not add one merely because the template retains an API.

## 學位與日期 / Degree and dates

**繁體中文**

使用`\MasterDegree`或`\PhdDegree`選擇一項。`\SetOralDate{year}{month}{day}`設定口試日期；`\SetCoverDate{year}{month}`只保存封面年月。NCKU profile會按成大政策由口試日期產生封面日期及民國年顯示，因此成大學生一般不需另外依賴`\SetCoverDate`。其他學校的日期政策應由該institution profile定義。

**English**

Select one of `\MasterDegree` or `\PhdDegree`. `\SetOralDate{year}{month}{day}` sets the oral-defense date; `\SetCoverDate{year}{month}` stores only a cover year and month. The NCKU profile derives the cover date and Taiwan-year display from the oral date under NCKU policy, so NCKU students normally do not rely on a separate cover date. Another institution's date policy belongs in its profile.

```tex
\MasterDegree
\SetOralDate{2026}{6}{30}
% \SetCoverDate{2026}{6}
```

Use Gregorian numeric input. Do not manually pre-convert the year to the Taiwan calendar.

## 系所與指導教授 / Department and advisors

**繁體中文**

NCKU專案可使用`\SetDeptCSIE`等成大系所preset；請在`template/style/ncku/department.tex`確認可用command。其他學校不要使用NCKU preset，應在自己的profile提供學校資料，或使用通用`\SetDeptName{中文名稱}{英文縮寫}{English full name}`。

封面最多預留三位指導教授。`\SetAdvisorNameA`為第一位，之後視需要使用`B`及`C`。雙語姓名可一次提供；中文suffix及英文prefix由profile控制。

**English**

NCKU projects may use department presets such as `\SetDeptCSIE`; inspect `template/style/ncku/department.tex` for available commands. Other institutions must not use NCKU presets. Provide institution data in the selected profile or use the generic `\SetDeptName{Chinese name}{English abbreviation}{English full name}`.

The cover reserves space for up to three advisors. `\SetAdvisorNameA` is the first advisor; add `B` and `C` only when needed. Both language forms may be supplied together, while Chinese suffixes and English prefixes are profile policy.

```tex
\SetDeptCSIE
\SetAdvisorNameA{指導教授姓名}{Advisor Name}
% \SetAdvisorNameB{共同指導姓名}{Co-advisor Name}
```

## 學位考試證明書與委員 / Defense certificate and committee

**繁體中文**

正式提交應優先使用學位考試系統產出的證明書圖片，透過`\DisplayOralImage`及`\SetOralImageChi`／`\SetOralImageEng`載入`context/oral/`內檔案。`\DisplayOralTemplate`產生的版本只供legacy/example及regression用途，並非官方文件。

`\SetCommitteeSize{n}`包括指導教授。NCKU profile按semantic degree state將碩士限制為3至5人、博士限制為5至9人；neutral/custom profile的generic renderer支援2至9人。請先設定degree，再設定committee size。

**English**

For final submission, prefer certificate images produced by the official degree-examination system. Use `\DisplayOralImage` with `\SetOralImageChi` / `\SetOralImageEng` to load files from `context/oral/`. The version produced by `\DisplayOralTemplate` is only a legacy/example and regression output, not an official document.

`\SetCommitteeSize{n}` includes advisors. The NCKU profile applies semantic degree policy: 3–5 members for a master's degree and 5–9 for a doctoral degree. The neutral/custom generic renderer supports 2–9. Set the degree before the committee size.

```tex
\DisplayOralImage
\SetOralImageChi{official-certificate-chi.pdf}
\SetOralImageEng{official-certificate-eng.pdf}
\SetCommitteeSize{5}
```

## 關鍵字、目錄與圖表名稱 / Keywords, indexes, and float names

**繁體中文**

`\SetKeywords`設定PDF metadata keywords。中文、英文及英文延伸摘要可分別使用`\SetAbstractChiKeywords`、`\SetAbstractEngKeywords`及`\SetAbstractExtKeywords`；沒有資料的版本不需呼叫。`\IndexChiMode`／`\IndexEngMode`控制目錄、圖目錄及表目錄的預設標題語言，亦可用對應title setter覆寫文字。`\SetCustomFigureName`及`\SetCustomTableName`只在確實需要自訂label時使用。

**English**

`\SetKeywords` sets PDF metadata keywords. Chinese, English, and extended-English abstracts have separate `\SetAbstractChiKeywords`, `\SetAbstractEngKeywords`, and `\SetAbstractExtKeywords` calls; omit a call when that abstract does not exist. `\IndexChiMode` / `\IndexEngMode` select default table-of-contents, list-of-figures, and list-of-tables title language, while the corresponding title setters override wording. Use `\SetCustomFigureName` and `\SetCustomTableName` only when a custom label is required.

```tex
\SetKeywords{thesis template}{XeLaTeX}{NCKU}
\SetAbstractChiKeywords{論文範本}{成大}{XeLaTeX}
\SetAbstractEngKeywords{thesis template}{NCKU}{XeLaTeX}
\IndexEngMode
```

## 參考文獻 / Bibliography

**繁體中文**

`\SetupReference`設定參考文獻標題及BibTeX style。沒有特殊格式要求時可保留預設。由`abbrv`／`plain`切換至`apacite`時，舊`.aux`、`.bbl`等中間檔可能不相容；先執行`latexmk -C thesis.tex`，再重新build。書目資料放在`context/references/`並由現有context選取。

**English**

`\SetupReference` sets the bibliography title and BibTeX style. Keep the default when no special format is required. When switching from `abbrv` / `plain` to `apacite`, old `.aux`, `.bbl`, and related intermediates may be incompatible; run `latexmk -C thesis.tex` before rebuilding. Bibliography data belongs under `context/references/` and is selected by the existing context files.

```tex
\SetupReference{
  Title = {\TextDefaultTitleReferenceEng},
  BibStyle = {plain},
}
```

## 章節編號與定理 / Section numbering and theorems

**繁體中文**

沒有明確格式要求時，保留預設編號及theorem style。`\SetNumberingFormat[<type>]{...}`可分別調整一般／附錄的Chapter、Section、SubSection及SubSubSection；支援`Arabic`、Roman、alphabetic、`ChiNum`及`Tiangan`等number style。`\SetTheoremFormat[<type>]{...}`設定顯示文字與counter關係。未知key會hard fail，因此每次只修改一個family並立即build。

**English**

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

## 其他學校Profile / Other institution profiles

**繁體中文**

`conf/conf.tex`只保存論文資料，不應承擔學校geometry、校名、日期政策、institution wording或assets。非NCKU維護者應由`template/style/custom/`開始，並跟隨[`../template/style/Customization.md`](../template/style/Customization.md)。文件語言或封面語言不會自動選擇profile。

**English**

`conf/conf.tex` stores thesis data; it must not own institution geometry, names, date policy, wording, or assets. Non-NCKU maintainers should start from `template/style/custom/` and follow [`../template/style/Customization.md`](../template/style/Customization.md). Documentation or cover language never selects an institution profile automatically.

Exactly one profile is loaded by `template/style/style.tex`; the default remains `ncku`.

## 建置與故障排除 / Build and troubleshoot

**繁體中文**

每次小幅修改後，在包含`thesis.tex`的目錄執行direct build。出現引用或書目不收斂時，先查看log；切換BibTeX style或遇到stale intermediates時才清除後重建。不要以手動重複XeLaTeX/BibTeX次數取代`latexmk`。

**English**

After each small configuration change, run the direct build from the directory containing `thesis.tex`. Inspect the log when references or bibliography fail to converge; clean and rebuild when changing BibTeX style or stale intermediates are involved. Do not replace `latexmk` with a guessed manual count of XeLaTeX/BibTeX runs.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Before submission / 提交前：

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Confirm no unresolved references/citations, unexpected Draft marker, text watermark, or institution-logo watermark.
