<!-- bilingual:complete -->

# 維護文件 / Maintainer documentation

目前正式release：[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

## 文件入口 / Start here

**繁體中文**

本目錄是已發行成大論文範本的維護文件。學生應優先閱讀套件內的`thesis/README.md`及`thesis/conf/README.md`；本目錄負責migration、architecture、validation、release及Overleaf records。Root `README.md`是public router，不是maintainer runbook。

**English**

This directory contains maintainer documentation for the released NCKU thesis template. Students start from the packaged `thesis/README.md` and `thesis/conf/README.md`; this directory owns migration, architecture, validation, release, and Overleaf records. Root `README.md` is the public router, not the maintainer runbook.

| Audience or task / 讀者或工作 | Canonical document / 文件 |
| --- | --- |
| Student build/edit / 學生撰寫 | [`thesis/README.md`](../thesis/README.md) |
| Student configuration / 學生設定 | [`thesis/conf/README.md`](../thesis/conf/README.md) |
| 1.x to 2.x migration / 1.x升級 | [`v1-to-v2-migration.md`](v1-to-v2-migration.md) |
| V2 architecture / V2架構 | [`features/v2-modernization.md`](features/v2-modernization.md) |
| Tests/output/performance / 測試輸出效能 | [`features/validation-and-performance.md`](features/validation-and-performance.md) |
| Release/Overleaf / 發行與Overleaf | [`features/release-and-distribution.md`](features/release-and-distribution.md) |
| Version history / 版本記錄 | [`CHANGELOG.md`](../CHANGELOG.md) |
| Active implementation / 進行中工作 | [Requirement 02](requirements/02-bilingual-documentation.md) and [Todo 01](../todos/01-bilingual-documentation.md) |

## 文件結構 / Directory model

**繁體中文**

User journeys提供完整繁中及英文。Maintainer feature records以繁中executive summary加完整英文technical body，避免將每個hash、run ID及benchmark重複兩次。Active requirements只保存owner-approved what/why promise，active todos只保存implementation progress；完成後會整合durable knowledge並移除兩者。

**English**

User journeys are complete in Traditional Chinese and English. Maintainer feature records use a Traditional-Chinese executive summary plus the complete English technical body so hashes, run IDs, and benchmarks are not duplicated. Active requirements store only owner-approved what/why promises and active todos store implementation progress; both are removed after durable knowledge is consolidated.

```text
docs/
  README.md
  v1-to-v2-migration.md
  features/
    README.md
    v2-modernization.md
    validation-and-performance.md
    release-and-distribution.md
  requirements/
    .gitkeep
    02-bilingual-documentation.md  # active only while implementation remains

todos/
  01-bilingual-documentation.md    # active implementation progress
```

Git history keeps per-branch checklists, superseded plans, and detailed chronology.

## 雙語政策 / Bilingual policy

**繁體中文**

公開及student-facing內容使用正式台灣繁體中文（`zh-Hant-TW`）與自然technical English。每個topic將兩種語言相鄰放置，paths、commands、macros、logs及code blocks只保留一份。文件語言、institution profile、cover language、degree及content mode互相獨立。新中文prose使用「論文範本」；產品名稱統一使用`LaTeX`、`XeLaTeX`、`BibTeX`、`latexmk`及`SyncTeX`正確casing。

Mechanical checker只證明section、links、casing及selected terminology結構；翻譯語義一致性必須由human parity review確認。

**English**

Public and student-facing content uses formal Taiwan Traditional Chinese (`zh-Hant-TW`) and natural technical English. The language blocks are adjacent within each topic, while paths, commands, macros, logs, and code blocks have one shared copy. Documentation language, institution profile, cover language, degree, and content mode are independent. New Chinese prose uses `論文範本`; product names retain exact `LaTeX`, `XeLaTeX`, `BibTeX`, `latexmk`, and `SyncTeX` casing.

The mechanical checker proves only section, link, casing, and selected-terminology structure. Semantic translation parity remains a human review gate.

Run / 執行：

```bash
python3 scripts/test/check-bilingual-docs.py
```

## 文件生命週期 / Documentation lifecycle

**繁體中文**

1. 從owner-approved Intent開始。
2. 真正promise active時，建立`docs/requirements/<NN>-<slug>.md`。
3. 使用`todos/<NN>-<slug>.md`追蹤implementation，並保持雙向links。
4. Work shipped後，更新所有user surfaces及現有topical feature record。
5. 移除completed requirement及todo；不要為每個branch、commit、parser或bugfix永久保留active doc。
6. 沒有active requirement時，`docs/requirements/`只留`.gitkeep`。

**English**

1. Start from an owner-approved Intent.
2. Create `docs/requirements/<NN>-<slug>.md` only while a real promise is active.
3. Track implementation in `todos/<NN>-<slug>.md` and keep backlinks synchronized.
4. When work ships, update every user surface and the owning topical feature record.
5. Remove the completed requirement and todo; do not keep an active document per branch, commit, parser, or bugfix.
6. When no requirement is active, retain only `.gitkeep` under `docs/requirements/`.

Current bilingual-documentation work remains active until exact staged-tree, package, direct-build, semantic, and canonical-output gates pass.

## Source of truth / Source-of-truth order

**繁體中文**

文件有差異時，依序以current tracked source／tests／scripts／`justfile`、immutable release tag及publicly re-downloaded assets、current docs、historical Git evidence解決。History解釋decision，不會覆蓋current tested behavior或自動重開deferred work。

**English**

On drift, resolve facts in this order: current tracked source/tests/scripts/`justfile`; immutable release tag and publicly re-downloaded assets; current documentation; historical Git evidence. History explains decisions but does not override current tested behavior or automatically reopen deferred work.

```text
source and deterministic tests
-> immutable public release evidence
-> current user/maintainer documentation
-> historical commits, PRs, and removed notes
```

## 現行狀態 / Current state

**繁體中文**

正式source line為V2，使用XeLaTeX及direct `latexmk`學生build。最新immutable release為`v2.0.1.260719010734`。`main`是唯一persistent development branch，work使用short-lived `feat/<short-name>`。GitHub Releases在Overleaf update未approved及public read-back前仍是最新package的canonical source。

**English**

The production source line is V2 with XeLaTeX and a direct `latexmk` student build. The latest immutable release is `v2.0.1.260719010734`. `main` is the only persistent development branch and work uses short-lived `feat/<short-name>` branches. GitHub Releases remains canonical for the latest package until the Overleaf update is approved and publicly read back.

Active work / 進行中工作：[`requirements/02-bilingual-documentation.md`](requirements/02-bilingual-documentation.md) and [`todos/01-bilingual-documentation.md`](../todos/01-bilingual-documentation.md).
