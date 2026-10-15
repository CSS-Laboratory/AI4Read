---
id: minimax-risk
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch31-basics, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch35-entropic]
generated_by: build_kg.py
---

# minimax-risk

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch31-basics]] (p. 563): $\inf_{\hat\theta}\sup_\theta R_\theta(\hat\theta)$, worst-case limit [new]
- [[polyanskiy-2025-information/ch32-classical]] (pp. 575, 577): $\inf_{\hat\theta}\sup_\theta$ of expected loss; bounded below by the Bayes risk for any prior [new]
- [[polyanskiy-2025-information/ch35-entropic]] (p. 603): $\inf_{\hat P}\sup_\theta\mathbb E_\theta\,\mathrm{loss}$; here $R^*_{\rm KL}(n)$ [new]

## Instances that use it

- [[blind-guess-randomization]] — $\theta\in\{0,1\}$, no data: minimax risk $\tfrac12$ needs a randomized guess — from [[polyanskiy-2025-information/ch31-basics]]
- [[erased-observation-tensorization]] — $X=\theta Z$: product minimax risk strictly below the sum — from [[polyanskiy-2025-information/ch31-basics]]
- [[gaussian-location-model]] — unconstrained, ball, sparse and non-quadratic-loss minimax risk by MIM — from [[polyanskiy-2025-information/ch33-mutual]]
