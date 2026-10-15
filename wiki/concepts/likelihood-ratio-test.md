---
id: likelihood-ratio-test
type: concept
fields: [information-theory, complex-systems]
n_sources: 5
tiers: [deep, reference, core]
grounding: digests
sources: [clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2, cover-2006-elements/ch12-information-p2, jaynes-2003-probability/ch14-simple, polyanskiy-2025-information/ch16-neyman]
generated_by: build_kg.py
---

# likelihood-ratio-test

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch12-information-p2]] (p. 307): compare P₁(x)/P₂(x) with T; equals a difference of relative-entropy distances of the sample type [new]
- [[jaynes-2003-probability/ch14-simple]] (p. 433): compare $p(V|S_1)/p(V|S_0)$ with a threshold set by prior odds and losses; the quantity the optimum receiver computes; it gives all the information needed for Bayes decisions [new]
- [[polyanskiy-2025-information/ch16-neyman]] (p. 281, 284, 285): deterministic threshold test on the extended LLR $T$; optimal by the NP lemma when no randomization at the threshold is needed ($\lambda=0$), otherwise the optimal test randomizes there [new]

### complex-systems

- [[clauset-2009-powerlaw/main-p1]] (p. 19): compare two fitted models by $R$, the log likelihood ratio, with Vuong's $p$-value for its sign [new]
- [[clauset-2009-powerlaw/main-p2]] (pp. 37–38): a test of the sign of ℛ against a null of zero expected value. The p-value measures trust in the sign, not goodness of fit [new]

## Candidate bridges

- [structural-analogy] Likelihood-ratio test between non-nested models ↔ model selection in agent-based/many-model work — rival generative models compared on one data set. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
