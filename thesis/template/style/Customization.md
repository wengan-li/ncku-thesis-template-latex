<!-- bilingual:complete -->

# 其他學校樣式自訂 / Institution style customization

V2將通用thesis helpers與學校規範分開，讓非成大維護者可保留template capabilities，同時維護自己的institution format。文件語言、封面語言與institution profile是獨立決定。

V2 separates reusable thesis helpers from institution policy so non-NCKU maintainers can retain template capabilities while maintaining their own institution format. Documentation language, cover language, and institution profile are independent decisions.

## 架構邊界 / Architecture boundary

**繁體中文**

學生論文資料仍放在`conf/conf.tex`。學校層級的geometry、日期規則、校名、封面／證明書文字、department catalogues及watermark policy放在`template/style/<profile>/`；不要建立`conf/style.tex`。`template/style/style.tex`每次只載入一個profile，V2不會先載入NCKU再用custom file覆寫。

**English**

Student thesis data remains in `conf/conf.tex`. Institution geometry, date rules, names, cover/certificate wording, department catalogues, and watermark policy belong under `template/style/<profile>/`; do not create `conf/style.tex`. `template/style/style.tex` loads exactly one profile. V2 does not load NCKU first and then override it with a custom file.

```text
template/command/        reusable public helpers, state, and renderer mechanisms
template/compat/v1.tex   1.x compatibility adapter throughout 2.x
template/cover/          shared cover renderer
template/oral/           shared certificate renderer
template/style/base/     profile contract and wording tokens
template/style/ncku/     NCKU data, geometry, date policy, and watermark asset
template/style/custom/   directly buildable neutral/non-NCKU skeleton
```

## 建立新Profile / Create a new profile

**繁體中文**

以下以`UnivAbc`為例。由neutral `custom` skeleton複製，將profile file改名，登記同一名稱，再由`\TemplateStyleName`選擇。Profile名稱及path大小寫必須完全一致。

**English**

The following example uses `UnivAbc`. Copy the neutral `custom` skeleton, rename the profile file, register the same name, and select it through `\TemplateStyleName`. Profile name and path casing must match exactly.

```bash
cp -R template/style/custom template/style/UnivAbc
mv template/style/UnivAbc/custom.tex template/style/UnivAbc/UnivAbc.tex
```

In `UnivAbc.tex` / 在`UnivAbc.tex`：

```tex
\RegisterTemplateStyle{UnivAbc}
```

In an institutional fork's `template/style/style.tex` / 在institutional fork內：

```tex
\providecommand{\TemplateStyleName}{UnivAbc}
```

For a focused test, define the profile before `\input{./template/configure}` / 測試時可在載入configure前指定：

```tex
\def\TemplateStyleName{UnivAbc}
```

Modify institution geometry, names, wording tokens, date policy, and watermark style in `UnivAbc.tex`. Keep student metadata in `conf/conf.tex`.

## 必要Profile Contract / Required profile contract

**繁體中文**

每個profile必須恰好呼叫一次`\RegisterTemplateStyle{<name>}`、設定body geometry、定義cover-page geometry enable/disable hooks、設定校名及cover/oral tokens、明確選擇watermark behavior，並只在有不同學校規定時override policy hooks。不要override public metadata setters。

**English**

Every profile must call `\RegisterTemplateStyle{<name>}` exactly once, set body geometry, define cover-page geometry enable/disable hooks, set institution names and cover/oral tokens, choose watermark behavior explicitly, and override policy hooks only when institution rules differ. Do not override public metadata setters.

```tex
\geometry{a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead}

\newcommand{\EnableCoverPageStyle}{%
  \newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead,nofoot}%
}
\newcommand{\DisableCoverPageStyle}{\restoregeometry}
```

Build a minimal profile before adding institution-specific refinements. A missing profile or registration-name mismatch must fail rather than silently falling back to NCKU.

## 學校名稱與浮水印 / Institution names and watermark

**繁體中文**

使用通用setters提供中英文學校、學院及系所名稱。沒有可合法再發佈的institution asset時，保持watermark style為空。`\SetWatermaskFigureStyle`／`\SetWatermaskTextStyle`只定義style；`\UseWatermarkFigureStyle`／`\UseWatermarkTextStyle`才啟用。正式提交前依該校及圖書館現行規定處理，不要因API存在便加入浮水印。

**English**

Use generic setters for Chinese and English institution, college, and department names. Keep watermark styles empty when no redistributable institution asset is available. `\SetWatermaskFigureStyle` / `\SetWatermaskTextStyle` define styles; `\UseWatermarkFigureStyle` / `\UseWatermarkTextStyle` enable them. Follow the institution's current submission rules and do not add a watermark merely because an API exists.

```tex
\SetUniversityName{範例大學}{Example University}
\SetCollName{範例學院}{Example College}
\SetDeptName{測試學系}{TEST}{Department of Testing}

% Safe neutral defaults / 安全neutral defaults
\SetWatermaskFigureStyle{}
\SetWatermaskTextStyle{}
```

The second `\SetDeptName` argument is the English abbreviation returned by `\GetDeptEngShortName`; the third is the full name returned by `\GetDeptEngName`.

## 封面文字與日期Tokens / Cover wording and date tokens

**繁體中文**

共用renderer從profile token setters取得student/advisor labels、prefix/suffix及Master／Doctoral English date format。`\SetCoverDate{year}{month}`沒有day，因此neutral Doctoral cover不可從independent oral metadata借day。若institution規定需要oral day，profile必須在自己的Doctoral date token中明確加入`\GetOralEngDay`。

**English**

The shared renderer obtains student/advisor labels, prefixes/suffixes, and Master/Doctoral English date formats from profile token setters. `\SetCoverDate{year}{month}` owns no day, so a neutral Doctoral cover must not borrow one from independent oral metadata. If institution policy requires the oral day, the profile must explicitly include `\GetOralEngDay` in its Doctoral date token.

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

Use explicit `\space` where a control-word getter meets following text and the old contract included a visible space.

## 證明書文字與Semantic Degree / Certificate wording and semantic degree

**繁體中文**

Profile提供location、approval、committee、advisor、chair及Master／Doctoral submission wording。English certificate renderer使用numeric `\GetFlagDegreeType`選擇Master／Doctoral branch，不比較可自訂的display degree text。因此profile可更改degree名稱而不會進入錯誤branch。即使目前只使用英文certificate，仍應完整設定兩種語言的contract，避免之後切換出現空白label。

**English**

The profile provides location, approval, committee, advisor, chair, and Master/Doctoral submission wording. The English certificate renderer selects its branch from numeric `\GetFlagDegreeType`, not customizable display degree text. A profile may therefore rename degrees without selecting the wrong branch. Even if only an English certificate is currently used, define the complete bilingual contract to avoid blank labels after a later language switch.

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

Template-generated certificates are demonstrations/regression outputs, not official institution documents.

## 口試委員政策 / Committee-size policy

**繁體中文**

Generic renderer支援2至9個簽名欄位，neutral/custom profile預設保留此範圍。`\SetCommitteeSize{n}`的public signature不變；若institution按學位限制不同範圍，profile只override `\ApplyCommitteeSizePolicy{n}`，並以`\GetFlagDegreeType`判斷semantic Master／Doctoral state，不比較display text。

NCKU profile把Master requests收斂至3–5、Doctoral requests收斂至5–9。使用者先呼叫degree setter，再設定committee size。其他profile沒有degree-specific規定時不需override hook。

**English**

The generic renderer supports 2–9 signature fields and neutral/custom keeps that range by default. The public `\SetCommitteeSize{n}` signature remains unchanged. If an institution has degree-specific limits, override only `\ApplyCommitteeSizePolicy{n}` and branch on semantic `\GetFlagDegreeType`, never display text.

NCKU clamps Master requests to 3–5 and Doctoral requests to 5–9. Users select the degree before committee size. Another profile needs no hook override when it has no degree-specific rule.

Keep renderer capacity and institution policy separate.

## 日期政策與Raw/Resolved State / Date policy and raw/resolved state

**繁體中文**

Public commands保持`\SetOralDate{year}{month}{day}`及`\SetCoverDate{year}{month}`。Generic policy把兩者保存為獨立metadata，Chinese renderers預設使用Gregorian year。NCKU profile透過hooks將oral date視為authoritative cover date並選擇民國年。其他學校如有相同規定，只override policy hooks及display getters；不要`\renewcommand` public setters。

`\GetRequestedCoverYear`／`\GetRequestedCoverMonth`回傳raw user input；`\GetThesisYear`／`\GetThesisMonth`回傳profile解決後的display values。

**English**

Public commands remain `\SetOralDate{year}{month}{day}` and `\SetCoverDate{year}{month}`. Generic policy keeps them as independent metadata and uses Gregorian years in Chinese renderers. NCKU hooks make the oral date authoritative for the cover and select Taiwan-year display. Another institution with the same rule overrides policy hooks and display getters, not public setters.

`\GetRequestedCoverYear` / `\GetRequestedCoverMonth` expose raw user input; `\GetThesisYear` / `\GetThesisMonth` expose profile-resolved display values.

```tex
\renewcommand{\ApplyOralDatePolicy}[3]{%
  \SetThesisTaiwanYear{#1}%
  \renewcommand{\ThesisYear}{#1}%
  \renewcommand{\ThesisMonth}{#2}%
}
\renewcommand{\ApplyCoverDatePolicy}[2]{}
```

If Taiwan-year display is required, explicitly override its policy/display getters in the profile. Do not leave Taiwan-calendar conversion inside generic setters.

## 2.x相容層 / 2.x compatibility adapter

**繁體中文**

`template/compat/v1.tex`在整個2.x line載入，既有NCKU college／department presets仍然defined。Data ownership已移至`template/style/ncku/`，舊command paths只是wrappers。`template/compat/deprecated.tex`保存23個已於1.x停用的public commands，維持原名、diagnostic及`\stop`。有效的一參數`\RefTo{label}`仍在active command file，不會被historical comment-only tombstone取代。

Custom profile的source graph因此仍define NCKU legacy presets，但不載入NCKU geometry、date policy、watermark asset，也不應在visible output顯示NCKU內容。這是有意保留的2.x source-level compatibility cost；不要透過刪除舊API來「清理」。

**English**

`template/compat/v1.tex` loads throughout 2.x so existing NCKU college/department presets remain defined. Data ownership moved under `template/style/ncku/`; old command paths are wrappers. `template/compat/deprecated.tex` preserves 23 commands already unsupported during 1.x with the same names, diagnostics, and `\stop`. The valid one-argument `\RefTo{label}` remains active and is not replaced by a historical comment-only tombstone.

A custom profile source graph therefore still defines NCKU legacy presets, but it does not load NCKU geometry, date policy, or watermark assets and must not show NCKU content. This intentional 2.x source-level compatibility cost must not be “cleaned” by deleting old APIs.

Compatibility preserves correct contracts, not verified defects.

## 驗證 / Verification

**繁體中文**

學生套件內沒有`justfile`、`scripts/`或`tests/`；從包含`thesis.tex`的project root使用direct XeLaTeX/latexmk。完整repository maintainers則執行focused custom-style、API、V1 migration及full gates。Custom fixture應以不同oral/cover dates同時建置Chinese/English Master及Doctoral branches，確認沒有NCKU visible policy或watermark asset。

**English**

The student package contains no `justfile`, `scripts/`, or `tests`; run direct XeLaTeX/latexmk from the project root containing `thesis.tex`. Full-repository maintainers run focused custom-style, API, V1 migration, and full gates. The custom fixture uses distinct oral/cover dates across Chinese/English Master and Doctoral branches and rejects NCKU visible policy or watermark assets.

Student/package command / 學生套件指令：

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
```

Maintainer commands / 維護者指令：

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
```

Verify profile registration, A4 pages, names, dates, committee ranges, both degree branches, absence of unintended assets in `.fls`, converged references, and the final rendered cover/certificate pages.

## 故障處理 / Troubleshooting

**繁體中文**

如出現`Template style file ... was not found`，檢查directory、filename及`\TemplateStyleName`大小寫。如出現`did not register itself`，確認profile file呼叫一次相同名稱的`\RegisterTemplateStyle`。如custom output出現NCKU文字或asset，檢查是否直接input NCKU profile、從NCKU複製後漏刪policy，或在generic renderer硬編碼institution values。

任何output regression均先回到最後可建置commit，一次重套一個profile change；不要停用tests、降低expected counts或改compatibility manifests。

**English**

For `Template style file ... was not found`, check directory, filename, and `\TemplateStyleName` casing. For `did not register itself`, ensure the profile file calls exactly one matching `\RegisterTemplateStyle`. If custom output shows NCKU wording or assets, check for a direct NCKU-profile input, copied NCKU policy left in the new profile, or institution values hard-coded into a generic renderer.

For any output regression, return to the last buildable commit and reapply one profile change at a time. Do not disable tests, lower expected counts, or edit compatibility manifests.
