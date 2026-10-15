---
id: reference-set-point
type: concept
fields: [control-theory, economics-finance, political-science]
fields_strong: [control-theory, economics-finance, political-science]
n_sources: 13
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch11-pid, maxwell-1868-governors/main, meadows-2008-thinking/app-untitled, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch02-brief, meadows-2008-thinking/ch05-system, meadows-2008-thinking/ch06-leverage, taylor-1993-discretion/main, wlezien-1995-thermostat/main]
raw_ids: [reference (set point)]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# reference-set-point

## Canon spine entry

- **reference (set point)** (control-theory): the target value the controller tries to hold (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch12-error]] (p. 219): Ashby's η is the given set of acceptable states of E, not a single value (p. 219). The match is loose. [as `reference (set point)`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-4, 1-16): desired output $r$ (also "setpoint" for inner loops) [as `reference (set point)`]
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-1, p. 4-18): $v_r$ for speed, a deflection reference for the AFM
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-10): constant target value $r$ for $y$
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-2): command signal $r$, called setpoint in PID literature [as `reference (set point)`]
- [[maxwell-1868-governors/main]] (p. 271): the "normal velocity" $V$ the governor returns to [as `reference (set point)`]
- [[meadows-2008-thinking/app-untitled]] (pp. 189, 197): the loop's "goal" (e.g. thermostat setting 18°C), used loosely here [as `reference (set point)`]
- [[meadows-2008-thinking/ch01-basics]] (pp. 27, 29): the desired level or goal, e.g. desired energy level, room temperature
- [[meadows-2008-thinking/ch02-brief]] (pp. 36, 40, 63): the goal of a loop (thermostat setting, desired inventory, growth goal); here it must include compensation for leaks
- [[meadows-2008-thinking/ch05-system]] (pp. 113, 122): the goal or desired state compared with the actual state
- [[meadows-2008-thinking/ch06-leverage]] (pp. 153, 161): here called the "goal" of a balancing loop (thermostat setting) or of the whole system. Meadows ranks the whole-system goal above self-organization [as `reference (set point)`]
- [[taylor-1993-discretion/main]] (p. 202): the 2 percent inflation target and the output trend $Y^*$ in the rule [as `reference (set point)`; work fields: control-theory, economics-finance]
- [[wlezien-1995-thermostat/main]] (p. 982; p. 987): the public's preferred level of policy, $P^*$, which itself can change and is unobserved [work fields: control-theory, political-science]

## Candidate bridges

- [structural-analogy] System "goal" as leverage ↔ control theory: reference (set point) — changing the reference moves where the loop settles, while tuning changes speed. — from [[meadows-2008-thinking/ch06-leverage]] (control-theory → control-theory)
