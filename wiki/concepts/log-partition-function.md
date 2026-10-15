---
id: log-partition-function
type: concept
fields: [bayesian, linear-algebra]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, murphy-2023-pml2/ch02-probability-p2]
generated_by: build_kg.py
---

# log-partition-function

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch02-probability-p2]] (p. 34, 39): $A(\boldsymbol\eta)=\log Z(\boldsymbol\eta)$; its derivatives give moments of $\mathcal T$ (new)

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 211): $A(\theta)$, the normalizer in the exponent [new]

## Candidate bridges

- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → other)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity. — from [[mackay-2003-information/ch31-ising]] (information-theory → information-theory)
