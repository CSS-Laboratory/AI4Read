---
id: d-separation
type: concept
fields: [bayesian, linear-algebra]
n_sources: 18
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch09-measurement, hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch21-g, murphy-2023-pml2/ch04-graphical-p1, murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch36-causality-p1, murphy-2023-pml2/ch36-causality-p2, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch08-counterfactuals]
canon_spine: bayesian
generated_by: build_kg.py
---

# d-separation

## Canon spine entry

- **d-separation** (bayesian): a graphical rule that reads off which conditional independences a DAG implies (grad)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch06-graphical]] (p. 82): four path-blocking rules; with causal Markov, d-separation implies independence
- [[hernan-2020-whatif/ch07-confounding]] (p. 102): read off exchangeability from the SWIG
- [[hernan-2020-whatif/ch08-selection]] (pp. 110, 121): the rule used to read which paths conditioning opens or blocks
- [[hernan-2020-whatif/ch09-measurement]] (p. 127): used to show $U_A$ and $U_Y$ are independent
- [[hernan-2020-whatif/ch19-time]] (p. 261): used in the generalized backdoor criterion and SWIG checks
- [[hernan-2020-whatif/ch21-g]] (p. 301): used to reduce the big g-formula
- [[murphy-2023-pml2/ch04-graphical-p1]] (p. 149): path-blocking rule (chain, fork, collider) giving the directed global Markov property; checked by Bayes ball
- [[murphy-2023-pml2/ch04-graphical-p2]] (p. 181): compared with undirected separation
- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 200): graphical CI rule; used via m-separation for ADMGs
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1189): recalled (from Ch. 4) as the tool giving independences implied by the graph
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1229): basis of the rule conditions on mutilated graphs
- [[pearl-2016-primer/ch02-graphical]] (p. 46): graph criterion: a path is blocked by a conditioned chain/fork middle node, or by an unconditioned collider without conditioned descendants; separation implies independence
- [[pearl-2016-primer/ch03-effects]] (p. 84): used here to show $Z\perp X$ in $G_m$ (p. 56) and in the $G_\alpha$ rule
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 103): used to test independence of $Y_x$ from $X$ given $Z$ via the node $U_2$ and collider $Z$
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 114): the full rule combining the three junctions, promised for Chapter 7
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 222): Rule that path blocking tells which independencies hold; credited to Verma
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 257): blocking implies conditional independence; gives a test of a diagram

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (p. 281): graph criterion implying conditional independence (8.34) [new]

## Instances that use it

- [[d-separation-example-8-9]] — Fig. 8.11 with four independence statements — from [[deisenroth-2020-mml/ch08-when]]

## Candidate bridges

- [same-math] Conditioning on a collider (p. 243) ↔ Causal DAG: collider path opening — the same phenomenon, discussed under d-separation and fork/chain/collider. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [structural-analogy] Granger and Suppes screening-off ↔ d-separation: both express "no predictive value given $Z$". — from [[holland-1986-statistics/main]] (bayesian → other)
- [structural-analogy] The adjustment steps (Z1, Z2 and "X disconnected from Y") ↔ back-door criterion and d-separation; the exact steps are on slides not in the text. — from [[pearl-2009-causality/main]] (bayesian → unspecified)
- [same-math] d-separation ↔ conditional independence in probabilistic graphical models: the graph reads off $P(A|B,C)=P(A|C)$ for the product decomposition (cited as (1.29), p. 51). — from [[pearl-2016-primer/ch02-graphical]] (bayesian → other)
- [same-math] Conditional independence in chains and forks ↔ causal inference: d-separation on paths. — from [[pearl-2018-bookofwhy/ch03-evidence]] (bayesian → bayesian)
