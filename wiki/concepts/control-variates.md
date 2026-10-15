---
id: control-variates
type: concept
fields: [bayesian]
n_sources: 3
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch11-monte]
generated_by: build_kg.py
---

# control-variates

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 274): subtract a correlated baseline with known mean to lower variance [new]
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 455): subtract a zero-mean correlated baseline to cut gradient variance [new]
- [[murphy-2023-pml2/ch11-monte]] (p. 495–496): subtract a correlated, known-mean baseline term; variance factor $1-\rho^2$ at the optimal $c$ [new]

## Instances that use it

- [[control-variate-1-over-1-plus-x]] — se 0.0037 → 0.0007 — from [[murphy-2023-pml2/ch11-monte]]
- [[antithetic-uniform]] — $y'=1-y$ with same se as control variates — from [[murphy-2023-pml2/ch11-monte]]

## Candidate bridges

- [structural-analogy] Pinto–Neal correction using $Q$ ↔ control variates: correct an estimate with a correlated one whose true value is known (p. 420). — from [[mackay-2003-information/ch32-exact]] (information-theory → control-theory)
- [structural-analogy] Control variate/baseline ↔ Monte Carlo variance reduction in estimating expectations (p. 275) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → unspecified)
- [structural-analogy] Control variate with $c^*$ ↔ regression: $c^*=-\mathrm{Cov}/\mathbb V$ is a regression slope on the baseline. — from [[murphy-2023-pml2/ch11-monte]] (bayesian → other)
- [same-math] SGLD-CV / SVRG gradient (12.124) ↔ Monte Carlo variance reduction: a control variate subtracts a correlated term of known mean. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → other)
- [structural-analogy] Control variate in (7.13) ↔ statistics: variance reduction by adding a zero-mean term — the same trick of subtracting a correlated term with known expectation. — from [[sutton-2018-rl/ch07-n]] (control-theory → other)
