---
id: mixed-strategy
type: concept
fields: [decision-game-theory, control-theory]
n_sources: 15
tiers: [core]
grounding: digests
sources: [bellman-1957-dp/ch10-x, dixit-2008-art-strategy/ch01-ten, dixit-2008-art-strategy/ch04-beautiful, dixit-2008-art-strategy/ch05-choice, dixit-2008-art-strategy/ch08-interpreting, dixit-2008-art-strategy/ch14-case, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch04-mixed-p2, osborne-2004-introduction/ch09-bayesian, osborne-2004-introduction/ch11-strictly, osborne-2004-introduction/ch13-evolutionary, schelling-1960-conflict/appc-re-p2, schelling-1960-conflict/appc-re-p3, schelling-1960-conflict/ch04-toward, schelling-1960-conflict/ch07-randomization]
raw_ids: [mixed strategy]
canon_spine: decision-game-theory
generated_by: build_kg.py
---

# mixed-strategy

## Canon spine entry

- **mixed strategy** (decision-game-theory): randomizing over actions; guarantees equilibrium existence (UG)

## Definitions in the sources

### decision-game-theory

- [[dixit-2008-art-strategy/ch01-ten]] (pp. 34–35): randomizing or being unpredictable so the other side cannot exploit a pattern
- [[dixit-2008-art-strategy/ch04-beautiful]] (pp. 111, 138): mixing moves; needed for existence in general
- [[dixit-2008-art-strategy/ch05-choice]] (p. 141, 144): choosing among pure strategies at random with chosen proportions
- [[dixit-2008-art-strategy/ch08-interpreting]] (p. 245): randomizing so that actions reveal information only partly
- [[dixit-2008-art-strategy/ch14-case]] (p. 398): equilibrium when budgets are unknown in the dollar auction [as `mixed strategy`]
- [[osborne-2004-introduction/ch04-mixed-p1]] (p. 105): a probability distribution over a player's actions; pure strategy = probability 1 on one action
- [[osborne-2004-introduction/ch04-mixed-p2]] (p. used throughout; p. 126): a probability distribution over a player's actions; payoffs are expected values
- [[osborne-2004-introduction/ch09-bayesian]] (p. 304): used in the symmetric jury equilibrium
- [[osborne-2004-introduction/ch11-strictly]] (pp. 337–338): used to raise the guaranteed payoff [as `mixed strategy`]
- [[osborne-2004-introduction/ch13-evolutionary]] (pp. 286, 288–289): can be inherited or mutated. Read as one randomizing organism or a polymorphic population [as `mixed strategy`]
- [[schelling-1960-conflict/appc-re-p2]] (pp. 359–360): randomising over choices; here it reduces conflict, as in the card-table game
- [[schelling-1960-conflict/appc-re-p3]] (n. 98, p. 374): also read as adding continuity to a discrete game, giving it a saddle point [as `mixed strategy`]
- [[schelling-1960-conflict/ch04-toward]] (pp. 117–118): randomizing as a tool that destroys communication and labels; in a common-interest game a random device can only guarantee that tacit cooperation is impossible
- [[schelling-1960-conflict/ch07-randomization]] (p. 203): randomizing over actions; here the main role is making objects, promises and threats divisible, not mainly disguising play

### control-theory

- [[bellman-1957-dp/ch10-x]] (p. 285): a probability distribution over one's plays, used to protect against the opponent [new]

## Instances that use it

- [[football-mixed-strategy]] — mixing run and pass can beat both pure strategies for a rare large gain — from [[cover-2006-elements/ch12-information-p2]]
- [[card-table-seating-game]] — mixed-strategy equilibrium worth an expected $2 apiece — from [[schelling-1960-conflict/appc-re-p2]]
- [[game-mixed-strategy-25]] — payoff [1 0 4; 3 −1 2]; x* = (¼,¾), y* = (½,0,½), value 2.5 — from [[strang-2023-introduction/ch09-linear]]

## Candidate bridges

- [same-math] Strictly dominated by a mixed strategy ↔ the dominance notion used in iterated elimination of dominated strategies: the same definition used on a different footing. — from [[osborne-2004-introduction/ch12-rationalizability]] (decision-game-theory → other)
- [same-math] Mixed ESS as a polymorphic population (fractions = probabilities) ↔ mixed-strategy equilibrium interpreted as population proportions (the author cites Section 4.1) (p. 289). — from [[osborne-2004-introduction/ch13-evolutionary]] (decision-game-theory → unspecified)
- [structural-analogy] Cumulative distribution on a continuum ↔ mixed strategy over a continuum of actions: the chapter points to Section 4.11 for this use. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → other)
- [metaphor] Least-favorable prior ↔ capacity-achieving input distribution: the adversary's best mixed strategy. — from [[polyanskiy-2025-information/ch31-basics]] (information-theory → other)
- [structural-analogy] fractional threat probability $\pi$ ↔ mixed strategy: both are probability distributions over actions, but here the odds are meant to be learned by the other player. — from [[schelling-1960-conflict/ch07-randomization]] (decision-game-theory → other)
