---
id: boyd-2018-vmls/ch19-constrained
work: boyd-2018-vmls
unit: Chapter 19 — Constrained nonlinear least squares
pages: 419-434
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Constrained nonlinear least squares

## L0 — One line
Equality-constrained nonlinear least squares can be attacked heuristically by solving a sequence of ordinary nonlinear least squares problems with Levenberg–Marquardt, and the augmented Lagrangian method does this more reliably than the plain penalty method.

## L1 — The gist (≤ 120 words)
How do we minimize $\|f(x)\|^2$ when $x$ must also satisfy nonlinear equations $g(x)=0$? Exact solution is hard in general. The chapter gives optimality conditions (Lagrange multipliers), then two heuristics. The penalty algorithm adds $\mu\|g(x)\|^2$ and keeps doubling $\mu$, which can make Levenberg–Marquardt slow or fail once $\mu$ is very large. The augmented Lagrangian algorithm also updates a multiplier estimate $z$, so $\mu$ does not need to grow as much (the book gives this as part of why it works better). A two-variable example compares the two. Nonlinear control (steering a car to a target state) is then written as a large constrained problem and solved with the augmented Lagrangian method.

**Prerequisites:** least squares; Jacobian $Df$ and gradients; Levenberg–Marquardt (ch. 18); Lagrange multipliers (appendix C.3); basic dynamical systems $x_{k+1}=f(x_k,u_k)$.

## L2 — Key ideas
- Problem (19.1): minimize $\|f(x)\|^2$ subject to $g(x)=0$. It is hard in general; the chapter's algorithms are heuristics (p. 420).
- Optimality condition (19.4) together with feasibility (19.3) is necessary for a solution, provided the rows of $Dg(\hat x)$ are linearly independent, but is not sufficient (pp. 420–421).
- Penalty algorithm: minimize $\|f\|^2+\mu\|g\|^2$ for increasing $\mu$. It is simple, but large $\mu$ can make Levenberg–Marquardt slow or fail (pp. 421–422).
- Each penalty iterate gives a multiplier estimate $z^{(k+1)}=2\mu^{(k)}g(x^{(k+1)})$, for which (19.4) almost holds (p. 422).
- Augmented Lagrangian: add the multiplier term $g^Tz$. Completing the square turns the minimization into an ordinary nonlinear least squares problem (19.10) (p. 423).
- If $\tilde x$ minimizes the augmented Lagrangian, the update $\tilde z=z+2\mu g(\tilde x)$ gives a multiplier that satisfies (19.4) with $\tilde x$. $\mu$ is raised only when $\|g\|$ does not shrink enough (pp. 423–424).
- In the example, the augmented Lagrangian method keeps $\mu$ small, while penalty $\mu$ grows past $10^4$ (pp. 424–429).
- Nonlinear control becomes a constrained problem with the dynamics as equality constraints; the car example is solved this way (pp. 429–433).

## L3 — Walkthrough

### 19.1 Constrained nonlinear least squares (p. 419)
Problem:
$$\text{minimize } \|f(x)\|^2 \quad\text{subject to } g(x)=0 \tag{19.1}$$
- $x$ is an $n$-vector, $f(x)$ an $m$-vector, $g(x)$ a $p$-vector.
- $f_i$ are the scalar residuals; $g_i(x)=0$ are the scalar equality constraints.
- If $f,g$ are affine, this is the linear equality-constrained least squares problem of chapter 16.
- $x$ is *feasible* if $g(x)=0$.
- $\hat x$ is a *solution* if it is feasible and $\|f(x)\|^2\ge\|f(\hat x)\|^2$ whenever $g(x)=0$.

The problem is in general hard to solve exactly. Levenberg–Marquardt (LM, the unconstrained method of ch. 18) can be leveraged. The chapter presents the penalty algorithm and the better augmented Lagrangian algorithm, both heuristics (p. 420).

**Linear constraints.** If $g$ is affine, the constraints read $Cx=d$ with $C$ of size $p\times n$. Then LM can approximately solve the problem by adding $Cx=d$ to the linear least squares problem in its step 2. The harder case is non-affine $g$ (p. 420).

### 19.1.1 Optimality condition (pp. 420–421)
Lagrangian, with multiplier $p$-vector $z$:
$$L(x,z)=\|f(x)\|^2+z_1g_1(x)+\dots+z_pg_p(x)=\|f(x)\|^2+g(x)^Tz \tag{19.2}$$
For any solution $\hat x$, there are multipliers $\hat z$ with $\partial L/\partial x_i(\hat x,\hat z)=0$ ($i=1..n$) and $\partial L/\partial z_i(\hat x,\hat z)=0$ ($i=1..p$). This holds provided the rows of $Dg(\hat x)$ are linearly independent. $\hat z$ is an optimal Lagrange multiplier (p. 420).
- The $z$-equations are $g(\hat x)=0$ (19.3), feasibility.
- The $x$-equations are
$$2Df(\hat x)^Tf(\hat x)+Dg(\hat x)^T\hat z=0 \tag{19.4}$$
This extends condition (18.3) of the unconstrained problem. Together, (19.4) and (19.3) are the optimality conditions (p. 420).
- A solution satisfies them for some $\hat z$ (under the rank proviso). They are *not sufficient*: some $x,z$ satisfy them although $x$ is not a solution (p. 421).

*Intuition note:* At a solution (when the rows of $Dg(\hat x)$ are linearly independent), the gradient of the cost is cancelled by a combination of the constraint gradients. The multiplier $z$ gives the weights of that combination. A point can satisfy this and still not be the best feasible point.

### 19.2 Penalty algorithm (pp. 421–422)
The equality-constrained problem can be seen as a limit of a bi-objective problem ($\|f\|^2$ and $\|g\|^2$) as the weight on the second goes to infinity (p. 421). For $\mu>0$ use
$$\|f(x)\|^2+\mu\|g(x)\|^2 \tag{19.5}$$
It is approximately minimized by LM applied to the stacked residual (shape $(m+p)$-vector):
$$\left\|\begin{bmatrix} f(x)\\ \sqrt\mu\, g(x)\end{bmatrix}\right\|^2 \tag{19.6}$$
For large enough $\mu$, $g(x)$ should be very small and $\|f\|^2$ small (p. 421).

**Algorithm 19.1 (penalty).** Given $f,g$, start $x^{(1)}$, $\mu^{(1)}=1$. For $k=1,\dots,k^{\max}$:
1. Set $x^{(k+1)}$ to the approximate minimizer of $\|f(x)\|^2+\mu^{(k)}\|g(x)\|^2$ by LM, started at $x^{(k)}$.
2. $\mu^{(k+1)}=2\mu^{(k)}$.

Stop early if $\|g(x^{(k)})\|$ is small enough (p. 421).

Drawback: $\mu^{(k)}$ rises rapidly (it must, to drive $g\to0$). For very high $\mu$, LM can take many iterations or fail (pp. 421–422).

**Multiplier estimate.** $x^{(k+1)}$ (almost) satisfies $2Df(x^{(k+1)})^Tf(x^{(k+1)})+2\mu^{(k)}Dg(x^{(k+1)})^Tg(x^{(k+1)})=0$. Define $z^{(k+1)}=2\mu^{(k)}g(x^{(k+1)})$. Then (19.4) almost holds for $x^{(k+1)},z^{(k+1)}$. Feasibility holds only in the limit $k\to\infty$ (p. 422).

### 19.3 Augmented Lagrangian algorithm (pp. 422–424)
Proposed by Hestenes and Powell in the 1960s (p. 422). It addresses the growth of $\mu^{(k)}$.

$$L_\mu(x,z)=L(x,z)+\mu\|g(x)\|^2=\|f(x)\|^2+g(x)^Tz+\mu\|g(x)\|^2 \tag{19.7}$$
- It is the Lagrangian plus $\mu\|g\|^2$, or the penalty objective (19.5) plus $g^Tz$.
- It is the ordinary Lagrangian of "minimize $\|f\|^2+\mu\|g\|^2$ subject to $g(x)=0$". That problem has exactly the same solutions as (19.1), because $\mu\|g\|^2=0$ at feasible $x$ (p. 422).

**Minimizing over $x$.** Identity:
$$L_\mu(x,z)=\|f(x)\|^2+\mu\|g(x)+z/(2\mu)\|^2-\mu\|z/(2\mu)\|^2 \tag{19.8}$$
Proof: expand
$$\mu\|g+z/(2\mu)\|^2=\mu\|g\|^2+2\mu g^T\big(z/(2\mu)\big)+\mu\|z/(2\mu)\|^2=g^Tz+\mu\|g\|^2+\mu\|z/(2\mu)\|^2.$$
Substituting into the right side of (19.8) gives (19.7) (p. 423).

The last term of (19.8) does not depend on $x$. So minimizing $L_\mu$ over $x$ is the same as minimizing
$$\|f(x)\|^2+\mu\|g(x)+z/(2\mu)\|^2 \tag{19.9}$$
$$\left\|\begin{bmatrix} f(x)\\ \sqrt\mu\, g(x)+z/(2\sqrt\mu)\end{bmatrix}\right\|^2 \tag{19.10}$$
This is a nonlinear least squares problem, approximately solvable by LM (p. 423).

**Optimality of a minimizer $\tilde x$:**
$$0=2Df(\tilde x)^Tf(\tilde x)+2\mu Dg(\tilde x)^T\big(g(\tilde x)+z/(2\mu)\big)=2Df(\tilde x)^Tf(\tilde x)+Dg(\tilde x)^T\big(2\mu g(\tilde x)+z\big)$$
- If $\tilde x$ minimizes $L_\mu$ and is feasible, (19.4) holds with multiplier $z$.
- If not feasible, the choice
$$\tilde z=z+2\mu g(\tilde x) \tag{19.11}$$
satisfies (19.4) with $\tilde x,\tilde z$ (p. 423).

The algorithm alternates approximate minimization of $L_\mu$ with the update (19.11). It raises $\mu$ only when $\|g(x)\|$ does not decrease enough (p. 423).

**Algorithm 19.2 (augmented Lagrangian).** Start $x^{(1)}$, $z^{(1)}=0$, $\mu^{(1)}=1$. For $k=1,\dots,k^{\max}$:
1. $x^{(k+1)}$ = approximate minimizer (LM, started at $x^{(k)}$) of $\|f(x)\|^2+\mu^{(k)}\|g(x)+z^{(k)}/(2\mu^{(k)})\|^2$.
2. $z^{(k+1)}=z^{(k)}+2\mu^{(k)}g(x^{(k+1)})$.
3. $\mu^{(k+1)}=\mu^{(k)}$ if $\|g(x^{(k+1)})\|<0.25\|g(x^{(k)})\|$; otherwise $\mu^{(k+1)}=2\mu^{(k)}$.

It stops early if $g(x^{(k)})$ is very small. By the $z$ update, $x^{(k+1)}$ (almost) satisfies (19.4) with $z^{(k+1)}$. The method is only slightly more complicated than the penalty algorithm but works much better in practice, partly because $\mu^{(k)}$ need not grow as much (p. 424).

*Intuition note:* In the penalty method, $\mu$ must rise rapidly to drive $g$ to zero, and $z$ is only a by-product estimate. In the augmented Lagrangian method $z$ is updated each step and used in the next minimization. The book says this is part of why $\mu$ does not need to grow as much (p. 424).

**Example (pp. 424–429).** $n=2$, $f(x)=(x_1+e^{-x_2},\;x_1^2+2x_2+1)$, $g(x)=x_1+x_1^3+x_2+x_2^2$.
- $\hat x=(0,0)$ is optimal with $\hat z=-2$. Check: $g(\hat x)=0$ and
$$2\begin{bmatrix}1&0\\-1&2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}-2\begin{bmatrix}1\\1\end{bmatrix}=0$$
- The unconstrained minimizer of $\|f\|^2$ is at $(-0.666,-0.407)$ (p. 424).
- Start at $x^{(1)}=(0.5,-0.5)$. Figure 19.2 (augmented Lagrangian) shows $\mu^{(k)}=1,2,4,4,4,4$ and $z^{(k)}=0,-0.893,-1.569,-1.898,-1.976,-1.994$ for $k=1..6$ (p. 426). So $z$ approaches $\hat z=-2$.
- Figure 19.3 (penalty) shows $\mu^{(k)}=1,2,4,8,16,32$ (p. 427).
- Figures 19.4–19.5: the two methods are compared on feasibility residual $|g(x^{(k)})|$ and on the norm of the optimality residual $\|2Df^Tf+Dg^Tz\|$, against cumulative LM iterations. The optimality-residual curve jumps when $\mu$ and $z$ are updated (steps 2–3 of AL, step 2 of penalty) (p. 425). In the plots the augmented Lagrangian needs roughly 110 LM iterations and keeps $\mu$ at about 4. The penalty method needs roughly 135 and $\mu$ exceeds $10^4$ (pp. 425, 428–429; plot readings, approximate).

### 19.4 Nonlinear control (pp. 425, 429–433)
A nonlinear dynamical system: $x_{k+1}=f(x_k,u_k)$, $k=1,\dots,N$, with state $x_k\in\mathbf R^n$ and input $u_k\in\mathbf R^m$. If $f$ is affine, it is linear (p. 425). The goal is to choose inputs, often with $x_1$ and $x_N$ fixed. To make inputs small and smooth, minimize
$$\sum_{k=1}^N\|u_k\|^2+\gamma\sum_{k=1}^{N-1}\|u_{k+1}-u_k\|^2,\quad \gamma>0$$
(p. 429). With a norm-squared objective, this is a large constrained nonlinear least squares problem, solved by the augmented Lagrangian method (p. 429).

**Car.** Position $p=(p_1,p_2)$, orientation $\theta$, wheelbase $L$ (known constant), steering angle $\phi$, speed $s$ (negative means reverse). Dynamics (p. 429):
$$\dot p_1=s\cos\theta,\quad \dot p_2=s\sin\theta,\quad \dot\theta=(s/L)\tan\phi$$
Assume $|\phi|<90^\circ$. At fixed $s,\phi$ the car moves in a circle (p. 430). Discretize with step $h$ (e.g. $p_1(t+h)\approx p_1(t)+hs(t)\cos\theta(t)$). State $x_k=(p_1,p_2,\theta)(kh)$, input $u_k=(s,\phi)(kh)$:
$$f(x_k,u_k)=x_k+h(u_k)_1\begin{bmatrix}\cos(x_k)_3\\ \sin(x_k)_3\\ \tan(u_k)_2/L\end{bmatrix}$$
Problem:
$$\begin{aligned}\text{minimize }&\textstyle\sum_{k=1}^N\|u_k\|^2+\gamma\sum_{k=1}^{N-1}\|u_{k+1}-u_k\|^2\\ \text{subject to }& x_2=f(0,u_1),\quad x_{k+1}=f(x_k,u_k),\ k=2,\dots,N-1,\quad x_{\rm final}=f(x_N,u_N)\end{aligned}\tag{19.12}$$
Variables are $u_1,\dots,u_N$ and $x_2,\dots,x_N$ (p. 430).

Results use $L=0.1$, $N=50$, $h=0.1$, $\gamma=10$ and several $x_{\rm final}$. Inputs start random, states at zero. Figure 19.7 shows trajectories, 19.8 the inputs, 19.9 the residuals (pp. 431–433).

*Intuition note:* The dynamics at each time step become equality constraints $g=0$. The input size and smoothness terms become the residuals $f$. The unknowns are all inputs and states stacked in one long $x$.

## Toy example (ours, not from the text)
Minimize $(x-2)^2$ subject to $g(x)=x-1=0$, $n=m=p=1$. Solution: $\hat x=1$. Condition (19.4): $2\cdot1\cdot(1-2)+1\cdot\hat z=0$, so $\hat z=2$. Run Algorithm 19.2 with $\mu=1$ held fixed (a simplification; the full rule would double $\mu$ here, since $\|g\|$ shrinks only by a factor 0.5), $z^{(1)}=0$:
- Step 1: minimize $(x-2)^2+(x-1+0)^2$. Derivative $2(x-2)+2(x-1)=0$, so $x=1.5$. Then $z=0+2\cdot1\cdot0.5=1$. (The penalty method's multiplier estimate $2\mu g$ is also 1 here.)
- Step 2: minimize $(x-2)^2+(x-1+0.5)^2$. Derivative $2(x-2)+2(x-0.5)=0$, so $x=1.25$. Then $z=1+2\cdot0.25=1.5$.
- Step 3: minimize $(x-2)^2+(x-1+0.75)^2$. Derivative $2(x-2)+2(x-0.25)=0$, so $x=1.125$. Then $z=1.5+2\cdot0.125=1.75$.

After three steps $x=1.125$ and $z=1.75$; the errors halve each step, so $x$ appears to approach 1 and $z$ to approach 2 with $\mu$ fixed at 1. Without the $z$ term, a penalty solution with $\mu=2$ gives $x$ from $2(x-2)+4(x-1)=0$, i.e. $x=4/3$, still infeasible.

## Concepts
- [[constrained-nonlinear-least-squares]] (new) — minimize $\|f(x)\|^2$ subject to $g(x)=0$ (p. 419)
- [[feasible-point]] (new) — a point with $g(x)=0$ (p. 419)
- [[lagrange-multiplier]] (new) — the vector $z$ in $L(x,z)=\|f\|^2+g^Tz$ (p. 420)
- [[optimality-condition-constrained]] (new) — $2Df^Tf+Dg^Tz=0$ plus $g=0$; necessary under a rank proviso, not sufficient (pp. 420–421)
- [[penalty-method]] (new) — minimize $\|f\|^2+\mu\|g\|^2$ for increasing $\mu$ (p. 421)
- [[augmented-lagrangian-method]] (new) — Lagrangian plus $\mu\|g\|^2$; update $z\leftarrow z+2\mu g$ (pp. 422–424)
- [[levenberg-marquardt-algorithm]] (new) — the ch. 18 unconstrained nonlinear least squares solver used as the inner step (p. 420)
- [[least-squares]] — the stacked residuals (19.6), (19.10) are ordinary nonlinear least squares problems (pp. 421, 423)
- [[nonlinear-control]] (new) — choose inputs of $x_{k+1}=f(x_k,u_k)$ to meet goals (p. 425)

## Canonical instances
- [[two-variable-al-example]] — $f,g$ with $\hat x=(0,0)$, $\hat z=-2$; AL vs penalty (pp. 424–429)
- [[car-steering-control]] — discretized car model solved as (19.12) (pp. 429–433)

## Bridges (candidates)
- [structural-analogy] penalty method with growing $\mu$ ↔ regularization/bi-objective least squares: the weighted trade-off $\|f\|^2+\mu\|g\|^2$ (ch. 16 bi-objective view, mentioned on p. 421)
- [structural-analogy] inner step (19.10) ↔ ordinary stacked least squares: minimize $\|r(x)\|^2$ for the stacked residual
- [metaphor] multiplier update $z\leftarrow z+2\mu g$ ↔ feedback correction: the constraint violation is fed back to adjust the price $z$

## Questions this raises
- Under what conditions do these heuristics converge to a solution, rather than only to a point satisfying (19.4)?
- Why is $\mu$ raised only when $\|g\|$ shrinks by less than a factor of 4 (the 0.25 in step 3)?
- How would inequality constraints be handled?
- What happens when the rows of $Dg(\hat x)$ are not linearly independent?

## Exercises worth doing
- Ex. 19.1 (p. 434) — implement augmented Lagrangian and penalty methods on a point-to-curve projection; compare residuals and $\mu$ — difficulty: medium
- Ex. 19.2(a) (p. 434) — formulate downside-risk portfolio optimization as constrained nonlinear least squares ($f$ and $g$) — difficulty: medium
- Ex. 19.2(b)–(c) (p. 434) — find $Df$, and use LM with linear equality constraints on real or simulated returns — difficulty: hard

## Reading notes
- Printed = pdf − 10.
- Some equations in the text layer (e.g. 19.6, 19.10, 19.12) are garbled or linearised; they were transcribed from the page images.
- Section 19.4 says the goal is to choose $u_1,\dots,u_{N-1}$, but problem (19.12) uses $u_1,\dots,u_N$; I follow (19.12).
- Iteration counts and the $\mu$ values quoted from figures 19.4 and 19.5 are read from plots, so they are approximate.
