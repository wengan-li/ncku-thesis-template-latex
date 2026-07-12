# Release versioning and promotion

## Version format

Release tags use this repository-specific format:

```text
vMAJOR.MINOR.PATCH.YYMMDDhhmmss
```

The timestamp is always UTC:

```text
YY  two-digit year
MM  month
DD  day
hh  hour (24-hour clock)
mm  minute
ss  second
```

Example:

```text
v1.8.0.260712140500
```

Generate a candidate tag string on macOS or Linux with:

```bash
date -u +v1.8.0.%y%m%d%H%M%S
```

The fourth numeric component makes the tag unique and chronologically sortable. It is a deliberate repository convention, not strict Semantic Versioning; tools that require exactly `MAJOR.MINOR.PATCH` may reject it.

## Workflow boundary

The release workflow has two stages:

1. **Build** — a tag push or manual dispatch runs `just test`, runs `just release`, and uploads the verified files as a temporary workflow artifact.
2. **Promote** — only a matching Git tag event downloads that exact workflow artifact and attaches it to a GitHub Release.

A manual dispatch is build-only. It does not create a GitHub Release.

Release tags must match:

```text
^v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{12}$
```

The workflow also parses the final 12 digits as a real UTC date and time, so impossible timestamps are rejected.

## Same-source guarantee

`just release` requires a clean Git worktree. This prevents release PDFs built from uncommitted files from being combined with a ZIP produced from `HEAD`.

The ZIP expands to one `ncku-thesis-template-latex/` project directory. It includes the canonical `justfile`, `latexmkrc`, and focused test fixture beside the `thesis/` source directory, so the extracted package can run `just test` without the rest of the Git repository.

The promoted release contains:

```text
ncku-thesis-template-latex.zip
example-cover.pdf
example-thesis-chi.pdf
example-thesis-eng.pdf
example-thesis-full.pdf
example-legacy-defense-certificate-master.pdf
example-legacy-defense-certificate-phd.pdf
```

The two generated defense-certificate assets are explicitly labelled `legacy`. Normal thesis example PDFs do not embed generated defense certificates; current official documents should come from the school system.
