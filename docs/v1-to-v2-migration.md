<!-- doc-pair: v1-v2-migration; lang: zh-Hant-TW; topics: before-you-start,compatibility-first-path,build-and-compare,new-project-path,stable-project-boundaries,current-helper-behavior,date-configuration,institution-port,compatibility-boundary,recovery-and-troubleshooting -->

[繁體中文](v1-to-v2-migration.md) | [English](v1-to-v2-migration.en.md)

# 成大論文範本 1.x 至 2.x 升級指南

正在用 1.x 撰寫的論文可升級到 2.x，不必重寫內容。先保留原專案，在新目錄升級，再對照舊 PDF。2.x 仍使用 XeLaTeX。

## 開始前

備份完整的 1.x 專案及最新 PDF，包括自己加入的圖片、書目、字型與學校正式證明書。記下 XeLaTeX 版本、頁數、封面與口試日期，以及原本啟用的浮水印，供升級後比對。不要覆寫唯一的論文副本。

## 保留原設定升級

1. 從 [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載 2.x 學生套件，解壓到新目錄。
2. 搬入舊專案的 `conf/conf.tex`、`context/` 內容、圖片、書目及正式證明書，用自己的檔案取代同名範例檔。
3. 將自行加入的字型放回 `template/fonts/`。不要把舊 `template/` 整個蓋回去。
4. 若改過 `thesis.tex` 或 `cover.tex`，將自己的修改逐項合併到新檔案，不要直接覆蓋新版本。

完成後依下方「建置及比對」檢查輸出，再繼續修改論文。

## 建置及比對

在含有 `thesis.tex` 的目錄建置：

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Overleaf 選 XeLaTeX，主文件設為 `thesis.tex`；編輯器使用相同主文件及 XeLaTeX/BibTeX 建置流程。

對照舊 PDF，檢查 A4 紙張、頁數、封面資料與日期、證明書、目錄、圖表、引用、參考文獻及最後一頁。確認沒有未解決的引用或非預期浮水印。產生 PDF 不代表升級已完成。

## 改用新設定開始

若想重新整理設定，可保留 2.x 的 `conf/conf.tex`，依[設定指南](../thesis/conf/README.md)逐項填回自己的資料。撰寫自己的論文時，將 `\ExampleMode` 註解，否則會建置教學範例。

搬移完整專案時，保留套件的隱藏 `.agents/`、`.claude/` 及相對連結。寫作協助見[內容與寫作指南](../thesis/context/README.md)。

## 檔案位置

- `conf/conf.tex` 放論文資料，`context/` 放章節內容。
- `template/` 是範本實作，`example/` 是教學範例。
- 學校版面與規則放在 `template/style/`，不要新增 `conf/style.tex`。

成大同學保留預設 `ncku` 設定即可。封面語言、學位及是否建置教學範例分別設定，選英文封面不需要切換學校樣式。

## 升級後要檢查的變更

| 項目 | 檢查方式 |
| --- | --- |
| 章節引用 | 使用 `\StartSubSubSection{title}{label}` 時，標題即使不顯示編號，引用仍能取得章節編號。重建後核對引用。 |
| 系所英文名稱 | 自訂 `\SetDeptName{chi}{short}{full}` 時，檢查縮寫與全名是否正確。`\SetDeptDPS` 使用 Department of Photonics。 |
| 口試委員人數 | 先選 `\MasterDegree` 或 `\PhdDegree`，再呼叫 `\SetCommitteeSize`。成大碩士為 3–5 人、博士為 5–9 人；通用設定為 2–9 人。 |
| 定理與圖表引用 | 重建後核對 `\ref` 與 `\nameref`。圖表標籤不再受後續圖說設定覆蓋。 |
| 自訂編號 | 檢查前綴、分隔符號及目錄；重複設定不應累加前綴，計數值仍會更新。 |
| 定理 `FollowCounter` | 可引用稍後定義的計數器，也可串接多層；若出現循環錯誤，移除循環相依。 |
| 自訂字型 | `\SetCustomEngFontFiles`、`\SetCustomChiFontFiles` 現在會載入指定檔案。缺檔時補齊 `template/fonts/`，或移除自訂設定以使用預設字型。 |

## 日期設定

成大封面由口試日期決定；其他學校的通用設定使用明確填入的封面年月。兩者不要混用：

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

升級後同時檢查封面與口試日期。`\GetOralYearInTaiwanYear` 不再改寫論文年份，`\SetOralEngDate` 也會更新口試民國年；英文證明書範例使用口試本身的日、月、年。正式提交仍須使用學校系統的證明書。

自行修改學校日期規則時，依[自訂指南](../thesis/template/style/Customization.md)設定，不要改寫 `\SetOralDate` 或 `\SetCoverDate` 本身。

## 其他學校的同學

從 `template/style/custom/` 建立自己的學校樣式，不要先載入成大設定再逐項撤銷。校名、系所、版面、日期、浮水印及證明書文字都在學校樣式中設定；學生資料仍放在 `conf/conf.tex`。

依[自訂指南](../thesis/template/style/Customization.md)登記並選擇新樣式，將原有成大系所指令換成通用的 `\SetCollName`、`\SetDeptName` 或自己學校的指令。用不同的口試與封面日期，檢查中英文、碩博士輸出，確認沒有混入成大名稱或資產。

`custom` 與臺大接線範例都不是可直接送審的格式。請逐項核對自己學校及系所的現行規定。

## 舊指令與限制

2.x 保留已宣告的 1.x 公開指令、環境名稱與參數用法，`template/compat/v1.tex` 會自動載入。已停用的指令仍會報錯，`\RefTo{label}` 則可繼續使用。原有成大系所指令只在預設 `ncku` 設定下提供。

目前 PDF 未加結構標記，不宣稱符合 PDF/UA，也不代表學校認可。深入資料見[範本架構](features/v2-modernization.md)及[驗證方式](features/validation-and-performance.md)；一般升級不需要執行儲存庫測試工具。

## 回復與故障處理

若輸出不符預期，先停止修改，保留出問題的版本供比對。回到可建置的備份，再分別檢查搬入的資料、字型及 `thesis.tex` 合併內容，一次處理一項。

舊輔助檔或 BibTeX 樣式切換造成錯誤時，先清除再建置：

```bash
latexmk -C thesis.tex
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

缺少自訂字型時，補上檔案或取消自訂設定，不要忽略錯誤。其他情況見[學生排錯指南](../thesis/README.md)。
