# Overleaf distribution decision

Status: Gallery template published; V2 update submitted through the original project and pending update review

Checked: 2026-07-17

## Decision

Maintain two reproducible Overleaf profiles without changing the canonical teaching/student source:

1. `just overleaf <version>` produces the editable StudentMode import package;
2. `just overleaf-gallery <version>` produces the public Gallery preview package.

The canonical student configuration is final-ready by default: the cover Draft marker, diagonal `draftwatermark` text layer, and institutional logo watermark are explicit opt-ins. The Gallery profile independently enforces the same clean publication state as defence in depth, excludes unused watermark/oral-example PDFs, keeps dummy metadata, and retains XeLaTeX and the same thesis layout/API surface. The source configuration is never edited and restored by hand for publication.

Overleaf's current policy generally lists non-official university thesis templates as unsuitable, but it also reserves discretion to accept templates outside its listed categories and already hosts older community NCKU templates. The repository therefore submitted an accurately labelled community template for moderation rather than claiming institutional endorsement or assuming automatic acceptance.

The submitted public title is:

```text
National Cheng Kung University Thesis and Dissertation Template — XeLaTeX
```

The description identifies the project as unofficial/community-maintained, links to NCKU guidance and the source repository, and instructs students to verify current university and departmental requirements.

The Overleaf-specific ZIPs remain maintainer/import artifacts, not additional GitHub Release assets. The public GitHub Release contract remains exactly two versioned ZIP files.

## Why the complete student ZIP is not the Overleaf import artifact

The complete `thesis/` tree currently contains more than Overleaf's 180-file per-upload limit and includes the 271-page teaching corpus. It also has both `thesis.tex` and `cover.tex`, whereas Overleaf recommends one output document per project and a root-level main document.

The generated Overleaf package contains only:

- `README.md`;
- `conf/`;
- `context/`;
- `template/`;
- root-level `thesis.tex`.

Generation also disables the repository's active `\ExampleMode` line so the imported project opens in StudentMode. The package excludes `example/` and `cover.tex` but does not alter the committed teaching source.

## Verified workflows

Run from a clean worktree:

```bash
just overleaf <version>
just overleaf-gallery <version>
```

Both commands:

1. export committed `HEAD:thesis` rather than uncommitted files;
2. remove the teaching corpus and second main document;
3. change the packaged `conf/conf.tex` to default to StudentMode;
4. move the active `\documentclass` declaration into root `thesis.tex`, allowing Overleaf to detect the correct main document rather than nested `template/configure.tex`;
5. create a root-level ZIP and check required files plus official upload/resource limits;
6. extract the ZIP into a fresh temporary directory;
7. run a cold `latexmk -xelatex` build of `thesis.tex`;
8. reject unresolved references/citations and missing PDF output;
9. record the local cold-build duration and SHA-256.

The Gallery command additionally copies `scripts/overleaf/config/gallery.tex` into the package, loads it after canonical `conf/conf.tex`, rejects Draft markers in extracted PDF text, removes the unused logo/oral-example PDFs, and verifies that the overlay and exclusions are present. This avoids hand-editing and restoring the student configuration.

`tests/student-mode.tex` separately proves that StudentMode has no `example/` dependency. This caught and corrected a prior student-path leak from `context/context.tex` to `example/nomenclature/nomenclature.tex`.

### Upload/import failures caught on 2026-07-12

Two real Overleaf uploads exposed requirements that a local XeLaTeX build alone did not prove:

1. A newly uploaded ZIP defaulted to pdfLaTeX and correctly hit the template's XeLaTeX engine gate. Overleaf users must select XeLaTeX explicitly.
2. Overleaf auto-detected nested `template/configure.tex` as the main document because root `thesis.tex` did not directly contain `\documentclass`. Relative paths then failed with a misleading missing `template/command/command.tex` error even though that file was present in the ZIP. The generator now creates an unambiguous root main document and verifies that the nested configure file has no active document-class declaration.

The clean StudentMode starter also removed three inherited diagnostics seen during the authenticated import: an empty bibliography, an unused figure-caption setup, and an underfull nomenclature paragraph. The starter now includes one replaceable sample citation, uses caption's starred type-specific setup, and uses explicit vertical space instead of an empty paragraph.

### Verified Gallery result on 2026-07-12

`just overleaf-gallery v1.8.0.260712123948` produced:

- `ncku-thesis-template-latex-overleaf-gallery-v1.8.0.260712123948.zip`;
- 64 files;
- 298,715 bytes of editable material;
- a 4,681,568-byte ZIP;
- SHA-256 `178b8872ec70461b0acdeda2f9d02ed7cf272c3dc0c5a26d7859435f3adcc5c6`;
- an 11-page A4 StudentMode PDF;
- a 3.95-second cold local XeLaTeX/latexmk build;
- no teaching-example dependency, unresolved reference/citation state, Draft marker, institutional logo watermark, or excluded institutional PDF.

The cover, abstract, and acknowledgements pages were rendered to images and visually checked as clean white final-state pages without Draft text or a logo watermark. The exact ZIP was uploaded to a new Overleaf project, configured for XeLaTeX, root `thesis.tex`, and the latest TeX Live, and compiled cleanly in the authenticated Overleaf runtime.

The Overleaf import artifacts remain under ignored `build/overleaf/`; they are not GitHub Release assets or permanent public URLs.

## Required Overleaf settings

After ZIP upload/import:

- main document: `thesis.tex` at project root;
- compiler: XeLaTeX (Overleaf otherwise commonly defaults to pdfLaTeX);
- TeX Live: latest available version; the project declares LaTeX2e format `2020-10-01` or newer and recommends TeX Live 2021 or newer;
- editing mode: Code Editor is the safer default for this macro-heavy template.

Overleaf's API can encode the required engine and main document:

```text
https://www.overleaf.com/docs?snip_uri=<URL-ENCODED-PERMANENT-ZIP-URL>&engine=xelatex&main_document=thesis.tex
```

The ZIP URL must be publicly reachable over HTTP or HTTPS. Do not point this link at a mutable branch archive; use an immutable versioned artifact whose SHA-256 was verified.

## Official limits checked by the verifier

As checked on 2026-07-12:

- maximum files per upload: 180;
- maximum files per project: 2,000;
- maximum individual upload: 50 MB;
- maximum editable project data: 7 MB;
- maximum individual editable text file: 2 MB;
- free-plan compile timeout: 10 seconds;
- premium-plan compile timeout: 240 seconds.

## Licensing and asset provenance

Overleaf requires clear license information for Gallery content and recommends LPPL for templates. This repository currently declares CC BY-NC-SA 4.0; the submission must not silently claim a different license without agreement from the relevant copyright holders.

A project-level license does not prove redistribution rights for every bundled third-party asset. The Gallery profile removes the institutional logo watermark and example oral PDFs, but it still includes bundled Times-family and KaiU font files because the verified layout currently depends on them and no adjacent font-license files were found during this review. Font provenance and redistribution permission remain a possible moderation issue. Do not claim that the repository license relicenses those fonts; if Overleaf requests a licensing correction, replace them only through a separately approved, visual-regression-tested Gallery change rather than silently changing the canonical thesis output.

## Publication and update ownership

The Gallery project was submitted on 2026-07-12 and approved/published by Overleaf on 2026-07-15. The public template is:

<https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn>

Owner-confirmed on 2026-07-17: the V2 update has been submitted through that original Overleaf project and is pending Gallery update review. Until Overleaf approves the update and the public template is independently read back, GitHub Releases remains the canonical source for the latest V2 student package. Do not describe the public Gallery copy as V2 merely because the update has been submitted.

Operational rules:

- preserve the original submitted Overleaf project; it is the update identity if the template is approved;
- do not open a different project to submit future updates;
- changes to the original project do not replace a published Gallery version until the same project is resubmitted and Overleaf approves the update;
- keep dummy data and the unofficial/community-maintained description;
- retain the official NCKU guidance link without implying institutional endorsement;
- treat moderation requests about similarity, licensing, fonts, or institutional status as unresolved gates rather than working around them in a replacement submission.

The approved public template was independently re-opened and verified with XeLaTeX, `thesis.tex` as the main document, TeX Live 2025, and a clean publication preview. Future changes must update the source generator first, rebuild and verify the Gallery ZIP, then update and resubmit the original Overleaf project; editing GitHub alone does not update the Gallery.

## Official sources

- Uploading a project and upload limits: <https://docs.overleaf.com/managing-projects-and-files/uploading-a-project>
- Compiler and TeX Live selection: <https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler>
- Main document requirements: <https://docs.overleaf.com/getting-started/recompiling-your-project/the-main-document>
- Plan and timeout limits: <https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits>
- Gallery eligibility and update rules: <https://docs.overleaf.com/templates/submitting-to-the-overleaf-template-gallery>
- Alternatives for unofficial thesis templates: <https://docs.overleaf.com/templates/submitting-to-the-overleaf-template-gallery/alternatives-to-templates>
- Licensing and copyright: <https://docs.overleaf.com/templates/licensing-and-copyright>
- Open in Overleaf API: <https://www.overleaf.com/devs>
