---
id: affine-function
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch08-linear]
generated_by: build_kg.py
---

# affine-function

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch02-linear]] (p. 32): linear plus a constant, $a^Tx+b$; restricted superposition holds when $\alpha+\beta=1$ (linear functions satisfy it for any $\alpha,\beta$) [new]
- [[boyd-2018-vmls/ch08-linear]] (pp. 149–150): $f(x)=Ax+b$, with unique $A,b$; linear only if $b=0$ [new]

## Candidate bridges

- [structural-analogy] "$n+1$ measurements fix an affine function" ↔ system identification / calibration of a sensor from reference inputs. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → unspecified)
- [same-math] Pareto line $w=w^0+\rho v$ ↔ affine combinations: the solution of a linear KKT system with a right-hand side affine in a parameter is an affine function of that parameter (p. 365). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other:affine-combinations)
