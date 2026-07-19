<!-- doc-pair: project-index; lang: en; topics: start-here,student-guides,project-records,current-release-state -->

[繁體中文](README.md) | [English](README.en.md)

# Project documentation

Current production release: [`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

## Start here

This directory records migration, architecture, validation, release, and Overleaf evidence for the released NCKU thesis template. To write a thesis, start from `README.en.md` and `conf/README.en.md` inside the student package; root [`README.en.md`](../README.en.md) provides the project overview and download routes.

## Student guides

| Task | Document |
| --- | --- |
| Build and edit a thesis | [`thesis/README.en.md`](../thesis/README.en.md) |
| Enter student configuration | [`thesis/conf/README.en.md`](../thesis/conf/README.en.md) |
| Review NCKU college and department presets | [`thesis/template/style/ncku/README.en.md`](../thesis/template/style/ncku/README.en.md) |
| Migrate from 1.x to 2.x | [`v1-to-v2-migration.en.md`](v1-to-v2-migration.en.md) |
| Create an institution profile for students from other institutions | [`thesis/template/style/Customization.en.md`](../thesis/template/style/Customization.en.md) |
| Review version changes | [`CHANGELOG.md`](../CHANGELOG.md) |

Each complete guide uses one predominant language and links to its equivalent Traditional-Chinese or English page at the top. Documentation language, institution profile, cover language, degree, and content mode are independent settings.

## Project records

| Topic | Document |
| --- | --- |
| V2 architecture and compatibility boundary | [`features/v2-modernization.md`](features/v2-modernization.md) |
| Tests, output, and performance | [`features/validation-and-performance.md`](features/validation-and-performance.md) |
| Releases, downloads, and Overleaf | [`features/release-and-distribution.md`](features/release-and-distribution.md) |
| All shipped feature records | [`features/README.en.md`](features/README.en.md) |

Feature records preserve shipped architecture, validation results, and public state.

## Current release state

The template currently uses the V2 source line, XeLaTeX, and a direct `latexmk` student build. The latest immutable release is `v2.0.1.260719010734`; [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases/latest) is canonical for the latest production student package.

The existing Overleaf Gallery page remains public. The template's V2 update has been submitted for review; until Overleaf approves it and the public page is read back, that page does not represent the latest V2 package. See [`features/release-and-distribution.md`](features/release-and-distribution.md) for the detailed state.
