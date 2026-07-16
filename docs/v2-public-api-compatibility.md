# V1 Public API Compatibility in V2

V2 changes ownership and internals, not the availability of existing helpers.
Every explicitly declared command and environment captured before v2 work is
preserved throughout the 2.x line.

## Machine-Checked Contract

The committed baseline is:

```text
tests/v1-public-api.json
```

It contains the command/environment name, argument signature, and historical
definition path for 612 entries. The path is inventory context; compatibility
requires the name and argument shape, so implementations may move behind an
adapter.

Run the gate with:

```bash
python3 scripts/test/check-v1-api.py
```

It is also part of `just test` and `just ci`.

The baseline must not be regenerated after v2 implementation starts merely to
make a deletion pass. A deliberate future removal requires an owner decision
for a later major version and a migration record.

## Runtime Project Migration Contract

The API baseline proves declaration and argument-shape availability; it does not
claim that all 612 helpers have been individually behavior-tested. Runtime
migration coverage is separate:

```text
tests/v1-project-migration.json
scripts/test/check-v1-project-migration.py
```

The manifest pins 18 student-owned project files (296,726 bytes) to the immutable
`v1.8.2.260715154703` release at commit
`2c9557a74983023bba7a8f0cf233e1eb812edec7`. It covers the root entry point,
student configuration/content, bibliography data, and oral-certificate assets
as a byte-for-byte source-integrity contract.

Runtime coverage is intentionally split. The canonical test builds the exact v1
entry/configuration through the current v2 compatibility adapter, base contract,
and NCKU profile, then verifies the 271-page A4 output and legacy sentinels. The
StudentMode test separately asserts its active content inputs from `.fls` and all
three bibliography databases from `.blg`. Manifest files disabled by the v1
configuration remain source-pinned without being misreported as runtime-loaded.

Run the source half directly with:

```bash
python3 scripts/test/check-v1-project-migration.py
```

The complete source-plus-runtime gate is part of `just test` and `just ci`.

## Compatibility Classes

| Class | V2 treatment |
| --- | --- |
| Documented/user-facing helper | Keep name and arguments; delegate internally when useful. |
| Style-extension helper | Keep as a protected extension API for institution profiles. |
| Legacy/deprecated helper | Keep through 2.x; emit a bounded migration warning only when safe. |
| Proven bug | Keep the API, correct behavior, add a fixture, document the change. |
| Internal state macro captured by the conservative manifest | Keep an alias during 2.x even if native v2 code stops using it. |

Because v1 did not formally mark private macros, the baseline is deliberately
conservative. This prevents a cleanup from silently breaking real student
projects or non-NCKU forks.

## Architecture Rule

```text
v1 command/environment
        -> compatibility adapter when needed
        -> v2 mechanism/state
        -> selected template/style profile policy
        -> existing renderer/output
```

Profiles must not change public command arity. Institution policy should be
implemented through profile hooks or resolved state rather than by redefining
public setters.

## Implemented Adapter Boundary

The v2 command facade loads `template/compat/v1.tex`. The adapter preserves the
historical college/department preset commands and old source paths, while the
institution-owned data now lives in:

```text
template/style/ncku/college.tex
template/style/ncku/department.tex
```

A custom profile therefore keeps the complete v1 command surface but does not
load NCKU geometry, date hooks, or watermark assets. Removing the adapter or
regenerating the baseline is not an acceptable 2.x cleanup.

Public date setters now call profile policy hooks:

```text
SetOralDate    -> ApplyOralDatePolicy
SetCoverDate   -> ApplyCoverDatePolicy
SetOralChiDate -> ApplyOralChiYearPolicy
Chinese cover  -> profile cover-prefix/year display getters
```

Profiles override the hooks/getters, not setter signatures or raw metadata
storage. Generic Chinese dates remain Gregorian; the NCKU profile explicitly
selects Taiwan-year rendering.

## Behavior Corrections

Compatibility does not preserve verified defects. Each correction must include:

1. a focused fixture that fails against the old behavior;
2. the smallest source correction;
3. unchanged public name and argument shape;
4. an entry in `thesis/MIGRATION-1.x-TO-2.x.md`;
5. integration proof that unrelated NCKU output remains intact.
