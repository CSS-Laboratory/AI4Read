---
id: bayesian-occams-razor
type: concept
fields: [bayesian, information-theory, control-theory, llm]
fields_strong: [bayesian, information-theory, control-theory, llm]
n_sources: 16
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch22-finite, gelman-2013-bda3/ch23-dirichlet, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch20-model, mackay-2003-information/ch03-more, mackay-2003-information/ch24-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch44-supervised, mackay-2003-information/ch45-gaussian, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch28-latent-p1, murphy-2023-pml2/ch29-state-p1, tenenbaum-2011-grow/main]
aliases: [bayesian-occam-razor]
raw_ids: ["Bayesian Occam's razor"]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# bayesian-occams-razor

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `bayesian-occam-razor` — 2 digest(s)

## Canon spine entry

- **Bayesian Occam's razor** (bayesian): the marginal likelihood automatically penalizes models that spread probability over too many possible datasets (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch22-finite]] (p. 535): the "intrinsic Bayes penalty": marginal likelihood tends to fall as items are spread across more components
- [[gelman-2013-bda3/ch23-dirichlet]] (pp. 553–554): author's explanation of why no overfitting in clustering via $\alpha$
- [[jaynes-2003-probability/ch06-elementary-p2]] (p. 195): low prior credence, not likelihood, rejects $H_S$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch20-model]] (pp. 604–607): the Ockham factor $W$ in $p(D|MI)=L_{\max}W$ penalises models whose prior is spread beyond the data's high-likelihood region [work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 119): a model with too much flexibility wastes prior predictive mass, lowering the expected likelihood
- [[murphy-2023-pml2/ch05-information-p2]] (p. 258): the prior $2^{-K(\nu)}$ is motivated by Occam's razor (author's words) [work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch15-generalized]] (p. 607): evidence penalizes irrelevant features that waste probability mass
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 718): in (18.163) the $\log|K_\sigma|$ term penalises complex kernels while the quadratic form measures fit [alias `bayesian-occam-razor`]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 949): ARD/MFA prefers simpler models when data are scarce
- [[murphy-2023-pml2/ch29-state-p1]] (p. 986): author's explanation for the fall in marginal likelihood for $K>4$ [work fields: bayesian, control-theory]
- [[tenenbaum-2011-grow/main]] (p. 1284): automatic trade-off of complexity and fit; new structure only if data require it

### information-theory

- [[mackay-2003-information/ch03-more]] (p. 53): only the observed behaviour is stated: the simple model can lose by a large margin and the complex one cannot (p. 53). The name is canon, not used in this unit. [weak: not really used in this unit; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch24-exact]] (p. 322): the Occam factor in (24.13), a volume factor from integrating out μ [alias `bayesian-occam-razor`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch28-model]] (p. 344): the data-dependent ratio of evidences penalizes complex models without any prior bias for simplicity [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch44-supervised]] (p. 531): over-complex models are less probable (via Chapter 28) [as `Bayesian Occam's razor`; work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch45-gaussian]] (p. 546): handles the complexity-control problem of choosing hyperparameters [work fields: information-theory, bayesian]

## Candidate bridges

- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] Class Ω of alternatives in the ψ-test ↔ bayesian: model-class choice behind Bayesian Occam's razor; "undefined over all conceivable theories". — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → bayesian)
- [structural-analogy] Lindley's Paradox ↔ bayesian: Bayesian Occam's razor — a precise hypothesis with a huge sample is judged against alternatives, not by p alone. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] ARD evidence maximization ↔ Bayesian Occam's razor: irrelevant features waste predictive mass. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
- [structural-analogy] Random labels getting low marginal likelihood ↔ Bayesian Occam's razor: a model spreading mass over many datasets gives each less. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Fit-plus-complexity split of the log marginal likelihood (18.74) ↔ bayesian-occam-razor (canon link; the text does not use that name). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → unspecified)
- [structural-analogy] ARD pruning of weights ↔ Bayesian Occam's razor: marginal-likelihood-based models shrink as data shrink (p. 949) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] $K$ selection by marginal likelihood ↔ Bayesian Occam's razor: more states fit no better, so evidence falls (p. 986). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [structural-analogy] Automatic introduction of new classes only when data demand it (CRP/Occam's razor) ↔ bayesian: Bayesian Occam's razor via marginal likelihood — complexity is penalized without a hand-set cost. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
