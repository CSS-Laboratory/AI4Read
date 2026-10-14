---
id: bellman-1957-dp/ch09-ix
work: bellman-1957-dp
unit: "Chapter IX. A New Formalism in the Calculus of Variations"
pages: 245-282
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# A New Formalism in the Calculus of Variations (Bellman, Ch. IX)

## L0 — One line
A variational problem can be treated as a continuous multi-stage decision process: the optimal value, as a function of the current state (and remaining time), obeys a partial differential equation (or a difference recursion) that also gives the optimal action as a function of the state.

## L1 — The gist (≤ 120 words)
Bellman asks how to solve classical variational problems without treating the optimal curve as one point in function space. His answer: let the optimal value depend on the current state (and remaining time), apply the principle of optimality (the remaining path must be optimal for the state reached) over a short interval, and let the interval shrink. This gives a partial differential equation and a policy that maps state to action. He adds discrete recursions that compute solutions and avoid a number of analytic and stability difficulties. He also covers inequality constraints, integral constraints, an eigenvalue problem, and improvement of policies step by step. The treatment is explicitly formal: existence and differentiability are assumed, not proved.

**Prerequisites:** partial derivatives; first-order Taylor expansion and $o(S)$; 2×2 determinants; ordinary differential equations; the classical Euler equation (named in the text, not derived); $\limsup/\liminf$ (for §12).

## L2 — Key ideas (5–10 bullets)
- **Policy view of extremals.** An extremal (the optimal curve) is a continuous policy: the next move expressed through the current state (e.g. $dy/dx$ in terms of $y$ and the velocity, or of $y$ and remaining length). Curves are described by tangents, a dual to point coordinates (pp. 246–248).
- **Basic equation.** For $\max\int_0^\infty F\,dt$ with $dx/dt=G$, the value $f(c)$ satisfies $0=\max_v[F(c,v)+G(c,v)f'(c)]$. Eliminating $f'$ gives a determinantal equation (a $2\times2$ determinant set to zero) for $v(c)$ (pp. 249–251).
- **Finite horizon.** With remaining time $T$ as extra state, $0=\max_v[F+Gf_c-f_T]$. Equating mixed partials gives a first-order PDE for $v(c,T)$, with $v(c,0)$ from maximizing $F(c,v)$ (pp. 252–253).
- **Constraints and structure.** For $0\le y\le x$, no uniform analytic technique exists. Under strict concavity in $v$ and $G$ linear in $v$, the maximizer is continuous, so boundary arcs must be adjacent to interior arcs (pp. 253–256).
- **Discrete recursion as a rigorous and, in cases treated so far, more reliable route.** Replace the PDE by $f_{N+1}(c)=\max_v[\Delta F+f_N(c+\Delta G)]$. Convergence to $f(c,T)$ is proved for a typical case (Theorem 2). This avoids a number of the stability difficulties of difference-equation solvers for the PDE (pp. 246, 259–263).
- **Eigenvalue problem.** The two-point boundary problem is embedded in a family indexed by the starting point $a$ and value $k=u(a)$, with renormalization. This yields a PDE for $f(a,k)$ (pp. 267–270).
- **Successive approximation in policy space.** Iterating on $f$ directly is useless (it returns $f$). Iterating on the policy $v$ gives a monotonically increasing sequence $f_n$ (pp. 271–272).
- **Uniqueness** of the PDE solution follows from a comparison argument (p. 273).
- **Min-max cost** problems reduce to a recursion with a $\max$ outside the $\min$ (pp. 273–274).

## L3 — Walkthrough

### §1 Introduction (pp. 245–246)
The unit studies two classes of problems; every statement below is the author's.

Class 1: extremize
$$J(z)=\int_0^T F(x_1,\dots,x_n,z_1,\dots,z_m)\,dt \tag{2}$$
subject to $dx_i/dt=G_i(x,z)$, $x_i(0)=c_i$ (3a) and $R_k(x,z)\le 0$, $k=1,\dots,l$ (3b). This generalizes the production problem of earlier chapters: maximize $(x(T),a)$ subject to $dx/dt=Az$, $x(0)=c$, $Bz\le Cx$, $z\ge0$ (1). There the maximum depends only on $c$ and $T$ (assumed attained), which led to a functional equation and then a PDE (p. 245).

Class 2: the eigenvalue problem $u''+\lambda^2\varphi(t)u=0$, $u(0)=u(1)=0$ (4). Under reasonable assumptions on $\varphi$ it is equivalent to finding relative minima of $J(u)=\int_0^1u'^2dt$ (5) subject to $\int_0^1\varphi u^2dt=1$ and $u(0)=u(1)=0$ (6). The two-point boundary condition brings "novelty and difficulty" (p. 246).

Plan: state variables, a functional equation, its limiting PDE; numerical solution by partial difference equations, then an alternative route by difference equations that bypasses analytic difficulties and stability problems; Chebyshev ("Cebycev") functionals $\max_{0\le t\le T}F$. The viewpoint is purely formal; rigor is deferred to a second volume (p. 246).

### §2 A new approach (pp. 246–248)
Classical technique treats an extremal as a point in function space characterized by variational properties. Here the calculus of variations is a class of continuous multi-stage decision processes, and an extremal is a continuous policy (p. 246).

- Example 1 (brachistochrone: least-time path of a particle under gravity from $P$ to $Q$). Whatever the path from $P$ to an intermediate point $R$, the path $RQ$ must minimize the time from $R$ to $Q$, given the velocity at $R$. The extremal can be expressed as $dy/dx$ in terms of $y$ and the left-hand velocity at $(x,y)$ (p. 247).
- Example 2 (isoperimetric problem: curve of fixed length $L$ from $P$ to $Q$ enclosing maximum area). The continuation from $R$ to $Q$ must maximize the area $RR'Q'Q$ given length $L-L'$. The policy is $dy/dx$ in terms of $y$ and $L-L'$ (p. 247).

Both are applications of the principle of optimality (p. 247). Advantage: the next move in terms of the current state is often a simpler, more natural, even more important piece of information than the whole move sequence from a fixed start (p. 248). Geometrically we seek intrinsic equations, regarding the curve as an envelope of tangents (dual to point coordinates). Combining local and global descriptions is most powerful (p. 248).

*Intuition note.* Instead of asking "what is the whole best curve?", ask "standing here, with this much left, which way do I go?" Both answers describe the same extremal.

### §3 $\max_y\int_0^\infty F(x,y)\,dt$ (pp. 248–251)
Motivating discrete process (Ch. 1): $f(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f(ay+b(x-y))]$, $f(0)=0$ (1). Its continuous version maximizes $\int_0^\infty[g(y)+h(x-y)]dt$ with $dx/dt=-ay-b(x-y)$, $a,b>0$, $x(0)=c$, $0\le y\le x$ (2, 3) (p. 249).

General problem (constraint (3b) omitted at first): maximize $J(y)=\int_0^\infty F(x,y)dt$ (4) subject to $dx/dt=G(x,y)$, $x(0)=c$ (5). We assume maxima exist and extremals are differentiable enough (p. 249).

The maximum depends only on $c$:
$$\max_y J(y)=f(c). \tag{6}$$
For the maximizing $y$ and any $S>0$: $f(c)=\int_0^SF\,dt+\int_S^\infty F\,dt$ (7). Over $[S,\infty)$ the problem has the same form with initial value $c(S)=x(S)$, because integrand and differential equation do not depend on $t$ (pp. 249–250). By the principle of optimality
$$f(c)=\int_0^SF(x,y)\,dt+f(c(S)),\tag{8}$$
and since $y$ is chosen to achieve the maximum,
$$f(c)=\max_{y[0,S]}\Big[\int_0^SF(x,y)\,dt+f(c(S))\Big]\quad\text{for any }S>0.\tag{9}$$
For small $S$, under continuity assumptions,
$$f(c)=\max_{y[0,S]}[F(c,y(0))S+f(c+SG(c,y(0))+o(S))].\tag{10}$$
With $v=y(0)$ and a first-order expansion of $f$:
$$f(c)=\max_v[F(c,v)S+f(c)+SG(c,v)f'(c)]+o(S),\tag{11}$$
and letting $S\to0$ (cancel $f(c)$, divide by $S$):
$$0=\max_v[F(c,v)+G(c,v)f'(c)].\tag{12}$$
Calculus on the maximum gives two equations
$$0=F(c,v)+G(c,v)f'(c),\qquad 0=F_v(c,v)+G_v(c,v)f'(c).\tag{13}$$
Eliminating $f'(c)$:
$$\begin{vmatrix}F(c,v)&G(c,v)\\F_v(c,v)&G_v(c,v)\end{vmatrix}=0,\tag{14}$$
which determines $v$ as a function of $c$ (p. 250). Then solve
$$dx/dt=G[x,y(x)],\quad x(0)=c\tag{15}$$
for $x(t)$ and then $y(t)$ (p. 251). A relatively simple policy $y=\varphi(x)$ may give a relatively complicated extremal $x(t)$ (p. 251).

*Intuition note.* The optimal value from the current state must equal the best short-term gain plus the optimal value from where you land. Letting the step shrink turns this into one equation in the state alone, from which the best action follows.

### §4 Discussion (p. 251)
Take $G=-A(x,y)$ with $A>0$ (uniformly negative $G$): $F$ is a rate of return, $A$ the rate of resource expenditure. From $0=\max_v[F(c,v)-A(c,v)f'(c)]$ (1): for all $v$, $0\ge F-Af'$ (2), so $f'(c)\ge F(c,v)/A(c,v)$ (3), with equality for at least one $v$:
$$f'(c)=\max_v\frac{F(c,v)}{A(c,v)}.\tag{4}$$
The overall-optimal policy locally maximizes the ratio of return rate to expenditure rate, a policy met earlier (Ch. 1 Exer. 18; Ch. 2 §8). This is an interpretation of the Euler equation. The author leaves to the reader to verify that (14) of §3 is a first integral of the classical Euler equation (p. 251).

### §5 Two-dimensional case (pp. 251–252)
Left as an exercise: for $\max\int_0^\infty F(x_1,x_2,y_1,y_2)dt$ with $dx_1/dt=G$, $dx_2/dt=H$, the same technique yields a $3\times3$ determinantal equation
$$\begin{vmatrix}F&G&H\\F_u&G_u&H_u\\F_v&G_v&H_v\end{vmatrix}=0\tag{3}$$
(entries evaluated at $(c_1,c_2,u,v)$), connecting $y_1(0)=u(c_1,c_2)$, $y_2(0)=v(c_1,c_2)$. It is an open problem whether the solution can be written as $y_1=\varphi_1(x_1,x_2)$, $y_2=\varphi_2(x_1,x_2)$ as in the one-dimensional case (p. 252).

### §6 $\max_y\int_0^TF(x,y)\,dt$ (pp. 252–253)
Now the state is $(c,T)$: $c$ = initial resources, $T$ = duration. Let $\max_yJ(y)=f(c,T)$ (3). As in §3:
$$f(c,T)=\max_{y[0,S]}\Big[\int_0^SF\,dt+f(c(S),T-S)\Big],\tag{4}$$
leading as $S\to0$ to the nonlinear PDE
$$0=\max_v[F(c,v)+G(c,v)f_c-f_T],\tag{5}$$
i.e.
$$f_T=F(c,v)+G(c,v)f_c,\qquad 0=F_v(c,v)+G_v(c,v)f_c.\tag{6}$$
Solving for the derivatives:
$$f_c=-F_v/G_v\equiv P(c,v),\qquad f_T=F-GF_v/G_v\equiv Q(c,v).\tag{7}$$
Equating $f_{cT}=P_vv_T$ with $f_{Tc}=Q_vv_c+Q_c$:
$$P_v\,v_T=Q_v\,v_c+Q_c.\tag{8}$$
This is a first-order linear PDE for $v(c,T)$, solvable by characteristics (the author refers forward to §14) or numerically given $v(0,T)$ or $v(c,0)$ (p. 253). The $T$-dependent formulation helps: for small $T$, $f(c,T)=\max_v[F(c,v)T+o(T)]$ (9), so $v(c,0)$ is the maximizer of $F(c,v)$ (p. 253).

*Intuition note.* With one more variable (time left) we gain a known starting line, $T=0$. The equation for the policy $v$ can then be marched forward in $T$ from that line.

### §7 Constraint $0\le y\le x$ (pp. 253–254)
Problem: maximize $\int_0^TF\,dt$, $dx/dt=G(x,y)$, $x(0)=c$, $0\le y\le x$ (1). Classical difficulty: $y$ cannot generally be found by unrestricted variation. Where $0<y<x$, $y$ satisfies the Euler equation. Where $y=0$ or $y=x$ one has only an Euler *inequality*. The task is to fit together the three solution types and find the transition points. No uniform technique exists for explicit analytic solutions (p. 253).

Functional-equation form with $f(c,T)=\max_yJ(y)$:
$$f_T=\max_{0\le v\le c}[F(c,v)+G(c,v)f_c],\qquad f(c,0)=0\ \text{for all }c.\tag{3, 4}$$
The constraint prevents free differentiation in $v$; §10 uses (3) to derive solution structure under assumptions on $F,G$ (p. 254).

### §8 Computational solution (pp. 254–255)
For $f_T=\max_v[F+Gf_c]$, $f(c,0)=0$, use grids $T=0,\Delta,2\Delta,\dots$ and $c=0,\pm\delta,\pm2\delta,\dots$ with
$$f_T\approx\frac{f(c,T+\Delta)-f(c,T)}{\Delta},\qquad f_c\approx\frac{f(c+\delta,T)-f(c-\delta,T)}{2\delta}.\tag{3}$$
Then
$$f(c,T+\Delta)=f(c,T)+\Delta\max_v\Big[F(c,v)+G(c,v)\frac{f(c+\delta,T)-f(c-\delta,T)}{2\delta}\Big],\quad f(c,0)=0,\tag{4}$$
and one computes $f(c,\Delta),f(c,2\Delta),\dots$ successively (p. 255).

Difficulty: choosing $\Delta,\delta$, on which convergence and stability depend. For the linear equations obtained when the max is removed, there is a fairly complete theory. For nonlinear equations "practically no theory exists" and the matter rests on "art and experience" (p. 255). The constrained equation (7.3) is easier numerically than the unconstrained one, since the constraint narrows the range searched for the maximum. So a more realistic process may have a simpler computational solution. §11 gives an alternative scheme (p. 255).

### §9 Discussion: structure of solutions (pp. 255–256)
Assume $F(c,v)$ strictly concave in $v$ for all $c$ and $G=g(c)+h(c)v$ linear in $v$:
$$f_T=\max_{0\le v\le c}[F(c,v)+(g(c)+h(c)v)f_c].\tag{1}$$
The bracket is strictly concave in $v$, so the maximizer is unique; it may be $0$, $c$ or interior (p. 256). Assuming all functions vary continuously with $c,T$, the maximum cannot move from $v=0$ to $v=c$ without passing through interior points. Consequently an interval with $y=0$ must be preceded and followed by an interval with $0<y<x$, and likewise for $y=x$. This continuity can shorten computation greatly and makes multi-dimensional numerical solution feasible (p. 256). How many switches occur needs further assumptions; examples with arbitrarily many transitions can be built by suitable choice of $F$ (p. 256).

### §10 An example (pp. 256–258)
Maximize $J=\int_0^T(x-y)dt$ with $dx/dt=b(y)$, $x(0)=c$, $0\le y\le x$. Equation: $f_T=\max_{0\le v\le c}[c-v+b(v)f_c]$ (3). Assume
$$b(0)=0,\ b'(0)=\infty;\quad b'(y)>0,\ b'(y)\to0\ (y\to\infty);\quad b''(y)<0\tag{4}$$
(e.g. $b=y^{1/2}$) (pp. 256–257). Assume (called plausible) $f_c>0$, and $f_c=0$ at $T=0$ and increasing in $T$. For $K(v)=c-v+b(v)f_c$, $K'(v)=-1+b'(v)f_c$ is positive for small $v$, negative for large $v$ and zero at exactly one $v$. Unconstrained, a root always exists. With $v\le c$: if $f_c$ is large (i.e. $T$ large), $K'>0$ on $[0,c]$, so the max is at $v=c$, i.e. $y=x$, for $T$ large compared with $c$ (p. 257).

Solution form:
$$y=x\ \ (0\le t\le t_1),\qquad 0<y<x\ \ (t_1<t<T).\tag{5}$$
The first part occurs only for $T$ sufficiently large; for small $T$ only the second (p. 257).

*Small $T$, two routes.* (i) The max is interior, so (3) is equivalent to
$$f_T=c-v+b(v)f_c,\qquad 0=-1+b'(v)f_c,\tag{6}$$
with $f(c,0)=0$, $v(c,0)=0$ (7), enough to determine $f(c,T)$. (ii) Ignore the constraint and use the classical method: with $x(t)=c+\int_0^tb(y)ds$,
$$J(y)=\int_0^T\Big[c+\int_0^tb(y)\,ds-y\Big]dt,\tag{8}$$
the Euler equation is
$$(T-t)\,b'(y)-1=0,\tag{9}$$
which determines $y$ uniquely and so $J$ and $f(c,T)$ (p. 257).

Critical $T$: the cross-over occurs when $-1+b'(v)f_c=0$ (10) has the solution $v=c$, i.e. when
$$f_c(c,T)=\frac1{b'(c)}.\tag{11}$$
If $f_c$ is monotone increasing in $T$ (as surmised), this has one root $T(c)$, which fixes the solution completely (p. 258).

*Intuition note.* Spending $y$ now costs $y$ immediately but yields growth $b(y)$ later. With little time left, the interior optimum is below the cap $c$. With much time left, the unconstrained optimum would exceed what is available, so you spend everything allowed until the horizon is near enough.

### §11 A discrete version (pp. 258–260)
To make the above rigorous, use a discrete approximation. For §10: maximize $J=\sum_{k=0}^N(x_k-y_k)$ (1), with $x_{k+1}=x_k+b(y_k)$, $0\le y_k\le x_k$ (2). With $u_N(c)=\max J$:
$$u_0(c)=c,\qquad u_{N+1}(c)=\max_{0\le v\le c}[c-v+u_N(c+b(v))].\tag{4}$$

**Theorem 1.** For each $N\ge1$ there is a function $v_N(c)$ such that (as printed, p. 259):
(a) $v_N(c)$ is monotone decreasing as $c$ increases; (b) $v_{N+1}(c)>v_N(c)$; (c) there is a unique solution of $v_N(c)=c$, called $c_N$, with $c_{N+1}>c_N$; (d) for $0\le c\le c_N$, $u_N(c)=u_{N-1}(c+b(c))$, i.e. $v=c$; (e) for $c_N\le c$, $u_N(c)=c-v_N(c)+u_{N-1}[c+b(v_N(c))]$; (f) $u_N'(c)\ge u'_{N-1}(c)$, $c\ge0$.
The proof is inductive "along the usual lines" and left to the reader. A similar result holds for the general problem of §7 under suitable conditions on $F,G$; the proof is "much more detailed" (p. 259). (See Reading notes on (a), (c).)

General problem (§§7–8): maximize $\int_0^TF\,dt$ with $dx/dt=G$, $x(0)=c$, $0\le y\le x$ reduces to $f_T=\max_{0\le v\le c}[F+Gf_c]$, $f(c,0)=0$ (7), which can be solved by partial differences. To use that with confidence one must show (i) the variational problem is equivalent to the PDE, difficult with constraints, and (ii) the difference method approximates its solution. Both are avoided by replacing the problem by: maximize
$$J(\{y_k\})=\Delta\sum_{k=0}^NF(x_k,y_k),\tag{8}$$
$$x_{k+1}=x_k+\Delta G(x_k,y_k),\ x_0=c;\quad 0\le y_k\le x_k;\quad N\Delta=T.\tag{9}$$
With $f_N(c)=\max J$ (10):
$$f_0(c)=0,\qquad f_{N+1}(c)=\max_{0\le v\le c}[\Delta F(c,v)+f_N(c+\Delta G(c,v))].\tag{11}$$
In cases treated to date this has been a more reliable computational procedure. It is "not too difficult" to show
$$\lim_{\Delta\to0}f_N(c)=f(c,T)\tag{12}$$
under conditions normally assumed in the calculus of variations (which can be greatly lightened; not discussed) (p. 260).

*Intuition note.* Instead of discretizing the PDE and hoping it converges, discretize the original decision problem. The recursion is then exactly the optimum of a finite problem, so one need not first prove that the PDE is equivalent to the variational problem or that its difference scheme approximates it. That the recursion converges to the continuous optimum still has to be shown (§12 does so for a typical case).

### §12 A convergence proof (pp. 260–263)
Typical result. Problem: $f(c,T)=\max_y\int_0^TF(x,y)dt$, $dx/dt=G(x,y)$, $x(0)=c$, $0\le y\le x$. Substitute $y=\varphi x$ (new $F,G$): maximize $\int_0^TF(x,\varphi)dt$ with
$$dx/dt=G(x,\varphi),\ x(0)=c,\quad 0\le\varphi\le1.\tag{4}$$
This fixes the maximization region (footnote 6, p. 260).

Approximating problems, $n=1,2,\dots$: maximize
$$J_N(\{\varphi_k\},n)=\sum_{k=0}^NF(x_k,\varphi_k)/n,\quad N=[T/n]\ \text{(as printed)},\tag{5}$$
with $x_{k+1}-x_k=G(x_k,\varphi_k)/n$, $x_0=c$ (6) and $0\le\varphi_k\le1$ (7). Let $f(c,T,n)=\max J_N$ (8). Goal: $\lim_{n\to\infty}f(c,T,n)=f(c,T)$ (9) (p. 261).

**Lemma.** Let $G(x,\varphi)$ satisfy a Lipschitz condition (changes at most in proportion to changes in its arguments) for $m\le x\le M$, $0\le\varphi\le1$. Let $\varphi(t)$ be a step function (constant pieces) with value $\varphi_k$ on $k/n\le t<(k+1)/n$; $\{x_k\}$ be given by (6) with uniform bounds $m\le x_k\le M$; $\bar x(t)$ be the step function with value $x_k$ on the same intervals; $x(t)$ solve the differential equation in (4). Then there is a constant $\kappa$, depending only on $G$ and $T$, with $|x(t)-\bar x(t)|\le\kappa/n$ (p. 261). Proof: the Cauchy–Lipschitz method, as in the existence theorem for ordinary differential equations (p. 261).

**Theorem 2.** Assume (a) $F$ and $G$ have continuous second partial derivatives; (b) constants $p,q,r$ exist with $px\le G(x,y)\le qx+r$ for $x>0$, $0\le y\le x$; (c) $G_y$ has one sign ($G_y>0$ or $G_y<0$) for all $x>0$, $0\le y\le x$. Then $\lim_{n\to\infty}f(c,T,n)=f(c,T)$ for all $c\ge0$, $T>0$ (p. 262).

Proof steps (pp. 262–263):
1. (11b) bounds $x(t)$ on $[0,T]$: $m\le x(t)\le M$, hence $m\le x_k\le M$. $F,G$ are Lipschitz in this region, so the Lemma gives a constant $B'$ (depending on $c,T,F,G$) with
$$|J(\varphi)-J_N(\{\varphi_k\},n)|\le B'/n\tag{13}$$
for $\varphi(t),\varphi_k$ as in the Lemma.
2. Hence $f(c,T,n)\le f(c,T)+B'/n$ for all $n$ (14).
3. Take a subsequence $\{n_i\}$ with $\lim f(c,T,n_i)=\liminf_nf(c,T,n)$. For $\varepsilon>0$ choose $\varphi$ with $f(c,T)<J(\varphi)+\varepsilon$ (15).
4. $\varphi$ is the a.e. limit of step functions $\varphi_m$ with $0\le\varphi_m\le1$ and $J(\varphi_m)\to J(\varphi)$. So $\varphi$ may be taken as a step function constant on intervals $k/n\le t<(k+1)/n$ for arbitrarily large $n=n_i$.
5. From (13): $f(c,T)<J_N(\{\varphi_k\},n)+B'/n+\varepsilon\le f(c,T,n)+B'/n+\varepsilon$ (16).
6. Hence $f(c,T)\le\lim f(c,T,n_i)+\varepsilon=\liminf f(c,T,n)+\varepsilon$ (17).
7. From (14): $\limsup f(c,T,n)\le f(c,T)$ (18).
8. As $\varepsilon$ is arbitrary, (12) holds.

Policy convergence: if $\{\varphi_{kn}\}$ maximizes $J_N$, it defines step functions $\varphi_n(t)$ with $\lim J(\varphi_n)=f(c,T)$ (19). If a subsequence converges a.e. to $\varphi(t)$, then $\lim J(\varphi_n)=J(\varphi)$ and $\varphi$ is a maximizing function. With suitable monotonicity, Helly's theorem gives a convergent subsequence; otherwise weak-convergence arguments are needed (p. 263).

*Intuition note.* Step policies approximate any policy arbitrarily well and cost only $O(1/n)$ in value. So the best value of the discrete problems cannot stay far below, or above, the best value of the continuous one.

### §13 Time-dependent case (pp. 263–264)
Maximize $\int_0^TF(x,y,t)dt$, $dx/dt=G(x,y,t)$, $x(0)=c$. Embed it in the family $J=\int_a^TF\,dt$, $x(a)=c$, $a\in[0,T]$, with $T$ fixed and state $(a,c)$: $\max J=f(a,c)$ (5). Then
$$f(a,c)=\max_{y[a,a+S]}\Big[\int_a^{a+S}F\,dt+f(a+S,c(S))\Big],\quad 0<S<T-a.\tag{6}$$
As $S\to0$:
$$0=\max_v[F(c,v,a)+f_a+G(c,v,a)f_c],\tag{7}$$
giving $0=F+f_a+Gf_c$ and $0=F_v+G_vf_c$ (8), hence
$$f_c=-F_v/G_v=P(c,v,a),\qquad f_a=(FG_v-F_vG)/G_v=Q(c,v,a).\tag{9}$$
Equating $f_{ca}=f_{ac}$:
$$P_vv_a+P_a=Q_vv_c+Q_c.\tag{10}$$
The author says those familiar with quasi-linear PDEs will "readily verify" that its characteristics are equivalent to the classical Euler equations (not proved here) (p. 264).

### §14 Generalization (pp. 264–265)
For vectors $x,y,c,g\in\mathbb R^n$ and scalar $F(x,y)$: maximize $\int_0^TF(x(t),y(t))dt$ with $dx/dt=g(x,y)$, $x(0)=c$. Time dependence can be removed by adding $x_{n+1}$ with $dx_{n+1}/dt=1$, $x_{n+1}(0)=0$ (footnote 7). With $f(c,T)=\max J$,
$$f(c,S+T)=\max_{y[0,S]}\Big[\int_0^SF\,dt+f(c(S),T)\Big].\tag{4}$$
The classical transversality conditions fall out as a special case, as expected from the point/tangent duality. The calculations analogous to (8),(9) give a system of quasi-linear PDEs for $v(c,T)=y(0)$. Its characteristics are equivalent to the Euler equations; the rigorous proof is "quite complicated" and omitted (p. 265).

### §15 Integral constraints (p. 265)
Add $\int_0^Ty\,dt\le m$ to the problem of §7. The optimum is a function $f(c,T,m)$ of three state variables, and
$$f_T=\max_{0\le v\le c}[F(c,v)+G(c,v)f_c-vf_m].\tag{2}$$
Such constraints model realistic bounds on velocity, acceleration, curvature, resource allocation rate; integral constraints (e.g. $\int_0^Ty'^2dt\le m$, bounded resources or kinetic energy) are generally more readily handled than point constraints. The Lagrange multiplier method can in theory treat both, but in practice one must decide whether the variable is interior or on the boundary (p. 265).

### §16 Remarks on numerical solution (pp. 266–267)
Maximize $J(x)=\int_0^TF(x,x',t)dt$, $x(0)=c$, otherwise free. The Euler equation $\partial F/\partial x-\frac d{dt}\partial F/\partial x'=0$ (2) is second order, $x''=G(x,x',t)$ (3), and needs two boundary conditions: $x(0)=c$ and, from the variation, $\partial F/\partial x'|_{t=T}=0$ (4). One condition is at $t=0$, the other at $t=T$, but numerical integration needs both $x,x'$ at one end: the classical two-point boundary difficulty. If $G$ is linear in $x,x'$ it is manageable; for nonlinear $G$ there is no systematic technique. The usual procedure integrates from $t=0$ over a range of $x'(0)$ and narrows the range until (4) holds. It is slow, may have stability problems, and becomes rapidly less efficient as dimension grows. Non-smooth $F$ (e.g. $|x-a|$, $\max(x-a,x'-b,g(t))$) or constraints make the usual approach harder still. Sensitivity and stability remarks from Ch. 7 apply equally to continuous decision processes (pp. 266–267).

### §17 Eigenvalue problem (pp. 267–268)
The values of $\lambda$ for which $u''+\lambda^2\varphi(t)u=0$, $u(0)=u(1)=0$ has a non-trivial solution are tied to a variational problem. Under light conditions on $\varphi$ the eigenvalue problem is equivalent to finding relative minima of $\int_0^1u'^2dt$ subject to $\int_0^1\varphi u^2dt=1$, $u(0)=u(1)=0$ (2), or relative maxima of $\int_0^1\varphi u^2dt$ subject to $\int_0^1u'^2dt=1$, $u(0)=u(1)=0$ (3) (p. 267).

Difficulty: along an extremal the condition $u(0)=0$ is violated (the remaining problem starts from $u\neq0$). So embed in a larger class, in two ways (p. 267):

*First formulation.* Minimize $J(u)=\int_a^1u'^2dt$ subject to $u(a)=k$, $u(1)=0$, $\int_a^1\varphi u^2dt=1$ (4, 5), with state variable $0\le a<1$ and $0<b_1\le\varphi\le b_2$, $\varphi$ continuous on $[0,1]$. Equivalent: maximize $K(u)=\int_a^1\varphi u^2dt$ with $\int_a^1u'^2dt=1$ and the same end conditions (6, 7) (p. 268).

*Second formulation.* Minimize $\int_a^1u'^2dt$ subject to $u(a)=0$, $u(1)=0$ and
$$\int_a^1[\varphi(t)u^2+k(1-t)\varphi(t)u]\,dt=1\tag{9}$$
(p. 268).

### §18 First formulation: the PDE (pp. 268–269)
Let $f(a,k)=\min\int_a^1u'^2dt$ subject to $u(a)=k$, $u(1)=0$, $\int_a^1\varphi u^2dt=1$. Along an extremal, to $o(s)$:
$$\int_{a+s}^1\varphi u^2dt=1-s\varphi(a)k^2,\quad u(a+s)=k+sv,\quad f(a,k)=v^2s+\int_{a+s}^1u'^2dt.\tag{3}$$
To keep the normalization, set $u(t)=[1-s\varphi(a)k^2/2]\,w(t)$, $a+s\le t\le1$ (4). Then
$$w(a+s)=k+sv+s\varphi(a)k^3/2,\qquad f(a,k)=v^2s+(1-s\varphi(a)k^2)\int_{a+s}^1w'^2dt.\tag{5}$$
So
$$f(a,k)=\min_v\big[v^2s+(1-s\varphi(a)k^2)f(a+s,\,k+sv+s\varphi(a)k^3/2)\big]+o(s).\tag{6}$$
Letting $s\to0$:
$$0=\min_v[v^2+vf_k]+f_a+\frac{\varphi(a)k^3}{2}f_k-\varphi(a)k^2f,\tag{7}$$
$$\text{or}\quad f_a=\frac{f_k^2}4-\frac{\varphi(a)k^3f_k}2+\varphi(a)k^2f.\tag{8}$$
(Added step: the minimum over $v$ of $v^2+vf_k$ is $-f_k^2/4$, at $v=-f_k/2$, which turns (7) into (8).) The initial condition is at $a=1$ and is non-trivial, because $f(a,k)\to\infty$ as $a\to1$. Two ways to find it follow in §19 (p. 269).

### §19 An approximate solution (pp. 269–270)
For $a$ near 1 and $\varphi$ continuous, replace the problem by: minimize $\int_a^1u'^2dt$ with $u(a)=k$, $u(1)=0$, $\int_a^1u^2dt=1$ (absorbing the factor $\varphi(1)$ into $u$). Method 1 (classical): Euler equation $u''+\lambda u=0$ solved explicitly, with $\lambda$ fixed by the constraints. Method 2: use the PDE (8) of §18 (printed "(17.8)") with $\varphi\equiv1$. For $k=0$ the solution is known:
$$f(a,0)=\frac{\pi^2}{(a-1)^2},\tag{3}$$
so that PDE can be solved as a power series in $k$ ($k\ge0$), useful for small $k$ (p. 270).

### §20 Second formulation (p. 270)
The PDE for the problem (16.8)–(16.9) is left as an exercise. Hint: renormalize $u(t)$ constantly so as to maintain $u(a)=0$ (p. 270).

### §21 Discrete approximations (pp. 270–271)
Because the PDE for $f(a,k)$ has "unpleasant features" for initial values, use a discrete version: minimize
$$F(u_1,\dots,u_{N-1})=\sum_{k=1}^N(u_k-u_{k-1})^2\tag{1}$$
subject to $\sum_{k=1}^{N-1}\varphi_ku_k^2=1$, $u_0=a$, $u_N=0$ (2) (here $a$ is the boundary value). State variable $R$: define
$$f_R(a)=\min\sum_{k=R}^N(u_k-u_{k-1})^2\ \text{ with }\ \sum_{k=R}^N\varphi_ku_k^2=1,\ u_{R-1}=a,\ u_N=0,\quad R=1,\dots,N-1.\tag{3, 4}$$
Since the range of each $u_k$ varies, change variables $\varphi_ku_k=v_k$ (5), assuming $0<b_1\le\varphi_k\le b_2<\infty$:
$$f_R(a)=\min\sum_{k=R}^N\Big(\frac{v_k}{\varphi_k}-\frac{v_{k-1}}{\varphi_{k-1}}\Big)^2,\tag{6}$$
$$\sum_{k=R}^Nv_k^2=1,\quad v_{R-1}=\varphi_{R-1}a,\ v_N=0.\tag{7}$$
The recurrence for $\{f_R(a)\}$ is left as an exercise (p. 271). The bibliography says this last formulation "seems the most promising" for computation (p. 282).

### §22 Successive approximation (pp. 271–272)
Iterating $f_1(c)=\max_{y[0,S]}[\int_0^SF\,dt+f_0(c(S))]$ from a continuous $f_0$ gives $f_1=f_0$ in the limit $S\to0$ (2), so naive iteration in function space fails. What works is approximation in *policy space*: concentrate on $v(c,T)$, with $f$ in an auxiliary role (p. 271).

Procedure for $f_T=\max_v[F(c,v)+G(c,v)f_c]$ (5):
1. Choose $v_0(c,T)$, equivalently $y_0(x,T-t)$ ($T-t$ = remaining time).
2. Compute $x_0$ from $dx_0/dt=G(x_0,y_0(x_0,T-t))$, $x_0(0)=c$ (6), then $f_0(c,T)=\int_0^TF(x_0,y_0)dt$ (7). It satisfies the *linear* PDE $f_{0T}=F(c,v_0)+G(c,v_0)f_{0c}$ (8).
3. Choose $v_1(c,T)$ to maximize $F(c,v)+G(c,v)f_{0c}$ (9); get $y_1,x_1,f_1$ as above.
4. Choose $v_2$ to maximize $F(c,v)+G(c,v)f_{1c}$ (10); continue, giving sequences $\{f_n\}$, $\{v_n\}$ (p. 272).

### §23 Monotone approximation (p. 272)
$f_{1T}=F(c,v_1)+G(c,v_1)f_{1c}$ and $f_{0T}=F(c,v_0)+G(c,v_0)f_{0c}\le F(c,v_1)+G(c,v_1)f_{0c}$ (1), because $v_1$ maximizes (9). Hence
$$(f_1-f_0)_T\ge G(c,v_1)(f_1-f_0)_c.\tag{2}$$
Since $f_1(c,0)=f_0(c,0)=0$, $f_1-f_0\ge0$ for $T\ge0$. Continuing, $\{f_n\}$ is monotone increasing. If uniformly bounded it converges, but convergence of $f_{nc}$, $f_{nT}$ and of the policies $v_n$ is a difficult question, not treated. The method is a systematic technique for improving any policy (p. 272).

*Intuition note.* Pick a policy, compute its value, then re-optimize the action at each state against that value. The result is never worse than before. The same step can be repeated.

### §24 Uniqueness (p. 273)
Suppose $f$ and another solution $g$ of $f_T=\max_v[F+Gf_c]$ have $f(c,0)=g(c,0)=0$. Let $v$ attain the max for $f$ and $w$ for $g$. Then
$$f_T=F(c,v)+G(c,v)f_c\ge F(c,w)+G(c,w)f_c,\quad g_T=F(c,w)+G(c,w)g_c\ge F(c,v)+G(c,v)g_c.\tag{4}$$
(Added step: subtract the lower bound in each line to get $G(c,w)(f_c-g_c)\le f_T-g_T\le G(c,v)(f_c-g_c)$; the printed (5) writes this as one chain with mixed inequality signs.) With $u=f-g$:
$$G(c,w)u_c\le u_T\le G(c,v)u_c.\tag{6}$$
The solutions of $x_T-G(c,w)x_c=0$ and $y_T-G(c,v)y_c=0$ with zero initial data are identically zero. By a comparison theorem, $u\equiv0$. The device is that of Lemma 1, Ch. 3 (p. 273).

### §25 Minimum maximum deviation (p. 274)
Minimize $\max_{0\le t\le T}|u-a|$ over $v(t)$ with $-1\le v\le1$, $du/dt=g(u,v)$, $u(0)=c_1$. Discrete version: $u_{k+1}=u_k+g(u_k,v_k)\Delta$, $u_0=c_1$, $\Delta=T/N$. With $f_N(c_1)=\min_{\{v_k\}}\max_{0\le k\le N}|u_k-a|$:
$$f_0(c_1)=|c_1-a|,\qquad f_{N+1}(c_1)=\max\Big[|c_1-a|,\ \min_{|v|\le1}f_N(c_1+g(c_1,v)\Delta)\Big].$$
The problem becomes a sequence of one-variable functions (p. 274).

### Exercises and bibliography (pp. 274–282)
41 exercises/research problems follow (functional equations for various integrals, quadratic problems, rocket flight, stochastic cases, eigenvalue approximations). The bibliography notes the method was announced in a 1953 paper (§1), that the proof of §12 is due to W. Fleming, and that an equivalence proof for §14 is due to H. Osborn (p. 282).

## Toy example (ours, not from the text)
Maximize $J=\int_0^\infty-(x^2+y^2)\,dt$ with $dx/dt=y$, $x(0)=c$. So $F=-(x^2+y^2)$, $G=y$ (formula (12) of §3).

1. Condition (14): $F\,G_v-G\,F_v=0$. With $F=-c^2-v^2$, $G_v=1$, $G=v$, $F_v=-2v$: $(-c^2-v^2)(1)-(v)(-2v)=v^2-c^2=0$, so $v=\pm c$.
2. Use (13): $f'(c)=-F/G=(c^2+v^2)/v$. For $v=c$: $f'=2c$. For $v=-c$: $f'=2c^2/(-c)=-2c$.
3. The second derivative $\partial^2/\partial v^2[F+Gf']=-2<0$ holds for either root, so it does not choose between them. We pick $v=-c$ because it gives a decaying trajectory and a value $f\le0$ (as $F\le0$); $v=c$ would give $f=c^2>0$ and a growing $x$. With $v=-c$ the policy $y=-x$ gives $dx/dt=-x$, $x=ce^{-t}$.
4. Check: $f(c)=-c^2$ (from $f'=-2c$, $f(0)=0$). Direct value: $\int_0^\infty-(c^2e^{-2t}+c^2e^{-2t})dt=-2c^2\cdot\tfrac12=-c^2$. ✓
5. Check (12): $\max_v[-c^2-v^2+v(-2c)]$ is at $v=-c$, value $-c^2-c^2+2c^2=0$. ✓

Lesson (cf. p. 251): the *policy* $y=-x$ is simple (linear in the state); the *extremal* $x(t)=ce^{-t}$ is an exponential found afterwards from (15).

## Concepts
- [[principle-of-optimality]] — whatever the first decisions, the remaining path must be optimal for the state reached; applied to extremals as continuous policies (p. 247)
- [[bellman-equation-value-function]] — $f(c)$ (or $f(c,T)$) = optimal value as a function of state; satisfies (9)/(4) of §3/§6 (p. 249)
- [[hamilton-jacobi-bellman-equation]] — the limiting PDE $0=\max_v[F+Gf_c-f_T]$ (name not used in this unit; same equation) (p. 252)
- [[policy]] — a rule giving the action $v$ (or $dy/dx$) from the current state; here "continuous policy" (p. 246)
- [[state]] — variables on which the optimal value depends: $c$; $(c,T)$; $(a,c)$; $(c,T,m)$; $(a,k)$ (pp. 249, 252, 263, 265, 268)
- [[imbedding-invariant]] (new) — embed a problem in a family indexed by extra state variables (e.g. $T$, $a$, $k$) so that its tail belongs to the family (pp. 252, 263, 267)
- [[approximation-in-policy-space]] (new) — iterate on the policy $v$ instead of on $f$; gives monotone $f_n$ (pp. 271–272)
- [[intrinsic-equation-tangential-description]] (new) — the extremal described by slope as a function of state, "envelope of tangents" (p. 248)
- [[two-point-boundary-value-problem]] (new) — Euler equation with conditions at $t=0$ and $t=T$; no systematic nonlinear solution (p. 266)
- [[euler-equation-calculus-of-variations]] (new) — classical necessary condition; here compared with the determinantal equation (p. 251)
- [[method-of-characteristics]] (new) — solves first-order PDEs for $v$; characteristics correspond to Euler equations (author's claim, pp. 253, 264)
- [[minimal-intervention-principle]] — not stated in this unit; no link made.

## Canonical instances
- [[brachistochrone]] — least-time curve as a policy for $dy/dx$ given velocity (p. 247)
- [[isoperimetric-problem]] — max area with length budget $L-L'$ as state (p. 247)
- [[continuous-allocation-process]] — $F/A$ ratio rule from $f'=\max F/A$ (p. 251)
- [[resource-spend-example-x-minus-y]] — $\int(x-y)dt$, $dx/dt=b(y)$; switch from $y=x$ to interior (pp. 256–258)
- [[sturm-liouville-eigenvalue-as-variational-problem]] — $u''+\lambda^2\varphi u=0$ via $f(a,k)$ (pp. 267–270)
- [[minimax-deviation-recursion]] — $\min\max|u-a|$ recursion (p. 274)

## Bridges (candidates)
- [same-math] §6 equation $0=\max_v[F+Gf_c-f_T]$ ↔ control-theory: Hamilton–Jacobi–Bellman equation for finite-horizon optimal control — same PDE (canon link; name not used in this unit)
- [structural-analogy] Policy $v(c,T)$ as feedback on state ↔ control-theory: state feedback $u=-Kx$ — action as function of the current state (the toy example gives $y=-x$)
- [structural-analogy] §22–23 policy iteration with monotone $f_n$ ↔ reinforcement learning: policy improvement — evaluate a policy, then improve greedily
- [structural-analogy] Characteristics of the $v$-PDE equal the Euler equations ↔ control-theory: Pontryagin's necessary conditions (not stated in this unit)
- [metaphor] Curve as envelope of tangents ↔ economics: marginal rule "maximize return per unit resource spent"

## Questions this raises
- When the maximum is only attained at the constraint boundary, how can the policy $v(c,T)$ be non-smooth and the PDE still hold? (Only formal arguments are given.)
- What conditions make the policies $v_n$ of §22 converge, not only $f_n$? (Left open, p. 272.)
- Can the two-dimensional case (§5) always be written as $y_i=\varphi_i(x_1,x_2)$? (Stated as open, p. 252.)
- How does the discrete recursion's cost grow with the state dimension, given the "multi-dimensional" claims of §9?

## Exercises worth doing
- Ex. 1 (p. 274) — write the functional equation for $\max\int f^2dt$ with $\int f'^2dt=1$; practice choosing state variables — difficulty: medium
- Ex. 3 (p. 275) — first terms of the power series of $f(a,k)$ in $k$ from (18.8), $a$ near 1 — difficulty: hard
- Ex. 13–15 (p. 276) — quadratic cost with $x'$: $f_s=\dots$, show $f=u(s)+cv(s)+c^2w(s)$ and derive the ODEs — difficulty: medium
- Ex. 29 (p. 278) — solve brachistochrone and isoperimetric problems by the functional-equation approach — difficulty: medium
- Ex. 34 (p. 280) — discrete recursion for a rocket-aircraft maximum range — difficulty: medium
- Ex. 40 (p. 281) — monotone decreasing approximation of the first eigenvalue in policy space — difficulty: hard

## Reading notes
- Printed page = pdf − 23 (pdf 268 = p. 245). Running header "A NEW FORMALISM".
- Edition facts are not visible on these pages beyond the chapter title.
- The text layer is heavily garbled in equations. I checked all equations against the page images.
- Possible misprints, reported as printed:
  - (11.5) the text layer reads $u_N$ in (a); the page image shows $v_N$, which I follow. As printed, (a) "$v_N$ decreasing in $c$" and (c) "unique solution of $v_N(c)=c$" look hard to reconcile with (d) "$v=c$ for all $0\le c\le c_N$".
  - (11.11) $f_0=0$ with recursion adding one term per step, versus the sum from $k=0$ to $N$ in (8).
  - (12.5) $N=[T/n]$ although the step is $1/n$ (probably $[nT]$ is meant); (12.6) runs $k=0,\dots,n-1$.
  - (21.5)–(21.7) $\varphi_ku_k=v_k$ is inconsistent with (7a) unless a square root of $\varphi_k$ is meant, while (6), (7b) use $v_k/\varphi_k$.
  - §14 refers to "(8) and (9) in §11"; the matching equations seem to be those of §6 or §13.
  - §15 speaks of "the minimum" but equation (2) has $\max$.
  - §24 (5) shows mixed inequality signs; (6) gives the intended bounds.
- Solutions to the exercises are not printed on these pages; none is solved here.
