#!/usr/bin/env bash
set -euo pipefail

asset_dir=${1:-build/release}
student_zip=${2:-ncku-thesis-template-latex-dev.zip}
examples_zip=${3:-ncku-thesis-template-latex-examples-dev.zip}
version=${4:-dev}
package_root=ncku-thesis-template-latex-examples

# shellcheck source=scripts/release/example-assets.sh
source "$(dirname "$0")/example-assets.sh"

required=(
  "$student_zip"
  "$examples_zip"
  "${example_asset_sources[@]}"
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
  local info

  info=$(pdfinfo "$pdf")
  grep -q '^Page size:.*A4' <<< "$info"
  pages=$(awk '/^Pages:/ { print $2 }' <<< "$info")
  if [[ $expected_pages == +* ]]; then
    test "$pages" -ge "${expected_pages#+}"
  else
    test "$pages" -eq "$expected_pages"
  fi
}

for index in "${!example_asset_sources[@]}"; do
  check_pdf "${example_asset_sources[$index]}" "${example_asset_pages[$index]}"
done

# An errexit-exempt `! grep` loop body can never fail the script; assert each
# log explicitly so one bad build log aborts verification.
while IFS= read -r log; do
  if grep -Eiq 'undefined references|undefined citations|Rerun to get (cross-references|outlines) right' "$log"; then
    printf 'unresolved reference or rerun warnings in %s\n' "$log" >&2
    exit 1
  fi
done < <(find "$asset_dir" -maxdepth 1 -name '*.log' -type f -print)

scripts/release/verify-student-archive.sh "${asset_dir}/${student_zip}"

expected_example_entries=$(printf '%s\n' \
  "${example_package_documents[@]}" \
  "${example_asset_destinations[@]}" | sed "s#^#${package_root}/#" | sort)
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
for index in "${!example_asset_sources[@]}"; do
  cmp "${asset_dir}/${example_asset_sources[$index]}" \
    "${extract_dir}/${package_root}/${example_asset_destinations[$index]}"
done
cmp <(git show HEAD:LICENSE) "${extract_dir}/${package_root}/LICENSE"

grep -Fq "Version: \`${version}\`" "${extract_dir}/${package_root}/README.md"
grep -Fq 'Current students must use the official files produced by the university degree-examination system' \
  "${extract_dir}/${package_root}/README.md"

printf 'Verified %d generated example PDFs and 2 release ZIP packages in %s\n' \
  "${#example_asset_sources[@]}" "$asset_dir"
