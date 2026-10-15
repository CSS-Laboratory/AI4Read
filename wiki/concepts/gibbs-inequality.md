---
id: gibbs-inequality
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch02-probability, mackay-2003-information/ch05-symbol]
generated_by: build_kg.py
---

# gibbs-inequality

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch02-probability]] (p. 34): $D_{\rm KL}(P\|Q)\ge0$, with equality only if $P=Q$ [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch05-symbol]] (p. 97): $\sum p_i\log1/q_i\ge\sum p_i\log1/p_i$, used in the lower-bound proof [new; work fields: information-theory, bayesian]

## Candidate bridges

- [same-math] Integral in (8.51) ↔ information-theory: minus the KL divergence $D(p_{\theta_0}\|p_\theta)$; non-positivity is Gibbs' inequality. The unit does not name KL. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [same-math] Gibbs inequality (9.72) ↔ information-theory: non-negativity of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (bayesian → information-theory)
- [same-math] $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$ ↔ information-theory: relative entropy and Gibbs' inequality. — from [[mackay-2003-information/ch08-dependent]] (information-theory → information-theory)
