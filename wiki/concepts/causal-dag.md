---
id: causal-dag
type: concept
fields: [bayesian, information-theory]
n_sources: 24
tiers: [core, reference, deep]
grounding: digests
sources: [hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch09-measurement, hernan-2020-whatif/ch18-variable, hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch20-treatment, hernan-2020-whatif/ch21-g, hernan-2020-whatif/ch23-causal, holland-1986-statistics/main, mackay-2003-information/ch35-random, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch36-causality-p1, pearl-2009-causality/main, pearl-2016-primer/ch01-preliminaries, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch03-effects, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch09-mediation-p2]
raw_ids: [Causal DAG]
canon_spine: bayesian
generated_by: build_kg.py
---

# causal-dag

## Canon spine entry

- **Causal DAG** (bayesian): a directed acyclic graph encoding qualitative causal assumptions about which variables affect which (UG)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch06-graphical]] (pp. 75–76): DAG whose arrows are direct causal effects; no arrow means no direct effect; all common causes included
- [[hernan-2020-whatif/ch09-measurement]] (p. 132): a DAG all of whose arrows have a causal interpretation, in this book's usage
- [[hernan-2020-whatif/ch18-variable]] (p. 245): graphs used to decide adjustment sets; the text says they ignore temporal order.
- [[hernan-2020-whatif/ch19-time]] (p. 261): used in the generalized backdoor criterion and SWIG checks
- [[hernan-2020-whatif/ch20-treatment]] (p. 268): acyclic graphs can show feedback by unrolling in discrete time
- [[hernan-2020-whatif/ch21-g]] (p. 279, 300): used to check which histories are needed and to define the big g-formula
- [[hernan-2020-whatif/ch23-causal]] (pp. 323, 326–327, 330–331): Figures 23.1–23.8, with SWIGs for the interventions [as `Causal DAG`]
- [[holland-1986-statistics/main]] (p. 958): path diagrams; Holland finds some meaningful (e.g. $S\to Y_S$) and some meaningless (e.g. attribute $\to$ response)
- [[murphy-2023-pml2/ch15-generalized]] (p. 620): Fig. 15.10 models of admissions
- [[murphy-2023-pml2/ch19-beyond]] (pp. 737, 740): causal (X→Y) vs anticausal (Y→X) prediction and selection diagrams
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1188): graph of which variables are parents of which, leaving the functional forms unspecified; implies a PGM
- [[pearl-2009-causality/main]] (pp. 417, 422): the diagram saying which equation to delete and licensing transformations
- [[pearl-2016-primer/ch01-preliminaries]] (pp. 25, 27): directed acyclic graph with nodes as variables and an edge from each variable in a function to the variable it determines
- [[pearl-2016-primer/ch02-graphical]] (p. 36): graph of which variables cause which; here read for independencies
- [[pearl-2016-primer/ch03-effects]] (pp. 54, 81): the graph and equations behind surgery and linear path analysis
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 14, 19): Pearl's causal diagram: dots = variables, arrows = known or suspected "listens to" links
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 29, 46): dots-and-arrows model; here also an answer-extraction representation for all three rungs
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 77–78): Wright's path diagram: one-way arrows from cause to effect, two-headed arrows for correlated causes
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 94, 125): Bayesian network whose arrows mean direct causation, with the "listening" reading
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 132, 149): diagram used to find confounders and sufficient adjustment sets
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 180, 191): a diagram encoding how data were generated; it decides what to adjust for
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 210, 231): Diagram whose absent arrows encode the assumptions licensing each method
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 301): diagram stating which variables directly affect which; assumptions for the Mediation Formula are read from it

### information-theory

- [[mackay-2003-information/ch35-random]] (p. 447): here, arrows read as "is a parent of"

## Candidate bridges

- [structural-analogy] Dropping post-treatment controls ↔ causal DAGs: conditioning on a mediator (ours; not stated in this unit). (canon link: fork, chain, collider) — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → bayesian)
- [structural-analogy] marginal $\Pr[Y^a=1]$ versus conditional $\Pr[Y=1|A=a]$ ↔ causal-DAG field: $P(Y|do(X=x))$ versus $P(Y|X=x)$ — same intervention-versus-observation distinction in a different notation. — from [[hernan-2020-whatif/ch01-definition]] (bayesian → bayesian)
- [same-math] Conditioning on a collider (p. 243) ↔ Causal DAG: collider path opening — the same phenomenon, discussed under d-separation and fork/chain/collider. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [same-math] conditioning on $S=1$ (being per-protocol) opens $Z\to A\leftarrow L\leftarrow U\to Y$ ↔ causal DAGs: collider conditioning opens a spurious path — the same graph rule. — from [[hernan-2020-whatif/ch22-target]] (bayesian → bayesian)
- [structural-analogy] Path diagrams (36)–(43) ↔ causal DAG: arrows read as exposure-to-response, but meaningful only for manipulable causes. — from [[holland-1986-statistics/main]] (bayesian → bayesian)
- [structural-analogy] Logic flow $C\to B\to A$ with no direct $C\to A$ ↔ bayesian: chain in a causal DAG, $A\perp C\mid B$. — from [[jaynes-2003-probability/ch05-queer]] (information-theory → bayesian)
- [structural-analogy] Fig. 6.2(b), a common source $s$ pointing to every $n_i$ ↔ bayesian: causal DAG fork, where conditioning on the common cause blocks the link between the others — from [[jaynes-2003-probability/ch06-elementary-p2]] (information-theory → bayesian)
- [structural-analogy] $I(X;Y|Z)>0$ while $I(X;Y)=0$ ↔ bayesian (causal DAGs): conditioning on a collider opens a path between independent causes. — from [[mackay-2003-information/ch08-dependent]] (information-theory → bayesian)
- [structural-analogy] Likelihood-equivalence of $A\to B$ and $B\to A$ ↔ bayesian: causal DAGs, where observational data alone cannot fix arrow direction (canon link; not stated in this unit). — from [[mackay-2003-information/ch35-random]] (information-theory → bayesian)
- [structural-analogy] $x_{real}\to x_{spur}$ and $x_{real}\to y$ (p. 135) ↔ Causal DAG: a fork, where a common cause creates an association between its two effects — the text does not use DAG language. — from [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (bayesian → bayesian)
- [structural-analogy] Bayesian networks ↔ causal DAGs: both are graphs of nodes with links, though the source treats the links as quantifiable belief. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → bayesian)
- [structural-analogy] RBM versus directed two-layer model ↔ explaining away in causal DAGs (p. 172). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → unspecified)
- [structural-analogy] fully connected ARM DAG (Fig. 22.1) ↔ causal DAG: both are DAGs, but here the ordering is a modelling choice and the text does not claim it is causal. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → bayesian)
- [same-math] SCM as a DAG with functional links plus exogenous noise ↔ causal DAG/SCM concepts in the causal-inference field — same object (p. 1045). — from [[murphy-2023-pml2/ch30-graph]] (bayesian → unspecified)
- [structural-analogy] Bayesian networks (Pearl, rung one) ↔ causal DAG: same graph, different questions answerable. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → bayesian)
- [structural-analogy] Causal structure learned as a directed graph with a schema prior ↔ causal inference: causal DAGs — nodes and directed edges encode causal assumptions; the paper also links this to interventions. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
