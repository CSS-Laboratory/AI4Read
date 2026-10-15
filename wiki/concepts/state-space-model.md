---
id: state-space-model
type: concept
fields: [control-theory, bayesian]
n_sources: 26
tiers: [deep, core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch09-transfer-p1, bellman-1957-dp/ch06-vi, kalman-1960-filtering/main, liberzon-2012-calculus/ch01-introduction, liberzon-2012-calculus/ch03-calculus, murphy-2023-pml2/ch08-gaussian-p1, murphy-2023-pml2/ch29-state-p1, sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch03-batch, sarkka-2023-bayesianfiltering/ch04-discretization, sarkka-2023-bayesianfiltering/ch05-modeling, sarkka-2023-bayesianfiltering/ch06-bayesian, sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch09-gaussian, sarkka-2023-bayesianfiltering/ch11-particle, sarkka-2023-bayesianfiltering/ch12-bayesian, sarkka-2023-bayesianfiltering/ch16-parameter, sarkka-2023-bayesianfiltering/ch17-epilogue, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional, sarkka-2023-bayesianfiltering/ch21-list, welch-2004-kalmanintro/main]
raw_ids: [state-space model]
canon_spine: control-theory
generated_by: build_kg.py
---

# state-space-model

## Canon spine entry

- **state-space model** (control-theory): dx/dt = Ax + Bu, y = Cx: dynamics, input and measurement as matrices (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p1]] (pp. 3-6, 3-10): $\dot x=f(x,u)$, $y=h(x,u)$; linear case $\dot x=Ax+Bu$, $y=Cx+Du$
- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. e.g. p. 3-29): differential equations in state variables, used throughout the examples
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-13, p. 4-23): dynamics written as vector equations with matrices, e.g. (4.16) and (4.28)
- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-1): $\dot x=f(x,u)$, $y=h(x,u)$, possibly nonlinear
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-3): $\dot x=Ax+Bu,\ y=Cx+Du$ as the general linear system form
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-3): $\dot x=Ax+Bu,\ y=Cx+Du$ (9.2), the starting point for deriving $G$
- [[bellman-1957-dp/ch06-vi]] (p. 191): $dx/dt=A_1x+A_2z$, $B_1z\le B_2x$ [as `state-space model`]
- [[kalman-1960-filtering/main]] (p. 39): first-order difference or differential equations $x(t+1)=\Phi x+\dots$, $y=Mx$
- [[liberzon-2012-calculus/ch01-introduction]] (p. 1): here the control system $\dot x=f(t,x,u)$, $x(t_0)=x_0$
- [[liberzon-2012-calculus/ch03-calculus]] (p. 67): control system $\dot x=f(t,x,u)$
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (pp. xx–xxi): dynamic function $\mathbf f$, measurement function $\mathbf h$; continuous-time linear form uses $\mathbf F$, $\mathbf L$
- [[sarkka-2023-bayesianfiltering/ch03-batch]] (p. 39): dynamics $p(\mathbf x_k\mid\mathbf x_{k-1})$ plus measurement $p(\mathbf y_k\mid\mathbf x_k)$
- [[sarkka-2023-bayesianfiltering/ch04-discretization]] (p. 44): dynamic model plus measurement model; here the dynamic part is built from physics, then discretized
- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (pp. 73, 83–87): dynamics $p(\mathbf{x}_k\mid\mathbf{x}_{k-1})$ plus measurement model; here also linear regression, AR and HMM forms
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (p. 91): here a probabilistic one: dynamic model and measurement model as conditional distributions
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 113): $\mathbf x_k=\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf y_k=\mathbf h(\mathbf x_k)+\mathbf r_k$
- [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (p. 169–171): the three families: additive (9.1), non-additive (9.9), conditional distributions (9.10)
- [[sarkka-2023-bayesianfiltering/ch11-particle]] (p. 234): model (11.14) with possibly discrete components
- [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (pp. 255, 259): the linear (6.17) and affine (6.34) models the smoothers assume
- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 319): dynamics and measurement model, here with unknown parameters θ
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 349): model (17.1): state transition $f$ plus noise, measurement $h$ plus noise
- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (pp. 359, 371): linear dynamics $Fx+b+Lw$ and measurement $Hx+r$, as used here
- [[sarkka-2023-bayesianfiltering/ch21-list]] (p. 400): "linear state space models" appear in 16.13
- [[welch-2004-kalmanintro/main]] (p. 2): here $x_k=Ax_{k-1}+Bu_{k-1}+w_{k-1}$, $z_k=Hx_k+v_k$

### bayesian

- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 359): latent Markov chain $z_t$ with observations $y_t$ and optional inputs $u_t$ [new]
- [[murphy-2023-pml2/ch29-state-p1]] (p. 979): hidden Markov state $z_t$ plus observations $y_t$ drawn from it; optional inputs [new]

## Candidate bridges

- [same-math] Canonical representation $x'=f(x)$ ↔ control-theory: autonomous discrete-time state-space model $x_{k+1}=f(x_k)$ — same one-step rule, repeated powers. — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [same-math] Population update $D'=MD$ with a column-stochastic $M$ ↔ control-theory: discrete-time linear state-space model $x_{k+1}=Ax_k$. The equilibrium is a fixed vector of $M$, and the "dying oscillations" are mode behaviour. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [same-math] Two-compartment drug model (4.28) ↔ any linear state-space model $\dot x=Ax+Bu$, $y=Cx$ — literally the same matrix form. — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [structural-analogy] Vector-state multi-activity recursion ↔ state-space models: resources as state vector, allocations as inputs. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → other)
- [same-math] GP with Matérn kernel ↔ state-space models: for the kernels where the SDE conversion is exact, a 1d GP is a linear-Gaussian SSM and Kalman smoothing gives the same posterior. — from [[murphy-2023-pml2/ch18-gaussian-p2]] (bayesian → other)
- [same-math] Dynamic topic model chain on $w_k^t$ ↔ State-space models: linear-Gaussian chain, Kalman smoothing (p. 969). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → other)
- [same-math] Linear-in-parameters regression as $\mathbf{x}_k=\mathbf{x}_{k-1}$, $y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k$ ↔ control-theory: observer for a constant unknown parameter — the same linear Gaussian state space model. — from [[sarkka-2023-bayesianfiltering/ch05-modeling]] (control-theory → control-theory)
