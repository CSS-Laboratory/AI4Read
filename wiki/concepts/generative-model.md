---
id: generative-model
type: concept
fields: [bayesian, llm]
n_sources: 5
tiers: [reference, core]
grounding: digests
sources: [gelman-2020-workflow/main-p1, murphy-2023-pml2/ch20-generative, prince-2023-udl/ch01-introduction, prince-2023-udl/ch14-unsupervised, tenenbaum-2011-grow/main]
generated_by: build_kg.py
---

# generative-model

## Definitions in the sources

### bayesian

- [[gelman-2020-workflow/main-p1]] (p. 11): a joint distribution of data and parameters; needed for simulation and checking though not for inference, which needs only the likelihood [new]
- [[murphy-2023-pml2/ch20-generative]] (p. 773): joint distribution $p(\boldsymbol x)$, or $p(\boldsymbol x|\boldsymbol c)$ if conditional [new]
- [[tenenbaum-2011-grow/main]] (p. 1280): probabilistic mental model of the causal processes and latent variables behind observations [new]

### llm

- [[prince-2023-udl/ch01-introduction]] (p. 7): model that synthesizes new examples statistically indistinguishable from the training data [new]
- [[prince-2023-udl/ch14-unsupervised]] (p. 270): model that can synthesise new examples, e.g. by sampling $\mathbf{z}$ and mapping to $\mathbf{x}$ [new]

## Instances that use it

- [[binomial-vs-negative-binomial-sampling]] — same likelihood for θ, different generative models and predictive checks — from [[gelman-2020-workflow/main-p1]]
- [[transformer-decoder-as-autoregressive-generator]] — probabilistic generative model without latent variables — from [[prince-2023-udl/ch14-unsupervised]]

## Candidate bridges

- [structural-analogy] Likelihood-ratio test between non-nested models ↔ model selection in agent-based/many-model work — rival generative models compared on one data set. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [structural-analogy] g-formula simulation of $(Y^{\bar a},\bar L^{\bar a})$ and Monte Carlo of Technical Point 21.9 ↔ Bayesian computation: ancestral sampling from a sequential generative model, drawing each $L_k$ given the history set by the strategy. — from [[hernan-2020-whatif/ch21-g]] (bayesian → bayesian)
- [structural-analogy] Amortized inference network ↔ rational analysis: a learned procedure approximately inverts the generative model of the environment. — from [[murphy-2023-pml2/ch21-variational]] (bayesian → other)
- [metaphor] "$Y$ listens to $X$" ↔ conditional dependence in a generative model: parents determine children's distributions. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → other)
- [metaphor] Searle's lookup-table cheat vs compact causal diagram ↔ Bayesian model: a small generative model, not a table of all data. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → bayesian)
- [structural-analogy] ToMnet vs BIRL ↔ statistics: bias/variance trade-off between a fixed generative model and a flexible learner (pdf 4) — from [[rabinowitz-2018-machine-tom/main]] (theory-of-mind → other)
