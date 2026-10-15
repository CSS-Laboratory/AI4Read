---
id: liberzon-2012-calculus/index
work: liberzon-2012-calculus
type: work-map
units: [liberzon-2012-calculus/ch01-introduction, liberzon-2012-calculus/ch02-calculus, liberzon-2012-calculus/ch03-calculus, liberzon-2012-calculus/ch04-maximum-p1, liberzon-2012-calculus/ch04-maximum-p2, liberzon-2012-calculus/ch05-hamilton, liberzon-2012-calculus/ch06-linear, liberzon-2012-calculus/ch07-advanced]
---

# Liberzon, D. (2012). *Calculus of Variations and Optimal Control Theory: A Concise Introduction*. Princeton University Press. ISBN 9780691151878.

## In one paragraph
The book teaches how to choose a control function that minimizes a cost. It follows the historical order. First, perturbing a candidate minimum gives necessary conditions: the Euler–Lagrange equation and its second-order tests. Next, the same idea applied to controls leads to Pontryagin's maximum principle. This gives an open-loop answer through a costate (adjoint vector), but only as a necessary condition. Dynamic programming gives the other route. The value function satisfies the Hamilton–Jacobi–Bellman (HJB) equation, which yields a feedback law and a sufficient condition for optimality. Where the value function is not smooth, viscosity solutions are needed. The linear-quadratic regulator (LQR) is the case where both routes meet and reduce to a Riccati equation. A last chapter sketches extensions: manifolds, characteristics, $\mathcal H_\infty$ control and hybrid systems.

## The path through the work
- [[liberzon-2012-calculus/ch01-introduction]] — Optimal control means minimizing a cost functional over control functions; this chapter prepares for it by showing, first for $f:\mathbb R^n\to\mathbb R$ and then for functionals, how perturbing a candidate minimum along a one-parameter family reduces the question to ordinary calculus on a scalar function $g(\alpha)$.
- [[liberzon-2012-calculus/ch02-calculus]] — To minimise a cost $J(y)=\int_a^b L(x,y,y')\,dx$ over curves with fixed endpoints, a minimiser must satisfy the Euler–Lagrange equation, and second-order tests (Legendre's condition, absence of conjugate points) then help decide whether an extremal is a weak minimum.
- [[liberzon-2012-calculus/ch03-calculus]] — Perturbing the control instead of the curve, and using the Hamiltonian with an adjoint vector, gives conditions that look like the maximum principle. The same chapter shows why that variational route is too narrow.
- [[liberzon-2012-calculus/ch04-maximum-p1]] — If a control is optimal, then a costate (adjoint vector) exists such that the state and costate obey the canonical equations and the Hamiltonian is maximized over the controls at every time. The proof builds a cone of possible terminal perturbations and separates it from the cost-decreasing direction.
- [[liberzon-2012-calculus/ch04-maximum-p2]] — The maximum principle gives only necessary conditions; in time-optimal problems it gives bang-bang controls for the double integrator and for normal linear systems, nonlinear systems can have singular arcs that are detected through Lie brackets, and existence of an optimal control is tied to (compact) reachable sets.
- [[liberzon-2012-calculus/ch05-hamilton]] — Dynamic programming turns optimal control into a PDE for the value function (the HJB equation), which can give a feedback law (once the PDE is solved) and a sufficient test for optimality, but the value function is often not differentiable, so the PDE must be read in the viscosity sense.
- [[liberzon-2012-calculus/ch06-linear]] — For linear dynamics and quadratic cost, the optimal control is a linear state feedback $u^*=-R^{-1}B^TPx$, where $P$ solves a Riccati equation and $x^TPx$ is the optimal cost.
- [[liberzon-2012-calculus/ch07-advanced]] — Four independent extensions of the maximum principle and HJB theory: the costate is really a covector on a manifold, canonical equations are the HJB characteristics, Riccati inequalities give $\mathcal L_2$-gain and $\mathcal H_\infty$ bounds, and the maximum principle extends to hybrid systems.

## Big ideas across units
- **Perturb the candidate and read off the condition.** Variations reduce a minimization to calculus on a scalar function. This runs from $g(\alpha)$ in the first chapter, to Euler–Lagrange, to control perturbations, to needle perturbations in the maximum-principle proof. Units: ch01, ch02, ch03, ch04-p1.
- **Hamiltonian and momentum become costate.** The momentum $p=L_{y'}$ and $H=py'-L$ of calculus of variations return as the adjoint vector and the maximized Hamiltonian of the maximum principle. They then reappear in HJB (with $p^*=-V_x$) and as a covector on a manifold. Units: ch02, ch03, ch04-p1, ch05, ch07.
- **Multipliers lead to the costate.** Finite-dimensional Lagrange multipliers lead to function multipliers for pointwise constraints. The author says these correspond to the costate, which is later read as a shadow price. Units: ch01, ch02, ch04-p1, ch05.
- **Norms and strong vs weak minima.** What counts as "close" changes which conditions apply. Weak-minimum tests are not enough for control, which motivates strong-minimum conditions (corner, Weierstrass E) and the maximum principle. The maximum principle stays necessary under a local notion between weak and strong. Units: ch01, ch02, ch03, ch04-p2.
- **Necessary vs sufficient vs existence.** First- and second-order conditions are only necessary. The maximum principle gives candidates that can mislead if no optimum exists. HJB supplies a sufficient condition, and existence is tied to compact reachable sets. Units: ch01, ch04-p2, ch05, ch06.
- **Open-loop vs closed-loop.** The maximum principle gives an open-loop control from ODEs. HJB gives a state-feedback law but needs a PDE. LQR is where the feedback becomes explicit. Units: ch04-p2, ch05, ch06.
- **Non-smooth value functions.** A simple example shows $V$ need not be $\mathcal C^1$. Viscosity solutions repair this. Characteristics recast the canonical equations as the HJB's ODE system. Units: ch05, ch07.
- **Riccati equations as the tractable core.** LQR replaces the HJB PDE with a Riccati ODE or algebraic equation. Riccati inequalities then give $\mathcal L_2$-gain and $\mathcal H_\infty$ bounds. Units: ch06, ch07.

## How to read it
- **Essential:** ch02, ch03, ch04-p1, ch05 and ch06 form the main line named in the catalog entry. Ch01 is background; skim it if multivariable optimization, Lagrange multipliers and norms are familiar.
- **Dependencies:**
  - Ch02 uses the norms and first variation from ch01.
  - Ch03 uses the Euler–Lagrange equation and Hamiltonian from ch02, and its listed shortcomings motivate ch04.
  - Ch04-p2 needs the statement and transversality from ch04-p1.
  - Ch05 builds on the Bolza cost and Hamiltonian of ch03–ch04.
  - Ch06 needs the maximum principle (ch04) and HJB (ch05).
  - Ch07 needs ch04, ch05 and ch06.
- **Can be skipped on a first pass:**
  - The proof details in ch04-p1.
  - In ch04-p2, the Lie-bracket singular arcs, Fuller's problem and the existence proof. The double integrator and the extension remarks are worth keeping.
  - Ch07, whose four topics are independent of one another. The author says the treatment is introductory, not fully rigorous.

## Concepts introduced
Variant spellings of the same id in the units are merged under one kebab-case id.

- [[optimal-control-problem]] — ch01
- [[cost-functional]] — ch01
- [[state]] — ch01
- [[state-space-model]] — ch01
- [[pontryagin-maximum-principle]] — ch01 (referenced), developed in ch04-p1
- [[principle-of-optimality]] — ch01 (referenced), developed in ch05
- [[first-order-necessary-condition]] — ch01
- [[second-order-conditions]] — ch01
- [[lagrange-multipliers]] — ch01 (also written [[lagrange-multiplier]] in ch02)
- [[augmented-cost]] — ch01
- [[first-variation]] — ch01
- [[second-variation]] — ch01
- [[function-space-norm]] — ch01
- [[convexity-and-global-minima]] — ch01
- [[functional]] — ch02
- [[weak-and-strong-extrema]] — ch02 (see also [[strong-vs-weak-minimum]], ch03)
- [[euler-lagrange-equation]] — ch02
- [[momentum]] — ch02
- [[hamiltonian]] — ch02
- [[legendre-transformation]] — ch02
- [[principle-of-least-action]] — ch02
- [[abnormal-multiplier]] — ch02
- [[holonomic-constraint]] — ch02
- [[legendre-condition]] — ch02
- [[jacobi-equation-conjugate-point]] — ch02
- [[transversality-condition]] — ch02
- [[strong-vs-weak-minimum]] — ch03
- [[weierstrass-erdmann-corner-conditions]] — ch03
- [[weierstrass-excess-function]] — ch03
- [[legendre-clebsch-condition]] — ch03
- [[adjoint-vector-costate]] — ch03 (also written [[costate-adjoint-vector]] and [[costate]] in ch04)
- [[bolza-lagrange-mayer-problems]] — ch03
- [[target-set]] — ch03
- [[linearization]] — ch03
- [[needle-perturbation]] — ch04-p1
- [[variational-equation]] — ch04-p1
- [[terminal-cone]] — ch04-p1
- [[separating-hyperplane-theorem]] — ch04-p1
- [[lagrange-to-mayer-form]] — ch04-p1
- [[nontriviality-condition]] — ch04-p2
- [[bang-bang-control]] — ch04-p2
- [[switching-function]] — ch04-p2
- [[singular-control]] — ch04-p2
- [[lie-bracket]] — ch04-p2
- [[normal-linear-system]] — ch04-p2
- [[controllability]] — ch04-p2 (also written [[controllability-reachability]] in ch06)
- [[reachable-set]] — ch04-p2
- [[filippov-theorem]] — ch04-p2
- [[fuller-phenomenon]] — ch04-p2
- [[open-loop-vs-closed-loop]] — ch04-p2 (also in ch05)
- [[state-feedback]] — ch04-p2
- [[bellman-equation-value-function]] — ch05
- [[hamilton-jacobi-bellman-equation]] — ch05
- [[policy]] — ch05
- [[dynamic-programming]] — ch05
- [[curse-of-dimensionality]] — ch05
- [[sufficient-condition-for-optimality]] — ch05
- [[costate-as-shadow-price]] — ch05
- [[super-sub-differential]] — ch05
- [[viscosity-solution]] — ch05
- [[lqr]] — ch06
- [[state-feedback-pole-placement]] — ch06
- [[riccati-differential-equation]] — ch06
- [[algebraic-riccati-equation]] — ch06
- [[hamiltonian-matrix]] — ch06
- [[finite-escape-time]] — ch06
- [[observability]] — ch06
- [[stability]] — ch06
- [[costate-as-covector]] — ch07
- [[manifold-state-space]] — ch07
- [[symplectic-form]] — ch07
- [[method-of-characteristics]] — ch07
- [[l2-gain]] — ch07
- [[riccati-inequality-lmi]] — ch07
- [[robustness]] — ch07
- [[observer-state-estimator]] — ch07
- [[hybrid-optimal-control]] — ch07
