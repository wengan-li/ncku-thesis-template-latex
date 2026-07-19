<!-- bilingual:complete -->

# 成大論文範本學生專案 / NCKU thesis-template student project

此目錄是可直接使用的學生專案。版本化的GitHub Release學生套件會將這些檔案放在單一`ncku-thesis-template-latex/`目錄內；完整儲存庫的測試、發行腳本及維護工具不會包含在學生套件中。

This directory is the complete student project. The versioned GitHub Release student package places these files directly under one `ncku-thesis-template-latex/` directory; repository tests, release scripts, and maintainer tooling are intentionally excluded.

## 開始撰寫 / Start writing

**繁體中文**

1. 開啟`conf/conf.tex`。撰寫自己的論文時，請將`\ExampleMode`註解；啟用時會編譯完整教學範例。
2. 按照[`conf/README.md`](conf/README.md)填寫題目、姓名、學位、日期、系所、指導教授及其他論文資料。
3. 在`context/context.tex`選擇章節，並於`context/`內撰寫內容。
4. 始終以`thesis.tex`作為主文件。

**English**

1. Open `conf/conf.tex`. Comment out `\ExampleMode` for your own thesis; when enabled, it builds the complete teaching example.
2. Follow [`conf/README.md`](conf/README.md) to enter the title, names, degree, dates, department, advisors, and other thesis information.
3. Select chapters in `context/context.tex` and write your content under `context/`.
4. Always use `thesis.tex` as the root document.

The teaching example is useful as a reference but rebuilds more slowly than a normal thesis.

## 選擇設定 / Choose independent settings

**繁體中文**

文件語言、學校樣式設定檔、封面語言、學位及內容模式互相獨立。國際學生可以使用成大`ncku` profile；台灣使用者亦可以維護其他學校的profile。不要因讀者語言而選擇學校profile。

**English**

Documentation language, institution profile, cover language, degree, and content mode are independent. An international student may use the NCKU `ncku` profile, while a Taiwan reader may maintain another institution profile. Do not select an institution profile from the reader's language.

| Decision / 決定 | Choices / 選項 |
| --- | --- |
| Institution / 學校 | default `ncku`; maintained custom profile for another institution |
| Cover language / 封面語言 | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree / 學位 | `\MasterDegree` or `\PhdDegree` |
| Content / 內容 | own `context/context.tex` or `\ExampleMode` teaching example |

The default project selects the NCKU profile in `template/style/style.tex`. Follow [`template/style/Customization.md`](template/style/Customization.md) only when maintaining a non-NCKU institutional fork.

## 設定論文資料 / Configure thesis information

**繁體中文**

`conf/conf.tex`是從v1.8.2保留的相容設定檔。為確保既有1.x專案可安全升級，該檔案在2.x保持byte-identical，因此原有註解主要為中文。請使用套件內的雙語[`conf/README.md`](conf/README.md)逐項查閱設定；不要為了翻譯而更改macro名稱或新增`conf/style.tex`。

**English**

`conf/conf.tex` is the compatibility-preserved configuration file from v1.8.2. It remains byte-identical throughout 2.x so existing projects can migrate safely, and its original comments are therefore mainly Chinese. Use the packaged bilingual [`conf/README.md`](conf/README.md) for a field-by-field guide. Do not rename macros or add `conf/style.tex` merely for translation.

Student metadata belongs in `conf/`; institution geometry, wording, date policy, and assets belong under `template/style/<profile>/`.

## 由1.x升級 / Migrate from 1.x

**繁體中文**

V2透過相容層保留完整、經machine audit的1.x helper surface。升級進行中的論文前，先commit或封存完整1.x專案並保存最新PDF。保留`conf/conf.tex`、`context/`、圖片、書目資料及本地證明書檔案；以V2替換template-owned檔案，並有意識地merge對`thesis.tex`的本地修改。完成後，使用下方direct build command，逐項比較封面、日期、目錄、引用、參考文獻、正文及最後頁。

**English**

V2 preserves the complete machine-audited 1.x helper surface through a compatibility adapter. Before migrating a thesis in progress, commit or archive the complete 1.x project and save its latest PDF. Preserve `conf/conf.tex`, `context/`, figures, bibliography data, and local certificate files; replace template-owned files with V2 and deliberately merge local edits to `thesis.tex`. Then run the direct build command below and compare the cover, dates, contents, citations, bibliography, body, and final pages.

The complete compatibility-first and native-v2 paths are maintained at [`docs/v1-to-v2-migration.md`](https://github.com/wengan-li/ncku-thesis-template-latex/blob/main/docs/v1-to-v2-migration.md). Existing 1.x helper calls do not require renaming during 2.x.

## 建置正式文件 / Build the final document

**繁體中文**

安裝包含XeLaTeX、BibTeX及`latexmk`的TeX發行版。最低要求為LaTeX2e format 2020-10-01；建議使用TeX Live 2021或更新版本，發行CI目前使用TeX Live 2026。在包含`thesis.tex`的專案根目錄執行以下唯一正式建置指令。

**English**

Install a TeX distribution containing XeLaTeX, BibTeX, and `latexmk`. The minimum LaTeX2e format is 2020-10-01; TeX Live 2021 or newer is recommended, and release CI currently uses TeX Live 2026. Run the following canonical final-build command from the project root containing `thesis.tex`.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

`latexmk` automatically runs XeLaTeX and BibTeX until the table of contents, bibliography, references, and PDF outline converge. Do not guess a manual sequence of compiler runs.

To remove generated files / 清除產生檔案：

```bash
latexmk -C thesis.tex
```

## 持續預覽與編輯器 / Continuous preview and editors

**繁體中文**

撰寫期間可保持下方指令運行。每次儲存追蹤中的TeX、書目、圖片或included file時，`latexmk`只執行所需的compiler passes。`-view=none`避免開啟第二個PDF viewer；請讓Texmaker、TeXstudio或其他viewer重新載入現有`thesis.pdf`。按`Ctrl-C`停止。

**English**

Keep the following command running while writing. Whenever a tracked TeX, bibliography, figure, or included file changes, `latexmk` runs only the required compiler passes. `-view=none` prevents a second PDF viewer from opening; let Texmaker, TeXstudio, or another viewer reload the existing `thesis.pdf`. Stop with `Ctrl-C`.

```bash
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

Texmaker/TeXstudio compiler command / 編譯指令：

```text
latexmk -xelatex -synctex=1 -interaction=nonstopmode %.tex
```

Set `thesis.tex` as the root/master document / 將`thesis.tex`設為主文件。

## 初稿、浮水印與證明書 / Draft, watermark, and certificate

**繁體中文**

正式輸出預設不顯示封面`(初稿)`／`(Draft)`、斜向`DRAFT`文字或學校logo浮水印。只有在撰寫或審閱期間確實需要時，才於`conf/conf.tex`啟用`\DisplayDraft`。斜向文字浮水印及學校logo浮水印是另外兩個明確opt-in功能；不要因API存在就加入正式提交PDF。學校系統可能會對核准後的電子全文加入自己的浮水印。

正式提交時，應按學校規定使用學位考試系統產出的證明書。本範本產生的證明書只供legacy/example及regression用途，並非官方文件。

**English**

Final output defaults to no `(初稿)` / `(Draft)` cover marker, no diagonal `DRAFT` text, and no institution-logo watermark. Enable `\DisplayDraft` in `conf/conf.tex` only when deliberately required during writing or review. Diagonal text and institution-logo watermarks are two separate explicit opt-ins; do not add either to a submission PDF merely because the APIs exist. The university system may apply its own watermark to the approved electronic copy.

For final submission, use the defense-certificate document produced by the official degree-examination system when required. Template-generated certificates are legacy/example and regression outputs, not official documents.

## 提交前檢查 / Before submission

**繁體中文**

1. 停止任何continuous-preview process，重新執行正式建置指令。
2. 確認log沒有未解決的references、citations或rerun warnings。
3. 確認PDF沒有非預期的初稿標記、文字浮水印或logo浮水印。
4. 完整檢查頁碼、目錄、圖表清單、參考文獻、字型及最後頁。
5. 核對當年度成大、圖書館及所屬系所的最新要求；現行官方規定永遠優先。
6. 使用學校系統要求的正式證明書與提交流程。

**English**

1. Stop any continuous-preview process and run the final-build command again.
2. Confirm that the log contains no unresolved references, citations, or rerun warnings.
3. Confirm that the PDF has no unexpected Draft marker, text watermark, or logo watermark.
4. Review pagination, contents, figure/table lists, bibliography, fonts, and final pages.
5. Check the current NCKU, library, and department requirements; current official rules always take precedence.
6. Use the official certificate and submission workflow required by the university system.

## 其他社群方案 / Other community alternatives

**繁體中文**

如本範本不符合需要，可評估下列不定期更新的社群專案。它們並非由本專案維護；使用前請自行核對版本、授權及學校規定。

**English**

If this template does not meet your needs, evaluate the following independently maintained community projects. They are not maintained by this project; verify their versions, licences, and current university requirements before use.

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX
