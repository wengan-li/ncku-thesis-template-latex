## Style Customization 自定成其他學校的模版

由[v1.5.0](https://github.com/wengan-li/ncku-thesis-template-latex/releases)開始, 本模版分離模版的功能和學校要求的格式或相關的設定. 以改造成可讓非國立成功大學的同學或人士都能建基於這模版以建立出自己學校所需的模版, 同時保留能使用本模版所提供的功能.

所有模版的功能都是放在`thesis/template`底下的`command`, `cover`, `fonts`和`oral`這些資料夾內. 但至於不同學校的不同設定, 則是放在`style`中. 這模版基礎的國立成功大學的設定和檔案, 都以放在`style/ncku`當中, 有需要的話請參考其檔案如何設定.

### 使用方式則為:
  1. 請先在`style`中把`ncku`複製成你學校的名字 (例如為: `UnivAbc`).
  2. 把`UnivAbc`的`ncku.tex`改成`UnivAbc.tex`
  3. 修改`thesis/template/style/style.tex`, 把`\input{./template/style/ncku/ncku}`改成`\input{./template/style/UnivAbc/UnivAbc}`
  4. 之後修改`UnivAbc.tex`以定出你所需的內容或設定.

### 有以下的功能使用:
  1. 頁面邊界
  2. `\SetUniversityName`: 設定學校名字
  3. `\SetWatermaskFigureStyle`和`\SetWatermaskTextStyle`: 自定浮水印
  4. `\UseWatermarkFigureStyle`和`\UseWatermarkTextStyle`: 設定預設浮水印的類型

至於其他的一些功能設定, 請參考[conf.tex](https://github.com/wengan-li/ncku-thesis-template-latex/blob/master/thesis/conf/conf.tex)當中提供的功能. 假如`style`和`conf.tex`當中的設定都沒法達到你所想要的功能, 即是你需要更詳細的方式的設定, 那你應該去嘗試修改在`command`當中所模版設定.

Happy hacking.
