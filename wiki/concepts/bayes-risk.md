---
id: bayes-risk
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch34-decision, polyanskiy-2025-information/ch31-basics]
generated_by: build_kg.py
---

# bayes-risk

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch34-decision]] (p. 1106): expected frequentist risk averaged over a prior $\pi(h)$; minimiser is a Bayes estimator [new]

### information-theory

- [[polyanskiy-2025-information/ch31-basics]] (p. 562): $R^*_\pi=\inf_{\hat\theta}R_\pi(\hat\theta)$, average-case limit under prior $\pi$ [new]

## Instances that use it

- [[gaussian-location-model]] — Bayes risk $s/(sn+1)$, exactly met by Bayesian HCR/CR bounds — from [[polyanskiy-2025-information/ch32-classical]]

## Candidate bridges

- [structural-analogy] Bayes risk with Gaussian prior and $s\to\infty$ ↔ I-MMSE: Bayes risk under quadratic loss is the MMSE (p. 562). — from [[polyanskiy-2025-information/ch31-basics]] (information-theory → other)
