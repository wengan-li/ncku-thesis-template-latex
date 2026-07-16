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

The custom ZIP is a student-ready download containing only the tracked contents of `thesis/`. Its filename includes the complete release tag as `ncku-thesis-template-latex-<version>.zip`; for example, tag `v1.8.0.260712074004` produces `ncku-thesis-template-latex-v1.8.0.260712074004.zip`. It expands to one stable `ncku-thesis-template-latex/` directory with `thesis.tex`, `conf/`, `context/`, `example/`, and `template/` directly inside. The version belongs in the archive filename, not the extracted project directory, so editor paths and student instructions remain stable. The ZIP intentionally excludes repository tooling and tests because GitHub already provides automatic full-source archives.

The promoted release contains exactly two custom packages:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

The examples package expands to one stable `ncku-thesis-template-latex-examples/` directory containing `README.md`, `cover.pdf`, `thesis-chi.pdf`, `thesis-eng.pdf`, `thesis-full.pdf`, `defense-certificate-master.pdf`, and `defense-certificate-phd.pdf`. The outer archive carries the version, so the files inside do not repeat an `example-` prefix or version suffix. Its README records the version and source commit, explains each PDF, links back to Releases for the editable student project, and states that the generated defense-certificate PDFs are unofficial demonstrations/regression outputs rather than school-system documents.

## Release implementation lessons

The release system has three explicit layers:

1. `scripts/release/*.tex` and `thesis/thesis.tex` define the document cases. Each case selects its own language, degree, committee-size, or cover behavior in TeX rather than relying on a maintainer to edit and restore `conf.tex` by hand.
2. `just release` is the single local/CI orchestration command. It runs the required test gate, builds every case with XeLaTeX through `latexmk`, creates the student ZIP from `HEAD:thesis`, verifies that its regular-file list exactly matches the complete tracked `HEAD:thesis` tree, bundles the six verified PDFs plus a public README into the examples ZIP, and verifies both package allowlists. The focused test gate also removes the packaged migration guide from a temporary copy and requires the exact-tree checker to fail. Loose PDFs remain build intermediates and are not promoted.
3. `.github/workflows/release.yml` supplies the reproducible TeX environment and promotes only the workflow artifact produced by the successful build job. The workflow must not duplicate the case logic.

GitHub Actions portability details include:

- the TeX container must mark `$GITHUB_WORKSPACE` as a Git safe directory before `git status` or `git archive`;
- values written to the runner's `$GITHUB_ENV` are not automatically visible inside `xu-cheng/texlive-action`; interpolate the resolved version into the action's `run` input and assert the exact host-side artifact paths before upload;
- a promotion job without a checkout must set `GH_REPO=${{ github.repository }}` so `gh release` does not try to discover the repository from `.git`.

The custom packages and GitHub's automatic source archives have different purposes:

- `ncku-thesis-template-latex-<version>.zip` is for students and contains only the tracked contents of `thesis/`, placed directly under one stable `ncku-thesis-template-latex/` directory;
- `ncku-thesis-template-latex-examples-<version>.zip` is a same-revision preview bundle containing the six generated and verified PDFs under one stable directory;
- GitHub's automatic Source code archives are for contributors who need the full repository, CI, tests, scripts, and documentation.

A release is not considered verified merely because the workflow is green. Download the public assets again, confirm the exact two-package allowlist, extract both ZIPs, compare every bundled example PDF with the verified build output, require the student ZIP file list to equal `HEAD:thesis` exactly (including the migration guide, v1 adapter, and all profile files), confirm that repository tooling and a redundant `thesis/` layer are absent, verify the pinned v1 student-owned files by SHA-256/size, and compile the downloaded `thesis.tex` directly with XeLaTeX/`latexmk`.

If a newly published release fails this contract and has not been announced as stable, publish and verify a corrected immutable timestamp tag first, then remove the superseded release and tag. Do not move an existing tag to a different commit.

The two generated defense-certificate files use clear public names inside the examples package, while its README states that they are unofficial template demonstrations and regression outputs. Normal thesis example PDFs do not embed generated defense certificates; current official documents should come from the school system.
