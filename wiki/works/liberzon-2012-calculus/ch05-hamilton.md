---
id: liberzon-2012-calculus/ch05-hamilton
work: liberzon-2012-calculus
unit: "Chapter 5 — The Hamilton-Jacobi-Bellman equation"
pages: 125-144
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Hamilton-Jacobi-Bellman equation

## L0 — One line
Dynamic programming turns optimal control into a PDE for the value function (the HJB equation), which can give a feedback law (once the PDE is solved) and a sufficient test for optimality, but the value function is often not differentiable, so the PDE must be read in the viscosity sense.

## L1 — The gist (≤ 120 words)
How can we find the optimal decision at every state, not only the optimal path from one start? Bellman's idea is to work backward from the end. The principle of optimality gives a recursion for the value function V (the optimal cost-to-go). Taking small time steps turns it into the HJB partial differential equation. If a smooth solution exists and a control attains the HJB minimum along its path, that control is optimal; the minimizing control is a feedback law. But V can fail to be differentiable, even in a simple scalar example. The fix is the viscosity solution. V is, under suitable assumptions, its unique solution. The maximum principle is a different, open-loop route that avoids PDEs.

**Prerequisites:** Bolza cost and Hamiltonian $H=\langle p,f\rangle-L$ (Ch. 3–4); first-order Taylor expansion; gradients and partial derivatives; infimum; Lipschitz functions.

## L2 — Key ideas (5–10 bullets)
- Going backward in time costs $O(NMT)$ operations, versus $O(M^TT)$ forward, and it returns a state feedback law (p. 127).
- The value function $V(t,x)$ is the infimum of the cost from $(t,x)$. It obeys the principle of optimality (5.4), and existence of an optimal control is not assumed (pp. 127–128).
- A Taylor expansion of (5.4) gives the HJB equation (5.10), equivalently $V_t=\sup_u H(t,x,u,-V_x)$. The terminal cost enters only through the boundary condition (pp. 129–130).
- A $\mathcal C^1$ solution of HJB with the boundary condition, together with a control that attains the minimum along a trajectory, gives a globally optimal control, and its proof is a short integration argument (pp. 132–133).
- HJB gives closed-loop (feedback) control but needs a PDE solved. The maximum principle is open-loop but needs only ODEs. Formally, $p^*=-V_x$ (pp. 135–136).
- For $\dot x=xu$ with cost $x(t_1)$, $V$ is not $\mathcal C^1$ at $x=0$, so $V\in\mathcal C^1$ cannot be assumed in general (p. 136).
- Super- and sub-differentials generalize the gradient. Viscosity solutions are defined with them, and the sign convention of the PDE matters (pp. 137–141).
- Under suitable assumptions, $V$ is the unique viscosity solution of HJB with boundary condition (5.3) and is locally Lipschitz (p. 141).

## L3 — Walkthrough

### 5.1 Dynamic programming and the HJB equation
Bellman's aim: determine the optimal decision at any state, not only the optimal sequence from one fixed state (p. 125). The resulting theory differs from Chapter 4's, but both have roots in calculus of variations (p. 125).

#### 5.1.1 The discrete problem
System $x_{k+1}=f(x_k,u_k)$, $k=0,\dots,T-1$. Here $x_k$ lies in a finite set of $N$ elements and $u_k$ in a finite set of $M$ elements. Each transition has a cost, and there is a terminal cost on $x_T$. The total cost is the sum of the transition costs plus the terminal cost. The final state is free (p. 125).

- **Forward enumeration.** There are $M^T$ trajectories and $T$ additions per cost, so about $O(M^TT)$ operations (p. 126).
- **Backward scheme.** At $k=T$ the costs are the terminal costs. For $k=T-1,\dots,0$, at each $x_k$ pick the jump minimizing one-step cost plus the already computed cost-to-go, and record it. Ties are broken at random (p. 126).
- Justification: the principle of optimality. If $x_k$ lies on an optimal trajectory, the remaining decisions are optimal with $x_k$ as initial condition. So discarded paths cannot be parts of optimal trajectories (p. 126).
- Cost: for each $k$, $x_k$ and $u_k$ one addition, so $O(NMT)$. This is better than $O(M^TT)$ for large $T$ with $N,M$ fixed. It is still large if $N,M$ are large (the "curse of dimensionality") (p. 127).
- Backward also yields the optimal decision at every $x_k$ for all $k$, i.e. a state feedback law. Forward would need $O(NM^TT)$ to cover all initial conditions and still gives no feedback (p. 127).

*Intuition note:* Backward, each state keeps only its best continuation, so the number of paths never explodes. What remains is a table "at this state, do this", which is a feedback rule.

#### 5.1.2 Principle of optimality
Fixed-time, free-endpoint problem, target set $S=\{t_1\}\times\mathbb R^n$ (p. 127). Family of cost functionals, for $t\in[t_0,t_1)$ and $x\in\mathbb R^n$:
$$J(t,x,u)=\int_t^{t_1}L(s,x(s),u(s))\,ds+K(x(t_1)),\quad x(t)=x \tag{5.1}$$
Value function:
$$V(t,x):=\inf_{u_{[t,t_1]}}J(t,x,u)\tag{5.2}$$
An optimal control is not assumed to exist, hence the infimum. If one exists, $V$ is the optimal cost-to-go. In general the infimum need not be attained and may even be $-\infty$ (pp. 127–128).

Boundary condition: $V(t_1,x)=K(x)$ for all $x$ (5.3). For a general target set $S$ it reads $V=K$ on $S$ (p. 128).

**Principle of optimality.** For every $(t,x)\in[t_0,t_1)\times\mathbb R^n$ and every $\Delta t\in(0,t_1-t]$,
$$V(t,x)=\inf_{u_{[t,t+\Delta t]}}\Big\{\int_t^{t+\Delta t}L(s,x(s),u(s))\,ds+V(t+\Delta t,x(t+\Delta t))\Big\}\tag{5.4}$$
with $x(t)=x$ (p. 128). The problem on $[t,t_1]$ splits into one on $[t,t+\Delta t]$ and one on $[t+\Delta t,t_1]$ (p. 128).

**Proof of "one half".** Let $\overline V(t,x)$ denote the right side of (5.4). Claim: $V\ge\overline V$ (5.5). For every $\varepsilon>0$ there is $u_\varepsilon$ with
$$V(t,x)+\varepsilon\ge J(t,x,u_\varepsilon)\tag{5.6}$$
Then, with $x_\varepsilon$ the trajectory:
$$J(t,x,u_\varepsilon)=\int_t^{t+\Delta t}L(s,x_\varepsilon,u_\varepsilon)ds+J(t+\Delta t,x_\varepsilon(t+\Delta t),u_\varepsilon)\ \ge\ \int_t^{t+\Delta t}L\,ds+V(t+\Delta t,x_\varepsilon(t+\Delta t))\ \ge\ \overline V(t,x).$$
The two inequalities come from the definitions of $V$ and $\overline V$. Since $\varepsilon$ is arbitrary, (5.5) follows (p. 129). The reverse inequality is Exercise 5.1 (p. 129).

#### 5.1.3 The HJB equation
Assume for now that $V\in\mathcal C^1$ (validity examined later, p. 129). Taylor expansions (using $x(t+\Delta t)=x+f(t,x,u(t))\Delta t+o(\Delta t)$):
$$V(t+\Delta t,x(t+\Delta t))=V+V_t\Delta t+\langle V_x,f(t,x,u(t))\Delta t\rangle+o(\Delta t)\tag{5.7}$$
$$\int_t^{t+\Delta t}L\,ds=L(t,x,u(t))\Delta t+o(\Delta t)\tag{5.8}$$
Insert both in (5.4). The $V(t,x)$ terms cancel, because the one inside the infimum does not depend on $u$:
$$0=\inf_{u_{[t,t+\Delta t]}}\{L\Delta t+V_t\Delta t+\langle V_x,f\rangle\Delta t+o(\Delta t)\}\tag{5.9}$$
Divide by $\Delta t$ and let $\Delta t\to0$. The $o(\Delta t)/\Delta t$ term vanishes, and the infimum is over the instantaneous value of $u$. $V_t$ is pulled out (p. 129–130). The result is the **HJB equation**, which must hold for all $t\in[t_0,t_1)$ and $x\in\mathbb R^n$:
$$-V_t(t,x)=\inf_{u\in U}\{L(t,x,u)+\langle V_x(t,x),f(t,x,u)\rangle\}\tag{5.10}$$
It is a PDE, with boundary condition (5.3) (p. 130).

- The terminal cost and terminal time play no role in the derivation. Only the boundary condition changes with the target set. HJB does not hold on $S$, nor at $t=t_1$, because the principle of optimality is not valid there (p. 130).
- Equivalent form (5.11): $V_t=\sup_u\{\langle -V_x,f\rangle-L\}$. With $H(t,x,u,p)=\langle p,f(t,x,u)\rangle-L(t,x,u)$ (3.29), the expression is the Hamiltonian with $-V_x$ as costate:
$$V_t(t,x)=\sup_{u\in U}H(t,x,u,-V_x(t,x))\tag{5.12}$$
- If a globally optimal $u^*$ exists, the infimum becomes a minimum attained at $u^*$. The same steps give
$$-V_t(t,x^*(t))=\min_u\{L(t,x^*,u)+\langle V_x,f(t,x^*,u)\rangle\}=L(t,x^*,u^*)+\langle V_x,f(t,x^*,u^*)\rangle\tag{5.13}$$
$$H(t,x^*,u^*,-V_x(t,x^*))=\max_{u\in U}H(t,x^*,u,-V_x(t,x^*))\tag{5.14}$$
This is analogous to the maximum principle's Hamiltonian maximization (p. 130–131). If the maximizer has a closed form, HJB becomes more explicit (p. 131).

*Intuition note:* The HJB equation says that the cost-to-go decreases at the best possible rate: running cost plus the drift of $V$ along the dynamics is minimized by the optimal control. The $V$ in the PDE is the unknown.

**Example 5.1.** $\dot x=u$, $L=x^4+u^4$. HJB: $-V_t=\inf_u\{x^4+u^4+V_xu\}$ (5.15). Setting $4u^3+V_x=0$ gives $u=-(\tfrac14V_x)^{1/3}$. Substituting:
$$-V_t=x^4-3(\tfrac14V_x)^{4/3}\tag{5.16}$$
If solved, $u^*(t)=-(\tfrac14V_x(t,x^*(t)))^{1/3}$ is a state feedback. Solving (5.16) appears difficult (p. 131).

**Example 5.2.** Minimal-time parking (Section 4.4.1). This is a free-time, fixed-endpoint problem, with $V(t,0)=0$ and HJB valid away from $x=0$:
$$-V_t=\inf_{u\in[-1,1]}\{1+V_{x_1}x_2+V_{x_2}u\}\tag{5.17}$$
The infimum is attained at $u=-\operatorname{sgn}(V_{x_2})$: $u=1$ if $V_{x_2}<0$, $u=-1$ if $V_{x_2}>0$, undetermined if $V_{x_2}=0$. Then
$$-V_t=1+V_{x_1}x_2-|V_{x_2}|\tag{5.18}$$
The feedback $u^*=-\operatorname{sgn}(V_{x_2}(t,x^*))$ is usable only if (5.18) can be solved (p. 131). Exercise 5.2 invites the reader to simplify and solve it.

**Infinite-horizon problem.** Suppose $f=f(x,u)$, $L=L(x,u)$, $K\equiv0$, and let $t_1\to\infty$ with the final state free. Then $V=V(x)$, $V_t=0$, and
$$0=\inf_{u\in U}\{L(x,u)+\langle V_x(x),f(x,u)\rangle\}\tag{5.19}$$
For scalar $x$ this is an ODE. The problem is treated formally; well-posedness is not checked here (p. 132, footnote 2). For Example 5.1 it becomes $x^4-3(\tfrac14V_x)^{4/3}=0$, so $V_x=\pm(\tfrac13)^{3/4}4x^3$. The plus sign is chosen because $V$ should be positive definite, since $L$ is. The feedback needs only $V_x$:
$$u^*=-(\tfrac14V_x(x^*))^{1/3}=-(\tfrac13)^{1/4}x^*(t)$$
(p. 132).

#### 5.1.4 Sufficient condition for optimality
So far HJB and (5.14) have been shown only to be necessary (p. 132). **Theorem.** Suppose a $\mathcal C^1$ function $\widehat V:[t_0,t_1]\times\mathbb R^n\to\mathbb R$ satisfies
$$-\widehat V_t(t,x)=\inf_{u\in U}\{L(t,x,u)+\langle\widehat V_x(t,x),f(t,x,u)\rangle\}\tag{5.20}$$
for all $t\in[t_0,t_1)$ and all $x$, and
$$\widehat V(t_1,x)=K(x).\tag{5.21}$$
Suppose a control $\hat u$ and trajectory $\hat x$ with $\hat x(t_0)=x_0$ satisfy, everywhere,
$$L(t,\hat x,\hat u)+\langle\widehat V_x(t,\hat x),f(t,\hat x,\hat u)\rangle=\min_{u\in U}\{L(t,\hat x,u)+\langle\widehat V_x(t,\hat x),f(t,\hat x,u)\rangle\}\tag{5.22}$$
which is equivalent to $H(t,\hat x,\hat u,-\widehat V_x)=\max_uH(t,\hat x,u,-\widehat V_x)$. Then $\widehat V(t_0,x_0)=V(t_0,x_0)$ and $\hat u$ is optimal. Uniqueness of the optimal control is not claimed (pp. 132–133).

**Proof.**
1. By (5.20) and (5.22): $-\widehat V_t(t,\hat x)=L(t,\hat x,\hat u)+\langle\widehat V_x,f(t,\hat x,\hat u)\rangle$. The terms $\widehat V_t+\langle\widehat V_x,f\rangle$ form the total derivative of $\widehat V$ along $\hat x$, so $0=L(t,\hat x,\hat u)+\frac d{dt}\widehat V(t,\hat x(t))$ (p. 133).
2. Integrate over $[t_0,t_1]$ and use (5.21) and the initial condition:
$$\widehat V(t_0,x_0)=\int_{t_0}^{t_1}L(t,\hat x,\hat u)dt+K(\hat x(t_1))=J(t_0,x_0,\hat u)\tag{5.23}$$
3. For any other control $u$ with the same initial condition, (5.20) gives $-\widehat V_t(t,x)\le L+\langle\widehat V_x,f\rangle$, i.e. $0\le L(t,x,u)+\frac d{dt}\widehat V(t,x(t))$. Integrating:
$$\widehat V(t_0,x_0)\le J(t_0,x_0,u)\tag{5.24}$$
So $\hat u$ attains $\widehat V(t_0,x_0)$ and no control does better (p. 133).

The optimality is global. $\widehat V(t,\hat x(t))$ is also the optimal cost-to-go along $\hat x$. If a family of controls parameterized by $(t,x)$ satisfies the maximization condition along its trajectories, each starting at $x(t)=x$, then $\widehat V$ is the value function and all of them are optimal. Such a family typically arises from a state feedback law (Chapter 6) (p. 134). Exercises 5.3 and 5.4 give variants (p. 134).

*Intuition note:* If you can guess any smooth $\widehat V$ that fits HJB and its boundary condition, then the cost of any control is at least $\widehat V(t_0,x_0)$. A control that makes the HJB infimum an equality along its path reaches that bound.

#### 5.1.5 Historical remarks (pp. 134–135)
The HJB PDE originates with Hamilton and Jacobi (late 1830s) as a necessary condition in calculus of variations. Carathéodory (1920s–1935) proposed its use as a sufficient condition. The principle of optimality goes back to Jacob Bernoulli (1697) and was formalized by Isaacs in the early 1950s, slightly before Bellman. Bellman coined "dynamic programming" and used it to study value functions globally. Kalman, in the early 1960s, explicitly made the connection to Hamilton-Jacobi (it is not clear that Bellman was aware of it) and was apparently the first to use the name "HJB equation". The maximum principle developed in the Soviet Union around the same time.

### 5.2 HJB equation versus the maximum principle
Take time-invariant $f,L$ (p. 135).
- **Maximum principle:** canonical equations $\dot x^*=H_p|_*$, $\dot p^*=-H_x|_*$ (5.25) and $u^*(t)=\arg\max_uH(x^*,u,p^*)$ (5.26). This is **open-loop**, since $u^*$ depends on the costate $p^*$ from the adjoint ODE.
- **HJB:** $u^*(t)=\arg\max_uH(x^*,u,-V_x(t,x^*))$ (5.27). This is **closed-loop**, since $u^*$ is determined by the current state once $V$ is known.
- Computation: finding $V$ means solving a PDE, which is generally very hard. The maximum principle needs only ODEs and often solves problems where HJB is intractable. In principle, dynamic programming gives more information, including sufficiency (p. 135).

**Can the maximum principle be proved from HJB?** The formulas suggest $p^*(t):=-V_x(t,x^*(t))$ (5.29). Then (5.26) follows from (5.27). If $V(t_1,x)=K(x)$, then $p^*(t_1)=-K_x(x^*(t_1))$, which matches (4.43). That $p^*$ satisfies $\dot p^*=-H_x$ is true too (Exercise 5.5) (pp. 135–136).

So the adjoint vector can be read as the gradient of the value function, i.e. the sensitivity of optimal cost to the state. In economic terms it is a "marginal value" or "shadow price" (p. 136).

The gap: the argument needs second-order derivatives of $V$, and at least $V\in\mathcal C^1$, which is not true in general (p. 136).

#### 5.2.1 Example: nondifferentiable value function
Scalar $\dot x=xu$, $u\in[-1,1]$, fixed time, free endpoint, cost $J=x(t_1)$. By inspection: if $x_0>0$ use $u\equiv-1$; if $x_0<0$ use $u\equiv1$; if $x_0=0$ then $x\equiv0$. Then
$$V(t,x)=\begin{cases}e^{-(t_1-t)}x&x>0\\ e^{t_1-t}x&x<0\\0&x=0\end{cases}\tag{5.30}$$
Away from $x=0$ it satisfies $-V_t=\inf_u\{V_xxu\}=-|V_xx|$ with $V(t_1,x)=x$. At $x=0$, $V$ is Lipschitz but not $\mathcal C^1$ (Fig. 5.4). It can be shown that this HJB equation has no $\mathcal C^1$ solution (p. 136).

Such behavior is typical for problems with bounded controls and terminal cost. Local Lipschitz continuity is a known property of value functions for some reasonably general classes of problems. So there is no "easy" proof of the maximum principle, and HJB theory needs a generalized solution concept. Rigor came in the early 1980s with Crandall and Lions's viscosity solutions (p. 137).

*Intuition note:* At $x=0$ the optimal action changes sign, and $V$ has a kink there. At a kink the gradient, and hence a costate $-V_x$, is not defined.

### 5.3 Viscosity solutions of the HJB equation

#### 5.3.1 One-sided differentials
Let $v:\mathbb R^n\to\mathbb R$ be continuous. $\xi$ is a **super-differential** of $v$ at $x$ if, for $y$ near $x$,
$$v(y)\le v(x)+\langle\xi,y-x\rangle+o(|y-x|)\tag{5.31}$$
i.e. the linear function lies locally above the graph. The set is $D^+v(x)$. A **sub-differential** satisfies
$$v(y)\ge v(x)+\langle\xi,y-x\rangle-o(|y-x|)\tag{5.32}$$
(lies below), with set $D^-v(x)$ (pp. 137–138).

**Example 5.3.** $v(x)=0$ for $x<0$, $\sqrt x$ for $0\le x\le1$, $1$ for $x>1$. Then $D^+v(0)=\emptyset$, $D^-v(0)=[0,\infty)$, $D^+v(1)=[0,1/2]$, $D^-v(1)=\emptyset$ (p. 138).

Properties:
- **Test functions** (proof not given). $\xi\in D^+v(x)$ iff there is a $\mathcal C^1$ $\varphi$ with $\nabla\varphi(x)=\xi$, $\varphi(x)=v(x)$ and $\varphi\ge v$ near $x$, i.e. $\varphi-v$ has a local minimum at $x$. Likewise $\xi\in D^-v(x)$ iff $\varphi-v$ has a local maximum at $x$ (pp. 138–139).
- **Relation with classical differentials.** If $v$ is differentiable at $x$, then $D^+v(x)=D^-v(x)=\{\nabla v(x)\}$ (5.33). If both are nonempty, $v$ is differentiable at $x$ and (5.33) holds. Proof of the second claim:
  1. Take $\varphi_1,\varphi_2\in\mathcal C^1$ with $\varphi_1(x)=v(x)=\varphi_2(x)$ and $\varphi_1\le v\le\varphi_2$ near $x$. Then $\varphi_1-\varphi_2$ has a local maximum at $x$, so $\nabla\varphi_1(x)=\nabla\varphi_2(x)$.
  2. For $y>x$, $\frac{\varphi_1(y)-\varphi_1(x)}{y-x}\le\frac{v(y)-v(x)}{y-x}\le\frac{\varphi_2(y)-\varphi_2(x)}{y-x}$. The outer fractions tend to the same limit, so the middle one does too, and that limit is $\nabla v(x)$ (p. 139).
- **Non-emptiness and denseness.** The sets $\{x:D^+v(x)\ne\emptyset\}$ and $\{x:D^-v(x)\ne\emptyset\}$ are nonempty and dense in the domain of $v$. Idea: a steep enough $\mathcal C^1$ $\varphi$ makes $\varphi-v$ have a local maximum near any chosen $x_0$ (Fig. 5.8) (p. 139). Exercise 5.6 asks for a $v$ where both sets are empty at some $x$ (p. 140).

#### 5.3.2 Viscosity solutions of PDEs
PDE: $F(x,v(x),\nabla v(x))=0$ with $F$ continuous (5.34).
- **Viscosity subsolution:** continuous $v$ with $F(x,v(x),\xi)\le0$ for all $\xi\in D^+v(x)$, all $x$ (5.35). Equivalently, $F(x,v,\nabla\varphi(x))\le0$ for every $\mathcal C^1$ $\varphi$ with $\varphi-v$ having a local minimum at $x$.
- **Viscosity supersolution:** $F(x,v(x),\xi)\ge0$ for all $\xi\in D^-v(x)$ (5.36); equivalently with $\varphi-v$ having a local maximum.
- **Viscosity solution:** both (p. 140).

Conditions bind only where $D^\pm v$ is nonempty, a dense set. Where $v$ is differentiable the PDE holds classically. If $v$ is Lipschitz, it is differentiable almost everywhere (Rademacher's theorem) (p. 140).

**Example 5.4.** $F=1-|\xi|$ (PDE $1-|v'|=0$). $v=\pm x+c$ are classical solutions. $v=|x|$ is a viscosity solution: $D^+v(0)=\emptyset$, so (5.35) holds; $D^-v(0)=[-1,1]$ and $1-|\xi|\ge0$ there, so (5.36) holds (p. 140). The definition is not symmetric: for the PDE written as $|v'|-1=0$, $|x|$ is no longer a viscosity solution (p. 141).

**Why "viscosity".** A viscosity solution $v$ can be obtained as the limit $\varepsilon\to0$ of smooth solutions $v_\varepsilon$ of
$$F(x,v_\varepsilon,\nabla v_\varepsilon)=\varepsilon\Delta v_\varepsilon\tag{5.37}$$
($\Delta$ is the Laplacian; it appears in viscous-fluid motion). Sketch for the supersolution property: take $\xi\in D^-v(x_0)$ and a $\mathcal C^2$ test function $\varphi$ with $\varphi-v$ having a local maximum at $x_0$. If $v_\varepsilon$ is close to $v$ for small $\varepsilon$, then $\varphi-v_\varepsilon$ has a local maximum at some $x_\varepsilon$ near $x_0$, so $\nabla\varphi(x_\varepsilon)=\nabla v_\varepsilon(x_\varepsilon)$ and $\Delta\varphi(x_\varepsilon)\le\Delta v_\varepsilon(x_\varepsilon)$. Hence $F(x_\varepsilon,v_\varepsilon(x_\varepsilon),\nabla\varphi(x_\varepsilon))\ge\varepsilon\Delta\varphi(x_\varepsilon)$. As $\varepsilon\to0$, continuity of $F$ gives $F(x_0,v(x_0),\nabla\varphi(x_0))\ge0$. The subsolution argument is similar (p. 141).

#### 5.3.3 HJB equation and the value function
Rewrite HJB as
$$-V_t(t,x)-\inf_{u\in U}\{L(t,x,u)+\langle V_x(t,x),f(t,x,u)\rangle\}=0\tag{5.38}$$
This sign convention is the correct one for viscosity solutions. The variable $t$ can be absorbed via $x_{n+1}:=t$, with domain $[t_0,t_1]\times\mathbb R^n$ (p. 141).

**Main result.** Under suitable technical assumptions on $f,L,K$, the value function $V$ is the unique viscosity solution of (5.38) with boundary condition (5.3). It is also locally Lipschitz, but not necessarily $\mathcal C^1$. The assumptions hold, for example, if $f,L,K$ are uniformly continuous, $f_x,L_x,K_x$ are bounded, and $U$ is compact (p. 141). Uniqueness and Lipschitz continuity are not proved here (p. 142).

**Proof that $V$ is a viscosity subsolution** (no extra assumptions needed). Fix $(t_0,x_0)$. Suppose, for contradiction, that a $\mathcal C^1$ $\varphi$ and $u_0\in U$ exist with
$$\varphi(t_0,x_0)=V(t_0,x_0),\ \ \varphi\ge V\text{ near }(t_0,x_0)\tag{5.39}$$
$$-\varphi_t(t_0,x_0)-L(t_0,x_0,u_0)-\langle\varphi_x(t_0,x_0),f(t_0,x_0,u_0)\rangle>0\tag{5.40}$$
Apply $u\equiv u_0$ on $[t_0,t_0+\Delta t]$ with $\Delta t$ small. Then
$$V(t_0+\Delta t,x(t_0+\Delta t))-V(t_0,x_0)\le\varphi(t_0+\Delta t,x(\cdot))-\varphi(t_0,x_0)=\int_{t_0}^{t_0+\Delta t}\tfrac d{dt}\varphi\,dt=\int(\varphi_t+\langle\varphi_x,f\rangle)dt<-\int L(t,x(t),u_0)dt$$
The first inequality uses (5.39), the last uses (5.40) and continuity. Hence
$$V(t_0,x_0)>\int_{t_0}^{t_0+\Delta t}L(t,x(t),u_0)dt+V(t_0+\Delta t,x(t_0+\Delta t))\tag{5.41}$$
This contradicts the principle of optimality (5.4), which gives "$\le$" for this particular control (p. 142). The supersolution case is Exercise 5.7. Exercise 5.8 asks the reader to formulate and prove a sufficient condition for optimality in the viscosity framework (p. 142).

*Intuition note:* A smooth function touching $V$ from above would force $V$ to fall faster than any control allows. That would beat the principle of optimality. So the HJB inequality holds in the weak sense even at kinks.

### 5.4 Notes and references (p. 143)
The author lists sources for each section: [Son98, Section 8.1] for the discrete case, [BP07, Chapter 8] for Section 5.3, and [CL83] as the original reference on viscosity solutions. Details are in the book's bibliography.

## Toy example (ours)
Discrete backward DP (Section 5.1.1). States $\{0,1\}$, controls $u\in\{0,1\}$, dynamics $x_{k+1}=u_k$, $T=2$. Transition costs $c(x,u)$: $c(0,0)=2$, $c(0,1)=1$, $c(1,0)=4$, $c(1,1)=3$. Terminal cost $K(0)=5$, $K(1)=0$.

- $k=2$: $V_2(0)=5$, $V_2(1)=0$.
- $k=1$: $V_1(0)=\min\{2+5,\ 1+0\}=1$ (choose $u=1$). $V_1(1)=\min\{4+5,\ 3+0\}=3$ (choose $u=1$).
- $k=0$: $V_0(0)=\min\{2+V_1(0),\ 1+V_1(1)\}=\min\{3,4\}=3$ (choose $u=0$). $V_0(1)=\min\{4+V_1(0),\ 3+V_1(1)\}=\min\{5,6\}=5$ (choose $u=0$).

The feedback is "$u=0$ at $k=0$, $u=1$ at $k=1$", from either state. Check by brute force from $x_0=0$, over $(u_0,u_1)$: (0,0): $2+2+5=9$; (0,1): $2+1+0=3$; (1,0): $1+4+5=10$; (1,1): $1+3+0=4$. The minimum is 3, equal to $V_0(0)$. Backward needed $2\cdot2\cdot2=8$ additions; the enumeration needed 4 paths × 2 additions = 8. The saving appears only for larger $T$.

## Concepts
- [[principle of optimality]] — the tail of an optimal plan is optimal from the state where it starts; here stated as (5.4) (p. 128)
- [[Bellman equation / value function]] — $V(t,x)=\inf_u J(t,x,u)$, the optimal cost-to-go; infimum allowed, no existence assumed (p. 127)
- [[Hamilton–Jacobi–Bellman equation]] — PDE (5.10) for $V$; equivalently $V_t=\sup_uH(t,x,u,-V_x)$ (p. 130)
- [[Pontryagin maximum principle]] — open-loop necessary condition via costate; compared with HJB in 5.2 (p. 135)
- [[open loop vs closed loop]] — maximum principle gives $u^*(t)$ via costate (open); HJB gives $u^*$ from the current state (closed) (p. 135)
- [[policy]] — optimal control as a state feedback law, obtained by backward DP (p. 127)
- [[dynamic-programming]] (new) — solving a family of problems backward via the value function (p. 127)
- [[curse-of-dimensionality]] (new) — backward cost $O(NMT)$ is still large if $N,M$ are large (p. 127)
- [[sufficient-condition-for-optimality]] (new) — a $\mathcal C^1$ $\widehat V$ solving HJB plus (5.22) implies optimality (pp. 132–133)
- [[costate-as-shadow-price]] (new) — $p^*=-V_x$, sensitivity of optimal cost to state (p. 136)
- [[super-sub-differential]] (new) — sets $D^\pm v(x)$ of slopes of locally touching lines, from above or below (pp. 137–138)
- [[viscosity-solution]] (new) — continuous $v$ that is both sub- and supersolution via $D^\pm v$; sign convention matters (pp. 140–141)

## Canonical instances
- [[discrete-backward-dp]] — backward recursion beats forward enumeration and gives feedback (pp. 126–127)
- [[quartic-integrator-hjb]] — $\dot x=u$, $L=x^4+u^4$, HJB (5.16) and infinite-horizon feedback $-(1/3)^{1/4}x$ (pp. 131–132)
- [[minimal-time-parking-hjb]] — HJB (5.18), bang-bang feedback $-\operatorname{sgn}(V_{x_2})$ (p. 131)
- [[nondifferentiable-value-function]] — $\dot x=xu$, cost $x(t_1)$, $V$ not $\mathcal C^1$ at 0 (p. 136)
- [[abs-value-viscosity-solution]] — $|x|$ solves $1-|v'|=0$ in the viscosity sense, not $|v'|-1=0$ (pp. 140–141)

## Bridges (candidates)
- [structural-analogy] value function and HJB ↔ reinforcement learning: Bellman equation — the continuous-time, deterministic analogue of the recursion (5.4)
- [structural-analogy] costate $p^*=-V_x$ ↔ economics: shadow price — the author makes this analogy (p. 136)
- [structural-analogy] backward elimination of discarded paths ↔ discrete-time optimal control: backward recursion for feedback — both build a state-dependent policy
- [metaphor] vanishing viscosity limit ↔ fluid mechanics: adding diffusion $\varepsilon\Delta v$ smooths solutions; the limit selects the weak solution

## Questions this raises
- Under what assumptions on $f,L,K,U$ does uniqueness of the viscosity solution hold, and what breaks if $U$ is not compact?
- How does the HJB feedback look for linear systems with quadratic cost (the next chapter's case)?
- How could the maximum principle be derived using viscosity solutions or one-sided differentials of $V$ (Section 7.2 is mentioned)?
- Can numerical schemes preserve the viscosity property when $V$ has kinks?

## Exercises worth doing
- Ex. 5.1 (p. 129) — reverse inequality of the principle of optimality — difficulty: medium
- Ex. 5.2 (p. 131) — solve the parking HJB and recover the bang-bang law — difficulty: hard
- Ex. 5.3 (p. 134) — sufficiency when $\widehat V(t_0,x_0)$ equals the cost of $\hat u$ — difficulty: medium
- Ex. 5.5 (p. 136) — show $p^*=-V_x$ satisfies the adjoint equation — difficulty: hard
- Ex. 5.6 (p. 140) — function with both $D^+v$ and $D^-v$ empty at a point — difficulty: easy
- Ex. 5.7 (p. 142) — $V$ is a viscosity supersolution — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 135 = p. 125). Pdf 154 (p. 144) holds only the running header.
- Figures and some equations in the text layer were garbled; I checked all equations against the page images.
- In 5.1.5, the historical claims are the author's as stated there. I added no outside dates.
- In 5.4, I summarized only the reference notes (p. 143) very briefly and did not reproduce the bibliography.
