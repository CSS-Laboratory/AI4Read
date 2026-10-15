---
id: laplace-rule
type: concept
fields: [information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch03-more, mackay-2003-information/ch06-stream]
generated_by: build_kg.py
---

# laplace-rule

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch03-more]] (p. 52): $P(\texttt a|\mathbf s,F)=(F_a+1)/(F_a+F_b+2)$ from the uniform prior [new]
- [[mackay-2003-information/ch06-stream]] (p. 116): $P(\mathtt a)=(F_{\mathtt a}+1)/(F_{\mathtt a}+F_{\mathtt b}+2)$, the predictive probability from a uniform prior over the bias [new]

## Instances that use it

- [[urn-inversion]] — hypergeometric urn with unknown $(N,R)$; Laplace's rule — from [[jaynes-2003-probability/ch06-elementary-p1]]
- [[bent-coin]] — posterior for the bias, Laplace's rule and model comparison with $p_a=1/6$ — from [[mackay-2003-information/ch03-more]]
- [[bernoulli-class-redundancy]] — Bernoulli class: $\mathcal R_n^*=\frac12\log n+O(1)$, KT and Laplace rules — from [[polyanskiy-2025-information/ch15-universal]]
- [[laplace-rule-of-succession]] — $(n+1)/(n+2)$ compared with corroboration $n/(n+2)$ — from [[popper-1959-logic/appviii-untitled]]

## Candidate bridges

- [same-math] Laplace's rule (3.16) ↔ bayesian: Beta–Binomial conjugate updating with a Beta(1,1) prior, posterior mean $(F_a+1)/(F+2)$. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
- [same-math] Laplace rule in the coder ↔ bayesian: posterior predictive of a Beta–Bernoulli model with a uniform prior — MacKay derives it from the uniform prior (p. 117). — from [[mackay-2003-information/ch06-stream]] (information-theory → bayesian)
