#!/usr/bin/env bash
set -euo pipefail

asset_dir=${1:-build/release}
examples_zip=${2:-ncku-thesis-template-latex-examples-dev.zip}
version=${3:-dev}
source_commit=${4:-$(git rev-parse HEAD)}
package_root=ncku-thesis-template-latex-examples
repo_url=https://github.com/wengan-li/ncku-thesis-template-latex

mkdir -p "$asset_dir"
asset_dir=$(cd "$asset_dir" && pwd)

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

tmp_dir=$(mktemp -d)
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

package_dir=${tmp_dir}/${package_root}
mkdir -p "$package_dir"

for index in "${!sources[@]}"; do
  source_name=${sources[$index]}
  destination_name=${destinations[$index]}
  test -s "${asset_dir}/${source_name}" || {
    printf 'missing generated example PDF: %s\n' "$source_name" >&2
    exit 1
  }
  cp "${asset_dir}/${source_name}" "${package_dir}/${destination_name}"
done

cat >"${package_dir}/README.md" <<EOF
# NCKU thesis template — generated examples

Version: \`${version}\`

Source commit: \`${source_commit}\`

Project: <${repo_url}>

This package contains generated PDF examples from one verified source revision. It is for previewing output; it does not contain the editable student project.

## Contents

- \`cover.pdf\` — cover and inner-cover example
- \`thesis-chi.pdf\` — Chinese thesis example
- \`thesis-eng.pdf\` — English thesis example
- \`thesis-full.pdf\` — complete teaching and integration example
- \`defense-certificate-master.pdf\` — template-generated master's defense-certificate demonstration
- \`defense-certificate-phd.pdf\` — template-generated doctoral defense-certificate demonstration

## Defense-certificate notice

The two defense-certificate PDFs are unofficial template demonstrations and regression outputs. Current students must use the official files produced by the university degree-examination system and follow current university and department guidance.

## Editable student project

Download \`ncku-thesis-template-latex-${version}.zip\` from the same GitHub Release:

<${repo_url}/releases>
EOF

rm -f "${asset_dir}/${examples_zip}"
(
  cd "$tmp_dir"
  zip -q -r "${asset_dir}/${examples_zip}" "$package_root"
)

test -s "${asset_dir}/${examples_zip}"
printf 'Packaged %d generated PDFs plus README in %s\n' "${#sources[@]}" "${asset_dir}/${examples_zip}"
