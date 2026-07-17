#!/usr/bin/env bash
#
# check-feature-docs.sh — NON-BLOCKING reminder for the feature-documentation
# skill. New feature code since HEAD with no docs/planning update → one nudge.
# A Stop hook's plain stdout is swallowed, so the reminder is emitted as JSON
# `{"systemMessage": ...}`. Always exits 0; never blocks.
# Wired repo-wide as a Stop hook in the committed .claude/settings.json,
# via the .agents/hooks/ registry symlink.

set -uo pipefail

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Scope: files NEW since the last commit (HEAD baseline) — this session's
# output. A branch-level guarantee belongs in CI review, not a local reminder.
added="$(
  { git diff --name-only --diff-filter=A HEAD 2>/dev/null
    git ls-files --others --exclude-standard 2>/dev/null
  } | sort -u
)"

[ -z "$added" ] && exit 0

# New capability code in this repo: LaTeX template source under thesis/. Test files carry no doc obligation.
feature_added="$(printf '%s\n' "$added" | grep -E \
  -e '^thesis/.*\.(tex|sty|cls)$' \
  2>/dev/null | grep -Ev \
  -e '^thesis/example/' \
  2>/dev/null || true)"

[ -z "$feature_added" ] && exit 0

docs_touched="$(git status --porcelain -- docs todos 2>/dev/null || true)"
[ -n "$docs_touched" ] && exit 0

count="$(printf '%s\n' "$feature_added" | grep -c . )"
files="$(printf '%s' "$feature_added" | paste -sd ', ' -)"

msg="📝 feature-documentation: ${count} new feature file(s) added with no docs/ update — run the \`feature-documentation\` skill to update thesis/README.md / docs/ records (or ignore if this is a refactor/bugfix). Files: ${files}"

esc="$(printf '%s' "$msg" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"

printf '{"systemMessage": "%s", "suppressOutput": true}\n' "$esc"
exit 0
