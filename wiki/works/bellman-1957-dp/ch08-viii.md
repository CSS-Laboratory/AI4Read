---
id: bellman-1957-dp/ch08-viii
work: bellman-1957-dp
unit: "Chapter VIII. A Continuous Stochastic Decision Process"
pages: 222-244
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# A Continuous Stochastic Decision Process (continuous gold-mining problem)

## L0 — One line
Bellman turns the discrete gold-mining problem into a continuous one by letting a policy mix the two mines (a time-fraction $\varphi_1(t)$), then treats it with classical variational calculus plus insight from the discrete solution. For the two-choice problem with infinite time, optimal play is "go to a straight line, then stay on it with a fixed mixture"; the three-choice case (infinite time) is also worked out.

## L1 — The gist (≤ 120 words)
The discrete gold-mining problem of Chapter II (a machine mined in two or three ways, with a risk of breaking) leaves open cases. Bellman builds a continuous version in which a policy chooses, at each time, the fraction of time spent on each choice. The state equations are ordinary differential equations. A first-order perturbation of the policy gives "switching functions" $K_i(t)$. Their derivatives locate the lines on which mixing is allowed. For the two-choice problem the optimal policy is found for infinite and for finite total time, and is unchanged for any increasing utility (a score for the total gold). The three-choice problem is solved for infinite total time, with two cases depending on the sign of a constant $D$.

**Prerequisites:** ordinary differential equations; first-order perturbation (calculus of variations); integration by parts; the discrete gold-mining model of Chapter II (as recalled on p. 227).

## L2 — Key ideas (5–10 bullets)
- A direct differential version of the functional equation gives a nonlinear first-order equation (2.3). Bellman says it does not seem fruitful because existence and uniqueness are hard to establish. The integral version is not pursued because of many difficulties in justifying its equation and in defining general continuous policies (pp. 223–224).
- In the limit $\delta\to0$ the discrete optimal policy runs along the line $L$ with $r_1x/q_1=r_2y/q_2$. A path along $L$ is not a policy for any $\delta>0$, so a maximum may fail to exist. There may only be a sequence of policies approaching a supremum (a least upper bound that is never attained), unless the concept of policy is broadened by allowing mixing of decisions (pp. 225–226).
- Mixing "at a point" is defined by mixing over small intervals of length $\Delta$. As $\Delta\to0$ this gives the defining ODE system (7.2), with the policy $\varphi_1(t)\in[0,1]$ as control (pp. 226–228).
- A first-order perturbation of the policy yields functions $K_i(t)$. If $K_i>K_j$ then $\varphi_i=1,\varphi_j=0$ (p. 229). A mixed policy (several $\varphi_i>0$ at one time) can be optimal only where the $K$'s are equal, which means only on a line (p. 230).
- Two-choice, $T=\infty$ (Theorem 1): use $A$ below $q_1r_2y=q_2r_1x$, $B$ above, and the fixed mixture $\varphi_1=r_2/(r_1+r_2)$ on the line (p. 231). Finite $T$ adds a changeover time determined by a single root (pp. 231–233).
- Three-choice, $T=\infty$: the structure depends on the sign of $D=q_1r_2r_3+q_2r_1r_4-q_3r_1r_2$. For $D>0$ (with $r_3>r_4$ and the lines $C_2=0$, $C_3=0$ in the positive quadrant) the policy runs $B$, mixed $BC$, $C$, $A$ from the $y$-axis down (Theorem 2). For $D<0$, $C$ is never used (Theorem 3) (pp. 239–241).
- Nonlinear utility (a function $u$ scoring the total gold $R$): for any strictly increasing $u$ with continuous derivative the two-choice optimal policy is the same as for linear utility. Bellman says this should warn the unwary that continuous versions need close attention to the kind of approximation they afford (p. 242).

## L3 — Walkthrough

### §1 Introduction (p. 222–223)
The discrete problem leaves unsolved the three-choice problem, the nonlinear-utility problem and others (p. 222). Bellman hopes the "more powerful tools of continuity" resolve them (p. 222). The discrete problem had linear aspects that made variational analysis difficult, at least for expected return. The continuous version is nonlinear enough to allow a classical variational approach, modified for constraints. Knowing the discrete solution tells him in advance what to expect (p. 222). Two approaches that fail are discussed first (§2, §3). The chosen approach is a compromise. That its limit is the discrete process "in a suitable sense" is asserted but not discussed here (p. 223).

### §2 Continuous versions I: a differential approach (p. 223)
Assume each operation has high probability of a small gain without damage. This restricts attention to a small region of $(r_1,r_2,q_1,q_2)$-space (p. 223). Let $1-q_1\delta$ be the probability of obtaining $r_1x\delta$ with the machine undamaged if Anaconda ($A$) is mined, and $1-q_2\delta$ the same for Bonanza ($B$) with $r_2y\delta$. The $q_i$ are positive, and $\delta$ is small enough that $1-q_i\delta$ is a probability and $r_i\delta<1$. With $f(x,y)$ the optimal expected return, the functional equation (5.1 of Chapter II) becomes

$$f(x,y)=\max\begin{cases}A:&(1-q_1\delta)\big(r_1x\delta+f(x-r_1x\delta,\,y)\big)\\ B:&(1-q_2\delta)\big(r_2y\delta+f(x,\,y-r_2y\delta)\big)\end{cases}\tag{1}$$

If $f$ has continuous partial derivatives, then for small $\delta$

$$f(x,y)=\max\begin{cases}A:&f+\delta\,(r_1x-q_1f-r_1x\,\partial f/\partial x)+O(\delta^2)\\ B:&f+\delta\,(r_2y-q_2f-r_2y\,\partial f/\partial y)+O(\delta^2)\end{cases}\tag{2}$$

and as $\delta\to0$

$$0=\max\begin{cases}A:&r_1x-q_1f-r_1x\,\partial f/\partial x\\ B:&r_2y-q_2f-r_2y\,\partial f/\partial y\end{cases}\tag{3}$$

Bellman calls this approach unfruitful: existence and uniqueness theorems are hard to establish for such equations (p. 223). The comment on p. 244 adds that (3) can be used formally to get the character of the solution, but nonlinear PDEs of this type have not yet been studied.

### §3 Continuous versions II: an integral approach (p. 224)
This is the "diametrically opposed" approach. Let $S_N$ be a sequence of $N$ choices.
- $p_{Nk}(x,y)$ is the probability of surviving $N$ stages and ending in state $(x_{Nk},y_{Nk})$ under $S_N$.
- $R_N(x,y)$ is the expected return from $N$ stages under $S_N$.

If $S_N$ is the first $N$ choices of an optimal policy,

$$f(x,y)=R_N(x,y)+\sum_k p_{Nk}(x,y)\,f(x_{Nk},y_{Nk}).\tag{1}$$

Let $N\delta=t$ stay finite as $\delta\to0$, $N\to\infty$. The analogue is

$$f(x,y)=\max_S\Big[R_S(x,y,t)+\int_{r=0}^{1}\!\int_{s=0}^{1} f(xr,ys)\,dG_S(r,s,x,y,t)\Big],\tag{2}$$

where $S$ is a continuous policy on $[0,t]$ and $dG_S$ is a transition probability determined by it (p. 224). Such equations occur in the general theory of stochastic processes. Bellman does not pursue them because of the difficulty of justifying (2) and defining general continuous policies. His method is intermediate. It yields an equation related to (2) as the heat (diffusion) equation is related to the Chapman–Kolmogorov equation (p. 224). The comment on p. 244 says that rigorous treatment needs the modern theory of stochastic processes, which is "on an exalted plane".

### §4 Preliminary discussion (pp. 224–226)
By the Chapter II solution, the $A$- and $B$-regions are separated by the curve

$$L_\delta:\ (1-q_1\delta)\frac{r_1x}{q_1}=(1-q_2\delta)\frac{r_2y}{q_2}\tag{1}$$

which tends, as $\delta\to0$, to the line

$$L:\ \frac{r_1x}{q_1}=\frac{r_2y}{q_2}.\tag{2}$$

For each $\delta>0$ the optimal policy is as follows (pp. 224–225). Below $L_\delta$, use $A$ until you are in the $B$-region above $L_\delta$. Then use $B$ until you are back in the $A$-region, and so on. Start above $L_\delta$ and the roles swap. The paths are staircases of horizontal and vertical pieces (Fig. 1).

The limiting policy as $\delta\to0$ (Fig. 2): below $L$ use $A$ until $L$ is reached, above $L$ use $B$ until $L$ is reached, then move along $L$ thereafter (p. 225). Motion along $L$ is not in the policy set of any nonzero $\delta$, but a path like Fig. 2 can be arbitrarily closely approximated by optimal policies as $\delta\to0$ (p. 225).

**Conclusion:** the continuous version of the discrete problem may have no optimal policy attaining a maximum. There may only be a sequence of policies approaching a supremum, unless the concept of policy is broadened. The natural broadening is to allow mixing of decisions at each time (pp. 225–226).

*Intuition note.* Staircase paths get finer as $\delta$ shrinks, and they approach a diagonal path. The diagonal path is not itself a staircase. So the best you can do is approach it, never achieve it, unless you may "blend" the two actions.

### §5 Mixing at a point (p. 226–227)
Mixing at a point brings both mathematical difficulties (those of §3) and physical ones: one may be reluctant to accept mixing when a single choice is required (p. 226). The device used is the observation that, under certain natural continuity assumptions, mixing decisions at a point is equivalent to mixing them over small intervals about the point (p. 226).

At times $t=0,\Delta,2\Delta,\dots$ one decides the proportion of the next interval of length $\Delta$ given to $A$ and $B$. Over $[k\Delta,k\Delta+\varphi_1\Delta]$ use $A$, and over $[k\Delta+\varphi_1\Delta,(k+1)\Delta]$ use $B$ (Fig. 3). $\varphi_1$ depends on $x(k\Delta)$, $y(k\Delta)$, and on $k$ if the process is finite (p. 226). For small $\Delta$ the process is described by first-order effects. In the limit $\Delta\to0$ a set of differential equations is obtained and used to *define* the continuous process. A continuous policy is then a function $\varphi_1(t)$ (p. 226). That this is the limit of the discrete process is to be shown in the second volume (p. 227).

The method is later applied (p. 227) to: the two-choice problem, the finite-stage two-choice problem, the two-choice problem with nonlinear utility, and the three-choice problem of §13 of Chapter II. (In §6, p. 227, Bellman announces a continued interplay between classical calculus of variations and dynamic programming.)

### §6 Reformulation (p. 227)
At $t=k\Delta$ choose $\varphi_1$, with $\varphi_2=1-\varphi_1$. Use $A$ in the first part of the interval and $B$ in the second.
- With $x$ gold in $A$: probability $1-q_1\varphi_1\Delta$ that $r_1x\varphi_1\Delta$ is mined and the machine is undamaged. With probability $q_1\varphi_1\Delta$ no gold is mined and the machine is irretrievably damaged.
- For $B$ with $y$ gold: probability $1-q_2\varphi_2\Delta$ of obtaining $r_2y\varphi_2\Delta$, and probability $q_2\varphi_2\Delta$ that operation ceases.

The problem is to maximise the expected gold mined before the machine is damaged (p. 227).

### §7 Derivation of the differential equations (pp. 227–228)
Permuting the order of operations inside an interval is a second-order effect for small $\Delta$. This lets mixing over intervals do the work of mixing at a point (p. 227). A policy is a sequence $\{\varphi_1(k\Delta)\}$. Define, for a given policy:
- $x(t)$ and $y(t)$: gold left in $A$ and $B$ if operation has continued to $t$;
- $p(t)$: probability the machine survives to $t$;
- $f(t)$: expected gold mined up to $t$.

Ignoring second-order terms in $\Delta$ (p. 228):
$$\begin{aligned}x(t+\Delta)&=x(t)-r_1\varphi_1(t)x(t)\Delta,\\ y(t+\Delta)&=y(t)-r_2\varphi_2(t)y(t)\Delta,\\ p(t+\Delta)&=p(t)\big(1-q_1\varphi_1(t)\Delta-q_2\varphi_2(t)\Delta\big),\\ f(t+\Delta)&=f(t)+\Delta\,p(t)\,[\varphi_1(t)r_1x(t)+\varphi_2(t)r_2y(t)].\end{aligned}\tag{1}$$

Letting $\Delta\to0$:
$$\begin{aligned}dx/dt&=-\varphi_1r_1x, & x(0)&=x_0,\\ dy/dt&=-\varphi_2r_2y, & y(0)&=y_0,\\ dp/dt&=-p\,[\varphi_1q_1+\varphi_2q_2], & p(0)&=1,\\ df/dt&=p\,[\varphi_1r_1x+\varphi_2r_2y], & f(0)&=0.\end{aligned}\tag{2}$$

These are taken as the defining equations of the process. The problem is to choose $\varphi_1(t)$ with
$$0\le\varphi_1(t)\le1,\quad \varphi_2=1-\varphi_1\tag{3}$$
so as to maximise $f(T)$. The case $T=\infty$ is of particular importance (p. 228).

### §8 The variational procedure (pp. 228–229)
Let $\varphi_i$ be maximising functions. A footnote says the maximum is attained, as an easy consequence of the uniform boundedness of $\varphi_1(t)$. Set
$$\bar\varphi_i=\varphi_i+\varepsilon\beta_i(t),\tag{1}$$
with $\varepsilon>0$ small and $\beta_i$ functions of $t$ satisfying
$$0\le\varphi_i+\varepsilon\beta_i\le1,\qquad \beta_1+\beta_2=0\tag{2}$$
(so $|\beta_i|\le1/\varepsilon$ and the $\bar\varphi_i$ are admissible). Hence $\beta_i\le0$ where $\varphi_i=1$, $\beta_i\ge0$ where $\varphi_i=0$, and $\beta_i$ can have either sign where $0<\varphi_i<1$ (p. 229).

Performing the variation (bars denote perturbed variables), with $B_i(t)=\int_0^t\beta_i(s)\,ds$ (4):
$$\begin{aligned}\bar x&=x(1-\varepsilon r_1B_1)+o(\varepsilon),\quad \bar y=y(1-\varepsilon r_2B_2)+o(\varepsilon),\\ \bar p&=p(1-\varepsilon q_1B_1-\varepsilon q_2B_2)+o(\varepsilon),\end{aligned}$$
$$\bar f(T)-f(T)=\varepsilon\!\int_0^T\!\{-f'(q_1B_1+q_2B_2)+r_1B_1\,p\,x'+r_2B_2\,p\,y'+r_1\beta_1\,p\,x+r_2\beta_2\,p\,y\}\,dt+o(\varepsilon).\tag{3}$$

Integrating by parts to remove the $B_i$:
$$\bar f(T)-f(T)=\varepsilon\!\int_0^T[K_1\beta_1+K_2\beta_2]\,dt+o(\varepsilon)\tag{5}$$
$$K_i(t)=-q_i\!\int_t^T f'(s)\,ds+r_i\,p(T)\,\xi_i(T)-r_i\!\int_t^T p'(s)\,\xi_i(s)\,ds,\tag{6}$$
where $\xi_1=x$ and $\xi_2=y$ (the author writes $K_1,K_2$ out separately). Since $\bar f(T)-f(T)\le0$, whenever $K_i(t)>K_j(t)$ we must have $\varphi_i(t)=1$, $\varphi_j(t)=0$. These relations are implicit equations for the $\varphi_i$ (p. 229).

*Intuition note.* $K_i(t)$ measures how much the final return would rise if a little more time at $t$ were given to choice $i$, accounting for the future effects on gold and survival. The better choice at each moment takes all the time. A split is possible only where the two are tied.

### §9 The behavior of $K_i$ (p. 230)
The fundamental relation is
$$\frac{d}{dt}(K_1-K_2)=(q_1-q_2)f'(t)-p'(t)(r_2y-r_1x)=p\,[q_1r_2y-q_2r_1x].\tag{1}$$
(Added step: differentiate (8.6) to get $K_i'=q_if'+r_ip'\xi_i$. Then substitute $f'=p[\varphi_1r_1x+\varphi_2r_2y]$, $p'=-p[\varphi_1q_1+\varphi_2q_2]$, and use $\varphi_1+\varphi_2=1$.)

A "mixed policy" (more than one $\varphi_i>0$ at a given $t$, which implies $K_1=K_2$) can therefore be optimal only on the line $q_1r_2y=q_2r_1x$. This is precisely the limit as $\Delta\to0$ of the discrete boundary of §4. Bellman notes that being led to expect this line from the discrete case made it easy to spot (p. 230, footnote).

If a mixed policy is pursued along the line, the slope $s=y/x$ must stay constant. Since
$$\frac{d}{dt}(y/x)=y'/x-(x'/x)s=[r_1\varphi_1-r_2\varphi_2]\,s,\tag{2}$$
we need $r_1\varphi_1=r_2\varphi_2$, hence
$$\varphi_1=\frac{r_2}{r_1+r_2},\qquad\varphi_2=\frac{r_1}{r_1+r_2}.\tag{3}$$

### §10 The solution for $T=\infty$ (pp. 230–231)
With infinite time, after any initial actions one faces a problem of the same type with new initial values. Together with homogeneity in $x$ and $y$, this means the decision at any point depends only on the slope $s=y/x$ (p. 230).

1. If $A$ is ever used above the line $q_1r_2y=q_2r_1x$, it is used thereafter. By (9.1) $K_1-K_2$ increases there. Use of $A$ lowers $x$ and leaves $y$ unchanged, which keeps the point above the line (p. 230).
2. Near the $y$-axis, continual $A$ ($\varphi_1=1$) gives $x=x_0e^{-r_1t}$, $y=y_0$, $p=e^{-q_1t}$, $f(t)=\int_0^tr_1x_0e^{-r_1s}e^{-q_1s}ds$, so $f_A(\infty)=r_1x_0/(q_1+r_1)$ (p. 230). Likewise $f_B(\infty)=r_2y_0/(q_2+r_2)$. For $y_0/x_0$ large enough $f_B(\infty)>f_A(\infty)$, so $B$ is used near the $y$-axis (p. 231).
3. $B$ is used all the way down to the line. Above the line no mixed policy is possible. If $A$ were ever used above it, it would be used forever, and that would eventually carry $(x,y)$ into the region near the $y$-axis where $B$ is optimal, which is a contradiction. Symmetrically $A$ is always used below the line. Once the line is reached the point must stay on it, since otherwise $A$ would be used in a $B$-region or vice versa. So the mixture (9.3) is used there (p. 231).

**Theorem 1** (for (7.2), (7.3)): $\max f(\infty)$ is attained by
$$\varphi_1=1\ \text{for}\ q_1r_2y<q_2r_1x;\quad \varphi_2=1\ \text{for}\ q_1r_2y>q_2r_1x;\quad \varphi_1=\tfrac{r_2}{r_1+r_2},\ \varphi_2=\tfrac{r_1}{r_1+r_2}\ \text{for}\ q_1r_2y=q_2r_1x.\tag{2}$$
$\varphi_1,\varphi_2$ are determined almost everywhere, hence essentially unique. The constructive derivation is an alternative existence proof (p. 231).

*Intuition note.* Far from the line, one mine clearly dominates and is mined down. On the line the two are balanced, so the policy splits time in the fixed ratio that keeps them balanced.

### §11 Solution for finite total time (pp. 231–233)
Start from the last policy used. For small $T$,
$$f(T)=\int_0^Tp(s)[\varphi_1r_1x+\varphi_2r_2y]\,ds=r_1x_0\!\int_0^T\!\varphi_1\,ds+r_2y_0\!\int_0^T\!\varphi_2\,ds+o(T).\tag{1}$$
So for small $T$ the maximum takes $\varphi_1=1$ if $r_1x_0>r_2y_0$ and $\varphi_2=1$ if $r_2y_0>r_1x_0$: expected gain dominates when duration is short (p. 231).

If $q_1=q_2$ the lines $r_2y=r_1x$ and $q_1r_2y=q_2r_1x$ coincide and the policy is that for $T=\infty$ (p. 232). For $q_1\ne q_2$, assume without loss of generality that $r_2y=r_1x$ lies above $q_1r_2y=q_2r_1x$. The quadrant splits into regions I (below the lower line), II (between) and III (above the upper line) (Fig. 4). As in §10:
- In I a $B$-policy once used must continue; in II and III the same holds for an $A$-policy.
- In I and II $A$ is used if the remaining time is small enough; in III, $B$.
- Hence $A$ is always used in I and $B$ always in III (p. 232).

An optimal policy never switches from $A$ to $B$. A change at $t_0$ would put the point in I or on the I/II boundary. $B$ would keep it in I, but $A$ is used in I when little time remains, a contradiction. Likewise a mixed policy followed by $B$ cannot occur (p. 232). Six types of solution remain: $A$ always; $B$ always; mixed then $A$; $A$, mixed, then $B$; $B$, mixed, then $A$; $B$ then $A$ (p. 232).

Let $t_0$ be the last change of policy, with $\varphi_1=1$ on $(t_0,T]$. Then
$$x(t)=x(t_0)e^{-r_1(t-t_0)},\ y(t)=y(t_0),\ p(t)=p(t_0)e^{-q_1(t-t_0)},\ f'(t)=p(t_0)e^{-(q_1+r_1)(t-t_0)}r_1x(t_0),\tag{2}$$
and after simplification
$$K_1(t_0)-K_2(t_0)=p(t_0)\,r_1x(t_0)\Big[\Big(1-\frac{q_2}{q_1+r_1}\Big)e^{-(q_1+r_1)(T-t_0)}+\frac{q_2}{q_1+r_1}-\frac{r_2\,y(t_0)}{r_1\,x(t_0)}\Big].\tag{3}$$
For a fixed point in II, the right side is positive for small $T-t_0$ and negative for large $T-t_0$. It vanishes for exactly one value of $T-t_0$, and that zero fixes the changeover time. After it, $A$ is used for the remaining time (p. 233).

### §12 The three-choice problem (pp. 233–234)
The continuous form of the Chapter II §13 problem gives, with $\varphi_3$ the weight of a third choice $C$ (which works both mines, with rates $r_3,r_4$ and breakdown rate $q_3$) (p. 233):
$$\begin{aligned}dx/dt&=-[\varphi_1r_1+\varphi_3r_3]x,\quad dy/dt=-[\varphi_2r_2+\varphi_3r_4]y,\\ dp/dt&=-p[\varphi_1q_1+\varphi_2q_2+\varphi_3q_3],\\ df/dt&=p\,[(\varphi_1r_1+\varphi_3r_3)x+(\varphi_2r_2+\varphi_3r_4)y],\end{aligned}\tag{1}$$
with $x(0)=x_0$, $y(0)=y_0$, $p(0)=1$, $f(0)=0$, and
$$\varphi_1+\varphi_2+\varphi_3=1,\quad\varphi_i\ge0.\tag{2}$$
Only $T=\infty$ is treated. With $\bar\varphi_i=\varphi_i+\varepsilon\beta_i$, $B_i=\int_0^t\beta_i$, the same technique gives
$$\bar f(T)-f(T)=\varepsilon\!\int_0^T(K_1\beta_1+K_2\beta_2+K_3\beta_3)\,dt+o(\varepsilon),\tag{4}$$
$$\begin{aligned}K_1&=-q_1\!\int_t^Tf'\,ds+r_1p(T)x(T)-r_1\!\int_t^Tp'x\,ds,\\ K_2&=-q_2\!\int_t^Tf'\,ds+r_2p(T)y(T)-r_2\!\int_t^Tp'y\,ds,\\ K_3&=-q_3\!\int_t^Tf'\,ds+p(T)[r_3x(T)+r_4y(T)]-\int_t^Tp'(s)[r_3x(s)+r_4y(s)]\,ds.\end{aligned}\tag{5}$$

### §13 Lemmas and preliminary results (pp. 234–235)
All statements hold almost everywhere.
- **Lemma 1.** If $K_i(t)>K_j(t)$ then $\varphi_i=1$ or $\varphi_j=0$. *Proof:* let $E$ be the set where this fails. Take $\beta_i=1$, $\beta_j=-1$ on $E$ and zero elsewhere. The variation is admissible for small $\varepsilon$ and makes $\bar f(T)-f(T)$ positive if $m(E)>0$ (p. 234).
- **Lemma 2.** If $K_i>K_j$ for all $j\ne i$, then $\varphi_i=1$ (immediate).
- **Lemma 3.** If $K_i<K_j$ for some $j$, then $\varphi_i=0$ (a consequence of Lemma 1) (p. 234).

Derivatives (p. 234):
$$K_1'=p[C_1\varphi_2+C_2\varphi_3],\quad K_2'=p[-C_1\varphi_1-C_3\varphi_3],\quad K_3'=p[-C_2\varphi_1+C_3\varphi_2],\tag{1}$$
$$\begin{aligned}C_1&=q_1r_2y-q_2r_1x,\\ C_2&=q_1r_4y-(q_3r_1-q_1r_3)x,\\ C_3&=(q_3r_2-q_2r_4)y-q_2r_3x.\end{aligned}\tag{2}$$
The relative positions of the lines $C_i=0$ are governed by
$$D=q_1r_2r_3+q_2r_1r_4-q_3r_1r_2.\tag{3}$$
If all three lines lie in the positive quadrant, $D>0$ gives the arrangement of Fig. 5 and $D<0$ that of Fig. 6. Both cases can occur. If $C_2=0$ or $C_3=0$ lies outside the quadrant the arguments simplify without changing the structure, so only the main cases are detailed (p. 235).

### §14 Mixed policies (pp. 235–236)
An $A$-policy means $\varphi_1=1$, a $B$-policy $\varphi_2=1$, a $C$-policy $\varphi_3=1$.

**Lemma 4.** No optimal policy mixes all of $A,B,C$. *Proof:* if $\varphi_1,\varphi_2,\varphi_3>0$ on an interval, then $K_1=K_2=K_3$ there, so
$$K_1'-K_2'=p[C_1\varphi_1+C_1\varphi_2+(C_2+C_3)\varphi_3]=0,\quad K_1'-K_3'=p[C_2\varphi_1+(C_1-C_3)\varphi_2+C_2\varphi_3]=0.\tag{1}$$
If $C_1-C_2-C_3\ne0$ the solution is
$$\varphi_1=\frac{-C_3}{C_1-C_2-C_3},\ \ \varphi_2=\frac{-C_2}{C_1-C_2-C_3},\ \ \varphi_3=\frac{C_1}{C_1-C_2-C_3}.\tag{2}$$
Positivity needs $C_1,-C_2,-C_3$ all of the same sign. Bellman says this "can never occur" in either case $D>0$, $D<0$ (he says it is "easily verified" from figures; the text cites Figs. 2 and 3, see Reading notes; I did not re-derive it). Also $C_1-C_2-C_3=0$ only if the three lines coincide, and then the problem is equivalent to the two-choice problem (p. 236).

**Lemma 5** (mixing exactly two policies) (p. 236):
- (a) $A$–$B$ only along $C_1=0$, with $\varphi_1=r_2/(r_1+r_2)$, $\varphi_2=r_1/(r_1+r_2)$.
- (b) $A$–$C$ only along $C_2=0$, with $\varphi_1=\dfrac{r_4-r_3}{r_1+r_4-r_3}$, $\varphi_3=\dfrac{r_1}{r_1+r_4-r_3}$.
- (c) $B$–$C$ only along $C_3=0$, with $\varphi_2=\dfrac{r_3-r_4}{r_2+r_3-r_4}$, $\varphi_3=\dfrac{r_2}{r_2+r_3-r_4}$.

*Proof of (a):* for $\varphi_1,\varphi_2>0=\varphi_3$ we need $K_1=K_2>K_3$. Then $0=K_1'-K_2'=p[C_1(\varphi_1+\varphi_2)]$, so $C_1=0$. The values of $\varphi$ that keep the point on this line follow as in the two-choice case. The others are obtained similarly (p. 236).

### §15 The solution for $T=\infty$, $D>0$ (pp. 236–240)
Assume $r_3>r_4$. The case $r_4>r_3$ follows by interchanging $x\leftrightarrow y$ and $A\leftrightarrow B$. The case $r_3=r_4$ is treated in §17. When $r_3>r_4$ the mixed $AC$ policy is never used, since by Lemma 5(b) $\varphi_1$ and $\varphi_3$ cannot both be positive (p. 236).

**Lemma 6.** $B$ is used near the $y$-axis. *Proof* (pp. 237):
- Where $C_1>0,C_2>0$ and $A$ is used, $K_1'=0$, $K_2'<0$, $K_3'<0$. So $K_1$ stays largest and $A$ must be pursued thereafter.
- The values of continuing one policy forever are
$$f_A(\infty)=\frac{r_1x_0}{q_1+r_1},\quad f_B(\infty)=\frac{r_2y_0}{q_2+r_2},\quad f_C(\infty)=\frac{r_3x_0}{q_3+r_3}+\frac{r_4y_0}{q_3+r_4}.\tag{1}$$
- $f_B(\infty)>f_A(\infty)$ for $y_0/x_0$ large.
- Above $C_3=0$, if $C$ is used it is used forever. $C$ raises the slope since $s'(t)=s(t)(r_3-r_4)>0$ (2), while $B$ lowers it, so $B$ cannot follow $C$. $A$ cannot follow $C$ near the $y$-axis.
- $B$ beats $C$ near the $y$-axis if $r_2y/(q_2+r_2)>r_4y/(q_3+r_4)$, i.e. $q_3r_2-q_2r_4>0$. This is exactly the condition that $C_3=0$ lies in the positive quadrant, which is assumed.
- So neither $A$ nor $C$ is used near the $y$-axis. No mixture is possible above $C_3=0$ (Lemma 5), so $B$ is used there.

**Lemma 7.** The lower boundary of the $B$-region adjoining the $y$-axis is $C_3=0$. A mixed $BC$-policy is employed on it. Below $C_3=0$, $B$ is never used. *Proof* (pp. 237–238):
- $B$ cannot continue forever, since it would approach the $x$-axis where $A$ is superior ($f_A$ vs $f_B$).
- $A$ and $C$ both raise $y/x$ and would put the point back where $B$ is optimal. So $B$ is followed by a mixed policy.
- If a mixed policy is used on $(t_0,t_1)$, homogeneity makes continuing it forever optimal, because the point stays on the same ray.
- For $D>0$, $AB$ cannot occur. By Lemma 5(a) it would be on $C_1=0$, where $C_2>0$, $C_3<0$, so $K_3'=p[C_3\varphi_2-C_2\varphi_1]<0$. With $K_1(\infty)=K_2(\infty)=K_3(\infty)=0$ and $K_1=K_2=0$ during $AB$, this gives $K_3>K_1=K_2$ and hence $\varphi_3=1$, a contradiction.
- Hence $BC$ follows $B$ on $C_3=0$.

**Lemma 8.** There is a line $L=0$ between $C_2=0$ and the $x$-axis such that $C$ is used between $C_3=0$ and $L=0$, and $A$ below $L=0$. *Proof* (pp. 238–239):
- Below $C_3=0$ only $A$ and $C$ can occur. Both raise the slope exponentially, so the point eventually reaches $C_3=0$, where $BC$ is used.
- When only $C$ or $A$ is used, $K_1'-K_3'=pC_2[\varphi_1+\varphi_3]$. This is positive above $C_2=0$ and negative below.
- A change $C\to A$ needs $K_1'-K_3'\ge0$, so it cannot occur below $C_2=0$. A change $A\to C$ cannot occur above $C_2=0$.
- $A\to BC$ is impossible: above $C_2=0$, $K_1-K_3$ is positive and increasing, but $BC$ needs $K_3>K_1$. So $A$ cannot be used above $C_2=0$, since $BC$ must be reached eventually.
- $A\to C$ cannot occur on $C_2=0$: there $K_1=K_3$, and $C$ moves the point above $C_2=0$ where $K_1'-K_3'>0$, so $K_1>K_3$ and $A$ would be needed.

Two cases remain: (1) $C$ is used in the whole region below $C_3=0$; (2) there is a line $L=0$ with $A$ below it and $C$ above.

Case (1) is excluded by contradiction (p. 239). Take $(x_0,y_0)$ below $C_3=0$. Only $C$ and $BC$ are used, so $K_3'=0$ and, since $K_3(\infty)=0$, $K_3(0)=0$. $C$ is preferred, so $0=K_3(0)\ge K_1(0)$. With $t'$ the changeover time from $C$ to $BC$,
$$0\le K_1(\infty)-K_1(0)=\int_0^{t'}pC_2\,dt+\int_{t'}^\infty p\,[C_1\varphi_2+C_2\varphi_3]\,dt.\tag{4}$$
Fix $x_0$ and let $y_0\to0$, so $t'\to\infty$. The second integral tends to zero, since $C_1\varphi_2+C_2\varphi_3$ is uniformly bounded. Using the $C$-policy expressions,
$$\lim_{y_0\to0}\int_0^{t'}e^{-q_3t}\big[q_1r_4y_0e^{-r_4t}-(q_3r_1-q_1r_3)x_0e^{-r_3t}\big]dt\ge0,\tag{5}$$
$$-\int_0^\infty(q_3r_1-q_1r_3)\,x_0\,e^{-(q_3+r_3)t}\,dt=-\frac{q_3r_1-q_1r_3}{q_3+r_3}\,x_0\ge0.\tag{6}$$
This contradicts the assumption that $C_2=0$ passes through the positive quadrant (which means $q_3r_1-q_1r_3>0$).

**Theorem 2.** If $D=q_1r_2r_3+q_2r_1r_4-q_3r_1r_2>0$, the solution maximising $f(\infty)$ subject to (12.1) is given schematically by Fig. 7. From the $y$-axis down: $B$; mixed $BC$ on $C_3=0$; $C$ between $C_3=0$ and $L=0$; $A$ below $L=0$. It does not seem possible to specify $L$ in any simple way (p. 239–240). If $C_3=0$ lies outside the quadrant, the $C$-region extends to the $y$-axis (p. 240).

*Intuition note.* For $D>0$ the third choice pays off in a middle band of ratios. A balanced $B$–$C$ mixture on one line separates that band from the $B$-region near the $y$-axis. The lower edge of the band is found only implicitly.

### §16 $D<0$ (pp. 240–241)
Here $C$ is never used, so the solution has the two-choice form.
- **Lemma 11.** $B$ is used near the $y$-axis (proof "precisely as before").
- **Lemma 12.** The lower boundary of the $B$-region adjoining the $y$-axis is $C_1=0$. There $AB$ is used. Below it $B$ is not used. *Proof:* as for $D>0$, $B$ must be followed by $AB$ or $BC$. $BC$ is impossible for $D<0$: there $K_1'=p[C_1\varphi_2+C_2\varphi_3]<0$ because $C_3=0$ lies below $C_2=0$ and $C_1=0$. With $K_1(\infty)=K_2(\infty)=K_3(\infty)=0$ and $K_2'=K_3'=0$ during $BC$, this gives $K_1>K_2=K_3$, so $\varphi_1=1$, a contradiction (p. 240).
- **Lemma 12 (second so numbered).** $A$ is used in the entire region between $C_1=0$ and the $x$-axis. *Proof:* during $AB$, $K_1'=K_2'=0$ and $K_3'=p[-C_2\varphi_1+C_3\varphi_2]>0$. So $K_3<K_1,K_2$ just before $AB$, and $C$ is not used immediately before $AB$. Below $C_1=0$ next to the line, $A$ is therefore used. Then $K_1'=0$, $K_2'=-pC_1>0$, $K_3'=-pC_2>0$, so $K_1$ is largest for all earlier $t$ and the $A$-region reaches the $x$-axis (pp. 240–241).

**Theorem 3.** If $D<0$, the solution never uses a $C$-policy and has the two-choice form: $B$ above $C_1=0$, $A$ below, with $AB$ on the line (Fig. 8) (p. 241).

### §17 The case $r_3=r_4$ (pp. 241–242)
Some arguments fail because $C$ keeps $y/x$ constant. By (14.3b,c) neither $AC$ nor $BC$ is ever used (p. 241).

*$D<0$:* $C$ is never used. Compare continual $AB$ with continual $C$:
$$f_{AB}(\infty)=\frac{r}{r+s}(x_0+y_0),\qquad r=\frac{r_1r_2}{r_1+r_2},\quad s=\frac{q_1r_2+q_2r_1}{r_1+r_2},\tag{1,2}$$
$$f_C(\infty)=\frac{r_3}{q_3+r_3}(x_0+y_0).\tag{3}$$
$f_{AB}(\infty)>f_C(\infty)$ is equivalent to $D<0$ (pp. 241–242). (The printed denominator of $s$ differs; see Reading notes. Added step: $r(q_3+r_3)>r_3(r+s)\iff rq_3>r_3s\iff q_3r_1r_2>r_3(q_1r_2+q_2r_1)\iff D<0$ with $r_4=r_3$.)

*$D>0$:* no mixed policy occurs. Which of $C_2=0$, $C_3=0$ lie in the quadrant gives different cases. As before, if $C_3=0$ lies in the quadrant, $B$ beats $C$ near the $y$-axis. For the changeover at $t_0$ from $B$ to $C$, for $t>t_0$: $K_3'=0$ and $K_2'=-pC_3$ (p. 242). Also $K_1(t_0)\le K_2(t_0)=K_3(t_0)$. With $K_1(\infty)=K_2(\infty)=K_3(\infty)$ this forces $C_3=0$ for $t\ge t_0$. So $B$ is followed until $C_3=0$ is met, and then $C$ is followed. $C$ plays the role of $BC$. Similarly $A\to C$ occurs on reaching $C_2=0$. If $C_3=0$ is not in the quadrant, $C$ is used up to the $y$-axis. If $C_2=0$ is not, $C$ is used up to the $x$-axis (p. 242).

### §18 Nonlinear utility, two-choice problem (pp. 242–243)
Maximise the expected value of a function $u$ of total return $R$. Bellman finds it surprising, given the lack of results in the discrete case, that for every strictly increasing $u$ with continuous derivative the optimal policy is precisely that of the linear problem. He says this should warn the unwary that continuous versions need close attention to the approximation they afford (p. 242). Since a monotone-increasing utility can be approximated arbitrarily closely by such a function, the policy is optimal for any monotone-increasing utility, though not necessarily unique (p. 242).

An important example is the step utility
$$u(R)=0\ (0\le R<R_0),\qquad u(R)=1\ (R\ge R_0),\tag{1}$$
whose expected value is the probability that $R\ge R_0$ (p. 243). The equations are (7.2) without $f$. Let $z(t)=x_0+y_0-x(t)-y(t)$, the gold mined up to $t$ if the machine has survived. The expected utility is
$$G=-\int_0^\infty u(z(t))\,dp(t),\tag{3}$$
because we are paid for the total gold mined up to the time of damage. We maximise $G$ over $0\le\varphi_i\le1$, $\varphi_1+\varphi_2=1$. The same perturbation gives
$$\bar G-G=\varepsilon\!\int_0^\infty[K_1\beta_1+K_2\beta_2]\,dt+o(\varepsilon),\tag{5}$$
$$K_1=q_1p(t)u(z(t))-\!\int_t^\infty\!\big[p'(s)u'(z(s))\,r_1x(s)-q_1p'(s)u(z(s))\big]ds,\tag{6}$$
$K_2$ analogously with $r_2y$ and $q_2$, and
$$K_1'(t)-K_2'(t)=p(t)\,u'(z(t))\,[q_1r_2y(t)-q_2r_1x(t)].\tag{7}$$
If $u'(z)>0$ for $z>0$, the arguments and results of the linear case carry over with very slight modifications (p. 243).

*Intuition note.* The sign of $K_1'-K_2'$ is still set by the same line, because $u'>0$ only rescales it. So the geometry of the optimal policy does not change.

### Bibliography and comments (p. 244)
Results are in collaboration with R. S. Lehman (Bellman–Lehman, *Proc. Nat. Acad. Sci.* 1954, and an unpublished paper). Doob's *Stochastic Processes* is named as the basis for a rigorous theory (§3). Mixing over small intervals was used by Bellman–Blackwell in simple two-person poker games (§5). Convergence of the discrete to the continuous process is treated by H. Osborn in RAND reports (§5).

## Toy example (ours, not from the text)
Take the two-choice problem with $r_1=2$, $r_2=1$, $q_1=q_2=1$, start $(x_0,y_0)=(1,2)$.
- The line $q_1r_2y=q_2r_1x$ is $y=2x$, and $(1,2)$ lies on it. Theorem 1 gives $\varphi_1=r_2/(r_1+r_2)=1/3$, $\varphi_2=2/3$.
- Slope check: $r_1\varphi_1=2/3=r_2\varphi_2$, so $y/x$ stays $2$. Both $x$ and $y$ decay at rate $2/3$: $x=e^{-2t/3}$, $y=2e^{-2t/3}$.
- Survival: $dp/dt=-p(\varphi_1q_1+\varphi_2q_2)=-p(1/3+2/3)=-p$, so $p=e^{-t}$.
- $f'=p[\varphi_1r_1x+\varphi_2r_2y]=e^{-t}[(2/3)e^{-2t/3}+(2/3)\cdot2e^{-2t/3}]=2e^{-5t/3}$. Hence $f(\infty)=2/(5/3)=1.2$.
- Pure $A$: $r_1x_0/(q_1+r_1)=2/3\approx0.667$. Pure $B$: $r_2y_0/(q_2+r_2)=2/2=1$.

The mixture (1.2) beats both pure policies. This shows only that mixing helps here. Optimality is the content of Theorem 1.

## Concepts
- [[policy]] — here a function $\varphi_1(t)\in[0,1]$, the fraction of time given to choice $A$ (p. 226).
- [[mixing-at-a-point]] (new) — allowing a blend of decisions at each instant, realised as mixing over small intervals of length $\Delta$ (p. 226).
- [[bellman-equation-value-function]] — the functional equation (5.1 of Chapter II) for the optimal expected return $f(x,y)$; its small-$\delta$ limit is (2.3) (p. 223).
- [[hamilton-jacobi-bellman-equation]] — the limiting first-order equation (2.3) is of this kind (canon link; not named in this unit). Bellman rejects it as the working route (p. 223).
- [[switching-function-K]] (new) — $K_i(t)$, the first-variation coefficients; $K_i>K_j$ forces $\varphi_i=1$ (p. 229).
- [[mixed-policy-singular-line]] (new) — a policy with more than one $\varphi_i>0$; only possible where $K$'s are equal, i.e. on a line (p. 230).
- [[homogeneity-slope-reduction]] (new) — for $T=\infty$ the decision depends only on $s=y/x$ (p. 230).
- [[principle-of-optimality]] — the continuation of an optimal policy is optimal, used in §11 (p. 231).

## Canonical instances
- [[gold-mining-problem]] — machine mined in two (or three) ways with breakdown risk; continuous version solved here (pp. 223, 227).
- [[two-choice-optimal-policy]] — Theorem 1: $A$ below, $B$ above, mixture on $q_1r_2y=q_2r_1x$ (p. 231).
- [[three-choice-optimal-policy]] — Theorems 2 and 3, depending on the sign of $D$ (pp. 239–241).
- [[step-utility-probability-of-target]] — $u(R)=1$ if $R\ge R_0$ else $0$ (p. 242).

## Bridges (candidates)
- [structural-analogy] $K_i(t)$ switching functions and the mixed line ↔ control-theory: costates, bang-bang control and singular arcs in the Pontryagin maximum principle — the sign of $K_i-K_j$ selects the control; equality allows an intermediate control.
- [structural-analogy] Replacing a non-existent maximiser by a "mixture" ↔ control-theory: relaxed controls / chattering — a limit of finer and finer switching is itself admitted as a control.
- [metaphor] The staircase-to-diagonal limit of §4 ↔ sliding-mode behaviour in switching control — finer switching approximates motion along a line.
- [structural-analogy] Equation (2.3) as the limit of a Bellman recursion ↔ control-theory: Hamilton–Jacobi–Bellman equation — Bellman himself compares his intermediate approach to the heat equation versus Chapman–Kolmogorov (p. 224).

## Questions this raises
- Under what exact conditions is the solution of the continuous mixed-policy problem the limit of the discrete problem (promised for volume 2)?
- Why does a nonlinear increasing utility change nothing in the two-choice continuous problem, yet cause trouble in the discrete one?
- How can the line $L=0$ separating $C$ from $A$ (Theorem 2) be determined, since Bellman says no simple form seems available?
- What happens in the three-choice problem for finite $T$, or for $D>0$ with $C_2=0$ or $C_3=0$ outside the quadrant?

## Reading notes
- Printed page = pdf page − 23 (pdf 245 = p. 222). The unit includes the chapter's bibliography (p. 244).
- OCR text of many equations was garbled. I checked equations against the page images.
- Cross-references that seem off in print:
  - §5 (p. 226) says the differential equations are derived "in the next chapter", but they are derived in §7 of this chapter. The solved problems listed there also appear in this chapter.
  - In §14 (p. 236) "Figs. 2 and 3" for the arrangements of the lines $C_i=0$ presumably means Figs. 5 and 6. Similar loose "cf. Fig. 2 / Fig. 7" citations appear in §15–§16.
  - Lemma numbering: two lemmas are numbered 12, and 9–10 are missing (11, 12, 12 in §16). The theorem of §16, called Theorem 3 here, is printed as "Theorem 8" (p. 241).
- Possible misprints:
  - In (15.1) the first denominator of $f_C(\infty)$ looks printed as $q_2+r_3$. Direct computation gives $q_3+r_3$, which I used (it is also consistent with (17.3) and the condition $q_3r_2-q_2r_4>0$).
  - In (17.2) the denominator of $s$ appears printed as $r_1r_2$. The computation from the mixed policy gives $r_1+r_2$, which is needed for "equivalent to $D<0$".
  - In (17.4) the printed $K_1'$ appears as $-C_2$. From (13.1) with $\varphi_3=1$, $K_1'=pC_2$. I used the latter.
  - In (18.2) the first line appears printed with $\varphi_2$ where $\varphi_1$ is expected.
  - In (18.6) the lower limit of the $K_1$ integral looks printed as $0$; I wrote $t$, as in $K_2$.
- Bellman's proofs use the figures for sign facts about the $C_i$; I did not re-derive these signs.
