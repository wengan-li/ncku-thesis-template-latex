# Draft and institutional watermark history and policy

Status: fixed and included in `v1.8.2.260715154703`

Checked: 2026-07-15

Scope: `(Draft)` / `(初稿)` cover markers, the `draftwatermark` text layer, and the bundled NCKU institutional-logo watermark

## Summary

The template has three independent mechanisms that were historically enabled together but must not be confused:

1. `\DisplayDraft` changes only the cover marker to `(Draft)` or `(初稿)`.
2. Loading the third-party `draftwatermark` package creates a diagonal `DRAFT` text layer unless its default `text=DRAFT` option is explicitly cleared. `\SetWatermarkText{...}` controls this layer.
3. `\UseWatermarkFigureStyle` registers the bundled `template/style/ncku/watermark-20160509_v2-a4.pdf` as a page background. The PDF asset itself contains only the pale institutional seal/logo; it does not contain the diagonal `DRAFT` text.

The three layers are independent. Disabling `\DisplayDraft` does not clear the package text or institutional logo; clearing the figure watermark does not change the cover marker or package text.

The safe maintained policy is now:

- normal StudentMode and teaching/example builds are final-ready by default: no Draft marker, no diagonal `DRAFT` text, and no institutional watermark;
- Draft-marker, text-watermark, and figure-watermark APIs remain available only as explicit opt-ins for writing/review, compatibility, or a current documented requirement;
- final/ETDS output must follow current university, library, and department instructions rather than historical template defaults;
- the Overleaf Gallery overlay continues to clear all three mechanisms as defence in depth.

## Historical evidence

### Draft marker

Commit `526b422b1b9333d4faa2ff37ba21683dc7cd9ca9` (`2015-07-24`, `Add the feature of 'Draft'`) introduced the Draft feature and immediately added an active `\DisplayDraft` line to the distributed `thesis/conf/conf.tex`.

The lower-level command state itself defaulted to off:

```tex
\newcommand{\VarCoverDisplayDraft}{0}
```

but the distributed configuration then opted in with:

```tex
\DisplayDraft
```

Therefore the API default and the actual out-of-box project behaved differently. From the feature's introduction through v1.8.1, a normal build showed `(Draft)` / `(初稿)` unless the student manually removed or commented the line. The teaching text described how to enable the feature but did not clearly say that final submission must keep it disabled.

### Institutional-logo watermark

Commit `9861434b` (`2016-09-11`, `Refactoring files to provide customization of different users`) placed an unconditional call in the generic watermark command module:

```tex
\UseWatermarkFigureStyle
```

The NCKU style also had its own call. By v1.6.0, the NCKU-style call had been commented out, matching the changelog intent to remove the internal-page watermark, but the generic unconditional call remained active. As a result, loading the template still registered the bundled NCKU logo watermark globally.

This left contradictory public surfaces:

- `CHANGELOG.md` says v1.6.0 removed the unnecessary NCKU internal-page watermark;
- `thesis/context/context.tex` and `thesis/example/context.tex` say the inner cover has no school logo;
- root `README.md` says the uploaded PDF should not contain an inserted watermark or security and explains that the school system applies its own processing;
- the implementation still enabled the bundled logo watermark by default.

Source inspection of v1.5.13, v1.6.0, and pre-fix `main` confirmed that the generic unconditional call survived all three states.

### Third-party diagonal `DRAFT` default

`thesis/template/configure.tex` loads the third-party `draftwatermark` package for the legacy/custom DOI text-watermark API. The package declares its text option with the default value `DRAFT`:

```tex
\DeclareStringOption[DRAFT]{text}
```

Merely loading the package therefore adds a diagonal `DRAFT` layer unless the template calls:

```tex
\SetWatermarkText{}
```

This layer is graphical in the rendered page and was not reliably exposed by `pdftotext`. It was discovered during post-fix pixel inspection after the cover marker and institutional-logo asset dependency had both been removed. The initial text/dependency assertions were therefore insufficient and were strengthened with direct package-state checks plus rendered-page inspection.

The bundled NCKU watermark PDF was rendered separately to identify provenance: it contains only the pale institutional seal/logo. The diagonal letters come from `draftwatermark`, not from the bundled PDF.

## Verified pre-fix behavior

The exact v1.8.1 student source and pre-fix `main` were built with XeLaTeX and rendered:

- StudentMode page 1 visibly contained all three layers: `(Draft)`, diagonal `DRAFT` text, and the pale institutional seal/logo;
- StudentMode page 2 retained both the diagonal `DRAFT` text and institutional logo behind the abstract;
- the full teaching build behaved the same way;
- this contradicted the final-submission guidance and the comments claiming no inner-cover logo.

The public Overleaf Gallery was not affected because its generated publication overlay explicitly set the Draft flag to zero, cleared the package text, cleared registered shipout watermarks, prevented helpers from adding them back, removed the bundled institutional watermark asset, and verified the rendered publication preview.

## Corrected default contract

After this fix:

```text
normal StudentMode             no marker, diagonal text, or institutional logo
normal teaching/example build no marker, diagonal text, or institutional logo
explicit \DisplayDraft         cover marker appears
explicit \SetWatermarkText     diagonal text layer appears
explicit figure watermark API institutional logo asset is loaded and rendered
Overleaf Gallery profile      remains clean by independent overlay
```

The public/customization APIs are preserved:

```tex
\DisplayDraft
\SetWatermarkText{...}
\UseWatermarkFigureStyle
\UseWatermarkTextStyle
\ClearWatermarkStyle
```

No API was renamed or removed. The change is limited to default activation and truthful documentation.

## Verification contract

The deterministic test gate must prove both sides:

1. default StudentMode and canonical cover text contain no `(Draft)` / `(初稿)` marker;
2. the internal `draftwatermark` text state is empty by default rather than the package's built-in `DRAFT` value;
3. default `.fls` dependency graphs do not include `watermark-20160509_v2-a4.pdf`;
4. an explicit opt-in fixture contains `(Draft)`, sets a non-empty diagonal text layer, and loads the institutional-logo asset;
5. final logs have no unresolved references/citations or rerun-required state;
6. cover and representative inner pages are rendered and visually inspected because graphical text can evade PDF text extraction;
7. Gallery packaging continues to exclude the institutional asset and reject Draft markers.

When these defaults change, lower-level tests are not enough: verify the exact student package and public-facing profile because configuration overlays can differ.

## Release and distribution boundary

Release `v1.8.1.260715130936` predates this fix and retains the legacy student-package defaults. Release `v1.8.2.260715154703` is the first immutable release whose student package uses the corrected final-ready defaults.

The v1.8.2 release must pass the full source, student package, examples package, and Gallery-profile gates plus public asset re-download verification. Updating the public Overleaf Gallery remains a separate owner action: edit and resubmit the original Overleaf project; source changes or a GitHub release do not update the Gallery automatically.

## Evidence locations

- `thesis/conf/conf.tex` — user-facing opt-ins and default guidance
- `thesis/template/command/cmd-cover.tex` — Draft flag default and cover marker
- `thesis/template/configure.tex` — `draftwatermark` package loading
- `thesis/template/command/cmd-watermark.tex` — text/figure watermark APIs and safe initialization
- `thesis/template/style/ncku/ncku.tex` — NCKU logo watermark definition
- `thesis/template/style/ncku/watermark-20160509_v2-a4.pdf` — bundled seal/logo-only asset
- `thesis/context/context.tex` — normal student document flow
- `scripts/overleaf/config/gallery.tex` — publication defence-in-depth overlay
- `scripts/overleaf/package-and-verify.sh` — Gallery asset/text verification
- `tests/student-mode.tex` — default student path and empty package-text assertion
- `tests/draft-watermark-opt-in.tex` — explicit opt-in behavior
- `CHANGELOG.md` v1.6.0 and historical Draft entries
- root `README.md` ETDS upload guidance
