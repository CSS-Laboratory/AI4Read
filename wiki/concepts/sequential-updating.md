---
id: sequential-updating
type: concept
fields: [bayesian, information-theory]
n_sources: 16
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch18-p, mackay-2003-information/ch28-model, mcelreath-2020-rethinking/ch02-small, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch12-who, mcgrayne-2011-theory/ch13-cold, mcgrayne-2011-theory/ch15-navy, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch08-gaussian-p1, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch29-state-p2]
raw_ids: [Sequential updating]
canon_spine: bayesian
generated_by: build_kg.py
---

# sequential-updating

## Canon spine entry

- **Sequential updating** (bayesian): today's posterior is tomorrow's prior; the order of data doesn't matter (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 9): use the previous posterior as the new prior
- [[gelman-2013-bda3/ch02-single]] (p. 42): the same posterior results from adding data one point at a time
- [[mcelreath-2020-rethinking/ch02-small]] (p. 31): each posterior becomes the next prior; order of data does not matter in this model, and updating can be reversed
- [[mcgrayne-2011-theory/ch01-causes]] (p. 8): each posterior becomes the prior of the next round
- [[mcgrayne-2011-theory/ch02-man]] (p. 23): each answer becomes the starting point for the next calculation
- [[mcgrayne-2011-theory/ch04-bayes]] (pp. 67, 80): add clues as they arrive and stop when evidence is enough
- [[mcgrayne-2011-theory/ch12-who]] (p. 157): each word's frequency improves the earlier estimate; the text says "one at a time"
- [[mcgrayne-2011-theory/ch13-cold]] (p. 171): keep updating odds as returns arrive
- [[mcgrayne-2011-theory/ch15-navy]] (p. 201): daily recomputation, with Bayes as the search's "group memory"
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 237, 249): continuous updating, as in RenTech's data stream and Bayesian filters
- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 361): each posterior becomes the next step's prior; constant work per step
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 672–677): online BNN inference where the previous posterior becomes the prior (EWC, EKF, ADF, VCL)
- [[murphy-2023-pml2/ch29-state-p2]] (p. 1008): today's posterior becomes tomorrow's prior (used for RLS)

### information-theory

- [[jaynes-2003-probability/ch08-sufficiency]] (p. 259): corresponds to chain consistency [as `Sequential updating`]
- [[jaynes-2003-probability/ch18-p]] (p. 557): the robot replaces (A_p|E) by (A_p|EF) and erases the old one
- [[mackay-2003-information/ch28-model]] (p. 353): the log evidence as a sum of on-line predictive terms (28.18)

## Candidate bridges

- [structural-analogy] Normal equations in row form (12.8) ↔ sequential updating of Gram sums (exercise 12.14 builds on it). — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → unspecified)
- [metaphor] Redundant information "drops out" (p. 369) ↔ bayesian: sequential updating with data that add nothing — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → bayesian)
- [structural-analogy] Submarine: product of conditional probabilities telescopes to log 1/P(location) (4.14) ↔ Bayesian: sequential updating, where the order of evidence does not change the final posterior. — from [[mackay-2003-information/ch04-source]] (information-theory → bayesian)
- [same-math] bit-by-bit match, ratio 2^r ↔ bayesian: sequential updating with likelihood ratios — odds multiply by the likelihood ratio. — from [[mackay-2003-information/ch12-hash]] (information-theory → bayesian)
- [structural-analogy] Adding $\log mA$ per match and subtracting for non-matches ↔ bayesian: sequential updating — independent observations contribute additive log-likelihood-ratio terms. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [structural-analogy] sum–product on a tree ↔ bayesian: sequential updating — local evidence is combined by multiplication. — from [[mackay-2003-information/ch26-exact]] (information-theory → bayesian)
- [structural-analogy] Stopping-rule irrelevance ↔ bayesian: sequential updating — the spies update after each toss, and only the data seen matter. — from [[mackay-2003-information/ch37-bayesian]] (information-theory → bayesian)
- [structural-analogy] Iterative message passing in turbo decoding ↔ bayesian: sequential updating — each trellis's output becomes the other's input, multiplied by the channel likelihood. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
- [same-math] Sequential analysis with stopping on enough evidence ↔ bayesian: sequential updating with a threshold on the posterior odds. — from [[mcgrayne-2011-theory/ch04-bayes]] (bayesian → bayesian)
- [structural-analogy] Interim monitoring allowed under Bayes ↔ sequential updating — current results can be used without a fixed stopping plan. — from [[mcgrayne-2011-theory/ch08-jerome]] (bayesian → unspecified)
- [structural-analogy] Updating election odds as returns arrive ↔ bayesian: sequential updating — each batch of returns revises earlier beliefs. — from [[mcgrayne-2011-theory/ch13-cold]] (bayesian → bayesian)
- [same-math] Kalman filter as derived from Bayes' rule (Aoki 1967) ↔ bayesian: sequential updating — the author says it can be derived directly from Bayes' rule (p. 205). — from [[mcgrayne-2011-theory/ch15-navy]] (bayesian → bayesian)
- [same-math] Bayes filter predict/update ↔ bayesian: sequential updating — yesterday's posterior is prior, then multiply by the likelihood. — from [[murphy-2023-pml2/ch08-gaussian-p1]] (bayesian → bayesian)
- [structural-analogy] Data tempering weight $p(y_t|y_{1:t-1},\theta)$ ↔ Bayesian canon: sequential updating — each datum's weight is its predictive probability under the current posterior. — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → bayesian)
- [metaphor] Catastrophic forgetting vs regularization to past posterior ↔ Sequential updating: yesterday's posterior as today's prior (the author says online Bayesian inference is of this type, p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] hidden state $z_t$ compressing the past ↔ sufficient statistic in sequential updating: both summarize history for predicting the next item. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → other)
- [same-math] RLS ↔ Bayesian: sequential updating of a Gaussian posterior for linear-regression weights; both are the same conjugate update. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → bayesian)
- [structural-analogy] Belief-state MDP in bandits ↔ sequential updating: today's posterior is tomorrow's prior, now used as the decision state. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → other)
- [structural-analogy] Bayes-adaptive MDP belief state ↔ bayesian: sequential updating, with the posterior predictive as transition model (p. 1149). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [metaphor] Front-door chaining of $P(t\mid s)$ and $P(c\mid do(t))$ ↔ sequential updating: composing two measured links to get an end-to-end quantity. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → other)
