---
id: random-variable
type: concept
fields: [information-theory, linear-algebra, llm]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, prince-2023-udl/ch23-probability, stone-2022-information/ch02-entropy]
generated_by: build_kg.py
---

# random-variable

## Definitions in the sources

### information-theory

- [[stone-2022-information/ch02-entropy]] (p. 23): function mapping experiment outcomes to numeric outcome values [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 175): a function $X:\Omega\to\mathcal T$, not random and not a variable [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 449): an uncertain quantity, discrete or continuous, described by a distribution [new]

## Instances that use it

- [[two-dice-sum]] — sum of two dice as an example of a weighted sum of random variables — from [[markowitz-1952-portfolio/main]]

## Candidate bridges

- [same-math] Inverse-CDF sampling (D.3) ↔ simulation of any 1-D random variable — the same transformation. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [same-math] Cholesky sampling of a Gaussian with covariance $\Sigma=LL^\top$ ↔ probability (Chapter 6): linear transformation of random variables (as sketched on p. 115). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other)
- [structural-analogy] non-centred θ = μ + τη ↔ Variational inference: reparameterising a random variable as a deterministic transform of a fixed-distribution noise variable — similar form, different purpose. — from [[gelman-2013-bda3/appc-computation]] (bayesian → other)
- [same-math] Portfolio variance $\sum\sum\sigma_{ij}X_iX_j$ ↔ statistics: variance of a linear combination of random variables — the same formula. — from [[markowitz-1952-portfolio/main]] (economics-finance → other)
- [structural-analogy] Non-centered parameterization ↔ variational inference: reparameterizing a random variable as a deterministic transform of fixed noise (canon link; not stated in this unit). — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → other)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other)
- [same-math] $E[h(X)]=\sum p(x)h(x)$ ↔ statistics: expectation of a function of a random variable — entropy is the special case $h=\log(1/p)$. — from [[stone-2022-information/appd-probability]] (information-theory → other)
