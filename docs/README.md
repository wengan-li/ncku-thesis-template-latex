<!-- doc-pair: project-index; lang: zh-Hant-TW; topics: start-here,student-guides,project-records,releases-and-downloads -->

[繁體中文](README.md) | [English](README.en.md)

# 專案文件

## 文件入口

本目錄記錄已發行成大論文範本的migration、architecture、validation、release及Overleaf evidence。如果只需要撰寫論文，請由學生套件內的`README.md`及`conf/README.md`開始；root [`README.md`](../README.md)提供專案概覽及下載入口。

## 學生文件

| 用途 | 文件 |
| --- | --- |
| 建置及編輯論文 | [`thesis/README.md`](../thesis/README.md) |
| 填寫學生設定 | [`thesis/conf/README.md`](../thesis/conf/README.md) |
| 查看NCKU學院及系所preset | [`thesis/template/style/ncku/README.md`](../thesis/template/style/ncku/README.md) |
| 從1.x升級至2.x | [`v1-to-v2-migration.md`](v1-to-v2-migration.md) |
| 其他學校的同學建立institution profile | [`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md) |
| 查看版本變更 | [`CHANGELOG.md`](../CHANGELOG.md) |

每份完整guide使用一個主要語言，並於頁首提供繁體中文及英文equivalent page連結。文件語言、institution profile、封面語言、學位及內容模式是獨立設定。

## 專案記錄

| 主題 | 文件 |
| --- | --- |
| V2架構及相容邊界 | [`features/v2-modernization.md`](features/v2-modernization.md) |
| 測試、輸出及效能 | [`features/validation-and-performance.md`](features/validation-and-performance.md) |
| 發行、下載及Overleaf | [`features/release-and-distribution.md`](features/release-and-distribution.md) |
| 全部已發行功能記錄 | [`features/README.md`](features/README.md) |

Feature records保存已發行architecture、驗證結果及公開狀態。

## 發行與下載

本模版使用XeLaTeX及direct `latexmk`學生build。正式學生套件與generated examples請由[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載；各次發行的使用者可見變更記錄於[`CHANGELOG.md`](../CHANGELOG.md)。

既有Overleaf Gallery頁面仍可公開使用。GitHub Releases與Overleaf publication是獨立狀態；詳細記錄見[`features/release-and-distribution.md`](features/release-and-distribution.md)。
