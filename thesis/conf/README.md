<!-- doc-pair: student-config; lang: zh-Hant-TW; topics: usage-and-compatibility-boundary,content-doi-and-line-spacing,cover-language-titles-and-names,draft-and-three-watermark-layers,degree-and-dates,department-and-advisors,defense-certificate-and-committee,keywords-indexes-and-float-names,bibliography,section-numbering-and-theorems,other-institution-profiles,build-and-troubleshoot -->

[繁體中文](README.md) | [English](README.en.md)

# 論文設定指南

`conf/conf.tex`是論文的設定檔。本指南按檔案順序說明每一項要不要改、在第幾行、改成什麼；必改項目的總表及常見錯誤見[`../README.md`](../README.md)。

## 使用原則與相容邊界

`conf/conf.tex`內每個項目都有中文註解。只改指令的值，不要改指令名稱，也不要新增其他設定檔。同一類設定如出現多次，以最後一次為準；每一組只保留真正選擇的一項，小步修改後立即建置。

用1.x版本寫到一半的論文可以把原有的`conf/conf.tex`原封不動帶過來，本範本在2.x期間保留所有1.x的指令。

## 論文內容、DOI與行距

**必改**：第13行`\ExampleMode`。**選填**：第20行DOI（現行流程不需要）、第29行行距。

啟用`\ExampleMode`會使用`example/context.tex`編譯完整教學文件。撰寫自己的論文時，請將該行註解，專案便會使用`context/context.tex`。現行ETDS流程不需要自行加入DOI、浮水印或PDF保全；只有其他明確規定要求時才使用保留的舊版或自訂 `\ShowDOI{...}` 功能。`\SetLineStretch{...}`可調整行距，預設為`1.2`。

```tex
% \ExampleMode
% \ShowDOI{doi:example}
% \SetLineStretch{1.2}
```

## 封面語言、題目與姓名

**必填**：第44–45行封面語言與姓名顯示、第71–73行題目、第111行姓名。

封面語言只決定封面用中文還是英文，與論文內容的語言無關。使用`\DisplayCoverInChi`或`\DisplayCoverInEng`選擇一項；`\DisplayCoverPeoplesBothNames`可讓封面同時顯示中英文姓名。

圖書館流程通常要求中英文題目都存在，建議使用`\SetTitle{中文題目}{English Title}`。姓名亦可用`\SetMyName{中文姓名}{English Name}`一次設定兩種語言；只有一種資料時才使用分開設定中文或英文的指令。需要強制換行時才使用 `\\`，並檢查 PDF 屬性中的題目。

```tex
\DisplayCoverInEng
\DisplayCoverPeoplesBothNames
\SetTitle{中文題目}{English Title}
\SetMyName{中文姓名}{English Name}
```

## 初稿與三層浮水印

**選填**：第80、84、89行；正式輸出前全部保持註解。

三個狀態互相獨立：`\DisplayDraft`控制封面`(初稿)`／`(Draft)`標記；`\SetWatermarkText{...}`控制斜向文字層；`\UseWatermarkFigureStyle`控制學校標誌／圖片層。正式輸出預設全部關閉。只有在撰寫或審閱階段確實需要時才啟用，提交前再次關閉並核對學校規定。

```tex
% \DisplayDraft
% \SetWatermarkText{DRAFT}
% \UseWatermarkFigureStyle
```

## 學位與日期

**必填**：第99行學位、第125行口試日期。第138行封面日期成大同學不用改。

使用`\MasterDegree`或`\PhdDegree`選擇一項。`\SetOralDate{year}{month}{day}`設定口試日期；`\SetCoverDate{year}{month}`只保存封面年月。成大的封面日期由口試日期自動產生（含民國年），所以第138行不用改。其他學校的同學如有不同的日期規則，在自己學校的樣式內定義。

```tex
\MasterDegree
\SetOralDate{2026}{6}{30}
% \SetCoverDate{2026}{6}
```

## 系所與指導教授

**必填**：第148行系所、第166–168行指導教授；只有一位指導教授時刪除B、C兩行。

本範本內建9個成大學院及110個系所的指令，例如`\SetDeptCSIE`會同時設定系所及所屬學院。完整指令、中文名稱、英文縮寫、英文全名及學院對應見[`../template/style/ncku/README.md`](../template/style/ncku/README.md)；最快的找法是在該頁用中文系名搜尋，複製左欄的指令。其他學校的同學使用通用的`\SetUniversityName`、`\SetCollName`及`\SetDeptName{中文名稱}{英文縮寫}{English full name}`，或在自己學校的樣式內建立指令。

封面最多三位指導教授。`\SetAdvisorNameA`是第一位；出廠檔案已填了B、C兩位示範用的名字，只有一位指導教授時要刪掉那兩行，否則會印在封面上。中文的「博士」及英文的「Dr.」由範本自動加上，不用自己寫。

```tex
\SetDeptCSIE
\SetAdvisorNameA{指導教授姓名}{Advisor Name}
% \SetAdvisorNameB{共同指導姓名}{Co-advisor Name}
```

## 學位考試證明書與委員

**必填**：第204–206行證明書檔名。第176–193行只在使用舊版範例證明書時才需要。

正式提交應優先使用學位考試系統產出的證明書圖片，透過`\DisplayOralImage`及`\SetOralImageChi`／`\SetOralImageEng`載入`context/oral/`內檔案。`\DisplayOralTemplate` 產生的版本只供舊版範例、示範與測試，並非官方文件。

`\SetCommitteeSize{n}`包括指導教授。成大的規定是碩士3至5人、博士5至9人，範本會按學位自動限制範圍，所以先設定學位再設定人數。這個人數只在使用舊版範例證明書時才有作用。

```tex
\DisplayOralImage
\SetOralImageChi{official-certificate-chi.pdf}
\SetOralImageEng{official-certificate-eng.pdf}
\SetCommitteeSize{5}
```

## 關鍵字、目錄與圖表名稱

**必填**：第224行PDF關鍵字、第246–248行摘要關鍵字。**選填**：第264–265行目錄語言、第273–279行目錄標題、第288與297行圖表名稱。

`\SetKeywords` 設定 PDF 屬性中的關鍵字。中文、英文及英文延伸摘要可分別使用`\SetAbstractChiKeywords`、`\SetAbstractEngKeywords`及`\SetAbstractExtKeywords`；沒有資料的版本不需呼叫。`\IndexChiMode`／`\IndexEngMode`控制目錄、圖目錄及表目錄的預設標題語言，亦可用對應的標題設定指令修改文字。`\SetCustomFigureName`及`\SetCustomTableName`只在需要修改圖、表名稱時使用。

```tex
\SetKeywords{thesis template}{XeLaTeX}{NCKU}
\SetAbstractChiKeywords{論文範本}{成大}{XeLaTeX}
\SetAbstractEngKeywords{thesis template}{NCKU}{XeLaTeX}
\IndexEngMode
```

## 參考文獻

**選填**：第362–365行；沒有特殊要求時保留預設。

`\SetupReference` 設定參考文獻標題及 BibTeX 樣式。沒有特殊格式要求時可保留預設。由`abbrv`／`plain`切換至`apacite`時，舊`.aux`、`.bbl`等中間檔可能不相容；先執行`latexmk -C thesis.tex`，再重新建置。書目資料放在 `context/references/`，並由現有內容檔載入。

```tex
\SetupReference{
  Title = {\TextDefaultTitleReferenceEng},
  BibStyle = {plain},
}
```

## 章節編號與定理

**選填**：第564行起的章節編號、第629行起的定理；沒有格式要求時不用理會。

沒有明確格式要求時，保留預設編號及定理樣式。`\SetNumberingFormat[<type>]{...}` 可分別調整一般章節及附錄的 Chapter、Section、SubSection 與 SubSubSection 編號，支援 `Arabic`、羅馬數字、英文字母、`ChiNum` 及 `Tiangan` 等樣式。`\SetTheoremFormat[<type>]{...}` 設定顯示文字及計數器之間的關係。選項名稱不正確會停止建置；每次只改一組設定，隨即建置檢查。

```tex
\SetNumberingFormat[Chapter]{
  BeginText = {Chapter },
  CNumStyle = {Arabic},
  SepAtIndex = {.},
}
\SetTheoremFormat[Theorem]{ShowText = {Theorem}}
```

## 其他學校的同學如何設定學校樣式

`conf/conf.tex` 只放論文資料。學校版面、校名、日期規則、文字與圖片放在 `template/style/`。`template/style/custom/` 是起始範例，不是任何學校的正式格式；本專案目前也沒有可直接使用的臺大樣式。其他學校的同學可依[自訂指南](../template/style/Customization.md)建立自己的樣式，參考其中的臺大設定示範。建立學校專用的系所指令後，在 `conf/conf.tex` 用它取代原有成大 `\SetDept...` 指令。文件語言、封面語言及學校樣式分別設定；`template/style/style.tex` 每次只載入一種樣式，預設為 `ncku`。

## 建置與故障排除

每次小幅修改後，在包含`thesis.tex`的目錄執行建置。若引用或參考文獻仍有警告，先查看建置記錄；切換 BibTeX 樣式或舊輔助檔造成問題時，才清除後重建。不要以手動重複XeLaTeX/BibTeX次數取代`latexmk`。常見錯誤訊息與解法見[`../README.md`](../README.md)的「常見錯誤」一節。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```
