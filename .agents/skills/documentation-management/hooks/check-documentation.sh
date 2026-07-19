#!/usr/bin/env bash
# Non-blocking documentation reminder for newly added template capability files.
# Wired through .agents/hooks/check-documentation.sh and .claude/settings.json.

set -uo pipefail

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

added="$(
  { git diff --name-only --diff-filter=A HEAD 2>/dev/null
    git ls-files --others --exclude-standard 2>/dev/null
  } | sort -u
)"

[ -z "$added" ] && exit 0

feature_added="$(printf '%s\n' "$added" | grep -E \
  -e '^thesis/.*\.(tex|sty|cls)$' \
  2>/dev/null | grep -Ev \
  -e '^thesis/example/' \
  2>/dev/null || true)"

[ -z "$feature_added" ] && exit 0

docs_touched="$(git status --porcelain -- docs todos thesis/README.md CHANGELOG.md 2>/dev/null || true)"
[ -n "$docs_touched" ] && exit 0

count="$(printf '%s\n' "$feature_added" | grep -c .)"
files="$(printf '%s' "$feature_added" | paste -sd ', ' -)"
msg="Documentation reminder: ${count} new template source file(s) have no docs/requirements/todo update. Load the documentation-management skill or confirm the change is documentation-neutral. Files: ${files}"
esc="$(printf '%s' "$msg" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"
printf '{"systemMessage": "%s", "suppressOutput": true}\n' "$esc"
exit 0
