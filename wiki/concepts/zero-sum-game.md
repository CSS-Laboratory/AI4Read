---
id: zero-sum-game
type: concept
fields: [decision-game-theory, control-theory, linear-algebra]
fields_strong: [decision-game-theory, control-theory, linear-algebra]
n_sources: 18
n_works: 6
tiers: [core]
grounding: digests
sources: [axelrod-1984-cooperation/ch01-problemof, axelrod-1984-cooperation/ch04-live, axelrod-1984-cooperation/ch06-choose, bellman-1957-dp/ch10-x, dixit-2008-art-strategy/ch01-ten, dixit-2008-art-strategy/ch02-games, dixit-2008-art-strategy/ch03-prisoners, dixit-2008-art-strategy/ch05-choice, dixit-2008-art-strategy/ch07-making, dixit-2008-art-strategy/ch09-cooperation, osborne-2004-introduction/ch11-strictly, schelling-1960-conflict/appc-re-p3, schelling-1960-conflict/ch02-essay, schelling-1960-conflict/ch04-toward, schelling-1960-conflict/ch05-enforcement-p2, schelling-1960-conflict/ch06-game, schelling-1960-conflict/ch07-randomization, strang-2023-introduction/ch09-linear]
aliases: [zero-sum-game-minimax, zero-sum-minimax]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# zero-sum-game

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `zero-sum-game-minimax` — 15 digest(s)
- `zero-sum-minimax` — 2 digest(s)

## Canon spine entry

- **zero-sum game & minimax** (decision-game-theory): one player's gain is the other's loss; each guarantees the best worst case (UG)

## Definitions in the sources

### decision-game-theory

- [[axelrod-1984-cooperation/ch01-problemof]] (pp. 5, 14–15): the Senate case is "hardly" zero-sum. Chess contrasts as a game of completely antagonistic interests, where assuming the most feared move is safe [alias `zero-sum-game-minimax`]
- [[axelrod-1984-cooperation/ch04-live]] (p. 77): Axelrod's description of the war at the national level [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[axelrod-1984-cooperation/ch06-choose]] (p. 110): one side's gain is the other's loss; chess is the example. The chapter contrasts it with the Prisoner's Dilemma [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch01-ten]] (p. 37): a game where one side's gain is the other's loss, as in futures trades [alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch02-games]] (p. 52): here only the notion: one player's gain is the other's loss; the authors stress that many games are not zero-sum [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch03-prisoners]] (p. 78): only the contrast is used: the pricing game is not zero-sum, as both are better off at top-left than at bottom-right [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch05-choice]] (pp. 144, 147): payoffs always sum to a constant; minimax payoff equals maximin payoff [alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch07-making]] (p. 219): the early focus on pure conflict [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[dixit-2008-art-strategy/ch09-cooperation]] (p. 255): contrast case: in a zero-sum game it is not possible to make everyone better off; relative-rank games are not zero-sum, since everyone can gain by cutting inputs [alias `zero-sum-game-minimax`]
- [[osborne-2004-introduction/ch11-strictly]] (pp. 339–340): here, a two-player game with exactly reversed preferences; payoffs can be chosen to sum to zero [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[schelling-1960-conflict/appc-re-p3]] (n. 97, p. 374): von Neumann says there could be no theory of games "on these bases" without the minimax theorem [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[schelling-1960-conflict/ch02-essay]] (p. 65): here "minimax" is an outcome either party can secure alone, with no worse threat available [alias `zero-sum-game-minimax`]
- [[schelling-1960-conflict/ch04-toward]] (pp. 105, 127): treated as a limiting case; randomized minimax is "anti-communicative" and self-effacing [alias `zero-sum-minimax`]
- [[schelling-1960-conflict/ch05-enforcement-p2]] (pp. 188–189): pure-conflict contrast case: not being found out matters, and between rational players with full information moving first can never be an advantage [alias `zero-sum-minimax`]
- [[schelling-1960-conflict/ch06-game]] (p. 191): here: pure conflict where minimax makes each decision unilateral, needing no meeting of minds [as `zero-sum game & minimax`; alias `zero-sum-game-minimax`]
- [[schelling-1960-conflict/ch07-randomization]] (p. 202): pure conflict, where randomization prevents the adversary's anticipation [alias `zero-sum-game-minimax`]

### control-theory

- [[bellman-1957-dp/ch10-x]] (p. 285): two players with opposed payoffs, $b_{ij}=-a_{ij}$; the only case with a satisfactory general theory [new]

### linear-algebra

- [[strang-2023-introduction/ch09-linear]] (p. 367–368): payoff matrix, mixed strategies, minimax theorem equivalent to LP duality [alias `zero-sum-game-minimax`; new]

## Instances that use it

- [[oneill-game]] — 4-action zero-sum game tested experimentally — from [[osborne-2004-introduction/ch11-strictly]]

## Candidate bridges

- [structural-analogy] Minimax DP with an adversarial maximizer ↔ robust control and zero-sum games — footnote lists these names (p. 317). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → unspecified)
- [structural-analogy] Competitive optimality ($\Pr$ of winning over another code) ↔ game theory: two-person zero-sum game with payoff $\operatorname{sgn}(l-l')$ — the author states it literally as a zero-sum game, but his results bound probabilities rather than solve for equilibria. — from [[cover-2006-elements/ch05-data-p2]] (information-theory → decision-game-theory)
- [same-math] Maxmin = minmax in a strictly competitive game ↔ decision-game-theory: the equality part of the minimax theorem for zero-sum games — here shown only under the assumption that an equilibrium exists (Prop. 341.1). — from [[osborne-2004-introduction/ch11-strictly]] (decision-game-theory → decision-game-theory)
- [same-math] Max-min rule (A) ↔ decision-game-theory: pure-strategy maximin of a zero-sum game — both choose the action with the best worst case. — from [[simon-1955-behavioral/main]] (decision-game-theory → decision-game-theory)
