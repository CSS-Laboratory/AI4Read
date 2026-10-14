---
id: bellman-1957-dp/ch07-vii
work: bellman-1957-dp
unit: "Chapter VII. Bottleneck Problems: Examples"
pages: 207-221
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Bottleneck Problems: Examples (Auto–Steel Production)

## L0 — One line
A two-industry (auto/steel) production problem with capacity bottlenecks is solved completely by building, case by case, a dual "w-solution" that can be paired with a feasible policy, which then proves the policy optimal; impulses at time 0 are sometimes needed.

## L1 — The gist (≤ 120 words)
Can the continuous multi-stage production theory of Chapter VI give explicit solutions? Bellman works one example. Two lumped industries have four state variables (stockpiles and capacities of autos and steel). Steel is allocated at each instant to make autos or to raise either capacity, so as to maximise autos at time $T$. The solution splits into cases by horizon $T$ (planning period) and initial data. Each policy is proved optimal by constructing a dual solution (a bound on the best possible value) that is "paired" with it. Impulses (delta functions) at $t=0$ are sometimes needed. A priority rule summarises the result. Bellman stresses that the analysis is hard and the problems are not "tamed."

**Prerequisites:** linear-programming duality (weak duality, complementary slackness); first-order linear ODEs and exponentials; integrals; the idea of a delta (impulse) function.

## L2 — Key ideas (5–10 bullets)
- The model has four states (auto/steel stockpile and capacity) and four rates $z_i$. Steel is the resource that is allocated (no steel is needed to make steel), and capacities are bottleneck constraints $z_1\le x_2$, $z_3\le x_4$ (pp. 207–208).
- The problem is a continuous linear program with an explicit dual. Weak duality says the primal value is at most the dual value. A feasible $z$ and a dual $w$ that give equal values are "paired," so $z$ is optimal (pp. 209–210).
- Optimality is stated as complementary-slackness conditions (a variable may be positive only where its partner is tight) between $z_i$ and the slacks $l_i$ (the left-hand sides of the dual inequalities), and between $w_i$ and the constraints (p. 210).
- Because $z_2,z_4$ have no upper bound, $Z$ and $W$ are enlarged with delta functions. Only impulses at $t=0$ are ever needed for an optimal $z$, and impulses in $w$ (a delta in $w_3$) appear in the modified and short-time solutions (pp. 211, 214, 217).
- The optimal policy is found by constructing dual solutions (basic, modified, equilibrium, short-time) with $w_4,w_2$ exponential (constant in the short-time case) and matching each to a policy (pp. 211–217).
- Four main cases (I–IV), ten subcases in all, depend on $T$ relative to the critical times $t_0,t_1$ and to $b_4$, and on the initial data. Each policy is paired with one of the four $w$-solutions (pp. 218–220).
- Summary: after an initial adjustment, a priority rule gives steel first to steel capacity, then to autos; steel left over goes to steel capacity until $t_0$ and to auto capacity afterwards (p. 221).

## L3 — Walkthrough

### §1 Introduction (pp. 207–209)
- Aim: show by detailed work that the dynamic-programming approach gives explicit analytic solutions. Bellman says the analysis is "decidedly difficult" and the problems are not "tamed" (p. 207).
- States: $x_1$ auto stockpile, $x_2$ auto capacity, $x_3$ steel stockpile, $x_4$ steel capacity (p. 207).
- Steel is allocated to (a) making autos, (b) raising auto capacity, (c) raising steel capacity. Only $x_1(T)$ is maximised; (b) and (c) serve it (pp. 207–208).
- Assumptions (p. 208):
  - one unit of capacity makes one unit of stockpile per unit time;
  - $b_1$ steel per unit of autos, $b_2$ per unit of auto capacity, $b_4$ per unit of steel capacity;
  - no steel is needed to make steel;
  - no time lag between allocation and capacity increase (lag problems are "an order of magnitude more difficult").
- Controls: $z_1$ auto production, $z_2$ auto-capacity growth, $z_3$ steel production, $z_4$ steel-capacity growth (p. 208).
$$\dot x_1=z_1,\quad \dot x_2=z_2,\quad \dot x_3=z_3-b_1z_1-b_2z_2-b_4z_4,\quad \dot x_4=z_4,\qquad x_i(0)=c_i \tag{1.4}$$
- Constraints (1.5), p. 208: $z_1\le x_2$; $z_3\le x_4$; $z_i\ge0$ (no scrapping); $x_3\ge0$ (no borrowing). The first two are the bottleneck constraints.
- With no upper bound on $z_2,z_4$, delta functions are needed (p. 209).

### §2 Preliminaries (pp. 209–210)
- The system is equivalent to integral inequalities (p. 209):
$$z_1(t)-\int_0^t z_2\,ds\le c_2,\qquad \int_0^t(-z_3+b_1z_1+b_2z_2+b_4z_4)\,ds\le c_3,\qquad z_3(t)-\int_0^t z_4\,ds\le c_4 \tag{2.1}$$
- General problem: $Z$ is the set of $z(t)\ge0$ with $Bz(t)+\int_0^tCz(s)ds\le c$. Maximise $\int_0^T(z,a)\,dt$. $W$ is the set of $w(t)\ge0$ with $B'w(t)+C'\int_t^Tw(s)ds\ge a$. The dual problem minimises $\int_0^T(w,c)\,dt$ over $W$ (p. 209).
- Weak duality (from Chapter 4 §11), p. 210:
$$\int_0^T(z,a)\,dt\le\int_0^T(w,c)\,dt \tag{2.5}$$
- If equality holds for some $z\in Z$, $w\in W$, they give the max and min. Such $z,w$ are called **paired**. So a $z\in Z$ is optimal if it can be paired with some $w\in W$ (a sufficient condition) (p. 210).
- Here (p. 210; $a$ must have four components, see Reading notes):
$$B=\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&1&0\end{pmatrix},\quad C=\begin{pmatrix}0&-1&0&0\\ b_1&b_2&-1&b_4\\0&0&0&-1\end{pmatrix},\quad a=(1,0,0,0)'. \tag{2.6}$$
Shapes: $B,C$ are $3\times4$, $z$ is $4\times1$, $c=(c_2,c_3,c_4)'$.
- Dual inequalities, with components $w_2,w_3,w_4$ matching $z_1\le x_2$, $0\le x_3$, $z_3\le x_4$ (p. 210):
$$\begin{aligned}l_1&\equiv w_2(t)+b_1\!\int_t^T\!w_3\,ds-1\ge0\\ l_2&\equiv-\!\int_t^T\!w_2\,ds+b_2\!\int_t^T\!w_3\,ds\ge0\\ l_3&\equiv w_4(t)-\!\int_t^T\!w_3\,ds\ge0\\ l_4&\equiv b_4\!\int_t^T\!w_3\,ds-\!\int_t^T\!w_4\,ds\ge0\end{aligned}\tag{2.7}$$
- The optimality conditions, i.e. the conditions that equality hold in (2.5), are (p. 210):
  - $z_i>0\Rightarrow l_i=0$ $(i=1,\dots,4)$;
  - $z_1<x_2\Rightarrow w_2=0$;
  - $x_3>0\Rightarrow w_3=0$;
  - $z_3<x_4\Rightarrow w_4=0$. (2.8)
- Equivalent form (2.9): $l_i>0\Rightarrow z_i=0$; $w_2>0\Rightarrow z_1=x_2$; $w_3>0\Rightarrow x_3=0$; $w_4>0\Rightarrow z_3=x_4$.

*Intuition note.* $w$ acts like a price on each constraint. If a feasible plan and a set of prices give the same total, no other plan can do better. Each piece of the plan must also "fit" the prices: a resource with positive price is fully used, and an activity with positive net cost is not run.

### §3 Delta functions (p. 211)
- Over integrable functions only, $Z$ and $W$ may have no solutions. Bellman says this is the usual case here (p. 211).
- Fix: enlarge $Z$ and $W$ with delta functions. $\omega\delta(t-t_0)$ is defined by $\int_0^t\omega\delta(s-t_0)\varphi(s)ds=0$ for $t<t_0$ and $=\omega\varphi(t_0)$ for $t>t_0$ (for $\varphi$ continuous at $t_0$) (p. 211).
- Rigour can come from Stieltjes integrals or from completing the space of integrable functions (p. 211).
- The optimality conditions stay the same. Violations at isolated points or on sets of measure zero do no harm when only measurable functions are allowed as components of $z$ and $w$, but if $w_i$ has a delta at $t_0$ then the matching condition must hold at $t_0$ (p. 211).
- Only deltas at $t=0$ are needed to obtain an optimal $z$: discontinuous changes are not necessary except at the beginning (p. 211).

### §4 The solution (pp. 211–214)
- Method: construct $w$-solutions, guided by "guesswork" and by properties an optimal $z$ should have, and pair each with a $z$ (p. 211).
- Always take $z_3=x_4$ (too much steel is harmless). So $l_3\equiv0$ and $w_4(t)=\int_t^Tw_3\,ds$ (pp. 211–212). Then (p. 212):
$$l_1=w_2+b_1w_4-1,\quad l_2=b_2w_4-\!\int_t^T\!w_2\,ds,\quad l_4=b_4w_4-\!\int_t^T\!w_4\,ds\tag{4.1}$$
- Near $T$, $z_1>0$, so $l_1=0$ there. Basic $w$-solution: also $l_2=0$ near the end, with $w_4(T)=0$ (p. 212):
$$w_4(t)=\tfrac1{b_1}\bigl(1-e^{-b_1(T-t)/b_2}\bigr),\qquad w_2(t)=e^{-b_1(T-t)/b_2},\tag{4.2}$$
with $w_2,w_3,w_4$ positive as $t$ decreases. Then
$$l_4=\tfrac{b_4}{b_1}\bigl(1-e^{-b_1(T-t)/b_2}\bigr)-\tfrac{T-t}{b_1}+\tfrac{b_2}{b_1^2}\bigl(1-e^{-b_1(T-t)/b_2}\bigr)\tag{4.3}$$
This is positive for $T-t$ small and negative for $T-t$ large. Its zero $t_0$ solves (p. 212)
$$T-t_0=\bigl(b_4+\tfrac{b_2}{b_1}\bigr)\bigl(1-e^{-b_1(T-t_0)/b_2}\bigr).\tag{4.4}$$
- At $t_0$ one of the equations $l_1=0$, $l_2=0$ must be abandoned. Bellman tries $l_1=0$ and $l_4=0$ before $t_0$ (so $l_2=0$ is dropped), i.e. take $l_1=0$, $l_4=0$ (p. 212):
$$w_4(t)=w_4(t_0)e^{(t_0-t)/b_4},\quad w_2(t)=1-b_1w_4(t_0)e^{(t_0-t)/b_4}\tag{4.5}$$
$$\frac{dl_2}{dt}=b_2\frac{dw_4}{dt}+w_2=1-\bigl(b_1+\tfrac{b_2}{b_4}\bigr)w_4(t_0)e^{(t_0-t)/b_4}\tag{4.6}$$
- $l_2\ge0$ is ensured if $dl_2/dt\le0$ for $t\le t_0$. This holds if $w_4(t_0)\ge b_4/(b_2+b_1b_4)$ (4.7), which by (4.2) and (4.4) is equivalent to $T-t_0\ge b_4$. That is checked by putting $b_4$ for $T-t$ in (4.3):
$$\tfrac1{b_1}\Bigl[\bigl(b_4+\tfrac{b_2}{b_1}\bigr)(1-e^{-b_1b_4/b_2})-b_4\Bigr]=\tfrac{b_2}{b_1^2}e^{-b_1b_4/b_2}\Bigl[e^{b_1b_4/b_2}-\bigl(1+\tfrac{b_1b_4}{b_2}\bigr)\Bigr]>0\tag{4.8}$$
so $l_2\ge0$ for $t\le t_0$ (p. 213).
- $w_2$ stays positive until it hits zero at $t_1$ (p. 213):
$$e^{(t_0-t_1)/b_4}=\frac{b_4+b_2/b_1}{T-t_0}.\tag{4.9}$$
- Before $t_1$ take $w_2=0$ and keep $l_4=0$. Then $dl_2/dt=b_2dw_4/dt<0$ and $dl_1/dt=b_1dw_4/dt<0$, so $l_1,l_2>0$ (p. 213).
- **Basic solution (Fig. 1, p. 213).** Any feasible $z$ with these properties is optimal.

| interval | slack $l_i$ and $z$ | $w$ and consequences |
|---|---|---|
| $t<t_1$ | $l_1,l_2>0$ so $z_1=z_2=0$; $l_3=l_4=0$ | $w_2=0$; $w_3>0$ so $x_3=0$; $w_4>0$ so $z_3=x_4$ |
| $t_1<t<t_0$ | $l_1=0$; $l_2>0$ so $z_2=0$; $l_3=l_4=0$ | $w_2>0$ so $z_1=x_2$; $w_3>0$ so $x_3=0$; $w_4>0$ so $z_3=x_4$ |
| $t_0<t<T$ | $l_1=l_2=l_3=0$; $l_4>0$ so $z_4=0$ | $w_2>0$ so $z_1=x_2$; $w_3>0$ so $x_3=0$; $w_4>0$ so $z_3=x_4$ |

- Partial solution for $c_3=0$ (pp. 213–214):
  - for $t<t_1$: $z_1=0$, $z_2=0$, $z_3=x_4$, $z_4=x_4/b_4$ (4.11);
  - for $t_1<t<t_0$: $z_1=x_2$, $z_2=0$, $z_3=x_4$, $z_4=(x_4-b_1x_2)/b_4$ (4.12);
  - for $t_0<t<T$: $z_1=x_2$, $z_2=(x_4-b_1x_2)/b_2$, $z_3=x_4$, $z_4=0$ (4.13).
  - (4.12) can be done iff $x_4(t_1)-b_1x_2(t_1)\ge0$. (4.13) is possible provided $x_4(t_1)-b_1x_2(t_1)\ge0$. So for certain initial conditions we obtain the optimal solution (p. 214); for $x_4(t_1)-b_1x_2(t_1)<0$ Bellman says "we run into trouble" and turns to §5.

*Intuition note.* Late in the horizon, steel goes to autos and to auto capacity; early on, steel goes to growing steel capacity. The switch time $t_0$ is where the slack $l_4$ reaches zero (4.4), and $t_1$ is where $w_2$ reaches zero (4.9).

### §5 The modified $w$ solution (pp. 214–215)
- Needed when $x_4(t_1)-b_1x_2(t_1)<0$ (p. 214). Choose $u_0\in[t_1,T]$.
  - For $t>u_0$, $w$ is as in the basic solution.
  - For $t<u_0$ set $w_2=0$, and near $u_0$ take $w_4=1/b_1$ so $l_1=0$. $u_1$ is the point where $l_4$ becomes 0.
  - For $t<u_1$ choose $w$ with $l_4=0$.
- Then $l_1,l_2>0$, $w_3,w_4>0$ for all $t<u_1$. For $u_0=t_1$, $u_1=t_1$ and the basic solution is recovered. $u_1$ depends continuously on $u_0$. For $u_0=T$, $u_1=T-b_4$. So there is a $w$ solution for each $u_1\in[t_1,T-b_4]$ (p. 214).
- Fig. 2 (p. 214), by interval. The column headers are hard to read; the assignment follows the remark on p. 215.
  - $t<u_1$: $l_1,l_2>0$; $l_4=0$; $w_2=0$; $w_3>0$; $w_4>0$.
  - $u_1<t<u_0$: $l_1=0$; $l_2>0$; $l_4>0$ so $z_4=0$; $w_2=0$; $w_3=0$; $w_4>0$.
  - $u_0<t<t_0$: $l_1=0$; $l_2>0$; $l_4=0$; $w_2>0$ so $z_1=x_2$.
  - last interval: $l_2=0$; $l_4>0$ so $z_4=0$; $w_2>0$ so $z_1=x_2$.
  - Throughout, $z_3=x_4$ where $w_4>0$. Where $w_3>0$ or where $w_3$ is a delta, $x_3=0$. Since $w_3$ is a delta at $u_0$, $x_3(u_0)=0$.
- If $u_0>t_0$ the third column is empty; if $u_0=T$ the last is empty (p. 215).

### §6 The equilibrium solution (pp. 215–217)
- Policy idea: an initial adjustment brings $x_3$ to 0 so that $x_4=b_1x_2$. Afterwards no capacity increase is needed and all steel goes to autos. This needs $l_2(0)=l_4(0)=0$, since $z_2,z_4$ are generally deltas. The basic solution has this property when $t_0=0$ (p. 215).
- Try $w_4(t)=ae^{-b_1(T-t)/b_2}+\beta$ (6.1). With $w_2$ chosen so $l_1=0$ (p. 215):
$$l_2=b_2w_4-(T-t)+b_1\!\int_t^T\!w_4\,ds\ge0,\quad l_4=b_4w_4-\!\int_t^T\!w_4\,ds\ge0\tag{6.2}$$
$l_2(0)=l_4(0)=0$ gives $w_4(0)=T/(b_2+b_1b_4)$ (6.3).
- With $E=e^{-b_1T/b_2}$, (6.1)–(6.3) give (p. 215)
$$b_2a+(b_2+b_1T)\beta=T,\qquad (b_2+b_1b_4)Ea+(b_2+b_1b_4)\beta=T\tag{6.4}$$
$$a=\tfrac{T}{\Delta}\,b_1(b_4-T),\qquad \beta=\tfrac{T}{\Delta}\bigl[b_2(1-E)-b_1b_4E\bigr]\tag{6.5}$$
$$\Delta=(b_2+b_1b_4)(b_2-b_2E-b_1ET)\tag{6.6}$$
$$\Delta=(b_2+b_1b_4)E\,(b_2e^{b_1T/b_2}-b_2-b_1T)>(b_2+b_1b_4)E(b_2+b_1T-b_2-b_1T)=0\tag{6.7}$$
(the last step uses $e^x>1+x$, an added step) (p. 216).
- Assume $T-t_0\ge T\ge b_4$. Then $a\le0$ by (6.5). We need $0\le w_4\le1/b_1$ and $dw_4/dt\le0$ (this gives $w_2,w_3,w_4\ge0$). $dw_4/dt=a\frac{b_1}{b_2}e^{-b_1(T-t)/b_2}\le0$ (the printed exponent seems to omit the minus sign), so it is enough to check $w_4(T)\ge0$ and $w_4(0)\le1/b_1$ (p. 216):
$$w_4(0)=\tfrac{T}{b_2+b_1b_4}\le\tfrac{T-t_0}{b_2+b_1b_4}<\tfrac{b_4+b_2/b_1}{b_2+b_1b_4}=\tfrac1{b_1}\tag{6.8}$$
$$w_4(T)=a+\beta=\tfrac{T}{\Delta}\,b_1\bigl[(b_4+\tfrac{b_2}{b_1})(1-E)-T\bigr]\ge0\tag{6.9}$$
(Bellman states $\ge0$ without further proof.)
- $l_2$ and $l_4$ (p. 216):
$$\frac{dl_2}{dt}=b_2\frac{dw_4}{dt}+1-b_1w_4(t)=1-b_1\beta\tag{6.10}$$
and $l_2(T)=b_2w_4(T)\ge0$, so $l_2\ge0$ on $[0,T]$ (since $l_2(0)=0$ and $l_2$ is linear, an added step). $l_4(T)=b_4w_4(T)\ge0$, so $l_4\ge0$ follows if $d^2l_4/dt^2\le0$. Printed (6.11): $d^2l_4/dt^2=a(b_4+b_2/b_1)(b_1/b_2)^2$ and the printed relation at the end is $\ge0$, which does not fit $a\le0$ (see Reading notes).
- **Fig. 3 (p. 217), valid only for $T\ge b_4$:** at $t=0$, $l_2=l_4=0$. On $0<t<T$: $l_1=l_3=0$; $l_2,l_4>0$ so $z_2=z_4=0$; $w_2>0$ so $z_1=x_2$; $w_3>0$ so $x_3=0$; $w_4>0$ so $z_3=x_4$.

*Intuition note.* If the system starts "balanced" ($x_3=0$, $x_4=b_1x_2$), steel capacity just supports auto production at capacity, so nothing more should be built. The dual check is that the slack prices $l_2,l_4$ stay positive after $t=0$.

### §7 A short-time $w$ solution (p. 217)
- For $T<b_4$. This solution allows $x_3>0$ and $z_2$ to be a delta at 0.
- Take $w_4=\gamma$, $w_2=1-b_1\gamma$ on $[0,T]$, $0<\gamma<1/b_1$. Then $l_1=0$, $l_4>0$ for $0\le t<T$, and
$$l_2=b_2\gamma-(T-t)(1-b_1\gamma)=[b_2+b_1(T-t)]\gamma-(T-t).\tag{7.1}$$
- Choosing $\gamma=T/(b_2+b_1T)$ gives $l_2(0)=0$ and $l_2(t)>0$ for $t>0$.
- **Fig. 4 (p. 217), valid for $T<b_4$:** $l_1=l_3=0$; $l_2,l_4>0$ so $z_2=z_4=0$; $w_2>0$ so $z_1=x_2$; $w_4>0$ so $z_3=x_4$; $w_3=0$ on $(0,T)$ and a delta at $T$, so $x_3(T)=0$.

### §8 Description of the solution and proof (pp. 218–221)
- The critical times $t_0$ (4.4) and $t_1$ (4.9) depend on $T$, but $T-t_0$ and $T-t_1$ are constants for fixed $b$'s (p. 218).
- **Case I ($t_1\ge0$).** $z_4$ is a delta at 0 that brings $x_3$ to 0. This is allowed since $l_4=0$ near 0. For $0<t<t_1$: (1) $z_1=z_2=0$, $z_3=x_4$, $z_4=x_4/b_4$ (p. 218).
  - **IA:** $x_4(t_1)-b_1x_2(t_1)\ge0$. Use (4.12) on $[t_1,t_0]$ and (4.13) on $(t_0,T]$. Optimal, paired with Fig. 1 (p. 218).
  - **IB:** $x_4(t_1)-b_1x_2(t_1)<0$. Keep (1) until $x_4-b_1x_2=0$ (at $t'$) or $t=T-b_4$, whichever is first. Then $z_1=x_2$, $z_2=0$, $z_3=x_4$, $z_4=0$. Paired with Fig. 2 with $u_1=t'$, for $t_1<t'\le T-b_4$. If $x_4(T-b_4)-b_1x_2(T-b_4)<0$, then on $(T-b_4,T]$ use $z_1=x_4/b_1$, $z_2=0$, $z_3=x_4$, $z_4=0$, paired with Fig. 2 with $u_0=T$, $u_1=T-b_4$ (pp. 218–219).
- **Case II ($t_1\le0\le t_0$).** Same delta in $z_4$ at 0. IIA: $x_4(0)-b_1x_2(0)\ge0$; IIB: $<0$. IIA: $z_1=x_2$; on $(0,t_0)$, $z_2=0$, $z_4=(x_4-b_1x_2)/b_4$; after $t_0$, $z_4=0$ and $z_2=(x_4-b_1x_2)/b_2$ (the printed (9) shows denominator $b_4$; see Reading notes). Paired with Fig. 1. IIB is like IB, paired with Fig. 2 (p. 219).
- **Case III ($t_0\le0\le T-b_4$)** (p. 219), with
  - IIIA: $c_4-b_1c_2\ge b_1c_3/b_2$;
  - IIIB: $c_4-b_1c_2<-c_3/b_4$;
  - IIIC: $-c_3/b_4\le c_4-b_1c_2<b_1c_3/b_2$.
  - IIIA: $z_2$ is a delta at 0 that brings $x_3$ to 0 (stock steel goes to auto capacity). Then $z_1=x_2$, $z_2=(x_4-b_1x_2)/b_2$, $z_3=x_4$, $z_4=0$. Paired with Fig. 1.
  - IIIB: same policy and proof as IB (p. 220).
  - IIIC: $z_2$ and $z_4$ are deltas at 0, so that $x_3=0$ and $x_4=b_1x_2$. Then $z_1=x_2$, $z_2=0$, $z_3=x_4$, $z_4=0$. Paired with the equilibrium solution of Fig. 3 (p. 220).
- **Case IV ($T\le b_4$)** (p. 220), with
  - IVA: $c_4-b_1c_2\ge b_1c_3/b_2$;
  - IVB: $c_4-b_1c_2>-c_3/T$ (as printed);
  - IVC: $-c_3/b_4\le c_4-b_1c_2<b_1c_3/b_2$.
  - IVA: as IIIA.
  - IVB: $z_2=z_4=0$, $z_3=x_4$, and $z_1(t)\le x_2(t)$ chosen so that $x_3(T)=0$. The solution is not unique. Paired with Fig. 2 with $u_0=T$.
  - IVC: an initial jump lowers $x_3$ to $c_3'$ (not to 0), spending the steel on auto capacity. Then $z_1=x_2$, $z_2=0$, $z_3=x_4$, $z_4=0$. With $c_3'$ chosen so that $x_3(T)=0$, printed (13) is
  $$c_3'=\frac{b_1c_3-b_2(c_4-b_1c_2)}{b_2+b_1T}.$$
  Paired with the short-time solution of Fig. 4.
- **Summary of initial adjustments (p. 221):**
  - Rows A (Cases I, II): bring $x_3$ to 0 by increasing $x_4$; (Cases III, IV): bring $x_3$ to 0 by increasing $x_2$ ("build auto capacity").
  - Rows B (I–III): "build steel capacity"; (IV): no initial adjustment.
  - Rows C: no case for I, II. Case III: adjust so $x_3=0$, $x_4=b_1x_2$, by increasing $x_2,x_4$. Case IV: lower $x_3$ but not to 0, so $x_3(T)=0$, and increase $x_2$.
- **Priority rule after the adjustments (p. 221):**
  1. Before $t_1$, $z_4$ (steel capacity) has first priority. This continues after $t_1$ until $x_4\ge b_1x_2$ or $t=T-b_4$, whichever is first (printed "$t=b_4$"; see Reading notes).
  2. Then autos ($z_1$) get first priority. This uses up all steel unless $x_4(t_1)>b_1x_2(t_1)$.
  3. In that case second priority goes to steel capacity until $t_0$, and after $t_0$ to auto capacity.
- Bibliography (p. 221): the results come from work with R. S. Lehman (RAND P-492, 1954).

*Intuition note.* Whether to invest first in steel capacity, in auto capacity, or in nothing depends on how long is left. Short horizons do not repay investment. Long ones favour expanding steel first.

## Toy example (ours, not from the text)
Use the short-horizon case: $b_1=1$, $b_2=1$, $b_4=2$, $T=1<b_4$; $c_1=0$, $c_2=1$, $c_3=1$, $c_4=1$.
- Case: $c_4-b_1c_2=0$. We have $b_1c_3/b_2=1$ and $-c_3/b_4=-0.5$, so $-0.5\le0<1$, which is IVC (the printed IVB test $0>-c_3/T=-1$ would also hold; this is one more reason to suspect its sign is misprinted).
- (13): $c_3'=(1\cdot1-1\cdot0)/(1+1\cdot1)=0.5$. The initial impulse in $z_2$ has size $(c_3-c_3')/b_2=0.5$, so $x_2=1.5$, $x_3=0.5$.
- Then $z_1=1.5$, $z_3=x_4=1$, $z_2=z_4=0$, so $\dot x_3=1-1.5=-0.5$ and $x_3(1)=0.5-0.5=0$ ✓. Autos: $x_1(1)=0+1.5=1.5$.
- Dual check (§7): $\gamma=T/(b_2+b_1T)=1/2$, $w_4=1/2$, $w_2=1-\tfrac12=\tfrac12$. $l_2(t)=(2-t)/2-(1-t)=t/2\ge0$, $l_2(0)=0$; $l_4=\tfrac12(1+t)>0$; $l_1=\tfrac12+\tfrac12-1=0$.
- Dual value $\int_0^T(w,c)dt=w_2c_2T+\gamma c_3+\gamma c_4T=0.5+0.5+0.5=1.5$. Counting the delta of $w_3$ at $T$ with full weight $\gamma$ is our convention. This equals the primal value 1.5, so the policy is paired and optimal.
- Sanity: total steel $=c_3+\int x_4=2$; raising auto capacity by $\delta$ costs $\delta$, and autos cost 1 steel each: $\delta+(1+\delta)=2$ gives $\delta=0.5$ ✓.

## Concepts
- [[state]] — here four numbers $x_1..x_4$: stockpiles and capacities of autos and steel (p. 207)
- [[bottleneck-constraint]] (new) — capacity limits $z_1\le x_2$, $z_3\le x_4$ on production rates (p. 208)
- [[dual-problem-pairing]] (new) — $z\in Z$ and $w\in W$ with equal primal/dual values; sufficient for optimality of $z$ (p. 210)
- [[complementary-slackness-conditions]] (new) — conditions (2.8)/(2.9) linking $z_i$, $l_i$, $w_i$ and the constraints (p. 210)
- [[impulse-control]] (new) — delta functions in $z$ or $w$; here only at $t=0$ for $z$ (p. 211)
- [[priority-policy]] (new) — order in which steel is assigned, derived from the case analysis (p. 221)
- [[delay (dead time)]] — assumed absent: no lag between allocation and capacity (p. 208)

## Canonical instances
- [[auto-steel-bottleneck]] (new) — two-industry model with four states and four allocation rates (pp. 207–208)
- [[lehman-bellman-bottleneck-study]] (new) — source studies cited for these results (p. 221)

## Bridges (candidates)
- [structural-analogy] weak duality and pairing (2.5) ↔ optimisation: LP duality with complementary slackness, in function space — same inequality structure.
- [structural-analogy] dual functions $w_i(t)$ as prices ↔ control-theory: Pontryagin costates (shadow prices) — both certify optimality along the trajectory.
- [structural-analogy] impulse at $t=0$ bringing $x_3$ to 0 ↔ impulse control: instantaneous jumps in state when controls are unbounded.

## Questions this raises
- How does the solution change if an allocation-to-capacity time lag is added (the author calls it an order of magnitude harder)?
- Can the guesswork in constructing $w$ be systematised for larger systems, such as three industries?
- Which ingredients of the cases (e.g., $t_0$, $t_1$) generalise to other investment models with capacity bottlenecks?

## Reading notes
- Printed = pdf − 23 (e.g., pdf 230 = printed 207).
- The vector $a$ in (2.6) appears with three entries in the image; $z$ has four components, so $a=(1,0,0,0)'$ is our inference.
- (4.2): the second line of the printed (4.2) is $w_2(t)=e^{-b_1(T-t)/b_2}$ (the text layer misreads it as $w_3$).
- §5: the image reads $w_4(t)=1/b_1$ (the text layer shows a spurious prime); this is what $w_2=0$, $l_1=0$ requires.
- The Fig. 2 column headers are garbled; the assignment of columns is reconstructed from the remark on p. 215.
- §6: the exponent in $dw_4/dt$ appears to lack its minus sign. At the end of (6.11) the image shows "$\ge0$" (legible); with $a\le0$ the expression is $\le0$, which the proof needs. In (6.11) the factor $e^{-b_1(T-t)/b_2}$ also seems to be missing.
- (8.9): the printed denominator is $b_4$; $b_2$ is expected, as in (4.13), (8.4), (8.11).
- (8.12) IVB: the printed inequality is "$>$". Our check (needing $x_3(T)=0$ with $z_1\le x_2$) suggests "$\le$" or "$<$". The formula (13) for $c_3'$ lacks a factor $T$ in the numerator by our own calculation (it agrees when $T=1$, as in the toy example). Neither is confirmed by the text.
- Summary, p. 221: printed "$t=b_4$" should presumably read $t=T-b_4$ (compare §8 Case IB).
- The unit contains no exercises.
