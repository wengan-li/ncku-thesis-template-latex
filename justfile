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

# Build the full teaching/demo document selected by the checked-in configuration.
demo: thesis

# Build and verify the canonical artifacts and resolved references.
check: thesis
    test -s "{{ artifact }}"
    test -s "{{ synctex }}"
    pdfinfo "{{ artifact }}" | grep -q '^Pages:'
    pdfinfo "{{ artifact }}" | grep -q '^Page size:.*A4'
    ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "{{ log }}"

# Run the required build and verification test gate.
test: check

# Run the complete local CI gate.
ci: test
    git diff --check

# Build and verify the complete same-source release asset set.
release: test
    rm -rf "{{ build_dir }}/release"
    mkdir -p "{{ build_dir }}/release"
    cp "{{ artifact }}" "{{ build_dir }}/release/example-thesis-demo.pdf"
    just _release-pdf ../scripts/release/cover.tex example-cover
    just _release-pdf ../scripts/release/thesis-chi.tex example-thesis-chi
    just _release-pdf ../scripts/release/thesis-eng.tex example-thesis-eng
    just _release-pdf ../scripts/release/defense-certificate-master.tex example-defense-certificate-master
    just _release-pdf ../scripts/release/defense-certificate-phd.tex example-defense-certificate-phd
    git archive --format=zip --prefix=ncku-thesis-template-latex/ --output="{{ build_dir }}/release/ncku-thesis-template-latex.zip" HEAD:thesis
    scripts/release/verify-assets.sh "{{ build_dir }}/release"

# Internal helper: build one named release PDF from the thesis source directory.
[private]
_release-pdf source job:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}/release" -jobname="{{ job }}" "{{ source }}"

# Remove generated LaTeX build artifacts.
clean:
    cd "{{ source_dir }}" && latexmk -r ../latexmkrc -outdir=../"{{ build_dir }}" -C thesis.tex
    rm -rf "{{ build_dir }}"
