#!/usr/bin/env bash
set -euo pipefail

asset_dir=${1:-build/release}
student_zip=${2:-ncku-thesis-template-latex-dev.zip}
examples_zip=${3:-ncku-thesis-template-latex-examples-dev.zip}
version=${4:-dev}
package_root=ncku-thesis-template-latex-examples

sources=(
  example-cover.pdf
  example-thesis-chi.pdf
  example-thesis-eng.pdf
  example-thesis-full.pdf
  example-legacy-defense-certificate-master.pdf
  example-legacy-defense-certificate-phd.pdf
)

destinations=(
  cover.pdf
  thesis-chi.pdf
  thesis-eng.pdf
  thesis-full.pdf
  defense-certificate-master.pdf
  defense-certificate-phd.pdf
)

required=(
  "$student_zip"
  "$examples_zip"
  "${sources[@]}"
)

for name in "${required[@]}"; do
  test -s "${asset_dir}/${name}" || {
    printf 'missing release build product: %s\n' "$name" >&2
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
check_pdf example-thesis-full.pdf +100
check_pdf example-legacy-defense-certificate-master.pdf 6
check_pdf example-legacy-defense-certificate-phd.pdf 10

while IFS= read -r log; do
  ! grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "$log"
done < <(find "$asset_dir" -maxdepth 1 -name '*.log' -type f -print)

student_entries=$(unzip -Z1 "${asset_dir}/${student_zip}")
test -n "$student_entries"
printf '%s\n' "$student_entries" | grep -qx 'ncku-thesis-template-latex/README.md'
printf '%s\n' "$student_entries" | grep -qx 'ncku-thesis-template-latex/thesis.tex'
printf '%s\n' "$student_entries" | grep -qx 'ncku-thesis-template-latex/conf/conf.tex'
printf '%s\n' "$student_entries" | grep -qx 'ncku-thesis-template-latex/example/abstract/extended.tex'
printf '%s\n' "$student_entries" | grep -qx 'ncku-thesis-template-latex/template/configure.tex'
if printf '%s\n' "$student_entries" | grep -Eq '^ncku-thesis-template-latex/(justfile|latexmkrc|tests/|thesis/)'; then
  printf 'student ZIP contains repository tooling or a redundant thesis/ layer\n' >&2
  exit 1
fi
if printf '%s\n' "$student_entries" | grep -qv '^ncku-thesis-template-latex/'; then
  printf 'student ZIP contains a path outside the project folder\n' >&2
  exit 1
fi

expected_example_entries=$(printf '%s\n' \
  "${package_root}/README.md" \
  "${destinations[@]}" | sed "2,\$s#^#${package_root}/#" | sort)
actual_example_entries=$(unzip -Z1 "${asset_dir}/${examples_zip}" | sed '/\/$/d' | sort)
if [[ "$actual_example_entries" != "$expected_example_entries" ]]; then
  printf 'examples ZIP contents differ from the exact allowlist\nExpected:\n%s\nActual:\n%s\n' \
    "$expected_example_entries" "$actual_example_entries" >&2
  exit 1
fi

extract_dir=$(mktemp -d)
cleanup() {
  rm -rf "$extract_dir"
}
trap cleanup EXIT
unzip -q "${asset_dir}/${examples_zip}" -d "$extract_dir"
for index in "${!sources[@]}"; do
  cmp "${asset_dir}/${sources[$index]}" "${extract_dir}/${package_root}/${destinations[$index]}"
done

grep -Fq "Version: \`${version}\`" "${extract_dir}/${package_root}/README.md"
grep -Fq 'Current students must use the official files produced by the university degree-examination system' \
  "${extract_dir}/${package_root}/README.md"

printf 'Verified 6 generated example PDFs and 2 release ZIP packages in %s\n' "$asset_dir"
