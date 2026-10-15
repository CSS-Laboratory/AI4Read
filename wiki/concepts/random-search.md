---
id: random-search
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p2, recht-2019-tour/main]
generated_by: build_kg.py
---

# random-search

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 306): uniform sampling over $\mathcal X$; a baseline that beat grid search for hyperparameters in [BB12] [new]

### control-theory

- [[recht-2019-tour/main]] (p. 10): REINFORCE with $p_0(z-\vartheta)$, read as finite-difference gradient ascent [new]

## Instances that use it

- [[ant-foraging-pheromone-trails]] — random search, trail reinforcement and evaporation — from [[mitchell-2009-guidedtour/ch12-information]]
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm — from [[recht-2019-tour/main]]
- [[mujoco-humanoid-random-search]] — linear policies with whitening match the state of the art; high variance across seeds — from [[recht-2019-tour/main]]
- [[rastrigin-inverted-pendulum]] — probably the earliest random-search proposal, motivated by an RL problem — from [[recht-2019-tour/main]]

## Candidate bridges

- [structural-analogy] Pheromone-weighted trail choice ↔ codelet resource allocation by promise: positive feedback plus residual random search. — from [[mitchell-2009-guidedtour/ch13-make]] (complex-systems → other)
- [structural-analogy] Simulated annealing (varying $T$ in (1)) ↔ optimisation: random search with decreasing randomness; also SAEM, which reduces simulation noise toward EM. — from [[robert-2011-mcmc/main]] (bayesian → other)
