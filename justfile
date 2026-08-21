# Canonical task interface for the NCKU thesis template.
# Run `just` to list available recipes.

set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

source_dir := "thesis"
build_dir := "build"
tests_dir := build_dir / "tests"
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

# Run the required build and focused regression test gate. Dependencies run
# concurrently ([parallel] needs just >= 1.42; CI pins 1.57): every fixture
# writes only its own build/tests/<jobname>.* files, and the two recipes that
# read the canonical build/thesis.* artifacts declare that dependency below.
# JUST_JOBS=1 restores serial execution when attributing interleaved failures.
[parallel]
test: check _test-bilingual-docs _test-test-layout _test-v1-api _test-v1-project-migration _test-release-student-archive _test-overleaf-gallery-package _test-diagnostics _test-engine-gate _test-set-thesis-date _test-sectioning-numbering _test-numbering-contract _test-numbering-family-contract _test-chapter-title-format-key-unknown _test-numbering-family-key-unknown _test-helper-values _test-deprecated-command-contract _test-float-contract _test-multi-figure-key-unknown _test-figure-key-unknown _test-table-key-unknown _test-reference-contract _test-reference-apacite-contract _test-reference-key-unknown _test-theorem-contract _test-theorem-key-unknown _test-theorem-format-key-unknown _test-theorem-style-counter _test-theorem-counter-cycle _test-custom-style _test-custom-institution-api _test-committee-size-policy _test-oral-default-state _test-metadata-bookmark _test-custom-font-files-contract _test-custom-font-files-key-unknown _test-font-option-contract _test-font-option-key-unknown _test-font-type-routing _test-font-cjk _test-keyword-values _test-student-mode _test-draft-watermark-opt-in

# Shared fixture builders. Every fixture clears its own build/tests/<job>.*
# files first so grep-count assertions never read stale state, then compiles
# ../tests/<fixture> from the source directory. Recipes keep their own
# assertion lines; only the mechanical build step is shared.

# Build one fixture with latexmk (BibTeX and reruns as needed).
[private]
_fixture-latexmk job fixture:
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/{{ job }}."*
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ tests_dir }}" -jobname={{ job }} ../tests/{{ fixture }}

# Build one fixture with a single halt-on-error XeLaTeX pass.
[private]
_fixture-xelatex job fixture *flags:
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/{{ job }}."*
    cd "{{ source_dir }}" && xelatex {{ flags }} -interaction=nonstopmode -halt-on-error -output-directory=../"{{ tests_dir }}" -jobname={{ job }} ../tests/{{ fixture }}

# Build a latexmk fixture and extract the pdfinfo/layout-text inputs that the
# fixture's Python contract checker reads.
[private]
_fixture-contract job fixture: (_fixture-latexmk job fixture)
    pdfinfo "{{ tests_dir }}/{{ job }}.pdf" > "{{ tests_dir }}/{{ job }}.pdfinfo"
    pdftotext -layout "{{ tests_dir }}/{{ job }}.pdf" "{{ tests_dir }}/{{ job }}.txt"

# Single-pass XeLaTeX variant of the contract-input builder.
[private]
_fixture-contract-xelatex job fixture: (_fixture-xelatex job fixture)
    pdfinfo "{{ tests_dir }}/{{ job }}.pdf" > "{{ tests_dir }}/{{ job }}.pdfinfo"
    pdftotext -layout "{{ tests_dir }}/{{ job }}.pdf" "{{ tests_dir }}/{{ job }}.txt"

# Structural language-pair and first-party Markdown-link gate.
[private]
_test-bilingual-docs:
    python3 scripts/test/check-bilingual-docs.py

# Flat three-digit test-source layout and reserved group ranges.
[private]
_test-test-layout:
    python3 scripts/test/check-test-layout.py

# Internal compatibility gate for every explicitly declared v1 command/environment.
[private]
_test-v1-api:
    python3 scripts/test/check-v1-api.py

# Internal integration gate for an unchanged v1.8.2 student project on v2.
[private]
_test-v1-project-migration: check
    python3 scripts/test/check-v1-project-migration.py
    test -s "{{ build_dir }}/thesis.fls"
    grep -Eq '^INPUT .*/thesis/thesis\.tex$' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./conf/conf.tex' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./template/compat/v1.tex' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./template/style/base/base.tex' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./template/style/ncku/ncku.tex' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./template/style/ncku/college.tex' "{{ build_dir }}/thesis.fls"
    grep -Fxq 'INPUT ./template/style/ncku/department.tex' "{{ build_dir }}/thesis.fls"
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
    @if [ -n "$(git status --porcelain -- thesis)" ]; then echo 'WARNING: thesis/ has uncommitted changes; this test verifies committed HEAD:thesis, not the working tree.' >&2; fi
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/student-archive."*
    git archive --format=zip --prefix=ncku-thesis-template-latex/ --output="{{ tests_dir }}/student-archive.zip" HEAD:thesis
    scripts/release/verify-student-archive.sh "{{ tests_dir }}/student-archive.zip"
    for doc in README.md conf/README.md README.en.md conf/README.en.md; do \
      cp "{{ tests_dir }}/student-archive.zip" "{{ tests_dir }}/student-archive-negative.zip"; \
      zip -dq "{{ tests_dir }}/student-archive-negative.zip" "ncku-thesis-template-latex/$doc"; \
      if scripts/release/verify-student-archive.sh "{{ tests_dir }}/student-archive-negative.zip" > "{{ tests_dir }}/student-archive-negative.log" 2>&1; then \
        echo "student-archive verification unexpectedly passed without $doc" >&2; exit 1; \
      fi; \
      grep -Fq 'student ZIP contents differ from the exact HEAD:thesis file list' "{{ tests_dir }}/student-archive-negative.log"; \
      grep -Fq -- "-ncku-thesis-template-latex/$doc" "{{ tests_dir }}/student-archive-negative.log"; \
      rm -f "{{ tests_dir }}/student-archive-negative.zip"; \
    done

# Internal regression test for the generated public Gallery package and overlay.
[private]
_test-overleaf-gallery-package:
    @if [ -n "$(git status --porcelain -- thesis)" ]; then echo 'WARNING: thesis/ has uncommitted changes; this test packages committed HEAD:thesis, not the working tree.' >&2; fi
    rm -rf "{{ tests_dir }}/overleaf-gallery"
    scripts/overleaf/package-and-verify.sh "test" "{{ tests_dir }}/overleaf-gallery" gallery

# Internal regression budget for final canonical-build diagnostics.
[private]
_test-diagnostics: thesis
    python3 scripts/test/check-diagnostics.py "{{ log }}"

# Internal negative regression test for the XeLaTeX-only engine gate.
[private]
_test-engine-gate:
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/engine-gate."*
    ! (cd "{{ source_dir }}" && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ tests_dir }}" -jobname=engine-gate ../tests/110-engine-gate.tex)
    grep -q '請使用XeLaTeX來產生論文' "{{ tests_dir }}/engine-gate.log"

# Internal regression test for the legacy cover-date command.
[private]
_test-set-thesis-date: (_fixture-xelatex "set-thesis-date" "120-set-thesis-date.tex")
    grep -q 'NCKU-TEST-PASS: legacy and current cover-date commands terminate safely' "{{ tests_dir }}/set-thesis-date.log"

# Internal regression test for starred headings and numbered references.
[private]
_test-sectioning-numbering: (_fixture-latexmk "sectioning-numbering" "121-sectioning-numbering.tex")
    grep -q 'NCKU-TEST-PASS: Start section helpers preserve exact references' "{{ tests_dir }}/sectioning-numbering.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right|Suppressing empty link' "{{ tests_dir }}/sectioning-numbering.log"
    grep -Eq 'newlabel\{ncku:test:chapter\}.*\{1\}\{' "{{ tests_dir }}/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:section\}.*\{1\.1\}\{' "{{ tests_dir }}/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:subsection\}.*\{1\.1\.1\}\{' "{{ tests_dir }}/sectioning-numbering.aux"
    grep -Eq 'newlabel\{ncku:test:subsubsection\}.*\{1\.1\.1\.1\}\{' "{{ tests_dir }}/sectioning-numbering.aux"
    pdftotext "{{ tests_dir }}/sectioning-numbering.pdf" "{{ tests_dir }}/sectioning-numbering.txt"
    grep -q 'NCKU Star Chapter Sentinel' "{{ tests_dir }}/sectioning-numbering.txt"
    grep -q 'NCKU Star Section Sentinel' "{{ tests_dir }}/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsection Sentinel' "{{ tests_dir }}/sectioning-numbering.txt"
    grep -q 'NCKU Star Subsubsection Sentinel' "{{ tests_dir }}/sectioning-numbering.txt"

# Internal general/appendix numbering state and repeatability contract.
[private]
_test-numbering-contract: (_fixture-contract "numbering-contract" "200-numbering-contract.tex")
    python3 scripts/test/check-numbering-contract.py "{{ tests_dir }}"

# Expanded/reset/omitted parser-state contract for nine numbering families.
[private]
_test-numbering-family-contract: (_fixture-xelatex "numbering-family-contract" "201-numbering-family-contract.tex")
    python3 scripts/test/check-numbering-family-contract.py "{{ tests_dir }}"

# Shared negative gate: an unknown key in the fixture must abort the XeLaTeX
# run with the parser's deterministic `unsupported` diagnostic.
[private]
_expect-unknown-key job fixture label:
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/{{ job }}."*
    if (cd "{{ source_dir }}" && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../"{{ tests_dir }}" -jobname={{ job }} ../tests/{{ fixture }}); then echo "unknown {{ label }} key unexpectedly compiled"; exit 1; fi
    grep -Fq 'unsupported' "{{ tests_dir }}/{{ job }}.log"
    ! grep -Fq 'NCKU-TEST-FAIL' "{{ tests_dir }}/{{ job }}.log"
    @echo "{{ label }} key unknown-option PASS: deterministic hard error"

# Unknown Chapter title-format keys remain deterministic hard errors.
[private]
_test-chapter-title-format-key-unknown: (_expect-unknown-key "chapter-title-format-key-unknown" "203-chapter-title-format-key-unknown.tex" "Chapter title-format")

# Unknown keys in all remaining numbering families remain hard errors.
[private]
_test-numbering-family-key-unknown:
    python3 scripts/test/check-numbering-family-unknown.py "{{ tests_dir }}"

# Internal regression test for helper values, state isolation, and equation labels.
[private]
_test-helper-values: (_fixture-latexmk "helper-values" "130-helper-values.tex")
    test "$(grep -c 'NCKU-TEST-PASS:' "{{ tests_dir }}/helper-values.log")" -eq 7
    ! grep -q 'NCKU-TEST-FAIL:' "{{ tests_dir }}/helper-values.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right' "{{ tests_dir }}/helper-values.log"
    pdftotext "{{ tests_dir }}/helper-values.pdf" "{{ tests_dir }}/helper-values.txt"
    grep -Fq 'Months: January, February, March, April, May, June, July, August, September, October,' "{{ tests_dir }}/helper-values.txt"
    grep -Fq 'November, December.' "{{ tests_dir }}/helper-values.txt"
    grep -Fq 'Oral year: 112.' "{{ tests_dir }}/helper-values.txt"
    grep -Fq 'DPS department: Department of Photonics.' "{{ tests_dir }}/helper-values.txt"
    grep -Fq 'Equation reference: (0.1).' "{{ tests_dir }}/helper-values.txt"

# Internal runtime contract for all v1 deprecated public-command tombstones.
[private]
_test-deprecated-command-contract: (_fixture-xelatex "deprecated-command-contract" "131-deprecated-command-contract.tex")
    test "$(grep -c 'NCKU-DEPRECATED-ERROR-PASS:' "{{ tests_dir }}/deprecated-command-contract.log")" -eq 23
    test "$(grep -c 'NCKU-DEPRECATED-STOP-PASS:' "{{ tests_dir }}/deprecated-command-contract.log")" -eq 23
    grep -Fq 'NCKU-TEST-PASS: deprecated command contract' "{{ tests_dir }}/deprecated-command-contract.log"
    python3 scripts/test/check-deprecated-command-contract.py

# Internal figure/multi-figure/table runtime and metadata contract.
[private]
_test-float-contract: (_fixture-contract "float-contract" "400-float-contract.tex")
    pdfimages -list "{{ tests_dir }}/float-contract.pdf" > "{{ tests_dir }}/float-contract.images"
    python3 scripts/test/check-float-contract.py "{{ tests_dir }}"

# Unknown top-level and nested multi-figure keys remain hard errors.
[private]
_test-multi-figure-key-unknown:
    python3 scripts/test/check-multi-figure-key-unknown.py "{{ tests_dir }}"

# Unknown single-figure keys must remain deterministic hard errors.
[private]
_test-figure-key-unknown: (_expect-unknown-key "figure-key-unknown" "401-figure-key-unknown.tex" "Figure")

# Unknown single-table keys must remain deterministic hard errors.
[private]
_test-table-key-unknown: (_expect-unknown-key "table-key-unknown" "403-table-key-unknown.tex" "Table")

# Internal SetupReference parser and rendered BibTeX contract.
[private]
_test-reference-contract: (_fixture-contract "reference-contract" "300-reference-contract.tex")
    python3 scripts/test/check-reference-contract.py "{{ tests_dir }}"

# SetupReference apacite route must retain its preamble package side effect.
[private]
_test-reference-apacite-contract: (_fixture-xelatex "reference-apacite-contract" "301-reference-apacite-contract.tex")
    grep -Fq 'NCKU-REFERENCE-APACITE-LOADED: yes' "{{ tests_dir }}/reference-apacite-contract.log"
    grep -Fq 'NCKU-REFERENCE-APACITE-OPTION: notocbib' "{{ tests_dir }}/reference-apacite-contract.log"
    grep -Fq 'NCKU-REFERENCE-APACITE-STATE: APA Contract References/apacite' "{{ tests_dir }}/reference-apacite-contract.log"
    grep -Fq 'NCKU-TEST-PASS: SetupReference apacite preamble side effect' "{{ tests_dir }}/reference-apacite-contract.log"
    @echo "Reference apacite contract PASS: package and notocbib side effect"

# Unknown SetupReference keys must remain deterministic hard errors.
[private]
_test-reference-key-unknown: (_expect-unknown-key "reference-key-unknown" "302-reference-key-unknown.tex" "Reference")

# Internal runtime contract for all 21 public theorem insertion helpers.
[private]
_test-theorem-contract: (_fixture-contract "theorem-contract" "500-theorem-contract.tex")
    python3 scripts/test/check-theorem-contract.py "{{ tests_dir }}"

# Unknown theorem-content keys must remain deterministic hard errors.
[private]
_test-theorem-key-unknown: (_expect-unknown-key "theorem-key-unknown" "501-theorem-key-unknown.tex" "Theorem")

# Unknown dynamic theorem-format keys remain deterministic hard errors.
[private]
_test-theorem-format-key-unknown: (_expect-unknown-key "theorem-format-key-unknown" "502-theorem-format-key-unknown.tex" "Theorem-format")

# Internal custom theorem style/counter matrix, including chained-empty counters.
[private]
_test-theorem-style-counter: (_fixture-contract "theorem-style-counter" "503-theorem-style-counter.tex")
    pdftohtml -xml -hidden -nodrm -i "{{ tests_dir }}/theorem-style-counter.pdf" "{{ tests_dir }}/theorem-style-counter"
    python3 scripts/test/check-theorem-style-counter.py "{{ tests_dir }}"

# Internal negative test for deterministic cyclic theorem-counter diagnostics.
[private]
_test-theorem-counter-cycle:
    mkdir -p "{{ tests_dir }}"
    rm -f "{{ tests_dir }}/theorem-counter-cycle."*
    if (cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ tests_dir }}" -jobname=theorem-counter-cycle ../tests/504-theorem-counter-cycle.tex); then echo "theorem counter cycle unexpectedly compiled"; exit 1; fi
    grep -Fq "Cyclic theorem counter configuration" "{{ tests_dir }}/theorem-counter-cycle.log"
    ! grep -Fq "TeX capacity exceeded" "{{ tests_dir }}/theorem-counter-cycle.log"
    @echo "Theorem counter cycle PASS: deterministic package error without recursive overflow"

# Internal integration test for the neutral non-NCKU style profile.
[private]
_test-custom-style: (_fixture-latexmk "custom-style" "600-custom-style.tex")
    grep -Fq 'NCKU-TEST-CUSTOM-PROFILE: custom' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COVER-DATE: 2024-7' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-REQUESTED-DATE: 2024-7' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-ORAL-CHI-YEAR: 2023' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COMMITTEE-MIN: 2' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-CUSTOM-COMMITTEE-MAX: 9' "{{ tests_dir }}/custom-style.log"
    grep -Fq 'NCKU-TEST-PASS: custom style profile builds without NCKU visible policy' "{{ tests_dir }}/custom-style.log"
    ! grep -Eiq 'undefined references|Rerun to get (cross-references|outlines) right' "{{ tests_dir }}/custom-style.log"
    test -s "{{ tests_dir }}/custom-style.fls"
    ! grep -Fq 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ tests_dir }}/custom-style.fls"
    ! grep -Fxq 'INPUT ./template/command/cmd-college.tex' "{{ tests_dir }}/custom-style.fls"
    ! grep -Fxq 'INPUT ./template/command/cmd-department.tex' "{{ tests_dir }}/custom-style.fls"
    ! grep -Fxq 'INPUT ./template/style/ncku/college.tex' "{{ tests_dir }}/custom-style.fls"
    ! grep -Fxq 'INPUT ./template/style/ncku/department.tex' "{{ tests_dir }}/custom-style.fls"
    pdftotext "{{ tests_dir }}/custom-style.pdf" "{{ tests_dir }}/custom-style.txt"
    pdftotext -f 4 -l 4 "{{ tests_dir }}/custom-style.pdf" "{{ tests_dir }}/custom-style-master-oral.txt"
    pdftotext -f 5 -l 5 "{{ tests_dir }}/custom-style.pdf" "{{ tests_dir }}/custom-style-doctoral-oral.txt"
    pdftotext -f 6 -l 6 "{{ tests_dir }}/custom-style.pdf" "{{ tests_dir }}/custom-style-doctoral-cover.txt"
    grep -Fq 'prepared by' "{{ tests_dir }}/custom-style-master-oral.txt"
    grep -Eq 'Example master.s submission in Department of Testing' "{{ tests_dir }}/custom-style-master-oral.txt"
    grep -Fq 'prepared by' "{{ tests_dir }}/custom-style-doctoral-oral.txt"
    grep -Fq 'Example doctoral submission in Department of Testing' "{{ tests_dir }}/custom-style-doctoral-oral.txt"
    grep -Fq 'July 2024' "{{ tests_dir }}/custom-style-doctoral-cover.txt"
    ! grep -Fq '31 July 2024' "{{ tests_dir }}/custom-style-doctoral-cover.txt"
    ! grep -Fq 'December 2023' "{{ tests_dir }}/custom-style-doctoral-cover.txt"
    ! grep -Eq 'Master of Science|Doctor of Philosophy' "{{ tests_dir }}/custom-style.txt"
    pdfinfo "{{ tests_dir }}/custom-style.pdf" > "{{ tests_dir }}/custom-style.pdfinfo"
    grep -Eq '^Pages:[[:space:]]+6$' "{{ tests_dir }}/custom-style.pdfinfo"
    grep -Eq '^Page size:.*A4' "{{ tests_dir }}/custom-style.pdfinfo"
    grep -Fq 'Example University' "{{ tests_dir }}/custom-style.txt"
    grep -Fq 'Department of Testing' "{{ tests_dir }}/custom-style.txt"
    grep -Fq 'Portable Thesis Style' "{{ tests_dir }}/custom-style.txt"
    grep -Fq 'July 2024' "{{ tests_dir }}/custom-style.txt"
    grep -Fq 'Example City, Example Country' "{{ tests_dir }}/custom-style.txt"
    grep -Fq '31 December 2023' "{{ tests_dir }}/custom-style.txt"
    grep -Fq '西 元' "{{ tests_dir }}/custom-style.txt"
    ! grep -Fq '中華民國' "{{ tests_dir }}/custom-style.txt"
    ! grep -Fq 'National Cheng Kung University' "{{ tests_dir }}/custom-style.txt"
    ! grep -Fq '國立成功大學' "{{ tests_dir }}/custom-style.txt"

# Focused generic institution API and prefixed-catalogue fixture.
[private]
_test-custom-institution-api: (_fixture-xelatex "custom-institution-api" "603-custom-institution-api.tex" "-recorder")
    test "$(grep -c 'NCKU-TEST-PASS: institution API' "{{ tests_dir }}/custom-institution-api.log")" -eq 8
    grep -Fq 'NCKU-TEST-PASS: custom profile excludes NCKU department presets' "{{ tests_dir }}/custom-institution-api.log"
    grep -Fq 'NCKU-TEST-PASS: custom profile excludes NCKU college presets' "{{ tests_dir }}/custom-institution-api.log"
    test -s "{{ tests_dir }}/custom-institution-api.fls"
    ! grep -Fxq 'INPUT ./template/command/cmd-college.tex' "{{ tests_dir }}/custom-institution-api.fls"
    ! grep -Fxq 'INPUT ./template/command/cmd-department.tex' "{{ tests_dir }}/custom-institution-api.fls"
    ! grep -Fxq 'INPUT ./template/style/ncku/college.tex' "{{ tests_dir }}/custom-institution-api.fls"
    ! grep -Fxq 'INPUT ./template/style/ncku/department.tex' "{{ tests_dir }}/custom-institution-api.fls"
    ! grep -Fq 'NCKU-TEST-FAIL:' "{{ tests_dir }}/custom-institution-api.log"

# Internal regression test for NCKU degree-specific committee-size policy.
[private]
_test-committee-size-policy: (_fixture-xelatex "committee-size-policy" "601-committee-size-policy.tex")
    test "$(grep -c 'NCKU-TEST-PASS: committee request' "{{ tests_dir }}/committee-size-policy.log")" -eq 6
    ! grep -q 'NCKU-TEST-FAIL:' "{{ tests_dir }}/committee-size-policy.log"

# Internal regression test for the oral-certificate default state.
[private]
_test-oral-default-state: (_fixture-xelatex "oral-default-state" "602-oral-default-state.tex")
    grep -q 'NCKU-TEST-PASS: oral certificate defaults to the external-image path' "{{ tests_dir }}/oral-default-state.log"

# Internal regression test for Unicode PDF metadata and bookmarks.
[private]
_test-metadata-bookmark: (_fixture-latexmk "metadata-bookmark" "700-metadata-bookmark.tex")
    grep -q 'NCKU-TEST-PASS: Unicode metadata and bookmark strings compile cleanly' "{{ tests_dir }}/metadata-bookmark.log"
    ! grep -Eiq 'Token not allowed in a PDF string|already defined|destination with the same identifier' "{{ tests_dir }}/metadata-bookmark.log"
    pdfinfo "{{ tests_dir }}/metadata-bookmark.pdf" > "{{ tests_dir }}/metadata-bookmark.pdfinfo"
    grep -Fq 'Title:           NCKU Metadata Line (成大中繼資料標題)' "{{ tests_dir }}/metadata-bookmark.pdfinfo"

# Internal contract for custom-font filename key parsing and shared aliases.
[private]
_test-custom-font-files-contract: (_fixture-contract-xelatex "custom-font-files-contract" "710-custom-font-files-contract.tex")
    python3 scripts/test/check-custom-font-files-contract.py "{{ tests_dir }}"

# Unknown custom-font filename keys remain deterministic hard errors.
[private]
_test-custom-font-files-key-unknown: (_expect-unknown-key "custom-font-files-key-unknown" "711-custom-font-files-key-unknown.tex" "Custom font filename")

# Internal contract for font-option parser state and English/CJK loading routes.
[private]
_test-font-option-contract: (_fixture-contract-xelatex "font-option-contract" "720-font-option-contract.tex")
    pdffonts "{{ tests_dir }}/font-option-contract.pdf" > "{{ tests_dir }}/font-option-contract.fonts"
    python3 scripts/test/check-font-option-contract.py "{{ tests_dir }}"

# Unknown font-option keys remain deterministic hard errors.
[private]
_test-font-option-key-unknown: (_expect-unknown-key "font-option-key-unknown" "721-font-option-key-unknown.tex" "Font option")

# Internal routing contract for numeric font-type dispatch, including custom.
[private]
_test-font-type-routing: (_fixture-xelatex "font-type-routing" "712-font-type-routing.tex")
    test "$(grep -c 'NCKU-FONT-ROUTE-INIT-TIMESKAIU' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    test "$(grep -c 'NCKU-FONT-ROUTE-INIT-NOTOSANSCJK' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    test "$(grep -c 'NCKU-FONT-ROUTE-INIT-CUSTOM' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    test "$(grep -c 'NCKU-FONT-ROUTE-USE-TIMESKAIU' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    test "$(grep -c 'NCKU-FONT-ROUTE-USE-NOTOSANSCJK' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    test "$(grep -c 'NCKU-FONT-ROUTE-USE-CUSTOM' "{{ tests_dir }}/font-type-routing.log")" -eq 1
    grep -Fq 'NCKU-FONT-ROUTE-TYPE-AFTER-CUSTOM: 10' "{{ tests_dir }}/font-type-routing.log"
    grep -Fq 'NCKU-TEST-PASS: font type routing dispatches every registered type' "{{ tests_dir }}/font-type-routing.log"
    ! grep -Fq 'NCKU-TEST-FAIL' "{{ tests_dir }}/font-type-routing.log"

# Internal regression test for bundled Latin/CJK font policy.
[private]
_test-font-cjk: (_fixture-latexmk "font-cjk" "730-font-cjk.tex")
    grep -q 'NCKU-TEST-PASS: bundled Latin and CJK font policies compile' "{{ tests_dir }}/font-cjk.log"
    ! grep -q 'Unknown CJK family' "{{ tests_dir }}/font-cjk.log"
    grep -Eq "Font shape .*m/sc.*undefined" "{{ tests_dir }}/font-cjk.log"
    pdftotext "{{ tests_dir }}/font-cjk.pdf" "{{ tests_dir }}/font-cjk.txt"
    grep -q 'Monospaced Latin and 中文等寬語境' "{{ tests_dir }}/font-cjk.txt"

# Internal regression test for keyword helper equivalence.
[private]
_test-keyword-values: (_fixture-latexmk "keyword-values" "740-keyword-values.tex")
    test "$(grep -c 'NCKU-TEST-PASS:' "{{ tests_dir }}/keyword-values.log")" -eq 4
    ! grep -q 'NCKU-TEST-FAIL:' "{{ tests_dir }}/keyword-values.log"
    pdfinfo "{{ tests_dir }}/keyword-values.pdf" > "{{ tests_dir }}/keyword-values.pdfinfo"
    grep -Fq 'Keywords:        Alpha, Beta' "{{ tests_dir }}/keyword-values.pdfinfo"

# Internal integration test for the student-only dependency path.
[private]
_test-student-mode: (_fixture-latexmk "student-mode" "800-student-mode.tex")
    grep -q 'NCKU-TEST-PASS: student mode compiles without teaching examples' "{{ tests_dir }}/student-mode.log"
    grep -q 'NCKU-TEST-PASS: default diagonal draft watermark text is empty' "{{ tests_dir }}/student-mode.log"
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "{{ tests_dir }}/student-mode.log"
    ! grep -F '/example/' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./conf/conf.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/context.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/abstract/eng.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/acknowledgments/eng.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/nomenclature/nomenclature.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/introduction/introduction.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/related-work/related-work.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/conclusion/conclusion.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'INPUT ./context/references/references.tex' "{{ tests_dir }}/student-mode.fls"
    grep -Fxq 'Database file #1: context/references/paper.bib' "{{ tests_dir }}/student-mode.blg"
    grep -Fxq 'Database file #2: context/references/misc.bib' "{{ tests_dir }}/student-mode.blg"
    grep -Fxq 'Database file #3: context/references/book.bib' "{{ tests_dir }}/student-mode.blg"
    pdftotext -f 1 -l 1 "{{ tests_dir }}/student-mode.pdf" "{{ tests_dir }}/student-mode-cover.txt"
    ! grep -Eiq '\(Draft\)|\(初稿\)' "{{ tests_dir }}/student-mode-cover.txt"
    ! grep -F 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ tests_dir }}/student-mode.fls"

# Internal regression test proving Draft and institutional watermark remain opt-in.
[private]
_test-draft-watermark-opt-in: (_fixture-latexmk "draft-watermark-opt-in" "801-draft-watermark-opt-in.tex")
    grep -q 'NCKU-TEST-PASS: draft and institutional watermark remain explicit opt-ins' "{{ tests_dir }}/draft-watermark-opt-in.log"
    grep -q 'NCKU-TEST-PASS: diagonal draft watermark text remains an explicit opt-in' "{{ tests_dir }}/draft-watermark-opt-in.log"
    pdftotext -f 1 -l 1 "{{ tests_dir }}/draft-watermark-opt-in.pdf" "{{ tests_dir }}/draft-watermark-opt-in-cover.txt"
    grep -Fq '(Draft)' "{{ tests_dir }}/draft-watermark-opt-in-cover.txt"
    grep -Fq 'template/style/ncku/watermark-20160509_v2-a4.pdf' "{{ tests_dir }}/draft-watermark-opt-in.fls"

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
    just _release-pdfs
    git archive --format=zip --prefix=ncku-thesis-template-latex/ --output="{{ build_dir }}/release/ncku-thesis-template-latex-{{ version }}.zip" HEAD:thesis
    scripts/release/package-examples.sh "{{ build_dir }}/release" "ncku-thesis-template-latex-examples-{{ version }}.zip" "{{ version }}"
    scripts/release/verify-assets.sh "{{ build_dir }}/release" "ncku-thesis-template-latex-{{ version }}.zip" "ncku-thesis-template-latex-examples-{{ version }}.zip" "{{ version }}"

# Build the five standalone release example PDFs. Each latexmk run uses its
# own jobname inside build/release, so the dependencies run concurrently
# ([parallel] honors JUST_JOBS; JUST_JOBS=1 restores serial execution).
[private]
[parallel]
_release-pdfs: (_release-pdf "../scripts/release/cover.tex" "example-cover") (_release-pdf "../scripts/release/thesis-chi.tex" "example-thesis-chi") (_release-pdf "../scripts/release/thesis-eng.tex" "example-thesis-eng") (_release-pdf "../scripts/release/defense-certificate-master.tex" "example-legacy-defense-certificate-master") (_release-pdf "../scripts/release/defense-certificate-phd.tex" "example-legacy-defense-certificate-phd")

# Internal helper: build one named release PDF from the thesis source directory.
[private]
_release-pdf source job:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/release" -jobname="{{ job }}" "{{ source }}"

# Remove generated LaTeX build artifacts.
clean:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}" -C thesis.tex
    rm -rf "{{ build_dir }}"
