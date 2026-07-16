# Style Customization 自定成其他學校的模版

由 v1.5.0 開始，本模版的方向就是把通用 thesis helpers 與學校規範分開，讓非國立成功大學的使用者可以保留模版功能，同時維護自己學校的格式。V2 正式將這個設計落實成 **institution style profile**。

## V2 邊界

```text
template/command/        通用 public helpers、state 與 renderer mechanism
template/compat/v1.tex   2.x 的 1.x helper compatibility adapter
template/cover/          共用封面 renderer
template/oral/           共用口試證明 renderer
template/style/base/     profile contract 與文字 tokens
template/style/ncku/     NCKU data、geometry、date policy、watermark asset
template/style/custom/   可直接 build 的 non-NCKU skeleton
```

學生論文資料仍放在 `conf/conf.tex`。學校層級的 geometry、日期規則、校名、封面／口試文字與 watermark policy 應放在 `template/style/<profile>/`，**不要建立 `conf/style.tex`**。

`template/style/style.tex` 每次只會載入一個 profile。V2 不再先載入 NCKU，再用 custom file 覆蓋 NCKU policy。

## 建立新學校 Profile

以下以 `UnivAbc` 為例。

1. 複製 neutral skeleton：

   ```bash
   cp -R template/style/custom template/style/UnivAbc
   mv template/style/UnivAbc/custom.tex template/style/UnivAbc/UnivAbc.tex
   ```

2. 在 `UnivAbc.tex` 將：

   ```tex
   \RegisterTemplateStyle{custom}
   ```

   改成：

   ```tex
   \RegisterTemplateStyle{UnivAbc}
   ```

3. 在 institutional fork 的 `template/style/style.tex` 將預設值改成：

   ```tex
   \providecommand{\TemplateStyleName}{UnivAbc}
   ```

   測試時亦可在 `\input{./template/configure}` **之前**暫時指定：

   ```tex
   \def\TemplateStyleName{UnivAbc}
   ```

4. 修改 `UnivAbc.tex` 的 geometry、校名、文字 tokens、date policy 與 watermark style。

5. 在 `conf/conf.tex` 使用通用 metadata helpers，例如：

   ```tex
   \SetUniversityName{範例大學}{Example University}
   \SetCollName{範例學院}{Example College}
   \SetDeptName{測試學系}{TEST}{Department of Testing}
   \SetTitle{中文題目}{English Title}
   \SetMyName{學生姓名}{Student Name}
   \SetAdvisorNameA{老師姓名}{Advisor Name}
   ```

   非 NCKU profile 不應使用 `\SetDeptCSIE`、`\SetCollEng` 等 NCKU catalog presets；這些 commands 在 2.x 仍存在只為兼容舊專案。

6. 使用 XeLaTeX／latexmk build，並檢查封面、口試日期、front matter、references 與最後頁。

## Profile 必要 Contract

每個 profile 必須：

- 呼叫一次 `\RegisterTemplateStyle{<name>}`；
- 設定 body geometry；
- 定義 `\EnableCoverPageStyle` 與 `\DisableCoverPageStyle`；
- 設定校名；
- 設定 cover/oral text tokens；
- 明確選擇 watermark behavior；
- 如學校日期規則不同，只覆寫 policy hooks，不覆寫 public setters。

### Geometry

```tex
\geometry{a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead}

\newcommand{\EnableCoverPageStyle}{%
  \newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead,nofoot}%
}
\newcommand{\DisableCoverPageStyle}{\restoregeometry}
```

### 校名與 Watermark

```tex
\SetUniversityName{範例大學}{Example University}

% 無 institutional asset 的安全預設
\SetWatermaskFigureStyle{}
\SetWatermaskTextStyle{}
```

`\SetWatermaskFigureStyle`／`\SetWatermaskTextStyle`只定義樣式；`\UseWatermarkFigureStyle`／`\UseWatermarkTextStyle`才會啟用。正式提交前應依當時學校／圖書館規定決定，不應因 API 存在就自動加入 watermark。

### Cover 文字 Tokens

共用 renderer 透過以下 setters 取得 institution wording：

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
```

對應 oral certificate 的 profile setters 包括：

```tex
\SetInstitutionLocationEng{Example City, Example Country}
\SetOralApprovalChiText{本論文業經審查及口試合格特此證明}
\SetOralApprovedByEngText{Approved by}
\SetOralCommitteeChiText{論文考試委員}
\SetOralAdvisorChiText{指導教授}
\SetOralChairChiText{系(所)主管}
\SetOralChairEngText{Chair}
\SetOralDateChiPrefix{西元}
```

如只使用英文 oral certificate，仍建議完整設定 contract，避免其他使用者切換語言時出現空白 label。

### 日期 Policy

Public commands 保持不變：

```tex
\SetOralDate{year}{month}{day}
\SetCoverDate{year}{month}
```

Generic/default policy 將 `\SetCoverDate`視為封面日期，並將 oral date 保持為獨立 metadata。Generic Chinese cover/oral renderers使用Gregorian year；`\SetCoverDateChiPrefix`與`\SetOralDateChiPrefix`控制顯示prefix。NCKU profile則透過hooks/getters將口試合格日期視為authoritative cover date，並明確選擇民國年。

如果另一間學校亦使用oral date作封面日期，只覆寫hooks：

```tex
\renewcommand{\ApplyOralDatePolicy}[3]{%
  \SetThesisTaiwanYear{#1}%
  \renewcommand{\ThesisYear}{#1}%
  \renewcommand{\ThesisMonth}{#2}%
}
\renewcommand{\ApplyCoverDatePolicy}[2]{}
```

如果profile需要民國年，亦必須明確覆寫Chinese-year policy/display getters；唔好將台灣年轉換留喺generic setters：

```tex
\renewcommand{\ApplyOralChiYearPolicy}[1]{%
  \renewcommand{\OralChiYear}{\OralTaiwanYearResult}%
}
\renewcommand{\GetCoverMasterYearChi}{\GetThesisYearInTaiwanYear}
\renewcommand{\GetCoverMasterYearNumInChi}{\zhnumber{\GetThesisYearInTaiwanYear}}
\renewcommand{\GetCoverDoctoralYearChi}{\GetOralYearInTaiwanYear}
\renewcommand{\GetCoverDoctoralYearNumInChi}{\GetOralYearInTaiwanYearNumInChi}
```

不要 `\renewcommand{\SetOralDate}` 或 `\renewcommand{\SetCoverDate}`；public setter 需要繼續保存 raw metadata 與維持 1.x signature。

`\GetRequestedCoverYear`、`\GetRequestedCoverMonth`可取得使用者傳給 `\SetCoverDate` 的原始值；`\GetThesisYear`、`\GetThesisMonth`則是 profile policy 解決後的顯示值。

## 2.x Compatibility Adapter

`template/compat/v1.tex`在整個 2.x line 都會載入，確保既有 NCKU college／department preset commands 仍可用。其 data files 已移到 `template/style/ncku/`，舊的 `template/command/cmd-college.tex`與`cmd-department.tex`路徑保留為 wrappers。

因此 custom profile 的 source graph 仍會定義 NCKU legacy presets；但它不會載入 NCKU geometry、date policy 或 watermark asset，也不會在 visible output 顯示 NCKU 內容。這是刻意的 2.x compatibility cost，不應以刪除舊 API 的方式「清理」。

## 驗證

完整 repository 可執行：

```bash
just _test-custom-style
just test
just ci
python3 scripts/test/check-v1-api.py
```

不依賴 `just` 的直接 build 仍然是：

```bash
cd thesis
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

`tests/custom-style.tex`是可執行reference：它選擇`custom` profile、產生中／英文cover與oral certificate共四頁A4、驗證Chinese dates使用Gregorian year、保持不同cover/oral dates，並確認output沒有NCKU校名或watermark asset。

## 不應修改的地方

優先使用 profile contract 與 `conf/conf.tex` public helpers。只有當共用 renderer 缺少真正跨學校需要的 hook，而且有 focused fixture 證明時，才修改 `template/command/`、`template/cover/`或`template/oral/`。

1.x 專案升級請同時閱讀 [`../../MIGRATION-1.x-TO-2.x.md`](../../MIGRATION-1.x-TO-2.x.md)。
