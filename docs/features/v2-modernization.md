<!-- language: zh-Hant-TW; summary-of: v2-modernization.en.md -->

[繁體中文摘要](v2-modernization.md) | [English technical record](v2-modernization.en.md)

# 範本架構與 2.x 相容性

本專案提供以 XeLaTeX、BibTeX 與 `latexmk` 建置的成大論文範本。學生資料、通用機制與學校政策分別管理；當前校方及系所規定優先。

- 學生在 `context/` 撰寫內容，`conf/conf.tex` 保存論文資料；學校版面、日期、文字與資產放在 `template/style/`，不使用 `conf/style.tex`。
- `template/configure.tex` 先載入通用指令與 `template/compat/v1.tex`，再載入 base 與唯一選定的學校設定，接著讀取 `\TemplateConfigurationFile`，最後執行 `\FillInPDFData`。學校目錄先定義，學生設定再選擇項目。
- 預設 `ncku` 設定擁有成大系所目錄與政策；`custom` 是不含成大資料的中性骨架。其他學校的同學須依[自訂指南](../../thesis/template/style/Customization.md)建立符合當地規定的設定，不能把骨架或 NTU 示範當成送審保證。
- 公開設定指令保留原始輸入，經政策函式解析後顯示。`\GetRequestedCoverYear` 讀取原始封面年份，`\GetThesisYear` 讀取解析後的年份；口試資料保持獨立。成大封面依口試日期，通用設定只使用封面本身擁有的年月。
- NCKU 委員人數政策為碩士 3–5 人、博士 5–9 人，通用設定容量為 2–9 人。應先選學位，再設定人數；學位狀態不依賴顯示語言。
- 2.x 保留所有已宣告的 1.x 公開指令名稱與參數形狀，相容層自動載入。已停用指令保留明確的升級診斷，`\RefTo{label}` 仍可使用；操作與復原見[升級指南](../v1-to-v2-migration.md)。
- 解析器、定理、編號與圖表各有固定責任及測試。標題與圖說的引用資料保持穩定，定理計數器循環會報錯，重複設定編號不會累加狀態。
- 支援引擎為 XeLaTeX，文獻系統為 BibTeX；輸出未標記，不宣稱 PDF/UA 合規或機構認可。完整架構見英文頁，現行檢查與套件契約分見[驗證](validation-and-performance.md)及[發行](release-and-distribution.md)。
