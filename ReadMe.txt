(this text file is encoded in UTF8)
v2.02 (Sep. 12, 2012)
** 包含了哪些檔？

這個「論文格式檔」其實包含了不只一個檔案，有下列 20 個檔案，再加上此篇 ReadMe.txt 文字檔：
my_ackn.tex
my_appendix.tex
my_bib.bib
my_cabstract.tex
my_chapters.tex
my_eabstract.tex
my_headerfooter.tex
my_names.tex
my_symbols.tex
my_vita.tex
my_watermark.jpg
my_watermark.xbb
yzu_backpages.tex
yzu_chnum.tex
yzu_coverbridge.tex
yzu_definitions.tex
yzu_frontpages.tex
yzu_report.cls
yzu_thesis.tex
yzu_watermark.tex

以上這些檔案請勿更改檔名。

以 yzu_ 為首的幾個檔案內容不需因人修改，除非校方的格式有所變動。
以 my_ 為首的幾個檔案內容則一定要依個人的情況加以修改撰寫：
	my_ackn.tex 的內容會出現在「誌謝」頁裡，不必含標題；
	my_appendix.tex 的內容會出現在「附錄」；如有多個附錄請都在此檔內繕寫，並以所附的編排碼作為每個附錄的起頭；
	my_bib.bib 是參考文獻的 BibTeX 資料庫。所有會引用到的文獻都請放入此檔；格式可以參考所附的範例，或以另外的工具程式管理，如 EndNote、BibDesk (免費，Mac OS X)、JabRef (Java, 跨平台 MS Windows, Mac OS X, Linux)；
	my_cabstract.tex 的內容會出現在「中文摘要」頁裡的摘要內容，不必含其他標題、姓名等制式格式；
	my_chapters.tex 裡指定了你的各章節的 tex 檔的檔名；
	my_eabstract.tex 的內容會出現在「英文摘要」頁裡的摘要內容，不必含其他標題、姓名等制式格式；
	my_headerfooter.tex 如果校方格式要求頁楣 (header)(如，章名戳記)以及頁碼以外的 footer (如日期)，則請在此檔內依所附範例 (檔內之註解) 修改。因為元智大學無此規定，所以檔內內容是以註解符號關閉的。
	my_names.tex 裡定義了你的姓名、論文題目、指導教授姓名、系所名、學位名等個人資料；
	my_symbols.tex 的內容會出現在「符號說明」頁；請依所附範例格式繕寫；
	my_vita.tex 的內容會出現在「自傳」頁裡，不必含標題；
	my_watermark.jpg  如果校方規定需要在內文裡加上浮水印，則請將所需的圖檔命名為 my_watermark，副檔名則不一定非得是 .jpg 不可，視圖檔格式而定，程式會自動取得；
	my_watermark.xbb  前述浮水印圖檔的 boundary box 定義檔；由系統的工具程式 ebb 產生；只有在 latex+divpdfmx 工作流程時，對於非 .eps 的圖檔才需要；所附的此檔只能配合所附的元智浮水印圖檔；詳情請看下面關於「工作流程」的介紹。

至於以 example_ 為首的幾個檔案，則是用來做示範用的，看完後可以丟棄:
	example_body.tex  示範論文的章節內容
	example_fig.png  示範論文所用的圖檔 (彩色元智校徽)
	example_fig.xbb  示範論文 png 圖檔在 latex+dvipdfmx 工作流程時所需的原圖尺寸檔
	example_prog_list.m  示範論文所用的 MATLAB 的程式列表用的文字檔
	example_thesis.pdf  所產生的論文 pdf (用 latex+dvipdfmx), 檔名已經從 yzu_thesis.pdf 改為 example_thesis.pdf，以防止再編譯 example 時被覆寫。
	example_coverbridge.pdf 是由獨立的 yzu_coverbridge.tex 所產生的論文書背列印檔。檔名已經從 yzu_coverbridge.pdf 改為 example_coverbridge.pdf，以防止再編譯時被覆寫。
	npc_macros_20120703.tex 裏頭定義了幾個方便插圖的指令，在 my_chapters.tex 裏載入。詳細用法可以看 example_thesis.pdf 裏第二章。可以搭配 my_fig_template 資料夾裏的模板使用。
	
這些格式檔案，要與 LaTeX 系統以及 CJK macro 配合使用。可以參考李果正先生寫的《大家來學 LaTeX》以及《我的 CJK》來進行 LaTeX 系統以及 CJK macro 的裝設。
<http://idv.sinica.edu.tw/jwang/SNGP/%A4%A4%A4%E5LaTeX/LaTeX123/>
http://hyperrate.com/thread.php?tid=22662


** 需要哪些 LaTeX 套件？

假設使用者的 LaTeX 系統安裝了下列這些套件： (TeXLive 這些都有安裝)
CJKutf8 (中文處理)
CJKnumb (中文章別)
geometry (頁面邊界設定)
graphicx (處理插圖)
fancyhdr (處理頁楣、頁碼，以及浮水印)
cite (處理參考文獻號碼之格式)
amsmath (進階數學方程式；可略)
amssymb (進階數學符號；可略)
listings (程式列表；可略)
url (方便寫出網址；可略)
mathrsfs (特殊草寫風格之數學符號，目前只在 my_symbols.tex 裏的範例有使用到；可略)
CJKfntef (中文加底線、波浪線做為私名號、書名號；可略)


** 如果用的不是 CJK 套件

如果你的 LaTeX 系統的中文處理能力是由其他方式達成的，則需要修改的是 yzu_thesis.tex 檔案裡標記有 %%% ZZZ %%% 的這幾行：
\usepackage{CJKutf8}
\usepackage{CJKnumb}
\usepackage{CJKspace}
\usepackage{CJKfntef}
\begin{CJK*}{UTF8}{bsmi}
\CJKindent
\end{CJK*}

對於許多人使用的 cwTeX, 請另外注意下列事項：
* 由於大家常用的 WinEdit 編輯器目前不支援 unicode 編碼，所以請用此格式檔檔案夾裡另附的 Big5 編碼的各檔；
* 每個 .tex 檔請轉存成 .ctx 檔 (詳見 cwTeX 手冊)
* 在轉存後的 yzu_thesis.ctx, my_chapters.ctx, yzu_frontpages.ctx, yzu_backpages.ctx 裡用到 \input{} 指令的地方，把副檔名去掉或改成 ctx

這裡假設你已經把 LaTeX 以及其中文套件裝設好了。


** 安裝格式檔

在 TeXLive 所安裝的 LaTeX 系統，不必把 yzu_report.cls 裝到某個 [texmf] 地方，只要與所有這些格式檔放在一起即可。

如果不是 TeXLive 所安裝的，在使用格式檔寫論文之前，須先把 yzu_report.cls 裝在你的 LaTeX 系統裡。這些個人裝設的額外檔案，一般是放在 [texmf]/tex/latex/ 這裡。
(這裡，[texmf] 代表你的 TeX 系統的 texmf 檔案路徑。以 Mac OS X 裡 Gerben Wierda 的 teTeX 系統為例，個人可以動用的 [texmf] 是 
/usr/local/teTeX/share/texmf.local/ 
以及 
~/Library/texmf/ 
後者有較高的優先次序，但無法與系統裡的其他使用者共用)
裝好後，請記得在終端機程式裡執行 sudo texhash 來更新 tex 的紀錄。


** 使用方式

yzu_thesis.tex 是主檔，以 latex 或 pdflatex 排版時請以此檔為輸入，其他檔案會自動被載入。如果有參考文獻的資料需編入，則在排版一次後，以 bibtex 對 yzu_thesis 執行一次，再排版。對於文內的圖表公式等編號的交互參考，則再排版兩次可得正確編號。所以，對於論文裏有文內的圖表公式等編號的交互參考，又有參考文獻的這種情況，最完整的作法是
latex yzu_thesis
bibtex yzu_thesis
latex yzu_thesis
latex yzu_thesis
dvipdfmx yzu_thesis

或者

pdflatex yzu_thesis
bibtex yzu_thesis
pdflatex yzu_thesis
pdflatex yzu_thesis

字體名稱在各系統裡的命名方式可能會不同，請更改 yzu_thesis.tex 檔案裡這行
\begin{CJK}{UTF8}{bsmi}
bsmi 改成適當的字體名稱，如「bkai」、「cwkai」。

此格式檔內的中文是以 unicode UTF8 編碼的。如果你的 LaTeX 中文套件必須用其他的編碼，如 Big5，則只需把格式檔用該編碼重新存一份，或用工具程式，把這些文字檔轉碼，就可以了。然後，請更改 yzu_thesis.tex 檔案裡這行
\begin{CJK}{UTF8}{bsmi}
把 UTF8 改成新的編碼名，如 Bg5。

關於 LaTeX 的一般用法，請參考李果正先生所寫的《大家來學 LaTeX》
<http://idv.sinica.edu.tw/jwang/SNGP/%A4%A4%A4%E5LaTeX/LaTeX123/>


** 元智大學的論文格式

關於元智大學的論文格式，可以在「元智教務處 > 學生專區 > 畢業/離校 > 學位論文格式規範」這網頁找到
<http://www.yzu.edu.tw/admin/aa/>
另有新的相關規定 (4/2006)，在「元智大學電子學位論文服務」網頁這裡
<http://etds.yzu.edu.tw/main/index>
是關於「電子檔規格說明」、「電子檔轉檔說明」、「電子檔上傳說明」。


** 浮水印

元智大學論文格式規範指定從書名頁開始要加上浮水印 (4/2006 新規範)；不過，其他有些學校沒有浮水印的要求，於是此一功能是可以關掉的 (在 yzu_thesis.tex 裡把 \input{yzu_watermark.tex} 這行以百分號關掉即可)。此一功能是借用加強型 header、footer 的套件 fancyhdr，佔用其中間 header 來擺放浮水印。在預設的情況下，是全篇加浮水印 (除封面以外)。如果要在單一頁加入浮水印，則在 yzu_watermark.tex 裡把全篇浮水印的程式碼關掉後 (詳見下一段)，依欲加浮水印該頁屬性，在該頁處使用下列之一的命令:
* 普通頁命令 (保留原頁面的 header、footer 設定): \thispagestyle{WaterMarkPage}
* plain 頁命令 (只保留 footer 頁碼，適合「章」層級的第一頁，以及「摘要」、目錄、參考文獻): \thispagestyle{PlainWaterMarkPage}
* empty 頁命令 (沒有頁碼，適合封面與書名頁): \thispagestyle{EmptyWaterMarkPage}

如果要關掉全篇加浮水印的功能，但保留少數頁自行加浮水印之功能，則請在 yzu_watermark.tex 這個檔案裡，把
%% >>> 全篇浮水印
%% <<< 全篇浮水印
之間的程式行首加上百分號，就可以了。

如果要加的是其他學校的浮水印，只要把校方提供的浮水印圖檔，改名為 my_watermark.xxx，這裡副檔名 .xxx 視實際圖檔格式而定，有可能是 .eps，.jpg，.png，.pdf 等各種 latex 或 pdftex 認得懂的格式。視你的工作流程 (pdftex 或 latex+dvipdfmx)，有可能需對此圖檔做前置作業。請參考下面的解釋。目前設定是在版面中間以寬度為 5.1 cm 加上浮水印的圖。


** 該用 pdflatex 還是 latex+dvipdfmx?

該用 pdflatex 還是 latex+dvipdfmx? 後者在內嵌字型時，使用較新的技術 (CID)，所以產生的 pdf 檔案較小，而且裡面的中文是可以拷貝出來、檢索的；不過，它在第一階段由 latex 編譯時，縱然由插圖套件 graphicx 加持，仍會遭遇到不識較近代的圖檔格式的圖的尺寸問題，如 jpg, png, pdf 等格式，必須先由一個叫 ebb 的小工具程式，在終端機程式裡先替這些圖檔程式產生 boundary box 的 .xbb 檔案。至於 pdflatex，不會做 CID 的中文內嵌，而是用傳統的 subfont 的方式，配合 CJKutf8 套件  (TeXLive 2009 或以後的版本)，即可避免無法拷貝、檢索裡面的中文 (成為亂碼) 的問題；而且，上述的圖檔則不需用 ebb 做前置處理，直接搞定，但反而對於較傳統的 .eps 檔需要先轉檔成 .pdf 或 .mps 的格式 。
請參考這個網頁
<http://www.2pi.info/latex/Includingeps.html>
(據說 TeXLive 2012 版本已解決這個問題)

在編寫如論文這樣的大型文件，用 latex+dvipdfmx 會較有效率。如前面所述，要取得完整正確的內文交互參考編號與文獻編號，要編譯好幾次。pdflatex 每次編譯都要花時間從字型檔取得字型資料嵌入產生的 pdf 檔中，前幾次編譯時，這些嵌入字型資料的動作都是浪費時間；相反的，latex+dvipdfmx 只有在最後一步驟 dvipdfmx 才會做嵌入字型資料的動作，省了不少時間。


** 其他 header, footer 的範例

其他學校有 header、footer 的不同要求 (例如加有「章」戳記、有畫分隔線的 header，加有「日期」的 footer)，可以用 fancyhdr 套件的現有功能，在 my_headerfooter.tex 裡加以定義。目前在 my_headerfooter.tex 檔案裡，列有範例，可以參考定義的方式。不過，因為浮水印會佔用中間的 header，所以只能用左、右 header。


** 封面所需的書背

獨立的書背列印檔 yzu_coverbridge.tex，直接由 my_names.tex 的資料合成出所需的書背，方便印刷店家製作書背。遵循元智大學論文格式的附件 18。此檔與 yzu_thesis.tex 無關。要使用時，直接以 pdflatex 或 latex + dvipdfmx 編譯此檔即可，不需修改任何地方。使用了 LaTeX CJK 的中文直排的功能。如果使用 latex + dvipdfmx 工作流程，要特別使用 -l 來指定 landscape 排版，亦即 dvipdfmx -l yzu_coverbridge.dvi。由於中文字直排的字型資料較缺乏製作資訊，建議只使用有 CJK 套件原裝資料的 bkai (楷體) 或 bsmi (明體)。


** 修改格式配合其他學校規定

yzu_thesis.tex 裏面可能要改的是頁面四邊的留白: tmargin, bmargin, lmargin, rmargin; 行距，段落之間的間隔，全篇預設的中文字體，完全關掉浮水印，完全關掉中文數字的章別。

yzu_frontpages.tex 關於封面、書名頁、中文摘要、英文摘要、誌謝、目錄、表目錄、圖目錄、符號說明
等頁之格式。

yzu_backpages.tex 關於參考文獻所使用的格式 (預設是 IEEEtran.bst)，以及附錄、自傳頁面的格式。

yzu_watermark.tex 浮水印圖檔呈現的大小、位置如有不同，要修改此檔。如果只有少數幾頁需要浮水印，則把此檔內特定幾行關閉即可，位於 
%% >>> 全篇浮水印
與
%% <<< 全篇浮水印
之間。請看檔內註解說明。

yzu_definitions.tex 如果對於 LaTeX 使用的特定名詞 (Figure, Table, Chapter, References) 的中文對應詞 (圖，表，第 x 章) 有所不同，則修改此檔內的設定。

yzu_chnum.tex 中文數字的章別，如何呈現在目錄裏，可能有不同的作法。可以參考檔內的註解加以修改。




** Version History:
* v2.02 (9/12/2012)
 - 上傳電子論文時，要把摘要、目錄、文獻列表的文字貼入網頁輸入。以 pdflatex 工作流程產生的 PDF 檔，常有亂碼產生，如，英文左引號, ff, fi, fl 等 ligature 特殊 LaTeX 字元 (非 ASCII)。在 preamble 引入 cmap 套件，可以解決這個問題。至於拷貝出來的中文字為亂碼，在 CJKutf8 套件加持下，目前內建的 bsmi (細明體)，bkai (標楷體) 沒有亂碼的問題；至於其他字型 (如 cw 系列)，則還在研究中。修改了 yzu_thesis.tex。
 - 如果文稿內有手動鍵入的換行鍵做為斷行 (通常從別的文書處理器複製貼入時會如此)，LaTeX 會把它換成空白，除非是連續兩個換行鍵才代表換段。中文字之間可能因此出現不該有的空白。使用 LaTeX CJK 特有的 CJKspace 套件與 CJK* 環境，可以消除這種空白。修改了 yzu_thesis.tex。
 - 範例裡示範了程式碼列表加註行號、列表編號、列表目錄。修改了 yzu_definitions.tex, yzu_frontpages.tex, my_appendix.tex, example_body.tex。
 - 附錄的編號，使用中文甲、乙、丙...在編圖目錄、表目錄、列表目錄時會出問題。把 v2.0 時加入的這項功能取消。修改了 my_appendix.tex。
 - 增加配合 excel2latex (EXCEL 巨集) 產生的表格碼所需的 booktabs, multirow 與 bigstrut 套件。修改了 yzu_thesis.tex, example_body.tex。
 - 增加改變字體顏色的套件 color, xcolor。修改 yzu_thesis.tex。
 - 配合 npc_macros_20120912.tex 指令的改版，修改了範例說明。修改了 example_body.tex。
 - my_names.tex 裏面的系所預設值從「光電工程學系」改為「光電工程研究所」。
 - 頁面標題「符號說明」改為「名詞與符號說明」以因應大多數同學的狀況。修改了 yzu_definitions.tex。
 - 修改書背列印，增加封面一起印，在印刷店裡較實用。修改了 yzu_coverbridge.tex。
 - 簡化封面、書名頁、中文摘要、英文摘要人名對齊的指令。修改了 yzu_frontpages.tex。

* v2.01 (7/3/2012)
 - 由 \chapter{} 產生的第X章，X前後一定有空白。如果X是中文數字一、二、三時，則這些空白很突兀。現在從 yzu_report.cls 核心裏拿掉這些空白。而是在 yzu_definitions.tex 裏預設「第 」與「 章」。但是，在 yzu_chnum.tex 裏選擇了中文顯示的章別，則仍可以把在 yzu_chnum.tex 那裏把空白拿掉而設成「第」與「章」。修改了 yzu_report.cls, yzu_definitions.tex, yzu_chnum.tex。
 - 把預設的 BibTeX 格式檔 ieeetr.bst 改成較新的 IEEEtran.bst。修改了 yzu_backpages.tex。
 - 加入 CJKfntef 套件以便加私名號 \CJKunderline{}、書名號 \CJKunderwave{}。修改了 yzu_thesis.tex, my_ackn.tex (示範用法)。
 - yzu_coverbridge.tex 畢業級別的三位數，中線對得較準了。更改了 yzu_coverbridge.tex。
 - (bug fixed) yzu_thesis.tex 裏面在 v2.0 時 graphicx 套件啟用時，latex+dvipdfm 流程使用 dvipdfm，應該是 dvipdfmx。另外，可能是因為 TeXLive2007 hyperref 裏的客製 graphicx / dvipdfmx 的設定檔不夠新，導致在 hyperref 套件的影響下，圖檔的辨識力退化。所做的權宜措施，是明確的列出可以處理的圖檔的副檔名。其中，應該使用的是 .xbb，而不是 .bb。已修正。更改了 yzu_thesis.tex，以及增加了 example_fig.xbb，my_watermark.xbb。
 - 在 example_body.tex 裏增加了許多範例，搭配 npc_macors_20120703.tex 裏定義的插圖指令，以及 my_fig_templates 資料夾裏搭配這些指令的模板，可以很方便的使用。修改了 example_body.tex, my_bib.bib, my_chapters.tex。

* v2.0 (4/5/2009)
 - 利用 LaTeX-CJK 套件 4.7 版的新功能，CJK 套件載入的是 CJKutf8。這可以讓 pdflatex 工作流程也可以產生可搜尋、拷貝的中文字串的 PDF 檔。為了解決在第二輪編譯時，toc 部份會出問題，在最後 \end{CJK}之前，加入 \clearpage。這是參考了 LaTeX-CJK 套件裏的說明文件 CJK.txt。修改了 yzu_thesis.tex。
 - 章名裏的章別，可以用中文數字，例如「第一章」。元智大學論文規範，從以前就是這樣規定。但是過去幾版的 yzu_thesis template, 並沒有找到方法做如此的排版。現在剛好有成大的詹魁元教授詢問，就一勞永逸，把它做出來了。修改了 yzu_report.cls, yzu_thesis.tex。目錄裏的呈現，可以是底下的各種組合
	1  簡介 ............................ 1
	一、簡介 ............................ 1
	第一章　簡介 ......................... 1
	第一章、簡介 ......................... 1
使用上很有彈性。相關設定在 yzu_chnum.tex 裏。
 - 把原本在 yzu_thesis.tex 裏關於各個排版相關的內定字詞 (Figure, Table, Chapter) 等的中文對應，移至 yzu_definitions.tex 裏。
 - 加入 hyperref 套件，可以產生具有超連結 (由目錄跳至特定章節) 之 pdf 檔。TeX 系統版本要求至少是 TeXLive2008。更改了 yzu_thesis.tex, yzu_frontpages.tex, yzu_backpages.tex, my_appendix.tex。
 - yzu_coverbridge.tex 畢業級別的兩位數，中線對得較準了。更改了 yzu_coverbridge.tex。
 - 同步釋出 LyX 可以用的格式檔。LyX 版本要求至少是 v1.6.2。 


* v1.7 (7/26/2007)
 - yzu_template.tex 改名為 yzu_thesis.tex
 - 配合校方規範，在英文摘要裏系名之前加入「Submitted to」字句，並在系名與校名之間，要安插院名。修改了 yzu_frontpages.tex。
 - 把中、英文摘要上方之論文題目字體改為相當於 14 pt 的大小，並把題目、姓名、系所名之文字塊間距稍微縮小。修改了 yzu_frontpages.tex。
 - 配合校方規範，在封面除了年份，再加上月份。修改了 yzu_frontpages.tex。
 - 增加預先載入的套件: url。修改了 yzu_thesis.tex, example_body.tex。
 - verbatim 套件對於長的程式行無法斷行，常會衝到右邊界外。改用 listings 套件。修改了 yzu_thesis.tex, my_appendix.tex。
 - 修正內部變數名之錯別字: \nameInnerCovver 改為 \nameInnerCover。修改了 yzu_thesis.tex, yzu_frontpages.tex。
 - 獨立的書背列印檔 yzu_coverbridge.tex 透過 my_names.tex 的資料合成出所需的書背，其畢業級別不再用畢業年份計算，而是直接在 my_names.tex 裏指定，以增加使用上的彈性。恢復西元年份以字串儲存。修改了 yzu_frontpages.tex, my_names.tex, yzu_coverbridge.tex。
 - 獨立的書背列印檔，改正了直排中文論文篇名與校名系所名之基準線與其他部分 (論文種類、姓名) 基準線有些微差距 (原因不明，但與選用的字體有關)，使得論文篇名與校所名會偏左。目前的修正是針對 bkai 這套楷體與 bsmi 這套明體。修改了 yzu_coverbridge.tex。
 - 以下未納入正式釋出的 v1.7
   X 修改 yzu_thesis.tex, 配合 XeTeX / XeLaTeX 的工作流程，把載入 graphicx 套件的條件判斷式加以修改。暫時命名為 yzu_template_xetex.tex
   X 利用 LaTeX-CJK 套件 4.7 版的新功能，CJK 套件載入的是 CJKutf8。這可以讓 pdflatex 工作流程也可以產生可搜尋、拷貝的中文字串的 PDF 檔。修改了 yzu_thesis.tex (在第二輪編譯時，toc 部份會出問題。)改回繼續使用 \usepackage{CJK}

* v1.6 (7/24/2006):
 - 修改 yzu_template.tex，使之可以無誤的自動判斷是 pdftex 還是 latex+dvipdfmx 的工作流程，而給 graphix 套件適當的引數。在格式檔 v1.2 版時使用 \pdftexversion 有否定義來推測編譯時是用何種流程；這種方式在新版的 TeXLive 則會失去效用，因為它是由單一程式 pdflatex 來處理 dvi 或 pdf 輸出，該變數一定會有定義。改由 \pdfoutput 變數定義來判定是 pdflatex 還是 pdflatex -output-format=dvi 模式。參考自 <http://www.tex.ac.uk/cgi-bin/texfaq2html?label=ifpdf>
 - 修改 yzu_frontpages.tex。對於多位指導教授之名字排列時，行距過寬、佔據版面的問題，作了調整。
 - 修改 yzu_frontpages.tex。對於多於一行的論文題目，行距過寬、佔據版面的問題，作了調整。
 - 修改 yzu_frontpages.tex。如果指導教授少於三位，則會把版面空間省下來；有較多的版面容納摘要內容。
 - 修改 yzu_frontpages.tex。對於封面、書名頁、摘要頁裡各項之間的留白，作細微調整。
 - 修改 yzu_frontpages.tex。將封面「研究生、指導教授姓名」的字體加大。
 - 修改 yzu_frontpages.tex，my_names.tex。將書名頁裡系所名稱，不再一律以「Institute of ...」起頭，以因應不同系所之需求。把系所全名之掌控，放在 my_names.tex。
 - 修改 yzu_frontpages.tex，my_names.tex。將書名頁裡系所名稱，多加一行學院名稱 (英文).
 - 修改 yzu_frontpages.tex。將書名頁裡學位所屬領域 (系所短名) 表示出來。
 - 把 yzu_template.tex 裡關於額外 header、footer 之部份，抽離出來放在獨立的檔案 my_headerfooter.tex。讓 yzu_template.tex 裡簡潔一些。
 - 增加獨立的書背列印檔 yzu_coverbridge.tex。直接由 my_names.tex 的資料合成出所需的書背。此檔與論文寫作 yzu_template.tex 無關。
 - 修改 yzu_frontpages.tex，my_names.tex。將西元年份改以 counter (整數變數) 儲存，而非字串 (command)。方便讓另外獨立的書背列印檔 yzu_coverbridge.tex 共用 my_names.tex 的資料。
 - 修改 yzu_template.tex, yzu_frontpages.tex, yzu_backpages.tex。對於用之於論文固定的各部分之中文名的定義 (出現於目錄)，集中於 yzu_template.tex 裡。
 
* v1.5: (4/25/2006)
 - 前一版的書名頁裡英文區把元智大學的所在地 hard coded 在 yzu_frontpages.tex 裡了。現在把它抽離出來，像其他項目一樣，放在 my_names.tex 裡定義。
 - 把 yzu_template.tex 裡關於浮水印之部份，抽離出來放在獨立的檔案 yzu_watermark.tex。讓 yzu_template.tex 裡簡潔一些。
 - watermark is off by default (for draft work flow); but can be turned on easily
 - 更改 yzu_frontpages.tex，在浮水印模式下，書名頁有浮水印。
 - 不再把浮水印大小固定為 80% 的文字區寬，而是以圖檔原尺寸為依據。元智大學所提供的浮水印為 200x200 像素，依據校方範例裡 MS WORD 的浮水印加入說明，以 100 dpi 插圖為本而得大小約為 5.1 cm x 5.1 cm。所以依此設定。(修改了 yzu_watermark.tex)
 - 微調了浮水印擺放的座標，使之配合元智大學規格之左寬右窄的 margin，而能擺放在可印區的中間 (水平、垂直)。(修改了 yzu_watermark.tex)
 - 書名頁底下英文的月份與年份之間的逗號，除去。(修改了 yzu_frontpages.tex)

* v1.4: (5/12/2005)
 - 前一版的浮水印功能只能全篇 (除封面、書名頁)，而無法在某一特定頁面加入浮水印。現在可以用 \thispagestyle{WaterMarkPage}、\thispagestyle{PlainWaterMarkPage}、\thispagestyle{EmptyWaterMarkPage} 來給特定頁面加入浮水印。(修改了 yzu_template.tex)
 - 在 yzu_template.tex 裡加入利用 fancyhdr 套件產生 header、footer 的範例。如果他校論文格式有規定，可以修改使用。(修改了 yzu_template.tex)
 
* v1.3: (4/22/2005)
 - 前一版的浮水印功能只能出現在每一章 (或參考文獻) 的第一頁，接下來的頁面不會有浮水印。原因是只設定了 plain 格式的頁面會有浮水印；而每一章 (或參考文獻) 的第一頁正是 plain 格式。
 - 在設定其他頁面 (fancy style) 有浮水印時，在目錄、表目錄、圖目錄、參考文獻等中文標題出現的頁面，由於是重新定義 latex 內設的變數值，並以 \makebox 製作出寬字距的效果，在那幾頁會有編譯錯誤。在看過 Leslie Lamport 寫的《LaTeX, a document preparation system》這本書的 p.23--24 關於 fragile command, moving argument 的討論後，瞭解了只要在出問題的 \makebox 前加上 \protect 的命令就行了。所以，浮水印功能完全 OK 了。(修改了 yzu_template.tex, yzu_frontpages.tex 以及 yzu_backpages.tex)

* v1.2: (4/21/2005)
 - 修改 yzu_template.tex，使之可以自動判斷是 pdftex 還是 latex+dvipdfmx 的工作流程，而給 graphix 套件適當的引數；
 - 加入浮水印的功能 (修改了 yzu_template.tex 以及 yzu_frontpages.tex)

* v1.1: (4/14/2005)
 - 修改 yzu_template.tex 以及 yzu_frontpages.tex，用 \makebox 來產生封面、書名頁等處寬字距的效果，而不是用 \CJKglue；減低對 CJK macros 的依賴至最小；如此，其他的 LaTeX 中文方案的使用者，也可以在最小的修改下，使用此格式檔。

* v1.0: (4/8/2005)
 - 剛完成符合元智大學論文格式規範的格式檔

陳念波
npchen at saturn.yzu.edu.tw
Apr 5, 2009