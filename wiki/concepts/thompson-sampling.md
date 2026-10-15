---
id: thompson-sampling
type: concept
fields: [bayesian, decision-game-theory]
fields_strong: [bayesian, decision-game-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch34-decision]
generated_by: build_kg.py
---

# thompson-sampling

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 302): sample a surrogate and greedily maximize the sample [new]
- [[murphy-2023-pml2/ch34-decision]] (p. 1126): act greedily on one posterior sample; plays each arm with probability of being optimal [new; work fields: bayesian, decision-game-theory]

## Candidate bridges

- [structural-analogy] Thompson sampling for BayesOpt ↔ bandits: posterior sampling over arms generalized to continuous inputs. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → control-theory)
- [same-math] Thompson sampling's one-sample estimate of $p_a$ ↔ Monte Carlo integration: the integral of an indicator under the posterior is estimated by a sample. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → bayesian)
- [same-math] Thompson sampling with a Dirichlet transition posterior ↔ bayesian: conjugate Dirichlet–categorical updating and posterior sampling (p. 1149). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
