---
id: bellman-1957-dp/ch04-iv
work: bellman-1957-dp
unit: "Chapter IV. Existence and Uniqueness Theorems"
pages: 116-151
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Existence and Uniqueness Theorems (Bellman, Dynamic Programming, Ch. IV)

## L0 — One line
A single inequality (Lemma 1) lets Picard successive approximation prove existence, uniqueness and stability for two classes (Types One and Two) of Bellman-type equations $f(p)=\operatorname{Sup}_q[g+h\,f(T(p,q))]$, without ever studying the maximizing choice $q(p)$.

## L1 — The gist (≤ 120 words)
The question: when does a dynamic-programming functional equation have a solution, is it unique, and can it be computed by iteration? Bellman proves a basic inequality comparing two such equations. With it, successive approximations converge geometrically for "Type One" (shrinking state transformation) and "Type Two" ($|h|\le a<1$) equations. This gives existence, uniqueness and stability bounds. If $h\ge0$, starting from a policy's value gives monotone convergence (given boundedness). Equations of neither type ("Type Three") need extra work, shown on an expected-time problem; an inventory integral equation follows. The chapter matters because it gives existence and uniqueness results for the equations of Chapter III.

**Prerequisites:** sup/max, norms, uniform convergence, geometric series, Stieltjes/ordinary integrals, and the functional equations of Chapters I–III.

## L2 — Key ideas
- **Lemma 1** bounds $|f_2-F_2|$ for two sup-transformations by $\operatorname{Sup}_q$ of ($|g-h|$ plus an integral of $|f_1-F_1|$). It avoids any study of how the maximizing $q$ depends on $p$ (pp. 118, 121).
- **Type One** equations (state norm shrinks, $\|T\|\le a\|p\|$, $|h|\le1$, $g(\theta,q)=0$, summability condition on $v$) have exactly one solution continuous at $\theta$ and zero there. It is the uniform limit of the iterates (pp. 119–120).
- **Type Two** equations ($|h|\le a<1$, $\|T(p,q)\|\le\|p\|$ or $D$ bounded) have a unique solution bounded on finite parts of $D$, by the same proof (p. 121).
- If $h\ge0$, starting from the value of an initial policy gives iterates that increase monotonically and, assuming they stay bounded, converge to a bounded solution (pp. 122–123).
- **Stability:** perturbing $g$ to $G$ changes the solution by at most $\sum_n u(a^nc)$ (Type One) or $u(c)/(1-a)$ (Type Two) (pp. 123–124).
- The same methods extend to several $T_i$, to Stieltjes-integral kernels and to systems; the optimal-inventory equation is an example (pp. 124–125).
- **Type Three** (neither condition): monotone iteration from a policy helps establish existence; uniqueness is generally harder and here needs a long case argument, shown for an expected-time problem (pp. 125–129).
- The inventory integral equation (Thm 6) is a contraction with factor $a\int\varphi=a<1$; monotone approximations from above and below are available (pp. 129–132).

## L3 — Walkthrough

### §1 Introduction (pp. 116–117)
- The chapter abstracts the methods of Chapters I–II and derives some existence and uniqueness theorems for the more general equations of Chapter III. The main tool is Picard's successive approximations (p. 116).
- Instead of one all-covering theorem, Bellman gives several theorems for particular classes. The method of proof is the same throughout (p. 116).
- **Type one:** each operation shrinks resources, i.e. the point transformations are shrinking (Cacciopoli) transformations. **Type two:** the survival probability decreases uniformly with each operation, which is equivalent to the functional transformation being shrinking. **Type three:** everything else (pp. 116–117).
- Both types include, in particular cases, the form
$$f(p)=\operatorname{Sup}_q\,[\,g(p,q)+h(p,q)\,f(T(p,q))\,]. \tag{1.1}$$
- Order of the chapter: existence/uniqueness, monotone convergence, stability, generalizations, a Type Three example (§8), and an inventory integral equation (§9). The equations are described as a bridge between linear and nonlinear equations (p. 117).

### §2 A fundamental inequality (pp. 117–118)
Define, with $dG(p,q,r)\ge0$,
$$S_1(f,p,q)=g(p,q)+\int_{r\in D}f(r)\,dG(p,q,r),\qquad S_2(f,p,q)=h(p,q)+\int_{r\in D}f(r)\,dG(p,q,r), \tag{2.1}$$
$$f_2(p)=\operatorname{Sup}_q S_1(f_1,p,q),\qquad F_2(p)=\operatorname{Sup}_q S_2(F_1,p,q). \tag{2.2}$$
The Stieltjes integral is used only formally. All results are applied to the case $\int f(r)\,dG\equiv h(p,q)f(T(p,q))$; a reader unfamiliar with Stieltjes integrals may make this substitution, or take $dG=H\,dr$ with $H\ge0$ (pp. 117–118).

**Lemma 1.**
$$|f_2(p)-F_2(p)|\le\operatorname{Sup}_q\Big[\,|g(p,q)-h(p,q)|+\int_{r\in D}|f_1(r)-F_1(r)|\,dG(p,q,r)\Big]. \tag{2.3}$$

*Proof* (p. 118). Assume first that both suprema are maxima. Let $q=q(p)$ attain the maximum in (2.2a) and $\bar q=\bar q(p)$ the one in (2.2b). Then
$$f_2(p)=S_1(f_1,p,q)\ge S_1(f_1,p,\bar q),\qquad F_2(p)=S_2(F_1,p,\bar q)\ge S_2(F_1,p,q). \tag{2.4}$$
Subtracting gives
$$f_2-F_2\ge\{g(p,\bar q)-h(p,\bar q)\}+\int(f_1-F_1)\,dG(p,\bar q,r),$$
$$f_2-F_2\le\{g(p,q)-h(p,q)\}+\int(f_1-F_1)\,dG(p,q,r). \tag{2.5}$$
Since $a\le x\le b$ implies $|x|\le\max(|a|,|b|)$, $|f_2-F_2|$ is at most the larger of $|g(p,\bar q)-h(p,\bar q)|+\int|f_1-F_1|\,dG(p,\bar q,r)$ and $|g(p,q)-h(p,q)|+\int|f_1-F_1|\,dG(p,q,r)$ (2.6). This gives (2.3). For a general supremum, the supremum is approached arbitrarily closely by some $q(p)$, and a limiting procedure follows (p. 118).

*Intuition note.* Two optimizers can be compared by looking only at each one's own best action. The gap between the two values is controlled by the worse of the two actions' local gaps. So we never need to know how the best action changes with the state (pp. 118, 121).

### §3 Equations of Type One (pp. 119–121)
**Conditions (3.1)** on (1.1) (p. 119):
- a. $g(p,q)$ is uniformly bounded for all $q\in S$ and all $p\in D$ with $\|p\|\le c_1$, where $\|p\|=(\sum_{i=1}^N p_i^2)^{1/2}$. $D$ is the domain of $f$, contains the null vector $\theta$, and $T(p,q)\in D$ for $p\in D$.
- b. $g(\theta,q)=0$ for all $q\in S$.
- c. $|h(p,q)|\le1$ for $p\in D$, $q\in S$.
- d. $\|T(p,q)\|\le a\|p\|$ for some $a<1$, all $q$, all $p\in D$.
- e. If $v(c)=\operatorname{Sup}_{\|p\|\le c}\operatorname{Sup}_q|g(p,q)|$, then $\sum_{n=0}^\infty v(a^nc)<\infty$.

The norm $\sum|p_i|$ may be used instead; the precise norm matters little (p. 119).

**Theorem 1.** Let
$$f(p)=\operatorname{Sup}_q[g(p,q)+h(p,q)f(T(p,q))],\ p\ne\theta;\qquad f(\theta)=0 \tag{3.2}$$
be of Type One. There is exactly one solution continuous at $\theta$ and equal to zero there, defined over all of $D$. It is the limit of
$$f_0(p)=\operatorname{Sup}_q g(p,q),\qquad f_{n+1}(p)=\operatorname{Sup}_q[g+h\,f_n(T(p,q))],\ n=0,1,2,\dots \tag{3.3}$$
Any initial $f_0$ that is continuous at $\theta$, zero there, and bounded for $\|p\|\le c_1$ (any $c_1>0$) also gives a convergent sequence. If $g,h,T$ are continuous in $p$ on any bounded portion of $D$, uniformly in $q$, then $f$ is continuous on any bounded portion of $D$ (pp. 119–120).

*Proof, existence* (p. 120). By Lemma 1, for $n\ge1$:
$$|f_{n+1}-f_n|\le\operatorname{Sup}_q|h|\,|f_n(T)-f_{n-1}(T)|\le\operatorname{Sup}_q|f_n(T(p,q))-f_{n-1}(T(p,q))|, \tag{3.4}$$
$$|f_1-f_0|\le\operatorname{Sup}_q|f_0(T(p,q))|=\operatorname{Sup}_q|g(p,q)|. \tag{3.5}$$
Define
$$v_n(c)=\operatorname{Sup}_{\|p\|\le c,\ p\in D}|f_{n+1}(p)-f_n(p)|, \tag{3.6}$$
so $v_0(c)=v(c)$ by (1e). Since $\|T\|\le a\|p\|$,
$$\operatorname{Sup}_{\|p\|\le c}|f_{n+1}-f_n|\le\operatorname{Sup}_p\operatorname{Sup}_q|f_n(T)-f_{n-1}(T)|\le\operatorname{Sup}_{\|p\|\le ac}|f_n(p)-f_{n-1}(p)|. \tag{3.7}$$
Hence each $v_n(c)$ is at most the previous one at $ac$, so $v_n(c)\le v_0(a^nc)$. By (1e), $\sum_n[f_{n+1}-f_n]$ converges uniformly for $\|p\|\le c$, so $f_n\to f$ uniformly there. Continuity follows from uniform convergence (p. 120).

*Proof, uniqueness.* Let $f,F$ be two solutions continuous at $\theta$, and let $v(c)=\sup_{\|p\|\le c}|f-F|$ (3.8). Lemma 1 gives $|f(p)-F(p)|\le\operatorname{Sup}_q|f(T(p,q))-F(T(p,q))|$ (3.9), whence
$$v(c)\le v(ac)\le\dots\le v(a^nc). \tag{3.10}$$
Continuity at $\theta$ with $f(\theta)=F(\theta)=0$ gives $v(a^nc)\to0$. So $v\equiv0$ and $f\equiv F$ (p. 120).

Lemma 1 lets us bypass the maximizing $q$ as a function of $p$, "of great difficulty about which little is known, in general" (p. 121).

*Intuition note.* Each application of $T$ moves the state closer to the origin, so errors measured on a ball of radius $c$ are controlled by errors on a smaller ball of radius $ac$. Repeating this squeezes the error to the origin, where both functions are pinned to zero.

### §4 Equations of Type Two (p. 121)
**Conditions (4.1):** a. $|g|$ uniformly bounded for $q\in S$, $\|p\|\le c_1$, $p\in D$. b. $|h(p,q)|\le a<1$ for all $q$, uniformly in any region $\|p\|\le c_1$. c. $\|T(p,q)\|\le\|p\|$ for all $p$; alternatively, $D$ is bounded and nothing is assumed about $T$ except $T(p,q)\in D$.

**Theorem 2.** For an equation (2) of Type Two there is a unique solution bounded on any finite part of $D$. It can be found by successive approximations, and the earlier statements on continuity remain valid.

*Proof.* The iteration is (3.3). Lemma 1 gives
$$|f_{n+1}-f_n|\le\operatorname{Sup}_q|h|\,|f_n(T)-f_{n-1}(T)|\le a\operatorname{Sup}_q|f_n(T(p,q))-f_{n-1}(T(p,q))|,\quad a<1. \tag{4.4}$$
From here the proof parallels Theorem 1. The vanishing at $\theta$ is now a consequence of the equation itself (p. 121).

*Intuition note.* In Type Two the contraction comes from $h$, a survival-probability factor below 1, rather than from the geometry of $T$. Successive differences of the iterates shrink by a factor $a$ per step.

### §5 Monotone convergence (pp. 122–123)
Assume $h(p,q)\ge0$ (true in all applications to date). Write $f(p)=\operatorname{Max}_q[g+h\,f(T(p,q))]$ (5.1). Take an initial policy $q_0(p)$ and let $f_0$ be its value:
$$f_0(p)=g(p,q_0)+h(p,q_0)f_0(T(p,q_0)), \tag{5.2}$$
$$f_{n+1}(p)=\operatorname{Sup}_q[g+h\,f_n(T(p,q))],\quad n=0,1,2,\dots \tag{5.3}$$
The supremum is used to avoid questions about continuity over $q$. Assume the $f_n$ are uniformly bounded on finite portions of $D$ (p. 122).
- It is "immediately seen" that $f_1\ge f_0$. By $h\ge0$, $f_{n+1}\ge f_n$ for all $n$. So $f_n\to f$ on any finite part of $D$ (p. 122).
- If $S$ is finite, $f$ solves the equation with Max. If $S$ is a continuum, one shows $f$ is the bounded solution of (5.4), the equation with Sup.
- By monotone convergence, $f_{n+1}\le\operatorname{Sup}_q[g+h\,f(T)]$ (5.5). Letting $n\to\infty$ gives $f\le\operatorname{Sup}_q[g+h\,f(T)]$ (5.6).
- Conversely $f(p)\ge\operatorname{Sup}_q[g+h\,f_n(T)]\ge g(p,q)+h(p,q)f_n(T(p,q))$ for all $q$ and $n$ (5.7). Letting $n\to\infty$ gives the reverse of (5.6), hence equality (p. 123).

This is useful for some Type Three equations where geometric convergence is hard or absent (p. 122). It is also useful in the calculus of variations, later (p. 123).

*Intuition note.* If you start from the value of a concrete plan, one round of choosing the best action can only improve it. With non-negative weights the improvement never reverses, so the sequence rises; with the assumed uniform bound it converges.

### §6 Stability theorems (pp. 123–124)
Compare two Type One equations: $f$ for $g$ (6.1a) and $F$ for $G$ (6.1b), with the same $h$ and $T$. Both solutions vanish and are continuous at $\theta$. Iterate both, with $f_1=\operatorname{Sup}g$, $F_1=\operatorname{Sup}G$ and the recursions as in (3.3) (printed (6.2), indexed from 1). By Lemma 1:
$$|F_1-f_1|\le\operatorname{Sup}_q|G-g|, \tag{6.3}$$
$$|F_{n+1}-f_{n+1}|\le\operatorname{Sup}_q\big[\,|G-g|+h(p,q)\,|F_n(T)-f_n(T)|\,\big]. \tag{6.4}$$
(The printed (6.4) shows $h$ without absolute value; with $|h|\le1$ this is what the bound uses.) Define
$$u(c)=\operatorname{Sup}_{\|p\|\le c}\operatorname{Sup}_q|G(p,q)-g(p,q)|. \tag{6.5}$$

**Theorem 3** (Type One):
$$\operatorname{Sup}_{\|p\|\le c}|F(p)-f(p)|\le\sum_{n=0}^\infty u(a^nc). \tag{6.6}$$
*Proof.* Let $w_n(c)=\operatorname{Sup}_{\|p\|\le c}\operatorname{Sup}_q|F_n-f_n|$ (6.7). One shows inductively that $w_n(c)\le\sum_{k=0}^{n-1}u(a^kc)$ for $n\ge1$, using (6.4) and the Type One hypotheses. Then let $n\to\infty$, since $F_n\to F$ and $f_n\to f$ (p. 124).
(added step) Inductive step: (6.4) and $\|T\|\le a\|p\|$ give $w_{n+1}(c)\le u(c)+w_n(ac)\le u(c)+\sum_{k=0}^{n-1}u(a^{k+1}c)$.

**Theorem 4** (Type Two): $\operatorname{Sup}_{\|p\|\le c}|F-f|\le u(c)/(1-a)$ (6.8). The proof is "the same lines" and omitted. Similar estimates hold when $h$ or $T$ is perturbed (p. 124).

*Intuition note.* A small change in the data of the equation cannot cause a much bigger change in the solution. In Type Two the amplification factor is the geometric-series sum $1/(1-a)$.

### §7 Some directions of generalization (pp. 124–125)
- A first generalization is $f(p)=\operatorname{Sup}_q[g+\sum_{i=1}^N h_i(p,q)f(T_i(p,q))]$ (7.1). It is a case of $f(p)=\operatorname{Sup}_q[g+\int_{r\in D}f(r)\,dG(p,q,r)]$ (7.2).
- The methods give analogues of the existence, uniqueness and stability theorems for these. The same holds for systems $f_i(p)=\operatorname{Sup}_q[g_i+\sum_{j=1}^N\int f_j(r)\,dG_{ij}(p,q,r)]$, $i=1,\dots,N$ (7.3). In vector–matrix notation (7.3) has the same form as (7.2) (p. 125).
- Example of (7.2), the optimal-inventory equation: $f(x)=\operatorname{Inf}_{y\ge x}[v(x,y)+a[(1-G(y))f(0)+\int_0^yf(y-s)\,dG(s)]]$ (7.4) (p. 125).

### §8 An equation of the third type (pp. 125–129)
Type Three equations are those that are neither Type One nor Two. Approximation in policy space (§5) is described as very useful for establishing existence; uniqueness is, in general, harder (p. 125). The example:
$$f(p)=\operatorname{Min}\Big[1+\sum_{k=0}^np_kf(x_k),\ \operatorname{Min}_l\,[1+f(T_lp)]\Big],\ p\ne x_0;\qquad f(x_0)=0, \tag{8.1}$$
with $l=1,\dots,M$. Here $p=(p_0,\dots,p_n)$, $p_i\ge0$, $\sum p_i=1$. $T_lp=(p_{0l},\dots,p_{nl})$ has $p_{il}\ge0$, $p_{0l}\ne1$, $\sum_ip_{il}=1$, where $p_{il}=p_{il}(p)$. $x_k=(0,\dots,1,\dots,0)$ has its 1 in place $k$. $f$ is a scalar function of $p$ (8.2) (p. 125).

*Interpretation* (p. 126). A system is in one of $N+1$ states $0,\dots,N$ with probabilities $\{p_k\}$. Each operation takes one unit of time. We want to bring the system to state 0 with certainty in minimum expected time. The options are: **L**, observe the actual state and proceed with that knowledge; **A**$_l$, apply an operation that turns $\{p_k\}$ into $\{p_{kl}\}$. $f(p)$ is the minimum expected time and satisfies (8.1). This extends Exercise 39 of Chapter I (p. 126).

**Theorem 5.** If for each $T_l$ and all $p$
$$\sum_{k=1}^np_{kl}\le c_1,\quad0<c_1<1, \tag{8.3}$$
then (8.1) has a unique bounded solution, positive for $p\ne x_0$ (p. 126).

*Proof, existence* (pp. 126–127). Use as first approximation the values of two policies in policy space. $L$ is the choice $1+\sum_{k=0}^np_kf(x_k)$ and $T_1$ is the choice $l=1$. $F_1$ is the value of the policy symbolized $LT_1LT_1\dots$ and $F_2$ that of $T_1LT_1L\dots$:
$$F_1(p)=1+F_2(T_1p),\quad F_2(p)=1+\sum_{k=0}^np_{kl}F_1(x_k)\ (p\ne x_0),\quad F_1(x_0)=F_2(x_0)=0. \tag{8.4}$$
(Printed as shown; see Reading notes on the subscripts.) Hence
$$F_1(x_l)=2+\sum_{k=1}^np_{kl}F_1(x_k),\quad l=1,\dots,n. \tag{8.5}$$
By (8.3) the determinant of this system does not vanish. It has a unique solution, "necessarily positive, as we see by solving iteratively". Then $F_2$ and $F_1$ follow for general $p$ (pp. 126–127). Define
$$f_0(p)=\operatorname{Min}[F_1(p),F_2(p)],\quad f_{n+1}(p)=\operatorname{Min}\Big[1+\sum_{k=1}^np_kf_n(x_k),\ \operatorname{Min}_l[1+f_n(T_lp)]\Big],\ p\ne x_0,\quad f_{n+1}(x_0)=0. \tag{8.6}$$
It is "readily seen" that $f_0\ge f_1\ge\dots\ge f_n\ge1$ for $p\ne x_0$. So $f_n$ converges monotonically to a function $f$ that "clearly" satisfies the equation, which gives a bounded solution (p. 127).

*Uniqueness.* The proof is "considerably more complicated". Let $f,g$ be two bounded solutions.

**Lemma 2.** $\operatorname{Sup}_p|f(p)-g(p)|=\operatorname{Max}_k|f(x_k)-g(x_k)|$.
The inequality "$\ge$" (8.7) is clear. For "$\le$" consider four cases (8.8) for the first-move choices in $f$ and $g$:
- (a) both use $L$;
- (b) $f$ uses $L$, $g$ uses $T_l$;
- (c) the reverse of (b);
- (d) both use $T$-moves, $T_l$ for $f$ and $T_{l'}$ for $g$.

Case (a): $f-g=\sum_{k=0}^np_k[f(x_k)-g(x_k)]$ (8.9), so $|f-g|\le\operatorname{Max}_k|f(x_k)-g(x_k)|$ (8.10). Case (a) holds whenever $p$ is close to $x_0$: then $1+\sum_{k\ge1}p_kf(x_k)<2$, while $1+f(T_lp)\ge2$, so the $L$-move wins (p. 128). The crux of the proof is that (a) "will always occur after a finite number of moves, by virtue of the condition in (3)" (p. 128).
Case (b): $f=1+\sum p_kf(x_k)\le1+f(T_lp)$ and $g=1+g(T_lp)\le1+\sum p_kg(x_k)$ (8.11). Hence
$$|f-g|\le\operatorname{Max}\{\operatorname{Max}_k|f(x_k)-g(x_k)|,\ \operatorname{Sup}_p|f(T_lp)-g(T_lp)|\}, \tag{8.12}$$
and similarly for (c). Case (d):
$$|f-g|\le\operatorname{Max}\{|f(T_lp)-g(T_lp)|,\ |f(T_{l'}p)-g(T_{l'}p)|\}. \tag{8.13}$$
Iterate these. For fixed $p$, $T_{l_1}T_{l_2}\dots T_{l_n}p$ lies in the region of case (a) for large $n$. So $\operatorname{Sup}_p|f-g|\le\operatorname{Max}_k|f(x_k)-g(x_k)|$ (8.14), which proves the lemma (p. 128).

*Remaining step* (pp. 128–129). Show $\operatorname{Max}_k|f(x_k)-g(x_k)|=0$. Let $k$ attain the maximum. The functional equations give
$$f(x_k)=1+f(T_lx_k),\ l=l(k);\qquad g(x_k)=1+g(T_{l'}x_k),\ l'=l'(k). \tag{8.15}$$
Also
$$f(x_k)\le1+f(T_{l'}x_k),\qquad g(x_k)\le1+g(T_lx_k). \tag{8.16}$$
If both inequalities were strict, then
$$|f(x_k)-g(x_k)|<\operatorname{Max}\{|f(T_lx_k)-g(T_lx_k)|,\ |f(T_{l'}x_k)-g(T_{l'}x_k)|\}\le\operatorname{Sup}_p|f-g|, \tag{8.17}$$
a contradiction. So for $l$ or $l'$ we have $f(x_k)=1+f(T_lx_k)$ or $g(x_k)=1+g(T_lx_k)$ (8.18). The first choices from $x_k$ can be the same, and the same argument applies to second moves, and so on inductively. Let $p_n=p_n(x_k)$ be the distribution after $n$ moves, where the $(n+1)$st move puts $x_k$ into the region of case (a). Then $f$ and $g$ land there on the same move, and
$$f(x_k)=(n+1)+\sum_{k=0}^np_{kn}f(x_k),\qquad g(x_k)=(n+1)+\sum_{k=0}^np_{kn}g(x_k), \tag{8.19}$$
$$|f(x_k)-g(x_k)|\le\sum_{k=1}^np_{kn}|f(x_k)-g(x_k)|\le|1-p_{0n}|\operatorname{Sup}_k|f(x_k)-g(x_k)|. \tag{8.20}$$
Since $1>p_{0n}>0$ (as stated), $|f(x_k)-g(x_k)|=0$. Hence $\operatorname{Sup}_p|f-g|=0$ (p. 129).

*Intuition note.* Neither the shrinking nor the discount mechanism applies here. Uniqueness instead comes from the fact that, after finitely many moves, every strategy ends in an "observe the state" step that mixes only the vertex values $f(x_k)$. At the vertices, the largest disagreement cannot survive that mixing.

### §9 An "optimal inventory" equation (pp. 129–132)
For $x\ge0$:
$$f(x)=\operatorname{Inf}_{y\ge x}\Big[k(y-x)+a\Big[\int_y^\infty p(s-y)\varphi(s)\,ds+f(0)\int_y^\infty\varphi(s)\,ds+\int_0^yf(y-s)\varphi(s)\,ds\Big]\Big]. \tag{9.1}$$
Write the bracket as $T(y,x,f)$ (9.2), so $f(x)=\operatorname{Inf}_{y\ge x}T(y,x,f)$ (9.3). The equation arises in "optimal inventory" or "stock level" control (next chapter). Only the non-Stieltjes form is treated (p. 130).

**Conditions (9.4):** a. $\varphi(s)\ge0$, $\int_0^\infty\varphi\,ds=1$. b. $p(s)$ is monotone increasing, continuous, and $\int_0^\infty p(s)\varphi(s)\,ds<\infty$. c. $k(y)$ is continuous for $y\ge0$, $k(\infty)=\infty$. d. $0<a<1$ (p. 130).

**Theorem 6.** There is a unique solution of (9.1) bounded for $x$ in any finite interval, and it is continuous. Let $f_0$ be any non-negative continuous function on $0\le x$, and
$$f_{n+1}(x)=\operatorname{Min}_{y\ge x}T(y,x,f_n),\quad n=0,1,2,\dots \tag{9.5}$$
Then $f=\lim f_n$ exists for $x\ge0$ and solves $f(x)=\operatorname{Min}_{y\ge x}T(y,x,f)$ (9.6) (p. 130).

*Proof* (p. 131). Let $y_n=y_n(x)$ attain the minimum of $T(y,x,f_n)$. Each $f_n$ is continuous inductively. The minimum is attained since $T(\infty,x,f_n)=\infty$. Then
$$f_{n+1}=T(y_n,x,f_n)\le T(y_{n-1},x,f_n),\qquad f_n=T(y_{n-1},x,f_{n-1})\le T(y_n,x,f_{n-1}). \tag{9.7}$$
Combining these in the usual way,
$$|f_{n+1}-f_n|\le\operatorname{Max}\{|T(y_n,x,f_n)-T(y_n,x,f_{n-1})|,\ |T(y_{n-1},x,f_n)-T(y_{n-1},x,f_{n-1})|\}. \tag{9.8}$$
Writing out the first term of (9.9): it is $a\int_0^{y_n}|f_n(y_n-s)-f_{n-1}(y_n-s)|\varphi\,ds+a|f_n(0)-f_{n-1}(0)|\int_{y_n}^\infty\varphi\,ds$. The second is the same with $y_{n-1}$ in place of $y_n$ (the printed second term of (9.9) has $f_{n-1}(y_n-s)$ in the integrand). Hence
$$\operatorname{Max}_x|f_{n+1}-f_n|\le a\operatorname{Max}_x|f_n-f_{n-1}|\int_0^\infty\varphi\,ds\le a\operatorname{Max}_x|f_n-f_{n-1}|. \tag{9.10}$$
Thus $\sum(f_{n+1}-f_n)$ converges uniformly in a finite interval, $f_n\to f$, and $f$ is continuous as a limit of continuous functions. For uniqueness, let $F$ be another solution uniformly bounded for $x\ge0$. The same technique applied to the two equations (9.11) shows $F-f\equiv0$. The case with Inf in (9.1) is handled by an approximation process (p. 131).

*Monotone approximations* (p. 132).
- Take $f_1(x)=\operatorname{Min}_{y\ge x}[k(y-x)+a\int_y^\infty p(s-y)\varphi\,ds]$ and $f_2=\operatorname{Min}_{y\ge x}T(y,x,f_1)$ (9.12), and so on. Then $f_2\ge f_1$ and inductively $f_{n+1}\ge f_n$: monotone increasing convergence.
- Alternatively, approximate in policy space with $y=x$ for all $x\ge0$. This gives, as printed, $f_1(x)=a\int_0^\infty p(s-x)\varphi(s)\,ds+a\int_0^xf_1(x-s)\varphi(s)\,ds+af_1(0)\int_x^\infty\varphi(s)\,ds$ for $x\ge0$ (9.13), a "renewal equation" whose solution is discussed in an appendix to the next chapter. Then define $f_2$ by (9.14) (the minimization with $f_1$ inside). It follows that $f_2\le f_1$. With $f_{n+1}=\operatorname{Min}_{y\ge x}T(y,x,f_n)$ (9.15) we get monotone decreasing convergence.

*Intuition note.* The inventory operator averages $f$ over the random demand with total weight $a\int\varphi=a<1$. That is a contraction, so the iteration converges, in the uniform norm, to a unique continuous fixed point. Starting from the cost of a simple policy gives a sequence from above, and starting from the penalty alone gives one from below.

### Exercises and Research Problems (pp. 132–150) and Bibliography (p. 151)
- Seventy problems follow. They include the structure of optimal policies under convexity (Ex. 1); systems and extensions of the theorems (Ex. 2–11); iterative root-finding via max/min representations (Ex. 12–17); a gambler betting on information received over a noisy channel (Ex. 33–43, with Kelly's logarithmic criterion in Ex. 34–36); the optimal routing problem (Ex. 28–31); a multi-stage rocket (Ex. 55); and chain-structured linear and quadratic problems (Ex. 56–64). The problems are listed without solutions (pp. 132–150).
- The chapter follows Bellman, "Functional equations in the Theory of Dynamic Programming — I", Trans. AMS 80 (1955). A more abstract treatment using Tychonoff's theorem is in an unpublished Karlin–Shapiro RAND memorandum. The choice of $f_0$ in (8.6) is credited to H. N. Shapiro (p. 151).

## Toy example (ours, not from the text)
**Setup.** A Type Two equation on a bounded domain. States $p\in\{1,2\}$, actions $q\in\{A,B\}$, $h\equiv0.5$ (so $a=0.5$).

| $(p,q)$ | $g$ | $T(p,q)$ |
|---|---|---|
| (1,A) | 2 | 2 |
| (1,B) | 1 | 1 |
| (2,A) | 0 | 1 |
| (2,B) | 3 | 2 |

The equation is $f(p)=\max_q[g(p,q)+0.5\,f(T(p,q))]$. Start at $f_0(p)=\max_q g$, so $f_0=(2,3)$.
- $f_1(1)=\max(2+0.5\cdot3,\ 1+0.5\cdot2)=\max(3.5,2)=3.5$. $f_1(2)=\max(0+0.5\cdot2,\ 3+0.5\cdot3)=\max(1,4.5)=4.5$.
- $f_2(1)=\max(2+2.25,\ 1+1.75)=4.25$. $f_2(2)=\max(0+1.75,\ 3+2.25)=5.25$.
- $f_3(1)=\max(2+2.625,\ 1+2.125)=4.625$. $f_3(2)=\max(0+2.125,\ 3+2.625)=5.625$.

**Contraction check.** $\max|f_{n+1}-f_n|$ is $1.5,\ 0.75,\ 0.375$ (using $f_1-f_0=(1.5,1.5)$, etc.). Each is $0.5\times$ the previous, as the Theorem 2 argument predicts.

**Fixed point.** Guess policy A at 1, B at 2: $f(2)=3+0.5f(2)\Rightarrow f(2)=6$, and $f(1)=2+0.5\cdot6=5$. Check the other actions: $1+0.5\cdot5=3.5<5$ and $0+0.5\cdot5=2.5<6$. So $f=(5,6)$. The iterates' errors are $3,1.5,0.75,0.375$, halving each time.

**Stability (Theorem 4).** Replace $g$ by $G=g+0.1$, so $u=0.1$ and the bound is $u/(1-a)=0.2$. The new fixed point satisfies $F(2)=3.1+0.5F(2)$, so $F(2)=6.2$, and $F(1)=2.1+3.1=5.2$. The other actions give $1.1+2.6=3.7<5.2$ and $0.1+2.6=2.7<6.2$. The difference from $f$ is $0.2$, exactly at the bound.

## Concepts
- [[bellman-equation-value-function]] — the functional equation $f(p)=\operatorname{Sup}_q[g+h f(T(p,q))]$ whose solution is the optimal return; (1.1) (p. 116)
- [[successive-approximations]] (new) — Picard iteration $f_{n+1}=\operatorname{Sup}_q[g+h f_n(T)]$ used to prove existence and uniqueness (p. 116)
- [[fundamental-inequality-lemma-1]] (new) — bound on $|f_2-F_2|$ for two sup-transformations without studying the maximizer (p. 118)
- [[shrinking-transformation]] (new) — $\|T(p,q)\|\le a\|p\|$, $a<1$ (Cacciopoli), the basis of Type One (pp. 116, 119)
- [[type-one-equation]] (new) — Bellman's class with conditions (3.1): shrinking $T$, $|h|\le1$, $g(\theta,q)=0$, $\sum v(a^nc)<\infty$ (p. 119)
- [[type-two-equation]] (new) — class with $|h|\le a<1$ and $\|T\|\le\|p\|$ or $D$ bounded (p. 121)
- [[type-three-equation]] (new) — any equation not of Type One or Two (p. 117)
- [[monotone-convergence-policy-space]] (new) — with $h\ge0$, start from the value of an initial policy; iterates are monotone (p. 122)
- [[policy]] — the choice $q=q(p)$ of action as a function of state; here also the initial approximation $q_0(p)$ (p. 122)
- [[stability]] — in this chapter: small changes in the equation give small changes in the solution (bounds in Thm 3–4) (p. 123)
- [[exploration-vs-exploitation]] is not used. [[principle-of-optimality]] is only implicit (the equations come from Ch. III).

## Canonical instances
- [[optimal-inventory-equation]] — stock-control integral equation, Thm 6; a contraction with monotone approximations (pp. 125, 129–132)
- [[expected-time-to-known-state]] — Type Three problem of reaching state 0 with certainty, by observing (L) or transforming ($T_l$) (pp. 125–129)
- [[kelly-gambler-noisy-channel]] — Exercises 33–36: betting on information over a noisy channel (pp. 140–141)
- [[multistage-rocket]] — Exercise 55: minimum-weight $k$-stage rocket as a recursion (p. 146)
- [[routing-problem]] — Exercises 28–31: shortest route as $f_i=\min_j[t_{ij}+f_j]$ (p. 139)

## Bridges (candidates)
- [same-math] Type Two equation with constant $h=\beta$ and sup over actions ↔ control-theory: value iteration for a discounted decision process; the argument is a sup-norm contraction by factor $\beta$.
- [structural-analogy] §5 monotone convergence from an initial policy's value ↔ policy iteration (improve a policy's value by one greedy step); the source only does the iteration, not full policy evaluation each round.
- [structural-analogy] Stability Thm 3–4 ($u(c)/(1-a)$) ↔ robustness: error in the model data bounded by a geometric-series amplification.
- [structural-analogy] Type Three problem with $p$ a probability vector over states ↔ belief-state formulation of decisions under partial observation: "observe the true state" resets the belief to a vertex.

## Questions this raises
- How does Lemma 1 relate to modern contraction-mapping arguments for Bellman operators, and what is lost when $h$ can be negative or equal to 1?
- In Type Three, why is $1>p_{0n}>0$ guaranteed along the paths used in (8.19)–(8.20)? Does condition (8.3) imply it?
- What happens to Theorems 1–2 when $S$ is a continuum and the sup is not attained? The text handles this only by "a limiting procedure".
- Can the monotone sequences from above and below (§9) be used together to get two-sided error bounds?

## Exercises worth doing
- Ex. 2 (p. 133) — carry the existence/uniqueness proof to systems of equations with integral kernels $dG_{ij}$ — difficulty: medium
- Ex. 12 (p. 134) — solve $x^2+ax=b$ via max/min representations and obtain two-sided bounds — difficulty: medium
- Ex. 17 (p. 135) — express a root found by Newton's method as a minimum over $y$ — difficulty: medium
- Ex. 29 (p. 139) — show the routing equation has a solution unique up to an additive constant; contrast with the unique solutions above — difficulty: hard
- Ex. 31 (p. 139) — prove convergence of approximation in policy space for the routing problem — difficulty: medium
- Ex. 36 (p. 141) — show by induction that with log utility $f_N(x)=\log x+Nk$ and a constant betting fraction is optimal — difficulty: medium

## Reading notes
- Printed pages 116–151 correspond to pdf pages 139–174 (printed = pdf − 23). Equation numbers in L3 are printed as (n) within each section; I prefix section numbers for clarity.
- The text layer is garbled in places (§§ 3, 5, 6, 8, 9); all equations were checked against the page images.
- Indices in (3.5)–(3.7): the printed $v_{n+1}(c)\le v_n(ac)$ ($n\ge0$) agrees with $v_n(c)\le v_{n-1}(ac)$ ($n\ge1$) obtained from (3.4) and (3.7); both give $v_n(c)\le v_0(a^nc)$. In (3.5), the equality $\operatorname{Sup}_q|f_0(T(p,q))|=\operatorname{Sup}_q|g(p,q)|$ is stated without justification: the left side is $f_0$ evaluated at the transformed point. §6 starts the iterates at $f_1$ rather than $f_0$.
- §8 uses $N$ and $n$ for the number of states interchangeably, and $k$ and $n$ do double duty in (8.19)–(8.20). In (8.4)–(8.5) the subscript $l$ labels both a transformation and a vertex $x_l$, and the second line of (8.4) shows $p_{kl}$ rather than $p_k$, which I could not reconcile with the policy ordering in the text. (8.5) is consistent if $p_{kl}$ denotes the components of $T_1x_l$. I reproduced (8.4) as printed.
- In (9.13) the first integral's lower limit appears to be printed as 0, whereas substituting $y=x$ into (9.2) would give $x$. I reproduced it as printed.
- The source omits the Theorem 4 proof ("same lines as above") and only remarks that similar estimates can be obtained when $h$ and $T$ are perturbed.
- The exercises (Ex. 1–70) are printed without solutions. I did not solve any.
