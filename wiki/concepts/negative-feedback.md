---
id: negative-feedback
type: concept
fields: [control-theory, information-theory]
n_sources: 7
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch05-stability, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch04-examples, meadows-2008-thinking/ch02-brief, meadows-2008-thinking/ch05-system, pierce-1980-introduction/ch11-cybernetics, wlezien-1995-thermostat/main]
generated_by: build_kg.py
---

# negative-feedback

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch05-stability]] (p. 80): loop in which a returning displacement diminishes the initial one; a simple stability test that is unreliable if complications are present
- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-3, 2-4, 2-5): lower block $-1$; widens linear range, cuts sensitivity and disturbance effect by $k+1$ in the static model
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. Fig. 4.9 caption, p. 4-9): the op-amp circuit feeds a fraction of the output back against the input, giving a stable amplifier
- [[meadows-2008-thinking/ch02-brief]] (pp. 36, 42): balancing loop (B); pulls a stock toward a goal, e.g., furnace loop, depreciation, deaths
- [[meadows-2008-thinking/ch05-system]] (p. 112): balancing loops hold behaviour in place (here also blocking change in policy resistance)
- [[wlezien-1995-thermostat/main]] (p. 998): a rise in appropriations lowers the public's wish for more spending, and vice versa

### information-theory

- [[pierce-1980-introduction/ch11-cybernetics]] (p. 215): output used to reduce departures from a desired behavior [new]

## Instances that use it

- [[gas-incubator]] — continuous error-controlled regulator with negative feedback — from [[ashby-1956-cybernetics/ch12-error]]
- [[centrifugal-governor]] — flyball negative feedback on steam-engine speed — from [[astrom-2021-feedbacksystems/ch01-introduction]]
- [[black-feedback-amplifier]] — negative feedback linearizes a nonlinear tube amplifier at the cost of gain — from [[astrom-2021-feedbacksystems/ch01-introduction]]
- [[saturating-static-loop]] — the $\operatorname{sat}$ process with gain $k$, positive or negative feedback — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[black-feedback-amplifier]] — negative feedback around a nonlinear amplifier — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[gene-self-repression]] — negative feedback attenuates low-frequency noise — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]]

## Candidate bridges

- [structural-analogy] TCP window halving on loss and growth otherwise ↔ negative feedback with quantized actions — the window shrinks when the congestion signal appears. — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [structural-analogy] Self-repressing gene attenuating disturbance ↔ negative feedback in engineered loops: lower low-frequency sensitivity. — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (control-theory → control-theory)
- [structural-analogy] Condition (iv), investment reversing its own marginal efficiency of capital ↔ negative feedback in cyclical models. — from [[keynes-1936-general/ch18-general]] (economics-finance → unspecified)
- [structural-analogy] balancing loop with discrepancy ↔ control theory: negative feedback on error signal = reference − output. The thermostat's discrepancy is an error signal, but it is floored at 0 and the furnace heat is capped at 5 (p. 197). — from [[meadows-2008-thinking/app-untitled]] (control-theory → control-theory)
- [structural-analogy] Balancing loop with desired level and discrepancy ↔ control theory: negative feedback with reference and error signal — same loop structure, in plain-language diagrams rather than equations. — from [[meadows-2008-thinking/ch01-basics]] (control-theory → control-theory)
- [structural-analogy] Pheromone reinforcement and evaporation ↔ positive and negative feedback in dynamical systems. — from [[mitchell-2009-guidedtour/ch12-information]] (complex-systems → unspecified)
