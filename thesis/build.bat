@ECHO off

rem ----------------------------------
rem Fast build the Tex files,
rem but only work when no error exist.
rem ----------------------------------

rem ----- Build thesis.tex -----
SET THESIS=thesis

xelatex -quiet -error-line=10000 -halt-on-error "%THESIS%.tex"
bibtex -quiet "%THESIS%.aux"
xelatex -quiet -error-line=10000 -halt-on-error "%THESIS%.tex"

FOR %%G IN (log, toc, aux, out, blg, bbl, loa, lof, lot) DO (
IF EXIST %THESIS%.%%G DEL /F %THESIS%.%%G
@ECHO %THESIS%.%%G
)

rem ----- Build spine.tex -----
SET SPINE=spine

xelatex -quiet "%SPINE%.tex"

FOR %%G IN (log, toc, aux, out, blg, bbl, loa, lof, lot) DO (
IF EXIST %SPINE%.%%G DEL /F %SPINE%.%%G
@ECHO %SPINE%.%%G
)
