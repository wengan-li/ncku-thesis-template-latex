<!-- doc-pair: v1-v2-migration; lang: zh-Hant-TW; topics: before-you-start,compatibility-first-path,native-v2-path,stable-project-boundaries,public-helper-compatibility,byte-identical-v1-project-gate,v1-adapter-layout,corrected-behaviors,date-migration,migrate-another-institution-style-port,portable-verification,repository-verification,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# 成大論文範本1.x至2.x升級指南

正式目標：[`v2.0.2.260719120024`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.2.260719120024)

V2透過完整2.x line的相容層，保留machine-audited 1.x LaTeX/xparse及literal `\def` declarations。既有專案可先升級template implementation、驗證NCKU輸出，再逐步採用native V2 profile架構。

## 開始前

1. Commit或封存完整、可正常建置的1.x專案。
2. 再建置一次1.x PDF並保留作文字及視覺reference。
3. 記錄XeLaTeX版本、頁數、紙張、封面／口試日期及所有刻意啟用的Draft／浮水印設定。
4. 分清學生資料、template implementation及主文件；不要覆寫尚未commit的論文目錄後再依賴Git猜測原值。

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

此路徑適用於正在撰寫中的NCKU論文。保留`conf/conf.tex`、內容、圖片、書目資料及本地證明書；以V2學生套件替換template-owned檔案，並手動merge `thesis.tex`的本地修改。保留現有helper calls；V1 adapter會自動載入。每完成一小步便建置，最後逐項比較保存的1.x PDF。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

No helper rename is required / 不需要重新命名helper。

## Native V2路徑

此路徑適用於新論文或長期維護的institutional fork。由V2學生套件開始，複製論文內容、圖片、書目及證明書，再於`conf/conf.tex`重新輸入或有意識地merge metadata。成大專案保留預設`ncku` profile；其他學校的同學依照[`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md)建立並選擇一個profile。2.x期間可繼續使用相容helpers，不需要一次改寫全部source。

每一個升級步驟後都要建置。

## 穩定專案邊界

2.x保持下列學生路徑穩定。`conf/`只存放學生論文資料。學校geometry、文字、catalogue、日期規則及assets放在`template/style/`；V2不新增`conf/style.tex`。文件語言、學校profile、封面語言、學位及內容模式是獨立決定。

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

## Public helper相容性

完整Git repository的`tests/100-v1-public-api.json`記錄597個runtime-visible 1.x LaTeX/xparse commands/environments及65個literal `\def`-style declarations；其名稱及完整argument shape在2.x均保留。另有22個declarations只存在於runtime-dead LaTeX `comment` environments，並由獨立audit記錄；它們不是被移除的public API。Native V2 internals可將舊helper委派到profile hooks，但相容層只保留正確contract，不重現已驗證的defect。

```bash
python3 scripts/test/check-v1-api.py
```

## Byte-identical V1專案gate

`tests/102-v1-project-migration.json`將18個student-owned files、合共296,726 bytes，pin至immutable release `v1.8.2.260715154703`。範圍包括`thesis.tex`、`conf/conf.tex`、學生內容、書目資料及口試證明assets。Runtime evidence分為兩條：unchanged entry/configuration經V2 adapter、base及NCKU profile建置271頁A4 canonical result；StudentMode fixture則從`.fls`及`.blg`確認active content及三個bibliography databases。

未被該V1 configuration載入的alternate abstracts及external certificate PDFs只作source pin，不會被誤稱為runtime-loaded。

```text
tests/102-v1-project-migration.json
scripts/test/check-v1-project-migration.py
```

## V1 adapter佈局

2.x相容性按照原本的NCKU使用情境保存：未修改的1.x專案繼續選擇預設`ncku` profile，因此原有NCKU college／department presets仍可使用。`template/compat/v1.tex`不再替每個profile載入NCKU catalogue；它只載入generic／deprecated adapter。`custom`及其他學校profile只取得generic institution API，並須在自己的`conf/conf.tex`以generic或學校prefix command取代原有NCKU department selection。

```text
template/compat/v1.tex
  template/compat/deprecated.tex        23 deprecated-command tombstones
template/style/ncku/ncku.tex            selected NCKU profile
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
template/command/cmd-college.tex        dormant direct-path wrapper
template/command/cmd-department.tex     dormant direct-path wrapper
```

## 已修正行為

下表是normative migration contract；每一個observable helper correction都必須同步更新兩份語言文件。相容性保留public API，不會保留已驗證的錯誤。

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

## 日期升級

Public setters不變。V2將raw input與profile-resolved display policy分開：`\GetRequestedCoverYear`／`\GetRequestedCoverMonth`回傳`\SetCoverDate`原始值，`\GetThesisYear`／`\GetThesisMonth`回傳profile解決後的封面值，oral getters保持獨立。NCKU profile仍以oral date作封面authoritative date，因此NCKU輸出不變。其他學校的profile預設使用explicit cover year/month，不借用oral day。

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

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

## Portable驗證

在解壓student ZIP或任何包含`thesis.tex`的migrated project root執行下列commands。檢查A4及預期頁數、學校／學院／系所／題目／作者／指導教授文字、cover/oral dates、目錄及references、書目收斂、Draft／watermark狀態，以及cover、front matter、正文及最後頁rendering。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Use the saved 1.x PDF as the comparison reference / 以保存的1.x PDF作比較reference。

## 完整儲存庫驗證

下列commands需要完整Git checkout並從repository root執行，student ZIP不提供。Acceptance evidence包括597/597 runtime-visible declarations、65/65 literal-def declarations、22個dead-comment audit entries、18個byte-identical student inputs、exact-tree student archive、direct build、neutral/custom six-page fixture，以及canonical 271-page NCKU output identity。

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
```

```text
pages:                 271
paper:                 A4
normalized bbox words: 40823
text:                  identical
fonts:                 identical
raster:                271/271 identical at 120 DPI
```

## 回復與故障處理

如升級後輸出不符預期，停止繼續修改，不要刪除舊專案或baseline PDF。確認改動屬student data、template-owned files或本地`thesis.tex`merge；回到上一個可建置commit，然後一次重新套用一個變更。切換BibTeX style或遇到stale intermediates時，以`latexmk -C thesis.tex`清除後再build。不要修改compatibility manifests、降低expected counts或停用tests來隱藏差異。
