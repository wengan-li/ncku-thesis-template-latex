<!-- doc-pair: student-writing; lang: zh-Hant-TW; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# 論文內容與寫作入口

## 學習寫作

在 `context/` 編寫章節，並於 `context/context.tex` 選擇要載入的內容。撰寫自己的論文前，依[學生專案指南](../README.md)填寫資料並停用 `\ExampleMode`。

章節、圖表、公式、定理、文獻與前置頁的完整教學，請閱讀[教學 PDF 的下載說明](../README.md#開始撰寫)。專案內的 `example/how-to/` 也保留教學來源；若已刪除教學目錄，仍可閱讀下載的 PDF。

## 使用代理與複製專案

使用 AI 協助時，請它先讀取 [SKILL.md](../.agents/skills/ncku-thesis-writing/SKILL.md)，再按需要查閱[英文指令參考](../.agents/skills/ncku-thesis-writing/references/template-usage.md)。若用戶端未自動找到技能，請明確提供 SKILL.md 的路徑。

搬移前先保存目的地資料，再複製整個學生專案，包含隱藏 `.agents/`、`.claude/` 與相對連結。不要只搬走 `context/`；請從含有 `thesis.tex` 的目錄建置。

若出現 `A matching complete thesis template containing thesis.tex, conf/ and template/configure.tex is required.`，表示缺少相符的完整專案。先取得完整學生套件，保留自己的內容及資料，再按[學生專案指南](../README.md)建置；不要改用無關專案。
