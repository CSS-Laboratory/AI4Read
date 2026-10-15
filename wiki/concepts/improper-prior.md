---
id: improper-prior
type: concept
fields: [information-theory, bayesian]
n_sources: 6
tiers: [reference, core, deep]
grounding: digests
sources: [gelman-2013-bda3/ch02-single, griffiths-2006-optimal/main, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch15-paradoxes, mackay-2003-information/ch24-exact]
generated_by: build_kg.py
---

# improper-prior

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 165–166): $d\theta/[\theta(1-\theta)]$ as limit of the concave prior, handled as a limit of ratios [new]
- [[jaynes-2003-probability/ch06-elementary-p2]] (p. 182): a prior that cannot be normalized, can be used directly when the integrals converge; in almost all cases it can be approached as a limit of proper priors [new]
- [[jaynes-2003-probability/ch15-paradoxes]] (pp. 476, 487): meaningful only as a limit of proper priors; the Jeffreys prior $\eta^{-1}$ is the case relevant to a scale parameter [new]
- [[mackay-2003-information/ch24-exact]] (p. 319): a prior that cannot be normalized, e.g. P(μ) = const. [new]

### bayesian

- [[gelman-2013-bda3/ch02-single]] (p. 52): prior with infinite integral; may still give a proper posterior, which must be checked [new]
- [[griffiths-2006-optimal/main]] (p. 773): a prior whose integral diverges; for $\gamma\le1$ the posterior is still proper [new]

## Candidate bridges

- [structural-analogy] Passage to the limit last ↔ Bayesian: improper prior as the limit of proper priors — the same ordering discipline in a different setting. — from [[jaynes-2003-probability/ch15-paradoxes]] (information-theory → bayesian)
