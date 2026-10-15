---
id: gaussian-conditioning
type: concept
fields: [bayesian, control-theory, linear-algebra]
fields_strong: [bayesian, control-theory, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]
generated_by: build_kg.py
---

# gaussian-conditioning

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (p. 356): closed-form conditional mean/covariance of a joint Gaussian, Lemma A.3 [new; work fields: control-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 199): formulas (6.66)–(6.67) for $p(x|y)$ in a joint Gaussian [new]

## Instances that use it

- [[gaussian-conditioning-example]] — Example 6.6: $p(x_1|x_2=-1)=\mathcal N(0.6,0.1)$ — from [[deisenroth-2020-mml/ch06-probability-p2]]
- [[em-mvn-missing-data]] — EM with Gaussian conditioning; imputation on $N=100$, $D=10$, 50% missing — from [[murphy-2023-pml2/ch06-optimization-p2]]

## Candidate bridges

- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] GP posterior mean/covariance ↔ multivariate normal conditioning (BDA §3.5): the formulas on p. 503 are Gaussian conditioning. — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → other:multivariate-normal-conditioning-bda)
