---
id: mixture-of-gaussians
type: concept
fields: [information-theory, linear-algebra]
n_sources: 3
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, mackay-2003-information/ch21-exact, mackay-2003-information/ch22-maximum]
generated_by: build_kg.py
---

# mixture-of-gaussians

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch21-exact]] (p. 298): density that is a weighted sum of Gaussians with weights summing to 1 [new]
- [[mackay-2003-information/ch22-maximum]] (p. 302): density as weighted sum of Gaussians with unknown class labels [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 202): weighted sum of densities (not of variables); moments in Theorem 6.12 [new]

## Instances that use it

- [[nade-rnade-made]] — neural, mixture-of-Gaussians and masked-network conditionals — from [[murphy-2023-pml2/ch22-autoregressive]]
- [[mixture-of-gaussians]] — discrete latent variable giving a multi-modal Pr(x) — from [[prince-2023-udl/ch17-variational]]

## Candidate bridges

- [structural-analogy] Mixture-of-Gaussians resolution as an ill-posed inverse problem ↔ Bayesian: hierarchical models and regularizing priors — prior information selects among many consistent decompositions. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → bayesian)
- [same-math] Student-$t$ as a scale mixture of Gaussians ↔ heavy-tailed robust priors: marginal over unknown variance gives the $t$ (pp. 89, 100). — from [[murphy-2023-pml2/ch03-statistics-p2]] (bayesian → other)
