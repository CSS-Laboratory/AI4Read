---
id: competitive-optimality
type: concept
fields: [information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch05-data-p2, cover-2006-elements/ch15-information]
generated_by: build_kg.py
---

# competitive-optimality

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch05-data-p2]] (pp. 107–110): a code beats another more often than it loses; Shannon code is uniquely so for dyadic $p$ [new]
- [[cover-2006-elements/ch15-information]] (p. 472): one-period result $\Pr(VS\ge U^*S^*)\le\frac12$ with fair randomization [new]

## Candidate bridges

- [structural-analogy] Competitive optimality ($\Pr$ of winning over another code) ↔ game theory: two-person zero-sum game with payoff $\operatorname{sgn}(l-l')$ — the author states it literally as a zero-sum game, but his results bound probabilities rather than solve for equilibria. — from [[cover-2006-elements/ch05-data-p2]] (information-theory → decision-game-theory)
- [structural-analogy] Competitive optimality of $\mathbf b^*$ ↔ competitive optimality of Shannon codes (Chapter 5): the source calls the two results similar (p. 471); here the proof uses $E[S/S^*]\le1$ plus Markov. — from [[cover-2006-elements/ch15-information]] (information-theory → other)
