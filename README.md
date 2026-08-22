<!-- doc-pair: root-readme; lang: zh-Hant-TW; topics: project-overview,start-by-need,quick-start,choose-the-correct-setup,downloads-and-examples,migrate-from-1-x,other-institution-profiles,historical-acceptance,thesis-upload-and-printing,defense-certificate-faq,documentation-and-project-work,other-community-alternatives,licence -->

[繁體中文](README.md) | [English](README.en.md)

# National Cheng Kung University (NCKU) Thesis/Dissertation Template in LaTex<br>台灣國立成功大學碩博士用畢業論文 LaTex 模版

[在Overleaf開啟範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 專案簡介

本範本以XeLaTeX建置，供國立成功大學碩博士論文使用，可撰寫中文、英文或中英混合內容，並自動產生封面、目錄、圖表清單及其他前置頁面。論文資料只需填在一個設定檔；圖表、公式、引用的常用指令已備好；用1.x版本寫到一半的論文可以直接升級；其他學校的同學也可以建立自己學校的樣式。

本專案並非國立成功大學官方軟體，也不代表學校、圖書館、學位考試系統或任何系所的現行認可。使用前必須核對當年度規定；官方規定永遠優先於本範本。

以下官方指引由本專案最後查核於`2026-07-12`：

- [成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)
- [論文建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [教務處課務組論文格式規範](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## 按需要開始

| 你想做的事 | 先看這裡 |
| --- | --- |
| 立即開始撰寫論文 | [快速開始](#快速開始)及學生套件[`README.md`](thesis/README.md) |
| 填寫姓名、題目、學位及系所 | [`conf/README.md`](thesis/conf/README.md) |
| 由1.x專案升級 | [`1.x至2.x升級指南`](docs/v1-to-v2-migration.md) |
| 為其他學校建立樣式 | [`Customization.md`](thesis/template/style/Customization.md) |
| 上傳論文、列印及選擇正式證明書 | [學位論文上傳和列印說明](#學位論文上傳和列印說明) |
| 查看架構、驗證、發行及Overleaf記錄 | [`docs/README.md`](docs/README.md) |

## 快速開始

建置方式有三種，選一種即可：不想安裝任何軟體就用[Overleaf](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)；已安裝TeX Live、MacTeX或MiKTeX的在終端機執行下方指令；習慣Texmaker或TeXstudio的把編譯指令設為`latexmk`並以`thesis.tex`為主文件。三種方式的詳細步驟都在學生套件的[`README.md`](thesis/README.md)。

1. 從[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載`ncku-thesis-template-latex-<version>.zip`。
2. 解壓後先閱讀套件根目錄的[`README.md`](thesis/README.md)，按照其中的必改清單修改`conf/conf.tex`；每個欄位的說明見[`conf/README.md`](thesis/conf/README.md)。
3. 在`conf/conf.tex`停用`\ExampleMode`並填寫論文資料。
4. 在`context/context.tex`選擇章節，並於`context/`撰寫內容。
5. 用上述任何一種方式建置；終端機指令如下。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

## 選擇正確設定

成大同學不需要選擇任何學校樣式：解壓後直接填寫`conf/conf.tex`即可，封面語言、學位及內容模式都在該檔案內選擇。其他學校的同學請先依[`Customization.md`](thesis/template/style/Customization.md)建立自己學校的樣式，再填寫論文資料。

| 決定 | 在哪裡選 |
| --- | --- |
| 封面語言 | `conf/conf.tex`：`\DisplayCoverInChi`或`\DisplayCoverInEng` |
| 學位 | `conf/conf.tex`：`\MasterDegree`或`\PhdDegree` |
| 內容 | `conf/conf.tex`：註解`\ExampleMode`即使用自己的`context/context.tex` |
| 學校樣式 | 成大同學保持預設；其他學校的同學見`Customization.md` |

## 下載內容與範例

每個正式發行提供兩個下載：

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

第一個是學生套件，解壓後就是可以直接建置的論文專案，不含測試與發行工具；撰寫論文下載這個。第二個是範例套件，內有用同一版本產生的六個PDF，用來預覽成品：

```text
README.md
LICENSE
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

範例套件內的證明書PDF只是示範，提交時請使用學校系統的正式文件。GitHub自動產生的「Source code」ZIP是完整儲存庫，包含測試與發行工具，一般同學不需要。

## 由1.x升級

用1.x版本寫到一半的論文可以直接換到2.x：所有1.x的指令都保留，不需要重新命名。先備份整個1.x專案和最新的PDF；保留自己的`conf/conf.tex`、`context/`、圖片、書目及證明書檔案；用2.x套件的`template/`、`thesis.tex`及`cover.tex`替換原有檔案（曾修改`thesis.tex`的話，先記下修改再合併）；最後重新建置，逐項比較封面、日期、目錄、引用、參考文獻、正文及最後頁。完整步驟見[`1.x至2.x升級指南`](docs/v1-to-v2-migration.md)。

## 其他學校樣式

其他學校的同學可以沿用本範本的所有撰寫功能，只需要為自己的學校建立一個樣式。本範本把成大的版面、校名、日期規則及文字放在`template/style/ncku/`，論文資料則一律放在`conf/conf.tex`；建立新樣式時由中性骨架`template/style/custom/`複製一份，填入自己學校的資料即可。`custom`不是任何學校的正式格式，本專案目前也沒有其他學校的現成樣式。做法見[`Customization.md`](thesis/template/style/Customization.md)；成大同學可另外查看[`9個學院／110個系所指令目錄`](thesis/template/style/ncku/README.md)。

## Available to use 已被學校負責單位接受

依本專案保存的歷史紀錄，本範本的格式／設計曾於2015年由成大圖書館系統管理組數位論文小組檢查；本範本當時產生的中英文學位考試論文證明書亦曾由教務處課務組檢查。2018年，課務組另指出本範本產生的中文版證明書未經授權。

以上只屬歷史查核紀錄，不代表目前的學校、圖書館、學位考試系統或任何系所接受本範本的每項設定。資訊工程學系是本專案唯一有保存歷史使用紀錄的系所，但此紀錄亦不等於現行認可。使用前必須核對當年度學校及系所規定。

## 學位論文上傳和列印說明

以下摘要依據成大博碩士論文系統的[論文建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)（本專案最後查核：`2026-07-19`）。流程可能更新，提交時必須以官方系統及系所通知為準。

1. 使用符合系所規定、經指導教授同意送印的定稿版本製作PDF。
2. 將封面、口試合格證明書、中英文摘要、目次、表圖次、正文、參考文獻及附錄合併為單一PDF，並檢查頁碼、圖表及版面。
3. 上傳的PDF不要加入浮水印或保全；系統會在審核通過後處理電子全文。
4. 登入[成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)，完成資料欄位及上傳步驟，並送出審核。
5. 收到核准通知後重新登入系統，在step 5列印授權書及下載核准後的電子全文。紙本份數、簽名及離校程序須再向系所與圖書館確認。

## 模版和學位考試系統的學位考試論文證明書的FAQ

本專案保存的紀錄顯示，相關中英文證明書曾於2015年由教務處課務組檢查；當時的回覆不構成學校正式認可。2018年，課務組指出本範本產生的中文版證明書未經授權。歷史討論見[Issue #30：學位考試合格證明書與成大學校學位考試系統中列印的證明書並不相符](https://github.com/wengan-li/ncku-thesis-template-latex/issues/30)。

現行使用原則：

1. 中文版學位考試論文證明書應優先使用學位考試系統產出的正式版本，並以當年度學校及系所規定為準。
2. 本範本產生的證明書只供legacy／example及版面預覽，不代表正式文件或現行授權。
3. 英文版證明書的要求可能由系所另行規定；使用前須向系所確認版本、文字及簽名需求。
4. 口試、簽名或提交前如有任何疑問，應先取得當期官方系統版本，不要只依賴本範本產生的證明書。

延伸政策紀錄：[發行、證明書與浮水印政策](docs/features/release-and-distribution.md)。

## 文件與專案工作

如果你只需要撰寫論文，請由套件內README及configuration guide開始。本專案的architecture、validation、release及Overleaf evidence記錄於[`docs/README.md`](docs/README.md)；歷年貢獻者記錄於[`CONTRIBUTE`](CONTRIBUTE)。完整儲存庫使用[`just`](https://just.systems/)統一專案commands；學生套件不依賴`just`。

```bash
just          # list commands
just thesis   # build canonical PDF and SyncTeX
just watch    # continuous incremental rebuild, no extra viewer
just test     # full regression gate
just ci       # canonical CI gate
just clean    # remove rebuildable artifacts
```

## 其他社群方案

下列社群專案由各自作者維護，與本專案沒有隸屬或背書關係。使用前請核對其版本、授權及學校最新規定。

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX

## 授權

本專案採用Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International授權；完整條款見[`LICENSE`](LICENSE)。成大浮水印、logo、官方證明書及其他institution assets可能由各自權利人擁有，repository-wide licence不會自動授權其他用途。使用或再發佈前請確認來源及權利。

<p align="center">
  <img src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" alt="Creative Commons BY-NC-SA 4.0" />
</p>
