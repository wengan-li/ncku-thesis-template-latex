<!-- doc-pair: student-writing; lang: zh-Hant-TW; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# 撰寫論文內容

## 按任務閱讀

先在完整學生專案的 `conf/conf.tex` 將 `\ExampleMode` 註解掉；`context/context.tex` 決定載入哪些檔案。保留 ExampleMode 會建置教學文件。參考頁中的路徑均由學生專案根目錄計算。

| 任務 | 文件 |
| --- | --- |
| 新增章節、文字、前置頁或附錄 | [專案與章節](usage/project-and-chapters.md) |
| 插入提供的圖片或表格 | [圖片與表格](usage/figures-and-tables.md) |
| 撰寫公式、定理或證明 | [公式、定理與證明](usage/equations-and-theorems.md) |
| 加入真實文獻及引用 | [引用與文獻](usage/references-and-bibliography.md) |
| 建置或排除錯誤 | [建置與診斷](usage/build-and-diagnostics.md) |

## 使用代理或複製內容

請代理先明確讀取 [SKILL.md](.agents/skills/ncku-thesis-writing/SKILL.md)，再讀取任務所需參考頁。不同用戶端不一定會自動註冊巢狀技能。應提供研究資料、圖片與文獻資訊，不得虛構缺少的輸入。一般人工編寫與建置不會載入代理指示。

複製時以能保留隱藏檔案及相對符號連結的目錄複製工具，帶走整個 `context/`，包括 `.agents/`、`AGENTS.md` 與 `CLAUDE.md -> AGENTS.md`。只複製可見檔案或 *.tex 會遺失知識。替換目的地內容目錄之前，先保存既有研究內容。目的地仍須有相符的完整論文範本，包含 `thesis.tex`、`conf/` 及 `template/configure.tex`；只有內容目錄無法編譯。若缺少，先取得相符的完整學生專案，再審慎調整其內容組裝與設定。閱讀這些參考文件不需教學範例或網路。

代理先從指定內容檔案或目錄向上尋找同時含 `thesis.tex`、`conf/` 及 `template/configure.tex` 的專案；未指定內容時才從工作目錄向上找。在經確認的儲存庫根目錄，另僅檢查 `thesis/` 子目錄是否具備三項條件，不遞迴搜尋其他目錄。孤立的內容不能因工作目錄附近有其他範本就被誤認為可編譯。
