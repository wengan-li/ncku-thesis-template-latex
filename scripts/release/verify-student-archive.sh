#!/usr/bin/env bash
set -euo pipefail

student_zip=${1:?usage: verify-student-archive.sh <student-zip>}
package_root=ncku-thesis-template-latex

test -s "$student_zip" || {
  printf 'missing student ZIP: %s\n' "$student_zip" >&2
  exit 1
}

student_entries=$(unzip -Z1 "$student_zip")
test -n "$student_entries"
student_files=$(sed '/\/$/d' <<< "$student_entries" | sort)
expected_student_files=$(git ls-tree -r --name-only HEAD:thesis | sed "s#^#${package_root}/#" | sort)

if [[ "$student_files" != "$expected_student_files" ]]; then
  printf 'student ZIP contents differ from the exact HEAD:thesis file list\n' >&2
  diff -u <(printf '%s\n' "$expected_student_files") <(printf '%s\n' "$student_files") >&2 || true
  exit 1
fi

require_entry() {
  grep -qx "${package_root}/$1" <<< "$student_entries" || {
    printf 'student ZIP is missing required entry: %s/%s\n' "$package_root" "$1" >&2
    exit 1
  }
}

for entry in \
  README.md \
  README.en.md \
  thesis.tex \
  conf/conf.tex \
  conf/README.md \
  conf/README.en.md \
  example/abstract/extended.tex \
  template/configure.tex \
  template/compat/v1.tex \
  template/style/Customization.md \
  template/style/Customization.en.md \
  template/style/base/base.tex \
  template/style/ncku/ncku.tex \
  template/style/custom/custom.tex; do
  require_entry "$entry"
done

# Assert the shared doc-pair contract (metadata + reciprocal switcher), then
# every additional per-document marker.
require_doc_markers() {
  local entry=$1 pair=$2 lang=$3
  shift 3
  local content marker
  content=$(unzip -p "$student_zip" "${package_root}/${entry}")
  for marker in \
    "<!-- doc-pair: ${pair}; lang: ${lang};" \
    '[繁體中文](README.md) | [English](README.en.md)' \
    "$@"; do
    grep -Fq "$marker" <<< "$content" || {
      printf 'student ZIP %s is missing required marker: %s\n' "$entry" "$marker" >&2
      exit 1
    }
  done
}

require_doc_markers README.md student-readme zh-Hant-TW \
  '## 由1.x升級' 'conf/README.md' 'docs/v1-to-v2-migration.md'
require_doc_markers README.en.md student-readme en \
  '## Migrate from 1.x' 'conf/README.en.md' 'docs/v1-to-v2-migration.en.md'
require_doc_markers conf/README.md student-config zh-Hant-TW \
  '../README.md' '../template/style/Customization.md'
require_doc_markers conf/README.en.md student-config en \
  '../README.en.md' '../template/style/Customization.en.md'

if grep -Eq "^${package_root}/(justfile|latexmkrc|tests/|scripts/|thesis/)" <<< "$student_entries"; then
  printf 'student ZIP contains repository tooling or a redundant thesis/ layer\n' >&2
  exit 1
fi
if grep -qv "^${package_root}/" <<< "$student_entries"; then
  printf 'student ZIP contains a path outside the project folder\n' >&2
  exit 1
fi

printf 'Verified student ZIP exact HEAD:thesis file list: %s\n' "$student_zip"
