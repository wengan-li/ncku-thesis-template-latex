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

grep -qx "${package_root}/README.md" <<< "$student_entries"
grep -qx "${package_root}/thesis.tex" <<< "$student_entries"
grep -qx "${package_root}/conf/conf.tex" <<< "$student_entries"
grep -qx "${package_root}/example/abstract/extended.tex" <<< "$student_entries"
grep -qx "${package_root}/template/configure.tex" <<< "$student_entries"
grep -qx "${package_root}/template/compat/v1.tex" <<< "$student_entries"
grep -qx "${package_root}/template/style/Customization.md" <<< "$student_entries"
grep -qx "${package_root}/template/style/base/base.tex" <<< "$student_entries"
grep -qx "${package_root}/template/style/ncku/ncku.tex" <<< "$student_entries"
grep -qx "${package_root}/template/style/custom/custom.tex" <<< "$student_entries"

student_readme=$(unzip -p "$student_zip" "${package_root}/README.md")
grep -Fq '## Migrating from 1.x' <<< "$student_readme"
grep -Fq 'docs/MIGRATION-1.x-TO-2.x.md' <<< "$student_readme"

if grep -Eq "^${package_root}/(justfile|latexmkrc|tests/|scripts/|thesis/)" <<< "$student_entries"; then
  printf 'student ZIP contains repository tooling or a redundant thesis/ layer\n' >&2
  exit 1
fi
if grep -qv "^${package_root}/" <<< "$student_entries"; then
  printf 'student ZIP contains a path outside the project folder\n' >&2
  exit 1
fi

printf 'Verified student ZIP exact HEAD:thesis file list: %s\n' "$student_zip"
