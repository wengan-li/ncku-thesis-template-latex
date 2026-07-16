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
    pdftotext -f 1 -l 1 "{{ artifact }}" "{{ build_dir }}/thesis-cover.txt"
    ! grep -Eiq '\(Draft\)|\(初稿\)' "{{ build_dir }}/thesis-cover.txt"
    ! grep -F 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ build_dir }}/thesis.fls"
    ! grep -q 'doi:10.6844/ncku.latex.template' "{{ build_dir }}/thesis.txt"
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "{{ log }}"

# Run the required build and focused regression test gate.
test: check _test-v1-api _test-v1-project-migration _test-release-student-archive _test-diagnostics _test-engine-gate _test-set-thesis-date _test-sectioning-numbering _test-helper-values _test-float-contract _test-theorem-contract _test-theorem-style-counter _test-theorem-counter-cycle _test-custom-style _test-committee-size-policy _test-oral-default-state _test-metadata-bookmark _test-font-cjk _test-keyword-values _test-student-mode _test-draft-watermark-opt-in

# Internal compatibility gate for every explicitly declared v1 command/environment.
[private]
_test-v1-api:
    python3 scripts/test/check-v1-api.py

# Internal integration gate for an unchanged v1.8.2 student project on v2.
[private]
_test-v1-project-migration:
    python3 scripts/test/check-v1-project-migration.py
    grep -Eq '^INPUT .*/thesis/thesis\.tex$' "{{ build_dir }}/thesis.fls"
    grep -Fq 'INPUT ./conf/conf.tex' "{{ build_dir }}/thesis.fls"
    grep -Fq 'INPUT ./template/compat/v1.tex' "{{ build_dir }}/thesis.fls"
    grep -Fq 'INPUT ./template/style/base/base.tex' "{{ build_dir }}/thesis.fls"
    grep -Fq 'INPUT ./template/style/ncku/ncku.tex' "{{ build_dir }}/thesis.fls"
    grep -Eq '^Pages:[[:space:]]+271$' "{{ build_dir }}/thesis.pdfinfo"
    grep -Eq '^Page size:.*A4' "{{ build_dir }}/thesis.pdfinfo"
    grep -Fq 'National Cheng Kung University' "{{ build_dir }}/thesis-cover.txt"
    grep -Fq 'Institute of Computer Science and' "{{ build_dir }}/thesis-cover.txt"
    grep -Fq 'Advisor： Dr. A' "{{ build_dir }}/thesis-cover.txt"
    grep -Fq '31 December 2023' "{{ build_dir }}/thesis-cover.txt"
    ! grep -Eiq '\(Draft\)|\(初稿\)' "{{ build_dir }}/thesis-cover.txt"
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right|Suppressing empty link' "{{ log }}"

# Internal release gate: the student ZIP is the exact tracked thesis tree.
[private]
_test-release-student-archive:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/student-archive."*
    git archive --format=zip --prefix=ncku-thesis-template-latex/ --output="{{ build_dir }}/tests/student-archive.zip" HEAD:thesis
    scripts/release/verify-student-archive.sh "{{ build_dir }}/tests/student-archive.zip"
    cp "{{ build_dir }}/tests/student-archive.zip" "{{ build_dir }}/tests/student-archive-negative.zip"
    zip -dq "{{ build_dir }}/tests/student-archive-negative.zip" ncku-thesis-template-latex/MIGRATION-1.x-TO-2.x.md
    ! scripts/release/verify-student-archive.sh "{{ build_dir }}/tests/student-archive-negative.zip" > "{{ build_dir }}/tests/student-archive-negative.log" 2>&1
    grep -Fq 'student ZIP contents differ from the exact HEAD:thesis file list' "{{ build_dir }}/tests/student-archive-negative.log"
    grep -Fq -- '-ncku-thesis-template-latex/MIGRATION-1.x-TO-2.x.md' "{{ build_dir }}/tests/student-archive-negative.log"
    rm -f "{{ build_dir }}/tests/student-archive-negative.zip"

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
    grep -q 'NCKU-TEST-PASS: Start section helpers preserve exact references' "{{ build_dir }}/tests/sectioning-numbering.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right|Suppressing empty link' "{{ build_dir }}/tests/sectioning-numbering.log"
    grep -Eq 'newlabel\{ncku:test:chapter\}.*\{1\}\{' "{{ build_dir }}/tests/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:section\}.*\{1\.1\}\{' "{{ build_dir }}/tests/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:subsection\}.*\{1\.1\.1\}\{' "{{ build_dir }}/tests/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:subsubsection\}.*\{1\.1\.1\.1\}\{' "{{ build_dir }}/tests/sectioning-numbering.aux"
    pdftotext "{{ build_dir }}/tests/sectioning-numbering.pdf" "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Chapter Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Section Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsection Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsubsection Sentinel' "{{ build_dir }}/tests/sectioning-numbering.txt"

# Internal regression test for helper values, state isolation, and equation labels.
[private]
_test-helper-values:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=helper-values ../tests/helper-values.tex
    test "$(grep -c 'NCKU-TEST-PASS:' "{{ build_dir }}/tests/helper-values.log")" -eq 4
    ! grep -q 'NCKU-TEST-FAIL:' "{{ build_dir }}/tests/helper-values.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right' "{{ build_dir }}/tests/helper-values.log"
    pdftotext "{{ build_dir }}/tests/helper-values.pdf" "{{ build_dir }}/tests/helper-values.txt"
    grep -Fq 'Months: January, February, March, April, May, June, July, August, September, October,' "{{ build_dir }}/tests/helper-values.txt"
    grep -Fq 'November, December.' "{{ build_dir }}/tests/helper-values.txt"
    grep -Fq 'Oral year: 112.' "{{ build_dir }}/tests/helper-values.txt"
    grep -Fq 'DPS department: Department of Photonics.' "{{ build_dir }}/tests/helper-values.txt"
    grep -Fq 'Equation reference: (0.1).' "{{ build_dir }}/tests/helper-values.txt"

# Internal figure/multi-figure/table runtime and metadata contract.
[private]
_test-float-contract:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/float-contract."*
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=float-contract ../tests/float-contract.tex
    pdfinfo "{{ build_dir }}/tests/float-contract.pdf" > "{{ build_dir }}/tests/float-contract.pdfinfo"
    pdftotext -layout "{{ build_dir }}/tests/float-contract.pdf" "{{ build_dir }}/tests/float-contract.txt"
    pdfimages -list "{{ build_dir }}/tests/float-contract.pdf" > "{{ build_dir }}/tests/float-contract.images"
    python3 scripts/test/check-float-contract.py "{{ build_dir }}/tests"

# Internal runtime contract for all 21 public theorem insertion helpers.
[private]
_test-theorem-contract:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/theorem-contract."*
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=theorem-contract ../tests/theorem-contract.tex
    pdfinfo "{{ build_dir }}/tests/theorem-contract.pdf" > "{{ build_dir }}/tests/theorem-contract.pdfinfo"
    pdftotext -layout "{{ build_dir }}/tests/theorem-contract.pdf" "{{ build_dir }}/tests/theorem-contract.txt"
    python3 scripts/test/check-theorem-contract.py "{{ build_dir }}/tests"

# Internal custom theorem style/counter matrix, including chained-empty counters.
[private]
_test-theorem-style-counter:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/theorem-style-counter."*
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=theorem-style-counter ../tests/theorem-style-counter.tex
    pdfinfo "{{ build_dir }}/tests/theorem-style-counter.pdf" > "{{ build_dir }}/tests/theorem-style-counter.pdfinfo"
    pdftotext -layout "{{ build_dir }}/tests/theorem-style-counter.pdf" "{{ build_dir }}/tests/theorem-style-counter.txt"
    pdftohtml -xml -hidden -nodrm -i "{{ build_dir }}/tests/theorem-style-counter.pdf" "{{ build_dir }}/tests/theorem-style-counter"
    python3 scripts/test/check-theorem-style-counter.py "{{ build_dir }}/tests"

# Internal negative test for deterministic cyclic theorem-counter diagnostics.
[private]
_test-theorem-counter-cycle:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/theorem-counter-cycle."*
    if (cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=theorem-counter-cycle ../tests/theorem-counter-cycle.tex); then echo "theorem counter cycle unexpectedly compiled"; exit 1; fi
    grep -Fq "Cyclic theorem counter configuration" "{{ build_dir }}/tests/theorem-counter-cycle.log"
    ! grep -Fq "TeX capacity exceeded" "{{ build_dir }}/tests/theorem-counter-cycle.log"
    @echo "Theorem counter cycle PASS: deterministic package error without recursive overflow"

# Internal integration test for the neutral non-NCKU style profile.
[private]
_test-custom-style:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/custom-style."*
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=custom-style ../tests/custom-style.tex
    grep -Fq 'NCKU-TEST-CUSTOM-PROFILE: custom' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COVER-DATE: 2024-7' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-REQUESTED-DATE: 2024-7' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-ORAL-CHI-YEAR: 2023' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COMMITTEE-MIN: 2' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COMMITTEE-MAX: 9' "{{ build_dir }}/tests/custom-style.log"
    grep -Fq 'NCKU-TEST-PASS: custom style profile builds without NCKU visible policy' "{{ build_dir }}/tests/custom-style.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right' "{{ build_dir }}/tests/custom-style.log"
    ! grep -Fq 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ build_dir }}/tests/custom-style.fls"
    pdftotext "{{ build_dir }}/tests/custom-style.pdf" "{{ build_dir }}/tests/custom-style.txt"
    pdftotext -f 4 -l 4 "{{ build_dir }}/tests/custom-style.pdf" "{{ build_dir }}/tests/custom-style-master-oral.txt"
    pdftotext -f 5 -l 5 "{{ build_dir }}/tests/custom-style.pdf" "{{ build_dir }}/tests/custom-style-doctoral-oral.txt"
    pdftotext -f 6 -l 6 "{{ build_dir }}/tests/custom-style.pdf" "{{ build_dir }}/tests/custom-style-doctoral-cover.txt"
    grep -Fq 'prepared by' "{{ build_dir }}/tests/custom-style-master-oral.txt"
    grep -Eq 'Example master.s submission in Department of Testing' "{{ build_dir }}/tests/custom-style-master-oral.txt"
    grep -Fq 'prepared by' "{{ build_dir }}/tests/custom-style-doctoral-oral.txt"
    grep -Fq 'Example doctoral submission in Department of Testing' "{{ build_dir }}/tests/custom-style-doctoral-oral.txt"
    grep -Fq 'July 2024' "{{ build_dir }}/tests/custom-style-doctoral-cover.txt"
    ! grep -Fq '31 July 2024' "{{ build_dir }}/tests/custom-style-doctoral-cover.txt"
    ! grep -Fq 'December 2023' "{{ build_dir }}/tests/custom-style-doctoral-cover.txt"
    ! grep -Eq 'Master of Science|Doctor of Philosophy' "{{ build_dir }}/tests/custom-style.txt"
    pdfinfo "{{ build_dir }}/tests/custom-style.pdf" > "{{ build_dir }}/tests/custom-style.pdfinfo"
    grep -Eq '^Pages:[[:space:]]+6$' "{{ build_dir }}/tests/custom-style.pdfinfo"
    grep -Eq '^Page size:.*A4' "{{ build_dir }}/tests/custom-style.pdfinfo"
    grep -Fq 'Example University' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq 'Department of Testing' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq 'Portable Thesis Style' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq 'July 2024' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq 'Example City, Example Country' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq '31 December 2023' "{{ build_dir }}/tests/custom-style.txt"
    grep -Fq '西 元' "{{ build_dir }}/tests/custom-style.txt"
    ! grep -Fq '中華民國' "{{ build_dir }}/tests/custom-style.txt"
    ! grep -Fq 'National Cheng Kung University' "{{ build_dir }}/tests/custom-style.txt"
    ! grep -Fq '國立成功大學' "{{ build_dir }}/tests/custom-style.txt"

# Internal regression test for NCKU degree-specific committee-size policy.
[private]
_test-committee-size-policy:
    mkdir -p "{{ build_dir }}/tests"
    rm -f "{{ build_dir }}/tests/committee-size-policy."*
    cd "{{ source_dir }}" && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ build_dir }}/tests" -jobname=committee-size-policy ../tests/committee-size-policy.tex
    test "$(grep -c 'NCKU-TEST-PASS: committee request' "{{ build_dir }}/tests/committee-size-policy.log")" -eq 6
    ! grep -q 'NCKU-TEST-FAIL:' "{{ build_dir }}/tests/committee-size-policy.log"

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

# Internal integration test for the student-only dependency path.
[private]
_test-student-mode:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=student-mode ../tests/student-mode.tex
    grep -q 'NCKU-TEST-PASS: student mode compiles without teaching examples' "{{ build_dir }}/tests/student-mode.log"
    grep -q 'NCKU-TEST-PASS: default diagonal draft watermark text is empty' "{{ build_dir }}/tests/student-mode.log"
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "{{ build_dir }}/tests/student-mode.log"
    ! grep -F '/example/' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./conf/conf.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/context.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/abstract/eng.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/acknowledgments/eng.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/nomenclature/nomenclature.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/introduction/introduction.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/related-work/related-work.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/conclusion/conclusion.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'INPUT ./context/references/references.tex' "{{ build_dir }}/tests/student-mode.fls"
    grep -Fq 'Database file #1: context/references/paper.bib' "{{ build_dir }}/tests/student-mode.blg"
    grep -Fq 'Database file #2: context/references/misc.bib' "{{ build_dir }}/tests/student-mode.blg"
    grep -Fq 'Database file #3: context/references/book.bib' "{{ build_dir }}/tests/student-mode.blg"
    pdftotext -f 1 -l 1 "{{ build_dir }}/tests/student-mode.pdf" "{{ build_dir }}/tests/student-mode-cover.txt"
    ! grep -Eiq '\(Draft\)|\(初稿\)' "{{ build_dir }}/tests/student-mode-cover.txt"
    ! grep -F 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ build_dir }}/tests/student-mode.fls"

# Internal regression test proving Draft and institutional watermark remain opt-in.
[private]
_test-draft-watermark-opt-in:
    mkdir -p "{{ build_dir }}/tests"
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/tests" -jobname=draft-watermark-opt-in ../tests/draft-watermark-opt-in.tex
    grep -q 'NCKU-TEST-PASS: draft and institutional watermark remain explicit opt-ins' "{{ build_dir }}/tests/draft-watermark-opt-in.log"
    grep -q 'NCKU-TEST-PASS: diagonal draft watermark text remains an explicit opt-in' "{{ build_dir }}/tests/draft-watermark-opt-in.log"
    pdftotext -f 1 -l 1 "{{ build_dir }}/tests/draft-watermark-opt-in.pdf" "{{ build_dir }}/tests/draft-watermark-opt-in-cover.txt"
    grep -Fq '(Draft)' "{{ build_dir }}/tests/draft-watermark-opt-in-cover.txt"
    grep -Fq 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ build_dir }}/tests/draft-watermark-opt-in.fls"

# Run the complete local CI gate.
ci: test
    git diff --check

# Build and verify an Overleaf-compatible StudentMode import package from HEAD.
overleaf version="dev":
    test -z "$(git status --porcelain --untracked-files=all)" || { echo 'Overleaf packaging requires a clean Git worktree.' >&2; exit 1; }
    scripts/overleaf/package-and-verify.sh "{{ version }}" "{{ build_dir }}/overleaf" student

# Build and verify a clean public Gallery preview package from HEAD.
overleaf-gallery version="dev":
    test -z "$(git status --porcelain --untracked-files=all)" || { echo 'Overleaf Gallery packaging requires a clean Git worktree.' >&2; exit 1; }
    scripts/overleaf/package-and-verify.sh "{{ version }}" "{{ build_dir }}/overleaf" gallery

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
