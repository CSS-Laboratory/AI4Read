---
id: bellman-1957-dp/ch06-vi
work: bellman-1957-dp
unit: "Chapter VI. Bottleneck Problems in Multi-Stage Production Processes"
pages: 183-206
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Bottleneck Problems in Multi-Stage Production Processes

## L0 — One line
Production limited by the scarcest input gives a linear dynamic allocation problem, which Bellman attacks with a functional equation, a nonlinear partial differential equation (PDE) involving the time remaining, and a backward-running dual problem that verifies a guessed optimal policy.

## L1 — The gist (≤ 120 words)
How should scarce steel and tools be allocated over time when each output is limited by its scarcest input (a "bottleneck")? The discrete model is a linear programme. It is costly to solve directly when stages are many. Bellman writes the principle of optimality as a functional equation. Its continuous-time limit is a nonlinear partial differential equation (PDE) involving the remaining time. He solves a two-variable example by taking the trivial short-duration policy and extending it by conjecture. Then he proves the guess optimal with a dual problem (a companion problem that bounds the original) that runs backwards in time. Homogeneity cuts the tabulation to one-variable functions. He calls the general theory rudimentary.

**Prerequisites:** linear programming (vertices of polyhedra); vector–matrix ODEs; principle of optimality; integration by parts; partial derivatives and gradient.

## L2 — Key ideas (5–10 bullets)
- "Bottleneck" means output is proportional to the *minimum* of the required inputs. With proportional (linear) output this makes the multi-stage allocation problem a linear programme (pp. 185–187).
- Many stages with a moderate number of activities meet the usual difficulty of dimensionality when conventional computation is used. Bellman reformulates by functional equations (equations for the best value as a function of the starting state and the duration), and by continuous-time versions to get explicit analytic policies (pp. 183, 188).
- The basic equation is $f(c,S+T)=\max f(c(S),T)$. Its infinitesimal form is the nonlinear PDE $\partial f/\partial T=\max_{z(0)}(A_1c+A_2z(0),\partial f/\partial c)$ (pp. 192–193).
- The PDE continues a solution from short to longer durations. In the example, the form of the optimal policy changes as the duration $T$ passes $T_1$ and again $T^*=T_1+1/(a_1a_2)$ (pp. 194–196).
- Linearity gives a dual problem (a companion problem whose solutions bound the original's). A feasible primal–dual pair that satisfies relations (12.13) is optimal for both. This verifies conjectured policies (pp. 197–199).
- The example's optimal policy is verified through the dual, whose variables run backwards in time (pp. 200–202).
- Homogeneity, $f_N(c_1,c_2)=c_1f_N(1,c_2/c_1)$, reduces a two-variable tabulation on a growing grid to two one-variable sequences on a fixed grid (pp. 202–203).
- Continuous versions may need delta-function (impulsive) solutions and Stieltjes integrals (a more general kind of integral). Bellman proceeds formally and defers rigour (pp. 190, 192, 198).

## L3 — Walkthrough

### §1 Introduction (pp. 183–184)
The chapter treats a class of "significant and difficult" variational problems from multi-stage production (p. 183).
- Under proportionality of output to input, the discrete version is a maximum of a linear form under linear constraints. This is the linear-programming domain; a large class of applied problems can be solved numerically with computing machines and iterative techniques such as the simplex technique (p. 183).
- Many stages with a moderate number of activities per stage meet the dimensionality difficulty. The remedy is functional equations.
- For explicit analytic policies Bellman uses continuous versions. He says the continuous process may be closer to reality than the discrete one in many cases. He exploits the dual continuous process (p. 183).
- The theory is "in its rudimentary stages" (p. 184).

The general problem is to maximize over $z(t)$ the inner product $(x(T),a)$, where
$$dx/dt=Ax+Bz,\quad x(0)=c \tag{1}$$
$$Cz\le Dx,\quad 0\le t\le T. \tag{2}$$

### §2 A general class of multi-stage production problems (pp. 184–187)
Model: three lumped industries, auto, steel and tool. Each is described by a stockpile and a capacity. Changes occur at discrete times $t=0,1,\dots,T$ (p. 184).

State variables (p. 185), eq. (1):
- $x_1$ = autos produced up to $t$
- $x_2$ = auto capacity
- $x_3$ = steel stockpile
- $x_4$ = steel-mill capacity
- $x_5$ = tool stockpile
- $x_6$ = tool-factory capacity

Interdependence, eq. (2) (p. 185):
- (a) capacity increases need only steel and tools;
- (b) autos need only auto capacity and steel;
- (c) steel needs only steel capacity;
- (d) tools need only tool capacity and steel.

Decisions (eq. 3, p. 185): $z_i(t)$ is steel allocated to increasing $x_i$. $w_i(t)$ is tools allocated to increasing $x_i$. By (2): $z_3=0$ and $w_1=w_3=w_5=0$ (eq. 4).

Production is linear in the *minimum* of the required inputs. Output is proportional to capacity when raw material is abundant, and to the raw material when capacity is abundant. This is why the problems are called bottleneck problems (p. 186). Footnote 3 (p. 185) notes that a nonlinear law of diminishing returns may actually give a simpler mathematical problem, since nonlinear functions suit a variational approach, while linear problems may be easier numerically in some cases. For autos:
$$x_1(t+1)=x_1(t)+\mathrm{Min}(\gamma_1x_2(t),\alpha_1z_1(t)). \tag{2.5}$$

All the equations of (2.6) are conservation equations: new quantity = old − used + produced (footnote 4, p. 186). The full system is
$$\begin{aligned}
x_1(t+1)&=x_1+\mathrm{Min}(\gamma_1x_2,\alpha_1z_1)\\
x_2(t+1)&=x_2+\mathrm{Min}(\alpha_2z_2,\beta_2w_2)\\
x_3(t+1)&=x_3-z_1-z_2-z_4-z_5-z_6+\gamma_2x_4\\
x_4(t+1)&=x_4+\mathrm{Min}(\alpha_4z_4,\beta_4w_4)\\
x_5(t+1)&=x_5-w_2-w_4-w_6+\mathrm{Min}[\gamma_5x_6,\alpha_5z_5]\\
x_6(t+1)&=x_6+\mathrm{Min}(\alpha_6z_6,\beta_6w_6)
\end{aligned}\tag{2.6}$$

Constraints (p. 186):
- (7a) $z_i,w_i\ge0$.
- (7b) $z_1+z_2+z_4+z_5+z_6\le x_3$.
- (7c) $w_2+w_4+w_6\le x_5$.

"Common-sense" constraints (eq. 8): $\alpha_1z_1\le\gamma_1x_2$; $\alpha_2z_2=\beta_2w_2$; $\alpha_4z_4=\beta_4w_4$; $\alpha_5z_5\le\gamma_5x_6$; $\alpha_6z_6=\beta_6w_6$. Meaning: allocating beyond production capacity gains nothing, and the minimum resource fixes the output level (p. 187).

Eliminating $w_i$ with $\varepsilon_i=\alpha_i/\beta_i$ gives (p. 187)
$$\begin{aligned}
x_1(t+1)&=x_1+\alpha_1z_1,\quad x_2(t+1)=x_2+\alpha_2z_2,\\
x_3(t+1)&=x_3-z_1-z_2-z_4-z_5-z_6+\gamma_2x_4,\quad x_4(t+1)=x_4+\alpha_4z_4,\\
x_5(t+1)&=x_5-\varepsilon_2z_2-\varepsilon_4z_4-\varepsilon_6z_6+\alpha_5z_5,\quad x_6(t+1)=x_6+\alpha_6z_6,
\end{aligned}\tag{2.9}$$
with $x_i(0)=c_i$. The constraints are
- (10a) $z_i\ge0$
- (10b) $z_1+z_2+z_4+z_5+z_6\le x_3$
- (10c) $\gamma_2z_2+\gamma_4z_4+\gamma_6z_6\le x_5$ (as printed; see Reading notes)
- (10d) $z_1\le f_2x_2$
- (10e) $z_5\le f_6x_6$

Task: choose $z_i(t)$, $t=0,\dots,T-1$, to maximize $x_1(T)$.

*Intuition note.* Each output is capped by whichever input is scarcer. So output is proportional to the scarcer input, and, once the "common-sense" constraints (2.8) remove the minimum, the problem is a linear programme (p. 187).

### §3 Discussion of the model (pp. 187–188)
- $x_1(T)$ is linear in the $z_i(t)$. So the problem is a linear programme, solvable numerically for explicit coefficients if $T$ is not too large (p. 187).
- The real interest is a sensitivity (stability) analysis over a range of parameters. Conclusions about policy structure are valid only if they are relatively insensitive to parameter values. The model is crude: linear output, lumped capacities, no lead time (p. 188).
- Pure computation for this is tedious, time-consuming and inevitably incomplete. So Bellman asks for the intrinsic structure of the optimal policy, independent of parameter values (p. 188).

### §4 Functional equations (pp. 188–189)
The optimal total output depends only on initial resources and duration. $c_1$ need not be explicitly mentioned (p. 188). (added step: $x_1$ appears in none of the constraints and in none of the updates of the other states.) Define $f(c_2,\dots,c_6;T)$ as the optimal total output over duration $T$ (eq. 1, p. 188). By the principle of optimality,
$$f(c_2,\dots,c_6;T+1)=\max_{Z}\left[\alpha_1z_1+f(c_2',\dots,c_6';T)\right],\tag{2}$$
$$\begin{aligned}
c_2'&=c_2+\alpha_2z_2,\quad c_3'=c_3-z_1-z_2-z_4-z_5-z_6+\gamma_2c_4,\quad c_4'=c_4+\alpha_4z_4,\\
c_5'&=c_5-\varepsilon_2z_2-\varepsilon_4z_4-\varepsilon_6z_6+\alpha_5z_5,\quad c_6'=c_6+\alpha_6z_6.
\end{aligned}\tag{3}$$
$Z$ is the region in $(z_1,z_2,z_4,z_5,z_6)$-space cut out by the analogue of (2.10), with $c_3,c_5,c_2,c_6$ in place of $x_3,x_5,x_2,x_6$ (eq. 4, p. 189).
- Analysis and computation both remain hard: a function of five variables must be tabulated for each $T$. Homogeneity reduces this to four variables (p. 189).
- The maximum over the polyhedral region $Z$ occurs at vertices (p. 189).

### §5 A continuous version (pp. 189–190)
Decisions are made at $0,\Delta t,2\Delta t,\dots$ and allocations $z_i\Delta t$, $w_i\Delta t$ replace $z_i$, $w_i$. So $z_i,w_i$ become *rates of allocation* (p. 189). Letting $\Delta t\to0$ in (2.9):
$$\begin{aligned}
\dot x_1&=\alpha_1z_1,\quad \dot x_2=\alpha_2z_2,\quad \dot x_3=-z_1-z_3-z_4-z_5-z_6+\gamma_2x_4\ (\text{as printed; see Reading notes}),\\
\dot x_4&=\alpha_4z_4,\quad \dot x_5=-\varepsilon_2z_2-\varepsilon_4z_4-\varepsilon_6z_6+\alpha_5z_5,\quad \dot x_6=\alpha_6z_6,
\end{aligned}\tag{5.1}$$
with $x_i(0)=c_i$.

Constraints (5.2): $z_i\ge0$; the bounds (b), (c) become $\le\infty$ and disappear; (d) $z_1\le f_2x_2$; (e) $z_5\le f_6x_6$. Two conditions that held automatically in discrete time must now be added (eq. 3, p. 190): $x_3\ge0$ and $x_5\ge0$.
- When $x_3=0$: $z_1+z_3+z_4+z_5+z_6\le\gamma_2x_4$ (5.4, as printed).
- When $x_5=0$: $\varepsilon_2z_2+\varepsilon_4z_4+\varepsilon_6z_6\le\alpha_5z_5$ (5.5).
- Hence, as printed, $z_2,z_3,z_4,z_6$ are unbounded whenever $x_3$ and $x_5$ are positive. So delta-function solutions may occur. Rigour is postponed to a second volume, and Bellman proceeds formally (p. 190).

### §6 Notation (pp. 191–192)
Vectors $x(t),z(t),c$ and matrices $A_i,B_j$ (printed as $n\times m$; see Reading notes). $x\ge0$ means componentwise. The continuous system is
$$dx/dt=A_1x+A_2z,\ x(0)=c;\qquad z\ge0,\ B_1z\le B_2x \tag{6.1, 6.2}$$
The inner product is $(x,y)=\sum_{i=1}^nx_iy_i$ (6.3). The general problem is to maximize $(x(T),a)$ for a given vector $a$.

In the continuous case a maximum may not exist if $z(t)$ must be an ordinary function. Bellman *assumes* the constraints suffice for existence. This will be the case if (6.2) has the form $z\le B_3x$ with $B_3$ a positive matrix. A complete treatment needs Stieltjes integrals (p. 192).

### §7–§8 Dynamic programming formulation and basic equation (p. 192)
$\max_z(x(T),a)=f(c,T)\equiv f(c_1,\dots,c_n;T)$, a function only of duration and initial state, because the constraints are time-independent (7.1). The principle of optimality here says: any final sub-interval $[S,T]$ of an optimal policy is optimal for duration $T-S$ from the state $c(S)$. This gives
$$f(c,S+T)=f(c(S),T)\ \text{ for an optimal policy},\tag{8.1}$$
$$f(c,S+T)=\max_{[0,S]}f(c(S),T),\quad f(c,0)=(c,a)\tag{8.2}$$
The maximum in (8.2) is over all feasible $z(t)$ on $[0,S]$. Here $c(S)=x(S)$ is the state reached from (6.1).

### §9 The resultant nonlinear PDE (p. 193)
Assume enough differentiability (this is formal; a technique for verifying any proposed solution follows later). For infinitesimal $S$:
$$\begin{aligned}
&\text{(a)}\ f(c,S+T)=f(c,T)+Sf_T+o(S)\\
&\text{(b)}\ c(S)=c+S[A_1c+A_2z(0)]+o(S)\\
&\text{(c)}\ f(c(S),T)=f(c,T)+S\left((A_1c+A_2z(0),\tfrac{\partial f}{\partial c})\right)+o(S)
\end{aligned}\tag{9.1}$$
Here $\partial f/\partial c$ is the vector $(\partial f/\partial c_1,\dots,\partial f/\partial c_N)'$ (9.2). As $S\to0$ the maximum over $[0,S]$ becomes a maximum over $z(0)$. Equating (a) with (c) in (8.2) (added step: cancel $f(c,T)$, divide by $S$, let $S\to0$):
$$\frac{\partial f}{\partial T}=\max_{z(0)}\left[\left(A_1c+A_2z(0),\frac{\partial f}{\partial c}\right)\right],\tag{9.3}$$
with $z(0)$ constrained by (6.2).

*Intuition note.* With $T$ the time still to go, the rate at which optimal value grows equals the best possible instantaneous drift of the state, valued by the gradient of $f$. This is the continuous version of "best first step plus value of where you land".

### §10 Use of the PDE (pp. 193–194)
(9.3) extends a solution on $[0,T]$, known for *all* initial states, to $[0,T+\Delta T]$. For short durations obvious crude policies are often optimal. So in theory the solution can be continued to any $T$, though the details are "by no means trivial". Much analysis can be discarded once the structure is known, which is often plausible economically (p. 194).

### §11 A particular example (pp. 194–197)
Maximize $x_2(T)$ for
$$dx_1/dt=a_1z_1,\ x_1(0)=c_1;\qquad dx_2/dt=a_2z_2-z_1,\ x_2(0)=c_2,\tag{1}$$
with (2): $z_1,z_2\ge0$; $z_1+z_2\le x_2$; $z_2\le x_1$; $x_2\ge0$.

Here $z_1,z_2$ are uniformly bounded. A weak-convergence argument or classical calculus of variations shows the maximum is attained (p. 194). Define $f(c_1,c_2,T)=\max x_2(T)$ (3). Then (4) holds, $f(c_1,c_2,S+T)=\max f(x_1(S),x_2(S),T)$, and in the limit
$$\frac{\partial f}{\partial T}=\max_{z(0)}\left[a_1z_1\frac{\partial f}{\partial c_1}+(a_2z_2-z_1)\frac{\partial f}{\partial c_2}\right],\tag{5}$$
still purely formal, since continuity of $f$ is unknown. Maximization is over (6): $z_1,z_2\ge0$, $z_1+z_2\le c_2$, $z_2\le c_1$. If $x_2=0$ there is the extra constraint (7): $a_2z_2-z_1\ge0$.

*Case $c_2<c_1$ (the most complicated; p. 195).*
- Short duration: $z_1=0$, $z_2=x_2$, $f=c_2e^{a_2T}$ (8).
- This continues until a bottleneck develops, i.e. $c_2$ catches up with $c_1$. That happens once $T$ exceeds $T_1=\log(c_1/c_2)/a_2$.
- For $T>T_1$ rewrite (5) as
$$\frac{\partial f}{\partial T}=\max_{z(0)}\left[z_1\left(a_1\frac{\partial f}{\partial c_1}-\frac{\partial f}{\partial c_2}\right)+a_2\frac{\partial f}{\partial c_2}z_2\right].\tag{9}$$
- For $T<T_1$: $a_1\partial f/\partial c_1-\partial f/\partial c_2=-e^{a_2T}$ and $a_2\partial f/\partial c_2=a_2e^{a_2T}$ (10).
- By continuity of the derivatives, Bellman *suspects* that for $T$ slightly above $T_1$ the policy is
$$\text{(a) }z_1=0,z_2=x_2\ (0\le S\le T_1);\quad \text{(b) }z_1=0,z_2=x_1\ (T_1<S\le T).\tag{11}$$
- It gives $f=c_1+(T-T_1)a_2c_1$ (12).
- To see how long this lasts, restart at $S=T_1$ with $c_1'=c_1(T_1)$, $c_2'=c_2(T_1)$. Then $f=c_2'+a_2c_1'(T-T_1)$ (13), and (9) holds with primes (14).
- From (13): $a_1\partial f/\partial c_1'-\partial f/\partial c_2'=a_1a_2(T-T_1)-1$ and $a_2\partial f/\partial c_2'=a_2$ (15).
- The coefficient of $z_1$ is negative for $T<T^*=T_1+1/(a_1a_2)$, zero at $T^*$, positive after. So (11) remains optimal for $T_1\le T\le T^*$.
- $T^*-T_1$ is independent of $c_1,c_2$. So the form of the optimal policy over a tail interval is known (p. 196).
- For larger $T$ Bellman *suspects* the middle of $[0,T]$ has $z_1=x_2-x_1$, $z_2=x_1$ (16).

When $c_2>c_1$, in the constraint region (Figure 1) the crucial vertices are $P=(0,c_1)$, $Q=(c_2-c_1,c_1)$, $R=(c_2,0)$ in the $(z_1,z_2)$ plane. "The principle of continuity" leads to choosing $Q$ as the maximizing vertex as soon as $c_2$ surpasses $c_1$ (p. 196). Direct verification is possible, but Bellman prefers the duality technique (p. 197).

*Intuition note.* While $x_2\le x_1$, the whole of $x_2$ goes to $z_2$ and $z_1=0$. Once $x_2$ passes $x_1$, the constraint $z_2\le x_1$ caps $z_2$ at $x_1$, so the surplus $x_2-x_1$ is available for $z_1$. Bellman suspects this form in the middle phase (16). The text gives no economic meaning to $x_1,x_2$ in this example.

### §12 A dual problem (pp. 197–199)
Take the simpler form
$$dx/dt=Az,\ z(0)=c\ (\text{printed; read }x(0)=c),\quad z\ge0,\ Bz\le x,\ x\ge0.\tag{1, 2}$$
(6.1) can always be put in this form if $A_1\ge0$. Write $dx/dt=A_1w+A_2z$ with $w\le x$, and combine $w$ and $z$ into one vector (eqs. 3–4). Direct treatment is also possible (p. 197).

Since $x=c+\int_0^tAz\,dt$, the constraint $Bz\le x$ becomes
$$Bz+\int_0^tCz\,dt_1\le c,\quad C=-A.\tag{5, 6b}$$
Maximizing $(x(T),a)$ is equivalent to maximizing $J=\int_0^T(Az,a)dt=\int_0^T(z,a')dt$, with $a'=A'a$ ($A'$ is the transpose of $A$).

Let $w(t)\ge0$ have the dimension of $c$. By (6b):
$$\int_0^T\Big(w,Bz+\int_0^tCz\,dt_1\Big)dt\le\int_0^T(w,c)\,dt.\tag{7}$$
Use $(Bz,w)=(z,B'w)$ and integration by parts for constant $C$:
$$\int_0^T\Big(w,\int_0^tCz\,dt_1\Big)dt=\int_0^T\Big(\int_t^TC'w\,dt_1,z\Big)dt\tag{8}$$
Combining (7) and (8):
$$\int_0^T\Big(w,Bz+\int_0^tCz\,dt_1\Big)dt=\int_0^T\Big(B'w+\int_t^TC'w\,dt_1,z\Big)dt\tag{9}$$
Assume a $w\ge0$ exists with
$$B'w+\int_t^TC'w\,dt_1\ge a'.\tag{10}$$
Then (added step: the first inequality uses $w\ge0$ and (6b); the last uses $z\ge0$ and (10)):
$$\int_0^T(w,c)dt\ \ge\ \int_0^T\Big(w,Bz+\int_0^tCz\,dt_1\Big)dt=\int_0^T\Big(B'w+\int_t^TC'w\,dt,z\Big)dt\ \ge\ \int_0^T(a',z)dt\tag{11}$$
$$\inf_w\int_0^T(w,c)dt\ \ge\ \sup_z\int_0^T(z,a')dt\tag{12}$$
Infimum and supremum are over $w$ satisfying (10) and $z$ satisfying (6b). If they are not attained, delta-functions occur, and Stieltjes integrals are needed. The link to a min-max result of game theory is not discussed (footnote 8, p. 198).

If the two extremes in (11) are equal, then (apart from sets of measure zero; footnote 9, p. 199)
$$w_i=0\ \text{if}\ c_i>\Big(Bz+\int_0^tCz\,dt\Big)_i;\qquad z_j=0\ \text{if}\ a_j'<\Big(B'w+\int_t^TC'w\,dt\Big)_j.\tag{13}$$
*Converse.* Any non-negative $z$ and $w$ satisfying (13) and the original constraints solve the maximum and minimum problems.
- Under (13) all relations in (11) are equalities.
- Suppose some feasible $\bar z$ had $\int(z,a')dt<\int(\bar z,a')dt$ (14).
- Then, with the $w$ paired with $z$,
$$\int_0^T(\bar z,a')dt\le\int_0^T\Big(\bar z,B'w+\int_t^TC'w\,dt_1\Big)dt=\int_0^T\Big(B\bar z+\int_0^tC\bar z\,dt_1,w\Big)dt\le\int_0^T(c,w)dt=\int_0^T(z,a')dt\tag{15}$$
- This contradicts (14).

Verification procedure: given a conjectured $z$, find $w$ from (13), then test whether $w$ satisfies its constraints. Difficulties arise if $w$ is not uniquely determined by (13); then alternatives must be considered (p. 199).

*Intuition note.* Any admissible $w$ gives an upper bound on what $z$ can earn. If a $z$ reaches the bound, it must be optimal. The relations (13) say a constraint with slack carries no weight, and a variable that is not worth using is not used.

### §13 Verification of the solution of §11 (pp. 200–202)
The dual of §11 is to minimize $\int_0^T(c_1w_1+c_2w_2)dt$, with
$$\frac{dy_1}{dt}=-a_1w_1+w_2,\ y_1(T)=-1;\qquad \frac{dy_2}{dt}=-a_2w_2,\ y_2(T)=a_2.\tag{1}$$
The dual runs backwards in time (footnote 10). The constraints are (2): $w_1,w_2\ge0$; $w_1+w_2\ge y_2$; $w_2\ge y_1$.

Relations (12.13) become (3):
- (a) if $z_2<x_1$ then $w_1=0$;
- (b) if $z_1+z_2<x_2$ then $w_2=0$;
- (c) if $w_2>y_1$ then $z_1=0$;
- (d) if $w_1+w_2>y_2$ then $z_2=0$.

Conditions for $x_2\ge0$ are omitted. Bellman suspects the proposed policy keeps $x_2\ge0$, and says this is actually the case.

Claimed optimal policy (4):
- (a) for $T-1/(a_1a_2)<t\le T$: $z_1=0$, $z_2=\min(x_1,x_2)$.
- (b) for $0\le t\le T-1/(a_1a_2)$: if $x_2\le x_1$ then $z_1=0,z_2=x_2$. If $x_2\ge x_1$ then $z_1=x_2-x_1$, $z_2=x_1$.

It is permissible, since $z_1=x_2-x_1\ge0$ in the second branch. Assume $T\ge T_1$, so that $x_2$ can exceed $x_1$.

*Case I: $T-1/(a_1a_2)<T_1<T$.* (5): $z_1=0$ always; $z_2=x_2$ for $t<T_1$ and $z_2=x_1$ for $t\ge T_1$. From (2) and (3) (eq. 6 as printed has "$T_1<T$ / $T_1\ge T$" as labels; context requires $t<T_1$ / $t\ge T_1$):
- for $t<T_1$: $w_1=0$, $w_2=y_2$;
- for $t\ge T_1$: $w_2=0$, $w_1=y_2$.

For $t>T_1$, using (1): $y_2=a_2$ and $y_1=-1+a_1a_2(T-t)<0$ (7). For $t<T_1$:
$$y_2=a_2e^{a_2(T_1-t)}>0,\quad y_1=a_1a_2(T-T_1)-e^{a_2(T_1-t)}<0\tag{8}$$
Hence $w_1,w_2\ge0$, $w_2\ge y_1$, $w_1\ge y_2$ hold in their intervals.

*Case II: $T_1<T-1/(a_1a_2)$ (the most interesting).* (9):
- for $T-1/(a_1a_2)\le t\le T$: $z_1=0$, $w_2=0$; $z_2=x_1$, $w_1=y_2$;
- for $T_1\le t\le T-1/(a_1a_2)$: $z_1=x_2-x_1$, $w_2=y_1$; $z_2=x_1$, $w_1=y_2-y_1$;
- for $0\le t\le T_1$: $z_1=0$, $w_1=0$; $z_2=x_2$, $w_2=y_2$.

On the last interval, $y_2=a_2$ and $y_1=-1+a_1a_2(T-t)$ (10). So $y_1\le0=w_2$ there, and $y_1(T-1/(a_1a_2))=0$. In the middle range:
$$dy_1/dt=-a_2y_2+(a_1+1)y_1,\quad dy_2/dt=-a_2y_2\tag{11}$$
(as printed; see Reading notes). To show $y_1\ge0$ and $y_2\ge y_1$ there, start at $t=T-1/(a_1a_2)$, where these hold, and reverse time:
$$dy_1/dt=a_2y_2-(1+a_1)y_1,\quad dy_2/dt=a_2y_2\tag{12}$$
$$d/dt(y_2-y_1)=(1+a_1)y_1\tag{13}$$
- So if $y_1$ stays non-negative, $y_2-y_1\ge0$.
- $dy_1/dt$ starts positive and stays positive while $(y_1,y_2)$ lies above the line $a_2y_2-(1+a_1)y_1=0$.
- If the trajectory hit that line, then $dy_1/dt=0$, so $y_1$ would have a maximum or inflection point. This is excluded, since at such a point
$$\frac{d^2y_1}{dt^2}=a_2\frac{dy_2}{dt}-(1+a_1)\frac{dy_1}{dt}=a_2^2y_2>0\tag{14}$$
- Hence $w_1,w_2\ge0$ in this interval.

Finally, for $t<T_1$: $dy_1/dt=y_2$, $dy_2/dt=-a_2y_2$ (15). As $t$ decreases, $y_2$ increases and $y_1$ decreases, so $y_2\ge y_1$ remains valid. This completes the verification.

*Intuition note.* The proof does not search over policies. It builds a dual candidate $w$ from the claimed policy and checks that $w$ is feasible. Feasibility plus the slackness relations then give optimality by §12.

### §14 Computational solution (pp. 202–203)
Discrete two-variable problem: maximize $x_N$ for
$$x_{k+1}=a_{11}x_k+a_{12}y_k+b_{11}z_k+b_{12}w_k,\ x_0=c_1;\qquad y_{k+1}=a_{21}x_k+a_{22}y_k+b_{21}z_k+b_{22}w_k,\ y_0=c_2\tag{1}$$
subject to $d_{i1}z_k+d_{i2}w_k\le d_{i3}x_k+d_{i4}y_k$, $i=1,\dots,M$ (2). Then $f_1(c_1,c_2)=c_1$ and
$$f_{N+1}(c_1,c_2)=\max_R f_N\big(a_{11}c_1+a_{12}c_2+b_{11}z+b_{12}w,\ a_{21}c_1+a_{22}c_2+b_{21}z+b_{22}w\big)\tag{3}$$
over $R$: $d_{i1}z+d_{i2}w\le d_{i3}c_1+d_{i4}c_2$ (4).
- The maximum is attained at a vertex of $R$. Bellman recommends proving this as an exercise. So each stage's maximization is trivial.
- The burden is tabulating functions of two variables. The grid may grow: computing $f_N$ on a box needs $f_{N-1}$ on a larger region, and so on (p. 203).
- Homogeneity: $f_N(c_1,c_2)=c_1f_N(1,c_2/c_1)=c_2f_N(c_1/c_2,1)$ for $c_1,c_2>0$ (5). With it, (3) becomes (6): the value is $\max_R$ of the first new coordinate times $f_N$ evaluated at ratio of new coordinates, with $f_N(1,\cdot)$ or $f_N(\cdot,1)$.
- So if the two functions $g_N(x)=f_N(x,1)$ and $h_N(x)=f_N(1,x)$ for $0\le x\le1$ are known, $f_{N+1}$ can be computed (7). One computes two sequences of one-variable functions on a fixed grid (p. 203).
- (added step) One would use whichever form of (6) makes the ratio lie in $[0,1]$. The text states only the range in (7).

### §15 Nonlinear problems (pp. 203–204)
Many problems in analysis, engineering control and economics are of the form: maximize or minimize
$$J(z)=\int_0^TF(x_1,\dots,x_n;z_1,\dots,z_m)\,dt$$
subject to $dx_i/dt=G_i(x,z)$ and $R_j(x,z)\le0$ (eqs. 1–2).
- Nonlinearity may allow a more complete analysis. The extremal can then be found by classical variational techniques, rather than by testing vertices.
- Where constraints of the above type enter, the two approaches must be combined.
- The functional equation technique serves both analytic and numerical purposes (p. 204).
- This is taken up in Chapter 9.

### Exercises and Bibliography (pp. 204–206)
Eleven exercises are listed (see "Exercises worth doing"). The bibliography notes mention:
- Koopmans' *Activity Analysis* and Dantzig's simplex technique (§1).
- Boldyreff's "flooding" technique. Both are relaxation techniques in the sense of Southwell (§1).
- Bellman's earlier papers (§5).
- The expected need for Lebesgue–Stieltjes integrals and L. Schwarz's distributions (§9).
- Possible game-theoretic min-max = max-min results (§12).
- R. S. Lehman's continuous simplex method (§13) (pp. 205–206).

## Toy example (ours, using the chapter's §11 formulas)
Take $a_1=a_2=1$, $c_1=2$, $c_2=1$, $T=T_1+0.5$.
1. $T_1=\log(c_1/c_2)/a_2=\ln2\approx0.693$. $T^*=T_1+1/(a_1a_2)=T_1+1$. Since $T_1<T<T^*$, policy (11) applies.
2. Primal. On $[0,T_1]$, $z_1=0$, $z_2=x_2$, so $x_2=e^t$ grows from 1 to 2 (and $x_1$ stays 2). On $[T_1,T]$, $z_2=x_1=2$, so $\dot x_2=2$ for 0.5 time units, giving $x_2(T)=2+1=3$. Check with (12): $c_1+(T-T_1)a_2c_1=2+0.5\cdot1\cdot2=3$. ✓.
3. Dual (Case I). For $t\ge T_1$: $w_1=a_2=1$, $w_2=0$, $y_1=-1+0.5=-0.5$ at $t=T_1$ (using (7)). For $t<T_1$: $w_2=y_2=e^{T_1-t}$, $w_1=0$. At $t=0$, $y_1=0.5-2=-1.5<w_2=2$. All dual constraints hold.
4. Dual cost: $\int c_1w_1+c_2w_2\,dt=2\cdot1\cdot0.5+1\cdot\int_0^{T_1}e^{T_1-t}dt=1+(2-1)=2$.
5. (added step) The primal $\int(z,a')dt$ equals $x_2(T)-c_2=3-1=2$. So primal and dual agree, and by (11)–(12) the policy is optimal. The dual objective matches $x_2(T)-c_2$, not $x_2(T)$, because (12.5) maximizes only the integral part of $(x(T),a)$.

## Concepts
- [[bottleneck-production]] (new) — output proportional to the minimum of required inputs, so the scarcest input limits production (p. 186)
- [[principle of optimality]] — the continuation of an optimal policy over $[S,T]$ is optimal from $c(S)$ (p. 192)
- [[Bellman equation / value function]] — $f(c,T)$ obeys $f(c,S+T)=\max f(c(S),T)$ and its discrete analogue (2) (pp. 188, 192)
- [[Hamilton–Jacobi–Bellman equation]] — the author calls (9.3) a nonlinear PDE. The HJB name is not used in this unit (canon link; not stated in this unit) (p. 193)
- [[state]] — each industry's state is assumed to be completely specified by its stockpile and capacity (p. 184)
- [[state-space model]] — $dx/dt=A_1x+A_2z$, $B_1z\le B_2x$ (p. 191)
- [[curse-of-dimensionality]] (new) — Bellman calls it "the usual difficulty of dimensionality": many stages plus many activities make tabulation costly (pp. 183, 189, 203)
- [[linear-programming-dual]] (new) — dual process with variables $w,y$ running backwards in time, with weak-duality inequality (12.12) and verification via (12.13) (pp. 197–199)
- [[homogeneity-reduction]] (new) — $f_N(c_1,c_2)=c_1f_N(1,c_2/c_1)$, which reduces tabulation dimension (pp. 189, 203)
- [[impulsive-delta-function-solutions]] (new) — rates $z_i$ may be unbounded, so the optimal $z$ may involve delta functions and Stieltjes integrals (pp. 190, 198)

## Canonical instances
- [[auto-steel-tool-model]] — six-state discrete and continuous bottleneck process (pp. 185–190)
- [[two-variable-bottleneck-example]] — §11 example with threshold durations $T_1$ and $T^*=T_1+1/(a_1a_2)$ (pp. 194–196)
- [[dual-verification-of-policy]] — checking the §11 policy through the dual $y,w$ system (pp. 200–202)

## Bridges (candidates)
- [same-math] PDE (9.3), $\partial f/\partial T=\max_z(\dot x,\nabla f)$ ↔ control theory: HJB equation with time-to-go — same maximization of drift against the value gradient.
- [structural-analogy] Dual variables $y(t)$, which run backward from terminal conditions ↔ Pontryagin costates (shadow prices along a trajectory) — also evolve backward, price the state.
- [same-math] Discrete functional equation (4.2) ↔ RL: Bellman optimality equation for a deterministic MDP with action-dependent immediate payoff.
- [structural-analogy] Relations (13) ("unused constraint has zero price; unprofitable variable is zero") ↔ LP complementary slackness.

## Questions this raises
- When is a "suspected" policy guaranteed to be verifiable by the dual, and what happens when $w$ is not unique from (13)?
- How should delta-function (impulsive) allocations be defined rigorously, given that Bellman defers this?
- How do the switch times $T_1$ and $T^*$ depend on parameters in the full six-state model (the point of sensitivity analysis in §3)?
- Does the homogeneity trick of §14 extend beyond two state variables (Exercise 5 asks for this)?

## Exercises worth doing
- Ex. 1 (p. 204) — derive the one-stage and recursive DP equations for a linear form under linear resource constraints — difficulty: medium
- Ex. 2–3 (p. 204) — show $f_N$ is concave in $c$, and infer something about the number of non-zero maximizing $x_i$ — difficulty: medium
- Ex. 5 (p. 204) — reduce tabulation of $f_N(c_1,\dots,c_M)$ to $f_N(c_1,\dots,1)$, and prove the analogue for the bottleneck process — difficulty: medium
- Ex. 6 (p. 205) — scalar problem $\dot u=au+v$, $0\le v\le u$ — difficulty: easy
- Ex. 8 (p. 205) — show that a two-allocation problem is equivalent to PDE (c) — difficulty: medium
- Ex. 9 (p. 205) — show optimal policies depend only on a ratio and the time remaining — difficulty: medium

## Reading notes
- Printed page = pdf page − 23 (pdf 206 = printed 183).
- Misprints and ambiguities seen in the page images:
  - Constraints (2.10c) and (4c) print $\gamma_2z_2+\gamma_4z_4+\gamma_6z_6$ (bounded by $x_5$ and $c_5$ respectively). Elimination of $w_i$ via $w_i=\varepsilon_iz_i$ suggests $\varepsilon_i$. This is a reading from the text's own algebra, not stated by the author.
  - $f_2$, $f_6$ in (2.10d, e) are never defined on these pages.
  - Eqs. (5.1) (for $\dot x_3$) and (5.4) print $z_3$ where the discrete (2.9) has $z_2$. This is presumably a misprint, since $z_3=0$ by (2.4). I reproduced the printed form.
  - On p. 187 "in place of (4.6)" should presumably refer to (2.6).
  - Eq. (12.1) prints "$z(0)=c$"; context requires $x(0)=c$.
  - §6 says $A_i,B_j$ are $n\times m$ matrices, but the same sentence says $x,z,c$ are all $n$-dimensional. In §5 the allocation vector has five nonzero components against six states, so shapes are not consistent. The shape of $A_1$ must be $n\times n$ for $A_1x$.
  - §6 mentions a constraint $B_3$ not defined in (6.2) (which has $B_1,B_2$).
  - Eq. (13.6) labels intervals "$T_1<T$ / $T_1\ge T$" where the context requires $t<T_1$ / $t\ge T_1$.
  - On p. 190 the text lists "$z_2,z_3,z_4,z_6$" as unbounded, but $z_3=0$ by (2.4). Presumably $z_2,z_4,z_6$.
  - Eq. (13.11)–(13.12) print $a_2y_2$ in $dy_1/dt$. By (13.1) and (13.9), $dy_1/dt=-a_1w_1+w_2$ gives $-a_1y_2+(a_1+1)y_1$. The author's (13.13)–(13.14) are consistent with the printed $a_2$ version, not with the coefficient $a_1$. I reproduced the printed forms.
  - (13.14) drops the term $-(1+a_1)dy_1/dt$; it is evaluated at a point where $dy_1/dt=0$.
- The text layer is garbled in several formulas (e.g. (2.6), (4.3), (11.5), (11.9–11.15)). I checked every equation against the page images.
- Chapter VI is the full chapter, including exercises and bibliography.
