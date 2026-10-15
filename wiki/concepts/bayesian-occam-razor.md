---
id: bayesian-occam-razor
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch24-exact, murphy-2023-pml2/ch18-gaussian-p2]
generated_by: build_kg.py
---

# bayesian-occam-razor

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 718): in (18.163) the $\log|K_\sigma|$ term penalises complex kernels while the quadratic form measures fit

### information-theory

- [[mackay-2003-information/ch24-exact]] (p. 322): the Occam factor in (24.13), a volume factor from integrating out μ

## Candidate bridges

- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] Class Ω of alternatives in the ψ-test ↔ bayesian: model-class choice behind Bayesian Occam's razor; "undefined over all conceivable theories". — from [[jaynes-2003-probability/ch09-repetitive-p2]] (information-theory → bayesian)
- [structural-analogy] Lindley's Paradox ↔ bayesian: Bayesian Occam's razor — a precise hypothesis with a huge sample is judged against alternatives, not by p alone. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] ARD evidence maximization ↔ Bayesian Occam's razor: irrelevant features waste predictive mass. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
- [structural-analogy] Random labels getting low marginal likelihood ↔ Bayesian Occam's razor: a model spreading mass over many datasets gives each less. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Fit-plus-complexity split of the log marginal likelihood (18.74) ↔ bayesian-occam-razor (canon link; the text does not use that name). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → unspecified)
- [structural-analogy] ARD pruning of weights ↔ Bayesian Occam's razor: marginal-likelihood-based models shrink as data shrink (p. 949) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] $K$ selection by marginal likelihood ↔ Bayesian Occam's razor: more states fit no better, so evidence falls (p. 986). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [structural-analogy] Automatic introduction of new classes only when data demand it (CRP/Occam's razor) ↔ bayesian: Bayesian Occam's razor via marginal likelihood — complexity is penalized without a hand-set cost. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
