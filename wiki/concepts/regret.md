---
id: regret
type: concept
fields: [decision-game-theory, bayesian]
fields_strong: [decision-game-theory, bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [kahneman-2011-thinking/ch32-keeping, murphy-2023-pml2/ch34-decision]
generated_by: build_kg.py
---

# regret

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch34-decision]] (p. 1127): gap between oracle reward and agent reward; cumulative $L_T$; lower bound $\log T$ order [new; work fields: bayesian, decision-game-theory]

### decision-game-theory

- [[kahneman-2011-thinking/ch32-keeping]] (pdf 338): a counterfactual emotion and self-punishment, strongest when the alternative is easy to imagine [new]

## Instances that use it

- [[problems-6-7-regret]] — regret compounds in the larger sure-gift case — from [[kahneman-2011-thinking/ch26-prospect]]
- [[hitchhiker-brown-smith]] — regret versus blame (88/12 and 23/77) — from [[kahneman-2011-thinking/ch32-keeping]]
- [[paul-george-stocks]] — action versus inaction in regret (8/92) — from [[kahneman-2011-thinking/ch32-keeping]]
- [[newspaper-endorsement-regret]] — extra information may lead to a worse choice — from [[lupia-1998-dilemma/ch01-knowledge]]
- [[lottery-ticket-minimax-regret]] — regret tables and the 9/10 portfolio — from [[mackay-2003-information/ch36-decision]]
- [[lily-allen-bitcoin]] — regret story inside the Bitcoin constellation — from [[shiller-2019-narrative/ch08-seven]]

## Candidate bridges

- [structural-analogy] Online-to-batch (13.36) ↔ statistical learning: cumulative regret controls test error via averaging. — from [[polyanskiy-2025-information/ch15-universal]] (information-theory → llm)
- [structural-analogy] Individual-sequence regret ↔ adversarial online learning / no-regret algorithms: competing with the best static predictor in hindsight. — from [[polyanskiy-2025-information/ch15-universal]] (information-theory → other:computer-science)
- [same-math] $C_n$ as capacity of $\theta\mapsto X^n$ ↔ information-theory: redundancy and minimax regret of universal compression — the source states they are the same quantity (p. 604). — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → information-theory)
- [structural-analogy] Online-to-batch conversion ($nR_n^*\le C_n\le\sum R_t^*$) ↔ machine learning: relation between online regret and batch generalization — the same cumulative-versus-last-step logic. — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → llm)
