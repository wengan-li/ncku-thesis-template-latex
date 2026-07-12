# Canonical task interface for the NCKU thesis template.
# Run `just` to list available recipes.

set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

source_dir := "thesis"
build_dir := "build"
artifact := build_dir / "thesis.pdf"
synctex := build_dir / "thesis.synctex.gz"
log := build_dir / "thesis.log"

# List available recipes.
default:
    @just --list

# Build the canonical thesis project.
build: thesis

# Build the canonical thesis PDF and SyncTeX map with automatic reruns.
thesis:
    mkdir -p "{{ build_dir }}"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}" thesis.tex

# Watch thesis sources and rebuild automatically without opening another PDF viewer.
watch:
    mkdir -p "{{ build_dir }}"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}" -pvc -view=none thesis.tex

# Build the full teaching example selected by the checked-in configuration.
example: thesis

# Backward-compatible recipe name.
[private]
demo: example

# Build and verify the canonical artifacts and resolved references.
check: thesis
    test -s "{{ artifact }}"
    test -s "{{ synctex }}"
    pdfinfo "{{ artifact }}" > "{{ build_dir }}/thesis.pdfinfo"
    grep -q '^Pages:' "{{ build_dir }}/thesis.pdfinfo"
    grep -q '^Page size:.*A4' "{{ build_dir }}/thesis.pdfinfo"
    pdftotext "{{ artifact }}" "{{ build_dir }}/thesis.txt"
    ! grep -q 'doi:10.6844/ncku.latex.template' "{{ build_dir }}/thesis.txt"
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "{{ log }}"

# Run the required build and focused regression test gate.
test: check _test-diagnostics _test-engine-gate _test-set-thesis-date _test-sectioning-numbering _test-oral-default-state _test-metadata-bookmark _test-font-cjk _test-keyword-values

# Internal regression budget for final canonical-build diagnostics.
[private]
_test-diagnostics:
    python3 scripts/test/check-diagnostics.py "{{ log }}"

# Internal negative regression test for the XeLaTeX-only engine gate.
[private]
_test-engine-gate:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/engine-gate."*
    ! (cd "{{ source_dir }}" && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ build_dir }}/tests" -jobname=engine-gate ../tests/engine-gate.tex)
    grep -q '請使用XeLaTeX來產生論文' "{{ build_dir }}/tests/engine-gate.log"

# Internal regression test for the legacy cover-date command.
[private]
_test-set-thesis-date:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ build_dir }}/tests" -jobname=set-thesis-date ../tests/set-thesis-date.tex
    grep -q 'NCKU-TEST-PASS: legacy and current cover-date commands terminate safely' "{{ build_dir }}/tests/set-thesis-date.log"

# Internal regression test for starred headings and numbered references.
[private]
_test-sectioning-numbering:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=sectioning-numbering ../tests/sectioning-numbering.tex
    grep -q 'NCKU-TEST-PASS: sectioning headings and numbered references compile' "{{ build_dir }}/tests/sectioning-numbering.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right' "{{ build_dir }}/tests/sectioning-numbering.log"
    pdftotext "{{ build_dir }}/tests/sectioning-numbering.pdf" "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Chapter Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Section Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsection Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsubsection Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"

# Internal regression test for the oral-certificate default state.
[private]
_test-oral-default-state:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ build_dir }}/tests" -jobname=oral-default-state ../tests/oral-default-state.tex
    grep -q 'NCKU-TEST-PASS: oral certificate defaults to the external-image path' "{{ build_dir }}/tests/oral-default-state.log"

# Internal regression test for Unicode PDF metadata and bookmarks.
[private]
_test-metadata-bookmark:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=metadata-bookmark ../tests/metadata-bookmark.tex
    grep -q 'NCKU-TEST-PASS: Unicode metadata and bookmark strings compile cleanly' "{{ build_dir }}/tests/metadata-bookmark.log"
    ! grep -Eiq 'Token not allowed in a PDF string|already defined|destination with the same identifier' "{{ build_dir }}/tests/metadata-bookmark.log"
    pdfinfo "{{ build_dir }}/tests/metadata-bookmark.pdf" > "{{ build_dir }}/tests/metadata-bookmark.pdfinfo"
    grep -Fq 'Title:           NCKU Metadata Line (成大中繼資料標題)' "{{ build_dir }}/tests/metadata-bookmark.pdfinfo"

# Internal regression test for bundled Latin/CJK font policy.
[private]
_test-font-cjk:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=font-cjk ../tests/font-cjk.tex
    grep -q 'NCKU-TEST-PASS: bundled Latin and CJK font policies compile' "{{ build_dir }}/tests/font-cjk.log"
    ! grep -q 'Unknown CJK family' "{{ build_dir }}/tests/font-cjk.log"
    grep -Eq "Font shape .*m/sc.*undefined" "{{ build_dir }}/tests/font-cjk.log"
    pdftotext "{{ build_dir }}/tests/font-cjk.pdf" "{{ build_dir }}/tests/font-cjk.txt"
    grep -q 'Monospaced Latin and 中文等寬語境' "{{ build_dir }}/tests/font-cjk.txt"

# Internal regression test for keyword helper equivalence.
[private]
_test-keyword-values:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=keyword-values ../tests/keyword-values.tex
    test "$(grep -c 'NCKU-TEST-PASS:' "{{ build_dir }}/tests/keyword-values.log")" -eq 4
    ! grep -q 'NCKU-TEST-FAIL:' "{{ build_dir }}/tests/keyword-values.log"
    pdfinfo "{{ build_dir }}/tests/keyword-values.pdf" > "{{ build_dir }}/tests/keyword-values.pdfinfo"
    grep -Fq 'Keywords:        Alpha, Beta' "{{ build_dir }}/tests/keyword-values.pdfinfo"

# Run the complete local CI gate.
ci: test
    git diff --check

# Build and verify the complete same-source release asset set.
release version="dev": test
    test -z "$(git status --porcelain --untracked-files=all)" || { echo 'Release requires a clean Git worktree.' >&2; exit 1; }
    rm -rf "{{ build_dir }}/release"
    mkdir -p "{{ build_dir }}/release"
    cp "{{ artifact }}" "{{ build_dir }}/release/example-thesis-full.pdf"
    just _release-pdf ../scripts/release/cover.tex example-cover
    just _release-pdf ../scripts/release/thesis-chi.tex example-thesis-chi
    just _release-pdf ../scripts/release/thesis-eng.tex example-thesis-eng
    just _release-pdf ../scripts/release/defense-certificate-master.tex example-legacy-defense-certificate-master
    just _release-pdf ../scripts/release/defense-certificate-phd.tex example-legacy-defense-certificate-phd
    git archive --format=zip --prefix=ncku-thesis-template-latex/ --output="{{ build_dir }}/release/ncku-thesis-template-latex-{{ version }}.zip" HEAD:thesis
    scripts/release/package-examples.sh "{{ build_dir }}/release" "ncku-thesis-template-latex-examples-{{ version }}.zip" "{{ version }}"
    scripts/release/verify-assets.sh "{{ build_dir }}/release" "ncku-thesis-template-latex-{{ version }}.zip" "ncku-thesis-template-latex-examples-{{ version }}.zip" "{{ version }}"

# Internal helper: build one named release PDF from the thesis source directory.
[private]
_release-pdf source job:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/release" -jobname="{{ job }}" "{{ source }}"

# Remove generated LaTeX build artifacts.
clean:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}" -C thesis.tex
    rm -rf "{{ build_dir }}"
