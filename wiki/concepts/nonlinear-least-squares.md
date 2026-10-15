---
id: nonlinear-least-squares
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch18-nonlinear]
generated_by: build_kg.py
---

# nonlinear-least-squares

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 448): minimize $\|f(x)\|^2$; condition $2Df(\hat x)^Tf(\hat x)=0$ [new]
- [[boyd-2018-vmls/ch18-nonlinear]] (p. 382): minimize $\|f(x)\|^2$ for a possibly non-affine $f:\mathbf R^n\to\mathbf R^m$ [new]

## Instances that use it

- [[boolean-least-squares]] — a constrained nonlinear least squares special case whose brute force method is not practical for $n$ larger than about 30 — from [[boyd-2018-vmls/app-appendices]]
- [[constrained-nonlinear-least-squares-kkt]] — KKT system $2Df^Tf+Dg^T\hat z=0$, $g=0$ — from [[boyd-2018-vmls/app-appendices]]

## Candidate bridges

- [same-math] IEKF update ↔ optimisation: Gauss–Newton for a nonlinear least-squares/MAP cost (the text states this equivalence, p. 121–122). — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → other:optimization)
- [same-math] IERTSS iteration ↔ nonlinear least squares: Gauss–Newton on the cost (13.17), solved by Kalman filter and smoother. — from [[sarkka-2023-bayesianfiltering/ch13-extended]] (control-theory → linear-algebra)
