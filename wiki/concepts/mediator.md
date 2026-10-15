---
id: mediator
type: concept
fields: [bayesian, decision-game-theory]
fields_strong: [bayesian, decision-game-theory]
n_sources: 5
n_works: 2
tiers: [core]
grounding: digests
sources: [pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2, schelling-1960-conflict/appc-re-p1]
generated_by: build_kg.py
---

# mediator

## Definitions in the sources

### bayesian

- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 145–146): variable on the causal path from X to Y; controlling for it blocks the effect [new]
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 193): a variable on the causal path from treatment to outcome; conditioning on it blocks that path [new]
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 274): variable on the path from cause to effect, through which the effect (partly) acts [new]
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 293): a variable lying on a causal path from treatment to outcome, transmitting part of the effect [new]

### decision-game-theory

- [[schelling-1960-conflict/appc-re-p1]] (p. 344): a third party who sends non-binding suggestions to the players [new]

## Instances that use it

- [[aspirin-platelet-chain]] — conditioning on a mediator blocks the path — from [[hernan-2020-whatif/ch06-graphical]]
- [[simpson-bp-drug-table]] — Table 1.2: same numbers; BP is a mediator, so use pooled data — from [[pearl-2016-primer/ch01-preliminaries]]
- [[gender-hiring-qualification-income]] — mediation; conditioning on the mediator opens a collider — from [[pearl-2016-primer/ch03-effects]]
- [[drug-b-blood-pressure]] — same numbers; mediator; pool the data — from [[pearl-2018-bookofwhy/ch06-paradoxes]]
- [[lord-diet-paradox]] — mediator case and confounder case — from [[pearl-2018-bookofwhy/ch06-paradoxes]]
- [[wainer-brown-dining-halls]] — mediator case and confounder case — from [[pearl-2018-bookofwhy/ch06-paradoxes]]
- [[bert-caroline-matching]] — matching on a mediator creates mismatch — from [[pearl-2018-bookofwhy/ch08-counterfactuals]]
- [[scurvy-lind-vitamin-c]] — wrong assumed mediator (acidity) vs. true mediator (vitamin C) — from [[pearl-2018-bookofwhy/ch09-mediation-p1]]
- [[barbara-burks-1926]] — first mediator diagram; early collider-bias criterion — from [[pearl-2018-bookofwhy/ch09-mediation-p1]]
- [[smoking-gene]] — confounder vs mediator view; interaction between gene and smoking — from [[pearl-2018-bookofwhy/ch09-mediation-p2]]
- [[tourniquet-study]] — conditioning on a mediator via selection of survivors — from [[pearl-2018-bookofwhy/ch09-mediation-p2]]
- [[finder-reward-mediator]] — a mediator's rounded 2-1 split coordinates claims — from [[schelling-1960-conflict/ch03-bargaining]]

## Candidate bridges

- [structural-analogy] Dropping post-treatment controls ↔ causal DAGs: conditioning on a mediator (ours; not stated in this unit). (canon link: fork, chain, collider) — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → bayesian)
- [structural-analogy] Post-treatment variable (fungus) ↔ causal inference: conditioning on a mediator on the path treatment → outcome blocks that path (canon "fork, chain, collider"; not stated in this unit). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → bayesian)
- [structural-analogy] Revelation principle ↔ decision-game-theory: Aumann's correlated equilibrium, where a mediator recommends actions and obeying is optimal — the paper credits Aumann (1974) as a building block (p. 322). — from [[myerson-2008-mechanism/main]] (decision-game-theory → decision-game-theory)
- [metaphor] Mediator simulating lies ↔ simulation or compilation of a strategy into a program that tells the truth — suggests why truthful direct mechanisms lose no generality. — from [[myerson-2008-mechanism/main]] (decision-game-theory → unspecified)
- [structural-analogy] conditioning on the mediator in the tourniquet study ↔ Fork, chain, collider: conditioning on the middle of a chain blocks the path — from [[pearl-2018-bookofwhy/ch09-mediation-p2]] (bayesian → bayesian)
- [structural-analogy] a mediator's suggestions ↔ correlated-equilibrium-style recommendations: the third player's suggestions are non-authoritative (p. 344). — from [[schelling-1960-conflict/appc-re-p1]] (decision-game-theory → other:correlated-equilibrium-style-recommendat)
- [structural-analogy] Mediator who compares offers without revealing them ↔ mechanism design: a third party changes what information the players can act on. — from [[schelling-1960-conflict/ch05-enforcement-p2]] (decision-game-theory → decision-game-theory)
