# Sample repository migration record

Status: in progress

Checked: 2026-07-12

## Intent

Retire the separately maintained sample repository only after the main repository can generate equivalent, current examples from the exact release tag:

```text
https://github.com/wengan-li/ncku-thesis-template-latex-sample
```

The source template remains in this repository. Generated PDFs and the downloadable project ZIP belong to GitHub Releases, not the Git source tree.

## Source relationship

The two repositories have independent histories; the sample repository is not a GitHub fork of the source repository.

At the checked state, the sample repository contains:

```text
Default branch tip: d92659c13c34ca80efa00291d9839436cd99e58a
Commits:            43
Tags:               19
Reachable objects:  180
Latest sample:      v1.7.0
```

## Current sample artifact provenance

Current files at sample commit `d92659c13c34ca80efa00291d9839436cd99e58a`:

| File | SHA-256 | Classification |
|---|---|---|
| `cover.pdf` | `1eeecba5ce0f11ee2946d7d3ec650bf5186bc4a0856ff7644f9c4217ad169aa8` | Generated example; replace with same-tag release asset |
| `thesis (chi).pdf` | `74cd16db48e200ae8061e04f33bb75d9707e3460d42526eb4a55efb0355df796` | Generated example; replace with same-tag release asset |
| `thesis (eng).pdf` | `46ea454d921ee0d1d491e0ee521c5b280eb1b4ae83480ec4ad975067cc4fa1e6` | Generated example; replace with same-tag release asset |
| `thesis (demo).pdf` | `e7f7e9d25d55454b6d63d6ca5dbbbbfe3580a0e07923ad3d71b8efa4b62da9ee` | Generated example; replace with same-tag release asset |
| `defense-certificate (matser).pdf` | `03774ea661bfbed2e35d70cb8153a76b9ddda74c0c399baa0af99e90c54ca103` | Generated legacy example; filename contains a historical typo |
| `defense-certificate (phd).pdf` | `327bb6971ec6df6aa27fb185bf4ac208a59fd6bb7a28dd354f5a33b87db33b` | Generated legacy example |
| `defense-certificate-ncku-std.pdf` | `02596307b9fedcfe1414e218809931a61a27b3452efb6bb3214604c853dceaba` | Historical external school-system example; do not regenerate or imply ownership |
| `defense-certificate-ncku-std_origial.pdf` | `c913bee692bad75a5dfaf85b1c641107d8a9ee0dcfb1ec2e1e51aee180a87e4d` | Historical external school-system example; filename contains a historical typo |

## Replacement release assets

`just release` builds and verifies:

```text
ncku-thesis-template-latex.zip
example-cover.pdf
example-thesis-chi.pdf
example-thesis-eng.pdf
example-thesis-full.pdf
example-legacy-defense-certificate-master.pdf
example-legacy-defense-certificate-phd.pdf
```

The two historical external school-system PDFs are not normal generated release assets. Current students should obtain the current official certificate from the school system and follow current university/department guidance.

## Deletion gate

Do not delete the sample repository until all conditions are true:

- [x] Current artifact hashes and classifications are recorded.
- [x] Main source can locally build and verify all replacement generated assets.
- [x] Main README no longer treats the sample repository as the current source.
- [x] A tagged v1.8 release has built and published every replacement asset.
- [x] Published PDF page counts, A4 dimensions, extracted text, and expected variants are verified.
- [x] ZIP extraction starts at the intended project folder layer and passes `just test`.
- [ ] Old public links have a migration/redirect period or the owner explicitly accepts that deletion breaks them.
- [ ] The owner explicitly accepts the effect of deleting a repository with existing stars and forks.
- [ ] Required GitHub Admin permission is available.

Archiving with a redirect notice for at least one release cycle is safer than immediate deletion. If deletion remains the owner decision, the unchecked gates still apply.
