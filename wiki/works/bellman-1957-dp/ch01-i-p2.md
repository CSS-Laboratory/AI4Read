---
id: bellman-1957-dp/ch01-i-p2
work: bellman-1957-dp
unit: "Chapter I, part 2/3 (end of §13 to start of §25): concavity, closed forms, stability, generalizations, search, stochastic processes"
pages: 22-39
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 22
pipeline_version: 0.1
---
# A Multi-Stage Allocation Process (part 2): concavity, explicit solutions, stability, generalizations

## L0 — One line
Bellman's recursion for splitting a resource over $N$ stages can be solved or analysed in several cases: under strict concavity and further conditions the optimal policy has a threshold-plus-interior-split form, particular power and quadratic returns give closed forms, and the recursion is formulated for time-dependent, multi-resource and stochastic processes.

## L1 — The gist (≤ 120 words)
Each stage splits an amount $x$ into $y$ and $x-y$ for two activities, earning $g(y)+h(x-y)$ and keeping $ay+b(x-y)$. The part studies $f_{N+1}(x)=\max_y[g(y)+h(x-y)+f_N(ay+b(x-y))]$. Under strict concavity and further conditions, the best policy puts everything into the first activity up to a threshold $\bar x$ and splits for larger $x$. Returns with inflection points can give a discontinuous policy. Closed forms exist for particular power and quadratic returns, and a stability bound relates nearby returns to nearby solutions. The recursion is extended to time-dependent, multi-resource and stochastic processes. A function with a single relative maximum (unimodal) can be searched by Fibonacci search, and concavity may save memory.

**Prerequisites:** derivatives and concavity of one-variable functions; geometric series; induction; limits of sequences of functions; the one-resource process of §2 (restated on p. 39).

## L2 — Key ideas
- **Threshold structure.** If $g,h$ are strictly concave and increasing, with $b>a$ and further conditions, the optimal policy is $y=x$ for $x\le\bar x$, and an interior split $0<y(x)<x$ beyond it (p. 22). Successive approximations give $x_1>x_2>\dots>0$ with $x_n\to\bar x$, and $y_1>y_2>\dots$ (pp. 24–25).
- **Without concavity the solution can be complicated.** With inflection-point returns $e^{-c/x}$, $f$ looks smooth but the maximizing $y(x)$ is a discontinuous sawtooth (p. 25).
- **Closed forms.** For $f(x)=\max[cx^d+f(ax),\,ex^g+f(bx)]$ with $0<d<g$ (each stage chooses one of two operations), the solution uses the first operation below an explicit $\bar x$ and the second first above it (p. 26). For quadratic returns there are three explicit cases, the last two on a limited interval (p. 28).
- **Stability.** Under summability conditions, $|f-F|\le\sum_n D(c^nx)$, where $D$ bounds $|u-v|$ (p. 29). The author says explicit solutions matter as approximations and clues for harder problems, and that approximation is in general most useful in policy space rather than function space (p. 29).
- **Generalizations.** Stage-dependent returns give a double-subscript recursion; fixing $N$ and indexing by stage restores a single subscript, which the author calls essential for computation (p. 31). With several resources the state is a vector, and Theorem 10 shows the $f_N$ stay concave under its concavity and monotonicity hypotheses (pp. 32–33).
- **Dimension reduction.** The recursion turns an $Nk$-dimensional maximization into $N$ $k$-dimensional ones; a strictly concave function of $k$ variables has a unique relative maximum, which is the absolute maximum (p. 34).
- **Fibonacci search.** $F_n$ is the supremum of interval lengths on which the maximum of a strictly unimodal function can always be located within a unit subinterval with at most $n$ evaluations; it equals the $n$th Fibonacci number (Theorem 11, pp. 34–36).
- **Memory saving.** If $g,h$ are strictly concave, the maximizer $y_N(x)$ is continuous, so computing $f_{N+1}(x)$ needs only values of $f_N$ in a small neighbourhood of a point, not the whole range (pp. 37–38).
- **Stochastic processes.** Due to the linearity of the expected value, future decisions can be based solely on the present state (p. 39).

## L3 — Walkthrough

### §13 (end): Theorem 5
Each $f_N$ is shown strictly concave by induction. The limit function is therefore concave, and strictly so because of the strict concavity of $g,h$, using Lemma 1 (proved earlier in §13, not in this unit) on the functional equation (p. 22). Strict concavity of $f$ makes the maximizing $y$, hence the optimal policy, unique (p. 22).

### §14 Properties of the solution — III: Concavity
The recursion (p. 24): $f_{n+1}(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f_n(ay+b(x-y))]$.

**Theorem 6.** Assume (p. 22):
(1a) $g,h$ strictly concave for $x\ge0$, monotone increasing, with continuous derivatives, $g(0)=h(0)=0$.
(1b) $\dfrac{g'(0)}{1-a}>\dfrac{h'(0)}{1-b}$, $h'(0)>g'(\infty)$, $b>a$.

Then the optimal policy is (p. 22):
(2a) $y=x$ for $0\le x\le\bar x$, where $\bar x$ is the root of $h'(0)=g'(x)+(b-a)g'(ax)+(b-a)a\,g'(a^2x)+\dots$ (as printed; see Reading notes).
(2b) $y=y(x)$ for $x\ge\bar x$, with $0<y(x)<x$, solving
$$g'(y)-h'(x-y)+(a-b)f'(ay+b(x-y))=0.\tag{3}$$

*Remark (author).* Only one of the possible combinations of inequalities connecting $g'(0)$, $h'(0)$, $b$ and $a$ is treated. The author says it will be easily seen from the procedure below that corresponding results hold for the other cases. Interchanging $y$ and $x-y$ interchanges $a$ and $b$, which halves the number of cases (p. 22).

**Proof by successive approximations.**

*First approximation.*
$$f_1(x)=\max_{0\le y\le x}[g(y)+h(x-y)].\tag{4}$$
Using $g'(0)>h'(0)$ (as the author writes it; see Reading notes), for small $x$ we have $g'(y)-h'(x-y)>0$ on $[0,x]$. So the objective increases in $y$ and the maximum is at $y=x$ (p. 22). As $x$ grows, $g'(y)-h'(x-y)=0$ first has a root at $y=x$, then inside $[0,x]$. The critical value $x_1$ is the unique solution of $g'(x)-h'(0)=0$ (p. 23). For $x\ge x_1$, $y_1(x)$ is the unique solution of $g'(y)=h'(x-y)$. Uniqueness follows from concavity, existence from continuity of $g',h'$ (p. 23).
$$f_1(x)=g(x)\ (0\le x\le x_1);\qquad f_1(x)=g(y_1)+h(x-y_1)\ (x\ge x_1).\tag{5}$$
$$f_1'(x)=g'(x)\ (0\le x<x_1);\quad f_1'(x)=[g'(y_1)-h'(x-y_1)]\tfrac{dy_1}{dx}+h'(x-y_1)=h'(x-y_1)\ (x>x_1).\tag{6}$$
Since $y_1(x_1)=x_1$, $f_1'$ is continuous at $x_1$, hence everywhere. $f_1$ is concave (cf. §11) (p. 23).

*Second approximation.*
$$f_2(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f_1(ay+b(x-y))].\tag{7}$$
The critical function is $D(y)=g'(y)-h'(x-y)+f_1'(ay+b(x-y))(a-b)$ (p. 23). The author computes
$g'(0)-h'(0)+f_1'(0)(a-b)=g'(0)-h'(0)+g'(0)(a-b)>h'(0)\big[\tfrac{(1-a)(1+a-b)}{1-b}-1\big]>0$ (p. 23).
So $D>0$ on $[0,x]$ for small $x$, and the maximum is at $y=x$. The first $x$ with $D(x)=0$ is $x_2$, given by $g'(x)=h'(0)+(b-a)f_1'(ax)$. Comparing the pair
$$g'(x)=h'(0),\qquad g'(x)=h'(0)+(b-a)f_1'(ax),\tag{8}$$
gives $0<x_2<x_1$. Hence
$$g'(x)=h'(0)+(b-a)g'(ax).\tag{9}$$
(added step: at $x=x_2$ we have $ax_2<x_2<x_1$, so $f_1'(ax_2)=g'(ax_2)$ by (6).)
Then $y=x$ for $0\le x\le x_2$ and $y=y_2(x)$ for $x\ge x_2$, the unique solution of
$$g'(y)=h'(x-y)+(b-a)f_1'(ay+b(x-y)).\tag{10}$$
$$f_2'(x)=g'(x)\ (0\le x\le x_2);\quad f_2'(x)=h'(x-y_2)+b f_1'(ay_2+b(x-y_2))\ (x\ge x_2),\tag{11}$$
and $f_2'$ is continuous at $x_2$ (p. 24). Comparing (10) with the equation defining $y_1$ gives $y_2(x)<y_1(x)$ (p. 24).

*Induction step.* Induction needs $f_2'(x)\ge f_1'(x)$, argued on the three intervals $[0,x_2],[x_2,x_1],[x_1,\infty)$ (p. 24).
- For $x\ge x_2$, (10) and (11) give
$$f_2'(x)=\frac{bg'(y_2)-ah'(x-y_2)}{b-a}\tag{12}$$
(added step: substitute $f_1'(\cdot)=[g'(y_2)-h'(x-y_2)]/(b-a)$ from (10) into (11)).
- For $x\ge x_1$, from (6) and the equation for $y_1$:
$$f_1'(x)=\frac{bg'(y_1)-ah'(x-y_1)}{b-a}.\tag{13}$$
- The function $[bg'(y)-ah'(x-y)]/(b-a)$ is monotone decreasing in $y$ on $[0,x]$. Since $y_2<y_1$, $f_2'>f_1'$ on $[x_1,\infty)$. On $[0,x_2]$ they are equal (p. 24).
- On $[x_2,x_1]$: $f_1'=g'(x)$ and $f_2'$ is given by (12) with $y_2$ (eq. 14). Since $0\le y_2\le x$ and the expression decreases in $y$,
$$f_2'(x)\ge\frac{bg'(x)-ah'(0)}{b-a}>g'(x),\tag{15}$$
the last step because $g'(x)\ge h'(0)$ follows from $g'(y)\ge h'(x-y)$ on $0\le y\le x$ and $0\le x\le x_1$ (p. 24).

The author then states that the induction gives (p. 24):
$$x_1>x_2>\dots>x_n>\dots>0;\quad f_1'\le f_2'\le\dots\le f_n'\le\dots;\quad y_1(x)>y_2(x)>\dots\tag{16}$$
Since $f_n\to f$, $f_n'\to f'$, $y_n\to y$ and $x_n\to\bar x$, the solution has the stated form (p. 25).

*Intuition note.* Early on, the first activity pays more at the margin, so everything goes there. A larger remaining amount makes the second activity worth feeding, and looking more stages ahead moves the switch point down toward a limit $\bar x$.

### §15 An "ornery" example
$$f(x)=\max_{0\le y\le x}\big[e^{-10/y}+e^{-15/(x-y)}+f(.8y+.9(x-y))\big].\tag{1}$$
$e^{-c/x}$ is used as one of the simplest functions with a point of inflection (p. 25). Successive approximations give a well-behaved curve $f(x)$ (Fig. 1, $x\in[20,50]$, roughly a rising line). But the maximizing $y(x)$ (Fig. 2) is a sawtooth: decreasing runs separated by upward jumps, so it is discontinuous (p. 25). Author's conclusion: as soon as $g''$ and $h''$ are allowed to change sign, one seems to meet functional equations that defy precise analysis (p. 26).

### §16 A particular example — I
**Theorem 7.** The continuous solution of (each stage chooses one of the two terms)
$$f(x)=\max[cx^d+f(ax),\ ex^g+f(bx)],\quad f(0)=0,\tag{1}$$
with $0<a,b<1$; $c,d,e,g>0$; $0<d<g$, is
$$f(x)=\frac{cx^d}{1-a^d}\ (0\le x\le\bar x);\qquad f(x)=ex^g+f(bx)\ (x\ge\bar x),\tag{3}$$
$$\bar x=\left[\frac{c/(1-a^d)}{e/(1-b^d)}\right]^{1/(g-d)}.\tag{4}$$
Since $0<b<1$, $f$ can be found explicitly on $[\bar x,\bar x/b],\dots,[\bar x/b^n,\bar x/b^{n+1}],\dots$ (p. 26).

*Proof.* Let $A$ = choose $cx^d+f(ax)$ and $B$ = choose $ex^g+f(bx)$. An optimal choice sequence is written $S=A^{a_1}B^{b_1}A^{a_2}B^{b_2}\dots$ (exponent = repetitions) (p. 26).
- *Locating $\bar x$.* Assume the stated form. At $\bar x$ either choice is optimal and below it only $A$ is, so $\bar x$ solves $BA^\infty=A^\infty$ (pp. 26–27).
$$A^\infty:\ f=cx^d+c(ax)^d+c(a^2x)^d+\dots=cx^d/(1-a^d)\tag{7}$$
$$BA^\infty:\ f=ex^g+cb^dx^d/(1-a^d)\tag{8}$$
Equating them gives (4) (p. 27).
- *$A$ is used for small $x$.* It suffices to show $cx^d/(1-a^d)$ solves the equation for small $x$, then invoke uniqueness. The author notes (footnote 5) that this uniqueness theorem is not yet established, but the method of Theorem 1 works here. Need
$$\frac{cx^d}{1-a^d}=\max\Big[\frac{cx^d}{1-a^d},\ ex^g+\frac{cb^dx^d}{1-a^d}\Big]\tag{9}$$
for small $x$. This is clear if $g>d>0$ and $0<b<1$ (p. 27).
- *Beyond $\bar x$.* Let $z$ be the smallest $x$ where a $B$-choice is optimal; there $BA^\infty=A^\infty$, so $z=\bar x$. For $x>\bar x$, compare $AB$ and $BA$ as first two choices:
$$f_{AB}=cx^d+ea^gx^g+f(abx),\qquad f_{BA}=ex^g+cb^dx^d+f(abx).\tag{10}$$
They are equal at $p=[c(1-b^d)/e(1-a^g)]^{1/(g-d)}$ (11), and $p<\bar x$ since $g>d$. As $f_{AB}<f_{BA}$ for $x>p$, $AB$ plus optimal continuation is inferior to $BA$ plus optimal continuation for $x>\bar x$. So $A$ cannot be used for $x>\bar x$ unless followed by $A^\infty$, "which we know is also impossible" (pp. 27–28).

*Intuition note.* For small $x$, because $d<g$, the term $x^d$ is much larger than $x^g$, so the $A$ term wins for small amounts. Above the threshold $\bar x$, where $BA^\infty$ overtakes $A^\infty$, the faster-growing $x^g$ term of $B$ makes $B$ the first choice.

### §17 A particular example — II (quadratic returns)
**Theorem 8** (author "leaves as an exercise", p. 28). Let $c,d>0$, $0<b\le a<1$, and
$$f(x)=\max_{0\le y\le x}[cy-y^2+d(x-y)-(x-y)^2+f(ay+b(x-y))],\quad f(0)=0.\tag{1}$$
On $0\le x\le\min(c/2,d/2)$ (the largest interval where both return functions are increasing, footnote 6), the form depends on the sign of $\frac{c}{1-a}-\frac{d}{1-b}$ (p. 28):
- **Case I** ($=0$): $f(x)=\dfrac{(c-d)\alpha+d}{1-b+(b-a)\alpha}\,x-\dfrac{\alpha^2+(1-\alpha)^2}{1-[(a-b)\alpha+b]^2}\,x^2$, with
$\alpha=\Big\{1+\tfrac12\big(\tfrac{a^2-b^2}{1-ab}\big)+\sqrt{1+\tfrac14\big(\tfrac{a^2-b^2}{1-ab}\big)^2}\Big\}^{-1}$ (eqs. 2–3).
- **Case II** ($<0$): $f(x)=\dfrac{d}{1-b}x-\dfrac{1}{1-b^2}x^2$ for $0\le x\le\min(\lambda,c/2,d/2)$, $\lambda=\dfrac{(1+b)[d(1-a)-c(1-b)]}{2(1-ab)}$ (eqs. 4–5). If $\lambda<\min(c/2,d/2)$, using (1) as a recursion extends $f$ over the whole interval.
- **Case III** ($>0$): $f(x)=\dfrac{c}{1-a}x-\dfrac{1}{1-a^2}x^2$ for $0\le x\le\min(\mu,c/2,d/2)$, $\mu=\dfrac{(1+a)[c(1-b)-d(1-a)]}{2(1-ab)}$ (eqs. 6–7; the printed bracket in (7) is not closed).

### §18 Approximation and stability
The author says the true importance of explicit solutions of simple equations lies in their use as approximate solutions to more obdurate equations and as clues to optimal policies for more complicated processes (p. 29). Approximating $g(x)$ by $cx^d$ is equivalent to approximating $\log g(e^x)$ by the line $\log c+dx$. The approximating curve may be changed as $x$ changes. The author adds that in general approximation is most useful in policy space rather than function space (p. 29).

Compare $f(x)=\max_y[u(x,y)+f(ay+b(x-y))]$ and $F(x)=\max_y[v(x,y)+F(ay+b(x-y))]$, both with value 0 at 0. This is a stability theorem in the classical sense (p. 29).

**Theorem 9.** Let $f,F$ be the continuous solutions, $u,v$ continuous for $x,y\ge0$, $0<a,b<1$, and $\sum_{n\ge0}m(c^nz)<\infty$, where $m(z)=\max_{0\le x\le z}\max_{0\le y\le x}\{|u|,|v|\}$. Define
$$\max_{0\le x\le z}\max_{0\le y\le x}|u(x,y)-v(x,y)|=D(z).\tag{2}$$
If $\sum_n D(c^nz)<\infty$ with $c=\max(a,b)$, then
$$|f(x)-F(x)|\le\sum_{n=0}^\infty D(c^nx).\tag{3}$$
Existence and uniqueness of the continuous solutions follow by modifying the proof of Theorem 1 (footnote 7) (p. 29).

*Proof.* Define $f_1=\max_y u$, $f_{N+1}=\max_y[u+f_N(ay+b(x-y))]$, and likewise $F_N$ with $v$. $f_N\to f$ and $F_N\to F$ (p. 30). Then $|f_1-F_1|\le\max_y|u-v|\le D(x)$ (5), and as in §7
$$|f_{N+1}-F_{N+1}|\le\max_y|f_N(\cdot)-F_N(\cdot)|+\max_y|u-v|.\tag{6}$$
Induction gives $|f_{N+1}-F_{N+1}|\le\sum_{n=0}^ND(c^nx)$ (7); let $N\to\infty$ (p. 30). (Added step: induction uses $ay+b(x-y)\le cx$ and that $D$, defined as a maximum over $[0,z]$, is nondecreasing; the author does not spell this out.)

*Intuition note.* The bound adds the one-stage errors $D$ evaluated at the shrinking amounts $x,cx,c^2x,\dots$ visited along the way. So if these one-stage errors are small and their sum is finite, the total error is small. Each stage's error enters once.

### §19 Time-dependent processes
The author notes that the foregoing pages tacitly assumed time-independent processes: the total return depended only on the initial quantity $x$ and the duration $N$ (p. 30). Now at stage $k$, splitting $x$ into $y,x-y$ gives return $g_k(x,y)$ and leaves $a_k(x,y)$, with $g_k,a_k$ continuous and $0\le a_k(x,y)\le ax$, $a<1$ (pp. 30–31).
$f_{k,N}(x)$ = optimal total $N$-stage return starting with $x$ at stage $k$:
$$f_{k,1}(x)=\max_y g_k(x,y);\qquad f_{k,N}(x)=\max_y[g_k(x,y)+f_{k+1,N-1}(a_k(x,y))],\ N\ge2.\tag{2, 3}$$
Since $N$ is fixed from the start, define $f_k(x)$ = optimal return from stage $k$ to the end at stage $N$ (p. 31):
$$f_N(x)=\max_y g_N(x,y);\qquad f_k(x)=\max_y[g_k(x,y)+f_{k+1}(a_k(x,y))],\ k=1,\dots,N-1.\tag{5}$$
The author calls this simplification essential for computation: the effort of tabulating functions of two variables instead of one is enormous, and going from two to three variables may be the difference between a feasible and an unfeasible approach (p. 31). For $N=\infty$ one gets the system $f_k(x)=\max_y[g_k+f_{k+1}(a_k(x,y))]$ (eq. 6). The author says it is "not difficult" to obtain analogues of Theorem 1 for these systems (p. 31).

### §20 Multi-activity processes
There are $M$ resources $x_1,\dots,x_M$. At each stage a quantity $x_{ij}$ of resource $i$ is used to produce more of resource $j$ (p. 32):
$$x_i(k+1)=x_i(k)-\sum_{j=1}^Mx_{ij}(k)+g_i(x_{1i}(k),\dots,x_{Mi}(k)),\quad i=1,\dots,M,\tag{1}$$
with $x_{ij}(k)\ge0$ and $\sum_jx_{ij}(k)\le x_i(k)$ (2). The $g_i$ and $x_i(0)=c_i$ are known. The $x_{ij}(k)$ maximize $R_N=F(x_1(N),\dots,x_M(N))$ (3). Further constraints may arise (Chapter 6) (p. 32). With $f_N(c_1,\dots,c_M)=\max R_N$ (4):
$$f_N(c)=\max_{\{y_{ij}\}}f_{N-1}\Big(c_1-\sum_jy_{1j}+g_1(y_{11},\dots,y_{M1}),\dots\Big),\ N\ge2,\tag{5}$$
with $y_{ij}\ge0$, $\sum_jy_{ij}\le c_i$ (6), and $f_1(c)=F(c)$ (7) as printed. Existence and uniqueness for the unbounded versions are deferred to Chapter IV; bottleneck processes appear in Chapter VI (p. 33).

### §21 Multi-dimensional structure theorems
A scalar function $G(\mathbf x)$ of a vector is *convex* if
$$G(\lambda\mathbf x+(1-\lambda)\mathbf y)\le\lambda G(\mathbf x)+(1-\lambda)G(\mathbf y),\ 0\le\lambda\le1;\tag{1}$$
*concave* if the inequality is reversed. The multi-dimensional analogue of Lemma 1 holds with the same proof (p. 33). Notation: $\mathbf y^{(i)}$ has components $y_{ij}$; the domain $D(\mathbf x,\mathbf y)$ is given by $\mathbf x=\sum_i\mathbf y^{(i)}$, $\mathbf y^{(i)}\ge0$ (as printed) (p. 33).

**Theorem 10.** If $r(\mathbf x,\mathbf y)$ and $a(\mathbf x,\mathbf y)$ are continuous concave functions for $\mathbf x,\mathbf y\ge0$, monotone increasing in the components of $\mathbf x$, then
$$f_1(\mathbf x)=\max_{D}r(\mathbf x,\mathbf y),\qquad f_{N+1}(\mathbf x)=\max_{D}[r(\mathbf x,\mathbf y)+f_N(a(\mathbf x,\mathbf y))]$$
are all concave for $\mathbf x\ge0$ (p. 33). If $r$ is strictly concave, the optimal policy for each $N$ is unique (p. 34).

*Intuition note.* With $k$ decisions per stage, the functional equation splits an $Nk$-dimensional maximization into $N$ separate $k$-dimensional ones, though these still have thorny features (p. 34). A strictly concave function of $k$ variables has one relative maximum, which is the absolute maximum, so the author expects that a more efficient search than for a general function should be possible (p. 34).

### §22 Locating the unique maximum of a concave function
The author says optimal search procedures for the maximum of a concave function are an extremely important and difficult problem that "has not been solved to date". The one-dimensional case is solved for the more general unimodal functions (one relative maximum). "Optimal" depends on equipment, permitted operations and cost (footnote 8) (p. 34).

Let $y=f(x)$ be strictly unimodal on $[0,L_n]$. $L_n$ is the largest length for which the maximum can *always* be located within a unit-length subinterval using at most $n$ evaluations; $F_n=\sup L_n$ (1) (p. 34).

**Theorem 11.** $F_n$ is the $n$th Fibonacci number: $F_0=F_1=1$, $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$ (2) (p. 34).

*Proof.* $F_0$ is a convention, $F_1$ is fixed by the process (p. 34). Evaluate $y_1=f(x_1)$, $y_2=f(x_2)$ with $0<x_1<x_2<L_n$. If $y_1>y_2$ the maximum is in $(0,x_2)$; if $y_2>y_1$ in $(x_1,L_n)$; if equal, either interval may be taken, even though the maximum is known to lie in $(x_1,x_2)$. Each stage leaves a subinterval with one interior value already known. Since values at the ends of an interval furnish no information per se, the author restricts attention to interior points (p. 35).
- $n=2$: $L_2=2-\epsilon$, $x_1=1-\epsilon$, $x_2=1$, so $F_2=2=F_1+F_0$ (p. 35).
- $n>2$: assume the rule for $k=2,\dots,n-1$ and show $F_n\le F_{n-1}+F_{n-2}$ (3). If $y_1>y_2$, then $x_2<F_{n-1}$, since only $n-2$ further choices remain with $x_1$ already used. $x_1$ is bounded too, because the maximum could lie in $[0,x_1]$ with two $x$-values already used. If $y_2>y_1$, then $L_n-x_1<F_{n-1}$. So in all cases $L_n<F_{n-1}+F_{n-2}$ (p. 36).
- Choosing $L_n,x_1,x_2$ arbitrarily close to their upper bounds gives equality, and the choice is the optimal policy: each $x_i$ is either discarded or is the optimal first choice for the remaining subinterval (p. 36).

Terms: $1,1,2,3,5,8,13,21,34,55,\dots$ (4), $F_{20}>10{,}000$. So a strictly unimodal maximum can be located within $10^{-4}$ of the original length with at most 20 evaluations (p. 36). Explicit form:
$$F_n=\frac{r_2-1}{r_2-r_1}r_1^n+\frac{1-r_1}{r_2-r_1}r_2^n,\quad r_1=\tfrac{1+\sqrt5}2\simeq1.61,\ r_2=\tfrac{1-\sqrt5}2\simeq-.61.\tag{5, 6}$$
$F_{n+1}/F_n\to r_1$. For large $n$, a uniform approximate procedure is to put the first two points at distance $L/r_1$ from either end of an interval of length $L$; this suits machine computation (p. 36).

**Theorem 12** (discrete version). If the unimodal function is defined only at discrete points, let $K_n$ be the largest number of points whose maximum can always be identified in $n$ computations. Then $K_0=K_1=1$, $K_2=2$, $K_3=4$, and $K_n=1+F_n$ for $n\ge3$ (p. 36).

### §23 Continuity and memory
For $g(x)=\max_{0\le y\le x}f(x,y)$ with $f$ continuous, $g$ is continuous but the maximizing $y(x)$ need not be (cf. §15). If $f(x,y)$ is strictly concave in $y$ on $[0,x]$, the author says it is clear that the maximizing $y$ is continuous in $x$ (Fig. 5) (p. 37). Consider
$$f_{N+1}(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f_N(ay+b(x-y))].\tag{2}$$
With no information on the maximizer, all $f_N(z)$, $0\le z\le ax$, are needed. If $g,h$ are strictly concave and continuous, each $f_N$ is strictly concave, the objective is strictly concave in $y$, and $y_N(x)$ is unique and continuous (p. 37). On a grid $0,\Delta,2\Delta,\dots$, computing $f_{N+1}(x)$ then needs only values of $f_N(z)$ in a relatively small neighbourhood of $z=y_N(x-\Delta)$ (as printed) (pp. 37–38). The idea extended to several dimensions can give a considerable saving of memory space, and the author says a great saving in running time will result (p. 38).

### §24 Stochastic allocation processes
*Deterministic* processes: the outcome is fixed by the decision. *Stochastic* processes: a decision determines a distribution of outcomes. The author limits the book to these two types (p. 38). With uncertainty, lack of complete control effectively prevents a guarantee of maximum return; the author nevertheless holds that there must exist some means of comparing policies. The difficulty is not finding a measure but finding a *unique* one: no one method can claim the title of "best", and the choice depends on analytic and arithmetic aspects of the process and on the philosophical and psychological attitudes of the decision-makers (pp. 38–39).

The general idea, "fairly unanimously accepted", is to use an average of outcomes (p. 39). The author notes a definite lack of unanimity concerning the use of averages for processes carried through once or at best a few times. In some cases "distribution-free" policies can be obtained; in general there seems to be no other approach than the usual one presented (p. 39). Two criteria:
- **Expected value.** Due to its linearity this average has an invariant property that greatly simplifies the functional equations; it enables future decisions to be based solely on the present state, independently of the past history (p. 39).
- **Probability of reaching at least a given return.** Far less frequently used; it also has the proper invariant structure and is deferred to a later chapter (p. 39).

### §25 Functional equations (begins)
Stochastic version of §2 (p. 39): with probability $p_1$ the split gives return $g_1(y)+h_1(x-y)$ and leaves $a_1y+b_1(x-y)$; with probability $p_2=1-p_1$, return $g_2(y)+h_2(x-y)$ and leaves $a_2y+b_2(x-y)$. $f_N(x)$ = expected total return of an $N$-stage process under an optimal policy (1). Then
$$f_1(x)=\max_{0\le y\le x}[p_1(g_1(y)+h_1(x-y))+p_2(g_2(y)+h_2(x-y))],\tag{2}$$
and the unit ends here, at eq. (2) (p. 39).

## Toy example (ours, not from the text)
Take $g(y)=y-y^2$, $h(z)=z-z^2$ (so $c=d=1$ in §17's form), $a=0.5$, $b=0.25$, $x=0.4\le\min(c/2,d/2)=0.5$.

*One stage.* $f_1(x)=\max_y[y-y^2+(x-y)-(x-y)^2]=x+\max_y[-y^2-(x-y)^2]$. The maximum is at $y=x/2$, giving $f_1(x)=x-x^2/2$. At $x=0.4$: $0.4-0.08=0.32$ (check: $y=0.2$ gives $0.16+0.16$).

*Two stages.* The left-over quantity is $z=0.5y+0.25(0.4-y)=0.1+0.25y$. Then
$J(y)=0.4-y^2-(0.4-y)^2+f_1(z)$.
- $-y^2-(0.4-y)^2=-2y^2+0.8y-0.16$.
- $f_1(z)=z-z^2/2=(0.1+0.25y)-\tfrac12(0.01+0.05y+0.0625y^2)=0.095+0.225y-0.03125y^2$.
- Sum: $J(y)=0.4-0.16+0.095+(0.8+0.225)y-(2+0.03125)y^2=0.335+1.025y-2.03125y^2$.

The maximum is at $y^*=1.025/4.0625\approx0.2523$, with $f_2(0.4)=0.335+1.025^2/(4\times2.03125)=0.335+1.050625/8.125\approx0.4643$. Using the one-stage-best split $y=0.2$ instead gives $J(0.2)=0.335+0.205-0.08125=0.45875<0.4643$. The recursion's optimal split differs from the myopic one because it values what is left over.

## Concepts
- [[principle-of-optimality]] — the same recursion form $f_{N+1}=\max_y[\text{return}+f_N(\text{remaining})]$ is reused in the variants, introduced with "as before" or "arguing as in the preceding pages"; the principle itself is not named in these pages (pp. 24, 31, 32, 39)
- [[bellman-equation-value-function]] — $f_{k,N}(x)$ (or $f_N(x)$ in the one-resource process) is the optimal $N$-stage return from quantity $x$ (pp. 31, 39)
- [[policy]] — a rule giving the split $y(x)$ at each state (pp. 22, 25)
- [[concavity-of-value-function]] (new) — strict concavity of $g,h$ passes to every $f_N$, giving a unique optimal split; Theorem 10 gives concavity in the vector case (pp. 22, 33, 34, 37)
- [[switch-point-policy]] (new) — $y=x$ below a threshold $\bar x$, an interior split above (p. 22); in Theorem 7 the analogue is operation $A$ below $\bar x$ and $B$ first above it (p. 26)
- [[stability-of-solution-to-data]] (new) — a bound on $|f-F|$ in terms of $|u-v|$, called by the author a stability theorem "in the classical sense" (p. 29)
- [[approximation-in-policy-space]] (new) — fit simple returns and use the resulting policy as a guide (p. 29)
- [[time-dependent-process]] (new) — stage-dependent $g_k,a_k$; single-subscript recursion (pp. 30–31)
- [[multi-activity-process]] (new) — several resources, vector state, $M^2$ allocation variables $x_{ij}$ per stage (p. 32)
- [[unimodal-function]] (new) — a function with a single relative maximum (p. 34)
- [[fibonacci-search]] (new) — evaluation scheme giving $F_n$ as the supremum of intervals resolvable in $n$ evaluations (pp. 34–36)
- [[stochastic-allocation-process]] (new) — a decision fixes a probability distribution of outcomes; value = expected return (pp. 38–39)
- [[markov-decision-process]] — only anticipated: expected-value criterion lets future decisions be based solely on the present state (p. 39)

## Canonical instances
- [[ornery-example]] — inflection-point returns give a smooth $f$ but a discontinuous sawtooth $y(x)$ (p. 25)
- [[power-return-two-activity-example]] — $cx^d$ vs $ex^g$, threshold $\bar x$ in closed form (p. 26)
- [[quadratic-return-example]] — three explicit cases by the sign of $c/(1-a)-d/(1-b)$ (p. 28)
- [[fibonacci-search-example]] — 20 evaluations locate a unimodal maximum to within $10^{-4}$ of the interval (p. 36)

## Bridges (candidates)
- [structural-analogy] Fibonacci search for a unimodal maximum ↔ numerical optimization: golden-section line search — $F_{n+1}/F_n\to1.61$ gives the fixed-ratio rule (p. 36); the text does not name golden-section search.
- [structural-analogy] Stability bound $\sum_nD(c^nx)$ ↔ control-theory: robustness of optimal value to model error — bounds how much a perturbed return changes the solution.
- [structural-analogy] Quadratic closed forms of §17 ↔ LQR: value function quadratic in the state — here only on a restricted interval with constraint $0\le y\le x$.
- [structural-analogy] Expected-value recursion of §25 ↔ MDP: finite-horizon Bellman equation with two random outcomes.
- [structural-analogy] Vector-state multi-activity recursion ↔ state-space models: resources as state vector, allocations as inputs.

## Questions this raises
- How does the sawtooth policy of §15 arise from the recursion, and can concavity be weakened and still keep $y(x)$ continuous?
- What do the corresponding results look like for the other inequality cases that the author says follow from the procedure (p. 22)?
- How should one choose an average when the process runs only once, given the author's remark that no single method can claim to be "best" (pp. 38–39)?
- What is an "optimal search procedure" for concave functions beyond the one-dimensional unimodal case, which the author says is not solved (p. 34)?

## Exercises worth doing
- Theorem 8 (p. 28) — verify the quadratic closed forms (Cases I–III), including the thresholds $\lambda,\mu$ — difficulty: hard (stated by the author as an exercise; no solution printed).

## Reading notes
- This is part 2 of 3 of Chapter I. It starts in the closing sentences of §13 (proof of Theorem 5, p. 22) and ends mid-§25 at eq. (2) of "Functional equations" (p. 39). Printed page = pdf − 23.
- Text layer is heavily garbled on equations and subscripts. Everything above was checked against the images, except where noted below.
- Theorem 6 (2a) as printed (series with $+(b-a)g'(ax)+(b-a)a\,g'(a^2x)+\dots$) does not obviously agree with the proof's eq. (9), $g'(x)=h'(0)+(b-a)g'(ax)$, in sign or form. Reported as printed.
- The proof of Theorem 6 (p. 22) uses $g'(0)>h'(0)$, whereas the stated assumption (1b) is $g'(0)/(1-a)>h'(0)/(1-b)$; the text does not reconcile them.
- (15) uses "$>g'(x)$" while the stated justification gives "$g'(x)\ge h'(0)$".
- In Theorem 9 the statement uses $c^nz$ in $m$ before $c=\max(a,b)$ is defined.
- §17 Theorem 8: the symbol $\alpha$ appears as "a" in the text layer; the image shows it distinct from $a$.
- §20 (7): $f_1=F$ is printed, although (4)–(5) suggest an index shift; not resolved.
- §21 (2a) is printed as $x=\sum y^{(i)}$ while §20 used inequalities. Two equations are numbered (2) in §21.
- Theorem 11 proof: the printed bounds for $x_1,x_2$ near the end ("respectively $F_{n-1}$, $F_{n-2}$") do not match "$x_2<F_{n-1}$" earlier; likely an index slip. I did not state the index for $x_1$.
- §23: the printed neighbourhood centre $y_N(x-\Delta)$ is an allocation value, not obviously an argument of $f_N$; reported as printed.
- Figures 1–2 (p. 25) are qualitative; no numeric values beyond axes were read.
