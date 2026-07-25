# Shared release example-PDF manifest, sourced by package-examples.sh and
# verify-assets.sh so packaging and verification cannot drift apart.
# Index N of example_asset_sources is packaged as index N of
# example_asset_destinations and verified against index N of
# example_asset_pages (exact count, or +N meaning at-least-N).

example_asset_sources=(
  example-cover.pdf
  example-thesis-chi.pdf
  example-thesis-eng.pdf
  example-thesis-full.pdf
  example-legacy-defense-certificate-master.pdf
  example-legacy-defense-certificate-phd.pdf
)

example_asset_destinations=(
  cover.pdf
  thesis-chi.pdf
  thesis-eng.pdf
  thesis-full.pdf
  defense-certificate-master.pdf
  defense-certificate-phd.pdf
)

example_asset_pages=(
  2
  +10
  +10
  +100
  6
  10
)
