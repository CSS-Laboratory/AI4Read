---
id: spielman-2025-sagt/ch17-monotonicity
work: spielman-2025-sagt
unit: "Chapter 17 — Monotonicity and its Failures"
pages: 147–154
fields: [linear-algebra]
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
# Monotonicity and its Failures

## L0 — One line
In linear spring or resistor networks, weakening an edge can never improve the effective connection between two vertices, but in nonlinear networks (springs with wires) and selfish traffic networks, adding or keeping material can hurt, and a road can make everyone slower.

## L1 — The gist (≤ 120 words)
The chapter defines the effective spring constant and effective resistance between two vertices of a weighted graph. It proves Rayleigh's monotonicity for spring networks by an energy argument. It then shows the intuition failing: a spring-and-wire apparatus rises when a wire is cut, and Braess's paradox in traffic makes everyone slower when a free road is added. It introduces Nash equilibrium (no driver gains by switching routes), the social optimum (lowest average time) and the "price of anarchy" (Nash cost over optimal cost), which is 4/3 in the examples given. It proves that, for linear road costs, every local minimum of the social cost is a global minimum. The traffic material prepares the next lecture.

**Prerequisites:** graph Laplacian $L$ and its pseudoinverse; quadratic form $x^TLx$; Ohm's law; convex functions; basic derivatives.

## L2 — Key ideas (5–10 bullets)
- The effective spring constant between $s$ and $t$ is twice the minimum energy with $x(s)=0$, $x(t)=1$. Scaling the displacement to $y$ multiplies the energy by $y^2$ (pp. 147–148).
- Rayleigh monotonicity: lowering spring constants cannot raise the effective spring constant. Proof: the old minimiser costs no more in the new graph (p. 148).
- Effective resistance is $i_{ext}^TL^+i_{ext}$, the potential difference needed to push one unit of current from $s$ to $t$. It equals $v^TLv$ for the corresponding voltages (p. 149).
- Path resistances add, and parallel conductances add (p. 150).
- With nonlinear elements, monotonicity fails: cutting a wire in a spring–wire network lifts the hanging weight (pp. 150–151).
- In Braess's paradox, adding a zero-cost road moves the Nash equilibrium from cost 3/2 to cost 2 (p. 152).
- The price of anarchy is Nash cost over optimal cost, 4/3 in the examples. The author says the next lecture shows it never exceeds 4/3 for linear costs (pp. 152–153).
- For linear road costs, the social cost is convex in the flow, so local minima are global and the set of minima is convex (p. 153).

## L3 — Walkthrough

### 17.1 Overview
The section is empty in the source.

### 17.2 Effective spring constants (pp. 147–148)
A spring network is a weighted graph $G=(V,E,w)$, with $w_{a,b}$ the spring constant of edge $(a,b)$. The energy of one ordinary spring is spring constant × length² / 2. Fix $s$ at 0 and $t$ at 1. The other vertices then sit where they minimise
$$\mathcal E(x)\stackrel{def}{=}\frac12\sum_{(a,b)\in E}w_{a,b}\,(x(a)-x(b))^2.\tag{17.1}$$
The **effective spring constant** $c_{s,t}$ is defined as twice this minimum (p. 147). If $t$ is fixed at $y$ instead, homogeneity makes $yx$ the minimiser. Its energy is $y^2/2$ times the effective spring constant (p. 148).

*Intuition note:* The whole network acts like one big spring. Its stiffness is read off from the energy needed to stretch it by one unit (the constant is twice that energy).

### 17.3 Monotonicity (p. 148)
**Theorem 17.3.1.** Let $\hat G=(V,E,\hat w)$ have the same edges as $G$, with $\hat w_{a,b}\le w_{a,b}$ for all $(a,b)\in E$. Then $\hat c_{s,t}\le c_{s,t}$.

*Proof (key steps).* Let $x$ minimise the energy in $G$ with $x(s)=0$, $x(t)=1$. Its energy in $\hat G$ is no greater, because no term is larger (each $\hat w_{a,b}\le w_{a,b}$). So the minimum energy in $\hat G$ is at most the minimum in $G$, hence $\hat c_{s,t}\le c_{s,t}$.

*Intuition note:* Weaker springs can only make stretching easier. The old best positions still work, and they now cost no more.

The author says the principle seems obvious but fails in slightly more complicated situations (p. 148).

### 17.4 Effective resistance (pp. 148–149)
Ohm's law is written $i(a,b)=\frac{v(a)-v(b)}{r_{a,b}}$. The weight of an edge is the reciprocal of its resistance. The **effective resistance** is the potential difference needed to flow one unit of current from $s$ to $t$ (p. 149).

Let $i_{ext}(s)=1$, $i_{ext}(t)=-1$, and $i_{ext}(a)=0$ otherwise (added step: this is an $n$-vector, and $L$ is $n\times n$). Solve $Lv=i_{ext}$ by $v=L^+i_{ext}$. Then
$$v(s)-v(t)=i_{ext}^Tv=i_{ext}^TL^+i_{ext}\stackrel{def}{=}R_{\rm eff}(s,t).$$
The author says this agrees with defining it as twice the energy dissipated by one unit of flow (p. 149).

**Theorem 17.4.1.** If $i$ is the electrical flow of one unit from $s$ to $t$, then $R_{\rm eff}(s,t)=\mathcal E(i)$.

*Proof.* Since $i_{ext}=Lv$,
$$R_{\rm eff}(s,t)=i_{ext}^TL^+i_{ext}=v^TLL^+Lv=v^TLv=\mathcal E(v).$$
(added step: the last equality of the matrix part uses $LL^+L=L$.)

**Theorem 17.4.2 (Rayleigh).** Increasing the resistance of some edges cannot decrease the effective resistance between a pair of vertices. The text states it without proof (p. 149).

### 17.5 Examples (p. 150)
- Path with $n$ vertices and unit weights: $R_{\rm eff}=n-1$.
- Path with resistances $r(1,2),\dots,r(n-1,n)$: $R_{\rm eff}=r(1,2)+\dots+r(n-1,n)$. Set $v(i)=r(i,i+1)+\dots+r(n-1,n)$. Ohm's law then gives current $(v(i)-v(i+1))/r(i,i+1)=1$ on each edge.
- $k$ parallel edges with resistances $r_1,\dots,r_k$: $R_{\rm eff}(s,t)=\dfrac{1}{1/r_1+\dots+1/r_k}$. The flow on edge $i$ is $\dfrac{1/r_i}{1/r_1+\dots+1/r_k}$, and these flows sum to 1.

### 17.6 Breakdown of monotonicity (pp. 150–151)
The network has springs and wires (nonlinear elements). Point $a$ is fixed at the top; $d$ carries a weight of 1. There is a spring of constant 1 from $a$ to $b$, a spring of constant 1 from $c$ to $d$, and a very short wire from $b$ to $c$. Each spring carries the weight, so each has length 1, and the distance $a$–$d$ is 2 (p. 150).

Add a wire $a$–$c$ and a wire $b$–$d$, each of length $1+\epsilon$. They are slack, so nothing moves.

Now cut the short wire $b$–$c$. The structure becomes two parallel supports: spring $a$–$b$ then wire $b$–$d$, and wire $a$–$c$ then spring $c$–$d$. Each carries half the weight, so each spring has length 1/2. The distance $a$–$d$ is then essentially $3/2$ (p. 151). The weight goes up. The author says the real measurements are not exactly 2 and 3/2, because ideal springs are hard to find. He also says that with resistors and diodes one can increase flow between two points by cutting a wire (p. 151).

*Intuition note:* Cutting removes a rigid link, so the load is shared by two paths. Each spring now carries only half the weight, so it stretches only to 1/2. The author presents this as a breakdown of monotonicity in a network with nonlinear elements (springs and wires).

### 17.7 Traffic networks (pp. 151–152)
A road is a directed edge. With flow $f$, the traversal time is $af+b$ with $a,b\ge0$ (the road's characteristic function).

**Pigou's example.** Two roads from $s$ to $t$: a slow road with characteristic 1 and a fast road with characteristic $f$. One unit of traffic wants to go from $s$ to $t$. A planner minimises the average time. If $f$ is the fraction on the fast road, the average time is $f\cdot f+(1-f)\cdot1=f^2-f+1$. Setting $2f-1=0$ gives $f=1/2$ and average time 3/4 (half the traffic takes time 1, half takes 1/2) (p. 151).

Selfish drivers behave differently. If fewer than all drivers use the fast road, it is faster than the slow one, so anyone on the slow road would rather switch. The author concludes that all traffic ends up on the fast road, with time 1 (p. 152). This is the **Nash optimal** solution: each driver maximises their own benefit.

### 17.8 Braess's paradox (p. 152)
Start with slow roads $s\to c$ and $d\to t$, and fast roads $s\to d$ and $c\to t$. Half the traffic uses $sct$ and half uses $sdt$. All traffic takes time 3/2, and no one gains by switching, so this is a Nash equilibrium. Now build a road $c\to d$ with characteristic 0. Route $scdt$ looks like time 1 if others stay put. But all traffic switches to it, and everyone now takes 2.

Formally, let $p_1,p_2,p_3$ be the fractions on $sct$, $sdt$, $scdt$. The costs are $p_1+p_3+1$, $p_2+p_3+1$ and $p_3+p_3$, as printed. As long as $p_3<1$, the cheapest route is $scdt$. So all traffic goes that way, and every route costs 2.

### 17.9 Price of anarchy (pp. 152–153)
$\mathrm{Opt}(G)$ is the average time under the optimal flow. $\mathrm{Nash}(G)$ is the average time at a Nash equilibrium. The **price of anarchy** is $\mathrm{Nash}(G)/\mathrm{Opt}(G)$. It is 4/3 in these examples. The author says the next lecture will show it is never more than 4/3 for linear costs (pp. 152–153).

### 17.10 Nash optimum (p. 153)
Let the $s$–$t$ paths be $P_1,\dots,P_k$, with fraction $\alpha_i$ on $P_i$. Assume each car has negligible impact on traffic flow. Then in a Nash equilibrium, for all $i$ with $\alpha_i>0$ and all $j$: $c(P_i)\le c(P_j)$.

### 17.11 Social optimum (pp. 153–154)
The social cost is the average time:
$$c(\alpha_1,\dots,\alpha_k)\stackrel{def}{=}\sum_i\alpha_ic(P_i)=\sum_i\alpha_i\sum_{e\in P_i}c_e(f_e)=\sum_ec_e(f_e)\sum_{i:e\in P_i}\alpha_i=\sum_ec_e(f_e)f_e.$$

**Theorem 17.11.1.** All local minima of the social cost are global minima, and the set of global minima is convex.

*Proof (key steps).* The cost is $\sum_e c_e(f_e)f_e=\sum_e a_ef_e^2+b_ef_e$ with $a_e,b_e\ge0$. So each edge's cost is convex. For flows $f^0,f^1$, define $f^t_e=tf^1_e+(1-t)f^0_e$ for $0\le t\le1$. By convexity, the cost of $f^t$ is at most the maximum of the costs of $f^0,f^1$. If $f^1$ is a global optimum and $f^0$ costs more, then $f^\epsilon$ costs less than $f^0$, so $f^0$ is not a local optimum. If both are global optima, so is every $f^t$.

*Intuition note:* A bowl-shaped cost has no separate dips. Moving a little from a non-optimal flow toward a global optimum lowers the cost, so such a flow is not a local optimum and there is nowhere to get stuck.

## Toy example (ours)
Path $s - m - t$ with $w_{s,m}=2$, $w_{m,t}=2$. Fix $x(s)=0$, $x(t)=1$, $x(m)=m$.
- Energy $=\tfrac12[2m^2+2(1-m)^2]$. Its derivative $4m-4(1-m)=0$ gives $m=1/2$, and the energy is $\tfrac12[0.5+0.5]=0.5$. So $c_{s,t}=1$.
- Now lower $\hat w_{m,t}=1$. Using the old minimiser $m=1/2$: $\tfrac12[2\cdot\tfrac14+1\cdot\tfrac14]=\tfrac38\le\tfrac12$. This is the theorem's proof step.
- True minimum: $4m-2(1-m)=0$ gives $m=1/3$, energy $\tfrac12[\tfrac29+\tfrac49]=\tfrac13$. So $\hat c_{s,t}=2/3\le1$, and $\tfrac13\le\tfrac38$ as expected.
- Check by series formula: $1/(1/2+1)=2/3$ ✓.

## Concepts
- [[graph-laplacian]] — $L$ with $Lv=i_{ext}$ giving voltages (p. 149)
- [[pseudoinverse]] — $v=L^+i_{ext}$ solves for voltages (p. 149)
- [[quadratic-form]] — energy $v^TLv$ (p. 149)
- [[effective-resistance]] (new) — potential difference for one unit of current from $s$ to $t$; $i_{ext}^TL^+i_{ext}$ (p. 149)
- [[effective-spring-constant]] (new) — twice the minimum energy with $x(s)=0$, $x(t)=1$ (p. 147)
- [[rayleigh-monotonicity]] (new) — lowering spring constants cannot raise the effective spring constant (p. 148)
- [[nash-equilibrium]] (new) — every used path has minimal cost; no driver gains by switching (pp. 152–153)
- [[social-optimum]] (new) — flow minimising $\sum_ec_e(f_e)f_e$ (p. 153)
- [[price-of-anarchy]] (new) — $\mathrm{Nash}(G)/\mathrm{Opt}(G)$ (p. 152)
- [[convex-function]] (new) — used to show local minima are global (p. 153)

## Canonical instances
- [[path-effective-resistance]] — path resistances add (p. 150)
- [[parallel-resistors]] — conductances add (p. 150)
- [[spring-wire-nonmonotonicity]] — cutting a wire lifts the hanging weight: the $a$–$d$ distance goes from 2 to about 3/2 (p. 151)
- [[pigou-example]] — Nash 1 vs optimum 3/4 (pp. 151–152)
- [[braess-paradox]] — Nash cost 3/2 → 2 after adding a road (p. 152)

## Bridges (candidates)
- [same-math] effective resistance $i^TL^+i$ ↔ linear algebra: pseudoinverse solving $Lv=b$ — the same quadratic form.
- [structural-analogy] Rayleigh monotonicity ↔ variational principles: restricting or weakening a minimisation problem moves its minimum in a fixed direction.
- [structural-analogy] Braess's paradox ↔ game theory: equilibrium of selfish agents need not minimise total cost.
- [metaphor] Cutting a wire raising the weight ↔ network design: removing capacity can improve the system.

## Questions this raises
- Why does the energy argument break once elements are nonlinear?
- Can we prove that $\mathrm{Nash}/\mathrm{Opt}\le4/3$ for linear road costs (promised for the next lecture, p. 153)?
- How does the Nash condition relate to the convex social-cost problem?
- Does Rayleigh monotonicity (Theorem 17.4.2) follow from Theorem 17.3.1 by the energy view of resistance?

## Reading notes
- Printed page = pdf page − 24.
- Section 17.1 is empty; the draft notes warn they are unedited.
- p. 148: the text says decreasing spring constants means "effective resistance … will not increase". The theorem is about the effective spring constant, which does not increase. (The resistance version is Theorem 17.4.2.)
- p. 148 proof: it writes $\tfrac12\sum w(\dots)^2=c_{s,t}$, but $c_{s,t}$ was defined as twice the minimum energy. The ½ is inconsistent.
- p. 149: the proof ends with $R_{\rm eff}=v^TLv=\mathcal E(v)$, with no ½, while (17.1) defines $\mathcal E$ with a ½. The text does not say how the two normalisations fit together; the preceding sentence says $R_{\rm eff}$ is twice the energy dissipation. Also, Theorem 17.4.1 is stated with $\mathcal E(i)$ but the proof ends with $\mathcal E(v)$.
- p. 152, Braess: the vertices are called $a,b,c,d$ with $s=a$ and $t=d$, yet routes such as $scdt$ use $d$ as a middle vertex and $t$ as the end. The cost formula $p_3+p_3$ for $scdt$ does not follow from the stated road types (slow $s\to c$ and $d\to t$ would give cost $1+0+1=2$ for $scdt$). The conclusion (all traffic on $scdt$, cost 2) is as printed.
- p. 152: the 4/3 ratio for Braess is stated but $\mathrm{Opt}$ after adding the road is not computed in the text.
- p. 154: convexity gives cost($f^t$) ≤ max; the text then says $f^\epsilon$ costs strictly less than $f^0$. The strictness is not argued.
