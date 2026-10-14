---
id: bellman-1957-dp/ch11-xi
work: bellman-1957-dp
unit: "11 Chapter XI. Markovian Decision Processes"
pages: 317-337
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Markovian Decision Processes (Bellman, Ch. XI)

## L0 — One line
Choosing, at every stage, the transition rule that maximizes the next state gives "max-linear" difference and differential equations, and Bellman proves, under suitable conditions, that they have unique solutions, are solved by successive approximation (including approximation in policy space), and have a Perron-root growth rate in the discrete positive case.

## L1 — The gist (≤ 120 words)
Bellman asks what happens when the coefficients of a linear Markov-type system are chosen at each step to maximize a state. This yields nonlinear equations such as $x_i(n+1)=\max_q\sum_j a_{ij}(q)x_j(n)$ and their continuous limits. Under suitable conditions he proves existence and uniqueness by successive approximation and an integral inequality. He shows that the Riccati equation (a first-order nonlinear ODE) is a minimum over linear equations. He shows that monotone "policy-space" approximation converges if off-diagonal coefficients are nonnegative (a sufficient condition). In the discrete positive case, growth is $\lambda^n$ with $\lambda$ the largest Perron root (dominant eigenvalue) over the policies, under a uniqueness assumption. He also treats min-max (two-person) versions and a von Neumann ratio-game limit.

**Prerequisites:** matrices and norms; linear ODEs and integrating factors; Picard-type successive approximation; positive matrices (Perron root); Brouwer fixed-point theorem; von Neumann min-max theorem.

## L2 — Key ideas
- Maximizing over the transition parameter $q$ at each stage turns a linear Markov recurrence into the nonlinear system $y_1(n+1)=\max_q\sum_j a_{1j}(q)y_j(n)$. The limit $\Delta\to0$ gives a max-linear ODE (pp. 318–319).
- Existence and uniqueness (Theorem 1) come from converting to an integral equation, a Lemma bounding the difference of two max-operators, factorial-bounded iterates, and a Gronwall-type inequality (an integral bound showing that $u\le\int fu$ forces $u=0$) (pp. 320–324).
- Uniqueness can fail when maximizing $q$ is not unique. A two-state example has infinitely many solutions. A unique solution is obtained, under the hypotheses of Theorem 1, if one restricts to solutions found by first solving for $x_2,\dots,x_N$ in terms of $x_1$ (pp. 324–325).
- The Riccati equation is rewritten as $v'=\min_w[\dots]$, so its solution equals a minimum over linear solutions (pp. 325–326).
- Approximation in policy space gives monotone, bounded and hence convergent iterates in the scalar case. For systems, $a_{ij}\ge0$ for $i\ne j$ is a sufficient condition for convergence (pp. 326–328).
- In the discrete positive case there is a unique growth rate $\lambda=\max_q\varphi(q)$ with a positive eigenvector. Under a uniqueness assumption, $x_i(n)\sim a y_i\lambda^n$ (pp. 328–332).
- The min-max extension (Theorem 4) and a ratio-game generalization of von Neumann (Theorem 5) follow by the same method (pp. 332–334).

## L3 — Walkthrough

### §1 Introduction (p. 317)
The chapter studies a new class of functional equations. Three types appear:
- discrete one-person: $x_i(n+1)=\max_q\sum_{j=1}^N a_{ij}(q)x_j(n)$, $x_i(0)=c_i$ (1.1);
- continuous one-person: $dx_i/dt=\max_q\sum_j a_{ij}(q)x_j(t)$, $x_i(0)=c_i$ (1.2);
- continuous two-person: $dx_i/dt=\max_q\min_p[\sum_j a_{ij}(p,q)x_j(t)]=\min_p\max_q[\dots]$ (1.3).

The ties to classical difference and differential equations are postponed to a second volume (p. 317).

### §2 Markovian decision processes (pp. 317–319)
A system $S$ is in one of the states $S_1,\dots,S_N$ at times $t=0,\Delta,2\Delta,\dots$. $x_i(t)$ is the probability of being in state $i$. The author stresses that the transition-probability assumptions are very strong (pp. 317–318).

Let $a_{ij}$ be the probability of being in state $i$ at $t+\Delta$ given state $j$ at $t$. Then
$$x_i(t+\Delta)=\sum_{j=1}^N a_{ij}x_j(t),\qquad(2.2)$$
and with $y_i(n)=x_i(n\Delta)$:
$$y_i(n+1)=\sum_j a_{ij}y_j(n).\qquad(2.3)$$
The asymptotic behaviour is determined by the characteristic roots of $A=(a_{ij})$. This is a Markoff process (p. 318).

**Decision version.** Let $a_{ij}$ depend on a parameter $q$ (possibly a vector). At each stage, $q$ is chosen to maximize the probability of state $S_1$:
$$y_1(n+1)=\max_q\sum_j a_{1j}(q)y_j(n),\qquad y_i(n+1)=\sum_j a_{ij}(q^*)y_j(n),\ i=2,\dots,N,\qquad(2.4)$$
where $q^*=q^*(n)$ is one of the maximizing values for $y_1(n+1)$. Probabilities require $a_{ij}\ge0$, $\sum_i a_{ij}=1$ for all $q$ (p. 318; this condition is also numbered (4) in print).

**Generalization.** For $N$ item types with quantities $x_i(t)$, $a_{ij}>0$ means production of item $j$ from item $i$ and $a_{ij}<0$ means consumption. The goal is to maximize the first item. This gives (2.4) with no sign or size restriction on $a_{ij}$ (pp. 318–319).

**Continuous limit.** Set $a_{ij}=b_{ij}\Delta$ ($i\ne j$), $a_{ii}=1-b_{ii}\Delta$ (2.6), and let $\Delta\to0$:
$$\frac{dx_1}{dt}=\max_q\sum_j b_{1j}(q)x_j(t),\ x_1(0)=c_1;\qquad \frac{dx_i}{dt}=\sum_j b_{ij}(q^*)x_j(t),\ i\ge2.\qquad(2.5)$$
The process is then defined by (2.5), which requires proving existence and uniqueness (p. 319).

*Intuition note:* Choosing the best transition rule at every step breaks linearity, because "max" of linear maps is not linear. The rest of the chapter checks that this nonlinear object is still well defined.

### §3 Notation (pp. 319–320)
In vector form, $dx/dt=\max_q A(q)x$, $x(0)=c$ (3.3). The maximum is taken element by element: each row $i$ has its own set of parameters $q_{i1},\dots,q_{ik}$, so the row maximizations do not interact (3.4). The interacting case of (2.5) comes later. Norms: $\|x\|=\sum_i|x_i|$, $\|A\|=\sum_{i,j}|a_{ij}|$, and $\|Ax\|\le\|A\|\,\|x\|$ (numbered (10) in print; p. 320).

### §4 A lemma (pp. 320–321)
General problem: $dx/dt=\max_q[A(q,t)x+b(q,t)]$, $x(0)=c$ (4.1). It is converted to the integral equation
$$x=c+\int_0^t\max_q[A(q,s)x+b(q,s)]\,ds,\qquad(4.2)$$
which equals $x=\max_q[c+\int_0^t b\,ds+\int_0^t Ax\,ds]$ (4.3). Pointwise maximization yields global maximization because $q$ is a function of $t$ (p. 320).

**Lemma.** Let $T_1(x)=\max_q[b_1(q,t)+\int_0^tA(q,s)x\,ds]$ and $T_2(y)=\max_q[b_2(q,t)+\int_0^tA(q,s)y\,ds]$. Then
$$\|T_1(x)-T_2(y)\|\le\max_q\Big[\|b_1(q,t)-b_2(q,t)\|+\int_0^t\|A(q,s)\|\,\|x-y\|\,ds\Big].\qquad(4.5)$$
The author gives no proof; he says it is easy to show in much the same way as Lemma 1 of Chapter 2 (pp. 320–321).

### §5 Existence and uniqueness—I (pp. 321–324)
**Theorem 1.** Let $q$ range over a set $S$ of functions with $\|A(q,t)\|,\|b(q,t)\|\le f(t)$, where $f$ is integrable over every finite interval $[0,T]$. Assume the maximum of $A(q,t)x+b(q,t)$ is attained for some $q\in S$ for every fixed $t$ and $x$. Then (5.1) has a unique solution, satisfying the equation almost everywhere. It is the limit of
$$x_0=c,\qquad x_{n+1}=c+\max_q\int_0^t[A(q,s)x_n+b(q,s)]\,ds.\qquad(5.3)$$
The footnote says the "attained" assumption covers both discrete $q$ (always attained) and continuous $q$ (p. 321).

*Proof, boundedness.* Claim: $\|x_n\|\le a\exp(\int_0^tf\,ds)$ with $a=\|c\|+\int_0^tf\,ds$ (5.3–5.4 of the proof). It holds for $n=0$. Inductively,
$$\|x_{n+1}\|\le\|c\|+\int_0^t\max_q\|b\|\,ds+\int_0^t\max_q\|A\|\,\|x_n\|\,ds\le a+\int_0^tf\|x_n\|\,ds.$$
Inserting the bound gives $\|x_{n+1}\|\le a+\int_0^tf(s)\,a\exp(\int_0^sf)\,ds$, the same bound. (added step: the right side equals $a+a(e^{\int_0^tf}-1)=a\,e^{\int_0^tf}$.) (p. 322)

*Convergence.* Apply the Lemma to the relations for $x_{n+1}$ and $x_n$:
$$\|x_{n+1}-x_n\|\le\max_q\int_0^t\|A\|\,\|x_n-x_{n-1}\|\,ds\le\int_0^tf\,\|x_n-x_{n-1}\|\,ds.\qquad(8)$$
Iterating from $\|x_1-x_0\|$:
$$\|x_{n+1}-x_n\|\le(\|c\|+1)\frac{(\int_0^tf\,ds)^{n+1}}{(n+1)!}.\qquad(9)$$
So $x_n\to x(t)$ uniformly on $[0,T]$. The limit is continuous and satisfies $x(t)=c+\int_0^t\max_q[A x+b]\,ds$ (10), hence the differential equation almost everywhere (p. 323).

*Uniqueness.* Let $y$ be another solution on $[0,S]$. The Lemma gives $\|x-y\|\le\int_0^tf\|x-y\|\,ds$. Writing $u=\|x-y\|$: $u(t)\le\int_0^tf u\,ds$ (12), with $f,u\ge0$. For any small $a>0$, $u\le a+\int_0^tf u\,ds$ (13). Dividing, $f u/(a+\int_0^tf u\,ds)\le f$ (14). Integrating gives $a+\int_0^tf u\,ds\le a\,e^{\int_0^tf\,ds}$ (15). With (13): $u(t)\le a\,e^{\int_0^tf\,ds}$ (16). Since $a$ is arbitrary, $u\equiv0$ (p. 323).

*Alternative proof.* Let $b$ bound $\|x-y\|$. Then $u\le b\int_0^tf$ (17), $u\le b\int_0^tf(s)\int_0^sf(s_1)ds_1ds=\frac{b}{2!}(\int_0^tf)^2$ (18), and in general
$$u(t)\le\frac{b^n}{(n+1)!}\Big(\int_0^tf\,ds\Big)^{n+1}\qquad(19)$$
(as printed; see Reading notes). Letting $n\to\infty$, $u\equiv0$ (p. 324).

*Intuition note:* Each Picard iterate differs from the previous one by a factorially shrinking amount, so the sequence converges. The Gronwall-type inequality (13)–(16) says an error that is bounded by its own accumulated integral must be zero. The "max" is harmless because the Lemma lets us pass the maximum through the norm.

### §6 Existence and uniqueness—II (pp. 324–325)
For the interacting system (2.5), solutions need not be unique when the maximizing $q$ is not unique. **Example** (6.1):
$$\frac{dx_1}{dt}=\max_q[1-q^2(1-q)^2]+x_2,\ x_1(0)=0;\qquad \frac{dx_2}{dt}=q^*x_2,\ x_2(0)=1.$$
Since $q^*=0$ or $1$, there are infinitely many solutions, for example $x_1=2t,\,x_2=1$ and $x_1=t+(e^t-1),\,x_2=e^t$ (6.2) (p. 324).

Uniqueness theorems are available for solutions obtained as follows. First solve
$$dx_k/dt=b_k(q,t)+\sum_ja_{kj}(q)x_j,\ x_k(0)=c_k,\ k=2,\dots,N$$
(6.3) for $x_2,\dots,x_N$ in terms of $x_1$, treating $q$ as an unknown function. Each has the form $x_k=u_k(q,t)+\int_0^tv_k(q,t,s)x_1(s)\,ds$ (6.4). Substituting into $dx_1/dt=\max_q[b_1+\sum_ja_{1j}x_j]$ (6.5) gives
$$\frac{dx_1}{dt}=\max_q\Big[b(q,t)+a_{11}(q)x_1+\int_0^tv(q,t,s)x_1(s)\,ds\Big].\qquad(6.6)$$
Integrating in $t$ gives (6.7). The methods of §5 then give a unique solution under the hypotheses of Theorem 1 (p. 325).

### §7 Existence and uniqueness—III (p. 325)
The author says the same successive-approximation technique can give analogues for $dx/dt=\max_qf(x,q,t)$, $x(0)=c$. The author leaves this to the reader because it belongs to differential equations, not decision theory.

### §8 The Riccati equation (pp. 325–326)
The substitution $v=u'/u$ turns $u''+p(t)u'+q(t)u=0$ (8.2) into the nonlinear first-order Riccati equation $v'+v^2+p(t)v+q(t)=0$ (8.3). Its general solution is equivalent to that of (8.2), so in general it cannot be had explicitly in quadratures (p. 326).

Since $-v^2=\min_w(w^2-2wv)$ (8.4), we get
$$v'=\min_w[w^2-2wv-p(t)v-q(t)],\qquad(8.5)$$
with $w$ ranging over functions of $t$. For fixed $w$ let $V(w,t)$ solve $V'=w^2-2wV-p(t)V-q(t)$, $V(0)=v(0)=c$ (8.6). By an integrating factor,
$$V=c\,e^{-\int_0^t(p(s)+2w)ds}+\int_0^t(w^2-q(s))\,e^{-\int_s^t(p(s_1)+2w)ds_1}\,ds.\qquad(8.7)$$
**Claim:** $v=\min_wV(w,t)$ (8.8). *Proof.* For any $w$: $v'\le w^2-2wv-p\,v-q$ (8.9), "which shows" $v\le V(w,t)$ (the step uses positivity of the linear solution operator, as in §9; added comment). So $v\le\min_wV$. For the minimizing $w^*$ (which is actually $v(t)$), $v=V(w^*,t)$. Hence equality (p. 326).

*Intuition note:* A nonlinear equation is written as the lower envelope of a family of linear equations whose solutions are known in closed form. The solution is then "quadratures plus a minimization".

### §9 Approximation in policy space (pp. 326–328)
Two types of successive approximation exist: approximating the functions (the text says this method was applied "above in § 3"; the successive approximation of Theorem 1 is in §5) and approximating the policies (p. 326).

**Scalar case.** $du/dt=\max_q[b(q,t)+a(q,t)u]$, $u(0)=c$ (9.1), with $|a|,|b|\le f(t)$ and $f$ of finite integral. Procedure (pp. 327–328):
1. Guess a policy $q_0(t)$; solve $du_0/dt=b(q_0,t)+a(q_0,t)u_0$, $u_0(0)=c$ (9.2).
2. Choose $q_1$ to maximize $b(q,t)+a(q,t)u_0$; solve $du_1/dt=b(q_1,t)+a(q_1,t)u_1$, $u_1(0)=c$ (9.3). Continue to get $\{u_n\},\{q_n\}$.
3. By the definition of $q_1$, $du_0/dt\le b(q_1,t)+a(q_1,t)u_0$ (9.4).
4. The solution of $dv/dt=g(t)v+h(t)$, $v(0)=c$ is $v=c\,e^{\int_0^tg}+\int_0^th(s)e^{\int_s^tg(t_1)dt_1}ds=:L(h)$ (9.5–9.6). Since the exponential is $\ge0$, $L(h_1)\ge L(h_2)$ whenever $h_1\ge h_2$ for $t\ge0$ (9.7).
5. Hence $u_0\le u_1$ (9.8), and inductively $u_n\le u_{n+1}$. Each $u_n$ is bounded by $(c+\int_0^Tf)e^{\int_0^Tf}$, so $u_n\to u$. The limit satisfies $u=c+\int_0^t\max_q[b+a\,u]\,ds$ (9.9), hence the equation almost everywhere (p. 328).

**Systems.** For $dx/dt=\max_q[b(q,t)+A(q,t)x]$ (9.10), the question reduces to conditions on $A$ so that $f(t)\ge0$ implies $y\ge0$, where $dy/dt=A(q,t)y+f(t)$, $y(0)=0$ (9.11). The solution is $\int_0^tY(t)Y^{-1}(s)f(s)\,ds$ (9.12), with $dY/dt=A(q,t)Y$, $Y(0)=I$ (9.13). A necessary and sufficient condition is
$$Y(t)Y^{-1}(s)\ge0\ \text{for }t\ge s\ge0,\ \text{uniformly for }q\in S.\qquad(9.14)$$
This is hard to verify. A sufficient condition is $a_{ij}(q,t)\ge0$ for $i\ne j$. If it holds for $t\ge0$ and all $q\in S$, policy-space approximation converges (p. 328).

*Intuition note:* Improving the policy against the current solution can only raise the solution, and the solutions are bounded above, so they must converge. For systems, the same "improve means increase" property needs the linear flow to preserve positivity, which off-diagonal nonnegativity ensures.

### §10 Discrete versions (pp. 328–330)
Question: the behaviour of $x_i(n+1)=\max_q\sum_ja_{ij}(q)x_j(n)$, $n\ge0$ (10.1). Start with the homogeneous equation
$$\lambda y_i=\max_q\sum_ja_{ij}(q)y_j,\ i=1,\dots,N.\qquad(10.2)$$
Conditions (10.3): (a) $q=(q_1,\dots,q_N)$ ranges over a set $S$ such that the maximum in (10.1) is attained for any parameters $(y_1,\dots,y_N)$; (b) $0<a_{ij}(q)\le m<\infty$; (c) $\varphi(q)$ denotes the Perron root of $A(q)$ (characteristic root of largest absolute value), and $\varphi$ is assumed to attain its maximum on $S$ (p. 329).

**Theorem 2.** Under these assumptions there is a unique positive constant $\lambda$ for which (10.2) has a positive solution $y_i>0$. The solution is unique up to a multiplicative constant, and
$$\lambda=\max_{q\in S}\varphi(q).\qquad(10.4)$$

*Proof, existence.* On the simplex $y_i\ge0,\ \sum y_i=1$ (10.5), the normalized map
$$y_i'=\Big[\max_q\sum_ja_{ij}(q)y_j\Big]\Big/\sum_{i}\max_q\Big[\sum_ja_{ij}(q)y_j\Big]\qquad(10.6)$$
is continuous into itself. By Brouwer it has a fixed point, which is positive since $a_{ij}>0$. $\lambda$ is the denominator (p. 329).

*Uniqueness up to scale.* Let $[\mu,z]$ be another solution, $\mu>0$, $z$ positive. Let $q$ attain the maximum for $y$ and $\bar q$ for $z$. Then
$$\lambda y_i=\sum_ja_{ij}(q)y_j\ge\sum_ja_{ij}(\bar q)y_j,\qquad\mu z_i=\sum_ja_{ij}(\bar q)z_j.\qquad(10.7)$$
Assume without loss of generality $\lambda<\mu$; then $y,z$ are non-proportional (if proportional, $y=z$). Choose $\varepsilon>0$ so that all $y_i-\varepsilon z_i\ge0$ with at least one zero and one positive. At an index $i$ where it is zero:
$$0=\mu(y_i-\varepsilon z_i)>\lambda y_i-\varepsilon\mu z_i\ge\sum_ja_{ij}(\bar q)(y_j-\varepsilon z_j)>0,\qquad(10.8)$$
a contradiction. So $y,z$ are proportional and $\lambda=\mu$ (p. 330).

*Value of $\lambda$.* Let $\mu=\max_q\varphi(q)$. As the root of some $A(q)$, $\lambda\le\mu$. Suppose $\lambda<\mu$. Let $z>0$ be a characteristic vector for $\mu$, $\mu=\varphi(\bar q)$. Then $\mu z_i=\sum_ja_{ij}(\bar q)z_j\le\max_q\sum_ja_{ij}(q)z_j$ (10.9). Choose $m>0$ with $z_i\le my_i$ (10.10). Then $\mu z_i\le\max_q(\sum_ja_{ij}(q)y_j)\,m=m\lambda y_i$ (10.11). So $z_i\le my_i\lambda/\mu$, and iterating $z_i\le my_i(\lambda/\mu)^k\to0$, a contradiction. Hence $\lambda=\mu$ (p. 330).

*Intuition note:* The best "growth factor" of a system that picks its row of coefficients freely at every step is the largest Perron root among the allowed coefficient matrices. The positive eigenvector is the shape of the long-run state.

### §11 The recurrence relation (pp. 330–332)
**Theorem 3.** In addition to (10.3), assume there is a unique $q$ at which $\varphi$ is maximal, and $c_i\ge0$. Then $x_i(n)\sim a\,y_i\lambda^n$ as $n\to\infty$, with $a=a(c_1,\dots,c_N)$ (p. 330).

*Proof.* Take $c_i>0$ (the author says without loss of generality). There are $k,K>0$ with $ky_i\le c_i\le Ky_i$. Induction gives
$$k\,y_i\lambda^n\le x_i(n)\le K\,y_i\lambda^n,\qquad(2)$$
since $x_i(n+1)\le K\lambda^n\max_q\sum_ja_{ij}y_j=K\lambda^{n+1}y_i$, and likewise for the lower bound (3) (p. 331).

Then the author announces that he will show that for sufficiently large $n$ the maximizing $q$-set is precisely the one maximizing $\varphi$. Suppose instead a set $\bar q\ne q^*$ is used infinitely often. Then $x_i(n+1)=\sum_ja_{ij}(\bar q)x_j(n)\le(\sum_ja_{ij}(\bar q)y_j)K\lambda^n$ (4). For some $i$, $\sum_ja_{ij}(\bar q)y_j<\lambda y_i$ strictly (5). Otherwise the root of $A(\bar q)$ would be at least $\lambda=\max\varphi$, contradicting uniqueness of the maximum. So for some component, say the first, $x_1(n+1)\le\theta K\lambda^{n+1}y_1$ with $0<\theta<1$ (6). Since $a_{ij}(q^*)>0$,
$$x_i(n+2)\le K\lambda^{n+1}\Big[\sum_{j\ge2}a_{ij}(q^*)y_j+\theta a_{i1}(q^*)y_1\Big]\le\theta_1K\lambda^{n+2}y_i,\ \theta_1<1.\qquad(7)$$
If a set other than $q^*$ is used $R$ times, then $x_i(n)\le\theta_1^RK\lambda^ny_i$ for large $n$ (8). For large $R$ this contradicts the lower bound. So non-$q^*$ sets are used only a bounded number of times, with a bound determined by $k$ and $K$ (p. 332). The text ends there; it does not spell out the final passage to (1).

### §12 Min-max (p. 332)
**Theorem 4.** Consider $dx/dt=\max_p\min_q[A(p,q,t)x+b(p,q,t)]=\min_q\max_p[\dots]$, $x(0)=c$. Assume (a) for fixed $x,t$ the max-min equals the min-max, with $p,q$ over some admissible set $S$; (b) $\max_S\|A\|,\max_S\|b\|\le f(t)$ with $\int_0^Tf<\infty$. Then there is a unique solution on $0\le t\le T$ satisfying the equation almost everywhere. It is the limit of $x_0=c$, $x_{n+1}=c+\int_0^t\max_p\min_q[Ax_n+b]\,ds=c+\int_0^t\min_q\max_p[\dots]\,ds$. The proof is "the same method" as Theorem 1.

### §13 Generalization of a von Neumann result (pp. 332–334)
From the multi-stage-games chapter (stated as established there):
$$\max_p\min_q\frac{(Ap,q)}{(Bp,q)}=\min_q\max_p\frac{(Ap,q)}{(Bp,q)},\qquad(13.1)$$
with $A,B$ matrices, $p,q$ probability vectors, and $(Bp,q)\ge d>0$ for all $p,q$ (pp. 332–333).

**Theorem 5.** Consider $du/dt=\max_p\min_q[(Ap,q)-(Bp,q)u]=\min_q\max_p[\dots]$, $u(0)=c$ (13.2). If $(Bp,q)\ge d>0$ for all probability vectors, then
$$\lim_{t\to\infty}u(t)=\max_p\min_q\frac{(Ap,q)}{(Bp,q)}=\min_q\max_p\frac{(Ap,q)}{(Bp,q)}.\qquad(13.3)$$

*Proof.* Von Neumann's min-max theorem gives max-min = min-max for each $u$. The other conditions of Theorem 4 hold, giving existence and uniqueness (p. 333). For the limit, first take $du/dt=a-bu$ with $b>0$ (13.4). The solution is bounded. Where $du/dt=0$ we must have $u=a/b$, so $u$ has at most one turning point and is ultimately monotone. Being bounded, it tends to a finite limit, which must be $a/b$. For $du/dt=\max_p[a(p)-b(p)u]$ with $b(p)\ge b>0$ and $|a(p)|\le M$ (13.5), at a turning point $u=\max_pa(p)/b(p)$ (13.6). So $u$ is ultimately monotone with that limit. The same argument works for (13.2), where a turning point has $u=\max_p\min_q\frac{(Ap,q)}{(Bp,q)}=\min_q\max_p\frac{(Ap,q)}{(Bp,q)}$ (13.7) (p. 334).

*Intuition note:* The ODE has a single resting value, the value of the ratio game. Since the solution can turn only at that value, a bounded solution cannot oscillate and must settle there.

### Bibliography and comments (pp. 336–337)
The source notes that inequality (5.13)→(5.16) is a fundamental inequality for boundedness and stability of solutions of differential equations, and cites the author's earlier papers for §§1, 5, 8, 10, 13 (p. 336–337).

## Toy example (our own)
Take $N=2$, $x(0)=(2,1)$. Row 1 chooses between coefficient rows $(3,1)$ and $(1,3)$; row 2 chooses between $(2,1)$ and $(1,2)$. All entries are positive.

- $n=0$: row 1: $3\cdot2+1=7$ vs $2+3\cdot1=5$ → $7$. Row 2: $2\cdot2+1=5$ vs $2+2\cdot1=4$ → $5$. So $x(1)=(7,5)$.
- $n=1$: row 1: $21+5=26$ vs $7+15=22$ → $26$. Row 2: $14+5=19$ vs $7+10=17$ → $19$. So $x(2)=(26,19)$.
- $n=2$: row 1: $78+19=97$ vs $26+57=83$. Row 2: $52+19=71$ vs $26+38=64$. So $x(3)=(97,71)$.

At each of these three steps the chosen rows are $(3,1)$ and $(2,1)$, so $A^*=\begin{pmatrix}3&1\\2&1\end{pmatrix}$. Its Perron root solves $\lambda^2-4\lambda+1=0$, so $\lambda=2+\sqrt3\approx3.732$. The other three policies give $(5+\sqrt5)/2\approx3.618$, $(3+\sqrt{13})/2\approx3.303$ and $1+\sqrt6\approx3.449$, all smaller. So $\lambda=\max_q\varphi(q)$, as in Theorem 2.

The eigenvector is $y\approx(1,0.732)$. Check: $3+0.732=3.732=\lambda\cdot1$, and $2+0.732=2.732=\lambda\cdot0.732$. The alternative rows give less ($1+3\cdot0.732=3.196$; $1+2\cdot0.732=2.464$), as (10.2) requires. The ratios $97/26\approx3.731$ and $71/19\approx3.737$ are near $\lambda$, and $x(3)=(97,71)$ has ratio $71/97\approx0.732$, matching $y$, as Theorem 3 predicts.

## Concepts
- [[markov decision process]] — here: states with transition probabilities $a_{ij}(q)$, $q$ chosen at each stage to maximize the probability of $S_1$ (pp. 318–319)
- [[policy]] — here the function $q(t)$ (or $q_n$) choosing coefficients; improved iteratively in §9 (p. 327)
- [[max-linear-system]] (new) — $x'=\max_qA(q)x$ with row-wise independent maximization (p. 320)
- [[successive-approximation]] (new) — iterates (5.3) converging by factorial bounds (pp. 321–323)
- [[gronwall-type-inequality]] (new) — $u\le a+\int fu\ \Rightarrow\ u\le a\,e^{\int f}$ (p. 323)
- [[approximation-in-policy-space]] (new) — improve $q_n$ against $u_{n-1}$; monotone convergence (pp. 326–328)
- [[riccati-equation]] (new) — $v'+v^2+pv+q=0$, written as a minimum over linear equations (pp. 325–326)
- [[perron-root]] (new) — largest-modulus eigenvalue of a positive matrix; here $\lambda=\max_q\varphi(q)$ (pp. 329–330)
- [[eigenvalues and modes]] — canon concept; here used for the growth rate $\lambda$ of the max-linear recurrence (p. 329)

## Canonical instances
- [[maximize-state-one-probability]] — decision process maximizing the probability of $S_1$ (p. 318)
- [[nonunique-maxima-counterexample]] — two-state example with infinitely many solutions (p. 324)
- [[riccati-as-min-of-linear]] — $v=\min_wV(w,t)$ (p. 326)
- [[merchant-pricing]] — exercises 1–8: selling $n$ items by price $z$ with sale probability $\varphi(z)$ (pp. 334–335)

## Bridges (candidates)
- [structural-analogy] approximation in policy space (§9) ↔ control-theory canon "policy": improve the policy against the current value, with monotone convergence — resembles policy iteration, but the text does not say so.
- [structural-analogy] Riccati equation as $\min_w$ of linear equations (§8) ↔ LQR: a Riccati equation arising from minimizing over linear feedback-like choices.
- [structural-analogy] $\lambda=\max_q\varphi(q)$ with a positive eigenvector ↔ average-reward / growth-rate problems in MDPs: the optimal long-run rate is a dominant eigenvalue.
- [structural-analogy] Gronwall-type inequality (5.13–5.16) ↔ stability: bounds on solutions of perturbed linear systems.

## Questions this raises
- How restrictive is the "no interaction between rows" assumption (3.4), and what exactly is lost in the interacting case of §6?
- Why is nonnegativity of $Y(t)Y^{-1}(s)$ the right condition in (9.14), and how does it relate to $a_{ij}\ge0$ for $i\ne j$?
- What happens to Theorems 2–3 if some $a_{ij}(q)=0$ or the maximizing policy is not unique?
- How does Theorem 5's ratio game relate to the discrete-time results of the multi-stage games chapter?

## Exercises worth doing
- Ex. 1 (p. 334) — derive the stochastic recurrence for expected return from selling $n$ items by price — difficulty: medium
- Ex. 2 (p. 334) — take the continuous-time limit of Ex. 1 (compare the limit procedure of §2) — difficulty: medium
- Ex. 3–4 (p. 334–335) — the $N=1$ case: show $f_1(t)=\max_zF(t,z)$ (Ex. 3) and that the max-equation is equivalent to two equations, one a stationarity condition in $z$ (Ex. 4) — difficulty: medium
- Ex. 12 (pp. 335–336) — show a Riccati successive-approximation scheme is policy-space approximation, with monotone iterates — difficulty: hard
- Ex. 14 (p. 336) — relate this approximation to Newton's method — difficulty: medium

## Reading notes
- Printed = pdf − 23. Printed page labels are given in the page headers.
- OCR: many symbols are garbled in the text layer; math was checked against the images.
- Print numbering quirks: the probability conditions on p. 318 are labelled (4), duplicating the equation number; $\|Ax\|\le\|A\|\|x\|$ on p. 320 is labelled (10) (likely for (6)); equations in §5's proof are numbered (3)–(19) alongside the theorem's own (3).
- Misprint-like: in (5.19) (p. 324) the image shows $b^n/(n+1)!$; from (17)–(18) the factor looks like $b$ (not $b^n$). I kept the printed form. The conclusion $u\equiv0$ is unaffected.
- (9.11)–(9.12) use $y$ and then $w$ for the same solution; the integrability condition after (9.1) is printed with upper limit $t_0$ (the image reads $\int_0^{t_0}f\,dt<\infty$), while later pages use $\int_0^Tf$.
- (2.6): with $a_{ii}=1-b_{ii}\Delta$, the limit of $(x_i(t+\Delta)-x_i(t))/\Delta$ gives a diagonal term $-b_{ii}$, whereas (2.5) sums $b_{ij}x_j$ over all $j$ (added observation; the text does not comment). In (8.9) the step $v\le V(w,t)$ is given without detail.
- At the start of §9 (p. 327) the text says the traditional method was applied "above in § 3"; the successive approximation appears in §5. Theorem 3 states $c_i\ge0$; the proof assumes $c_i>0$. The final passage from "bounded number of non-$q^*$ steps" to (11.1) is not written out.
- Exercise 3 refers to "Problem 4" and Exercise 8 to "Problem 1"; these apparently mean Exercises 2 and 1. Exercise 2 as printed: $f_N(0)=0$, $f_0(t)=0$.
