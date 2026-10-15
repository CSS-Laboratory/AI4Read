---
id: pontryagin-maximum-principle
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 8
n_works: 1
tiers: [deep]
grounding: digests
sources: [liberzon-2012-calculus/ch01-introduction, liberzon-2012-calculus/ch02-calculus, liberzon-2012-calculus/ch03-calculus, liberzon-2012-calculus/ch04-maximum-p1, liberzon-2012-calculus/ch04-maximum-p2, liberzon-2012-calculus/ch05-hamilton, liberzon-2012-calculus/ch06-linear, liberzon-2012-calculus/ch07-advanced]
raw_ids: [Pontryagin maximum principle, pontryagin maximum principle]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# pontryagin-maximum-principle

## Canon spine entry

- **Pontryagin maximum principle** (control-theory): necessary conditions for optimality using costates (shadow prices) along the trajectory (grad)

## Definitions in the sources

### control-theory

- [[liberzon-2012-calculus/ch01-introduction]] (p. 3): only named here as one of two key developments, treated later
- [[liberzon-2012-calculus/ch02-calculus]] (pp. 37, 45): only previewed: $H$ is maximised in the velocity and $\lambda^*(\cdot)$ corresponds to the costate
- [[liberzon-2012-calculus/ch03-calculus]] (pp. 77, 79): only previewed; Hamiltonian maximisation conjectured here
- [[liberzon-2012-calculus/ch04-maximum-p1]] (pp. 81–83): necessary conditions for optimal control: canonical equations, $H$ maximized over $U$, $H\equiv0$ in free-time problems, transversality at a surface target
- [[liberzon-2012-calculus/ch04-maximum-p2]] (p. 102): necessary conditions via H maximization, costate, transversality; here extended and applied
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 135): open-loop necessary condition via costate; compared with HJB in 5.2 [as `Pontryagin maximum principle`]
- [[liberzon-2012-calculus/ch06-linear]] (p. 146): gives the unique candidate control with $p^*=-2Px^*$
- [[liberzon-2012-calculus/ch07-advanced]] (p. 165, 177): here recast with covector costate; also hybrid version [as `pontryagin maximum principle`]

## Candidate bridges

- [structural-analogy] $K_i(t)$ switching functions and the mixed line ↔ control-theory: costates, bang-bang control and singular arcs in the Pontryagin maximum principle — the sign of $K_i-K_j$ selects the control; equality allows an intermediate control. — from [[bellman-1957-dp/ch08-viii]] (control-theory → control-theory)
- [structural-analogy] Hamiltonian stationary in $y'$ (2.33) ↔ control theory: Pontryagin maximum principle — the text says the stationary point becomes a maximum there — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
