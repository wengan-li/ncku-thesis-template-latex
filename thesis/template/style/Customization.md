<!-- doc-pair: style-customization; lang: zh-Hant-TW; topics: create-a-new-profile,verification,architecture-boundary,load-order-and-customization-consequences,required-profile-contract,institution-names-and-watermark,generic-and-ncku-department-apis,illustrative-ntu-wiring,cover-wording-and-date-tokens,certificate-wording-and-semantic-degree,committee-size-policy,date-policy-and-raw-resolved-state,2-x-compatibility-adapter,troubleshooting -->

[繁體中文](Customization.md) | [English](Customization.en.md)

# 其他學校樣式自訂

其他學校的同學可先複製起始檔案、改名、登記並選擇學校樣式，再建置及檢查結果。文件語言、學校樣式、封面語言、學位及內容模式分別設定；起始檔案不代表已符合任何學校規定。

## 建立學校樣式

以下以 `UnivAbc` 為例。先在含有 `thesis.tex` 的專案目錄複製並改名：

```bash
cp -R template/style/custom template/style/UnivAbc
mv template/style/UnivAbc/custom.tex template/style/UnivAbc/UnivAbc.tex
```

開啟 `template/style/UnivAbc/UnivAbc.tex`，將原有的登記指令改成以下內容，只保留一次：

```tex
\RegisterTemplateStyle{UnivAbc}
```

選擇方式有兩種，擇一即可。若維護整份學校專案，將 `template/style/style.tex` 原有的預設 `ncku` 那一行改成：

```tex
\providecommand{\TemplateStyleName}{UnivAbc}
```

若只想讓某份主文件選用此樣式，在該文件的 `\input{./template/configure}` 之前加入：

```tex
\def\TemplateStyleName{UnivAbc}
```

名稱、目錄及檔名的大小寫必須完全一致。在 `UnivAbc.tex` 設定學校版面、校名、封面與證明書文字、日期規則及浮水印；學生資料仍填在 `conf/conf.tex`。

第一次建置前，將 `conf/conf.tex` 原有的成大 `\SetDept...` 指令換成通用 `\SetCollName`、`\SetDeptName`，或自己學校已定義的系所指令；出廠檔案的系所選擇在第 148 行。下文提供設定範例。從最小可建置設定開始，再依校規逐項調整。`custom` 只是起始範例，不是任何學校可直接送審的格式。

## 建置及檢查

完成登記、選擇樣式及必要設定後，從含有 `thesis.tex` 的目錄執行：

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
```

Overleaf 選 XeLaTeX，主文件設為 `thesis.tex`；編輯器使用相同主文件與 XeLaTeX/BibTeX 建置流程。

確認 PDF 為 A4，並逐項檢查樣式登記、學校及系所名稱、日期、委員人數、碩博士與中英文輸出。其他學校的輸出不應混入成大文字或浮水印。最後確認引用及文獻已完成更新，封面與證明書頁沒有缺字、截斷或重疊；各欄位與規則的設定方式見下文。

## 架構邊界

學生論文資料放在 `conf/conf.tex`。學校的版面、日期規則、名稱、封面與證明書文字、系所清單及浮水印規定放在 `template/style/<profile>/`，不要建立 `conf/style.tex`。`template/style/style.tex` 每次只載入一個學校樣式，不會先載入成大設定再由自訂檔案覆蓋。

以下是專案內各目錄的用途：

```text
template/command/        reusable public helpers, state, and renderer mechanisms
template/compat/v1.tex   1.x compatibility adapter throughout 2.x
template/cover/          shared cover renderer
template/oral/           shared certificate renderer
template/style/base/     profile contract and wording tokens
template/style/ncku/     NCKU data, geometry, date policy, and watermark asset
template/style/custom/   directly buildable other-institution skeleton
```

## 載入順序與自訂影響

`template/configure.tex` 依下列順序載入。調換順序會影響哪些指令可用，以及論文資料何時生效：

```text
template/configure.tex
1. template/command/command.tex
   - generic public setters, state, and renderer mechanisms
   - template/compat/v1.tex -> generic/deprecated adapters only
2. template/style/style.tex
   - template/style/base/base.tex
   - exactly one selected institution profile
     - ncku/ncku.tex -> NCKU college/department catalogue and policy
     - custom/custom.tex -> neutral policy with no NCKU catalogue
3. \TemplateConfigurationFile (default: ./conf/conf)
   - student metadata selects one profile-owned catalogue entry
4. \FillInPDFData and remaining metadata/render initialization
```

通用指令先載入，學校樣式才能呼叫它們及設定規則。學校樣式再先於學生設定載入，`conf/conf.tex` 才能使用該校提供的系所指令；未修改的成大設定因此仍可呼叫 `\SetDeptCSIE`。不要讓 `compat/v1.tex` 在選擇學校前載入成大清單，否則 `custom` 會混入成大資料。

學校樣式負責定義可重用的系所指令，學生在 `conf/conf.tex` 選擇自己的系所。不要在學校樣式內固定某位學生的系所。改用其他學校時，須將原有成大 `\SetDept...` 換成通用 `\SetDeptName` 或該校專用指令；若仍呼叫不存在的成大指令，建置會以未定義指令錯誤停止，避免輸出錯誤校名。

`\TemplateConfigurationFile` 預設為 `./conf/conf`；只有完整儲存庫中的自訂樣式測試會改用獨立的通用設定檔，保留原有 V1 設定檔不變。一般專案不需修改此路徑。學生設定不可先於學校樣式，也不要將成大清單移回通用指令或相容層。`\FillInPDFData` 及後續初始化須在學生設定之後，才能取得最終資料。

## 樣式必備設定

每個學校樣式須恰好呼叫一次 `\RegisterTemplateStyle{<name>}`，設定正文版面，並定義封面開始及結束時切換版面的指令。校名、封面與證明書文字及浮水印行為也要明確設定。只有校規不同時才改寫對應的規則函式，不要改寫學生用的公開資料設定指令。

在 `UnivAbc.tex` 中修改或替換從 `custom.tex` 複製的版面設定，以及既有的 `\EnableCoverPageStyle`、`\DisableCoverPageStyle` 定義，不要另行附加重複定義。下方範例示意要修改的內容，尺寸仍須依自己的校規調整：

```tex
\geometry{a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead}

\newcommand{\EnableCoverPageStyle}{%
  \newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead,nofoot}%
}
\newcommand{\DisableCoverPageStyle}{\restoregeometry}
```

找不到樣式或登記名稱不符時，建置必須停止，不可自動改用成大設定。

## 學校名稱與浮水印

以下示範直接設定中英文名稱。固定校名可放在 `UnivAbc.tex`；學院與系所由學生在 `conf/conf.tex` 選擇。可使用通用 `\SetCollName`、`\SetDeptName`，或改用學校樣式提供的專用指令，兩種方式擇一。

浮水印樣式放在 `UnivAbc.tex`。沒有合法可再發佈的學校圖片時，保持空白。`\SetWatermaskFigureStyle`／`\SetWatermaskTextStyle` 只定義樣式，`\UseWatermarkFigureStyle`／`\UseWatermarkTextStyle` 才會啟用；不要因指令可用就加上浮水印，正式提交須依學校及圖書館現行規定。

```tex
\SetUniversityName{範例大學}{Example University}
\SetCollName{範例學院}{Example College}
\SetDeptName{測試學系}{TEST}{Department of Testing}

% Safe neutral defaults / 安全neutral defaults
\SetWatermaskFigureStyle{}
\SetWatermaskTextStyle{}
```

## 通用與成大系所指令

跨校可使用 `\SetUniversityName{中文}{English}`、`\SetCollName{中文}{English}` 及 `\SetDeptName{中文}{英文縮寫}{English full name}`。讀取資料的指令分別為 `\GetUniversityChiName`／`\GetUniversityEngName`、`\GetCollChiName`／`\GetCollEngName`、`\GetDeptChiName`／`\GetDeptEngShortName`／`\GetDeptEngName`。

本範本另提供 9 個成大學院指令及 110 個成大系所指令，涵蓋系、研究所、學位學程與中心。`\SetDeptCSIE` 等指令會同時設定系所及一個成大學院；完整清單見 [`ncku/README.md`](ncku/README.md)。它們只在 `ncku` 樣式下提供，`custom` 不會定義這些指令。其他學校應以自己的名稱作為指令前綴，例如 `\SetNTUDept...`，不要沿用成大 `\SetDept...` 名稱。

縮寫相同不代表資料相同。成大 `\SetDeptCSIE` 設定的是 `資訊工程研究所` 及 `Institute of Computer Science and Information Engineering`；下方臺大範例則是 `資訊工程學系` 及 `Department of Computer Science and Information Engineering`。不能只因都使用 `CSIE` 就共用系所設定。

## 臺大設定示範：不是完整格式

以下只示範通用指令及命名方式，**不是可提交的臺大論文格式**，本專案目前沒有臺大樣式。依 2026-07-19 查核的臺大官方[中文學位論文格式規範](https://www.lib.ntu.edu.tw/doc/cl/THESISSAMPLE.pdf)、[英文格式指南](https://www.lib.ntu.edu.tw/doc/CL/thesissample_en.pdf)及[臺大資工系頁面](https://www.csie.ntu.edu.tw/en/AboutUs)，完整格式仍須實作封面、書脊、書名頁、審定書、正文邊界、字型、行距、日期及各院系所附加規定。只替換校名、學院及系所，不能證明符合規範。

可先由 `custom` 複製出 `template/style/ntu/ntu.tex`，將登記名稱及 `TemplateStyleName` 改為 `ntu`，再依官方規範逐項調整。以下第一段定義放在學校樣式檔；註解標示 `conf/conf.tex` 的最後一行放在學生設定檔，取代原有成大系所指令：

```tex
% template/style/ntu/ntu.tex
% Illustrative API wiring only. This is not a complete NTU profile.
\SetUniversityName{國立臺灣大學}{National Taiwan University}
\newcommand{\SetNTUDeptCSIE}{%
  \SetDeptName{資訊工程學系}{CSIE}{Department of Computer Science and Information Engineering}%
  \SetCollName{電機資訊學院}{College of Electrical Engineering and Computer Science}%
}

% conf/conf.tex: replace the existing NCKU department selection.
\SetNTUDeptCSIE
```

學校樣式只定義可重用指令，不直接固定某位學生的系所。完成名稱設定後，仍須核對正文與封面尺寸、書脊、碩博士文字、證明書、西元及民國日期、浮水印與 DOI 處理，以及圖片再發佈權。差異應放在 `ntu` 樣式，不要修改共用排版程式。

## 封面文字與日期

以下文字設定放在學校樣式檔，供共用排版程式取得學生、指導教授稱謂、前後綴與碩博士英文日期格式。`\SetCoverDate{year}{month}` 不含日期中的日，通用博士封面不能借用獨立口試資料中的日；若校規確實要求，才在博士日期格式中明確加入 `\GetOralEngDay`。

```tex
\SetCoverStudentChiBothText{學生}
\SetCoverStudentChiText{研究生}
\SetCoverStudentEngText{Student}
\SetCoverAdvisorChiText{指導老師}
\SetCoverAdvisorEngText{Advisor}
\SetCoverCoAdvisorChiText{共同指導}
\SetCoverCoAdvisorEngText{Co-Advisor}
\SetCoverAdvisorChiSuffix{博士}
\SetCoverAdvisorEngPrefix{Dr.}
\SetCoverDateChiPrefix{西元}
\SetCoverMasterDateEng{\GetThesisMonthInEng \thinspace \GetThesisYear}
\SetCoverDoctoralDateEng{\GetThesisMonthInEng \thinspace \GetThesisYear}
```

讀取資料的指令後接文字時，若原有格式需要空格，請明確加入 `\space`。

## 證明書文字與學位判斷

以下設定放在學校樣式檔，提供地點、審查、委員、指導教授、主管及碩博士送審文字。英文證明書依數值 `\GetFlagDegreeType` 選擇碩士或博士內容，不以可自訂的學位顯示文字判斷，因此更改學位名稱不會誤選格式。即使目前只用英文範例，也要完整設定兩種語言，避免日後切換時缺字。

```tex
\SetInstitutionLocationEng{Example City, Example Country}
\SetOralApprovalChiText{本論文業經審查及口試合格特此證明}
\SetOralApprovedByEngText{Approved by}
\SetOralCommitteeChiText{論文考試委員}
\SetOralAdvisorChiText{指導教授}
\SetOralChairChiText{系(所)主管}
\SetOralChairEngText{Chair}
\SetOralDateChiPrefix{西元}
\SetOralAuthorByEngText{prepared by}
\SetOralMasterSubmissionEngText{Example master's submission in}
\SetOralDoctoralSubmissionEngText{Example doctoral submission in}
```

範本產生的證明書只供示範及測試，不是學校正式文件；提交時須使用學校規定的正式版本。

## 口試委員人數

共用排版程式支援 2 至 9 個簽名欄，通用 `custom` 樣式預設保留此範圍。`\SetCommitteeSize{n}` 的用法不變。只有校規按學位限制人數時，才在學校樣式改寫 `\ApplyCommitteeSizePolicy{n}`，並用 `\GetFlagDegreeType` 判斷學位，不比較顯示文字。

成大碩士範圍為 3–5 人，博士為 5–9 人，超出範圍的要求會調整到界限內。使用者先選學位，再設定委員人數。其他學校若無此規定，不必改寫函式；排版可容納的人數與校規應分開處理。

## 日期規則與顯示值

公開用法仍是 `\SetOralDate{year}{month}{day}` 及 `\SetCoverDate{year}{month}`。通用規則分別保存口試與封面日期，中文預設顯示西元年。成大則以口試日期決定封面日期，並顯示民國年。其他學校如有相同要求，只改寫日期規則函式及顯示指令，不要以 `\renewcommand` 改寫公開設定指令。

`\GetRequestedCoverYear`／`\GetRequestedCoverMonth` 讀取原始輸入；`\GetThesisYear`／`\GetThesisMonth` 讀取依學校規則決定的顯示值。

以下放在學校樣式檔，示範以口試日期決定封面年月的規則；沒有此規定時保留兩者獨立：

```tex
\renewcommand{\ApplyOralDatePolicy}[3]{%
  \SetThesisTaiwanYear{#1}%
  \renewcommand{\ThesisYear}{#1}%
  \renewcommand{\ThesisMonth}{#2}%
}
\renewcommand{\ApplyCoverDatePolicy}[2]{}
```

需要民國年時，亦須在學校樣式明確設定對應的換算與顯示指令，不要把換算放進通用設定指令。

## 2.x相容層

`template/compat/v1.tex` 在整個 2.x 期間載入通用及舊版相容指令。成大學院與系所指令只由 `ncku` 樣式載入；未修改的 1.x 成大專案仍使用此預設樣式，因此原指令保持可用。舊路徑 `template/command/cmd-college.tex` 及 `cmd-department.tex` 只保留直接載入時的相容用途，不會自動進入 `custom` 的載入流程。

`template/compat/deprecated.tex` 保留 23 個已於 1.x 停用的公開指令，維持原名、錯誤訊息及 `\stop`。有效的一參數 `\RefTo{label}` 仍可使用，不會被歷史註解中的停用宣告取代。

`custom` 只載入通用學校資料設定，不載入成大系所、版面、日期規則或浮水印圖片。相容性保留正確用法，不要求保留已證實的錯誤。

## 故障處理

出現 `Template style file ... was not found` 時，檢查目錄、檔名與 `\TemplateStyleName` 的大小寫。出現 `did not register itself` 時，確認學校樣式檔恰好呼叫一次名稱相符的 `\RegisterTemplateStyle`。

其他學校的輸出若混入成大文字或圖片，檢查是否直接載入成大樣式、複製後遺留成大規則，或在共用排版程式內寫死學校資料。修正自己的學校樣式，不要另加覆蓋層掩蓋問題。
