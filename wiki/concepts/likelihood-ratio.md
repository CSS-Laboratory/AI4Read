---
id: likelihood-ratio
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch03-more, pearl-2018-bookofwhy/ch03-evidence]
generated_by: build_kg.py
---

# likelihood-ratio

## Definitions in the sources

### bayesian

- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 103): $P(T\mid D)/P(T)$, the factor that multiplies the prior (3.2) [new]

### information-theory

- [[mackay-2003-information/ch03-more]] (p. 55): $P(D|\mathcal H_1)/P(D|\mathcal H_2)$, the data's contribution to the posterior odds [new; work fields: information-theory, bayesian]

## Instances that use it

- [[blood-evidence]] — likelihood ratio 0.83 for Oliver, 50 for Alberto; general result $(n_O/N)/p_O$ — from [[mackay-2003-information/ch03-more]]
- [[phone-number-busy-signal]] — likelihood ratio of 100–1000 from a busy signal — from [[mackay-2003-information/ch03-more]]
- [[euro-coin-spin]] — 140 and 141 heads in 250 spins; p-values vs. likelihood ratios — from [[mackay-2003-information/ch03-more]]
- [[gaussian-channel-likelihood-ratio]] — $\exp(2xy_n/\sigma^2)$ — from [[mackay-2003-information/ch25-exact]]

## Candidate bridges

- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:statistics)
- [structural-analogy] "Partial" evaluation of Winograd completions ↔ likelihood-ratio comparison between two hypotheses — the choice is made by comparing probabilities of the same data under two conditions. — from [[brown-2020-gpt3/main-p3]] (llm → unspecified)
- [structural-analogy] Likelihood-ratio test between non-nested models ↔ model selection in agent-based/many-model work — rival generative models compared on one data set. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [same-math] posterior odds = prior odds × likelihood ratio ↔ Bayes' theorem in HS form (e.g. medical-test base rates): the same rule on a different scale. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [same-math] Evidence in db (log-likelihood ratio) ↔ information-theory: difference of surprisals $-\log P(D|\overline H)+\log P(D|H)$ (change of base and factor 10) — the same quantity. — from [[jaynes-2003-probability/ch04-elementary]] (bayesian → information-theory)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [same-math] Evidence in db, $10\log_{10}$ odds ↔ information-theory: log-likelihood ratio in bits (change of log base). — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [same-math] Likelihood-ratio threshold test (14.34) ↔ bayesian: posterior odds = prior odds × likelihood ratio, thresholded at loss ratio — literally the same rule (14.54). — from [[jaynes-2003-probability/ch14-simple]] (bayesian → bayesian)
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → bayesian)
- [same-math] Bayes's rule with prior and likelihood ratio ↔ Bayesian statistics generally: posterior odds = prior odds × likelihood ratio (our added step reproduces the author's 3% → 11% example). — from [[kahneman-2011-thinking/ch14-tom]] (decision-game-theory → bayesian)
- [same-math] Base rate plus witness reliability ↔ probability: Bayes' rule with prior 0.15 and likelihood ratio 4:1 gives 0.12/0.29. — from [[kahneman-2011-thinking/ch16-causes]] (decision-game-theory → other:probability)
- [structural-analogy] Majority vote as likelihood ratio γ^(votes) ↔ bayesian: independent observations multiply likelihood ratios (evidence accumulation). — from [[mackay-2003-information/ch01-introduction]] (information-theory → bayesian)
- [same-math] log posterior-ratio = log likelihood-ratio + log prior-ratio, (2.51) ↔ bayesian: the logistic (sigmoid) form of Ex. 2.17 is the inverse of log-odds — same algebra. — from [[mackay-2003-information/ch02-probability]] (information-theory → bayesian)
- [same-math] bit-by-bit match, ratio 2^r ↔ bayesian: sequential updating with likelihood ratios — odds multiply by the likelihood ratio. — from [[mackay-2003-information/ch12-hash]] (information-theory → bayesian)
- [same-math] Weight of evidence $\log\frac{P(D|\mathcal H_1)}{P(D|\mathcal H_2)}$ ↔ bayesian: log Bayes factor / posterior log odds minus prior log odds — the same likelihood ratio, expressed in decibans. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [structural-analogy] Adding $\log mA$ per match and subtracting for non-matches ↔ bayesian: sequential updating — independent observations contribute additive log-likelihood-ratio terms. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [same-math] DRE trick via Bayes' rule ↔ Bayes' theorem — posterior odds times prior odds correction gives the likelihood ratio. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
- [structural-analogy] Insensitivity to prior probability ↔ Bayesian updating: the judge acts as if the likelihood ratio alone fixed the posterior odds. — from [[tversky-1974-heuristics/main]] (decision-game-theory → bayesian)
- [structural-analogy] Concept selection by exponentially shrinking likelihood ratios $\exp(n\,r_n)$ ↔ Bayesian model comparison: the posterior concentrates on the best-fitting hypothesis as data accumulate. — from [[xie-2022-icl/main]] (llm → bayesian)
