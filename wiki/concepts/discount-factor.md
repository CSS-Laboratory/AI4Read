---
id: discount-factor
type: concept
fields: [control-theory, decision-game-theory, political-science]
fields_strong: [control-theory, decision-game-theory, political-science]
n_sources: 4
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p2, clark-2017-principles/ch04-origins-p2, osborne-2004-introduction/ch14-repeated, recht-2019-tour/main]
generated_by: build_kg.py
---

# discount-factor

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 43): $\alpha<1$ weights future costs less and makes the infinite sum finite for bounded $g$ [new]
- [[recht-2019-tour/main]] (pp. 7–8): $\gamma\in(0,1)$ in (3.5), used to get a simple Bellman equation; large $\gamma$ can make methods brittle [new]

### decision-game-theory

- [[osborne-2004-introduction/ch14-repeated]] (pp. 391–392): weight δ ∈ (0, 1) per period of delay. With borrowing and lending at rate $r$, δ = 1/(1+r) [new]

### political-science

- [[clark-2017-principles/ch04-origins-p2]] (p. 138): $d$ with $0\le d\le1$; how much future benefits are valued relative to today's [new]

## Instances that use it

- [[iterated-prisoners-dilemma]] — the game with discount factor w — from [[axelrod-1984-cooperation/appb-proofs]]

## Candidate bridges

- [structural-analogy] Discount parameter $w$ ↔ economics/finance: discount factor on future payoffs. The same geometric weighting, but here $w$ also stands for the chance of the relationship ending. — from [[axelrod-1984-cooperation/ch01-problemof]] (decision-game-theory → economics-finance)
- [structural-analogy] $w$, probability of meeting again ↔ repeated games: discount factor/patience in the folk theorem — both make future payoffs matter. — from [[axelrod-1984-cooperation/ch05-evolution]] (decision-game-theory → decision-game-theory)
- [same-math] Theorem 1's contraction argument, $u_{N+1}\le q\,u_N$ ↔ control-theory: value iteration for discounted Bellman equations — the survival probability $p_i<1$ plays the role of a discount factor. — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] Interest rate and the value of the future (p. 93) ↔ repeated games: the discount factor balances short-term gain against long-term loss. — from [[dixit-2008-art-strategy/ch03-prisoners]] (decision-game-theory → decision-game-theory)
- [same-math] discount factor δ = 1/(1+r) ↔ finance: present value of a payment stream at interest rate $r$ — the text derives δ from borrowing and lending (p. 392). — from [[osborne-2004-introduction/ch14-repeated]] (decision-game-theory → economics-finance)
