<!-- doc-pair: v1-v2-migration; lang: zh-Hant-TW; topics: before-you-start,compatibility-first-path,new-project-path,stable-project-boundaries,current-helper-behavior,date-configuration,institution-port,build-and-compare,compatibility-boundary,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# 成大論文範本 1.x 至 2.x 升級指南

2.x 透過自動載入的相容層保留已宣告的 1.x 公開指令名稱與參數形狀。既有論文可先升級範本、確認輸出，再逐步採用學校設定架構；不需要一次改寫論文內容。

## 開始前

保存完整可建置的 1.x 專案與 PDF，並記錄 XeLaTeX 版本、紙張、頁數、封面與口試日期及刻意啟用的浮水印。將資料與範本實作分開處理，不直接覆寫唯一的論文副本。校方系統的正式證明書與自行加入的字型也須備份。

```text
Student-owned:
  conf/conf.tex
  context/
  local figures, bibliography and official certificate files
  locally added fonts under template/fonts/

Template-owned:
  template/ (merge locally added fonts deliberately)
  packaged examples and build configuration

Root document:
  thesis.tex (merge local edits deliberately)
```

## 相容優先路徑

適用於正在撰寫的成大論文。保留學生資料、圖片、文獻與證明書，以 2.x 學生套件更新範本實作，手動合併 `thesis.tex` 的修改與自行加入的字型。原有指令繼續使用，`template/compat/v1.tex` 自動載入。每完成一小步就建置，並對照保存的 PDF。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Overleaf 選擇 XeLaTeX 與主文件 `thesis.tex`；編輯器亦使用相同根文件及 XeLaTeX/BibTeX 的 latexmk 建置鏈。

## 新專案路徑

由 2.x 學生套件開始，複製內容、圖片、文獻及證明書，再審慎合併 `conf/conf.tex` 資料。NCKU 專案保留預設 `ncku`；其他學校的同學依[自訂指南](../thesis/template/style/Customization.md)建立並選擇一個學校設定。可在整個 2.x 期間沿用相容指令。搬移專案時保留專案根目錄的隱藏 `.agents/`、`.claude/` 與相對連結；context/ 只放學生內容，詳見[寫作指南](../thesis/context/README.md)。

## 穩定專案邊界

`conf/` 只放學生論文資料；版面、學校目錄、日期規則與資產屬於 `template/style/`，不使用 `conf/style.tex`。文件語言、學校設定、封面語言、學位及內容模式互相獨立。

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

| 面向 | 選項 |
| --- | --- |
| 學校設定 | `ncku`、`custom` 或其他已註冊設定 |
| 封面語言 | `\DisplayCoverInChi`、`\DisplayCoverInEng` |
| 學位 | `\MasterDegree`、`\PhdDegree` |
| 內容 | 自己的 `context/` 或 `\ExampleMode` 教學範例 |

## 現行指令行為

下表說明升級後應確認的現行行為與必要動作。公開參數形狀保持相容，但不應依賴錯誤輸出或未實作的選項效果。

| 指令或功能 | 現行行為 | 升級檢查 |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}` | 即使標題不顯示編號，標籤仍保存穩定的階層值。 | 保留指令並重建引用。 |
| `\GetOralYearInTaiwanYear`、`\SetOralEngDate` | 口試資料不修改論文年份；英文日期設定同步口試民國年。 | 核對口試及封面日期。 |
| `\SetDeptName{chi}{short}{full}` | `\GetDeptEngShortName` 取得縮寫，`\GetDeptEngName` 取得全名。`\SetDeptDPS` 使用 Department of Photonics。 | 檢查自訂系所資料及封面。 |
| 英文口試證明書日期 | 使用口試本身的日、月、年。 | 不以封面日期代替口試日期；學生使用校方正式檔案。 |
| 英文封面日期 | 通用設定使用封面年月，NCKU 由自己的政策提供口試日期。 | 其他學校透過日期政策調整，不借用無關資料。 |
| `\SetCommitteeSize` | NCKU 碩士 3–5、博士 5–9；通用設定 2–9。 | 先呼叫 `\MasterDegree` 或 `\PhdDegree`。 |
| 定理標題及標籤 | 選項簽名不變，標籤及 `\nameref` 資料保持穩定。 | 保留用法並重建。 |
| 圖片、子圖及表格圖說 | 標籤保存實際圖說，不受後續設定改寫。 | 重跑至輔助檔收斂。 |
| 自訂編號 | 設定固定前綴及分隔符號，計數值持續變動；重複設定不累加。 | 重建標籤及目錄。 |
| 定理 `FollowCounter` | 支援前向及多層相依，循環以明確錯誤停止。 | 移除循環，不依賴初始化順序。 |
| `\SetCustomEngFontFiles`、`\SetCustomChiFontFiles` | 實際載入設定的字型檔，缺檔會報 fontspec 錯誤。 | 將字型放在 `template/fonts/`，或移除自訂設定以使用預設字型。 |

## 日期設定

`\GetRequestedCoverYear`／`\GetRequestedCoverMonth` 讀取封面原始輸入，`\GetThesisYear`／`\GetThesisMonth` 讀取學校政策解析後的值，口試資料保持獨立。NCKU 仍以口試日期決定封面，其他學校的通用設定使用明確的封面年月。

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

學校設定應使用 `\ApplyOralDatePolicy`、`\ApplyCoverDatePolicy` 與學位日期文字設定，不覆寫公開設定指令。

## 其他學校設定移植

1. 從 `template/style/custom/` 建立設定，不先載入 NCKU 再逐項撤銷。
2. 將學校版面、校名、浮水印、日期及證明書文字放入 `<profile>/<profile>.tex`。
3. 恰好呼叫一次 `\RegisterTemplateStyle{<profile>}`，並在 `template/style/style.tex` 以 `\TemplateStyleName` 選擇。
4. 以政策函式處理日期與學位委員人數，保留 `\SetOralDate`、`\SetCoverDate`、`\SetCommitteeSize` 的公開形狀。
5. 使用通用 `\SetCollName`、`\SetDeptName`，或以學校專用前綴建立目錄。目錄先定義，學生設定再選擇項目。
6. 使用刻意不同的口試與封面日期，檢查中英文及不同學位輸出。確認非空 `.fls` 沒有載入非預期的學校資產。

`custom` 與 NTU 接線示範都不是其他學校可直接送審的保證。完整程序見[自訂指南](../thesis/template/style/Customization.md)，當前校方規定仍優先。

## 建置及比對

在含 `thesis.tex` 的學生專案根目錄建置。確認 A4、預期頁數、姓名、系所、指導教授、日期、目錄、引用、文獻及浮水印，並檢視封面、前置頁、正文與最後頁。比對基準為保存的 1.x PDF，不能只看建置是否產生檔案。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Overleaf 與編輯器使用相同的 XeLaTeX 根文件及 BibTeX 流程；必要時從頭重建。

## 相容性邊界

1.x 公開指令與環境的名稱、參數形狀在整個 2.x 期間保留。已停用的指令提供明確診斷；`\RefTo{label}` 仍可使用。預設 `ncku` 讓既有成大專案繼續使用系所指令，其他設定只載入通用資料契約。

目前輸出未標記，不宣稱 PDF/UA 或任何學校的合規認可。架構責任見[範本架構](features/v2-modernization.md)，儲存庫驗證方式見[驗證與效能](features/validation-and-performance.md)；學生升級不需要執行儲存庫測試工具。

## 回復與故障處理

若輸出不符預期，停止追加變更，保留原專案與 PDF。先分辨問題位於學生資料、範本實作或 `thesis.tex` 合併，回復至可建置的版本，再一次套用一個變更。遇到舊輔助檔或切換 BibTeX 樣式，先執行 `latexmk -C thesis.tex` 再建置。自訂字型缺檔時補齊檔案或移除自訂設定，不掩蓋錯誤；其他問題依[學生排錯指南](../thesis/README.md)處理。
