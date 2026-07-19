<!-- doc-pair: project-index; lang: zh-Hant-TW; topics: start-here,directory-model,bilingual-policy,documentation-lifecycle,source-of-truth-order,current-state -->

[繁體中文](README.md) | [English](README.en.md)

# 專案文件

目前正式release：[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

## 文件入口

本目錄記錄已發行成大論文範本的migration、architecture、validation、release及Overleaf evidence。如果你只需要撰寫論文，請優先閱讀套件內的`thesis/README.md`及`thesis/conf/README.md`；root `README.md`是public router，不是專案runbook。

| 讀者或工作 | Canonical文件 |
| --- | --- |
| 學生建置／編輯 | [`thesis/README.md`](../thesis/README.md) |
| 學生設定 | [`thesis/conf/README.md`](../thesis/conf/README.md) |
| 1.x至2.x升級 | [`v1-to-v2-migration.md`](v1-to-v2-migration.md) |
| V2架構 | [`features/v2-modernization.zh-TW.md`](features/v2-modernization.zh-TW.md) |
| 測試、輸出與效能 | [`features/validation-and-performance.zh-TW.md`](features/validation-and-performance.zh-TW.md) |
| 發行與Overleaf | [`features/release-and-distribution.zh-TW.md`](features/release-and-distribution.zh-TW.md) |
| 版本歷史 | [`CHANGELOG.zh-TW.md`](../CHANGELOG.zh-TW.md) |

## 文件結構

User journeys每種語言使用獨立文件，頁首以文字language switcher連到equivalent page。Project feature records以英文technical record作canonical source，另設繁中executive-summary companion，避免將每個hash、run ID及benchmark重複兩次。Active requirements只保存owner-approved what/why promise，active todos只保存implementation progress；完成後會整合durable knowledge並移除兩者。

```text
docs/
  README.md
  README.en.md
  v1-to-v2-migration.md
  v1-to-v2-migration.en.md
  features/
    README.md
    README.en.md
    v2-modernization.md
    v2-modernization.zh-TW.md
    validation-and-performance.md
    validation-and-performance.zh-TW.md
    release-and-distribution.md
    release-and-distribution.zh-TW.md
  requirements/
    .gitkeep
```

## 雙語政策

公開及student-facing內容使用正式台灣繁體中文（`zh-Hant-TW`）與自然technical English。專案行動以「本模版」或「本專案」第三身敘述。每份文件只有一個主要語言；頁首使用`繁體中文 | English`文字switcher連到具有相同topic set的equivalent page，不使用flag。Pair metadata及stable topic IDs在render時隱藏，checker亦要求shared code blocks保持一致，降低translation drift。文件語言、institution profile、cover language、degree及content mode互相獨立。新中文prose使用「論文範本」；產品名稱統一使用`LaTeX`、`XeLaTeX`、`BibTeX`、`latexmk`及`SyncTeX`正確casing。

此模式跟隨W3C的localized-page links、USWDS頁首language selector、GitHub locale-specific documentation及WCAG predominant-language原則。Mechanical checker只證明pair topics、switchers、links、shared code、casing及selected terminology結構；翻譯語義一致性仍要manual parity review確認。

```bash
python3 scripts/test/check-bilingual-docs.py
```

## 文件生命週期

1. 從owner-approved Intent開始。
2. 真正promise active時，建立`docs/requirements/<NN>-<slug>.md`。
3. 使用`todos/<NN>-<slug>.md`追蹤implementation，並保持雙向links。
4. Work shipped後，更新所有user surfaces及現有topical feature record。
5. 移除completed requirement及todo；不要為每個branch、commit、parser或bugfix永久保留active doc。
6. 沒有active requirement時，`docs/requirements/`只留`.gitkeep`。

目前沒有active requirement；`docs/requirements/`只包含`.gitkeep`。

## Source of truth

文件有差異時，依序以current tracked source／tests／scripts／`justfile`、immutable release tag及publicly re-downloaded assets、current docs、historical Git evidence解決。History解釋decision，不會覆蓋current tested behavior或自動重開deferred work。

```text
source and deterministic tests
-> immutable public release evidence
-> current user/project documentation
-> historical commits, PRs, and removed notes
```

## 現行狀態

正式source line為V2，使用XeLaTeX及direct `latexmk`學生build。最新immutable release為`v2.0.1.260719010734`。`main`是唯一persistent development branch，work使用short-lived `feat/<short-name>`。GitHub Releases在Overleaf update未approved及public read-back前仍是最新package的canonical source。

目前沒有active requirement；已完成implementation chronology保留在Git history。
