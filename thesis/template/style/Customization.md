<!-- doc-pair: style-customization; lang: zh-Hant-TW; topics: architecture-boundary,create-a-new-profile,required-profile-contract,institution-names-and-watermark,generic-and-ncku-department-apis,illustrative-ntu-wiring,cover-wording-and-date-tokens,certificate-wording-and-semantic-degree,committee-size-policy,date-policy-and-raw-resolved-state,2-x-compatibility-adapter,verification,troubleshooting -->

[繁體中文](Customization.md) | [English](Customization.en.md)

# 其他學校樣式自訂

本模版將通用thesis helpers與學校規範分開，讓其他學校的同學可保留template capabilities，同時建立自己學校的institution format。文件語言、封面語言與institution profile是獨立決定。

## 架構邊界

學生論文資料仍放在`conf/conf.tex`。學校層級的geometry、日期規則、校名、封面／證明書文字、department catalogues及watermark policy放在`template/style/<profile>/`；不要建立`conf/style.tex`。`template/style/style.tex`每次只載入一個profile；本模版不會先載入NCKU再用custom file覆寫。

```text
template/command/        reusable public helpers, state, and renderer mechanisms
template/compat/v1.tex   1.x compatibility adapter throughout 2.x
template/cover/          shared cover renderer
template/oral/           shared certificate renderer
template/style/base/     profile contract and wording tokens
template/style/ncku/     NCKU data, geometry, date policy, and watermark asset
template/style/custom/   directly buildable other-institution skeleton
```

## 建立新Profile

以下以`UnivAbc`為例。由neutral `custom` skeleton複製，將profile file改名，登記同一名稱，再由`\TemplateStyleName`選擇。Profile名稱及path大小寫必須完全一致。

```bash
cp -R template/style/custom template/style/UnivAbc
mv template/style/UnivAbc/custom.tex template/style/UnivAbc/UnivAbc.tex
```

```tex
\RegisterTemplateStyle{UnivAbc}
```

```tex
\providecommand{\TemplateStyleName}{UnivAbc}
```

```tex
\def\TemplateStyleName{UnivAbc}
```

## 必要Profile Contract

每個profile必須恰好呼叫一次`\RegisterTemplateStyle{<name>}`、設定body geometry、定義cover-page geometry enable/disable hooks、設定校名及cover/oral tokens、明確選擇watermark behavior，並只在有不同學校規定時override policy hooks。不要override public metadata setters。

```tex
\geometry{a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead}

\newcommand{\EnableCoverPageStyle}{%
  \newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead,nofoot}%
}
\newcommand{\DisableCoverPageStyle}{\restoregeometry}
```

## 學校名稱與浮水印

使用通用setters提供中英文學校、學院及系所名稱。沒有可合法再發佈的institution asset時，保持watermark style為空。`\SetWatermaskFigureStyle`／`\SetWatermaskTextStyle`只定義style；`\UseWatermarkFigureStyle`／`\UseWatermarkTextStyle`才啟用。正式提交前依該校及圖書館現行規定處理，不要因API存在便加入浮水印。

```tex
\SetUniversityName{範例大學}{Example University}
\SetCollName{範例學院}{Example College}
\SetDeptName{測試學系}{TEST}{Department of Testing}

% Safe neutral defaults / 安全neutral defaults
\SetWatermaskFigureStyle{}
\SetWatermaskTextStyle{}
```

## Generic與NCKU系所API

跨校可重用contract是`\SetUniversityName{中文}{English}`、`\SetCollName{中文}{English}`及`\SetDeptName{中文}{英文縮寫}{English full name}`。對應getters為`\GetUniversityChiName`／`\GetUniversityEngName`、`\GetCollChiName`／`\GetCollEngName`、`\GetDeptChiName`／`\GetDeptEngShortName`／`\GetDeptEngName`。

本模版另外保存9個NCKU college presets及110個NCKU department presets；department slot實際涵蓋系、研究所、學位學程及中心。`\SetDeptCSIE`等shortcut不只寫入department，亦會呼叫一個NCKU college preset；完整source-checked目錄見[`ncku/README.md`](ncku/README.md)。即使2.x compatibility adapter令custom build仍會定義這些commands，其他學校的同學亦不應使用。可重用的新catalogue應使用學校prefix，例如`\SetNTUDept...`，不要重新定義保留中的NCKU `\SetDept...` names。

同一縮寫亦不代表資料相同：目前NCKU `\SetDeptCSIE` source寫入`資訊工程研究所`及`Institute of Computer Science and Information Engineering`，而以下NTU example使用`資訊工程學系`及`Department of Computer Science and Information Engineering`。因此不能因兩校都使用`CSIE`便共用preset。

## Illustrative NTU Wiring（不是完整NTU Profile）

以下只示範generic API及command namespace，**不是可提交的NTU論文格式**。本專案目前沒有NTU profile。2026-07-19檢查的NTU官方[中文學位論文格式規範](https://www.lib.ntu.edu.tw/doc/cl/THESISSAMPLE.pdf)、[English format guide](https://www.lib.ntu.edu.tw/doc/CL/thesissample_en.pdf)及[NTU CSIE官方頁面](https://www.csie.ntu.edu.tw/en/AboutUs)顯示，真正NTU port仍須實作封面／書脊、書名頁、審定書、body margins、字體／行距、日期及各院系所附加規定。只替換校名、學院及系所不足以證明compliance。

NTU fork可先複製`custom`為`template/style/ntu/ntu.tex`，將registration及`TemplateStyleName`改為`ntu`，再按官方規範替換skeleton policy。系所shortcut使用NTU prefix，避免與2.x保留的NCKU namespace衝突：

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

Profile負責定義可重用catalogue；每位學生在`conf/conf.tex`選擇自己的系所。不要在profile內直接固定某一個系所，也不要保留原本的NCKU `\SetDept...` selection。完成names wiring後，仍要逐項核對body／cover geometry、spine、Master／Doctoral wording、oral certificate、Gregorian／民國日期顯示、watermark／DOI處理及assets再發佈權；每個差異都應留在`ntu` profile，而不是改共用renderer。

## 封面文字與日期Tokens

共用renderer從profile token setters取得student/advisor labels、prefix/suffix及Master／Doctoral English date format。`\SetCoverDate{year}{month}`沒有day，因此neutral Doctoral cover不可從independent oral metadata借day。若institution規定需要oral day，profile必須在自己的Doctoral date token中明確加入`\GetOralEngDay`。

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

## 證明書文字與Semantic Degree

Profile提供location、approval、committee、advisor、chair及Master／Doctoral submission wording。English certificate renderer使用numeric `\GetFlagDegreeType`選擇Master／Doctoral branch，不比較可自訂的display degree text。因此profile可更改degree名稱而不會進入錯誤branch。即使目前只使用英文certificate，仍應完整設定兩種語言的contract，避免之後切換出現空白label。

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

## 口試委員政策

Generic renderer支援2至9個簽名欄位，neutral/custom profile預設保留此範圍。`\SetCommitteeSize{n}`的public signature不變；若institution按學位限制不同範圍，profile只override `\ApplyCommitteeSizePolicy{n}`，並以`\GetFlagDegreeType`判斷semantic Master／Doctoral state，不比較display text。

NCKU profile把Master requests收斂至3–5、Doctoral requests收斂至5–9。使用者先呼叫degree setter，再設定committee size。其他profile沒有degree-specific規定時不需override hook。

## 日期政策與Raw/Resolved State

Public commands保持`\SetOralDate{year}{month}{day}`及`\SetCoverDate{year}{month}`。Generic policy把兩者保存為獨立metadata，Chinese renderers預設使用Gregorian year。NCKU profile透過hooks將oral date視為authoritative cover date並選擇民國年。其他學校的同學如有相同規定，只override policy hooks及display getters；不要`\renewcommand` public setters。

`\GetRequestedCoverYear`／`\GetRequestedCoverMonth`回傳raw user input；`\GetThesisYear`／`\GetThesisMonth`回傳profile解決後的display values。

```tex
\renewcommand{\ApplyOralDatePolicy}[3]{%
  \SetThesisTaiwanYear{#1}%
  \renewcommand{\ThesisYear}{#1}%
  \renewcommand{\ThesisMonth}{#2}%
}
\renewcommand{\ApplyCoverDatePolicy}[2]{}
```

## 2.x相容層

`template/compat/v1.tex`在整個2.x line載入，既有NCKU college／department presets仍然defined。Data ownership已移至`template/style/ncku/`，舊command paths只是wrappers。`template/compat/deprecated.tex`保存23個已於1.x停用的public commands，維持原名、diagnostic及`\stop`。有效的一參數`\RefTo{label}`仍在active command file，不會被historical comment-only tombstone取代。

Custom profile的source graph因此仍define NCKU legacy presets，但不載入NCKU geometry、date policy、watermark asset，也不應在visible output顯示NCKU內容。這是有意保留的2.x source-level compatibility cost；不要透過刪除舊API來「清理」。

## 驗證

學生套件內沒有`justfile`、`scripts/`或`tests/`；從包含`thesis.tex`的project root使用direct XeLaTeX/latexmk。完整repository則執行focused custom-style、API、V1 migration及full gates。Custom fixture應以不同oral/cover dates同時建置Chinese/English Master及Doctoral branches，確認沒有NCKU visible policy或watermark asset。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
```

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
```

## 故障處理

如出現`Template style file ... was not found`，檢查directory、filename及`\TemplateStyleName`大小寫。如出現`did not register itself`，確認profile file呼叫一次相同名稱的`\RegisterTemplateStyle`。如custom output出現NCKU文字或asset，檢查是否直接input NCKU profile、從NCKU複製後漏刪policy，或在generic renderer硬編碼institution values。

任何output regression均先回到最後可建置commit，一次重套一個profile change；不要停用tests、降低expected counts或改compatibility manifests。
