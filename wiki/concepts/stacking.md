---
id: stacking
type: concept
fields: [bayesian]
n_sources: 3
tiers: [core]
grounding: digests
sources: [gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p2, gelman-2020-workflow/main-p3]
generated_by: build_kg.py
---

# stacking

## Definitions in the sources

### bayesian

- [[gelman-2020-workflow/main-p1]] (p. 25): combine chains or models with cross-validation weights; approximate, not necessarily equivalent to full Bayes [new]
- [[gelman-2020-workflow/main-p2]] (p. 44): combine models with weights minimizing cross-validation error; preferred to Bayesian model averaging here [new]
- [[gelman-2020-workflow/main-p3]] (p. 60): reweighting chain draws; treated as discarding chains stuck at local modes [new]

## Candidate bridges

- [structural-analogy] Stacking of chains/models with cross-validation weights ↔ model averaging in predictive ensembles — weights are chosen by predictive performance, not by posterior probability (p. 25). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
- [structural-analogy] Stacking the four latest frames to handle states not fully observable from one image ↔ control-theory: observability and state estimation — use history to recover hidden state (p. 438). — from [[sutton-2018-rl/ch16-applications]] (control-theory → control-theory)
