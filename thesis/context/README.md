<!-- doc-pair: student-writing; lang: zh-Hant-TW; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# 論文內容與寫作入口

## 學習寫作

完整教學由專案原有的 example/how-to 來源及產生的教學 PDF 提供，涵蓋章節、圖表、公式、定理、文獻與前置頁。本頁只提供入口，不另維護一份語法手冊。完整專案的 ExampleMode 可建置教學文件；自己的論文則依學生專案 README 關閉該模式，並由 context/context.tex 選擇內容。若套件未包含教學來源，可使用發行套件提供的完整教學 PDF。

## 使用代理與複製專案

請代理明確讀取 [SKILL.md](../.agents/skills/ncku-thesis-writing/SKILL.md)，再按任務讀取其[產生的英文參考片段](../.agents/skills/ncku-thesis-writing/references/template-usage.md)。這份精簡參考取自教學實際使用的程式碼，不是另一份人用手冊；不需要教學目錄或網路即可閱讀。若用戶端未自動辨識，須明確讀取技能；別名能解析不代表已驗證自動呼叫。

請複製完整可建置的學生專案，包含隱藏 .agents/、.claude/ 與相對連結。專案根目錄的 .claude/skills -> ../.agents/skills 別名指向同一份寫作技能。先保存目的地既有內容，再由含有 thesis.tex 的目錄建置。context/ 只放學生內容，不是獨立的代理專案，也不包含技能或範本執行環境。

代理由指定內容的祖先尋找執行環境；未指定時才從工作目錄尋找，在已確認的儲存庫根目錄另僅檢查 thesis/。相符完整專案須同時包含 thesis.tex、conf/ 與 template/configure.tex；孤立內容不得借用無關專案。一般建置不讀取代理指示，也不需要產生器。
