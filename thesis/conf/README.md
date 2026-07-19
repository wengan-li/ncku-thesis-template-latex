<!-- doc-pair: student-config; lang: zh-Hant-TW; topics: usage-and-compatibility-boundary,content-doi-and-line-spacing,cover-language-titles-and-names,draft-and-three-watermark-layers,degree-and-dates,department-and-advisors,defense-certificate-and-committee,keywords-indexes-and-float-names,bibliography,section-numbering-and-theorems,other-institution-profiles,build-and-troubleshoot -->

[繁體中文](README.md) | [English](README.en.md)

# 論文設定指南

`conf/conf.tex`是學生專案的主要設定檔。本指南按該檔案的順序解釋可調整項目，但不取代檔案本身。回到[`../README.md`](../README.md)查看完整student workflow。

## 使用原則與相容邊界

`conf/conf.tex`從`v1.8.2.260715154703`開始在2.x被byte-pinned，用來證明既有學生設定可原封不動地升級。因此它原有的中文註解及檔案bytes不會為翻譯而改寫。請在自己的論文副本內填寫值；repository baseline及migration hash不會為了配合翻譯而改動。

同一類設定如呼叫多次，通常以最後一次呼叫為準。每一組只保留你真正選擇的一項，並在小步修改後立即build。

## 論文內容、DOI與行距

啟用`\ExampleMode`會使用`example/context.tex`編譯完整教學文件。撰寫自己的論文時，請將該行註解，專案便會使用`context/context.tex`。現行ETDS流程不需要自行加入DOI、浮水印或PDF保全；只有其他明確規定要求時才使用legacy/custom `\ShowDOI{...}`。`\SetLineStretch{...}`可調整行距，預設為`1.2`。

```tex
% \ExampleMode
% \ShowDOI{doi:example}
% \SetLineStretch{1.2}
```

## 封面語言、題目與姓名

封面語言與學校profile互相獨立。使用`\DisplayCoverInChi`或`\DisplayCoverInEng`選擇一項；`\DisplayCoverPeoplesBothNames`可讓封面同時顯示中英文姓名。成大學生無論閱讀哪種文件語言，均保留`ncku` profile。

圖書館流程通常要求中英文題目都存在，建議使用`\SetTitle{中文題目}{English Title}`。姓名亦可用`\SetMyName{中文姓名}{English Name}`一次設定兩種語言；只有一種資料時才使用分開的Chinese/English setter。

```tex
\DisplayCoverInEng
\DisplayCoverPeoplesBothNames
\SetTitle{中文題目}{English Title}
\SetMyName{中文姓名}{English Name}
```

## 初稿與三層浮水印

三個狀態互相獨立：`\DisplayDraft`控制封面`(初稿)`／`(Draft)`標記；`\SetWatermarkText{...}`控制斜向文字層；`\UseWatermarkFigureStyle`控制學校logo／圖片層。正式輸出預設全部關閉。只有在撰寫或審閱階段確實需要時才啟用，提交前再次關閉並核對學校規定。

```tex
% \DisplayDraft
% \SetWatermarkText{DRAFT}
% \UseWatermarkFigureStyle
```

## 學位與日期

使用`\MasterDegree`或`\PhdDegree`選擇一項。`\SetOralDate{year}{month}{day}`設定口試日期；`\SetCoverDate{year}{month}`只保存封面年月。NCKU profile會按成大政策由口試日期產生封面日期及民國年顯示，因此成大學生一般不需另外依賴`\SetCoverDate`。其他學校的同學如有不同日期政策，應在自己的institution profile內定義。

```tex
\MasterDegree
\SetOralDate{2026}{6}{30}
% \SetCoverDate{2026}{6}
```

## 系所與指導教授

NCKU專案可使用`\SetDeptCSIE`等成大系所preset；請在`template/style/ncku/department.tex`確認可用command。其他學校的同學不應使用NCKU preset，應在自己的profile提供學校資料，或使用通用`\SetDeptName{中文名稱}{英文縮寫}{English full name}`。

封面最多預留三位指導教授。`\SetAdvisorNameA`為第一位，之後視需要使用`B`及`C`。雙語姓名可一次提供；中文suffix及英文prefix由profile控制。

```tex
\SetDeptCSIE
\SetAdvisorNameA{指導教授姓名}{Advisor Name}
% \SetAdvisorNameB{共同指導姓名}{Co-advisor Name}
```

## 學位考試證明書與委員

正式提交應優先使用學位考試系統產出的證明書圖片，透過`\DisplayOralImage`及`\SetOralImageChi`／`\SetOralImageEng`載入`context/oral/`內檔案。`\DisplayOralTemplate`產生的版本只供legacy/example及regression用途，並非官方文件。

`\SetCommitteeSize{n}`包括指導教授。NCKU profile按semantic degree state將碩士限制為3至5人、博士限制為5至9人；neutral/custom profile的generic renderer支援2至9人。請先設定degree，再設定committee size。

```tex
\DisplayOralImage
\SetOralImageChi{official-certificate-chi.pdf}
\SetOralImageEng{official-certificate-eng.pdf}
\SetCommitteeSize{5}
```

## 關鍵字、目錄與圖表名稱

`\SetKeywords`設定PDF metadata keywords。中文、英文及英文延伸摘要可分別使用`\SetAbstractChiKeywords`、`\SetAbstractEngKeywords`及`\SetAbstractExtKeywords`；沒有資料的版本不需呼叫。`\IndexChiMode`／`\IndexEngMode`控制目錄、圖目錄及表目錄的預設標題語言，亦可用對應title setter覆寫文字。`\SetCustomFigureName`及`\SetCustomTableName`只在確實需要自訂label時使用。

```tex
\SetKeywords{thesis template}{XeLaTeX}{NCKU}
\SetAbstractChiKeywords{論文範本}{成大}{XeLaTeX}
\SetAbstractEngKeywords{thesis template}{NCKU}{XeLaTeX}
\IndexEngMode
```

## 參考文獻

`\SetupReference`設定參考文獻標題及BibTeX style。沒有特殊格式要求時可保留預設。由`abbrv`／`plain`切換至`apacite`時，舊`.aux`、`.bbl`等中間檔可能不相容；先執行`latexmk -C thesis.tex`，再重新build。書目資料放在`context/references/`並由現有context選取。

```tex
\SetupReference{
  Title = {\TextDefaultTitleReferenceEng},
  BibStyle = {plain},
}
```

## 章節編號與定理

沒有明確格式要求時，保留預設編號及theorem style。`\SetNumberingFormat[<type>]{...}`可分別調整一般／附錄的Chapter、Section、SubSection及SubSubSection；支援`Arabic`、Roman、alphabetic、`ChiNum`及`Tiangan`等number style。`\SetTheoremFormat[<type>]{...}`設定顯示文字與counter關係。未知key會hard fail，因此每次只修改一個family並立即build。

```tex
\SetNumberingFormat[Chapter]{
  BeginText = {Chapter },
  CNumStyle = {Arabic},
  SepAtIndex = {.},
}
\SetTheoremFormat[Theorem]{ShowText = {Theorem}}
```

## 其他學校的同學如何使用Profile

`conf/conf.tex`只保存論文資料，不應承擔學校geometry、校名、日期政策、institution wording或assets。其他學校的同學應由`template/style/custom/`開始，並跟隨[`../template/style/Customization.md`](../template/style/Customization.md)。文件語言或封面語言不會自動選擇profile。

## 建置與故障排除

每次小幅修改後，在包含`thesis.tex`的目錄執行direct build。出現引用或書目不收斂時，先查看log；切換BibTeX style或遇到stale intermediates時才清除後重建。不要以手動重複XeLaTeX/BibTeX次數取代`latexmk`。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```
