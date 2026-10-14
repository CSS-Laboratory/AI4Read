---
id: bellman-1957-dp/ch01-i-p3
work: bellman-1957-dp
unit: "Chapter I (part 3/3): end of §25, §26 Stieltjes integrals, Exercises and Research Problems 1–78, Bibliography and Comments"
pages: 40–60
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
# Chapter I, part 3: the stochastic recurrence, Stieltjes form, and the problem set

## L0 — One line
If we judge a policy by its expected value, a stochastic multi-stage allocation process gives a recurrence with the same analytic form as the deterministic one, and a Stieltjes integral writes that recurrence compactly.

## L1 — The gist (≤ 120 words)
This part closes the stochastic allocation process of Chapter I. Question: how does randomness change the recurrence for the optimal return? Answer: if the "expected value" measures a policy, the equations keep the deterministic structure; a distribution function $dG$ turns them into short integral equations. The rest of the unit is 78 exercises and research problems. Many of them use the same recurrence idea on products, sums of powers, convex and concave returns, cattle breeding, investment, search, machine replacement, inventory of parts, and more. A short bibliography ends the chapter. The unit matters because it shows how widely the same set-up (a one-stage function, then a recurrence) is applied.

**Prerequisites:** the recurrence $f_N(x)=\max_y[\dots+f_{N-1}(\cdot)]$ from earlier in Chapter I; expected value; the idea of an integral against a distribution.

## L2 — Key ideas (5–10 bullets)
- With two random outcomes of probabilities $p_1,p_2$, the recurrence for $f_{N+1}$ is the probability-weighted sum of the two deterministic-looking branches, still under $\max_{0\le y\le x}$ (p. 40).
- Using the expected value as the measure of a policy removes the stochastic aspects, "at least as far as the analysis is concerned" (p. 40).
- A distribution function $dG(u,v;x,y)$ for (return, remaining quantity) gives $f_1$ and $f_{N+1}$ as Stieltjes integrals (integrals taken against a distribution function). This eases existence, uniqueness and analytic-property work (p. 40).
- Exercises 1–15 apply the recurrence to products, sums of powers, and concave or convex separable sums. They aim at closed forms and the structure of optimal policies, including the arithmetic–geometric mean inequality (pp. 40–44).
- Exercises 16–29 vary the §2 process and treat integer loading, cattle breeding, investment, and a dating problem with stochastic elements (pp. 44–47).
- Exercises 30–48 cover chain constraints, approximation, travel at fixed speed, quadratic forms, probabilistic sequential processes, and machine replacement (pp. 47–50).
- Exercises 49–78 mix search, success-probability equations, production, spare parts, gambling, multiple capitals, and a Lagrange-multiplier link $\lambda=f_N'(c)$ (pp. 50–59).
- The bibliography gives sources and remarks per section. It notes that limited machine storage makes one "quite stingy with subscripts" (p. 59) and cites a paper titled "Optimal Search is Fibonaccian" (p. 60).

## L3 — Walkthrough

### §25 (end of the section): the stochastic recurrence (p. 40)
This part starts mid-section. The page shows the last line of the recurrence for a process with two possible outcomes, probabilities $p_1$ and $p_2$. For $N\ge 1$ (p. 40):

$$f_{N+1}(x)=\max_{0\le y\le x}\Big[p_1\big[g_1(y)+h_1(x-y)+f_N(a_1y+b_1(x-y))\big]+p_2\big[g_2(y)+h_2(x-y)+f_N(a_2y+b_2(x-y))\big]\Big].$$

Symbols: $y$ is the amount allocated to the first use, $x-y$ the rest; $g_i,h_i$ are returns; $a_iy+b_i(x-y)$ is the quantity left for the next stage if outcome $i$ occurs. Their definitions are in the earlier part of the chapter, not on these pages; this reading is inferred from the later text on p. 40 ("a return of $u$ and a remaining quantity of $v$").

The author says this has the same analytic structure as the deterministic equations. Agreeing to use the "expected value" as the measure of a policy eliminates the stochastic aspects, at least for the analysis (p. 40).

*Intuition note.* Averaging over outcomes happens inside the bracket, and the choice $y$ is made before the outcome is known. So the stochastic problem is still one maximisation per stage. Only the bracket gets longer.

### §26 Stieltjes integrals (p. 40)
For readers who know the Riemann–Stieltjes integral (an integral against a distribution function), the equations can be shortened.

(1) $dG(u,v;x,y)$ is the distribution function of a return $u$ and a remaining quantity $v$, starting with quantity $x$ and allocating $y$.

With $f_N$ as before, the author obtains (2):

$$f_1(x)=\max_{0\le y\le x}\int u\,dG(u,v;x,y),\qquad f_{N+1}(x)=\max_{0\le y\le x}\int\,[u+f_N(v)]\,dG(u,v;x,y).$$

Claims (author): this notation makes it much simpler to describe the processes, to establish existence and uniqueness theorems for the functional equations, and to derive analytic properties of the solution. The basic mathematical ideas are the same. Equations of this type return in Chapter III in a more general framework (p. 40).

*Intuition note.* $dG$ packs all randomness into one object. A two-outcome case is a $dG$ with two point masses, so the integral becomes the $p_1,p_2$ sum above.

### Exercises and Research Problems for Chapter I (pp. 40–59)
No solutions are printed in this unit. Some problems carry credits to other people (Ex. 35, 49, 70, 73) and Ex. 77 gives a literature reference. Numbers follow the book. I describe each group without solving it.

**Products and sums of powers (Ex. 1–4, pp. 40–41).**
- Ex. 1: $f_N(a)=\max_R x_1x_2\cdots x_N$ with $x_1+\dots+x_N=a>0$, $x_i\ge0$. Prove $f_N(a)=\max_{0\le x\le a}x\,f_{N-1}(a-x)$ for $N\ge2$, with $f_1(a)=a$.
- Ex. 2: show inductively $f_N(a)=a^N/N^N$, hence the arithmetic–geometric mean inequality $\big(\frac{x_1+\dots+x_N}{N}\big)^N\ge x_1\cdots x_N$ for $x_i\ge0$, with equality only if all $x_i$ are equal.
- Ex. 3: for $f_N(a)=\min\sum x_i^p$, $p>0$, subject to $\sum x_i\ge a>0$, $x_i\ge0$, show $f_N(a)=\min_{0\le x\le a}[x^p+f_{N-1}(a-x)]$, $f_1(a)=a^p$.
- Ex. 4: show $f_N(a)=a^pc_N$ with $c_N=\min_{0\le x\le1}[x^p+(1-x)^pc_{N-1}]$. Determine $c_N$ for $0\le p<1$ and for $1<p$.

**Concave and convex separable problems (Ex. 5–15, pp. 41–44).**
- Ex. 5: minimise $\sum p_is_i/(s_i+x_i)$ ($p_i>0$, $\sum p_i=1$, $s_i>0$, $x_i\ge0$, $\sum x_i=a$). Obtain the recurrences. Show that, after suitable reordering, the solution has $x_j=0$ for $j\le t$ and $x_j>0$ for $t+1\le j\le N$.
- Ex. 6: maximise $\sum\varphi(x_i)$ with $\sum x_i=c$. Show the maximum is $\varphi(c)$ if $\varphi$ is convex.
- Ex. 7: for $\varphi$ monotone increasing and strictly concave, show the solution of $f_N(c)=\max_{0\le y\le c}[\varphi(y)+f_{N-1}(c-y)]$, $f_1=\varphi$, has $y_N=0$ for $0\le c\le c_N$ and $y_N=z_N$ for $c>c_N$. Here $z_N$ is the unique solution of $\varphi'(y)=f_{N-1}(c-y)$. Show how to find $\{c_N\}$.
- Ex. 8: do this explicitly for $\varphi(y)=y-by^2$, $b>0$, $0\le c\le 1/2b$.
- Ex. 9–10: analogues for $\sum\varphi_i(x_i)$, and for minimising with $\varphi$ non-negative, increasing, strictly convex, e.g. $\varphi(x)=x+bx^2$.
- Ex. 11: a two-resource problem $f_N(c_1,c_2)=\max[\varphi(x,y)+f_{N-1}(c_1-x,c_2-y)]$ with $\varphi$ strictly concave and monotone increasing in $x$ and $y$. The solution has four regions in the $(c_1,c_2)$ plane (Figure 6): $x=0$ with $0<y<c_2$; $x=y=0$; $0<x<c_1$ with $y=0$; and both positive. Show how to find the boundary curves. The quadratic case is $\varphi=u_1x+v_1y+u_2x^2+2u_3xy+u_4y^2$.
- Ex. 12–14: variants with constraints $\sum x_i\le c_1$ and $\sum x_i^p\le c_2$ ($p>1$, $p<1$); minimisation with constraints $\sum\psi_i(x_i)\ge a$ and bounds $0\le x_i\le r_i$; and a multi-dimensional version.
- Ex. 15: maximise $x_1\cdots x_N$ with $\sum x_i=1$ and $bx_k\le x_{k+1}$, $b>1$; the same with $\sum x_i^p$ for different ranges of $p$.

**Variations on the §2 process (Ex. 16–20, pp. 44–45).**
- Ex. 16: with $g(y)=c_1y^d$, $h(y)=c_2y^d$, $c_1,c_2,d>0$, show $f_N(x)=u_Nx^d$. Here $u_1=\max_{0\le v\le1}[c_1v^d+c_2(1-v)^d]$ and $u_{N+1}=\max_v[c_1v^d+c_2(1-v)^d+u_N(av+b(1-v))^d]$. Show $\lim u_N=\max_v\frac{c_1v^d+c_2(1-v)^d}{1-(av+b(1-v))^d}$.
- Ex. 17–18: drop the requirement to use all resources at each stage. Show the equation has the form $f(x)=\max_{y_1+y_2\le x}[g(y_1)+h(y_2)+f(ay_1+by_2+x-y_1-y_2)]$. Ask when a solution or optimal policy exists (concave or convex $g,h$). Show that an interior solution gives $g'(y_1)/(1-a)=h'(y_2)/(1-b)$ under suitable assumptions, and ask for its interpretation.
- Ex. 19: add resources at each stage and obtain the recurrences.
- Ex. 20: define $g_N(z)$ as the minimum cost to obtain total return $z$ in $N$ stages. Show $g_1(z)=\min[(1-a)y_1+(1-b)y_2]$ over $g(y_1)+h(y_2)=z$, and the corresponding recurrence for $g_{N+1}$.

**Loading, cattle, investment, dating (Ex. 21–29, pp. 45–47).**
- Ex. 21 (ship loading): maximise $\sum n_iv_i$ subject to $\sum n_iw_i\le w$, $n_i=0,1,2,\dots,N$ as printed. Show $f_1(w)=v_1[w/w_1]$ and $f_{N+1}(w)=\max_x[xv_{N+1}+f_N(w-xw_{N+1})]$ over integer $x\le[w/w_{N+1}]$.
- Ex. 22: a herd, with $y$ sold for $\varphi(y)$ and $z$ retained yielding $az$ ($a>1$) next year. Show $f_1(x)=\max\varphi(y)$ and $f_N(x)=\max_{0\le y\le x}[\varphi(y)+f_{N-1}(a(x-y))]$.
- Ex. 23–25: optimal-policy structure for $\varphi=ky$, quadratic, strictly convex, strictly concave; a 2-year age restriction with feeding cost and mortality; random price and demand.
- Ex. 26: for $\varphi(x)=cx^d$ show $f_N=c_Nx^d$ with $c_{N+1}=\max_{0\le r\le1}[r^d+c_Na^d(1-r)^d]$. Find the asymptotics of $c_{N+1}/c_N$ and $r_{N+1}/r_N$.
- Ex. 27–28: capital split among goods, bonds (return $ay$, $a>1$) and stocks (return $bz$, $b>1$) with utility $\psi(w)$; stocks stochastic in Ex. 28.
- Ex. 29: a dating problem with three friends whose willingness changes with probabilities, one-week memory, maximising expected dances attended.

**Chain constraints and approximation (Ex. 30–38, pp. 47–48).**
- Ex. 30: minimise $L=\sum x_i$ with $x_i\ge0$, $x_i+x_{i+1}\ge a_i$. Show $\min L=\max_i a_i$, granted one $a_i$ is positive.
- Ex. 31–33: the same with three consecutive terms; general coefficients $c_i$, $b_ix_i+d_ix_{i+1}\ge a_i$; and boundary variants.
- Ex. 34: approximate $f(x)$ on $[a,b]$ by $ux+v$ under a squared-integral deviation and under max deviation.
- Ex. 35–37 (35 credited to Greenspan): cover distance $x$ at fixed speed $v$ with a stop probability $p(v)\,ds$ and delay $d$. Minimise expected time; minimise the probability of taking more than $T$; minimise expected cost with a stop penalty and a time cost.
- Ex. 38: a recurrence for minimising $Q_N=\sum(x_k-x_{k-1})^2$ with $\sum x_k^2=1$, $x_0=c$.

**Probabilistic sequential problems (Ex. 39–41, pp. 48–49).**
- Ex. 39: a particle is in state $S$ or $T$ with initial probability $x$ of $T$. Operation $A$ turns $x$ into $ax$ ($0<a<1$); operation $L$ observes the state. Show $f(x)=\min\{L:1+xf(1);\ A:1+f(ax)\}$, $f(0)=0$.
- Ex. 40: show there is $x_0\in(0,1)$ such that $L$ is used for $x\le x_0$ and $A$ for $x>x_0$. Show $f(1)=\min_k\frac{k+1}{1-a^k}$ and $x_0=\frac{1}{(1-a)f(1)}=\frac{1-a^k}{(1-a)(k+1)}$ for the minimising $k$.
- Ex. 41: two actions, with probabilities $p_1,p_2$ of gaining 1 or 2 units and $p_3$ of stopping (primed for the second action). Maximise the probability of reaching $n$ units. Show $p(n)=\max[p_1p(n-1)+p_2p(n-2),\ p_1'p(n-1)+p_2'p(n-2)]$, $p(0)=1$, $p(1)=\max(p_1,p_1')$.

**Quadratic cases (Ex. 42–44, p. 49).** With reference to §7, Ex. 42 asks the reader to show that if $g,h$ are quadratic then $f_N(c)=\alpha_N+\beta_Nc+\gamma_Nc^2$ with coefficients independent of $c$. Show the coefficients obey rational recurrences $\alpha_{N+1}=R_1(\alpha_N,\beta_N,\gamma_N)$ and so on. Treat a smoothing sum with first and second differences similarly.

**Machines and search (Ex. 45–49, pp. 50–51).**
- Ex. 45–48: a machine with output $r(t)$, upkeep $u(t)$, trade-in $s(t)$ at age $t$; new price $p>s(0)$; keep or replace at each integer time; discount $\alpha$, $0<\alpha<1$; unbounded process. Show $f(t)$ satisfies a two-branch maximum (keep versus replace). Then solve it using the retain-then-replace structure, ask whether an over-age machine should always be replaced, and ask how to include technological improvement. (Equation garbled in text layer; not reproduced.)
- Ex. 49 (Mosteller): a secretary searches 6 places for a letter. Each place has an initial probability, a probability of finding the letter on one look if it is there, and a time per look. Minimise expected search time, or maximise the probability of finding it in a given time. (Table values were not reliably readable in the text layer.)

**Existence, success probability (Ex. 50–55, pp. 51–52).**
- Ex. 50: if $a(x)\le d<1$, show a solution of $u=\max_x[b(x)+a(x)u]$, if it exists, is unique and equals $\max_x b(x)/(1-a(x))$. When does it exist? Without that bound, the number of solutions is 0, 1, 2 or a continuum; give examples.
- Ex. 51–53: a quantity $x$ used on repeated attempts; amount $y$ gives success probability $a(y)$. Show $f(x)=\sup_{0\le y\le x}[a(y)+(1-a(y))f(x-y)]$. Derive the equation for $1-f(x)$. Treat convex and concave $a$; the author says one case has no optimal policy.
- Ex. 54–55: add a terminal return $k(x_N)$; find asymptotic behaviour of $f(x)$ for $g,h$ asymptotically power-like.

**Cyclic and coupled structures (Ex. 56–59, pp. 52–53).** Recurrences for a cyclic sum of ratios, and for cyclic sums $\sum g_k(r_k,r_{k+1})+\sum h_k(r_k)$ with $r_{N+1}=r_1$. The approach is an auxiliary problem $F(u,v,c)$ with the end values fixed. Ex. 57 shows the original minimum is $\min_{0\le r_1\le b_1}F(r_1,r_1,c-\varphi_1(r_1))$. Ex. 58 gives $F_R(u,v,c)=\min_{r_R}[g(u,r_R)+h_R(r_R)+F_{R+1}(r_R,v,c-\varphi_R(r_R))]$ under the stated range conditions. Ex. 59 asks for similar treatment of triple-term cyclic sums.

**Production, spare parts (Ex. 60–65, pp. 53–55).**
- Ex. 60: $N$ products with costs $a_i,b_i,c_i$ per unit and fixed cost $C_i$ if $x_i>0$; unit price $p_i$; maximise profit $\sum p_ix_i$ subject to total cost $\le x$. Show $f_1(x)=p_1(x-C_1)/(a_1+b_1+c_1)$ for $x\ge C_1$ and $0$ for $0\le x\le C_1$. Show $f_N(x)=\max[p_Nx_N+f_{N-1}(x-g_N(x_N))]$ and that $x_N\ge0$ can be replaced by $x_N\ge\frac{f_{N-1}(x)-f_{N-1}(x-C_N)}{p_N}$.
- Ex. 61–63: stochastic demand; maximising the probability that return exceeds $r$; limited machines and labour.
- Ex. 64: recurrences with complementarity constraints such as $x_ix_{i+1}=0$.
- Ex. 65: stocking spare parts under weight and size limits, under several criteria (expected time lost, expected cost, a function of both, probabilities of exceeding $T$ or $C$).

**Asymptotics, counting, multiple capitals (Ex. 66–70, pp. 55–57).**
- Ex. 66: asymptotic modes of $u_{n+1}=\max[au_n+b,\,cu_n+d]$, and of $\max_i[a_iu_n+b_i]$ (cf. Ex. 50).
- Ex. 67: minimise $\sum g_i(x_i)+\max(x_1,\dots,x_N)$ with $x_i\ge0$.
- Ex. 68: invest in at most $k$ of $N$ activities. Show $f_{k,N}(x)=\max\{\max_{0\le y\le x}[g_N(y)+f_{k-1,N-1}(x-y)],\ f_{k,N-1}(x)\}$ for $1\le k\le N-1$.
- Ex. 69: two corporations may not invest in the same enterprise. Show $f_N(x,y)=\max\{\max_{0\le y_N\le y}[g_N(y_N)+f_{N-1}(x,y-y_N)],\ \max_{0\le x_N\le x}[g_N(x_N)+f_{N-1}(x-x_N,y)]\}$; then the case of different returns per corporation.
- Ex. 70 (Savage): replace all bulbs at once, cost $a$ per replacement, lighting-loss cost $g(x)$ over an interval $x$. Choose replacement times over $[0,T]$ to minimise average loss $\sum(a+g(x_i))/T$.

**Multipliers and further forms (Ex. 71–78, pp. 57–59).**
- Ex. 71: if the maximum of $\sum g_i(x_i)$ with $\sum x_i=c$ can be found by a Lagrange multiplier $\lambda$, show $\lambda=f_N'(c)$. Obtain the analogue for two constraints.
- Ex. 72: recurrences for the $r$-th largest and $r$-th smallest of $x_1,\dots,x_N$.
- Ex. 73 (Whittaker): maximise $\sum2^{-x_i}$ subject to $x_i\ge0$, $\sum1/(1+x_i)\le x$.
- Ex. 74–75: show that a gambler's problem (probability $p_k$ of predicting outcome $k$) may be converted into maximising $\sum p_kx_k$ subject to $\sum_ix_i\le x+x_j$ for all $j$. Ex. 75 asks to show $f_N(u,v)=\max[p_Nx_N+f_{N-1}(u-x_N,\min(v-x_N,u))]$.
- Ex. 76–77: heavy-water distillation cascade, minimising $V=g(a_1)+g(a_2)/a_1+\dots$ with $a_i\ge1$, $a_1\cdots a_m=x$. Show $f_{k+1}(x)=\min_{a_1\ge1}[g(a_1)+\frac1{a_1}f_k(x/a_1)]$; solve for $g(y)=y^b$, $b>0$. Ex. 77 uses a different $g_i$ for each stage.
- Ex. 78: show that $f_N(c)$ obtained from the usual recurrences does not depend on how the activities are numbered.

*Intuition note.* Many exercises can be approached by one routine (this is the writer's summary, not a statement in the text): define $f_N$ of the remaining resource, split off the first (or last) decision, and write $f_N=\max[\text{immediate payoff}+f_{N-1}(\text{what is left})]$.

### Bibliography and Comments (pp. 59–60)
- §1: a bibliography up to 1954 is in Bellman, "The Theory of Dynamic Programming," Bull. AMS 60 (1954) (p. 59).
- §2: the process was first discussed in Econometrica 22 (1954) (p. 59).
- §7: further discussion in "A Class of Variational Problems"; a "smoothing" discussion in Schoenberg (p. 59).
- §11: approximation in policy space was stressed in the 1953 computational-problems symposium (p. 59).
- §12: the proof of Lemma 1 was found independently by Ghicksberg and Fleming (p. 59).
- §17: results derived by D. Anderson (p. 59).
- §18: stability of solutions of functional equations, see Stability Theory of Differential Equations (1954) (p. 59).
- §19: reducing $\{f_{k,N}\}$ to $\{f_1\}$ is called "mathematical legerdemain" for computation; storage limits make one stingy with subscripts and parameters (p. 59).
- §22: the proof follows S. Johnson, "Optimal Search is Fibonaccian." J. Kiefer found an equivalent result earlier by a harder argument. The corresponding higher-dimensional problem is said to seem extraordinarily difficult, with nothing known at present (p. 60).
- §24: Feller (probability) and Bartlett (stochastic processes) are cited. Exercise 76 refers to Bellman, Nuclear Engineering, 1957 (p. 60).

## Toy example (ours, not from the text)
Two outcomes, $p_1=p_2=\tfrac12$, no further parameters beyond the chosen functions. If $y$ of $x$ is allocated:
- Outcome 1: $g_1(y)=2y$, $h_1=0$, remaining $a_1y+b_1(x-y)=y$ (so $a_1=1$, $b_1=0$).
- Outcome 2: $g_2=0$, $h_2(z)=z$, remaining $x-y$ (so $a_2=0$, $b_2=1$).

One stage: $f_1(x)=\max_y[\tfrac12\cdot2y+\tfrac12(x-y)]=\max_y[\tfrac x2+\tfrac y2]=x$, at $y=x$.

Two stages, by the recurrence of p. 40:
$f_2(x)=\max_y\{\tfrac12[2y+f_1(y)]+\tfrac12[(x-y)+f_1(x-y)]\}=\max_y\{\tfrac32y+(x-y)\}=\max_y\{x+\tfrac y2\}=\tfrac32x$.

Check at $x=1$, $y=1$ by enumeration. Outcome 1 (prob ½): return 2, 1 left, $f_1(1)=1$, total 3. Outcome 2 (prob ½): return 0, 0 left, total 0. Expected value $=\tfrac12\cdot3+\tfrac12\cdot0=1.5=f_2(1)$ ✓. For $y=0.5$: outcome 1 gives $1+0.5=1.5$; outcome 2 gives $0.5+0.5=1.0$; mean $1.25=1+0.25$ ✓, which is less than 1.5.

In the Stieltjes form of §26, $dG$ puts mass $\tfrac12$ at $(u,v)=(2y,y)$ and $\tfrac12$ at $(x-y,x-y)$. Then $\int[u+f_1(v)]\,dG=\tfrac12[2y+f_1(y)]+\tfrac12[(x-y)+f_1(x-y)]$, the same bracket.

## Concepts
- [[expected-value-criterion]] (new) — judging a policy by its expected total return, so randomness drops out of the analysis (p. 40)
- [[functional-equation]] (new) — equation for $f_N(x)$ in terms of $f_{N-1}$ (or $f$ itself) that solves a multi-stage problem (p. 40)
- [[stieltjes-form-of-recurrence]] (new) — recurrence written with a distribution $dG(u,v;x,y)$ over return and remaining quantity (p. 40)
- [[bellman-equation-value-function]] — $f_N(x)$ is the best achievable return with $N$ stages and quantity $x$ (p. 40; the definition of $f_N$ is given earlier in the chapter, not on these pages)
- [[principle-of-optimality]] — used implicitly in each recurrence (first decision plus optimal remainder); not stated in this unit (canon link; not stated in this unit)
- [[markov-decision-process]] — the stochastic allocation process, with state $x$, allocation $y$ and random next state (canon link; the term is not used in this unit)
- [[policy]] — the allocation rule $y_N(x)$ studied in exercises such as Ex. 7 and 45–47 (p. 42)

## Canonical instances
- [[stochastic-allocation-two-outcome]] — the two-branch expected-value recurrence (p. 40)
- [[ship-loading-knapsack]] — integer loading recurrence (Ex. 21, p. 46)
- [[cattle-breeding]] — sell versus retain a herd (Ex. 22, p. 46)
- [[machine-replacement]] — keep or replace with discounting (Ex. 45, p. 50)
- [[sequential-search]] — secretary search and Fibonaccian optimal search (Ex. 49, p. 50; p. 60)
- [[arithmetic-geometric-mean-via-dp]] — Ex. 1–2 (pp. 40–41)

## Bridges (candidates)
- [structural-analogy] $f_{N+1}(x)=\max_y\int[u+f_N(v)]dG$ ↔ reinforcement learning: finite-horizon value iteration with transition kernel $dG$ — same expected-reward-plus-next-value structure.
- [structural-analogy] Ex. 71, $\lambda=f_N'(c)$ ↔ optimization: a Lagrange multiplier as the marginal value (shadow price) of the resource.
- [metaphor] Ex. 78 (order of activities does not matter) ↔ computer science: reordering subproblems in dynamic programming without changing the optimum.

## Questions this raises
- When does the expected-value criterion fail to reflect what a decision-maker wants (compare Ex. 36 and 62, which use probabilities of exceeding thresholds)?
- How are existence and uniqueness proved for the Stieltjes-form equation (the text only says that equations of this type are discussed again in Chapter III, p. 40)?
- Why does $\lambda=f_N'(c)$ hold, and for which $g_i$ does the multiplier method apply (Ex. 71)?
- When no optimal policy exists (Ex. 53), what does the supremum in Ex. 51 mean for decisions?

## Exercises worth doing
- Ex. 1–2 (pp. 40–41) — derive the product recurrence and prove the AM–GM inequality by induction — difficulty: easy
- Ex. 4 (p. 41) — reduce a power-sum recurrence to a scalar recurrence for $c_N$ — difficulty: medium
- Ex. 7 (p. 42) — structure of optimal allocation under strict concavity, with a threshold $c_N$ — difficulty: hard
- Ex. 39–40 (pp. 48–49) — a stochastic observe-versus-act decision with a threshold policy — difficulty: medium
- Ex. 50 (p. 51) — uniqueness and existence for $u=\max_x[b(x)+a(x)u]$ — difficulty: medium
- Ex. 71 (p. 57) — link between the recurrence and Lagrange multipliers, $\lambda=f_N'(c)$ — difficulty: hard

## Reading notes
- This part starts at the top of printed p. 40, inside what must be §25 (inferred, since §26 begins on the same page): the page begins with the end of the two-outcome recurrence. It ends at printed p. 60 with the end of the bibliography. Printed = pdf − 23.
- Source note: the split was at a section boundary; the earlier part of §25 is not in this unit.
- The running header on every page is "A MULTI-STAGE ALLOCATION PROCESS" (printed).
- The text layer is garbled in several places (Ex. 45 equation, Ex. 49 table, Ex. 33, Ex. 56, Ex. 76). I wrote the exercises I could not read exactly in words, and I did not reproduce the table values on p. 50. I read the other exercise formulas against the printed forms and report them as printed.
- Exercise numbering is continuous 1–78; credits are shown on these pages for Greenspan (35), Mosteller (49), Savage (70) and Whittaker (73).
