---
id: bayesian-network
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 7
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, mcgrayne-2011-theory/ch16-eureka, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch04-graphical-p1, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch10-big]
aliases: [directed-graphical-model]
generated_by: build_kg.py
---

# bayesian-network

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `directed-graphical-model` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[mcgrayne-2011-theory/ch16-eureka]] (p. 228): graph of nodes with cause-and-effect links, updated by Bayes' theorem [new]
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 239–240): network of variables with priors; purists dispute the name if priors are absent [new]
- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 143–144): DAG whose nodes are variables and whose joint is a product of CPDs given parents; "Bayesian" only in name [alias `directed-graphical-model`; new]
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 55–56): Pearl's earlier probabilistic model of uncertain reasoning; rung one until later extensions [new]
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 110): network of variables with conditional probability tables. Its arrows need not be causal [new]
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 322–323): probabilistic, modular AI tool; cannot tell causal direction [new]

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (pp. 278–280): a joint factorized as ∏ p(x_k | Pa_k) (8.31) [alias `directed-graphical-model`; new]

## Candidate bridges

- [same-math] Markov factorization $f(v)=\prod_j f(v_j\mid pa_j)$ ↔ Bayesian: factorisation of a joint distribution in a directed graphical model (Bayesian network) — same product of conditionals. — from [[hernan-2020-whatif/ch06-graphical]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning opens a path (M-bias) ↔ Bayesian networks: "explaining away", where conditioning on a common effect makes independent causes dependent — the same path logic. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → bayesian)
- [metaphor] SWIG node splitting ↔ conditioning vs intervening in Bayesian networks: separate the value "as observed" from the value "set by the analyst". — from [[hernan-2020-whatif/ch19-time]] (bayesian → bayesian)
- [structural-analogy] Jern et al.'s Bayesian network with hidden trust variable ↔ Bayesian updating: an apparently irrational reaction can follow from conditioning on source trust (paper gives no equations). — from [[lewandowsky-2012-misinformation/main]] (communication-theory → bayesian)
- [structural-analogy] Bayesian networks ↔ causal DAGs: both are graphs of nodes with links, though the source treats the links as quantifiable belief. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning (m-bias) ↔ bayesian: "explaining away" in Bayesian networks. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
- [same-math] Product decomposition (1.29) ↔ Bayesian network factorization: the book itself says it became the semantic basis of Bayesian networks (p. 33). — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [metaphor] "listens to" ↔ bayesian: conditional dependence in a directed graphical model, as in Bayesian networks, which Pearl says underlie causal diagrams (pdf 24). — from [[pearl-2018-bookofwhy/ch00-introduction]] (bayesian → bayesian)
- [structural-analogy] Bayesian networks (Pearl, rung one) ↔ causal DAG: same graph, different questions answerable. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → bayesian)
- [structural-analogy] Bayesian network message passing ↔ cognition: Rumelhart's parallel layers in reading. — from [[pearl-2018-bookofwhy/ch03-evidence]] (bayesian → other:psychology-cognitive-science)
- [metaphor] Web/field of belief ↔ Bayesian networks: revising one node shifts others; no probabilities appear in this paper. — from [[quine-1951-dogmas/main]] (analytic-philosophy → bayesian)
