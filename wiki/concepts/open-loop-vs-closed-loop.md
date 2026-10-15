---
id: open-loop-vs-closed-loop
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 9
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch04-examples, liberzon-2012-calculus/ch04-maximum-p2, liberzon-2012-calculus/ch05-hamilton, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch07-living, todorov-2002-ofc/main]
raw_ids: [open loop vs closed loop]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# open-loop-vs-closed-loop

## Canon spine entry

- **open loop vs closed loop** (control-theory): acting on a fixed plan versus acting on measured results (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch12-error]] (p. 223): Ashby's closed-loop regulator is the error-controlled one with feedback from E to R [as `open loop vs closed loop`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-1): closed: systems interconnected in a cycle; open: the interconnection is broken [as `open loop vs closed loop`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-2): open loop is controller plus process without feedback, $y=\operatorname{sat}(kr)$
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-21): "two pills three times a day" is open loop
- [[liberzon-2012-calculus/ch04-maximum-p2]] (p. 109): the principle gives open-loop controls; the double-integrator solution is state feedback
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 135): maximum principle gives $u^*(t)$ via costate (open); HJB gives $u^*$ from the current state (closed) [as `open loop vs closed loop`]
- [[meadows-2008-thinking/ch01-basics]] (p. 27): Meadows contrasts systems with feedback loops with open-ended chains of stocks and flows whose stock levels do not affect the flows
- [[meadows-2008-thinking/ch07-living]] (p. 177): a static, unbending policy versus a policy that changes with the system's state [as `open loop vs closed loop`]
- [[todorov-2002-ofc/main]] (pp. 2, 6): the desired-trajectory view executes a plan open loop. Optimal feedback uses online information

## Candidate bridges

- [metaphor] passive shell versus skilled fencer ↔ control-theory: fixed design versus information-using control (open-loop vs closed-loop). — from [[ashby-1956-cybernetics/ch10-regulation]] (control-theory → control-theory)
