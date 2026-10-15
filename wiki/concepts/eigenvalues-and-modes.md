---
id: eigenvalues-and-modes
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 8
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch06-black, astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch15-architecture-p2, bellman-1957-dp/ch11-xi, maxwell-1868-governors/main]
raw_ids: [eigenvalues and modes]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# eigenvalues-and-modes

## Canon spine entry

- **eigenvalues and modes** (control-theory): a linear system is stable when every eigenvalue of A has negative real part (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch06-black]] (p. 101): only loosely related: "normal modes" retained under normal-coordinate transformation [as `eigenvalues and modes`; weak: not really used in this unit]
- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-13): linear $\dot x=Ax$ is asymptotically stable iff all $\mathrm{Re}\,\lambda<0$ (Thm 5.1) [as `eigenvalues and modes`]
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-13): an eigenpair gives a mode $e^{\lambda t}v$; the eigenvector is the mode shape
- [[astrom-2021-feedbacksystems/ch07-state]] (pp. 7-17, 7-22): closed-loop eigenvalue locations determine the closed-loop behavior; the dominant pair often determines the step response
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-24): poles of a state-space system are the eigenvalues of $A$; unforced motion is a sum of modes [as `eigenvalues and modes`]
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-28): the cancelled mode has an eigenvalue at the origin
- [[bellman-1957-dp/ch11-xi]] (p. 329): canon concept; here used for the growth rate $\lambda$ of the max-linear recurrence [as `eigenvalues and modes`]
- [[maxwell-1868-governors/main]] (pp. 271, 276): here the roots $n$ of the characteristic equation; each gives a mode $e^{nt}$ [as `eigenvalues and modes`]

## Candidate bridges

- [structural-analogy] "The system causes its own behavior" ↔ control-theory: eigenvalues and modes — a linear system's natural modes are set by its own dynamics matrix; an input only excites them. — from [[meadows-2008-thinking/ch00-introduction]] (control-theory → control-theory)
