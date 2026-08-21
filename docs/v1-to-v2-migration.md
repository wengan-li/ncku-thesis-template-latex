<!-- doc-pair: v1-v2-migration; lang: zh-Hant-TW; topics: before-you-start,compatibility-first-path,native-v2-path,stable-project-boundaries,corrected-behaviors,date-migration,migrate-another-institution-style-port,portable-verification,compatibility-evidence,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# 成大論文範本1.x至2.x升級指南

V2透過相容層保留全部已宣告的1.x指令，因此既有論文可以先升級範本實作、確認輸出無誤，再按自己的步調採用V2的profile架構。本指南以升級中的同學為主要讀者；相容承諾如何被機器驗證，文末的[相容性證據](#相容性證據)有簡短說明。

## 開始前

1. Commit或封存完整、可正常建置的1.x專案。
2. 再建置一次1.x PDF，保留作為文字與版面的比對基準。
3. 記錄XeLaTeX版本、頁數、紙張、封面與口試日期，以及所有刻意啟用的Draft或浮水印設定。
4. 分清楚下列三類檔案；不要先覆寫尚未commit的論文目錄，再期望Git幫忙找回原值。

```text
Student-owned / 學生資料:
  conf/conf.tex
  context/
  figures/
  bibliography data
  local certificate files

Template-owned / 範本實作:
  template/
  fonts/
  build configuration
  packaged examples

Root document / 主文件:
  thesis.tex (merge local edits deliberately / 有意識地merge本地修改)
```

## 相容優先路徑

適用於正在撰寫中的成大論文。保留`conf/conf.tex`、內容、圖片、書目資料與本地證明書檔案；以V2學生套件替換範本實作檔案，並手動merge `thesis.tex`的本地修改。原有的helper呼叫全部保留，V1相容層會自動載入，不需要重新命名任何指令。每完成一小步就建置一次，最後逐項對照保存的1.x PDF。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

## Native V2路徑

適用於新論文或長期維護的institution fork。由V2學生套件開始，複製論文內容、圖片、書目與證明書檔案，再於`conf/conf.tex`重新輸入或有意識地merge論文資料。成大專案保留預設`ncku` profile；其他學校的同學依照[`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md)建立並選擇一個profile。2.x期間可以繼續使用相容helpers，不需要一次改寫全部內容。每個升級步驟後都建置一次。

## 穩定專案邊界

2.x保持下列學生路徑穩定。`conf/`只存放學生論文資料；學校的版面、文字、目錄資料、日期規則與資產放在`template/style/`，V2不新增`conf/style.tex`。文件語言、學校profile、封面語言、學位與內容模式是互相獨立的決定。

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

| 決定面向 | 選項 |
| --- | --- |
| 學校 | `ncku`、`custom`或另一個維護中的profile |
| 封面語言 | `\DisplayCoverInChi`、`\DisplayCoverInEng` |
| 學位 | `\MasterDegree`、`\PhdDegree` |
| 內容 | 自己的context或`\ExampleMode`教學範例 |

## 已修正行為

下表是normative migration contract；每一個可觀察的helper修正都必須同步更新兩份語言文件。相容性保留公開API，不保留已驗證的錯誤。

| 1.x行為 | 2.x行為 | 使用者動作 |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}`在預設隱藏number時寫出空reference。 | 標題仍不顯示number，但label保存如`1.1.1.1`的穩定階層值，並拒絕empty-link warnings。 | 無需改source；既有reference會恢復可用。 |
| `\GetOralYearInTaiwanYear`會經thesis state重算並可能改動thesis year。 | Getter只讀oral state；`\SetOralEngDate`同步oral Taiwan-year state。 | 無需動作。 |
| `\SetDeptName{chi}{short}{full}`第二參數被丟棄。 | Short name保存在`\GetDeptEngShortName`；`\GetDeptEngName`仍回傳full name。 | 可選擇使用新getter。 |
| `\SetDeptDPS`輸出`Departmment of Photonics`。 | 修正為`Department of Photonics`。 | 重新建置。 |
| English oral certificate混用oral day及cover month/year。 | 全部使用oral day/month/year。 | 其他學校的同學使用不同日期時會自動得到正確的口試日期。 |
| Doctoral English cover從oral metadata借day，雖然`\SetCoverDate`只有year/month。 | Master/Doctoral date tokens由profile擁有；generic/custom只render cover-owned month/year，NCKU明確保留既有oral-day policy。 | NCKU無需動作；其他profile可自訂date tokens。 |
| `\SetCommitteeSize`對所有degree接受generic 2–9，與NCKU教學文字不一致。 | Policy由profile擁有；NCKU Master為3–5、Doctoral為5–9，neutral/custom保留2–9。 | 先呼叫`\MasterDegree`／`\PhdDegree`再設定size。 |
| Theorem `label` option以錯誤braces傳遞，label key出現在正文且無label；mutable title亦令`\nameref`變空。 | 保留optional signature，正確寫label，並在`\label`前freeze title；`\ref`及`\nameref`均可用。 | 無需改source，重新build。 |
| Figure/subfigure/table caption把mutable temporary寫入nameref metadata。 | 所有caption wrappers在寫label前freeze rendered caption；`\ref`number不變，`\nameref`回傳literal caption。 | 重建足夠次數更新auxiliary files。 |
| Numbering getters保留shared scratch aliases，後續setup可改寫先前getter；repeated appendix equation setup亦會append。 | Prefix、separator及counter names被freeze，counter values保持dynamic；general/appendix setup可重複且idempotent。 | 自訂編號的使用者應重新產生labels及lists。 |
| Forward/multi-hop theorem `FollowCounter`受initializer order影響，cycles可recursive overflow。 | Chains遞迴resolve至frozen terminal；numbered／optional／starred syntax一致，cycles以deterministic package error停止。 | 無需改source，重新build。 |
| Custom font type值為兩位數，單token的`\if` dispatch永遠不成立；`\SetCustomEngFontFiles`／`\SetCustomChiFontFiles`後的字型初始化被靜默跳過，輸出回退到engine預設字型。 | Font-type dispatch改用`\ifnum`比較完整數值；custom type會實際載入`template/fonts/`中設定的字型檔，檔案缺失時以deterministic fontspec error停止。 | 有呼叫custom font setters的專案把字型檔放入`template/fonts/`，或移除該setters以保留預設字型。 |

## 日期升級

公開setters不變。V2把原始輸入與profile解析後的顯示政策分開：`\GetRequestedCoverYear`／`\GetRequestedCoverMonth`回傳`\SetCoverDate`的原始值，`\GetThesisYear`／`\GetThesisMonth`回傳profile解析後的封面值，oral getters保持獨立。NCKU profile仍以口試日期作為封面的authoritative date，因此成大輸出不變；其他學校的profile預設使用明確的封面年月，不借用口試的day。

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Institution fork應override `\ApplyOralDatePolicy`、`\ApplyCoverDatePolicy`與profile擁有的Master／Doctoral date tokens，不要`\renewcommand`公開setters。

## 其他學校Style Port升級

1. 以`template/style/custom/`作新profile base；不要先copy/load NCKU再撤銷policy。
2. 將舊custom file內的institution geometry、校名、watermark及date behavior移到`<profile>/<profile>.tex`。
3. 恰好呼叫一次`\RegisterTemplateStyle{<profile>}`。
4. 透過`template/style/style.tex`的`\TemplateStyleName`選擇profile。
5. 將舊`\SetOralDate`／`\SetCoverDate` overrides改成policy hooks。
6. 只有institution有degree-specific committee ranges時才override `\ApplyCommitteeSizePolicy`；保持`\SetCommitteeSize`不變。
7. 將cover/oral wording及English cover-date formats移到profile token setters。
8. 使用`\SetCollName`／`\SetDeptName`，或在profile內維護institution catalogue。
9. 以故意不同的oral／cover dates建置cover及certificate，證明policy separation。
10. 確認`.fls`沒有載入非預期institution asset。

完整指南：[`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md)

## Portable驗證

在解壓的學生ZIP或任何包含`thesis.tex`的migrated project root執行下列指令。檢查A4與預期頁數、學校／學院／系所／題目／作者／指導教授文字、cover/oral dates、目錄與references、書目收斂、Draft／watermark狀態，以及封面、前置頁、正文與最後頁的呈現。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

以保存的1.x PDF作為比對基準。

## 相容性證據

升級時不需要執行本節內容；它說明相容承諾在完整Git repository中如何被機器把關。三份manifest鎖定1.x的公開surface與學生檔案：

```text
tests/100-v1-public-api.json                     597 LaTeX/xparse + 65 literal \def declarations
tests/101-v1-comment-environment-artifacts.json  22 declarations from dead comment environments
tests/102-v1-project-migration.json              18 byte-pinned v1.8.2 student files
```

未修改的1.x專案仍選擇預設`ncku` profile，因此原有的NCKU college／department presets繼續可用；`custom`與其他學校的profile只取得generic institution API。相容層的載入方式如下：

```text
template/compat/v1.tex
  template/compat/deprecated.tex        23 deprecated-command tombstones
template/style/ncku/ncku.tex            selected NCKU profile
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
template/command/cmd-college.tex        dormant direct-path wrapper
template/command/cmd-department.tex     dormant direct-path wrapper
```

完整repository的測試會以未修改的v1.8.2專案建置出271頁A4的canonical輸出，並由StudentMode fixture的`.fls`／`.blg`記錄證明active content與三個書目資料庫。這些檢查與manifest刻意不放入學生ZIP：

```bash
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
```

完整的gate清單與輸出identity證據見[驗證與效能記錄](features/validation-and-performance.md)。

## 回復與故障處理

如升級後輸出不符預期，停止繼續修改，不要刪除舊專案或baseline PDF。先確認改動屬於學生資料、範本實作檔案，還是本地`thesis.tex`的merge；回到上一個可建置的commit，然後一次重新套用一個變更。切換BibTeX style或遇到stale intermediates時，先以`latexmk -C thesis.tex`清除再build。不要修改compatibility manifests、降低expected counts或停用tests來隱藏差異；已驗證的行為修正應記錄在上方的normative表格。
