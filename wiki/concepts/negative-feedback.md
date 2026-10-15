---
id: negative-feedback
type: concept
fields: [control-theory, economics-finance, information-theory, political-science]
fields_strong: [control-theory, information-theory, political-science]
n_sources: 17
n_works: 7
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch05-stability, ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch04-examples, maxwell-1868-governors/main, meadows-2008-thinking/app-untitled, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch02-brief, meadows-2008-thinking/ch03-systems, meadows-2008-thinking/ch04-systems, meadows-2008-thinking/ch05-system, meadows-2008-thinking/ch06-leverage, meadows-2008-thinking/ch07-living, pierce-1980-introduction/ch11-cybernetics, taylor-1993-discretion/main, wlezien-1995-thermostat/main]
aliases: [negative-balancing-feedback]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# negative-feedback

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `negative-balancing-feedback` — 10 digest(s)

## Canon spine entry

- **negative (balancing) feedback** (control-theory): the correction opposes the deviation, pulling the system toward a goal (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch05-stability]] (p. 80): loop in which a returning displacement diminishes the initial one; a simple stability test that is unreliable if complications are present
- [[ashby-1956-cybernetics/ch12-error]] (p. 237): for a regulator that must be stable with the desired temperature as its equilibrium, the feedback around the circuit must "usually" be negative [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-2): reacting to disturbances so their effects decrease [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-3, 2-4, 2-5): lower block $-1$; widens linear range, cuts sensitivity and disturbance effect by $k+1$ in the static model
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. Fig. 4.9 caption, p. 4-9): the op-amp circuit feeds a fraction of the output back against the input, giving a stable amplifier
- [[maxwell-1868-governors/main]] (p. 271): the correction opposes the speed deviation, though Maxwell does not use this term [as `negative (balancing) feedback`; alias `negative-balancing-feedback`; weak: not really used in this unit]
- [[meadows-2008-thinking/app-untitled]] (p. 187): stabilizing, goal-seeking loop that opposes imposed change [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[meadows-2008-thinking/ch01-basics]] (p. 28): balancing loop (B): goal-seeking, opposes imposed change [alias `negative-balancing-feedback`]
- [[meadows-2008-thinking/ch02-brief]] (pp. 36, 42): balancing loop (B); pulls a stock toward a goal, e.g., furnace loop, depreciation, deaths
- [[meadows-2008-thinking/ch03-systems]] (p. 76): a single balancing loop returns a stock to its desired state [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[meadows-2008-thinking/ch04-systems]] (p. 89): goal-seeking loop that approaches or holds equilibrium [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[meadows-2008-thinking/ch05-system]] (p. 112): balancing loops hold behaviour in place (here also blocking change in policy resistance)
- [[meadows-2008-thinking/ch06-leverage]] (p. 153): loop that keeps a stock near its goal. Needs goal, monitor and response [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[meadows-2008-thinking/ch07-living]] (p. 177): the gasoline tax rises as imports rise and falls as they fall, pushing imports back down [as `negative (balancing) feedback`; alias `negative-balancing-feedback`]
- [[taylor-1993-discretion/main]] (p. 202): the rate rises when inflation or output is above target and falls when below (canon link; not named by the author) [as `negative (balancing) feedback`; alias `negative-balancing-feedback`; weak: not really used in this unit; work fields: control-theory, economics-finance]
- [[wlezien-1995-thermostat/main]] (p. 998): a rise in appropriations lowers the public's wish for more spending, and vice versa [work fields: control-theory, political-science]

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
