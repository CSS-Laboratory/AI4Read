---
id: correlation-coefficient
type: concept
fields: [decision-game-theory, bayesian, information-theory, linear-algebra]
n_sources: 5
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch03-norm, kahneman-2011-thinking/ch17-regression, kahneman-2011-thinking/ch19-illusion, pearl-2018-bookofwhy/ch02-buccaneers, stone-2022-information/ch07-channel]
generated_by: build_kg.py
---

# correlation-coefficient

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/ch17-regression]] (pdf 177): 0 to 1 here; the relative weight of factors two measures share [new]
- [[kahneman-2011-thinking/ch19-illusion]] (pdf 200): strength of a relation, 0 to 1, as the share of shared determining factors [new]

### bayesian

- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 65–66): Pearson's formula for the rescaled regression slope; 1 means exact prediction, 0 means no better than guessing; blind to causal direction [new]

### information-theory

- [[stone-2022-information/ch07-channel]] (p. 164): $\rho$ of Eq. 7.43 [new]

### linear-algebra

- [[boyd-2018-vmls/ch03-norm]] (p. 60): cosine of the angle between de-meaned vectors; ρ = uᵀv/n [new]

## Candidate bridges

- [structural-analogy] Cauchy–Schwarz ⇒ cos θ ∈ [−1,1] ↔ statistics: correlation coefficient lies in [−1,1] — the same inequality bounds both. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → other)
- [same-math] Correlation coefficient ρ = cos∠(ã, b̃) ↔ cosine similarity of centred data vectors — the same formula, applied to mean-removed vectors. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → unspecified)
- [structural-analogy] I(X;Y) = −½ log(1−ρ²) for Gaussians ↔ statistics: correlation coefficient — both measure dependence, but I is bijection-invariant (p. 48). — from [[polyanskiy-2025-information/ch04-mutual]] (information-theory → other)
- [same-math] $\rho=\sqrt{1-2^{-2I}}$ for Gaussians ↔ statistics: correlation coefficient — the same bivariate Gaussian quantity expressed two ways. — from [[stone-2022-information/ch07-channel]] (information-theory → other)
