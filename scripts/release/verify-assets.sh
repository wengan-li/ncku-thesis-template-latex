#!/usr/bin/env bash
set -euo pipefail

asset_dir=${1:-build/release}

required=(
  ncku-thesis-template-latex.zip
  example-cover.pdf
  example-thesis-chi.pdf
  example-thesis-eng.pdf
  example-thesis-demo.pdf
  example-legacy-defense-certificate-master.pdf
  example-legacy-defense-certificate-phd.pdf
)

for name in "${required[@]}"; do
  test -s "${asset_dir}/${name}" || {
    printf 'missing release asset: %s\n' "$name" >&2
    exit 1
  }
done

check_pdf() {
  local name=$1
  local expected_pages=$2
  local pdf=${asset_dir}/${name}
  local pages

  pdfinfo "$pdf" | grep -q '^Page size:.*A4'
  pages=$(pdfinfo "$pdf" | awk '/^Pages:/ { print $2 }')
  if [[ $expected_pages == +* ]]; then
    test "$pages" -ge "${expected_pages#+}"
  else
    test "$pages" -eq "$expected_pages"
  fi
}

check_pdf example-cover.pdf 2
check_pdf example-thesis-chi.pdf +10
check_pdf example-thesis-eng.pdf +10
check_pdf example-thesis-demo.pdf +100
check_pdf example-legacy-defense-certificate-master.pdf 6
check_pdf example-legacy-defense-certificate-phd.pdf 10

while IFS= read -r log; do
  ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "$log"
done < <(find "$asset_dir" -maxdepth 1 -name '*.log' -type f -print)

archived=$(unzip -Z1 "${asset_dir}/ncku-thesis-template-latex.zip")
test -n "$archived"
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/justfile'
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/latexmkrc'
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/tests/set-thesis-date.tex'
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/thesis/thesis.tex'
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/thesis/conf/conf.tex'
printf '%s\n' "$archived" | grep -qx 'ncku-thesis-template-latex/thesis/example/abstract/extended.tex'
if printf '%s\n' "$archived" | grep -qv '^ncku-thesis-template-latex/'; then
  printf 'ZIP contains a path outside the release project folder\n' >&2
  exit 1
fi

printf 'Verified %d release assets in %s\n' "${#required[@]}" "$asset_dir"
