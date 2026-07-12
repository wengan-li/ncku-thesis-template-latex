#!/usr/bin/env bash
set -euo pipefail

version=${1:-dev}
output_dir=${2:-build/overleaf}
archive_name=ncku-thesis-template-latex-overleaf-${version}.zip
repo_root=$(git rev-parse --show-toplevel)
output_dir_abs=$(cd "$repo_root" && mkdir -p "$output_dir" && cd "$output_dir" && pwd)
work_dir=$(mktemp -d)
source_dir=${work_dir}/source
build_dir=${work_dir}/build
cleanup() {
  rm -rf "$work_dir"
}
trap cleanup EXIT
mkdir -p "$source_dir" "$build_dir"

git archive HEAD:thesis | tar -x -C "$source_dir"
rm -rf "$source_dir/example"
rm -f "$source_dir/cover.tex"

python3 - "$source_dir/conf/conf.tex" <<'PY'
from pathlib import Path
import sys
path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = "\n\\ExampleMode\n"
if text.count(needle) != 1:
    raise SystemExit("expected exactly one active \\ExampleMode line")
path.write_text(text.replace(needle, "\n\\StudentMode % Overleaf package default\n"), encoding="utf-8")
PY

# Overleaf detects a project's main document by looking for a direct
# \documentclass declaration. Keep the canonical source layout unchanged, but
# make the generated Overleaf entry point unambiguous and root-local.
python3 - "$source_dir/thesis.tex" "$source_dir/template/configure.tex" "$source_dir/README.md" <<'PY'
from pathlib import Path
import sys

thesis = Path(sys.argv[1])
configure = Path(sys.argv[2])
readme = Path(sys.argv[3])

declaration = "\\NeedsTeXFormat{LaTeX2e}[2020-10-01]\n\\documentclass[12pt, a4paper, onecolumn]{report}\n"

thesis_text = thesis.read_text(encoding="utf-8")
thesis_needle = "% 基本設定 Basic configuration\n\\input{./template/configure}"
if thesis_text.count(thesis_needle) != 1:
    raise SystemExit("expected one basic-configuration entry point in thesis.tex")
thesis.write_text(
    thesis_text.replace(
        thesis_needle,
        f"{declaration}\n% 基本設定 Basic configuration\n\\input{{./template/configure}}",
    ),
    encoding="utf-8",
)

configure_text = configure.read_text(encoding="utf-8")
configure_needle = declaration + "\n"
if configure_text.count(configure_needle) != 1:
    raise SystemExit("expected one document declaration in template/configure.tex")
configure.write_text(configure_text.replace(configure_needle, ""), encoding="utf-8")

readme_text = readme.read_text(encoding="utf-8")
readme.write_text(
    readme_text
    + "\n\n## Overleaf quick start\n\n"
      "After uploading this ZIP, open **Settings → Compiler** and select:\n\n"
      "- Compiler: **XeLaTeX**\n"
      "- TeX Live: the latest available version\n"
      "- Main document: **thesis.tex**\n\n"
      "Then choose **Recompile from scratch**. Overleaf defaults new ZIP uploads "
      "to pdfLaTeX, which this template intentionally rejects.\n",
    encoding="utf-8",
)
PY

rm -f "$output_dir_abs/$archive_name"
(
  cd "$source_dir"
  zip -qr "$output_dir_abs/$archive_name" .
)

python3 - "$output_dir_abs/$archive_name" <<'PY'
from pathlib import Path
from zipfile import ZipFile
import sys
archive = Path(sys.argv[1])
editable_suffixes = {".tex", ".bib", ".md", ".txt", ".sty", ".cls", ".cfg"}
with ZipFile(archive) as zf:
    files = [item for item in zf.infolist() if not item.is_dir()]
    names = {item.filename for item in files}
    required = {"README.md", "thesis.tex", "conf/conf.tex", "context/context.tex", "template/configure.tex"}
    missing = required - names
    if missing:
        raise SystemExit(f"missing required Overleaf files: {sorted(missing)}")
    if any(name.startswith("example/") for name in names):
        raise SystemExit("Overleaf package contains the teaching example corpus")
    if "cover.tex" in names:
        raise SystemExit("Overleaf package contains a second main document")
    thesis = zf.read("thesis.tex").decode("utf-8")
    configure = zf.read("template/configure.tex").decode("utf-8")
    if thesis.count("\\documentclass") != 1:
        raise SystemExit("Overleaf root thesis.tex must contain exactly one direct documentclass declaration")
    if any(line.lstrip().startswith("\\documentclass") for line in configure.splitlines()):
        raise SystemExit("nested template/configure.tex still contains an active documentclass declaration")
    if len(files) > 180:
        raise SystemExit(f"Overleaf package has {len(files)} files; limit is 180")
    too_large = [item.filename for item in files if item.file_size > 50 * 1024 * 1024]
    if too_large:
        raise SystemExit(f"files exceed 50 MB: {too_large}")
    editable = sum(item.file_size for item in files if Path(item.filename).suffix.lower() in editable_suffixes)
    if editable > 7 * 1024 * 1024:
        raise SystemExit(f"editable data is {editable} bytes; limit is 7 MB")
    if archive.stat().st_size > 50 * 1024 * 1024:
        raise SystemExit(f"archive is {archive.stat().st_size} bytes; upload limit is 50 MB")
    print(f"Overleaf package limits passed: {len(files)} files, {editable} editable bytes, {archive.stat().st_size} ZIP bytes")
PY

unzip -q "$output_dir_abs/$archive_name" -d "$build_dir"
python3 - "$build_dir" <<'PY'
from pathlib import Path
import subprocess
import sys
import time
root = Path(sys.argv[1])
started = time.monotonic()
result = subprocess.run(
    ["latexmk", "-xelatex", "-synctex=1", "-interaction=nonstopmode", "thesis.tex"],
    cwd=root,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
elapsed = time.monotonic() - started
(root / "overleaf-build.log").write_text(result.stdout, encoding="utf-8")
if result.returncode:
    print(result.stdout, file=sys.stderr)
    raise SystemExit(f"Overleaf package build failed with exit code {result.returncode}")
if not (root / "thesis.pdf").is_file():
    raise SystemExit("Overleaf package build did not produce thesis.pdf")
log = (root / "thesis.log").read_text(encoding="utf-8", errors="replace")
for pattern in ("undefined references", "undefined citations", "Rerun to get cross-references right"):
    if pattern.lower() in log.lower():
        raise SystemExit(f"Overleaf package final log contains: {pattern}")
print(f"Overleaf package cold local XeLaTeX build passed in {elapsed:.2f} seconds")
if elapsed > 10:
    print("WARNING: local cold build exceeds Overleaf free-plan 10-second timeout; an authenticated Overleaf build is required", file=sys.stderr)
PY

sha256=$(shasum -a 256 "$output_dir_abs/$archive_name" | awk '{print $1}')
printf 'Overleaf package: %s\nSHA-256: %s\n' "$output_dir_abs/$archive_name" "$sha256"
