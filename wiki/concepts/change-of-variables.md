---
id: change-of-variables
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, murphy-2023-pml2/ch02-probability-p3]
generated_by: build_kg.py
---

# change-of-variables

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (p. 44): $p_y(y)=p_x(f^{-1}(y))|\det J_{f^{-1}}(y)|$ for bijections [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 219): $f(y)=f_x(U^{-1}(y))\,|\det \partial U^{-1}/\partial y|$ [new]

## Candidate bridges

- [same-math] Jacobian determinant ↔ probability: change-of-variables density factor. The text defers this to Section 6.7 (p. 152). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → other:probability)
- [structural-analogy] MAP basis dependence (22.29) ↔ Bayesian: Jacobian of a density under change of variables — densities transform with $|\partial\theta/\partial u|$, so maxima move. — from [[mackay-2003-information/ch22-maximum]] (information-theory → bayesian)
- [same-math] Flat prior on ln σ ↔ probability theory: change-of-variables rule for densities, with $|\partial\sigma/\partial\ln\sigma|=\sigma$ — a flat density in ln σ is a $1/\sigma$ density in σ (p. 320). — from [[mackay-2003-information/ch24-exact]] (information-theory → other:probability)
- [structural-analogy] RJMCMC change of measure ↔ change of variables with Jacobian determinant in probability densities. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → unspecified)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other:probability)
- [structural-analogy] Encoding with the cdf to get a uniform output ↔ statistics: probability integral transform — same change-of-variables idea. — from [[stone-2022-information/ch07-channel]] (information-theory → other:statistics)
- [same-math] Waterwheel amplitude equations (9) ↔ Lorenz equations: the text states the change of variables exists (Exercise 9.1.3, not printed here). — from [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (complex-systems → complex-systems)
- [same-math] Jacobian determinant as area/volume scaling ↔ change-of-variables for densities under a map: both use $|\det\mathbf J|$. — from [[strogatz-2024-nonlinear/ch12-strange]] (complex-systems → other:change-of-variables-for)
