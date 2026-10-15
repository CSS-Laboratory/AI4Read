---
id: weight-of-evidence
type: concept
fields: [bayesian, information-theory, analytic-philosophy]
fields_strong: [bayesian, information-theory, analytic-philosophy]
n_sources: 4
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/ch18-p, mackay-2003-information/ch18-crosswords, murphy-2023-pml2/ch05-information-p1, popper-1959-logic/appix-untitled]
generated_by: build_kg.py
---

# weight-of-evidence

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch18-p]] (pp. 572–573): the intuitive notion is bound up with the sharpness of the A_p density; evidence with a much sharper density dominates [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch05-information-p1]] (p. 225): $\log p(D)/q(D)$; KL is its expectation under $P$ [new; work fields: bayesian, information-theory]

### analytic-philosophy

- [[popper-1959-logic/appix-untitled]] (pp. 424, 428): Keynes's and Good's notion, here measured by $E$, $C$ or their absolute values [new]

### information-theory

- [[mackay-2003-information/ch18-crosswords]] (pp. 264–265): log likelihood ratio (log odds), in bans or decibans [new; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Weight of evidence as sharpness of the A_p density ↔ information-theory: Fisher information as curvature of log-likelihood — narrower density means more information — from [[jaynes-2003-probability/ch18-p]] (bayesian → information-theory)
- [same-math] Weight of evidence $\log\frac{P(D|\mathcal H_1)}{P(D|\mathcal H_2)}$ ↔ bayesian: log Bayes factor / posterior log odds minus prior log odds — the same likelihood ratio, expressed in decibans. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [same-math] Turing's bans and decibans ↔ bayesian: log odds / weight of evidence, where evidence adds in log space. — from [[mcgrayne-2011-theory/ch04-bayes]] (bayesian → bayesian)
- [structural-analogy] Expected weight of evidence ↔ Bayes factor / log posterior odds (§5.1.3.3). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
