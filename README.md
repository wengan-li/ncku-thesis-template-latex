<!-- bilingual:complete -->

# 國立成功大學論文範本 / NCKU Thesis and Dissertation Template for LaTeX

[**Open as Template in Overleaf / 在Overleaf開啟範本**](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 專案簡介 / Project overview

**繁體中文**

這是由社群維護、以XeLaTeX建置的國立成功大學碩博士論文範本，可撰寫中文、英文或中英混合內容，並自動產生封面、目錄、圖表清單及其他前置頁面。它提供學生設定、可重用的LaTeX helpers、1.x相容層，以及將樣式移植到其他學校的profile架構。

本專案並非國立成功大學官方軟體，也不代表學校、圖書館、學位考試系統或任何系所的現行認可。使用前必須核對當年度規定；官方規定永遠優先於本範本。

**English**

This community-maintained XeLaTeX template supports Chinese, English, and mixed-language NCKU master's theses and doctoral dissertations. It generates the cover, contents, figure/table lists, and other front matter, and provides student configuration, reusable LaTeX helpers, a 1.x compatibility adapter, and institution profiles for maintained ports.

This is not official NCKU software and does not represent current endorsement by the university, library, degree-examination system, or any department. Verify the current rules before use; official requirements always take precedence.

Official guidance last checked on `2026-07-12` / 官方指引最後查核日期：`2026-07-12`：

- [NCKU thesis system / 成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)
- [Submission guidance / 建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [Curriculum Division thesis-format guidance / 教務處課務組論文格式規範](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## 發行與Overleaf狀態 / Release and Overleaf status

**繁體中文**

最新正式原始碼及學生套件由[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases/latest)提供。目前最新production release是`v2.0.1.260719010734`。V2保留完整machine-audited 1.x public API及XeLaTeX學生使用路徑，同時整理profile、相容層、測試及下載套件。

既有Overleaf Gallery頁面仍可公開使用。維護者已確認將V2上載到原本的Overleaf project並重新提交Gallery update review；在Overleaf批准並完成public read-back前，不能將「已提交」寫成「已批准」，最新V2仍以GitHub Releases為準。

**English**

The latest production source and student package are available from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases/latest). The current production release is `v2.0.1.260719010734`. V2 preserves the complete machine-audited 1.x public API and direct XeLaTeX student workflow while organizing profiles, compatibility, tests, and downloads.

The existing Overleaf Gallery page remains public. The maintainer has confirmed that V2 was uploaded to the original Overleaf project and resubmitted for Gallery update review. Until Overleaf approves it and the public page is independently read back, “submitted” must not be treated as “approved”; GitHub Releases remains canonical for the latest V2 package.

Detailed state / 詳細狀態：[`docs/features/release-and-distribution.md`](docs/features/release-and-distribution.md#recorded-gallery-state)

## 選擇正確設定 / Choose the correct setup

**繁體中文**

文件語言、學校profile、封面語言、學位及內容模式是不同決定。國際學生如就讀成大仍使用`ncku` profile；台灣維護者為其他學校建立範本時則使用`custom`或另一個institution profile。不要將「英文」等同「非成大」。

**English**

Documentation language, institution profile, cover language, degree, and content mode are separate decisions. An international student at NCKU still uses the `ncku` profile; a Taiwan maintainer porting the template to another institution uses `custom` or another maintained profile. Do not equate “English” with “non-NCKU.”

| Decision / 決定 | Choices / 選項 |
| --- | --- |
| Institution / 學校 | default `ncku`; maintained custom profile for another institution |
| Cover language / 封面語言 | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree / 學位 | `\MasterDegree` or `\PhdDegree` |
| Content / 內容 | own `context/context.tex` or `\ExampleMode` teaching example |

Historical checks in 2015 and reports from individual departments are provenance only, not current approval. CSIE is the only department with documented historical use in this repository; every student must still verify current department rules.

## 快速開始 / Quick start

**繁體中文**

1. 從[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載`ncku-thesis-template-latex-<version>.zip`。
2. 解壓後先閱讀套件根目錄的[`README.md`](thesis/README.md)及[`conf/README.md`](thesis/conf/README.md)。
3. 在`conf/conf.tex`停用`\ExampleMode`並填寫論文資料。
4. 在`context/context.tex`選擇章節，並於`context/`撰寫內容。
5. 在包含`thesis.tex`的目錄執行下方指令。

**English**

1. Download `ncku-thesis-template-latex-<version>.zip` from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases).
2. Extract it and read [`README.md`](thesis/README.md) and [`conf/README.md`](thesis/conf/README.md) at the package root.
3. Disable `\ExampleMode` in `conf/conf.tex` and enter thesis information.
4. Select chapters in `context/context.tex` and write content under `context/`.
5. Run the following command from the directory containing `thesis.tex`.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Use `thesis.tex` as the root/master document. `latexmk` handles XeLaTeX, BibTeX, and required reruns automatically.

## 下載內容與範例 / Downloads and examples

**繁體中文**

每個正式release提供兩個版本化下載。學生套件只包含可直接編輯的`thesis/`project tree，不包含`justfile`、CI、tests或release scripts。Examples套件包含由同一個immutable source revision產生並驗證的六個PDF，供預覽及regression evidence使用。GitHub自動產生的Source code ZIP則包含完整儲存庫。

**English**

Each production release provides two versioned downloads. The student package contains only the directly editable `thesis/` project tree, excluding `justfile`, CI, tests, and release scripts. The examples package contains six PDFs built and verified from the same immutable source revision for preview and regression evidence. GitHub's automatic Source code ZIP contains the complete repository.

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

Examples package / 範例套件：

```text
README.md
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

The generated certificate PDFs are unofficial demonstrations. Use current official documents for submission.

## 由1.x升級 / Migrate from 1.x

**繁體中文**

既有論文應先commit或封存完整1.x專案並保存最新PDF。保留`conf/conf.tex`、`context/`、圖片、書目資料及本地證明書；以V2替換template-owned檔案，並有意識地merge `thesis.tex`的本地修改。V2在完整2.x line保留經audit的1.x helper surface，compatibility-first path不要求重新命名helpers。

**English**

Commit or archive the complete 1.x project and save its latest PDF before migrating. Preserve `conf/conf.tex`, `context/`, figures, bibliography data, and local certificate files; replace template-owned files with V2 and deliberately merge local changes to `thesis.tex`. V2 preserves the audited 1.x helper surface throughout 2.x, so the compatibility-first path requires no helper renaming.

Complete guide / 完整指南：[`docs/v1-to-v2-migration.md`](docs/v1-to-v2-migration.md)

## 其他學校樣式 / Other institution profiles

**繁體中文**

V2將共用renderer、NCKU policy及其他學校port分成`base`、`ncku`及`custom`。學生論文資料仍放在`conf/conf.tex`；學校geometry、名稱、日期政策、文字及assets放在`template/style/<profile>/`。非成大維護者由`template/style/custom/`開始，不要直接修改共用renderer或先載入NCKU再覆寫。

**English**

V2 separates shared rendering, NCKU policy, and other-institution ports into `base`, `ncku`, and `custom`. Student thesis data remains in `conf/conf.tex`; institution geometry, names, date policy, wording, and assets belong under `template/style/<profile>/`. Non-NCKU maintainers start from `template/style/custom/` rather than editing the shared renderer or loading NCKU before overriding it.

Guide / 指南：[`thesis/template/style/Customization.md`](thesis/template/style/Customization.md)

## 提交、浮水印與證明書 / Submission, watermark, and certificate

**繁體中文**

正式輸出預設沒有封面初稿標記、斜向`DRAFT`文字或學校logo浮水印。三者是獨立的opt-in功能；不要因API存在就加入提交PDF。現行流程要求以學校系統產出的文件為準，系統亦可能在核准後的電子全文加入自己的浮水印。

學位考試合格證明書應優先使用學位考試系統產出的正式版本。本範本產生的證明書只供legacy/example及regression用途。2015／2018的歷史查核記錄不構成現時授權或官方認可。

**English**

Final output defaults to no cover Draft marker, diagonal `DRAFT` text, or institution-logo watermark. These are three independent opt-ins; do not add them to a submission PDF merely because APIs exist. Follow the current university-system workflow, which may apply its own watermark to the approved electronic copy.

Use the official degree-examination-system defense certificate when required. Template-generated certificates are legacy/example and regression outputs. Historical checks from 2015/2018 do not constitute current authorization or endorsement.

Policy record / 政策記錄：[`docs/features/release-and-distribution.md`](docs/features/release-and-distribution.md#draft-and-watermark-policy)

## 文件與維護 / Documentation and maintenance

**繁體中文**

學生應由套件內README及configuration guide開始。維護者可由[`docs/README.md`](docs/README.md)進入architecture、validation、release及Overleaf records。完整儲存庫使用[`just`](https://just.systems/)統一maintainer commands；學生套件不依賴`just`。

**English**

Students start from the packaged README and configuration guide. Maintainers use [`docs/README.md`](docs/README.md) to find architecture, validation, release, and Overleaf records. The full repository uses [`just`](https://just.systems/) for maintainer commands; the student package does not depend on `just`.

```bash
just          # list commands
just thesis   # build canonical PDF and SyncTeX
just watch    # continuous incremental rebuild, no extra viewer
just test     # full regression gate
just ci       # canonical CI gate
just clean    # remove rebuildable artifacts
```

Version history / 版本記錄：[`CHANGELOG.md`](CHANGELOG.md)

## 其他社群方案 / Other community alternatives

**繁體中文**

下列社群專案由各自作者維護，與本專案沒有隸屬或背書關係。使用前請核對其版本、授權及學校最新規定。

**English**

The following community projects are maintained by their respective authors and are neither affiliated with nor endorsed by this project. Verify their versions, licences, and current university rules before use.

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX

## 授權 / Licence

**繁體中文**

本專案採用Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International授權；完整條款見[`LICENSE`](LICENSE)。成大浮水印、logo、官方證明書及其他institution assets可能由各自權利人擁有，repository-wide licence不會自動授權其他用途。使用或再發佈前請確認來源及權利。

**English**

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International licence; see [`LICENSE`](LICENSE). NCKU watermarks, logos, official certificates, and other institution assets may remain owned by their respective rights holders, and the repository-wide licence does not automatically authorize unrelated use or redistribution. Verify provenance and rights before reuse.

<p align="center">
  <img src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" alt="Creative Commons BY-NC-SA 4.0" />
</p>
