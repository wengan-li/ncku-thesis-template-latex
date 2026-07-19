<!-- doc-pair: root-readme; lang: zh-Hant-TW; topics: project-overview,release-and-overleaf-status,choose-the-correct-setup,quick-start,downloads-and-examples,migrate-from-1-x,other-institution-profiles,submission-watermark-and-certificate,documentation-and-project-work,other-community-alternatives,licence -->

[繁體中文](README.md) | [English](README.en.md)

# 國立成功大學論文範本

[在Overleaf開啟範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 專案簡介

這是我以XeLaTeX維護的國立成功大學碩博士論文範本，可撰寫中文、英文或中英混合內容，並自動產生封面、目錄、圖表清單及其他前置頁面。它提供學生設定、可重用的LaTeX helpers、1.x相容層，以及讓其他學校的同學建立自己樣式的profile架構。

本專案並非國立成功大學官方軟體，也不代表學校、圖書館、學位考試系統或任何系所的現行認可。使用前必須核對當年度規定；官方規定永遠優先於本範本。

- [成大博碩士論文系統](https://thesis.lib.ncku.edu.tw/)
- [論文建檔說明](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [教務處課務組論文格式規範](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## 發行與Overleaf狀態

最新正式原始碼及學生套件由[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases/latest)提供。目前最新production release是`v2.0.1.260719010734`。V2保留完整machine-audited 1.x public API及XeLaTeX學生使用路徑，同時整理profile、相容層、測試及下載套件。

既有Overleaf Gallery頁面仍可公開使用。我已將V2上載到原本的Overleaf project並重新提交Gallery update review；在Overleaf批准並完成public read-back前，不能將「已提交」寫成「已批准」，最新V2仍以GitHub Releases為準。

## 選擇正確設定

文件語言、學校profile、封面語言、學位及內容模式是不同決定。國際學生如就讀成大仍使用`ncku` profile；其他學校的同學如要建立自己的範本，可使用`custom`或另一個institution profile。不要從讀者語言推斷學校profile。

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

V2將共用renderer、NCKU policy及其他學校port分成`base`、`ncku`及`custom`。學生論文資料仍放在`conf/conf.tex`；學校geometry、名稱、日期政策、文字及assets放在`template/style/<profile>/`。其他學校的同學可由`template/style/custom/`開始，不要直接修改共用renderer或先載入NCKU再覆寫。

## 提交、浮水印與證明書

正式輸出預設沒有封面初稿標記、斜向`DRAFT`文字或學校logo浮水印。三者是獨立的opt-in功能；不要因API存在就加入提交PDF。現行流程要求以學校系統產出的文件為準，系統亦可能在核准後的電子全文加入自己的浮水印。

學位考試合格證明書應優先使用學位考試系統產出的正式版本。本範本產生的證明書只供legacy/example及regression用途。2015／2018的歷史查核記錄不構成現時授權或官方認可。

## 文件與專案工作

如果你只需要撰寫論文，請由套件內README及configuration guide開始。我在[`docs/README.md`](docs/README.md)記錄architecture、validation、release及Overleaf evidence。完整儲存庫使用[`just`](https://just.systems/)統一專案commands；學生套件不依賴`just`。

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
