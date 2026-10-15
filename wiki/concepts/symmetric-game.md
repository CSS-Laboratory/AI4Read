---
id: symmetric-game
type: concept
fields: [decision-game-theory]
fields_strong: [decision-game-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [osborne-2004-introduction/ch02-nash-p2, osborne-2004-introduction/ch03-nash-p2]
generated_by: build_kg.py
---

# symmetric-game

## Definitions in the sources

### decision-game-theory

- [[osborne-2004-introduction/ch02-nash-p2]] (p. 49): same action sets and $u_1(a_1,a_2)=u_2(a_2,a_1)$ [new]
- [[osborne-2004-introduction/ch03-nash-p2]] (p. 77): same action sets and payoff of $(t_1,t_2)$ to 1 equals payoff of $(t_2,t_1)$ to 2 [new]

## Instances that use it

- [[alphazero-td-gammon-common-policy]] — common policy trained for both players in symmetric games; no reliable theory — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[prisoners-dilemma]] — *Fink* strictly dominates *Quiet*; symmetric game — from [[osborne-2004-introduction/ch02-nash-p2]]
- [[approaching-pedestrians]] — symmetric game (both step the same way is better) with two symmetric equilibria — from [[osborne-2004-introduction/ch02-nash-p2]]
- [[war-of-attrition]] — equilibria with no fight, asymmetric even in a symmetric game — from [[osborne-2004-introduction/ch03-nash-p2]]
- [[approaching-pedestrians]] — symmetric game with two pure and one mixed symmetric equilibrium; half of encounters collide in the mixed one — from [[osborne-2004-introduction/ch04-mixed-p2]]

## Candidate bridges

- [metaphor] foot race of equals ↔ symmetric games: when the outcome is foregone, tactics lose meaning — from [[schelling-1960-conflict/appb-abandonment]] (decision-game-theory → other:symmetric-games)
