---
id: hamiltonian
type: concept
fields: [control-theory]
n_sources: 2
tiers: [deep]
grounding: digests
sources: [liberzon-2012-calculus/ch02-calculus, liberzon-2012-calculus/ch04-maximum-p1]
generated_by: build_kg.py
---

# hamiltonian

## Definitions in the sources

### control-theory

- [[liberzon-2012-calculus/ch02-calculus]] (pp. 34, 36–37, 40): $H=p\cdot y'-L$; conserved when $L$ has no $x$; equals total energy in mechanics; stationary in $y'$ along an optimal curve [new]
- [[liberzon-2012-calculus/ch04-maximum-p1]] (pp. 81, 86): $H=\langle p,f\rangle+p_0L$, equivalently an inner product in $\mathbb R^{n+1}$ [new]

## Candidate bridges

- [structural-analogy] HMC's energy $-\log p(\theta)-\log p(\phi)$ conserved along a trajectory ↔ physics: Hamiltonian dynamics conserve total energy — the chapter says HMC imitates this, with the accept step correcting discretization error. — from [[gelman-2013-bda3/ch12-computationally]] (bayesian → other)
- [structural-analogy] Hamiltonian stationary in $y'$ (2.33) ↔ control theory: Pontryagin maximum principle — the text says the stationary point becomes a maximum there — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
- [same-math] Hamiltonian vector field flow (7.8) ↔ classical mechanics (Sec. 2.4): Hamilton's canonical equations — same equations, now read as a symplectic flow. — from [[liberzon-2012-calculus/ch07-advanced]] (control-theory → other)
