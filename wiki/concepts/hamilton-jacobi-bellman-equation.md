---
id: hamilton-jacobi-bellman-equation
type: concept
fields: [control-theory]
n_sources: 9
tiers: [core, deep, reference]
grounding: digests
sources: [bellman-1957-dp/ch03-iii, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bertsekas-2026-rlcourse/ch02-approximation-p4, liberzon-2012-calculus/ch05-hamilton, liberzon-2012-calculus/ch06-linear, liberzon-2012-calculus/ch07-advanced, todorov-2002-ofc/main]
raw_ids: [Hamilton–Jacobi–Bellman equation]
canon_spine: control-theory
generated_by: build_kg.py
---

# hamilton-jacobi-bellman-equation

## Canon spine entry

- **Hamilton–Jacobi–Bellman equation** (control-theory): the continuous-time Bellman equation, a PDE for the value function (grad)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch03-iii]] (p. 86): the name does not appear; the limit of (6.2) as $S\to0$ is a nonlinear PDE, treated in Ch. IX
- [[bellman-1957-dp/ch06-vi]] (p. 193): the author calls (9.3) a nonlinear PDE. The HJB name is not used in this unit (canon link; not stated in this unit) [as `Hamilton–Jacobi–Bellman equation`]
- [[bellman-1957-dp/ch08-viii]] (p. 223): the limiting first-order equation (2.3) is of this kind (canon link; not named in this unit). Bellman rejects it as the working route
- [[bellman-1957-dp/ch09-ix]] (p. 252): the limiting PDE $0=\max_v[F+Gf_c-f_T]$ (name not used in this unit; same equation)
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 256): PDE (2.67) satisfied by a policy's cost; implies (2.63) when $H_t=J_{\pi,t}$
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 130): PDE (5.10) for $V$; equivalently $V_t=\sup_uH(t,x,u,-V_x)$ [as `Hamilton–Jacobi–Bellman equation`]
- [[liberzon-2012-calculus/ch06-linear]] (p. 149): specialised to (6.16), used as sufficient condition
- [[liberzon-2012-calculus/ch07-advanced]] (p. 170): its characteristic strips are Hamilton's canonical equations [as `Hamilton–Jacobi–Bellman equation`]
- [[todorov-2002-ofc/main]] (p. 9): the equation $v^*$ satisfies; no analytical solution in general

## Candidate bridges

- [structural-analogy] Equation (2.3) as the limit of a Bellman recursion ↔ control-theory: Hamilton–Jacobi–Bellman equation — Bellman himself compares his intermediate approach to the heat equation versus Chapman–Kolmogorov (p. 224). — from [[bellman-1957-dp/ch08-viii]] (control-theory → control-theory)
- [same-math] §6 equation $0=\max_v[F+Gf_c-f_T]$ ↔ control-theory: Hamilton–Jacobi–Bellman equation for finite-horizon optimal control — same PDE (canon link; name not used in this unit) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] Bellman optimality equation (3.19) ↔ control theory: Hamilton–Jacobi–Bellman equation — the text calls the HJB equation the continuous-time, continuous-state counterpart (p. 71). — from [[sutton-2018-rl/ch03-finite]] (control-theory → control-theory)
