---
name: v2-modernization
description: The thesis template modernizes to v2 (XeLaTeX, hardened numbering/floats/theorems/API manifest, deprecated-command compatibility) without breaking the v1 public API for existing student documents.
status: active
---

# 01 — V2 template modernization

## Requirement

The v2 template line modernizes the XeLaTeX source and hardens local
behavior (numbering, floats, theorems, API manifest) while every v1 public
command keeps working per `docs/v2-public-api-compatibility.md`. Why:
students' in-progress theses must survive a template upgrade untouched.
Intent brief: `docs/v2-modernization.md` (stays in place — cited by README
and the repo-maintenance skill). Policy/history records under `docs/`.

## Mapped todos

All complete on `feat/v2.x`:

- `todos/v2-deprecated-command-compatibility.md` — deprecated command compatibility
- `todos/v2-full-review-repairs.md` — full review repairs
- `todos/v2-local-api-manifest-hardening.md` — API manifest hardening
- `todos/v2-local-float-hardening.md` — float hardening
- `todos/v2-local-numbering-hardening.md` — numbering hardening
- `todos/v2-local-theorem-hardening.md` — theorem hardening
- `todos/v2-super-optimization.md` — source super-optimization
