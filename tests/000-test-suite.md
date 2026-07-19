# Test suite layout

The `tests/` directory uses three-digit sparse prefixes so source fixtures sort by
execution concern while semantic `just` recipe and output job names remain stable.
All test files stay directly under `tests/`; do not add a second directory layer.

| Range | Group | Contents |
| --- | --- | --- |
| `000–099` | Suite documentation | This index and future suite-level contracts |
| `100–199` | Compatibility and core gates | V1 manifests, engine gate, dates, sectioning, helpers, deprecated commands |
| `200–299` | Numbering | Numbering contracts, family behavior, unknown-key failures |
| `300–399` | References | Reference and bibliography contracts |
| `400–499` | Floats | Figure, multi-figure, table, caption, and label contracts |
| `500–599` | Theorems | Theorem routes, styles, counters, and negative diagnostics |
| `600–699` | Profiles and policy | Custom institution profile, committee, and oral-date state |
| `700–799` | Metadata and fonts | PDF metadata, font files/options/CJK, and keywords |
| `800–899` | Student output | StudentMode and explicit Draft/watermark behavior |
| `900–999` | Historical references | Standalone investigation inputs; not automatic `just test` entrypoints |

## Naming rules

- Every file uses `<three-digit>-<descriptive-name>.<extension>`.
- Use the lowest unused number in the owning range; leave gaps when a group needs
  a related fixture later.
- Keep semantic `just` recipe names and build job names unnumbered. Numbers organize
  source inventory; they are not part of the public command or artifact contract.
- Update every script, document, and `justfile` path in the same change as a rename.
- Run `python3 scripts/test/check-test-layout.py` and `just test` after layout changes.

The `900` range is documented in
[`900-reference-fixtures.md`](900-reference-fixtures.md).
