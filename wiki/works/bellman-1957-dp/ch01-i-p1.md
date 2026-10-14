---
id: bellman-1957-dp/ch01-i-p1
work: bellman-1957-dp
unit: "Chapter I, §§1–13 (first part): A Multi-Stage Allocation Process"
pages: 3–21
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# A Multi-Stage Allocation Process, part 1 (§§1–13, up to the proof of Theorem 5)

## L0 — One line
Embed an N-stage allocation problem in a family of problems indexed by the resource $x$ and the number of stages $N$, so that one N-dimensional maximisation becomes a chain of one-dimensional maximisations linked by a functional equation.

## L1 — The gist (≤ 120 words)
Bellman asks how to maximise the total return when a resource is split at each of N stages and each choice shrinks what is left. Calculus, or grid search over N variables, quickly becomes unmanageable: ten stages with ten grid points each need $10^{10}$ evaluations. His answer is to embed the problem in a family indexed by the initial amount $x$ and the number of stages $N$. The maximum return $f_N(x)$ then obeys a recurrence, which turns one N-dimensional problem into N one-dimensional ones. This part also treats the infinite-stage equation: existence and uniqueness of its solution, two ways to approximate it, and structure results (convexity, start of concavity).

**Prerequisites:** maximisation of functions of several variables; continuity and uniform convergence; convex and concave functions; derivatives and implicit differentiation; geometric series.

## L2 — Key ideas (5–10 bullets)
- A simple N-stage allocation problem is posed. Classical calculus needs interior and boundary tests in N dimensions, and lattice search costs $10^{10}$ evaluations for 10 stages (pp. 4–6).
- The aim is the structure of the optimal policy, not only numbers. A person running the process needs only the best choice $y$ given $x$ and the stages left $N$ (p. 7).
- Key observation: whatever the first choice, the remainder must be used optimally for the remaining stages. It gives $f_N(x)=\max_y[g(y)+h(x-y)+f_{N-1}(ay+b(x-y))]$ (p. 8).
- Imbedding: solve the particular problem by solving the general family. This reduces one N-dimensional problem to N one-dimensional ones, and the same device handles the separable allocation problem and the "smoothing" problem (pp. 9–11).
- For $N=\infty$ the sequence of equations becomes one equation. Theorem 1 gives a unique solution continuous at 0 with value 0, by successive approximations (pp. 11–16).
- Under Theorem 1's conditions, any continuous start with $f_0(0)=0$ converges (Theorem 2). Under the same conditions, starting from a continuous policy also converges, monotonically (Theorem 3, approximation in policy space; the proof pages show monotonicity and continuity of $f_0$ but do not spell out the convergence step) (pp. 16–19).
- Structure follows from structure. If $g,h$ are convex (in addition to Theorem 1's assumptions), $f$ is convex and $y\in\{0,x\}$ (Theorem 4). For strictly concave $g,h$, Theorem 5 claims $f$ is strictly concave with a unique policy; Lemma 1 proves concavity is preserved by maximisation (pp. 19–21).

## L3 — Walkthrough

### §1 Introduction (p. 3–4)
The chapter first formulates the problem classically to show its difficulties. It then introduces the main approach: imbed the problem in a family of similar problems (p. 3). This replaces a multi-dimensional maximisation by a system of recurrence relations in functions of much smaller dimension (p. 3). Later parts of the chapter cover time-dependent processes, multi-dimensional analogues, and stochastic versions (pp. 3–4).

### §2 A multi-stage allocation process (p. 4–5)
Split a quantity $x$ into $y$ and $x-y$, with returns $g(y)$ and $h(x-y)$. Maximise
$$R_1(x,y)=g(y)+h(x-y),\quad 0\le y\le x. \tag{1}$$
$g,h$ are assumed continuous for $x\ge 0$, so the maximum exists (p. 4).

Two stages: $y$ shrinks to $ay$ and $x-y$ to $b(x-y)$, with $0\le a<1$, $0\le b<1$. The remainder is $x_1$:
$$ay+b(x-y)=x_1=y_1+(x_1-y_1),\quad 0\le y_1\le x_1, \tag{2}$$
$$R_2(x,y,y_1)=g(y)+h(x-y)+g(y_1)+h(x_1-y_1), \tag{3}$$
maximised over $0\le y\le x$, $0\le y_1\le x_1$ (4).

N stages:
$$R_N=g(y)+h(x-y)+g(y_1)+h(x_1-y_1)+\dots+g(y_{N-1})+h(x_{N-1}-y_{N-1}), \tag{5}$$
with $x_1=ay+b(x-y)$, $x_2=ay_1+b(x_1-y_1)$, …, $x_{N-1}=ay_{N-2}+b(x_{N-2}-y_{N-2})$, and $0\le y_i\le x_i$ (6). Maximise $R_N$ over this N-dimensional region (p. 5). Footnote 1 (p. 4): the return may be in different units from $x$; this is the simplest case.

### §3 Discussion (p. 5–7)
**Calculus route.** If the absolute maximum is interior ($0<y_i<x_i$) and $g,h$ are differentiable, the stationarity equations are (p. 5):
$$g'(y_{N-1})-h'(x_{N-1}-y_{N-1})=0,$$
$$g'(y_{N-2})-h'(x_{N-2}-y_{N-2})+(a-b)\,h'(x_{N-1}-y_{N-1})=0,\ \dots \tag{1}$$
We want the absolute maximum, so boundary values and all mixtures of boundary and interior points must also be tested. Non-uniqueness of the solutions of (1) requires further conditions to exclude minima and local maxima (pp. 5–6).

**Brute force.** Take 10 stages and divide each of the 10 intervals into ten parts. This gives $10^{10}$ lattice points (p. 6). At one second per point this is 2.77 million hours; at one millisecond 2.77 thousand hours; at one microsecond 2.77 hours. A 20-stage process multiplies the cost by $10^{10}$ (p. 6). Sensitivity analysis over $x$, $a$, $b$, $g$, $h$ makes it worse. Realistic extensions (more parts, more resources) raise the computing time at an exponential rate (pp. 6–7).

**What we really want.** The purpose of such models is the structure of the solution, because "concepts are, in many processes, more important than constants" (p. 7). A person carrying out the process needs only $y$ as a function of $x$ and $N$, a one-dimensional choice at each stage. So a formulation that keeps one dimension should exist (p. 7). Footnote 2 calls this "the useful principle of wishful thinking."

### §4 Functional equation approach (p. 7–9)
Define $f_N(x)$ = maximum return from an N-stage process starting with $x$ (p. 7). Then
$$f_N(x)=\max_{\{y,y_i\}}R_N(x,y,\dots,y_{N-1}),\ N\ge2;\qquad f_1(x)=\max_{0\le y\le x}[g(y)+h(x-y)]. \tag{2, 3}$$

**Key observation.** Whatever $y$ is chosen first, the remaining amount $ay+b(x-y)$ must be used in the best way for the remaining stage. Bellman calls it "the key to all of our subsequent mathematical analysis" and says it has "the deceptive simplicity of a half-truth" (p. 8). So the return from first choice $y$ is
$$R_2(x,y,y_1)\to g(y)+h(x-y)+f_1(ay+b(x-y)), \tag{4}$$
and maximising over $y$:
$$f_2(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f_1(ay+b(x-y))], \tag{5}$$
$$f_N(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f_{N-1}(ay+b(x-y))],\ N\ge2. \tag{6}$$
Computation: start from $f_1$ and use (6) to get $f_2,f_3,\dots$. Each step also gives $y_k(x)$, the optimal first allocation of a $k$-stage process starting with $x$ (p. 8). The solution is the tabulation of $\{y_k(x)\}$ and $\{f_k(x)\}$ (p. 9). For a given $N$ and $x$, the optimal sequence is recovered forward (p. 9):
$$y=y_N(x),\ y_1=y_{N-1}(ay+b(x-y)),\ y_2=y_{N-2}(ay_1+b(x_1-y_1)),\ \dots,\ y_{N-1}=y_1(ay_{N-2}+b(x_{N-2}-y_{N-2})). \tag{7}$$

*Intuition note.* The value of the leftover resource depends only on how much is left and how many stages remain, not on how it was reached. So we can tabulate "best return from here" once, as a function of $x$, and reuse it.

### §5 Discussion (p. 9)
A problem with particular $x,N$ is solved by solving the general problem with arbitrary $x,N$. This is the **imbedding** of the problem in a family of similar problems (p. 9). One N-dimensional problem becomes a sequence of N one-dimensional problems. The author also expects analytic gains: explicit solutions for large classes of $g,h$, and structural features even where complete solution is impossible (p. 9).

### §6 A multi-dimensional maximisation problem (p. 10)
Maximise $F(x_1,\dots,x_N)=\sum_{i=1}^N g_i(x_i)$ subject to $x_1+\dots+x_N=c$, $x_i\ge0$, with each $g_i$ continuous (1, 2). Define $f_N(c)=\max_{\{x_i\}}F$ (3). Then
$$f_N(c)=\max_{0\le x\le c}[g_N(x)+f_{N-1}(c-x)],\ N\ge2;\qquad f_1(c)=g_1(c). \tag{4, 5}$$

### §7 A "smoothing" problem (p. 10–11)
Minimise
$$F(x_1,\dots,x_N)=\sum_{k=1}^N g_k(x_k-r_k)+\sum_{k=1}^N h_k(x_k-x_{k-1}),\quad x_0=c, \tag{1}$$
with $\{r_k\}$ given, $g_k,h_k$ continuous and $\to\infty$ as $|x|\to\infty$ (p. 10). Let $f_R(c)$ be the minimum over $x_R,\dots,x_N$ of $F_R=\sum_{k=R}^N g_k(x_k-r_k)+\sum_{k=R}^N h_k(x_k-x_{k-1})$ with $x_{R-1}=c$ (2). Then (p. 11)
$$f_N(c)=\min_x[g_N(x-r_N)+h_N(x-c)], \tag{3}$$
$$f_R(c)=\min_x[g_R(x-r_R)+h_R(x-c)+f_{R+1}(x)],\ R=1,\dots,N-1. \tag{4}$$
The origin of the name is deferred to the exercises (not in these pages).

### §8 Infinite stage approximation (p. 11)
For large $N$ consider the infinite-stage process as an approximation. The N equations (4.6) are replaced by one equation (p. 11):
$$f(x)=\max_{0\le y\le x}[g(y)+h(x-y)+f(ay+b(x-y))]. \tag{1}$$
Cost: a maximum may not exist, only a supremum, so no policy may actually attain $f(x)$. Also one must show there are no extraneous solutions, so existence and uniqueness theorems are needed (p. 11). Footnote 3: "physical" means the real world (economic, biological, engineering…).

### §9 Existence and uniqueness (p. 12–16)
**Theorem 1.** Assume (p. 12):
(a) $g,h$ continuous for $x\ge0$, $g(0)=h(0)=0$;
(b) with $m(x)=\max_{0\le y\le x}\max(|g(y)|,|h(y)|)$ and $c=\max(a,b)$, $\sum_{n=0}^\infty m(c^nx)<\infty$ for all $x\ge0$;
(c) $0\le a<1$, $0\le b<1$.
Then (8.1) has a unique solution that is continuous at $x=0$ with value 0 there. Moreover this solution is continuous.

**Special case $g,h\ge0$ (monotone proof, p. 12–13).** Then $\{f_N\}$ from (4.6) is monotone increasing. The text says boundedness follows from (1b), to be shown "in a moment". So $f_N\to f$. Write $T(f,y)=g(y)+h(x-y)+f(ay+b(x-y))$ (3), so $f_{N+1}(x)=\max_{0\le y\le x}T(f_N,y)$ (4). The argument for (2) is:
- Monotonicity gives $f(x)\ge\max_y T(f_N,y)$ (5), so $f(x)\ge T(f_N,y)$ for every $y\in[0,x]$ (6).
- Letting $N\to\infty$: $f(x)\ge T(f,y)$ (7), hence $f(x)\ge\sup_y T(f,y)$ (8). "Max" cannot be written, since continuity of the limit $f$ is not guaranteed.
- From (4): $f_{N+1}(x)\le\sup_yT(f,y)$ (9) (added step: $f_N\le f$ and $T$ is increasing in $f$). Hence $f(x)\le\sup_yT(f,y)$ (10).
- Comparing (8) and (10) gives $f(x)=\sup_{0\le y\le x}T(f,y)$ (2).

This proof does not give continuity of $f$, which implies the existence of an optimal policy $y(x)$ attaining the max in $f(x)=\max_yT(f,y)$ (11). The existence of an optimal policy is directly of no particular importance computationally or in applications. It matters for the structure of optimal policies of the infinite process, and indirectly for numerics, since the infinite solution approximates the finite one (p. 13).

**Proof by successive approximations (pp. 14–16).** $f_1$ is continuous, so by induction every $f_N$ is continuous. The maximising $y$ need not depend continuously on $x$ (example in §15, not in this part) (p. 14). Let $y_N(x)$ attain the max in (4):
$$f_{N+1}=T(f_N,y_N),\quad f_{N+2}=T(f_{N+1},y_{N+1}). \tag{12}$$
By maximality,
$$f_{N+1}=T(f_N,y_N)\ge T(f_N,y_{N+1}),\quad f_{N+2}=T(f_{N+1},y_{N+1})\ge T(f_{N+1},y_N). \tag{13}$$
So $f_{N+1}-f_{N+2}$ lies between two numbers (14):
$$T(f_N,y_{N+1})-T(f_{N+1},y_{N+1})\le f_{N+1}-f_{N+2}\le T(f_N,y_N)-T(f_{N+1},y_N).$$
Therefore
$$|f_{N+1}-f_{N+2}|\le\max\big[|T(f_N,y_{N+1})-T(f_{N+1},y_{N+1})|,\ |T(f_N,y_N)-T(f_{N+1},y_N)|\big]. \tag{15}$$
By definition of $T$,
$$|T(f_N,y_N)-T(f_{N+1},y_N)|=|f_N(ay_N+b(x-y_N))-f_{N+1}(ay_N+b(x-y_N))|. \tag{16}$$
Define $u_N(x)=\max_{0\le z\le x}|f_N(z)-f_{N+1}(z)|$ (17). Since $ay+b(x-y)\le cx$, we get
$$u_{N+1}(x)\le u_N(cx). \tag{18}$$
For $N=1$: $|f_1-f_2|\le\max[|f_1(ay_1+b(x-y_1))|,|f_1(ay_2+b(x-y_2))|]\le m(cx)$ (19), as printed. So $u_1(x)\le m(cx)$ and by (18) $u_N(x)\le m(c^{N+1}x)$. By (1b), $\sum u_N$ converges uniformly in any finite interval. So $f=\lim f_N$ exists, is continuous for all $x$, and, by uniform convergence, solves (8.1) (p. 15).

**Uniqueness (pp. 15–16).** Let $F$ be another solution, continuous at 0 with $F(0)=0$. Let $y(x)$, $w(x)$ attain the max for $f$ and $F$ in $f=\max_yT(f,y)$ (20) and $F=\max_yT(F,y)$ (21). Then
$$f=T(f,y)\ge T(f,w),\quad F=T(F,w)\ge T(F,y), \tag{22}$$
$$|f-F|\le\max[|T(f,y)-T(F,y)|,|T(f,w)-T(F,w)|]\le\max[|f(ay+b(x-y))-F(ay+b(x-y))|,\ |f(aw+b(x-w))-F(aw+b(x-w))|]. \tag{23}$$
Define $u(x)=\sup_{0\le z\le x}|f(z)-F(z)|$ (24). Then $u$ is continuous at 0 with $u(0)=0$. From (23), $u(x)\le u(cx)$ (25) and by iteration $u(x)\le u(c^Nx)$ (26). Letting $N\to\infty$ gives $u(x)\le0$, so $f=F$ (p. 16).

*Intuition note.* Each extra stage changes the answer only through a resource amount that has been shrunk by the factor $c<1$. The differences between successive $f_N$ therefore shrink fast enough to sum, and two solutions cannot stay apart.

### §10 Successive approximations (p. 16)
**Theorem 2.** Let $f_0$ be continuous for $x\ge0$ with $f_0(0)=0$. If the conditions of Theorem 1 hold, then $f_{N+1}(x)=\max_{0\le y\le x}T(f_N,y)$, $N=0,1,\dots$, converges to the solution $f$ above, uniformly in any finite interval. The same methods prove it.

### §11 Approximation in policy space (p. 16–19)
A **policy** is a sequence of admissible choices of $y$; one yielding $f(x)$ is **optimal**. Formally a policy is $y(x)$, and it is not single-valued if the optimal policy is not unique (p. 17). The "duality" is the link between $f$ and the policies. Knowing $f$ gives $y(x)$. Conversely any $y(x)$ determines $f$ iteratively through
$$f(x)=T(f,y(x)). \tag{2}$$
Example: if the optimal policy is $y=0$ always, then $f(x)=h(x)+f(bx)$ (3), so $f(x)=\sum_{n=0}^\infty h(b^nx)$ (4) (p. 17). (Uses $g(0)=0$.)

Approximating in policy space is claimed to be more natural, since the policy is the part where experience gives some knowledge, and it always gives monotone approximations (p. 17). Procedure: take an initial policy guess $y_0(x)$ with return function $f_0$ solving $f_0=T(f_0,y_0(x))$ (5). Improve by taking $y_1(x)$ maximising $T(f_0,y)$, and continue (p. 18). The author says it is easy to show the resulting $\{f_N\}$ is monotone increasing, but that a rigorous proof of existence and convergence of $\{y_N\},\{f_N\}$ "seems difficult". He therefore states a weaker theorem (p. 18).

**Theorem 3.** Let $f_0=T(f_0,y_0(x))$ (6), with $y_0$ continuous and $0\le y_0(x)\le x$ (7). Under the assumptions of Theorem 1, $f_{N+1}=\max_{0\le y\le x}T(f_N,y)$ (8) converges uniformly to $f$, and the convergence is monotone.

Proof, as given in these pages: $f_1=\max_yT(f_0,y)$ (9) $\ge T(f_0,y_0)=f_0$, so $f_1\ge f_0$, and inductively $f_{N+1}\ge f_N$ (the induction uses that $T$ is increasing in $f$; added step). Continuity: the series $f_0(x)=g(y_0)+h(x-y_0)+\dots$ (10) converges uniformly in finite intervals and is continuous if $y_0$ is continuous (p. 19). These pages do not spell out the convergence step itself.

*Intuition note.* Starting from any workable rule of thumb, improving it by one-step lookahead never makes the return worse. That gives a guaranteed monotone path, unlike a general function guess.

### §12 Properties of the solution I: Convexity (p. 19–20)
**Theorem 4.** If, in addition to Theorem 1's assumptions, $g,h$ are convex, then $f$ is convex and for each $x$, $y$ equals 0 or $x$.

Proof (inductive, p. 19). $g(y)+h(x-y)$ is convex in $y$, and a convex function attains its maximum at an end-point. So
$$f_1(x)=\max(g(x),h(x))$$
(2), a maximum of convex functions, hence convex. Likewise $g(y)+h(x-y)+f_1(ay+b(x-y))$ is convex in $y$, so
$$f_2(x)=\max(g(x)+f_1(ax),\ h(x)+f_1(bx)) \tag{3}$$
is convex (end-points use $g(0)=h(0)=0$; added step). So every $f_N$ and the limit $f$ are convex. Then the equation reduces to
$$f(x)=\max(g(x)+f(ax),\ h(x)+f(bx)), \tag{4}$$
so $y=0$ or $x$. Bellman remarks that this is "surprisingly, still a difficult equation to solve in general" (pp. 19–20).

### §13 Properties of the solution II: Concavity (p. 20–21, part)
**Theorem 5.** If $g,h$ are strictly concave (plus Theorem 1's assumptions), then $f$ is strictly concave and the optimal policy is unique (p. 20).

**Heuristic one-stage check (pp. 20–21).** For $f_1=\max[g(y)+h(x-y)]$ with an interior maximum and second derivatives: $g'(y)=h'(x-y)$ (3). Then $f_1'(x)=(g'(y)-h'(x-y))\,dy/dx+h'(x-y)=h'(x-y)$ (4), so $f_1''(x)=h''(x-y)(1-dy/dx)$ (5). Differentiating (3): $g''(y)\,dy/dx=h''(x-y)(1-dy/dx)$ (6), so
$$dy/dx=\frac{h''(x-y)}{g''(y)+h''(x-y)}. \tag{7}$$
With $g'',h''<0$ this gives $0<dy/dx<1$, hence $f_1''<0$ (p. 21). If the maximum is on the boundary one can force it inside, for instance by adding $\epsilon\log y(x-y)$, but this is "a rather clumsy method" that does not extend easily to many dimensions (p. 21).

**Lemma 1.** If $G(x,y)$ is jointly concave for $x,y\ge0$ (footnote 4: $G(\lambda x_1+(1-\lambda)x_2,\lambda y_1+(1-\lambda)y_2)\ge\lambda G(x_1,y_1)+(1-\lambda)G(x_2,y_2)$), then $f(x)=\max_{0\le y\le x}G(x,y)$ is concave. Proof for $0\le\lambda\le1$ (p. 21):
$$f(\lambda x+(1-\lambda)z)=\max_{0\le y\le\lambda x+(1-\lambda)z}G(\lambda x+(1-\lambda)z,y). \tag{9}$$
Write $y=\lambda y_1+(1-\lambda)y_2$ with $y_1\in[0,x]$, $y_2\in[0,z]$ independent:
$$f(\lambda x+(1-\lambda)z)=\max_{0\le y_1\le x,\,0\le y_2\le z}G(\lambda x+(1-\lambda)z,\lambda y_1+(1-\lambda)y_2). \tag{10}$$
By concavity,
$$G(\lambda x+(1-\lambda)z,\lambda y_1+(1-\lambda)y_2)\ge\lambda G(x,y_1)+(1-\lambda)G(z,y_2). \tag{11}$$
Hence
$$f(\lambda x+(1-\lambda)z)\ge\max_{y_1,y_2}[\lambda G(x,y_1)+(1-\lambda)G(z,y_2)]\ge\lambda\max_{y_1}G(x,y_1)+(1-\lambda)\max_{y_2}G(z,y_2)=\lambda f(x)+(1-\lambda)f(z). \tag{12}$$
Application: $g(y)+h(x-y)$ is concave in $(x,y)$ if $g,h$ are, so $f_1$ is concave. Likewise $f_1(ay+b(x-y))$ is concave in $(x,y)$, so $f_2$ is concave; the text breaks off here (p. 21).

*Intuition note.* Taking a maximum over a range that grows with $x$ keeps a function concave, as long as the thing being maximised is jointly concave. That is why concavity passes from $g,h$ up the recursion.

## Toy example (ours, not from the text)
Take $g(y)=y^2$, $h(y)=y$, $a=\tfrac12$, $b=0$ (so the leftover after a choice $y$ is $y/2$). Both functions are convex with $g(0)=h(0)=0$, and $c=\tfrac12$, so $m(c^nx)$ is summable. Goal: $f_3(2)$ and its policy.

Because $g,h$ are convex, only $y=0$ or $y=x$ need be tried (Theorem 4).
- $f_1(x)=\max(x^2,x)$. So $f_1(0.5)=\max(0.25,0.5)=0.5$ and $f_1(1)=1$.
- $f_2(1)=\max(g(1)+f_1(0.5),\ h(1)+f_1(0))=\max(1+0.5,\ 1+0)=1.5$, with $y_2(1)=1$.
- $f_3(2)=\max(g(2)+f_2(1),\ h(2)+f_2(0))=\max(4+1.5,\ 2+0)=5.5$, with $y_3(2)=2$.

Recover the plan forward as in (7): $y=2$, leftover $x_1=2/2=1$; $y_1=y_2(1)=1$, leftover $x_2=0.5$; last stage $f_1(0.5)$ attained at $y=0$ (the $h$ branch). The returns are $4$, $1$ and $0.5$, which sum to $5.5$ ✓. A grid search over $(y,y_1,y_2)$ would instead need $N$-dimensional enumeration; the recursion needed only three small tables.

## Concepts
- [[principle-of-optimality]] — the "key observation": after any first choice the remainder must be used optimally; the name itself is not used in these pages (p. 8)
- [[bellman-equation-value-function]] — $f_N(x)=\max_y[g(y)+h(x-y)+f_{N-1}(ay+b(x-y))]$, with $f$ the maximal return (p. 8)
- [[policy]] — a sequence of choices of $y$, as a function of $x$; optimal if it yields $f(x)$ (p. 17)
- [[state]] — here the remaining quantity $x$ together with the number of stages left $N$ (p. 7)
- [[imbedding]] (new) — solve a particular problem by solving a family indexed by $x$ and $N$ (p. 9)
- [[functional-equation]] (new) — an equation in which the unknown function appears on both sides, such as (8.1) (p. 11)
- [[successive-approximations]] (new) — iterate $f_{N+1}=\max_yT(f_N,y)$; converges under Theorem 1's conditions (p. 14, 16)
- [[approximation-in-policy-space]] (new) — improve a policy guess iteratively; return functions rise monotonically (pp. 17–18)
- [[structure-of-optimal-policy]] (new) — the shape of $y(x)$, e.g. $y\in\{0,x\}$ when $g,h$ are convex (pp. 7, 19)

## Canonical instances
- [[multi-stage-allocation-process]] — split $x$ into $y,x-y$ over N stages with shrinkage $a,b$ (p. 4)
- [[lattice-search-10-stage]] — $10^{10}$ grid evaluations, 2.77 hours at one microsecond each (p. 6)
- [[separable-allocation-problem]] — maximise $\sum g_i(x_i)$ with $\sum x_i=c$ (p. 10)
- [[smoothing-problem]] — minimise tracking plus increment penalties (p. 10)

## Bridges (candidates)
- [same-math] $f_N(x)=\max_y[\dots+f_{N-1}(\dots)]$ ↔ control-theory: Bellman equation for a finite-horizon value function — the recursion has the same form.
- [structural-analogy] Theorem 1's $u_N(x)\le u_N(cx)$, $c<1$ ↔ contraction mappings: iterating shrinks successive differences geometrically.
- [structural-analogy] Approximation in policy space ↔ policy improvement in reinforcement learning: improve a policy by one-step maximisation against its own return function.
- [structural-analogy] §7 smoothing problem ↔ tracking problems with a cost on deviation from targets and on changes: the same backward recursion.

## Questions this raises
- Under what conditions does the maximising $y_N(x)$ fail to be continuous in $x$? (The text promises an example in §15.)
- What does Theorem 3 need for convergence of the policy-improvement sequence, which the author could not prove rigorously (p. 18)?
- How do the multi-dimensional analogues, with several decisions per stage, avoid or restate the exponential growth of cost?
- Can the convex case equation (4) of §12 be solved in a particular case? (The text says it will treat one below.)

## Reading notes
- Part starts at the chapter opening (§1, printed p. 3) and ends mid-proof of Theorem 5 in §13 (printed p. 21). Printed page = pdf − 23.
- Page 3 prints the infinite-stage equation as "(1) f(x)=Max[g(y)+h(x−y)+f(ay+b(x−y))]"; the text layer garbles it; the equation is read here as (8.1) on p. 11, where it prints clearly.
- p. 5, eq. (1) third line: the image prints "g′(y) + h′(x − y) + (a − b)h′(x₁ − y₁)…". By the pattern of the two lines above, the sign before $h'(x-y)$ is probably a misprint for minus. This is my inference.
- p. 15, eq. (19): the bound is printed as $\le m(cx)$ although $f_1=g+h$; a factor 2 may be needed. This is my observation and does not affect the convergence argument.
- p. 12: boundedness for the nonnegative case is stated as shown "in a moment". No separate bound is written in these pages; presumably the convergence $\sum u_N<\infty$ on p. 15 is what is meant (my inference).
- p. 18: in Theorem 3's proof the sentence "prove the continuity of $f_0$" is printed as "$f_1$" in the text layer in one place; the image reads $f_0(x)$ and (10) concerns $f_0$.
- p. 13: the text layer reads "(0, x]" before (6); the page image prints "[0, x]". This is an OCR slip, not a printed error.
