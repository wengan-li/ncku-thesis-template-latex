<!-- doc-pair: project-index; lang: en; topics: start-here,student-guides,project-records,releases-and-downloads -->

[繁體中文](README.md) | [English](README.en.md)

# Project documentation

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
| Review version changes | [`CHANGELOG.en.md`](../CHANGELOG.en.md) |

Each complete guide uses one predominant language and links to its equivalent Traditional-Chinese or English page at the top. Documentation language, institution profile, cover language, degree, and content mode are independent settings.

## Project records

| Topic | Document |
| --- | --- |
| V2 architecture and compatibility boundary | [`features/v2-modernization.en.md`](features/v2-modernization.en.md) |
| Tests, output, and performance | [`features/validation-and-performance.en.md`](features/validation-and-performance.en.md) |
| Releases, downloads, and Overleaf | [`features/release-and-distribution.en.md`](features/release-and-distribution.en.md) |
| All shipped feature records | [`features/README.en.md`](features/README.en.md) |

Feature records preserve shipped architecture, validation results, and public state.

## Releases and downloads

The template uses XeLaTeX and a direct `latexmk` student build. Download production student packages and generated examples from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases); [`CHANGELOG.en.md`](../CHANGELOG.en.md) records the user-visible changes for each release.

The existing Overleaf Gallery page remains public. GitHub Releases and Overleaf publication are independent states; see [`features/release-and-distribution.en.md`](features/release-and-distribution.en.md) for the detailed record.
