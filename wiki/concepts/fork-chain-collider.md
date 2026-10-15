---
id: fork-chain-collider
type: concept
fields: [bayesian]
n_sources: 25
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch09-measurement, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch15-outcome, hernan-2020-whatif/ch16-instrumental, hernan-2020-whatif/ch17-causal, hernan-2020-whatif/ch18-variable, hernan-2020-whatif/ch20-treatment, hernan-2020-whatif/ch22-target, murphy-2023-pml2/ch04-graphical-p1, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch36-causality-p1, murphy-2023-pml2/ch36-causality-p2, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch05-smoke, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch09-mediation-p1]
raw_ids: ["Fork, chain, collider"]
canon_spine: bayesian
generated_by: build_kg.py
---

# fork-chain-collider

## Canon spine entry

- **Fork, chain, collider** (bayesian): the three elementary path structures; conditioning on a collider *opens* a spurious path (UG)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch06-graphical]] (pp. 78–81): common cause, mediator, common effect; colliders block unless conditioned on
- [[hernan-2020-whatif/ch07-confounding]] (pp. 95, 97): a collider on a path blocks it. Conditioning on it opens the path
- [[hernan-2020-whatif/ch08-selection]] (pp. 109–110): a collider is a common effect; conditioning on it (or a descendant, Fig. 8.2) opens a path
- [[hernan-2020-whatif/ch09-measurement]] (pp. 127, 129): colliders $A^*$/$Y^*$ block the path between errors; a mismeasured collider conditioned on opens one
- [[hernan-2020-whatif/ch12-ip]] (p. 172): censoring $C$ as a collider (or its descendant) makes restricting to $C=0$ biasing
- [[hernan-2020-whatif/ch15-outcome]] (p. 207): colliders as covariates may cause bias even if they predict well
- [[hernan-2020-whatif/ch16-instrumental]] (p. 211): conditioning on $A$ (a collider) cannot check condition (ii)
- [[hernan-2020-whatif/ch17-causal]] (p. 231): conditioning on $D_1$ opens a path in Fig. 17.3
- [[hernan-2020-whatif/ch18-variable]] (p. 243, 245): adjusting for a collider (Fig. 18.1), a descendant of one (Fig. 18.2), or a collider that is pre-treatment (Fig. 18.6, M-bias) induces bias.
- [[hernan-2020-whatif/ch20-treatment]] (p. 271): $L_1$ is a collider on $A_0\to L_1\leftarrow U_1$; conditioning opens a path
- [[hernan-2020-whatif/ch22-target]] (p. 308): conditioning on $S$, a common effect of $Z$ and $A$, opens $Z\to A\leftarrow L\leftarrow U\to Y$
- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 149–151): three elementary path structures; conditioning on a collider makes its parents dependent
- [[murphy-2023-pml2/ch05-information-p2]] (p. 243): sign of MMI differs for common cause, common effect and chain
- [[murphy-2023-pml2/ch15-generalized]] (p. 620): conditioning on collider $D$ opens $G\to D\leftarrow U\to A$
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1189): the chapter states the fork Markov property and collider ($X\to Y\leftarrow Z$) behaviour; conditioning on a collider usually creates dependence
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1228): treatment as a collider when conditioning on $A$
- [[pearl-2016-primer/ch02-graphical]] (pp. 38–44): the three elementary three-node path structures; conditioning on the middle blocks chains/forks but opens colliders
- [[pearl-2016-primer/ch03-effects]] (pp. 62, 76): conditioning on a collider opens a path; this drives the backdoor rule and the mediation problem
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 103): $Z$ as a collider between $X$ and $U_2$ explains the education–salary result
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 114): the three three-node junctions that Pearl says suffice for reading off all independencies implied by a network (pdf 113); the full rule is d-separation
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 149): three junction types; controlling for a collider opens its path
- [[pearl-2018-bookofwhy/ch05-smoke]] (pdf 173): collider: a variable with two arrows into it; conditioning on it opens a spurious path
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 181): a collider is a variable with two arrows into it; conditioning on it creates a spurious dependence between its parents
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 208, 227): A collider blocks a path (used in the front-door and IV arguments)
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 281, 286): Social Status in Burks's diagram and Department in Kruskal's are colliders. Conditioning on them opens a spurious path [as `Fork, chain, collider`]

## Candidate bridges

- [structural-analogy] Dropping post-treatment controls ↔ causal DAGs: conditioning on a mediator (ours; not stated in this unit). (canon link: fork, chain, collider) — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → bayesian)
- [same-math] Conditioning on a collider (p. 243) ↔ Causal DAG: collider path opening — the same phenomenon, discussed under d-separation and fork/chain/collider. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [structural-analogy] Post-treatment variable (fungus) ↔ causal inference: conditioning on a mediator on the path treatment → outcome blocks that path (canon "fork, chain, collider"; not stated in this unit). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → bayesian)
- [structural-analogy] Collider in Burks's diagram ↔ causal-inference canon (fork, chain, collider): conditioning on a common effect opens a spurious path. — from [[pearl-2018-bookofwhy/ch09-mediation-p1]] (bayesian → bayesian)
- [structural-analogy] conditioning on the mediator in the tourniquet study ↔ Fork, chain, collider: conditioning on the middle of a chain blocks the path — from [[pearl-2018-bookofwhy/ch09-mediation-p2]] (bayesian → other)
