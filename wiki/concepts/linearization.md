---
id: linearization
type: concept
fields: [control-theory]
n_sources: 19
tiers: [deep, core]
grounding: digests
sources: [ashby-1956-cybernetics/ch03-determinate, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch08-output, liberzon-2012-calculus/ch03-calculus, liberzon-2012-calculus/ch04-maximum-p1, sarkka-2023-bayesianfiltering/ch04-discretization, sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch09-gaussian, sarkka-2023-bayesianfiltering/ch10-posterior, sarkka-2023-bayesianfiltering/ch13-extended, sarkka-2023-bayesianfiltering/ch14-general, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional, sarkka-2023-bayesianfiltering/ch21-list, welch-2004-kalmanintro/main]
canon_spine: control-theory
generated_by: build_kg.py
---

# linearization

## Canon spine entry

- **linearization** (control-theory): approximating a nonlinear system near an equilibrium by its Jacobian (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch03-determinate]] (p. 36): not stated here; only "linear" is defined: all functions in the canonical representation are linear
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-22): approximating $F$ by its slope $F'(u_0)$ at an operating point
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-13): here used as approximating a nonlinear model near $\theta\approx0$ with $\sin\theta\approx\theta$, $\cos\theta\approx1$ and dropping $\dot\theta^2$ terms
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-7, p. 4-13): the web-server model is linear around an equilibrium; $\sin\varphi\approx\varphi$ for the bicycle
- [[astrom-2021-feedbacksystems/ch05-dynamic]] (pp. 5-15, 5-26): $\dot z=Az$, $A=\partial F/\partial x|_{x_e}$; local asymptotic stability follows if all eigenvalues have strictly negative real part; the author also says one or more strictly positive real parts give instability
- [[astrom-2021-feedbacksystems/ch06-linear]] (pp. 6-30, 6-31): Jacobian matrices at an equilibrium give a local linear model; valid only near a solution
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-28): error dynamics linearized about the desired trajectory
- [[liberzon-2012-calculus/ch03-calculus]] (p. 72): $\dot\eta=A_*\eta+B_*\xi$ along the optimal trajectory
- [[liberzon-2012-calculus/ch04-maximum-p1]] (p. 90): the variational equation is the linearization of (4.7) around $y^*$
- [[sarkka-2023-bayesianfiltering/ch04-discretization]] (p. 59): first-order Taylor expansion of $\mathbf a$ around a nominal point (mean, initial point, or fixed point) to get tractable moments
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 109): first-order Taylor approximation of a non-linear map at the current mean, used as the basis for EKF equations
- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 133): the EKF alternative this chapter replaces by integration
- [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (p. 170): here a family: Taylor expansion (EKF/IEKF), SL, SLR; they differ in how $\mathbf A,\mathbf b,\boldsymbol\Lambda$ are chosen
- [[sarkka-2023-bayesianfiltering/ch10-posterior]] (p. 204): here: any affine map plus additive Gaussian noise approximating the model; the choice of linearization distribution matters
- [[sarkka-2023-bayesianfiltering/ch13-extended]] (p. 273): first-order Taylor approximation of $\mathbf f,\mathbf h$ at a point
- [[sarkka-2023-bayesianfiltering/ch14-general]] (p. 291): Approximating non-linear models by affine ones. Taylor (extended) or SLR (Gaussian) here
- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (p. 363): Jacobian $A_x(m)$ drives the covariance ODE (A.33)
- [[sarkka-2023-bayesianfiltering/ch21-list]] (p. 397–398): by their titles, the Ch. 7 and 9–10 entries concern linear approximations of non-linear transforms
- [[welch-2004-kalmanintro/main]] (pp. 7–8): EKF linearizes $f,h$ with Jacobians about the current estimate

## Instances that use it

- [[vectored-thrust-aircraft]] — eigenvalue 0 with a non-scalar Jordan block makes the linearization unstable — from [[astrom-2021-feedbacksystems/ch06-linear]]
- [[cruise-control]] — linearization validated on hills; feedback linearization example — from [[astrom-2021-feedbacksystems/ch06-linear]]
- [[ekf-iekf-as-enabling-linearization]] — EKF/IEKF are Algorithm 9.1 with Taylor expansion at different points — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]]

## Candidate bridges

- [same-math] Linearization and Jacobian eigenvalues ↔ dynamical-systems analysis of any fixed point: same criterion on $\partial F/\partial x$. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → other)
- [same-math] Linearization of a nonlinear ODE ↔ multivariable calculus: first-order Taylor expansion with the Jacobian — the matrices (6.35) are partial derivatives. — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → other)
- [structural-analogy] Feedback linearization (cancel the nonlinearity) ↔ inverse-model/computed-torque control in robotics (named in the text). — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → unspecified)
- [structural-analogy] Aggregation interpolation $\tilde J=\Phi r$ ↔ control-theory: linearization or gridding of a nonlinear value function — both replace a large problem by a small one and map back — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → control-theory)
- [structural-analogy] Taylor approximation $\hat f(x)=f(z)+\nabla f(z)^T(x-z)$ ↔ calculus: tangent line / linearization of a function at a point — same idea in $n$ variables. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → other)
- [structural-analogy] Newton/Gauss–Newton iteration ↔ linear-algebra: repeated linearization — nonlinear problem solved as a sequence of linear least squares problems. — from [[boyd-2018-vmls/ch18-nonlinear]] (linear-algebra → linear-algebra)
- [same-math] linearised perturbation $\dot\eta=A_*\eta+B_*\xi$ ↔ control-theory linearization: Jacobian linearisation along a trajectory (p. 72) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → control-theory)
- [same-math] Linearization $x_{j,k}=q_{j,k}y_{j,k}$ and constraint set ↔ operations research: linear programming — the paper says the optimal mechanism can be found by linear programming (p. 331). — from [[myerson-2008-mechanism/main]] (decision-game-theory → other)
- [structural-analogy] Enabling approximation (linearize, then exact Kalman) ↔ control theory: linearization about an operating point for linear design. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → control-theory)
- [structural-analogy] Noise added to cover linearization error ↔ robustness: model uncertainty treated as extra disturbance. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → other)
- [structural-analogy] Linearize-at-the-estimate loop ↔ gain scheduling/extended observers in nonlinear control: the linearization point is itself estimated. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
- [structural-analogy] SLR as an affine fit averaged over a density ↔ Jacobian linearization: SLR replaces the Taylor expansion at a point (p. 291) by a fit over a density. Not the same math in general. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → other)
- [structural-analogy] IPLS iteration (relinearize, resolve, repeat) ↔ control: iterative linearization for non-linear trajectory optimization — plausible, not stated in the text. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → control-theory)
- [same-math] Jacobian $A_x(m)$ in (A.33) ↔ control-theory: linearization about an equilibrium or trajectory — same Jacobian linearization. — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (control-theory → control-theory)
- [same-math] EKF Jacobians $A_k,W_k,H_k,V_k$ ↔ control-theory linearization: first-order Taylor expansion of $f,h$ about an operating point. — from [[welch-2004-kalmanintro/main]] (control-theory → control-theory)
