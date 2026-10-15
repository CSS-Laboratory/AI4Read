---
id: constrained-least-squares
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch16-constrained, boyd-2018-vmls/ch17-constrained]
generated_by: build_kg.py
---

# constrained-least-squares

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch16-constrained]] (p. 339): minimize $\|Ax-b\|^2$ subject to linear equalities $Cx=d$ [new]
- [[boyd-2018-vmls/ch17-constrained]] (p. 360, 367): least squares with linear equality constraints, solved via a KKT system; every problem in this chapter is of this form [new]

## Candidate bridges

- [structural-analogy] KKT conditions ↔ the KKT linear system of constrained least squares — in the linear case, $\nabla h+Dg^T\hat z=0$ and $g=0$ become linear equations (this unit does not state it). — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → unspecified)
- [structural-analogy] control/estimation duality ↔ optimization: both are the same stacked constrained least squares, with inputs chosen (control) or inputs unknown (estimation) — the text itself calls this duality (p. 373). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other)
