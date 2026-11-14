<!-- doc-pair: writing-equations-and-theorems; lang: en; topics: equations,theorems -->

[繁體中文](equations-and-theorems.md) | [English](equations-and-theorems.en.md)

# Equations, theorems and proofs

## Equations and references

Inside a chapter, pair `\EquationBegin{label}` with `\EquationEnd`. The optional label uses braces, not square brackets; omitting it still produces a numbered equation. An aligned environment is already present. Use & to align and a double backslash to break lines; do not wrap another math environment around it. `\RefEquation` prints the number alone and `\RefEquationB` adds parentheses. Use ordinary `$...$` for inline mathematics.

<!-- student-snippet: equations-theorems -->
```latex
\EquationBegin{eq:pilot-identity}
  x &= x
\EquationEnd
See Equation \RefEquationB{eq:pilot-identity}.
\InsertTheorem[title={Identity},label={thm:pilot-identity}]{For every $x$, $x=x$.}
\InsertProof{Both sides denote the same object.}
See Theorem \RefTo{thm:pilot-identity}.
```

## Theorems and proofs

The example uses `\InsertTheorem[title={title},label={label}]{content}`. Title and label default to empty. Public wrappers such as `\InsertLemma` and `\InsertDefinition` accept the same options; this page demonstrates the theorem route only. `\InsertProof{content}` has one required argument and adds its own end-of-proof symbol. Existing configuration owns numbering and headings; do not reset thesis-wide counters to add a theorem. For an unknown option, check spelling. For `??`, check the label and complete the build again. Researchers must supply proof content; the illustrative identity is not a research conclusion.
