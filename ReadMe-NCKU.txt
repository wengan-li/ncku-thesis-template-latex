%% NCKU 論文樣版是由陳念波老師的元智大學碩士論文樣板 (V.2.02) 修改而來.


建議寫作順序:
1. my_names.tex: 修改論文標題，作者姓名，指導教授，日期等資訊 (主要是用來產生 cover page 相關資訊).
   1.1: 注意如果是英文內文, 進入下面指令中的檔案: \input{ncku_definitions.tex} \input{ncku_chnum.tex}, 去修改或是註解關閉中文部分的指令.

2. my_chapters.tex: 修改 "main body 論文主體", e.g., \input{intro.tex} \input{experiment.tex} ...etc.

3. 其他 my_ 開頭的檔案需要修改 (ref. ReadMe.txt)
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

  3.1. 論文內文寫完後，就可以用 "00make-thesis.bat" 來編譯論文。如果一切順利，將可以產生 "ncku_thesis.pdf"
  
4. 如果要修改樣板，再考慮相關的 NCKU_ 開頭檔案. (一般都不用改!)