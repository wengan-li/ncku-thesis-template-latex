<!-- doc-pair: student-readme; lang: zh-Hant-TW; topics: start-writing,choose-independent-settings,configure-thesis-information,migrate-from-1-x,build-the-final-document,continuous-preview-and-editors,draft-watermark-and-certificate,before-submission,other-community-alternatives -->

[繁體中文](README.md) | [English](README.en.md)

# 成大論文範本學生專案

此目錄是可直接使用的學生專案。版本化的GitHub Release學生套件會將這些檔案放在單一`ncku-thesis-template-latex/`目錄內；完整儲存庫的測試、發行腳本及維護工具不會包含在學生套件中。

## 開始撰寫

1. 開啟`conf/conf.tex`。撰寫自己的論文時，請將`\ExampleMode`註解；啟用時會編譯完整教學範例。
2. 按照[`conf/README.md`](conf/README.md)填寫題目、姓名、學位、日期、系所、指導教授及其他論文資料。
3. 在`context/context.tex`選擇章節，並於`context/`內撰寫內容。
4. 始終以`thesis.tex`作為主文件。

## 選擇設定

文件語言、學校樣式設定檔、封面語言、學位及內容模式互相獨立。國際學生可以使用成大`ncku` profile；台灣使用者亦可以維護其他學校的profile。不要因讀者語言而選擇學校profile。

| 決定 | 選項 |
| --- | --- |
| 學校 | 預設`ncku`；其他學校使用維護中的custom profile |
| 封面語言 | `\DisplayCoverInChi`或`\DisplayCoverInEng` |
| 學位 | `\MasterDegree`或`\PhdDegree` |
| 內容 | 自己的`context/context.tex`或`\ExampleMode`教學範例 |

## 設定論文資料

`conf/conf.tex`是從v1.8.2保留的相容設定檔。為確保既有1.x專案可安全升級，該檔案在2.x保持byte-identical，因此原有註解主要為中文。請使用套件內的繁中[`conf/README.md`](conf/README.md)逐項查閱設定；不要為了翻譯而更改macro名稱或新增`conf/style.tex`。

## 由1.x升級

V2透過相容層保留完整、經machine audit的1.x helper surface。升級進行中的論文前，先commit或封存完整1.x專案並保存最新PDF。保留`conf/conf.tex`、`context/`、圖片、書目資料及本地證明書檔案；以V2替換template-owned檔案，並有意識地merge對`thesis.tex`的本地修改。完成後，使用下方direct build command，逐項比較封面、日期、目錄、引用、參考文獻、正文及最後頁。

完整指南：[`docs/v1-to-v2-migration.md`](https://github.com/wengan-li/ncku-thesis-template-latex/blob/main/docs/v1-to-v2-migration.md)

## 建置正式文件

安裝包含XeLaTeX、BibTeX及`latexmk`的TeX發行版。最低要求為LaTeX2e format 2020-10-01；建議使用TeX Live 2021或更新版本，發行CI目前使用TeX Live 2026。在包含`thesis.tex`的專案根目錄執行以下唯一正式建置指令。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

```bash
latexmk -C thesis.tex
```

## 持續預覽與編輯器

撰寫期間可保持下方指令運行。每次儲存追蹤中的TeX、書目、圖片或included file時，`latexmk`只執行所需的compiler passes。`-view=none`避免開啟第二個PDF viewer；請讓Texmaker、TeXstudio或其他viewer重新載入現有`thesis.pdf`。按`Ctrl-C`停止。

```bash
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

```text
latexmk -xelatex -synctex=1 -interaction=nonstopmode %.tex
```

Set `thesis.tex` as the root/master document / 將`thesis.tex`設為主文件。

## 初稿、浮水印與證明書

正式輸出預設不顯示封面`(初稿)`／`(Draft)`、斜向`DRAFT`文字或學校logo浮水印。只有在撰寫或審閱期間確實需要時，才於`conf/conf.tex`啟用`\DisplayDraft`。斜向文字浮水印及學校logo浮水印是另外兩個明確opt-in功能；不要因API存在就加入正式提交PDF。學校系統可能會對核准後的電子全文加入自己的浮水印。

正式提交時，應按學校規定使用學位考試系統產出的證明書。本範本產生的證明書只供legacy/example及regression用途，並非官方文件。

## 提交前檢查

1. 停止任何continuous-preview process，重新執行正式建置指令。
2. 確認log沒有未解決的references、citations或rerun warnings。
3. 確認PDF沒有非預期的初稿標記、文字浮水印或logo浮水印。
4. 完整檢查頁碼、目錄、圖表清單、參考文獻、字型及最後頁。
5. 核對當年度成大、圖書館及所屬系所的最新要求；現行官方規定永遠優先。
6. 使用學校系統要求的正式證明書與提交流程。

## 其他社群方案

如本範本不符合需要，可評估下列不定期更新的社群專案。它們並非由本專案維護；使用前請自行核對版本、授權及學校規定。

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX
