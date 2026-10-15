---
id: exchangeability
type: concept
fields: [bayesian, information-theory]
n_sources: 28
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch03-introduction, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch19-parametric, gelman-2013-bda3/ch22-finite, gelman-2013-bda3/ch23-dirichlet, hernan-2020-whatif/ch08-selection, jaynes-2003-probability/appa-other, jaynes-2003-probability/ch03-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch10-physics, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch21-outliers, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch18-crosswords, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch04-graphical-p1, murphy-2023-pml2/ch14-predictive, pearl-2018-bookofwhy/ch04-confounding, polyanskiy-2025-information/ch10-random]
canon_spine: bayesian
generated_by: build_kg.py
---

# exchangeability

## Canon spine entry

- **Exchangeability** (bayesian): a sequence whose joint distribution is unchanged under reordering; de Finetti's theorem says such sequences behave as i.i.d. given a latent parameter (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 5): joint density invariant to permuting indexes; commonly modelled as iid given $\theta$
- [[gelman-2013-bda3/ch02-single]] (p. 29): trial order irrelevant, so data reduce to counts; i.i.d. given θ
- [[gelman-2013-bda3/ch03-introduction]] (pp. 70, 75): used to justify the multinomial and binomial models
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 104): joint density invariant to permuting indexes; the form of "no information distinguishes units"
- [[gelman-2013-bda3/ch06-model]] (p. 159): here, a prior stance that the $\theta_j$ are symmetric and the data decide ordering and similarity
- [[gelman-2013-bda3/ch14-introduction]] (p. 364): old and new units are exchangeable given x, so x must hold all distinguishing information
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 383): here: exchangeability among units is obtained by conditioning on group indicators; coefficients within a batch are exchangeable
- [[gelman-2013-bda3/ch17-models]] (p. 436): a Cauchy or mixture prior is still exchangeable, so robust models stay Bayesian
- [[gelman-2013-bda3/ch19-parametric]] (p. 482): a new person "exchangeable with the subjects" is simulated from the population distribution
- [[gelman-2013-bda3/ch22-finite]] (p. 533): here: components are exchangeable in the prior (22.10)
- [[gelman-2013-bda3/ch23-dirichlet]] (p. 550): used to derive the full conditional prior (23.7)
- [[hernan-2020-whatif/ch08-selection]] (p. 113): property of treated and untreated groups whose lack results from confounding or selection bias; not formally defined in this unit
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (p. 81): values that can be reordered; de Finetti's theorem links them to mixtures of i.i.d. distributions
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 387): here: index values with no true ordering, arbitrary labels, so a batch can be pooled
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 72): joint invariant to permutation; de Finetti's theorem gives iid given hidden θ
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 108): a new group "exchangeable with" existing groups gets predictive (3.247)
- [[murphy-2023-pml2/ch04-graphical-p1]] (p. 162): here: order of iid data is irrelevant, so leaves can be permuted
- [[murphy-2023-pml2/ch14-predictive]] (p. 586): the only assumption behind the conformal guarantee
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 146–147): here the Greenland–Robins counterfactual sense: equal shares of doomed, causative, preventive, immune in both groups

### information-theory

- [[jaynes-2003-probability/appa-other]] (p. 655): de Finetti's theorem, called "marvellous and indispensable"
- [[jaynes-2003-probability/ch03-elementary]] (p. 62): the probability of a sequence is invariant under any permutation of the trial results, so it depends only on the counts; the author's definition is for $k$-valued trials
- [[jaynes-2003-probability/ch05-queer]] (p. 137): $H_{\rm ex}$, an exchangeable sampling distribution allowing correlated years
- [[jaynes-2003-probability/ch10-physics]] (p. 337): probability of $n$ heads at specified trials among $N$ depends only on $N$ and $n$; used with de Finetti to get the weak law
- [[jaynes-2003-probability/ch18-p]] (p. 586): probability of a sequence depends only on counts; by de Finetti every such sequence has a g(p) representation
- [[jaynes-2003-probability/ch21-outliers]] (p. 620): good/bad label probabilities depend only on counts, so a de Finetti mixture in u applies
- [[jaynes-2003-probability/ch22-introduction]] (p. 640): the multinomial (22.35) depends only on letter counts, not order
- [[mackay-2003-information/ch18-crosswords]] (p. 263): here: statistical properties of the generated text are homogeneous along the stream
- [[polyanskiy-2025-information/ch10-random]] (p. 170): distribution invariant under permutations; for binary strings, depends only on Hamming weight [new]

## Instances that use it

- [[divorce-rates-exchangeability]] — how information about states breaks or preserves exchangeability — from [[gelman-2013-bda3/ch05-hierarchical]]
- [[schoolchildren-prediction-example]] — second-grade reading scores; exchangeability and school indicators — from [[gelman-2013-bda3/ch14-introduction]]
- [[smoking-unmeasured-confounder]] — doctors prefer nonsmokers, so exchangeability given $L$ fails — from [[hernan-2020-whatif/ch03-observational]]
- [[hospital-aceso-panacea]] — a strong predictor of treatment that is unnecessary for exchangeability inflates variance — from [[hernan-2020-whatif/ch15-outcome]]
- [[flu-vaccine-response-types]] — four response types behind exchangeability — from [[pearl-2018-bookofwhy/ch04-confounding]]

## Candidate bridges

- [structural-analogy] de Finetti mixture (5.2) ↔ exchangeability in the canon: (5.2) is an exchangeable form, and de Finetti's theorem gives the converse only as $J\to\infty$, not for finite $J$. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other)
- [metaphor] Exchangeability of treated and untreated ↔ bayesian: de Finetti exchangeability — same word, different definitions; do not conflate. — from [[hernan-2020-whatif/ch02-randomized]] (bayesian → bayesian)
- [structural-analogy] conditional exchangeability / ignorable assignment ↔ missing data: $Y^a$ is missing for those with $A\neq a$; ignorability plays the role of "missing at random" given $L$. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → other)
- [structural-analogy] identifying assumption external to the data ↔ Bayesian inference: where data fit many effect values, a prior or assumption must supply the rest (here the prior is a point-mass-like assumption of exchangeability). — from [[hernan-2020-whatif/ch03-observational]] (bayesian → bayesian)
- [structural-analogy] sequential exchangeability ↔ sequential/adaptive Bayesian experimentation: assignment may depend on observed past but not on unobserved outcome drivers. — from [[hernan-2020-whatif/ch19-time]] (bayesian → bayesian)
- [structural-analogy] Exchangeability: all draws equally relevant ↔ bayesian: exchangeability / de Finetti — the chapter uses permutation invariance only; the representation theorem is not in this unit. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
- [structural-analogy] Robot on $I_0$ (independent trials) ↔ bayesian: i.i.d. sampling versus exchangeability, where past trials inform future ones (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → bayesian)
- [same-math] Exchangeability plus de Finetti, giving the weak law only under (D) ↔ bayesian: Exchangeability — the text uses the theorem directly (p. 337). — from [[jaynes-2003-probability/ch10-physics]] (information-theory → bayesian)
- [same-math] de Finetti theorem (p. 586) ↔ bayesian: exchangeability implies i.i.d. given a latent parameter — from [[jaynes-2003-probability/ch18-p]] (information-theory → bayesian)
- [structural-analogy] Interleaving to make errors look independent ↔ bayesian: assuming exchangeability or independence of errors that are not truly independent. — from [[mackay-2003-information/ch11-error]] (information-theory → bayesian)
- [structural-analogy] Epistemic-vs-aleatoric split in joint predictions ↔ exchangeability and de Finetti mixtures: agent 2 is a mixture of iid coins (p. 582) — from [[murphy-2023-pml2/ch14-predictive]] (bayesian → other)
- [structural-analogy] Ignorability ↔ exchangeability — the text calls them "in essence" the same, expressed on $Y_x$. — from [[pearl-2018-bookofwhy/ch08-counterfactuals]] (bayesian → unspecified)
- [structural-analogy] Exchangeability here ↔ de Finetti (Ex. I.52, p. 186): exchangeable laws are approximated by mixtures of i.i.d. laws. — from [[polyanskiy-2025-information/ch10-random]] (information-theory → other)
