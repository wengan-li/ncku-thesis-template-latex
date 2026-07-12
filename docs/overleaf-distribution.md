# Overleaf distribution decision

Status: verified package workflow; public Gallery submission rejected by policy

Checked: 2026-07-12

## Decision

Do not submit this project to the Overleaf Template Gallery while it remains an unofficial university thesis template.

Overleaf's current Gallery policy explicitly lists non-official university-based templates, including thesis templates, as not accepted. It requires an official university template to link to the university's own style guidelines or submission instructions. This repository must continue to describe itself as community-maintained and unofficial unless National Cheng Kung University provides explicit institutional ownership or endorsement.

Use these supported alternatives instead:

1. keep the versioned student ZIP as the complete offline source package;
2. generate and verify a smaller StudentMode-only Overleaf import package with `just overleaf <version>`;
3. after asset provenance is confirmed and a permanent public ZIP URL exists, expose an **Open in Overleaf** link using Overleaf's documented API;
4. retain direct ZIP upload instructions as a fallback.

The Overleaf-specific ZIP is a maintainer verification artifact, not a third GitHub Release asset. The public Release contract remains exactly two versioned ZIP files.

## Why the complete student ZIP is not the Overleaf import artifact

The complete `thesis/` tree currently contains more than Overleaf's 180-file per-upload limit and includes the 271-page teaching corpus. It also has both `thesis.tex` and `cover.tex`, whereas Overleaf recommends one output document per project and a root-level main document.

The generated Overleaf package contains only:

- `README.md`;
- `conf/`;
- `context/`;
- `template/`;
- root-level `thesis.tex`.

Generation also disables the repository's active `\ExampleMode` line so the imported project opens in StudentMode. The package excludes `example/` and `cover.tex` but does not alter the committed teaching source.

## Verified workflow

Run from a clean worktree:

```bash
just overleaf <version>
```

The command:

1. exports committed `HEAD:thesis` rather than uncommitted files;
2. removes the teaching corpus and second main document;
3. changes the packaged `conf/conf.tex` to default to StudentMode;
4. creates `build/overleaf/ncku-thesis-template-latex-overleaf-<version>.zip` with files at the ZIP root;
5. checks required files and official upload/resource limits;
6. extracts the ZIP into a fresh temporary directory;
7. runs a cold `latexmk -xelatex` build of `thesis.tex`;
8. rejects unresolved references/citations and missing PDF output;
9. records the local cold-build duration and SHA-256.

`tests/student-mode.tex` separately proves that StudentMode has no `example/` dependency. This caught and corrected a prior student-path leak from `context/context.tex` to `example/nomenclature/nomenclature.tex`.

A local build under ten seconds is useful evidence but is not proof of Overleaf free-plan performance because Overleaf infrastructure differs. An authenticated Overleaf import/recompile remains the final runtime check before publishing an Open-in-Overleaf link.

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

Overleaf requires clear license information for Gallery content and recommends LPPL for templates. This repository currently declares CC BY-NC-SA 4.0, which Overleaf says may be accepted only at its discretion; however, Gallery eligibility is already blocked by the unofficial-university-template rule.

More importantly, a project-level license does not prove redistribution rights for every bundled third-party asset. The package includes bundled Times-family and KaiU font files and institutional graphics, but no adjacent font-license files were found during this review. Before promoting a permanent public Open-in-Overleaf artifact, record provenance and redistribution permission for each bundled font/logo or replace it through a separately approved, visual-regression-tested change. Do not silently assume the repository license relicenses third-party assets.

## Publication and update ownership

If NCKU later endorses an official Gallery submission:

- the description must link to official NCKU style/submission instructions;
- the template must contain dummy data, not personal information;
- the original Overleaf project used for submission becomes the update identity;
- future updates must edit and resubmit that same project;
- changes do not replace the Gallery version until Overleaf approves them;
- ownership of the Overleaf project and the responsible institutional maintainer must be recorded outside student-facing documentation.

Until that endorsement exists, use the documented API/direct-upload alternative and label the project unofficial.

## Official sources

- Uploading a project and upload limits: <https://docs.overleaf.com/managing-projects-and-files/uploading-a-project>
- Compiler and TeX Live selection: <https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler>
- Main document requirements: <https://docs.overleaf.com/getting-started/recompiling-your-project/the-main-document>
- Plan and timeout limits: <https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits>
- Gallery eligibility and update rules: <https://docs.overleaf.com/templates/submitting-to-the-overleaf-template-gallery>
- Alternatives for unofficial thesis templates: <https://docs.overleaf.com/templates/submitting-to-the-overleaf-template-gallery/alternatives-to-templates>
- Licensing and copyright: <https://docs.overleaf.com/templates/licensing-and-copyright>
- Open in Overleaf API: <https://www.overleaf.com/devs>
