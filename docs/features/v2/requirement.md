---
name: v2-modernization
description: The thesis template modernizes to v2 (XeLaTeX, hardened numbering/floats/theorems/API manifest, deprecated-command compatibility) without breaking the v1 public API for existing student documents.
status: completed
---

# 01 — V2 template modernization

## Requirement

The v2 template line modernizes the XeLaTeX source and hardens local
behavior (numbering, floats, theorems, API manifest) while every v1 public
command keeps working per [`public-api-compatibility.md`](public-api-compatibility.md). Why:
students' in-progress theses must survive a template upgrade untouched.
Intent and final evidence: [`modernization.md`](modernization.md).

## Mapped todos

All completed and promoted into this feature record:

- [`deprecated-command-compatibility.md`](deprecated-command-compatibility.md)
- [`full-review-repairs.md`](full-review-repairs.md)
- [`api-manifest-hardening.md`](api-manifest-hardening.md)
- [`float-hardening.md`](float-hardening.md)
- [`numbering-hardening.md`](numbering-hardening.md)
- [`theorem-hardening.md`](theorem-hardening.md)
- [`super-optimization.md`](super-optimization.md)
