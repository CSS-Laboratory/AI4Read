---
id: laplace-rule-of-succession
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 5
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch18-p, mackay-2003-information/ch03-more, mackay-2003-information/ch06-stream, murphy-2023-pml2/ch03-statistics-p1]
aliases: [laplace-rule]
generated_by: build_kg.py
---

# laplace-rule-of-succession

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `laplace-rule` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch06-elementary-p1]] (p. 155): $(r+1)/(n+2)$ from a uniform prior; equals the posterior mean of the unsampled red fraction [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch18-p]] (p. 563, p. 571): P(A|N_n) = (n+1)/(N+2) from a flat A_p density; for K hypotheses (n₁+1)/(N+K) [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 69): (N₁+1)/(N+2) under a uniform prior [new]

### information-theory

- [[mackay-2003-information/ch03-more]] (p. 52): $P(\texttt a|\mathbf s,F)=(F_a+1)/(F_a+F_b+2)$ from the uniform prior [alias `laplace-rule`; new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (p. 116): $P(\mathtt a)=(F_{\mathtt a}+1)/(F_{\mathtt a}+F_{\mathtt b}+2)$, the predictive probability from a uniform prior over the bias [alias `laplace-rule`; new; work fields: information-theory, bayesian]

## Instances that use it

- [[laplace-rule-of-succession]] — $(n+1)/(n+2)$ compared with corroboration $n/(n+2)$ — from [[popper-1959-logic/appviii-untitled]]

## Candidate bridges

- [same-math] Laplace's rule (3.16) ↔ bayesian: Beta–Binomial conjugate updating with a Beta(1,1) prior, posterior mean $(F_a+1)/(F+2)$. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
- [same-math] Laplace rule in the coder ↔ bayesian: posterior predictive of a Beta–Bernoulli model with a uniform prior — MacKay derives it from the uniform prior (p. 117). — from [[mackay-2003-information/ch06-stream]] (information-theory → bayesian)
