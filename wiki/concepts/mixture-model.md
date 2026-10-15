---
id: mixture-model
type: concept
fields: [bayesian, linear-algebra, political-science]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch11-density, gelman-2013-bda3/ch01-probability, grimmer-2022-textasdata/ch06-multinomial, mcelreath-2020-rethinking/ch11-monsters, murphy-2023-pml2/ch28-latent-p1]
generated_by: build_kg.py
---

# mixture-model

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 18): the distribution of data as a weighted sum of component distributions, as in (1.7) [new]
- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 342): uses more than one likelihood for one outcome variable, because several causes can produce the same observation [new]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 929): convex combination $\sum_k\pi_kp_k(x)$, equivalently a discrete latent picking the component [new]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (p. 349): convex combination of base densities with mixture weights $\pi_k$ [new]

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 120): $W_i\sim\text{Mult}(M_i,\mu\pi_i)$ with indicator $\pi_i$; known labels here, unknown in clustering [new]

## Instances that use it

- [[record-linkage-calibration]] — mixture-model calibration of false-match rates, validated on test Census data — from [[gelman-2013-bda3/ch01-probability]]
- [[gaussian-mixture-model]] — $k$-component mixture, the example for EM — from [[polyanskiy-2025-information/ch06-extremization]]

## Candidate bridges

- [metaphor] "Many biases, not one" ↔ mixture models: a single model viewed as a mixture of subgroup distributions selected by conditioning (the authors say "combination of many distributions", p. 4) — from [[argyle-2023-silicon/main-p1]] (llm → other)
- [structural-analogy] Mixture model with observed $\pi_i$ ↔ supervised classification of documents by group (the book defers it to Ch. 19); unobserved $\pi$ ↔ clustering (Ch. 12). — from [[grimmer-2022-textasdata/ch06-multinomial]] (political-science → unspecified)
- [same-math] Mixture model $uG+(1-u)B$ with latent q_i ↔ bayesian: hierarchical model with exchangeable latent indicators (de Finetti). — from [[jaynes-2003-probability/ch21-outliers]] (information-theory → bayesian)
- [structural-analogy] K-means two-step loop ↔ bayesian: assigning data to hidden causes, then re-fitting parameters, as in mixture-model inference — the book says it returns to this view later (p. 290) — from [[mackay-2003-information/ch20-example]] (information-theory → bayesian)
- [structural-analogy] infinite mixture models ↔ bayesian: nonparametric priors (Dirichlet process) letting model size grow with data — from [[mackay-2003-information/ch34-independent]] (information-theory → bayesian)
- [structural-analogy] LDA vs mixture models ↔ Clustering: mixed vs single-cluster assignment (p. 963). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → other)
- [structural-analogy] Gaussian HMM ↔ Gaussian mixture model: clusters of observations, but with Markov temporal dependence between cluster labels (p. 982). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → other)
- [structural-analogy] Baum-Welch E/M steps ↔ EM for mixture models: soft responsibilities and normalised expected counts, with $\gamma$ and $\xi$ computed by forwards-backwards. — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → other)
- [structural-analogy] SLDS mode explosion ↔ hierarchical/mixture models: growth of mixture components under conditioning, controlled by pruning or merging. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → other)
