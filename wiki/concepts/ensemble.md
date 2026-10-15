---
id: ensemble
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, stone-2022-information/ch10-thermodynamic]
generated_by: build_kg.py
---

# ensemble

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch02-probability]] (p. 22): triple (outcome, alphabet, probabilities); a random variable with its alphabet and probabilities [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch04-source]] (p. 67): triple (x, A_X, P_X): outcome, alphabet, probabilities (new) [work fields: information-theory, bayesian]
- [[stone-2022-information/ch10-thermodynamic]] (p. 208): the set of microstates that yield one macrostate [new]

## Instances that use it

- [[balinese-cockfight]] — culture as an ensemble of texts, read over others' shoulders — from [[carey-1989-cultural/ch02-mass]]
- [[grand-canonical-ensemble]] — max-entropy estimate with $\langle E\rangle$, $\langle n_i\rangle$ given — from [[jaynes-1957-information/main]]
- [[pressure-ensemble]] — max-entropy with $\langle E\rangle,\langle V\rangle$ given — from [[jaynes-1957-information/main]]
- [[english-letter-ensemble]] — 27-symbol alphabet; monogram and bigram distributions; entropy about 4.11 bits — from [[mackay-2003-information/ch02-probability]]
- [[bent-coin-extended-ensemble]] — N flips with p₁=0.1; H_δ(X^N) staircases and typicality — from [[mackay-2003-information/ch04-source]]
- [[xor-three-variable-ensemble]] — $z=x+y \bmod 2$: $I(X;Y)=0$ but $I(X;Y|Z)=1$ bit — from [[mackay-2003-information/ch08-dependent]]
- [[random-linear-code-ensemble]] — average over all binary $\mathbf H$ shows good codes exist — from [[mackay-2003-information/ch14-very]]
- [[shifter-ensemble]] — plain and labelled; not learnable from second-order statistics alone (p. 524); Hinton and Sejnowski learned the labelled one with hidden units — from [[mackay-2003-information/ch43-boltzmann]]
- [[chair-images-ensemble]] — example where second-order pixel statistics are expected to be useless — from [[mackay-2003-information/ch43-boltzmann]]
- [[bars-and-stripes-ensemble]] — exercise on learnability without hidden units — from [[mackay-2003-information/ch43-boltzmann]]
- [[random-prior-ensemble]] — effect of $\beta$ on ensemble diffuseness — from [[murphy-2023-pml2/ch17-bayesian]]
- [[abab-baba-eeee-source]] — stationary source whose time averages differ from its ensemble average — from [[pierce-1980-introduction/ch03-mathematical]]
- [[14-hidden-unit-regression-fit]] — toy network fitted with different $\lambda$, training stages, ensembles and priors — from [[prince-2023-udl/ch09-regularization]]
- [[urban-distillation]] — shallow students fail to match a deep ensemble — from [[prince-2023-udl/ch20-does]]

## Candidate bridges

- [structural-analogy] Interpolated trigram with frequency-dependent weights $\alpha_i(q_t)$ ↔ ensemble methods: weights depending on how reliable each component is — from [[bengio-2003-nplm/main]] (llm → other:ensemble-methods)
- [structural-analogy] Partial pooling toward a mean ↔ ensemble or regularized estimators: both trade group-specific fit for stability. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other:ensemble-or-regularized-estimators)
- [structural-analogy] Stacking of chains/models with cross-validation weights ↔ model averaging in predictive ensembles — weights are chosen by predictive performance, not by posterior probability (p. 25). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
- [same-math] Raw bit content H₀ ↔ statistical mechanics: Boltzmann entropy k_B ln Ω for a microcanonical ensemble (p. 87). — from [[mackay-2003-information/ch04-source]] (information-theory → complex-systems)
- [metaphor] ensemble learning: a point estimate is a delta-function Q ↔ MAP estimation: the spike is the crudest member of the family. — from [[mackay-2003-information/ch33-variational]] (information-theory → bayesian)
- [structural-analogy] Model averaging ↔ forecasting: ensemble forecasts — predictions are combined by weights to express uncertainty. — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (bayesian → other:statistics)
- [structural-analogy] dropout ensemble ↔ Bayesian model averaging (Monte Carlo dropout, Ch. 17): both average over many networks; the chapter only points forward — from [[murphy-2023-pml2/ch16-deep]] (bayesian → bayesian)
- [structural-analogy] Birkhoff time average = ensemble average ↔ statistics: law of large numbers; iid case is the SLLN (p. 235). — from [[polyanskiy-2025-information/ch14-entropy]] (information-theory → other:statistics)
- [structural-analogy] pure selection by one variable ↔ statistics: selecting an ensemble by one variable need not fix the other — similar logic of subsetting a population. — from [[popper-1959-logic/appv-untitled]] (analytic-philosophy → other:statistics)
- [structural-analogy] Dropout / Monte Carlo dropout ↔ ensembling: many sub-networks as an implicit ensemble. — from [[prince-2023-udl/ch09-regularization]] (llm → llm)
- [structural-analogy] Ergodicity (one long sequence represents the ensemble) ↔ social-science time-series estimation: inferring population properties from a single long record — from [[shannon-1948-mathematical/main-p1]] (information-theory → other:social-science-time-series)
- [structural-analogy] Entropy of a source via an ensemble ↔ statistical physics: ensemble of microstates — both average over a set of possible configurations (p. 243). — from [[stone-2022-information/appa-glossary]] (information-theory → complex-systems)
