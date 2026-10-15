---
id: nonlinearity
type: concept
fields: [complex-systems, control-theory]
n_sources: 8
tiers: [core, reference]
grounding: digests
sources: [lorenz-1963-nonperiodic/main, meadows-2008-thinking/ch04-systems, mitchell-2009-guidedtour/ch02-dynamics, mitchell-2009-guidedtour/ch18-evolution, schelling-1971-segregation/main-p1, strogatz-2024-nonlinear/ch01-overview, strogatz-2024-nonlinear/ch07-limit-p1, strogatz-2024-nonlinear/ch09-lorenz-p1]
canon_spine: complex-systems
generated_by: build_kg.py
---

# nonlinearity

## Canon spine entry

- **nonlinearity** (complex-systems): output not proportional to input, so the effect of the whole is not the sum of the effects of the parts (HS)

## Definitions in the sources

### complex-systems

- [[lorenz-1963-nonperiodic/main]] (p. 131): advection terms let constant forcing yield variable response
- [[mitchell-2009-guidedtour/ch02-dynamics]] (pdf 42): the whole differs from the sum of the parts, because parts interact
- [[mitchell-2009-guidedtour/ch18-evolution]] (p. 150): genes act in networks where some control others, not as independent additive effects
- [[schelling-1971-segregation/main-p1]] (p. 159): segregation rises rapidly with demand between about 35% and 50%
- [[strogatz-2024-nonlinear/ch01-overview]] (pp. 6, 8–9): a system is nonlinear if some $x_i$ on the right-hand side is not simply to the first power (products, powers, functions); superposition then fails
- [[strogatz-2024-nonlinear/ch07-limit-p1]] (p. 199): here: limit cycles cannot occur in linear systems, whose closed orbits form non-isolated families
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (p. 319): Lorenz has only two quadratic terms, xy and xz, yet is chaotic

### control-theory

- [[meadows-2008-thinking/ch04-systems]] (pp. 91–92): cause does not give proportional effect; changes loop strengths and can flip modes [new]

## Instances that use it

- [[leukemia-aml-loglogistic-gp]] — latent GP on a log-logistic survival model; finds nonlinearity and WBC×deprivation interaction — from [[gelman-2013-bda3/ch21-gaussian]]
- [[russian-roulette-zeckhauser]] — illustrates the hypothesized nonlinearity of $\pi$ — from [[kahneman-1979-prospect/main]]
- [[weakly-nonlinear-spiral]] — Example 6.3.2: $\dot r=ar^3$, $\dot\theta=1$; a center destroyed by small nonlinearity — from [[strogatz-2024-nonlinear/ch06-phase-p1]]

## Candidate bridges

- [structural-analogy] Feedback linearization (cancel the nonlinearity) ↔ inverse-model/computed-torque control in robotics (named in the text). — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → unspecified)
- [same-math] Anti-windup circle-criterion test ↔ nonlinear stability: the sector-bounded nonlinearity test (10.17) applied to a saturation (p. 11-17). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → other)
- [structural-analogy] policy chattering in approximate PI ↔ control theory: limit cycles in a loop with nonlinearity (p. 387) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [structural-analogy] Asymmetric superposition and inhibition ↔ error-control design: turning costly error into clipped error via the output nonlinearity. — from [[elhage-2022-superposition/main-p2]] (llm → control-theory)
- [structural-analogy] Hidden-layer ReLU network ↔ llm: the per-token feed-forward block of a Transformer — same layer shape (linear, nonlinearity, linear), but the book here covers only the shallow case. — from [[prince-2023-udl/ch03-shallow]] (llm → llm)
- [structural-analogy] Composition F_L(…F₁(v)) with ReLU ↔ linear algebra: matrix product A_L⋯A₁ — without the nonlinearity the chain would be one matrix (p. 379) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
