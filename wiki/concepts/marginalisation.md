---
id: marginalisation
type: concept
fields: [information-theory]
n_sources: 3
tiers: [core]
grounding: digests
sources: [stone-2022-information/appf-rules, stone-2022-information/ch04-noisy, stone-2022-information/ch06-mutual]
generated_by: build_kg.py
---

# marginalisation

## Definitions in the sources

### information-theory

- [[stone-2022-information/appf-rules]] (p. 261–262): summing or integrating a joint distribution over one variable [new]
- [[stone-2022-information/ch04-noisy]] (p. 85): summing a joint distribution over one variable to get the marginal [new]
- [[stone-2022-information/ch06-mutual]] (p. 138): integrating a joint density over one variable to get a marginal [new]

## Candidate bridges

- [same-math] Quasi-likelihood mixture over good/bad labels ↔ bayesian: marginal likelihood averaged over a latent discrete variable — the sum over labellings is a marginalisation. — from [[jaynes-2003-probability/ch21-outliers]] (information-theory → bayesian)
- [structural-analogy] Marginalisation (H.21) ↔ entropy: marginals $p(x_i)$ from the joint give $H(X)$ from $p(X,Y)$. — from [[stone-2022-information/appf-rules]] (information-theory → other)
