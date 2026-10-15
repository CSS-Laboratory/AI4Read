---
id: occams-razor
type: concept
fields: [complex-systems, information-theory]
fields_strong: [complex-systems, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch07-kolmogorov, mitchell-2009-guidedtour/ch07-defining]
generated_by: build_kg.py
---

# occams-razor

## Definitions in the sources

### complex-systems

- [[mitchell-2009-guidedtour/ch07-defining]] (pdf 132): choose the smallest description that fits and minimizes leftover randomness [new]

### information-theory

- [[cover-2006-elements/ch07-kolmogorov]] (p. 161, 169): prefer the simplest explanation; here, shortest program / highest universal probability [new]

## Candidate bridges

- [structural-analogy] shortest program length $K$ ↔ Occam's razor / MDL: the simplest explanation as the shortest description (pp. 3–4) — from [[cover-2006-elements/ch01-introduction]] (information-theory → information-theory)
- [metaphor] Evidence and Occam's razor ↔ philosophy of science: prefer the simplest hypothesis consistent with the data (p. 285). — from [[deisenroth-2020-mml/ch08-when]] (linear-algebra → analytic-philosophy)
- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] Class Ω of alternatives in the ψ-test ↔ bayesian: model-class choice behind Bayesian Occam's razor; "undefined over all conceivable theories". — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → bayesian)
- [metaphor] Ulysses' compass ↔ Occam's razor: steering between two errors vs cutting away assumptions. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → bayesian)
- [structural-analogy] Lindley's Paradox ↔ bayesian: Bayesian Occam's razor — a precise hypothesis with a huge sample is judged against alternatives, not by p alone. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] ARD evidence maximization ↔ Bayesian Occam's razor: irrelevant features waste predictive mass. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
- [structural-analogy] Random labels getting low marginal likelihood ↔ Bayesian Occam's razor: a model spreading mass over many datasets gives each less. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Fit-plus-complexity split of the log marginal likelihood (18.74) ↔ bayesian-occam-razor (canon link; the text does not use that name). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → unspecified)
- [structural-analogy] ARD pruning of weights ↔ Bayesian Occam's razor: marginal-likelihood-based models shrink as data shrink (p. 949) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] $K$ selection by marginal likelihood ↔ Bayesian Occam's razor: more states fit no better, so evidence falls (p. 986). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [metaphor] over-parameterized network "choosing the smoothest fit" ↔ Occam's razor: prefer simpler explanations when data do not decide. — from [[prince-2023-udl/ch08-measuring]] (llm → bayesian)
- [structural-analogy] Automatic introduction of new classes only when data demand it (CRP/Occam's razor) ↔ bayesian: Bayesian Occam's razor via marginal likelihood — complexity is penalized without a hand-set cost. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
