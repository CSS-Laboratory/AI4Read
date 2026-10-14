---
id: bellman-1957-dp/ch05-v
work: bellman-1957-dp
unit: "5 Chapter V. The Optimal Inventory Equation (with Appendix, Exercises, Bibliography)"
pages: 152-182
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
# The Optimal Inventory Equation

## L0 — One line
When ordering costs are proportional to the amount ordered, the stochastic inventory dynamic program has a "constant stock level" solution: order up to a level fixed by a marginal-cost balance, otherwise order nothing; successive approximations then prove structure when explicit solutions fail.

## L1 — The gist (≤ 120 words)
How should one reorder stock when demand is random and shortage is penalised? Bellman writes the problem as a functional equation, $f(x)=\min_{y\ge x}[\dots]$. At an interior minimum of $u(x)=\min_y v(x,y)$, $u'(x)=v_x$, which gives the key relations. With proportional ordering and penalty costs, the optimal policy is explicit: order up to a level $\bar x$ if stock is below it, else do nothing. This holds for one item, many items, and finite horizons. Fixed ("red-tape") costs make the form of the solution unknown in general. Time lags and convex ordering costs give non-explicit policies whose general shape is found by successive approximations.

**Prerequisites:** differentiating integrals with variable limits; probability densities; the idea of a value function and of $f=\min(\dots f\dots)$; convexity.

## L2 — Key ideas (5–10 bullets)
- The inventory problem becomes a functional equation $f(x)=\min_{y\ge x}[\text{order cost}+\text{expected shortage penalty}+\text{discounted future}]$, with a finite-horizon version (a sequence $f_n$) and a discounted infinite-horizon version (one function $f$) (pp. 155–156).
- The basic tool is the observation that at an interior minimiser $u'(x)=v_x$, because $v_y=0$. With linear costs this gives an equation for the best level $y$ that does not contain $x$ (pp. 157–158).
- Theorem 1: with proportional costs and $ap>k$, the optimal policy is to order up to $\bar x$ when stock is below it and to order nothing otherwise. The level $\bar x$ solves $\int_0^{\bar x}\varphi=(ap-k)/(a(p-k))$ (pp. 160–161).
- With several items and a joint demand density, each $\bar x_i$ depends only on that item's marginal demand ("suboptimalization") (pp. 164–166).
- Finite horizon: the constant levels $\bar x_n$ increase with the number of remaining stages $n$; the proof is an induction on $f_n$ using monotonicity and convexity (pp. 166–169).
- A fixed penalty $q$ may still give a constant-level policy, if the last minimum of a certain function is the absolute minimum. In general several order-up-to regions can occur. Fixed ordering costs remain unsolved, and the $sS$ policy is not always optimal (pp. 171–173).
- Time lag and convex ordering cost: successive approximations show the optimal order $z(x)$, or target $y(x)$, is monotone, and give conditions for ordering at all, but no closed form (pp. 173–177).

## L3 — Walkthrough
Equation tags: "(s.n)" means equation $n$ of section $s$ of this chapter. Theorems keep the author's numbers.

### § 1. Introduction (pp. 152–153)
- Aim: a class of stochastic allocation problems from inventory control. A general solution seems hard. An explicit solution exists for one case, and the structure of optimal policies can be found in others (p. 152).
- Explicit solutions expose useful parameter combinations, and their economic interpretation can suggest approximate policies for harder processes (p. 152).
- Methodological point: successive approximations are not only for existence and uniqueness. They are also a tool to *discover and prove properties* of solutions of functional equations (p. 152).
- Plan: constant-stock-level policies arise when all ordering costs are proportional to amounts ordered, in one or many dimensions (p. 153). With a fixed ordering cost, "practically no solutions" of the equations exist, so it is not treated (p. 153).
- Two variants are treated by successive approximations: convex ordering cost (linearity dropped) and a time lag (simultaneity dropped). Their optimal policies "cannot be described in simple terms", but their general structure is found (p. 153). The equations are nonlinear versions of the renewal equation (Appendix) (p. 153).

### § 2. Formulation of the general problem (pp. 153–157)
**Setting.** Decisions under uncertain demand: stock items, with costs for oversupply and undersupply. The joint distribution of demands is known (pp. 153–154).

**A. Finite horizon, one item** (pp. 154–155). Orders are placed at equally spaced times and filled immediately. Then a demand arrives. Excess demand is penalised. Known, time-independent functions (p. 154):
- $\varphi(s)\,ds$ = probability that demand lies in $(s,s+ds)$.
- $k(z)$ = cost of ordering $z$ items initially.
- $p(z)$ = cost of ordering $z$ items to cover an excess $z$ of demand over supply (the penalty).

A *policy* is a set of functions $y_k=y_k(x)$, the quantity ordered at stage $k$ when stock is $x$. An *optimal* policy minimises expected total cost (p. 155). The state is two numbers: stock $x$ and remaining stages $n$ (p. 155). Define
$f_n(x)$ = expected total cost of an $n$-stage process from supply $x$ under an optimal policy \tag{2.2}

Order up to a level $y\ge x$ instead of ordering an amount, since the author finds the optimal stock level to be a more basic quantity than the amount ordered (p. 155):
$$f_1(x)=\min_{y\ge x}\Big[k(y-x)+\int_y^\infty p(s-y)\varphi(s)\,ds\Big]\tag{2.4}$$
For $n\ge 2$:
$$f_n(x)=\min_{y\ge x}\Big[k(y-x)+\int_y^\infty p(s-y)\varphi(s)ds+f_{n-1}(0)\int_y^\infty\varphi(s)ds+\int_0^y f_{n-1}(y-s)\varphi(s)ds\Big]\tag{2.5}$$
The terms: excess demand (penalty, then stock $0$ next stage), and demand met (stock $y-s$ next stage) (p. 155). Minimising the probability that cost exceeds a level is called harder (p. 155).

**B. Unbounded horizon, discounted** (p. 156). A discount ratio $a$, $0<a<1$, per period prevents infinite costs. With $f(x)$ the optimal expected discounted cost:
$$f(x)=\min_{y\ge x}\Big[k(y-x)+a\int_y^\infty p(s-y)\varphi(s)ds+af(0)\int_y^\infty\varphi(s)ds+a\int_0^y f(y-s)\varphi(s)ds\Big]\tag{2.7}$$
One function replaces the sequence $\{f_n\}$ (p. 156).

**C. Partially expendable items** (p. 156). A demand $s$ returns $bs$ items, $0\le b\le1$:
$$f(x)=\min_{y\ge x}\Big[k(y-x)+a\!\int_y^\infty p(s-y)\varphi ds+a\!\int_y^\infty f(bs)\varphi ds+a\!\int_0^y f(y-s+bs)\varphi ds\Big]\tag{2.8}$$

**D. One-period lag** (pp. 156–157). An order $z$ arrives one period later. $x$ is the total available for the next demand:
$$f(x)=\min_{z\ge0}\Big[k(z)+a\!\int_x^\infty p(s-x)\varphi ds+af(z)\!\int_x^\infty\varphi ds+a\!\int_0^x f(x-s+z)\varphi ds\Big]\tag{2.9}$$

**E. Two-period lag** (p. 157). Two state variables: $x$ = stock available for the next demand, $y$ = quantity arriving one period hence. Then
$$f(x,y)=\min_{z\ge0}\Big[k(z)+a\!\int_x^\infty p(s-x)\varphi ds+af(y,z)\!\int_x^\infty\varphi ds+a\!\int_0^x f(x-s+y,z)\varphi ds\Big]\tag{2.12}$$
(8), (9) and (12) are not treated, though the same techniques apply. No explicit solution as simple as that for (7) seems to exist (p. 157).

### § 3. A simple observation (pp. 157–158)
Consider $u(x)=\min_y v(x,y)$, $y\in R(x)$ \tag{3.1}. Assume that on $a\le x\le b$ the minimum is attained inside the region and $v$ is differentiable. Then at the minimiser
$$0=v_y\tag{3.2}$$
This defines $y(x)$, not necessarily single-valued, assumed differentiable. On one branch $u(x)=v(x,y(x))$ \tag{3.3}, so
$$u'(x)=v_x+v_y\,dy/dx=v_x\tag{3.4}$$
For two variables, $u(x_1,x_2)=\min_{y_1,y_2}v(x_1,x_2,y_1,y_2)$ with the minimum always interior \tag{3.5}:
$$u_{x_1}=v_{x_1},\quad u_{x_2}=v_{x_2}\tag{3.6}$$
at the minimising points (p. 158).

**Application to (2.7)** with $k(z)=kz$, $p(z)=pz$, $k>0$ (p. 158):
$$f(x)=\min_{y\ge x}\Big[ky-kx+a\!\int_y^\infty p(s-y)\varphi ds+af(0)\!\int_y^\infty\varphi ds+a\!\int_0^y f(y-s)\varphi ds\Big]\tag{3.7}$$
If the minimum is at $y>x$:
$$k-ap\int_y^\infty\varphi(s)ds+a\int_0^y f'(y-s)\varphi(s)ds=0\tag{3.8}$$
which is independent of $x$. At that $y$, $f'(x)=-k$ \tag{3.9}.

*Intuition note.* At the best choice, a small change in the choice does not change the cost to first order. So only the direct dependence on $x$ matters when asking how the optimal value changes with $x$. Here that dependence is $-kx$, so the marginal value of stock is $-k$ (the price of one unit).

### § 4. Constant stock level — preliminary discussion (pp. 158–159)
Common feature: ordering cost proportional to amount ordered, and demand distribution the same at each stage. Adding a fixed "red-tape" or "set-up" cost changes the optimal policy from a known form to an unknown form (p. 159, footnote). Roadmap: §5 one item, proportional penalty; §6 many items, with the sub-optimisation property; §7 finite horizon, where the constant level changes with the stage; §9 onward, harder cases (p. 159).

### § 5. Proportional cost — one-dimensional case (pp. 159–164)
**Theorem 1.** Consider
$$f(x)=\min_{y\ge x}\Big[k(y-x)+a\!\int_y^\infty p(s-y)\varphi ds+af(0)\!\int_y^\infty\varphi ds+a\!\int_0^y f(y-s)\varphi ds\Big]\tag{5.1}$$
with (5.2): (a) $k,p>0$ constants; (b) $\varphi>0$, $\int_0^\infty\varphi=1$, $\int_0^\infty s\varphi<\infty$; (c) $0<a<1$; (d) $ap>k$. Let $\bar x$ be the unique root of
$$k=ap\int_{y}^\infty\varphi(s)ds+ak\int_0^{y}\varphi(s)ds\quad(y=\bar x)\tag{5.3}$$
Then the optimal policy is: for $0\le x\le\bar x$, $y=\bar x$; for $x\ge\bar x$, $y=x$ \tag{5.4}. So the optimal stock level is $\bar x$. If $ap\le k$, the solution is $y=x$ for all $x\ge0$ (never order) (p. 160). Interpretation (footnote): the run-out probability is set where the marginal cost of holding inventory just balances the marginal run-out penalty (p. 160).

**Proof, heuristic construction** (pp. 160–161). Plausible solution found by formal means, then verified directly. Uniqueness (Chapter IV, §9) then says it is *the* solution. Successive approximations would have led here systematically (p. 160).
1. By §3, if the minimum is at $y>x$, $y$ satisfies
$$k+a\Big[-p\int_y^\infty\varphi ds+\int_0^yf'(y-s)\varphi ds\Big]=0\tag{5.5}$$
and $f'(x)=-k$ \tag{5.6}.
2. "Bootstrap": if the solution has the conjectured form, replace $f'(y-s)$ by $-k$ in (5.5). This gives (5.7), $k-ap\int_y^\infty\varphi-ak\int_0^y\varphi=0$, which is (5.3) (pp. 160–161).
3. Using $\int_0^\infty\varphi=1$,
$$\int_0^y\varphi(s)ds=\frac{ap-k}{a(p-k)}\tag{5.8}$$
The author says it has exactly one root under the assumption that $\varphi>0$. Limiting cases behave: $ap-k=0\Rightarrow y=0$; $a=1\Rightarrow y=\infty$; $p=\infty\Rightarrow y=\infty$ (p. 161).
4. For $0\le x\le\bar x$ the policy gives
$$f(x)=k(\bar x-x)+a\Big[\int_{\bar x}^\infty p(s-\bar x)\varphi ds+f(0)\!\int_{\bar x}^\infty\varphi ds+\!\int_0^{\bar x}f(\bar x-s)\varphi ds\Big]\tag{5.9}$$
and $f'(x)=-k$, i.e. $f(x)=f(0)-kx$ \tag{5.10}. Substituting (5.10) into (5.9) at $x=0$:
$$f(0)=\frac{k\bar x+pa\int_{\bar x}^\infty(s-\bar x)\varphi ds-ak\int_0^{\bar x}(\bar x-s)\varphi ds}{1-a}\tag{5.11}$$
Footnote: this $\bar x$ minimises the expression for $f(0)$ (p. 161).
5. For $x\ge\bar x$, $f(x)=a[\int_x^\infty p(s-x)\varphi ds+f(0)\int_x^\infty\varphi ds+\int_0^xf(x-s)\varphi ds]$ \tag{5.12}, i.e. $f(x)=u(x)+a\int_0^xf(x-s)\varphi ds$ with $u$ known \tag{5.13}. Split the integral at $x-\bar x$ (5.14). On $[x-\bar x,x]$, $f(x-s)$ is already known, so
$$f(x)=v(x)+a\int_0^{x-\bar x}f(x-s)\varphi(s)ds,\quad x\ge\bar x\tag{5.15}$$
With $z=x-\bar x$ and $g(z)=f(\bar x+z)$:
$$g(z)=v(\bar x+z)+a\int_0^zg(z-s)\varphi(s)ds,\quad z\ge0\tag{5.16}$$
This is a renewal equation (Appendix) (p. 162). Footnote: for $x>\bar x$ the solution matters little in applications, since at most one initial interval has $x>\bar x$ (p. 161).
6. Remark: in dynamic programming the derivatives seem to satisfy simpler equations and to be the more basic quantities. They are "marginal returns" or "prices", i.e. Lagrange multipliers, connected to dual processes (not pursued) (p. 162).

**Verification** (pp. 162–164). Let $F$ be the constructed function and $C=f(0)$ from (5.11):
$$F(x)=C-kx,\ 0\le x\le\bar x;\qquad F(x)=a\Big[\int_x^\infty p(s-x)\varphi+F(0)\int_x^\infty\varphi+\int_0^xF(x-s)\varphi\Big],\ x\ge\bar x\tag{5.17}$$
Key fact: $F(x)+kx$ is strictly increasing for $x>\bar x$ (constant on $[0,\bar x]$ by (5.17a)). From (5.17b), for $x\ge\bar x$:
$$F'(x)=-ap\int_x^\infty\varphi ds+a\int_0^xF'(x-s)\varphi ds\tag{5.18}$$
For $s\in[x-\bar x,x]$ we have $0\le x-s\le\bar x$, so $F'(x-s)=-k$. Hence
$$F'(x)=-ap\!\int_x^\infty\!\varphi-ka\!\int_{x-\bar x}^x\!\varphi+a\!\int_0^{x-\bar x}\!F'(x-s)\varphi\,ds\tag{5.19}$$
$$F'(x)+k=\Big[k-ap\!\int_x^\infty\!\varphi-ak\!\int_0^x\!\varphi\Big]+a\!\int_0^{x-\bar x}[F'(x-s)+k]\varphi\,ds\tag{5.20}$$
The bracket
$$u(x)=k-ap\int_x^\infty\varphi ds-ak\int_0^x\varphi ds\tag{5.21}$$
is $0$ at $\bar x$ and positive afterwards. With $z=x-\bar x$ and $g(z)=F'(\bar x+z)+k$, the source writes (5.22) as $g(z)=u(\bar x+z)+\int_0^zg(z-s)\varphi ds$, $z\ge 0$, without the factor $a$ that (5.20) carries (see Reading notes). Positivity for renewal equations (Appendix, p. 177 ff) gives $g(z)>0$ for $z>0$. So $F'(x)+k>0$ for $x>\bar x$ (p. 163).

Now check that $F$ satisfies (5.1) (p. 163):
- For $x\ge\bar x$: using (5.17b), $F(x)=\min_{y\ge x}[k(y-x)+F(y)]$ \tag{5.23}. Since $ky+F(y)\ge kx+F(x)$ for $y\ge x$, the minimum is at $y=x$.
- For $0\le x<\bar x$: split $\min_{y\ge x}=\min\{\min_{y\ge\bar x},\min_{\bar x\ge y\ge x}\}$ \tag{5.24}. The minimum over $y\ge\bar x$ is at $y=\bar x$, so $\min_{y\ge x}[\dots]=\min_{\bar x\ge y\ge x}[\dots]$ \tag{5.25}. As $F=C-kx$ on $[0,\bar x]$, the minimum is at $y=\bar x$, as in the derivation of $\bar x$.
- If $ap\le k$: take $\bar x=0$ in (5.17). Then $F(y)+ky$ is non-decreasing, and (5.23) holds (p. 164).

Conclusion: $F$ is a solution, hence *the* solution, among uniformly bounded functions on $x\ge0$. The part $0\le x\le\bar x$ (the important part) is found without reference to $x>\bar x$ (p. 164).

*Intuition note.* Below $\bar x$ the marginal value of a unit of stock is exactly its price $k$, so topping up costs nothing extra beyond $k$ per unit. Above $\bar x$ extra stock is worth less than it costs, so one orders nothing. The level $\bar x$ is where holding one more unit just balances the expected penalty of running out. *Skip path:* carry forward (5.3)/(5.8) for $\bar x$ and the policy (5.4); the rest is verification.

### § 6. Proportional cost — multi-dimensional case (pp. 164–166)
$N$ items, stocks $x_1,\dots,x_N$, joint demand density $\varphi(s_1,\dots,s_N)$. Only $N=2$ is written out. The solution has the same form as if demands were uncorrelated, which gives the sub-optimisation property (p. 164). The equation is
$$\begin{aligned}f(x_1,x_2)=\min_{y_i\ge x_i}\Big[&k_1(y_1-x_1)+k_2(y_2-x_2)+a\Big\{\int_{y_1}^\infty\!\!\int_{y_2}^\infty[p_1(s_1-y_1)+p_2(s_2-y_2)]\varphi\,ds_1ds_2\\&+f(0,0)\int_{y_1}^\infty\!\!\int_{y_2}^\infty\varphi\,ds_1ds_2+\int_{y_1}^\infty\!\!\int_0^{y_2}[p_1(s_1-y_1)+f(0,y_2-s_2)]\varphi\,ds_1ds_2\\&+\int_0^{y_1}\!\!\int_{y_2}^\infty[f(y_1-s_1,0)+p_2(s_2-y_2)]\varphi\,ds_1ds_2+\int_0^{y_1}\!\!\int_0^{y_2}f(y_1-s_1,y_2-s_2)\varphi\,ds_1ds_2\Big\}\Big]\end{aligned}\tag{6.1}$$
The four cases are: both items short, only item 1 short, only item 2 short, neither short. Write $\varphi\,ds_1ds_2=dG(s_1,s_2)$ and call the bracket $K(y_1,y_2)$. Its derivative is (pp. 164–165)
$$\frac{\partial K}{\partial y_1}=k_1+a\Big[-p_1\!\int_{y_1}^\infty\!\Big(\int_{s_2=0}^\infty\!dG\Big)+\int_0^{y_1}\!\frac{\partial f}{\partial y_1}(y_1-s_1,0)\Big(\int_{s_2=y_2}^\infty\!dG\Big)+\int_0^{y_1}\!\!\int_0^{y_2}\!\frac{\partial f}{\partial y_1}(y_1-s_1,y_2-s_2)\,dG\Big]\tag{6.2}$$
and symmetrically for $\partial K/\partial y_2$ (printed in the source). For $y_1>x_1$, $y_2>x_2$: $\partial f/\partial x_1=-k_1$, $\partial f/\partial x_2=-k_2$ \tag{6.3}. Assuming the same form as in one dimension, the critical levels satisfy
$$k_1+a\Big[-p_1\!\int_{\bar x_1}^\infty\!\Big(\int_{s_2=0}^\infty\! dG\Big)-k_1\!\int_0^{\bar x_1}\!\Big(\int_{s_2=0}^\infty\! dG\Big)\Big]=0\tag{6.4a}$$
and the same with $(1\to2)$, with inner integral over $s_1$ from $0$ to $\infty$ (6.4b). Roots exist and are unique if $ap_1>k_1$, $ap_2>k_2$, $dG>0$. $\bar x_1$ depends only on the marginal $\int_{s_2=0}^\infty dG$, and $\bar x_2$ only on $\int_{s_1=0}^\infty dG$: this is the sub-optimisation property (p. 165). The verification follows the one-dimensional lines and is omitted as "much more tedious" (p. 165).

**Theorem 2.** Under (6.5): $k_i,p_i>0$; $\varphi>0$, $\iint\varphi=1$, $\iint s_i\varphi<\infty$; $0<a<1$; $ap_i>k_i$. Let $\bar x_i$ be the unique root of (6.6) (the analogue of (5.3) with the marginal demand of item $i$). Then the optimal policy is $y_i=\bar x_i$ for $0\le x_i\le\bar x_i$ and $y_i=x_i$ for $x_i\ge\bar x_i$. If $ap_i\le k_i$ for any $i$, set $\bar x_i=0$. The form extends to $N$ items (pp. 165–166).

*Intuition note.* Items are ordered independently of each other even though their demands are correlated. Each item's target depends only on its own demand distribution. This lets one design item by item.

### § 7. Finite time period (pp. 166–169)
No discounting; $f_N(x)$ is the minimal expected cost over $N$ stages \tag{7.1}:
$$f_1(x)=\min_{y\ge x}\Big[k(y-x)+p\!\int_y^\infty(s-y)\varphi ds\Big],\quad f_{n+1}(x)=\min_{y\ge x}\Big[k(y-x)+p\!\int_y^\infty(s-y)\varphi+f_n(0)\!\int_y^\infty\varphi+\!\int_0^yf_n(y-s)\varphi\Big]\tag{7.2}$$
**Theorem 3.** If $p>k$: for each $n$ the optimal policy is $y=\bar x_n$ for $x\le\bar x_n$ and $y=x$ for $x\ge\bar x_n$, and the sequence $\bar x_n$ is monotone increasing in $n$ (p. 166).

**Proof (induction)** (pp. 166–169).
- $n=1$: $\bar x_1$ solves $k=p\int_y^\infty\varphi\,ds$ \tag{7.4}; it exists and is unique if $p>k$ (p. 167). For $x\ge\bar x_1$: $f_1=p\int_x^\infty(s-x)\varphi$, $f_1'=-p\int_x^\infty\varphi\ge-k$, $f_1''=p\varphi(x)>0$ \tag{7.5}. Hence $f_1'+k\ge0$.
- $n=2$: set the $y$-derivative of (7.6) to zero:
$$k=p\int_y^\infty\varphi ds-\int_0^yf_1'(y-s)\varphi ds=F_1(y)\tag{7.7}$$
$$F_1'(y)=-p\varphi(y)-f_1'(0)\varphi(y)-\int_0^yf_1''(y-s)\varphi ds\tag{7.8}$$
Since $f_1''>0$ and $p+f_1'(0)>k+f_1'(0)=0$ (as $f_1'(0)=-k$), $F_1$ is monotone decreasing: at most one root. Also $F_1(0)=p>k$ and $F_1(\infty)=0$, so there is exactly one root $\bar x_2$. The policy is $y=\bar x_2$ for $0\le x\le\bar x_2$ and $y=x$ for $x\ge\bar x_2$ (7.9) (p. 167).
- Geometry: write $f_2(x)+kx=\min_{y\ge x}v(y)$ \tag{7.10}, with $v$ a known function (Figure 1, a curve with minimum at $\bar x_2$). $f_2+kx$ is constant for $x\le\bar x_2$ and equals $v(x)$ for $x\ge\bar x_2$ (Figure 2) (p. 168).
- $\bar x_2>\bar x_1$: $\bar x_1$ solves (7.4) and $\bar x_2$ solves (7.7). Since $-f_1'\ge0$, the curve $w=g_2(y)=p\int_y^\infty\varphi-\int_0^yf_1'(y-s)\varphi$ \tag{7.11} lies above $w=g_1(y)=p\int_y^\infty\varphi$ \tag{7.12}. Hence it crosses $w=k$ further right (Figure 3) (p. 168).
- Induction step needs (7.13) $-f_2'(x)\ge-f_1'(x)$. We have $-f_1'=k$ on $[0,\bar x_1]$ and $=p\int_x^\infty\varphi$ on $[\bar x_1,\infty)$ (7.14). Also $-f_2'=k$ on $[0,\bar x_2]$ and $=p\int_x^\infty\varphi-\int_0^xf_1'(x-s)\varphi\,ds$ for $x\ge\bar x_2$ (7.15). The inequality is clear on $[0,\bar x_1]$ and $[\bar x_2,\infty)$; on $[\bar x_1,\bar x_2]$ it follows from the monotonicity of $k-p\int_x^\infty\varphi$, which is $0$ at $\bar x_1$ (p. 169).
- Convexity of $f_2$: clear on $[0,\bar x_2]$; for larger $x$, $f_2''=p\varphi(x)+f_1'(0)\varphi(x)+\int_0^xf_1''(x-s)\varphi\,ds>0$ since $f_1'(0)+p>0$ and $f_1''\ge0$ (7.16). These are the ingredients of the induction (p. 169).

*Intuition note.* With more periods remaining, it pays to hold more stock, so the order-up-to level rises with $n$. The proof tracks two facts through the induction: marginal value $-f_n'$ is at most the unit price $k$ and does not decrease in $n$, and $f_n$ is convex.

### § 8. Finite time, multi-dimensional (p. 169)
The author leaves it to the reader to verify that the multi-dimensional solution has the same general character (p. 169).

### § 9. Non-proportional penalty cost — red tape (pp. 169–171)
When the penalty is not proportional to the excess demand, it appears that the simple solution of the proportional case is no longer valid generally (p. 169). The case studied: penalty $p(s-y)+q$, where $q$ is a fixed administrative cost charged whenever excess demand occurs. Ordering cost stays proportional. Equation (9.1) is (5.1) with the extra term $aq\int_y^\infty\varphi\,ds$ (p. 170).
- Formally assuming a constant-level solution, the critical $y$ satisfies
$$0=k+a\Big[-p\!\int_y^\infty\!\varphi-q\varphi(y)+\!\int_0^yf'(y-s)\varphi ds\Big]\tag{9.2}$$
and with $f'=-k$: $0=k+a[-p\int_y^\infty\varphi-q\varphi(y)-k\int_0^y\varphi]$ \tag{9.3}, i.e.
$$(1-a)k=a(p-k)\int_y^\infty\varphi(s)ds+aq\varphi(y)\tag{9.4}$$
This need not have a unique root for every density; $\varphi'(y)\le0$ is a simple sufficient condition for uniqueness. With a unique root the proof is, the author says, almost exactly as before (p. 170).
- Otherwise the largest root of (9.4) may still correspond to an absolute minimum of the bracket over $[0,\bar x]$ (Figure 4).

**Theorem 4.** Under the assumptions of Theorem 1 on $a,k,p,q,\varphi$, and the additional assumption that the last minimum of
$$\psi(y)=ky+a\Big[\int_y^\infty[p(s-y)+q]\varphi ds-k\int_0^y(y-s)\varphi ds\Big]\tag{9.6}$$
is the absolute minimum on $0\le y\le\infty$, the optimal policy is $y=\bar x$ for $0\le x\le\bar x$ and $y=x$ for $x\ge\bar x$, where $\bar x$ is where the absolute minimum is attained (p. 171).

*Proof (as given).* As for $q=0$: $f(x)=f(0)-kx$ on $[0,\bar x]$, $f(0)$ is found by substituting into (9.1), and on $[\bar x,\infty)$ $f$ comes from setting $y=x$. Verification then continues as before (p. 171).

### § 10. Particular cases (p. 171)
Densities satisfying the conditions: (a) $\varphi(x)=e^{-(x-a)^2}\big/\int_{-a}^\infty e^{-u^2}du$; (b) $\varphi(x)=be^{-bx}$. Verification is left as an exercise (p. 171).

### § 11. The form of the general solution (pp. 171–172)
For (9.1), $f(x)+kx=\min_{y\ge x}F(y)$ with
$$F(y)=ky+a\Big[p\!\int_y^\infty(s-y)\varphi ds+(f(0)+q)\!\int_y^\infty\varphi ds+\!\int_0^yf(y-s)\varphi ds\Big]\tag{11.2}$$
If $F$ has several local minima (Figure 5), the optimal policy has several regions: $y=x_1$ for $0\le x\le x_1$; $y=x$ for $x_1\le x\le x_2$; $y=x_3$ for $x_2<x<x_3$; $y=x$ for $x\ge x_3$ (11.4), with $f+kx=F(x_1)$, $F(x)$, $F(x_3)$, $F(x)$ on the respective ranges (11.5). Determining how many regions arise from given costs and demand, and how to assemble them, "seems quite difficult" and is unsolved (p. 172).

### § 12. Fixed costs (pp. 172–173)
Add a fixed ordering cost $g(y-x)$ with $g(x)=g$ for $x>0$, $g(0)=0$ \tag{12.2}; the equation is (5.1) with this term. The problem is unsolved (p. 172). An "$sS$-policy" is tempting: $y=S$ for $0\le x\le s$ and $y=x$ for $s<x$, with $0<s<S<\infty$. It is used in various establishments and appeals to intuition. But the author says it is "easy to construct relatively simple examples" showing it cannot be optimal in all cases (p. 173).

### § 13. Preliminaries (p. 173)
Two harder cases follow (time lag; non-linear convex ordering cost), without red tape. Both use successive approximations (p. 173).

### § 14. Unbounded process, one-period lag (pp. 173–176)
Equation (14.1) is (2.9).

**Theorem 5.** The optimal policy is $z=z(x)$ for $0\le x\le\bar x$ and $z=0$ for $x\ge\bar x$, with $z(x)\ge0$, $z(\bar x)=0$, and $z(x)$ monotone decreasing (pp. 173–174).

**Proof** (pp. 174–176). Approximations: $f_0(x)=a[\int_x^\infty p(s-x)\varphi+f_0(0)\int_x^\infty\varphi+\int_0^xf_0(x-s)\varphi]$ \tag{14.3}, and $f_{n+1}(x)=\min_{z\ge0}T(z,x,f_n)$ \tag{14.4}, with $T$ the bracket in (14.1).
1. Take $M_1(z)=T(z,x,f_0)$:
$$M_1'(z)=k+af_0'(z)\!\int_x^\infty\!\varphi+a\!\int_0^x\!f_0'(x-s+z)\varphi\,ds\tag{14.5}$$
$$M_1''(z)=af_0''(z)\!\int_x^\infty\!\varphi+a\!\int_0^x\!f_0''(x-s+z)\varphi\,ds\tag{14.6}$$
Since $f_0''>0$ (asserted in the source without proof here), $M_1''>0$, so $M_1'(z)=0$ has at most one root. For large $x$ there is no root; for $x=0$ there is a root if $a,p,k$ are suitably related. Call the root $z_1(x)$ (p. 174).
2. Monotonicity: set $G_0(x,z)=-af_0'(z)\int_x^\infty\varphi-a\int_0^xf_0'(x-s+z)\varphi ds$. The root condition is $G_0=k$. Then
$$\partial G_0/\partial x=-a\int_0^xf_0''(x-s+z)\varphi(s)ds<0\tag{14.7}$$
so (Figure 6) $z_1(x)$ is monotone decreasing in $x$ and equals $0$ for $x\ge\bar x_1$ (pp. 174–175).
3. Convexity of $f_1$: $f_1(x)=T(z_1(x),x,f_0)$ on $[0,\bar x_1]$ and $T(0,x,f_0)$ beyond (14.8). On $[0,\bar x_1]$:
$$f_1'(x)=-ap\!\int_x^\infty\!\varphi+a\!\int_0^x\!f_0'(x-s+z)\varphi ds\tag{14.9}$$
$$f_1''(x)=ap\varphi(x)+af_0'(z)\varphi(x)+\Big(a\!\int_0^x\!f_0''(x-s+z)\varphi ds\Big)(1+dz_1/dx)\tag{14.10}$$
$f_0'(0)=-ap$ (from the analogue of (14.12); the source cites (14.9)) and $f_0'$ is increasing, so $ap+af_0'(z)\ge0$ for $z\ge0$. Thus $f_1''\ge0$ if $1+dz_1/dx\ge0$. Differentiating $M_1'(z_1(x))=0$:
$$\Big[af_0''(z)\!\int_x^\infty\!\varphi+a\!\int_0^x\!f_0''(x-s+z)\varphi ds\Big]\frac{dz}{dx}+a\!\int_0^x\!f_0''(x-s+z)\varphi ds=0\tag{14.11}$$
This shows $dz_1/dx\le0$ and $1+dz_1/dx\ge0$. (added step: write $A,B\ge0$ for the two terms in the bracket; then $dz/dx=-B/(A+B)$ and $1+dz/dx=A/(A+B)$.)
4. Link between successive approximations: $f_0'(x)=-ap\int_x^\infty\varphi+a\int_0^xf_0'(x-s)\varphi ds$ \tag{14.12}. Comparing with (14.9) on $[0,\bar x]$ and using that $f_0'$ is increasing, $f_0'\le f_1'$ there. Since $f_1=f_0$ for $x\ge\bar x$,
$$f_0'(x)\le f_1'(x)\ \ \text{for all }x\ge0\tag{14.13}$$
5. Continuing, each $n$ gives $z_n(x)>0$ for $0\le x<\bar x_n$ and $z_n(x)=0$ for $x\ge\bar x_n$ (14.14), with $z_n$ monotone decreasing. The sequence $\bar x_n$ is monotone *decreasing* and has a limit $\bar x$ (p. 176).
6. Final condition: at $x=0$, $k+af_0'(z)=0$ \tag{14.15} has a solution if $k+af_0'(0)<0$. With $f_0'(0)=-ap$ this requires
$$k<a^2p\tag{14.16}$$
which the author calls the "intuitive and expected condition" for a one-stage delay (p. 176).

*Intuition note.* With a lag, one chooses how much to put on order, and the best amount $z(x)$ shrinks as stock on hand grows, reaching zero at $\bar x$. There is no simple order-up-to formula here. The proof only gets the shape. The condition the author finds for the ordering equation to have a root at $x=0$ is $k<a^2p$: the discounted penalty $a^2p$ must exceed the price $k$.

### § 15. Convex cost function — unbounded process (pp. 176–177)
Ordering cost $g(y-x)$ strictly convex ($g''>0$), $g'$ continuous. Equation (15.1) is (5.1) with $g(y-x)$ replacing $k(y-x)$. $f_0$ is as in (14.3) (15.2), and $f_{n+1}=\min_{y\ge x}T(y,x,f_n)$ \tag{15.3}.
1. For $f_1$, an interior $y>x$ satisfies
$$g'(y-x)=a\Big[p\!\int_y^\infty\!\varphi-\!\int_0^yf_0'(y-s)\varphi ds\Big]\tag{15.4}$$
At most one root (left side increasing, right side decreasing). A root exists at $x=0$ if $g'(0)<ap$ \tag{15.5}. For large $x$ there is no root if $g'(0)>0$ (pp. 176–177).
2. If $y>x$: $f_1'(x)=-g'(y-x)$ \tag{15.6}, $f_1''(x)=-g''(y-x)(dy/dx-1)$ \tag{15.7}. Differentiating (15.4):
$$g''(y-x)(dy/dx-1)=\Big[-ap\varphi(y)-af_0'(0)\varphi(y)-a\!\int_0^y\!f_0''(y-s)\varphi ds\Big]dy/dx\tag{15.8}$$
From this, $dy/dx>0$ and $dy/dx-1<0$, so $f_1''>0$ (p. 177). (added step: with $f_0'(0)=-ap$ the bracket is $-C$ with $C>0$, so $dy/dx=g''/(g''+C)\in(0,1)$.) Also $-f_1'\ge-f_0'$, so the induction goes through.

**Theorem 6.** There is a function $y(x)$ and a number $\bar x$ with: (a) $y(x)\ge x$ and $y(x)$ is monotone increasing; (b) $y(x)>x$ for $x\le\bar x$ and $y(x)=x$ for $x\ge\bar x$; (c) $\bar x>0$ if $ap>g'(0)$. This $y(x)$ is the optimal policy in (15.1) (p. 177). (As printed, (b) says $y(x)>x$ for $x\le\bar x$, although $y(\bar x)=\bar x$ in the second clause.)

*Intuition note.* When ordering gets more expensive per unit as the order grows, one orders only part of the gap to a target, and the target moves with $x$. It does not jump to a fixed level.

### Appendix to Chapter V — The Renewal Equation (pp. 177–178)
$$u(x)=f(x)+\int_0^xu(x-s)\varphi(s)ds\tag{A.1}$$
Two methods: Laplace transform, and Liouville–Neumann successive approximations (p. 177). The Laplace transform turns the convolution into a product:
$$\int_0^\infty e^{-tx}\Big[\int_0^xu(x-s)\varphi(s)ds\Big]dx=\Big(\int_0^\infty e^{-tx}u\,dx\Big)\Big(\int_0^\infty e^{-st}\varphi(s)ds\Big)\tag{A.2}$$
Formally then
$$\int_0^\infty e^{-tx}u(x)dx=\frac{\int_0^\infty e^{-tx}f(x)dx}{1-\int_0^\infty e^{-tx}\varphi(x)dx}\tag{A.3}$$
from which asymptotics follow via Tauberian theorems or complex variables (p. 178). For positivity and convexity the author prefers $u_0=f$, $u_{n+1}=f+\int_0^xu_n(x-s)\varphi(s)ds$ (A.4), showing each $u_n$ has the property (p. 178).

**Theorem 9.** If (a) $f$ is bounded on every finite $[0,x_0]$ and (b) $\int_0^\infty|\varphi|ds<1$, then (A.1) has a unique solution bounded on every $[0,x_0]$, the limit of (A.4). If $f$ is differentiable and $\varphi$ continuous, $u'(x)=f'(x)+u(0)\varphi(x)+\int_0^xu'(x-s)\varphi(s)ds$ \tag{A.6}. If $f\ge0$ and $\varphi\ge0$ then $u\ge0$. Other condition combinations also give existence and uniqueness. The author says the proof follows techniques already applied many times (p. 178).

### Exercises and Bibliography (pp. 178–182)
19 exercises (pp. 178–182): see the list below. The bibliography (p. 182) says the model originated in Arrow, Harris and Marschak (1951). Dvoretzky–Kiefer–Wolfowitz (1952) treat existence/uniqueness and distributions of demand functions. The chapter's results came from Bellman, Glicksberg and Gross (1955). The comment on §3 repeats that derivatives ("marginal returns") often have simpler structure than the return functions (p. 182).

## Toy example (ours, not from the text)
Take Theorem 1 with $k=1$, $p=3$, $a=0.9$ (so $ap=2.7>k$ ✓) and exponential demand $\varphi(s)=e^{-s}$, so $\int_0^y\varphi=1-e^{-y}$.
- Right side of (5.8): $(ap-k)/(a(p-k))=(2.7-1)/(0.9\cdot2)=1.7/1.8=0.9444$.
- Solve $1-e^{-\bar x}=0.9444$: $e^{-\bar x}=0.0556=1/18$, so $\bar x=\ln18\approx2.890$.
- Check in (5.3): $ap\int_{\bar x}^\infty\varphi=2.7\cdot(1/18)=0.15$; $ak\int_0^{\bar x}\varphi=0.9\cdot(17/18)=0.85$; sum $=1.00=k$ ✓.
- Policy: starting stock $1.5$ → order $2.890-1.5=1.390$; starting stock $4$ → order nothing. If instead $k=3$ (so $ap=2.7\le k$), never order.

## Concepts
- [[bellman-equation-value-function]] — $f_n(x)$ or $f(x)$ = optimal expected (discounted) cost from stock $x$, defined by a min over the order-up-to level $y$ (pp. 155–156)
- [[policy]] — a set of functions $y_k=y_k(x)$ giving the order-up-to level (or order amount) at stage $k$ for stock $x$ (p. 155)
- [[state]] — stock $x$ and number of remaining stages $n$; with lags, extra variables for goods on order (pp. 155, 157)
- [[delay-dead-time]] — the supply lag in sections D, E and §14: orders arrive later; a one-period lag keeps the single state $x$ (total available), while a two-period lag needs two state variables (pp. 156–157)
- [[envelope-derivative-rule]] (new) — at an interior minimum $u'(x)=v_x$ since $v_y=0$; the marginal value is the direct partial derivative (p. 158)
- [[order-up-to-policy]] (new) — "constant stock level": if $x<\bar x$ order up to $\bar x$, else order nothing (p. 160)
- [[suboptimalization]] (new) — the critical level of each item depends only on its own marginal demand distribution, despite correlation (p. 165)
- [[red-tape-fixed-cost]] (new) — fixed cost independent of amount (in ordering, or in penalty); destroys the simple solution form in general (pp. 159, 169, 172)
- [[sS-policy]] (new) — order up to $S$ when $x\le s$, else nothing; intuitive but not always optimal (p. 173)
- [[successive-approximations]] (new) — define $f_0$ and iterate $f_{n+1}=\min T(\cdot,f_n)$; here used to prove positivity, monotonicity and convexity (pp. 152, 174)
- [[renewal-equation]] (new) — $u=f+\int_0^xu(x-s)\varphi(s)ds$; arises for the solution beyond $\bar x$ (pp. 162, 177)
- [[marginal-return-lagrange-multiplier]] (new) — derivatives of value functions are described as marginal returns or "prices", i.e. Lagrange multipliers (p. 162)

## Canonical instances
- [[optimal-inventory-problem]] — stocking under uncertain demand with shortage penalty: the chapter's whole model (p. 153)
- [[constant-stock-level-solution]] — Theorem 1: explicit order-up-to level with proportional costs (p. 160)
- [[finite-horizon-inventory]] — Theorem 3: order-up-to levels increase with remaining stages (p. 166)
- [[inventory-with-supply-lag]] — Theorem 5: one-period lag; optimal $z(x)$ decreasing; $k<a^2p$ is the condition found for a root of the ordering equation at $x=0$ (pp. 173–176)

## Bridges (candidates)
- [same-math] $f_{n+1}(x)=\min_z T(z,x,f_n)$ iterated from $f_0$ ↔ control-theory: value iteration for a discounted MDP with a continuous state — the same successive-approximation scheme.
- [structural-analogy] $f'(x)=-k$ as "price" of stock, with derivatives as Lagrange multipliers (p. 162) ↔ control-theory: costates / shadow prices in the Pontryagin principle — both give the marginal value of the state.
- [structural-analogy] Order-up-to rule: act only when stock falls below $\bar x$, do nothing above ↔ control-theory: minimal intervention (no correction where deviation does not matter) — a one-sided dead zone.
- [structural-analogy] Renewal equation transform $\hat u=\hat f/(1-\hat\varphi)$ ↔ control-theory: a closed-loop transfer function $1/(1-L)$ with a convolution kernel in the loop.
- [metaphor] Supply lag (§14) ↔ control-theory: a longer lag (two periods) forces extra state variables, and the optimal policy is no longer a simple order-up-to rule.

## Questions this raises
- With a fixed ordering cost, when is an $sS$ policy optimal and when does it fail, given the author's remark that it is not optimal in all cases? (p. 173)
- How do the order-up-to levels $\bar x_n$ in Theorem 3 behave as $n\to\infty$, and do they approach the discounted level $\bar x$ of Theorem 1 as $a\to1$?
- Can the "derivatives are simpler" principle (p. 162) be made into a general method via dual processes, as the author hints?
- In the lag problem, why does the limit of $\bar x_n$ decrease while the finite-horizon levels in §7 increase? (pp. 166, 176)

## Exercises worth doing
- Ex. 1 (p. 178) — analogue of Theorem 3 when the demand distribution varies by stage; tests whether the induction survives — difficulty: medium
- Ex. 4 (p. 179) — analogues of Theorems 1–3 with a storage cost proportional to the quantity stored; a natural extension — difficulty: medium
- Ex. 6 (p. 179) — analogue of Theorem 5 for arbitrary lags; builds intuition on state growth — difficulty: hard
- Ex. 11 (p. 180) — functional equations for minimising the probability that cost exceeds $c$ (the harder criterion on p. 155) — difficulty: medium
- Ex. 17 (p. 181) — find $L$ for the "order up to $L$" policy under a one-period lag — difficulty: medium
- Ex. 18 (p. 182) — prove or disprove that this policy is optimal (compare §14, which finds a decreasing $z(x)$) — difficulty: hard

## Reading notes
- Printed page = pdf − 23 (pdf 175 = printed 152); the page labels give printed numbers directly.
- The running header "THE OPTIMAL INVENTORY EQUATION" appears from p. 153 to p. 182 (the chapter-opening page 152 shows none); the unit includes the Appendix, Exercises 1–19 and the Bibliography and Comments (p. 182).
- OCR: the text layer garbles many equations. I used the page images for all equations.
- Theorem numbering: Chapter V has Theorems 1–6 and, in the Appendix, Theorem 9; no Theorems 7–8 appear in these pages.
- Eq. (5.22) (p. 163) is printed without the factor $a$ in front of the integral, while (5.20) has it. With the factor the kernel integrates to $a<1$, as Theorem 9(b), $\int|\varphi|<1$, requires; without it the kernel integrates to 1. I reproduced the printed form.
- Eq. (6) of Theorem 2 (p. 166) is printed with a minus sign between the two terms ($\dots-ak_i\int_0^y\dots$). This conflicts with (5.3) and (6.4), which have a plus. I took it as a misprint and read it with a plus, as in (5.3) and (6.4).
- p. 176: "It remains to show that $\bar x=0$ if $a,p,k$ are suitably related" is followed by a condition ($k<a^2p$) under which (14.15) has a root at $x=0$, so $z(0)>0$. As printed, the claim and the condition do not obviously match (possibly $\bar x>0$ was meant); I report it as printed.
- p. 175: "From (9), we see that $f_0'(0)=-ap$" — the value follows from (14.12), not (14.9).
- On p. 160, the section cites the uniqueness theorem of Chapter IV, § 9; that theorem is not in these pages.
- p. 162: the text says $F(x)+kx$ is strictly increasing for $x\ge0$, but $F(x)+kx$ is constant on $[0,\bar x]$ and the argument only covers $x>\bar x$; I wrote $x>\bar x$.
