---
id: positive-feedback
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 10
n_works: 3
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch05-stability, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, meadows-2008-thinking/app-untitled, meadows-2008-thinking/ch00-introduction, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch02-brief, meadows-2008-thinking/ch04-systems, meadows-2008-thinking/ch05-system, meadows-2008-thinking/ch06-leverage]
aliases: [positive-reinforcing-feedback]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# positive-feedback

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `positive-reinforcing-feedback` — 6 digest(s)

## Canon spine entry

- **positive (reinforcing) feedback** (control-theory): the correction amplifies the deviation, producing growth, runaway or switching (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch05-stability]] (p. 81): each variable raises the other; Ashby shows this can still be stable
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-2): an increase leads to further increase; destabilizing, usually limited by saturation [as `positive (reinforcing) feedback`; alias `positive-reinforcing-feedback`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-4, 2-5): lower block $+1$; gain $k/(1-k)$, shrunken linear range, higher sensitivity, hysteresis for $k>1$
- [[meadows-2008-thinking/app-untitled]] (pp. 187, 189): amplifying loop giving exponential growth or runaway collapse [as `positive (reinforcing) feedback`; alias `positive-reinforcing-feedback`]
- [[meadows-2008-thinking/ch00-introduction]] (p. 3): a loop that rewards winners with means to win more (competitive exclusion) [as `positive (reinforcing) feedback`; alias `positive-reinforcing-feedback`]
- [[meadows-2008-thinking/ch01-basics]] (p. 31): reinforcing loop (R): amplifies imposed change, giving exponential growth or collapse [alias `positive-reinforcing-feedback`]
- [[meadows-2008-thinking/ch02-brief]] (pp. 42, 49): reinforcing loop (R); drives exponential growth, e.g., births, investment of output
- [[meadows-2008-thinking/ch04-systems]] (p. 89): loop that generates exponential growth [as `positive (reinforcing) feedback`; alias `positive-reinforcing-feedback`]
- [[meadows-2008-thinking/ch05-system]] (pp. 117, 122, 124, 127, 135): reinforcing loops drive erosion, escalation, winner-take-all and addiction
- [[meadows-2008-thinking/ch06-leverage]] (p. 155): self-reinforcing loop, a source of growth, erosion and collapse [as `positive (reinforcing) feedback`; alias `positive-reinforcing-feedback`]

## Instances that use it

- [[superregenerative-amplifier]] — positive feedback gives gain 999 but is highly sensitive — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[schmitt-trigger-memory]] — positive feedback with saturation gives hysteresis — from [[astrom-2021-feedbacksystems/ch02-feedback]]

## Candidate bridges

- [structural-analogy] Feedback instability (microphone howl) ↔ positive feedback / runaway in markets or ecosystems — same loop-gain logic, but the chapter does not develop it. — from [[astrom-2021-feedbacksystems/ch01-introduction]] (control-theory → unspecified)
- [structural-analogy] Hysteresis from positive feedback with saturation ↔ bistable switches with two stable states — the same equilibrium-and-slope picture (stable where $G'>0$). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → unspecified)
- [metaphor] Positive feedback in bank runs, stampedes, boom-bust (p. 2-24) ↔ social dynamics: herding and self-reinforcing behaviour; the chapter gives no model for these. — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → other:social-dynamics)
- [metaphor] Ethnic outbidding as a "downward spiral" ↔ positive feedback loops in dynamical systems. — from [[clark-2017-principles/ch16-consequences-p3]] (political-science → unspecified)
- [metaphor] Phase-locking of agents into waves ↔ physics: positive-feedback oscillation — Jaynes's hedged economic analogy. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → other:physics)
- [structural-analogy] availability cascade ↔ network science: positive-feedback information cascades — each round of attention raises the next. — from [[kahneman-2011-thinking/ch13-availability]] (decision-game-theory → complex-systems)
- [structural-analogy] Reinforcing loop rewards winners ↔ control-theory: positive feedback — a deviation amplifies itself. — from [[meadows-2008-thinking/ch00-introduction]] (control-theory → control-theory)
- [structural-analogy] Reinforcing loop ↔ control theory: positive feedback — the stock's size sets its own growth rate. — from [[meadows-2008-thinking/ch01-basics]] (control-theory → control-theory)
- [structural-analogy] Deviation-amplifying system ↔ complex systems: positive feedback — reactions reinforce, not damp, a movement. — from [[minsky-1992-instability/main]] (economics-finance → complex-systems)
- [structural-analogy] Pheromone-weighted trail choice ↔ codelet resource allocation by promise: positive feedback plus residual random search. — from [[mitchell-2009-guidedtour/ch13-make]] (complex-systems → other:codelet-resource-allocation-by)
- [structural-analogy] Nervousness model (coupled "fear" functions) ↔ dynamics: two-variable positive feedback, stable if loop gain (product of slopes) is below 1. — from [[schelling-1960-conflict/ch09-reciprocal]] (decision-game-theory → complex-systems)
- [structural-analogy] cumulative evacuation ↔ positive feedback — each departure raises the ratio pressure on those who remain. — from [[schelling-1971-segregation/main-p2]] (complex-systems → unspecified)
