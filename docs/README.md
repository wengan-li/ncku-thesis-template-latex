<!-- doc-pair: project-index; lang: zh-Hant-TW; topics: start-here,student-guides,current-features,releases-and-downloads -->

[繁體中文](README.md) | [English](README.en.md)

# 專案文件

## 文件入口

本目錄記錄論文範本的現行架構、相容性、驗證與分發方式。撰寫論文請先閱讀學生專案內的 README、設定說明與內容指南；[專案首頁](../README.md)提供概覽及下載入口。此處描述現行來源，已發行套件以 GitHub Releases 為準。

## 學生文件

| 任務 | 文件 |
| --- | --- |
| 建置及編輯論文 | [學生專案指南](../thesis/README.md) |
| 填寫題目、學位與姓名等資料 | [設定指南](../thesis/conf/README.md) |
| 撰寫章節、圖表、公式及引用 | [內容寫作指南](../thesis/context/README.md) |
| 選擇成大學院及系所 | [NCKU 系所目錄](../thesis/template/style/ncku/README.md) |
| 升級既有 1.x 專案 | [1.x 至 2.x 升級指南](v1-to-v2-migration.md) |
| 其他學校的同學建立學校設定 | [自訂指南](../thesis/template/style/Customization.md) |

完整指南在頁首提供繁中與英文切換。文件語言、學校設定、封面語言、學位及內容模式彼此獨立。

## 範本功能

| 主題 | 文件 |
| --- | --- |
| 載入順序、學校政策及公開相容性 | [架構與 2.x 相容性](features/v2-modernization.md) |
| 測試、輸出及效能限制 | [驗證與效能](features/validation-and-performance.md) |
| 套件、Overleaf、授權及正式文件 | [發行與分發](features/release-and-distribution.md) |
| 寫作知識、代理入口與內容複製 | [學生寫作與代理技能](features/student-writing-and-agent-skills.md) |
| 依需求查找全部功能 | [功能索引](features/README.md) |

## 發行與下載

學生套件與產生的範例由 [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) 提供，版本變更保留在[變更記錄](../CHANGELOG.md)。本模版使用 XeLaTeX，學生可直接以 `latexmk` 建置。

[Overleaf Gallery](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)為獨立入口，不能假設其來源與儲存庫或某次發行完全相同。上傳、送審與公開核准的界線見[分發說明](features/release-and-distribution.md)。
