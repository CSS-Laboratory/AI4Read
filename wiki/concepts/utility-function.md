---
id: utility-function
type: concept
fields: [decision-game-theory, bayesian, economics-finance, information-theory, linear-algebra, political-science]
fields_strong: [decision-game-theory, bayesian, economics-finance, information-theory, linear-algebra, political-science]
n_sources: 14
n_works: 8
tiers: [core]
grounding: digests
sources: [clark-2017-principles/ch11-problems-p1, deisenroth-2020-mml/ch01-introduction, jaynes-2003-probability/ch13-decision, kahneman-1979-prospect/main, kahneman-2011-thinking/appb-choices, kahneman-2011-thinking/ch25-bernoulli, kahneman-2011-thinking/ch26-prospect, kahneman-2011-thinking/ch27-endowment, mackay-2003-information/ch36-decision, osborne-2004-introduction/ch01-introduction, osborne-2004-introduction/ch02-nash-p1, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch04-mixed-p2, simon-1955-behavioral/main]
raw_ids: [utility function]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# utility-function

## Canon spine entry

- **utility function** (decision-game-theory): a number assigned to options that represents a preference ranking (UG)

## Definitions in the sources

### decision-game-theory

- [[kahneman-1979-prospect/main]] (p. 264): here defined on final asset positions (asset integration, tenet ii) [as `utility function`; work fields: decision-game-theory, economics-finance]
- [[kahneman-2011-thinking/appb-choices]] (pdf 432–433): Bernoulli's subjective value of money, concave; the authors prefer value defined on gains and losses [as `utility function`]
- [[kahneman-2011-thinking/ch25-bernoulli]] (pdf 265): psychological value of wealth; here it rises with diminishing increments (Table 3) [as `utility function`]
- [[kahneman-2011-thinking/ch26-prospect]] (pdf 270): in Bernoulli's model, value attaches to states of wealth
- [[kahneman-2011-thinking/ch27-endowment]] (pdf 281–282): here the indifference map's idea of utility is criticized for depending only on the present state
- [[osborne-2004-introduction/ch01-introduction]] (p. 5): Osborne's "payoff function" $u$ satisfying (5.1); only ordinal information [as `utility function`]
- [[osborne-2004-introduction/ch02-nash-p1]] (p. 12): a payoff function representing preferences. Here only the ordering matters, not the size of differences
- [[osborne-2004-introduction/ch04-mixed-p1]] (p. 100–101): Bernoulli payoff function over deterministic outcomes whose expectation represents lottery preferences; not unique
- [[osborne-2004-introduction/ch04-mixed-p2]] (p. 145): ordinal payoff function for deterministic outcomes; distinct from the Bernoulli function
- [[simon-1955-behavioral/main]] (p. 102): $V(s)$, a cardinal payoff on outcomes [work fields: decision-game-theory, economics-finance]

### bayesian

- [[jaynes-2003-probability/ch13-decision]] (pp. 399–400): Bernoulli's "moral value" of money, taken ∝ log M; not to be taken literally at extremes [new; work fields: bayesian, information-theory]

### information-theory

- [[mackay-2003-information/ch36-decision]] (pp. 451, 454): the payoff $U(x,a)$; may be hard to choose, may be nonlinear, and may not exist for some people's preferences [new; work fields: information-theory, bayesian, decision-game-theory]

### linear-algebra

- [[deisenroth-2020-mml/ch01-introduction]] (p. 12): the measure of how well a model predicts the training data; training optimizes it [new]

### political-science

- [[clark-2017-principles/ch11-problems-p1]] (p. 427): a numerical scale in which higher numbers mean higher positions in a person's preference ordering [new]

## Instances that use it

- [[allais-paradox]] — common preferences that no utility function can represent — from [[mackay-2003-information/ch36-decision]]

## Candidate bridges

- [metaphor] Self-interest assumption that can include concern for others ↔ economics: utility functions that include others' welfare. — from [[axelrod-1984-cooperation/ch01-problemof]] (decision-game-theory → economics-finance)
- [structural-analogy] Less-is-more in single evaluation ↔ utility function: a value that fails to rise when a good is added violates monotonicity. — from [[kahneman-2011-thinking/ch15-linda]] (decision-game-theory → decision-game-theory)
- [structural-analogy] decision utility vs. experienced utility ↔ decision-game-theory: preference relation / utility function — the standard theory judges choices only by internal consistency; here an external standard is added. — from [[kahneman-2011-thinking/ch35-two]] (decision-game-theory → decision-game-theory)
