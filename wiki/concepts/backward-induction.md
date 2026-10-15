---
id: backward-induction
type: concept
fields: [decision-game-theory, political-science, economics-finance]
fields_strong: [decision-game-theory, political-science, economics-finance]
n_sources: 19
n_works: 7
tiers: [core]
grounding: digests
sources: [axelrod-1984-cooperation/ch01-problemof, clark-2017-principles/ch03-politics, dixit-2008-art-strategy/ch01-ten, dixit-2008-art-strategy/ch02-games, dixit-2008-art-strategy/ch03-prisoners, dixit-2008-art-strategy/ch06-strategic, dixit-2008-art-strategy/ch07-making, dixit-2008-art-strategy/ch09-cooperation, dixit-2008-art-strategy/ch11-bargaining, dixit-2008-art-strategy/ch12-voting, dixit-2008-art-strategy/ch14-case, dixit-2008-art-strategy/ch15-workouts, osborne-2004-introduction/ch05-extensive, osborne-2004-introduction/ch06-extensive, osborne-2004-introduction/ch07-extensive, schelling-1960-conflict/ch05-enforcement-p2, schelling-1960-conflict/ch09-reciprocal, shepsle-2010-analyzing/ch06-strategic, simon-1955-behavioral/main]
raw_ids: [backward induction]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# backward-induction

## Canon spine entry

- **backward induction** (decision-game-theory): solving a sequential game from the end backwards (UG)

## Definitions in the sources

### decision-game-theory

- [[axelrod-1984-cooperation/ch01-problemof]] (p. 10): here the "unravelling" argument: in a game of known finite length, defection spreads back to move one
- [[dixit-2008-art-strategy/ch01-ten]] (pp. 17, 23): reasoning from where the game ends to the choice now; announced for chapter 2 and used informally in Survivor
- [[dixit-2008-art-strategy/ch02-games]] (p. 47): Rule 1: look forward and reason backward from the end of the tree to choose the current move
- [[dixit-2008-art-strategy/ch03-prisoners]] (p. 86): used to argue that defection unravels back to round 1 in a finitely repeated dilemma [as `backward induction`]
- [[dixit-2008-art-strategy/ch06-strategic]] (p. 175): used to solve the alarm tree
- [[dixit-2008-art-strategy/ch07-making]] (p. 210): look forward and reason backward; shows why trust unravels from a known last step [as `backward induction`]
- [[dixit-2008-art-strategy/ch09-cooperation]] (pp. 273–274): "looking ahead and reasoning backward": used by the incumbent politician; advised for the associates as a group
- [[dixit-2008-art-strategy/ch11-bargaining]] (pp. 310–311): solve from the last round, so today's offer matches what waiting would bring [as `backward induction`]
- [[dixit-2008-art-strategy/ch12-voting]] (p. 338): the judges look ahead and reason backward to find what each early vote really decides
- [[dixit-2008-art-strategy/ch14-case]] (pp. 378, 381, 397): solving from the last move back; the book's "look forward and reason backward" [as `backward induction`]
- [[dixit-2008-art-strategy/ch15-workouts]] (p. 409): solve from the end: positions leaving the rival a winning move are losing
- [[osborne-2004-introduction/ch05-extensive]] (pp. 156, 168–170): solving subgames from the shortest to the longest; with ties, trace each combination of optimal actions [as `backward induction`]
- [[osborne-2004-introduction/ch06-extensive]] (pp. 180, 185, 191, 195): solve the last decisions first, then earlier ones given those answers; used in all the applications
- [[osborne-2004-introduction/ch07-extensive]] (pp. 205–206): as before, but simultaneous-move subgames are solved as strategic games, so pure equilibria may not exist [as `backward induction`]
- [[schelling-1960-conflict/ch05-enforcement-p2]] (p. 184): computing last moves first, then earlier ones. Schelling says deletion is identifiable with it
- [[schelling-1960-conflict/ch09-reciprocal]] (p. 250): the sequential version is solved from the last move back
- [[simon-1955-behavioral/main]] (p. 117): computing $d(i)$ backward from the last day [work fields: decision-game-theory, economics-finance]

### political-science

- [[clark-2017-principles/ch03-politics]] (p. 58): reasoning from the last choice node back to the first, choosing the best action at each node given later play (p. 58) (new)
- [[shepsle-2010-analyzing/ch06-strategic]] (p. 163): solve a sequence of choices from the last mover back; earlier movers substitute later movers' actual choices [new]

## Instances that use it

- [[senate-race-game]] — preemptive advertising to deter a challenger, solved by backward induction (pp. 76–79) (new) — from [[clark-2017-principles/ch03-politics]]
- [[flag-game]] — backward induction; losing totals 5, 9, …, 21 — from [[dixit-2008-art-strategy/ch15-workouts]]
- [[game-fig-158-1]] — player 1 moves twice; strategies count off-path actions; backward induction gives (DG, E) — from [[osborne-2004-introduction/ch05-extensive]]
- [[synergistic-relationship-sequential]] — continuous-action backward induction: $a_1=\tfrac32c$, $a_2=\tfrac54c$ — from [[osborne-2004-introduction/ch05-extensive]]

## Candidate bridges

- [structural-analogy] Finite-horizon unravelling of cooperation ↔ game theory: backward induction in finitely repeated games. — from [[axelrod-1984-cooperation/ch01-problemof]] (decision-game-theory → decision-game-theory)
- [same-math] Backward induction in the Transition Game ↔ other game trees in the book (Ch. 3) — the same solution method — from [[clark-2017-principles/ch08-democratic-p2]] (political-science → unspecified)
- [same-math] Rule 1, backward reasoning ↔ decision-game-theory: backward induction / subgame-perfect equilibrium — same procedure on a finite tree with perfect information. — from [[dixit-2008-art-strategy/ch02-games]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Unraveling from a known last step ↔ backward induction in finitely repeated games (p. 210). — from [[dixit-2008-art-strategy/ch07-making]] (decision-game-theory → unspecified)
- [structural-analogy] Agenda order reduced by looking ahead ↔ backward induction in extensive-form games — each early vote is replaced by the later outcome it implies. — from [[dixit-2008-art-strategy/ch12-voting]] (decision-game-theory → unspecified)
- [structural-analogy] Sunk-cost fallacy ↔ backward induction: both say only future payoffs should guide the current choice, and past costs should be ignored. — from [[kahneman-2011-thinking/ch32-keeping]] (decision-game-theory → decision-game-theory)
- [metaphor] Binary-agenda backward induction ↔ dynamic programming: solving from the last stage backward. — from [[osborne-2004-introduction/ch07-extensive]] (decision-game-theory → control-theory)
- [structural-analogy] warning-bell argument ↔ backward induction: reasoning from the last moment to what earlier play can achieve — from [[schelling-1960-conflict/appb-abandonment]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Commitment and first-mover advantage ↔ extensive-form games and backward induction: committing first changes the later player's best response. — from [[schelling-1960-conflict/ch02-essay]] (decision-game-theory → decision-game-theory)
- [same-math] Elimination of dominated rows and columns in Fig. 16 ↔ backward induction: Schelling identifies the two procedures (p. 184). — from [[schelling-1960-conflict/ch05-enforcement-p2]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Backward induction on a game tree ↔ dynamic programming: choose by working back from the final stage. — from [[shepsle-2010-analyzing/ch06-strategic]] (political-science → control-theory)
- [structural-analogy] Appendix recursion (A.10) ↔ decision-game-theory: backward induction — solve the last period first, then earlier ones. — from [[simon-1955-behavioral/main]] (decision-game-theory → decision-game-theory)
