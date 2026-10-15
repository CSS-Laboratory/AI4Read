---
id: lasso
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, gelman-2013-bda3/ch14-introduction]
generated_by: build_kg.py
---

# lasso

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch14-introduction]] (p. 368): posterior mode under a double-exponential prior; can set coefficients exactly to zero [new]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 303, 316): L1 regularization; equivalent to a Laplace prior; promotes sparsity [new]

## Instances that use it

- [[flow-cytometry-protein-network]] — graphical lasso on phosphorylation data from 11 proteins, λ varied — from [[murphy-2023-pml2/ch30-graph]]

## Candidate bridges

- [structural-analogy] Lasso's exact zeros from prior peak plus mode summary ↔ sparsity-inducing penalties in machine learning: penalty = −log prior. — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → llm)
- [structural-analogy] prior as regularization ↔ penalties in ridge, lasso, splines: all trade sensitivity for stability, as the authors say (p. 13) — from [[gelman-2013-philosophy/main]] (bayesian → other:penalties-in-ridge-lasso)
- [structural-analogy] Shrinkage of rare-word scores ↔ statistics: Lasso-type regularization — the chapter links MNIR's Gamma-Laplace prior to Lasso. — from [[grimmer-2022-textasdata/ch11-discriminating]] (political-science → other:statistics)
- [same-math] Lasso/ridge penalties ↔ Regression: regularized least squares — the same loss plus penalty form (Table 19.1). — from [[grimmer-2022-textasdata/ch19-classifying]] (political-science → other:statistics)
- [structural-analogy] Lasso selecting predictive words that are not necessarily confounders ↔ regression: omitted-variable bias — selecting controls by outcome fit alone can miss treatment-related confounders — from [[grimmer-2022-textasdata/ch27-text]] (political-science → other:statistics)
- [structural-analogy] Lasso/ridge penalty (p. 243) ↔ Bayesian inference: priors that pull coefficients toward zero — both stabilize estimates by trading variance against bias. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [same-math] Sparse coding MAP objective (28.160) ↔ Regularized regression: lasso, Gaussian noise with $\ell_1$ penalty (p. 977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → other:statistics)
- [structural-analogy] λ controlling graph sparsity in graphical lasso ↔ regularization strength in shrinkage/penalized estimation — a single parameter trades fit against simplicity. — from [[murphy-2023-pml2/ch30-graph]] (bayesian → unspecified)
