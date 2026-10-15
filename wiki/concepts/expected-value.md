---
id: expected-value
type: concept
fields: [decision-game-theory, information-theory, linear-algebra]
fields_strong: [decision-game-theory, information-theory, linear-algebra]
n_sources: 4
n_works: 4
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, kahneman-2011-thinking/ch25-bernoulli, osborne-2004-introduction/ch17-mathematics, stone-2022-information/appd-probability]
raw_ids: [expected value]
generated_by: build_kg.py
---

# expected-value

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/ch25-bernoulli]] (pdf 264): probability-weighted average of dollar outcomes, used before Bernoulli [as `expected value`; new]
- [[osborne-2004-introduction/ch17-mathematics]] (p. 451): probability-weighted average $\sum p_ix_i$ of a lottery's numerical outcomes [new]

### information-theory

- [[stone-2022-information/appd-probability]] (p. 257–258): mean obtained as $\sum_i p(x_i)x_i$, or the integral version [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 187–189): $\mathbb E_X[g(x)]$, a linear operator; mean is $g=$ identity [new]

## Instances that use it

- [[stochastic-allocation-two-outcome]] — the two-branch expected-value recurrence — from [[bellman-1957-dp/ch01-i-p3]]
- [[societies-a-and-b-loyalty-example]] — W/S of 0.01 vs 0.1 and expected values $10,000 vs $100,000 — from [[clark-2017-principles/ch10-varieties-p3]]
- [[st-petersburg-paradox]] — infinite expected value, small willingness to pay; mentioned only — from [[kahneman-2011-thinking/ch25-bernoulli]]
- [[roses-vs-cash-gambles]] — 84% chance of $59 vs. roses; anchoring on expected value — from [[kahneman-2011-thinking/ch30-rare]]
- [[marbles-expected-value-simulation]] — 100000 random distributions with mean 1.4 never beat the binomial's entropy — from [[mcelreath-2020-rethinking/ch09-big]]
- [[lottery-12-4-6]] — expected value 7 for $\$12$, $\$4$, $\$6$ with probabilities $\tfrac13,\tfrac12,\tfrac16$ — from [[osborne-2004-introduction/ch17-mathematics]]
- [[st-petersburg-paradox]] — infinite expected value, yet people pay little — from [[thaler-2015-misbehaving/ch04-value]]

## Candidate bridges

- [structural-analogy] Expected-value recursion of §25 ↔ MDP: finite-horizon Bellman equation with two random outcomes. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [metaphor] Averaging out uncontrollable components ↔ certainty-equivalence or expected-value reductions. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → unspecified)
- [same-math] $f^Tp$ for probabilities $p$ ↔ probability: expected value $E[f]=\sum p_if_i$. — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → other:probability)
- [same-math] Expected payoff and critical probability ↔ decision theory: expected-value comparison of two lotteries, here solved as a linear inequality in $p$. — from [[clark-2017-principles/ch08-democratic-p3]] (political-science → decision-game-theory)
- [same-math] Downs's expected return = probability of being decisive × gain from a correct vote ↔ decision theory: expected value compared with marginal cost. Downs states only the verbal logic, so same-math is conditional on that reading. — from [[downs-1957-democracy/main]] (political-science → decision-game-theory)
- [structural-analogy] Fair-game excess return (eqs. 2–5) ↔ economics-finance (no-arbitrage & risk-neutral pricing): expected value of the surprise is zero given the information set; the underlying measure differs. — from [[fama-1970-efficient/main]] (economics-finance → economics-finance)
- [structural-analogy] Decision weights ↔ behavioural finance/insurance pricing: paying above expected value for peace of mind — both price a premium for removing small risks. — from [[kahneman-2011-thinking/ch29-fourfold]] (decision-game-theory → economics-finance)
- [structural-analogy] Coverage × effectiveness ↔ decomposing aggregate effect into reach and per-person effect (as in expected value = probability × size). — from [[katz-1955-personalinfluence/ch07-further]] (communication-theory → unspecified)
- [structural-analogy] Theorem 2.2 (ignore stimuli when attention is costly) ↔ political-science: [[rational-ignorance]] — both say ignorance can be rational when information costs exceed its expected value. — from [[lupia-1998-dilemma/app-ch02]] (political-science → political-science)
- [same-math] first-price equilibrium bid $E[X\mid X<v]$ ↔ order statistics: expected value of the maximum of $n-1$ draws conditional on being below $v$. — from [[osborne-2004-introduction/ch09-bayesian]] (decision-game-theory → other:statistics)
- [same-math] Expected value $\sum p_ix_i$ ↔ decision-game-theory: expected utility — the same weighted average, with utilities as the numbers. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Entropy as average surprisal ↔ statistics: sample mean converging to the expected value $E[\cdot]$ — Eq. 2.74 is a sample mean of $-\log p$, and Eq. 2.58 is its expectation. — from [[stone-2022-information/ch02-entropy]] (information-theory → other:statistics)
