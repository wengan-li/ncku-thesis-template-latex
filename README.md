<!-- doc-pair: root-readme; lang: zh-Hant-TW; topics: project-overview,historical-acceptance,choose-the-correct-setup,quick-start,downloads-and-examples,migrate-from-1-x,other-institution-profiles,thesis-upload-and-printing,defense-certificate-faq,documentation-and-project-work,other-community-alternatives,licence -->

[繁體中文](README.md) | [English](README.en.md)

# National Cheng Kung University (NCKU) Thesis/Dissertation Template in LaTex<br>台灣國立成功大學碩博士用畢業論文 LaTex 模版

[在Overleaf開啟範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 專案簡介

本模版以XeLaTeX建置，供國立成功大學碩博士論文使用，可撰寫中文、英文或中英混合內容，並自動產生封面、目錄、圖表清單及其他前置頁面。本模版提供學生設定、可重用的LaTeX helpers、1.x相容層，以及讓其他學校的同學建立自己樣式的profile架構。

本專案並非國立成功大學官方軟體，也不代表學校、圖書館、學位考試系統或任何系所的現行認可。使用前必須核對當年度規定；官方規定永遠優先於本範本。

- [成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)
- [論文建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [教務處課務組論文格式規範](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## Available to use 已被學校負責單位接受

依本專案保存的歷史紀錄，本模版的格式／設計曾於2015年由成大圖書館系統管理組數位論文小組檢查；本模版當時產生的中英文學位考試論文證明書亦曾由教務處課務組檢查。2018年，課務組另指出本模版產生的中文版證明書未經授權。

以上只屬歷史查核紀錄，不代表目前的學校、圖書館、學位考試系統或任何系所接受本模版的每項設定。資訊工程學系是本專案唯一有保存歷史使用紀錄的系所，但此紀錄亦不等於現行認可。使用前必須核對當年度學校及系所規定。

## 選擇正確設定

文件語言、學校profile、封面語言、學位及內容模式是不同設定。成大同學無論使用中文或英文文件，都使用`ncku` profile；其他學校的同學如要建立自己的範本，可使用`custom`或另一個institution profile。

| 決定 | 選項 |
| --- | --- |
| 學校 | 成大同學使用預設`ncku`；其他學校的同學可使用custom profile |
| 封面語言 | `\DisplayCoverInChi`或`\DisplayCoverInEng` |
| 學位 | `\MasterDegree`或`\PhdDegree` |
| 內容 | 自己的`context/context.tex`或`\ExampleMode`教學範例 |

## 快速開始

1. 從[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載`ncku-thesis-template-latex-<version>.zip`。
2. 解壓後先閱讀套件根目錄的[`README.md`](thesis/README.md)及[`conf/README.md`](thesis/conf/README.md)。
3. 在`conf/conf.tex`停用`\ExampleMode`並填寫論文資料。
4. 在`context/context.tex`選擇章節，並於`context/`撰寫內容。
5. 在包含`thesis.tex`的目錄執行下方指令。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

## 下載內容與範例

每個正式release提供兩個版本化下載。學生套件只包含可直接編輯的`thesis/`project tree，不包含`justfile`、CI、tests或release scripts。Examples套件包含由同一個immutable source revision產生並驗證的六個PDF，供預覽及regression evidence使用。GitHub自動產生的Source code ZIP則包含完整儲存庫。

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

```text
README.md
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

## 由1.x升級

既有論文應先commit或封存完整1.x專案並保存最新PDF。保留`conf/conf.tex`、`context/`、圖片、書目資料及本地證明書；以V2替換template-owned檔案，並有意識地merge `thesis.tex`的本地修改。V2在完整2.x line保留經audit的1.x helper surface，compatibility-first path不要求重新命名helpers。

## 其他學校樣式

本模版將共用renderer、NCKU policy及其他學校port分成`base`、`ncku`及`custom`。學生論文資料仍放在`conf/conf.tex`；學校geometry、名稱、日期政策、文字及assets放在`template/style/<profile>/`。`custom`是neutral skeleton，不是任何學校的ready-to-submit profile；本專案目前亦沒有NTU profile。其他學校的同學可由`template/style/custom/`開始，不要直接修改共用renderer或先載入NCKU再覆寫。

NCKU學生可查看完整[`9個學院／110個系所preset目錄`](thesis/template/style/ncku/README.md)；其他學校的同學則使用generic institution APIs，並參考[`Customization.md`](thesis/template/style/Customization.md)內明確標示為illustrative的NTU wiring例子。

## 學位論文上傳和列印說明

以下摘要依據成大博碩士論文系統的[論文建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)（本專案最後查核：`2026-07-19`）。流程可能更新，提交時必須以官方系統及系所通知為準。

1. 使用符合系所規定、經指導教授同意送印的定稿版本製作PDF。
2. 將封面、口試合格證明書、中英文摘要、目次、表圖次、正文、參考文獻及附錄合併為單一PDF，並檢查頁碼、圖表及版面。
3. 上傳的PDF不要加入浮水印或保全；系統會在審核通過後處理電子全文。
4. 登入[成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)，完成資料欄位及上傳步驟，並送出審核。
5. 收到核准通知後重新登入系統，在step 5列印授權書及下載核准後的電子全文。紙本份數、簽名及離校程序須再向系所與圖書館確認。

## 模版和學位考試系統的學位考試論文證明書的FAQ

本專案保存的紀錄顯示，相關中英文證明書曾於2015年由教務處課務組檢查；當時的回覆不構成學校正式認可。2018年，課務組指出本模版產生的中文版證明書未經授權。歷史討論見[Issue #30：學位考試合格證明書與成大學校學位考試系統中列印的證明書並不相符](https://github.com/wengan-li/ncku-thesis-template-latex/issues/30)。

現行使用原則：

1. 中文版學位考試論文證明書應優先使用學位考試系統產出的正式版本，並以當年度學校及系所規定為準。
2. 本模版產生的證明書只供legacy／example及版面預覽，不代表正式文件或現行授權。
3. 英文版證明書的要求可能由系所另行規定；使用前須向系所確認版本、文字及簽名需求。
4. 口試、簽名或提交前如有任何疑問，應先取得當期官方系統版本，不要只依賴本模版產生的證明書。

延伸政策紀錄：[發行、證明書與浮水印政策](docs/features/release-and-distribution.md)。

## 文件與專案工作

如果你只需要撰寫論文，請由套件內README及configuration guide開始。本專案的architecture、validation、release及Overleaf evidence記錄於[`docs/README.md`](docs/README.md)。完整儲存庫使用[`just`](https://just.systems/)統一專案commands；學生套件不依賴`just`。

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
