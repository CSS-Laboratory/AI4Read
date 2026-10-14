---
id: spielman-2025-sagt/ch35-conjugate
work: spielman-2025-sagt
unit: "Chapter 35 — The Conjugate Gradient and Diameter"
pages: 280–286
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# The Conjugate Gradient and Diameter

## L0 — One line
Conjugate Gradient (CG) finds the A-norm-optimal vector in the Krylov subspace using an A-orthogonal basis, and the same polynomial viewpoint shows that a Laplacian with few distinct eigenvalues forces a small graph diameter.

## L1 — The gist (≤ 120 words)
How should we measure the error of an iterative solver for $Ax=b$, and how well can the solver do? The chapter measures error in the A-norm. It shows that CG gives the best $x_t$ in the Krylov subspace, using a short recurrence on an A-orthogonal basis, with $t$ multiplications by $A$. CG is "at least as good as" Chebyshev iteration, and in exact arithmetic it should need at most $k-1$ iterations for $k$ distinct eigenvalues. For Laplacians, fast polynomial solvers imply small diameter: for a connected graph, at most $k$ distinct nonzero eigenvalues gives diameter $\le k$, and diameter $\le (\tfrac12\sqrt{\lambda_n/\lambda_2}+1)\ln 2n$.

**Prerequisites:** positive semidefinite matrices and $A^{1/2}$; spectral norm; Loewner order ($X\preceq Y$ means $Y-X$ is PSD); Krylov subspaces; graph Laplacian and its pseudoinverse; polynomials in a matrix.

## L2 — Key ideas
- The A-norm $\|x\|_A=\sqrt{x^TAx}$ is, for many applications, the right way to measure solver error. A polynomial $p$ with $\|p(A)A-I\|\le\epsilon$ gives A-norm error at most $\epsilon\|x\|_A$ (p. 280).
- A positive definite $Z$ has A-norm error $\le\epsilon$ for all $x$ iff $(1-\epsilon)A^{-1}\preceq Z\preceq(1+\epsilon)A^{-1}$ (Thm 35.1.1, p. 281).
- For approximate Fiedler vectors, the A-norm is the right kind of approximation, and the author runs the power method with an approximate inverse $Z$ (p. 281).
- CG minimizes $\tfrac12x_t^TAx_t-b^Tx_t$ over the Krylov subspace. With an A-orthogonal basis the coefficients decouple: $c_i=b^Tp_i/(p_i^TAp_i)$ (pp. 282–283).
- The basis obeys a three-term recurrence, so $t$ multiplications by $A$ and $O(tn)$ other work suffice (pp. 283–284).
- With $k$ distinct eigenvalues CG should finish in $k-1$ iterations in exact arithmetic. It works well when eigenvalues cluster (pp. 284–285).
- For Laplacians the goal is $p(L)L=\Pi$ (p. 285).
- Diameter $\le k$ for a connected graph with at most $k$ distinct nonzero eigenvalues (Thm 35.6.1, p. 286). Chung–Faber–Manteuffel gives, for any connected graph, $(\tfrac12\sqrt{\lambda_n/\lambda_2}+1)\ln 2n$ (Thm 35.6.2, p. 286).

## L3 — Walkthrough

### 35.1 The matrix norm (pp. 280–281)
For PSD $A$: $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$ (p. 280). The author says this is often the right accuracy measure for $\|x-x_t\|_A$, and that it passes naturally to outer algorithms that call the solver (p. 280).

Richardson and Chebyshev iteration produce $x_t=p(A)b$. If $\|p(A)A-I\|\le\epsilon$, then, using $b=Ax$:
$$\|p(A)b-x\|_A=\|A^{1/2}p(A)Ax-A^{1/2}x\|=\|(p(A)A-I)A^{1/2}x\|\le\epsilon\|A^{1/2}x\|=\epsilon\|x\|_A.$$
This works because $p(A)$ commutes with $A$. Most solvers are linear operators that do not commute with $A$, but they can still have small A-norm error (p. 281).

**Theorem 35.1.1.** For positive definite $A,Z$: $\|ZAx-x\|_A\le\epsilon\|x\|_A$ for all $x$ $\iff$ $(1-\epsilon)A^{-1}\preceq Z\preceq(1+\epsilon)A^{-1}$ (p. 281).

*Proof (p. 281).* The condition is equivalent to $\|A^{1/2}(ZA-I)x\|\le\epsilon\|A^{1/2}x\|$ for all $x$. Put $y=A^{1/2}x$: $\|(A^{1/2}ZA^{1/2}-I)y\|\le\epsilon\|y\|$ for all $y$. This means $\|A^{1/2}ZA^{1/2}-I\|\le\epsilon$, which is equivalent to
$$-\epsilon I\preceq A^{1/2}ZA^{1/2}-I\preceq\epsilon I\iff(1-\epsilon)I\preceq A^{1/2}ZA^{1/2}\preceq(1+\epsilon)I\iff(1-\epsilon)A^{-1}\preceq Z\preceq(1+\epsilon)A^{-1},$$
the last step by multiplying left and right by $A^{-1/2}$.

*Intuition note.* "Small A-norm error for every $x$" and "$Z$ is a spectral $\epsilon$-approximation of $A^{-1}$" are equivalent for positive definite $A$ and $Z$ (Thm 35.1.1). So, in that setting, a solver can be judged either way.

### 35.2 Approximating Fiedler vectors (p. 281)
For the smallest eigenvalue, it is natural to use the power method on the inverse. Since only approximations are computed, we might as well use an approximate inverse $Z$ ($\epsilon$-approximating $A^{-1}$) instead. Its top eigenvalue is within $1\pm\epsilon$ of that of $A^{-1}$, and its eigenvector has large Rayleigh quotient for $A^{-1}$. If there is an eigenvalue gap, that vector makes a small angle with the true eigenvector. The author refers to [ST14, §7] (p. 281).

### 35.3 Optimality in the A-norm (pp. 282–284)
After $t$ iterations the iterate lies in $\mathrm{span}\{b,Ab,\dots,A^tb\}$, the $(t{+}1)$st Krylov subspace (p. 282). Expanding,
$$\|x_t-x\|_A^2=x_t^TAx_t-2b^Tx_t+b^Tx.$$
Since $b^Tx$ is fixed, minimize
$$\tfrac12x_t^TAx_t-b^Tx_t.\tag{35.2}$$
Write $x_t=\sum_{i=0}^tc_ip_i$ for a basis $p_0,\dots,p_t$ of the subspace. Then (35.2) equals
$$\tfrac12\sum_i c_i^2p_i^TAp_i-\sum_ic_ib^Tp_i+\tfrac12\sum_{i\ne j}c_ic_jp_i^TAp_j.$$
CG chooses an **A-orthogonal** basis, meaning $p_i^TAp_j=0$ for $i\ne j$. The cross term vanishes, the terms for different $i$ do not interact, and each is minimized separately. Setting the derivative in $c_i$ to zero gives $c_i=\dfrac{b^Tp_i}{p_i^TAp_i}$ (pp. 282–283).

*Basis construction (p. 283).* Start with $p_0=b$. Then $p_1=Ap_0-p_0\frac{(Ap_0)^TAp_0}{p_0^TAp_0}$, and $p_0^TAp_1=0$. In general:
$$p_{t+1}=Ap_t-\sum_{i=0}^tp_i\frac{(Ap_t)^TAp_i}{p_i^TAp_i}.\tag{35.3}$$
*Check, assuming $p_0,\dots,p_t$ are A-orthogonal:* for $j\le t$, only the $i=j$ term survives in the sum, so
$$p_j^TAp_{t+1}=p_j^TA^2p_t-p_j^TAp_j\frac{(Ap_t)^TAp_j}{p_j^TAp_j}=0.$$
*Simplification:* for $i<t-1$, $(Ap_t)^TAp_i=p_t^TA(Ap_i)=0$, because $Ap_i\in\mathrm{span}\{p_0,\dots,p_{i+1}\}$ and $i+1<t$. Hence
$$p_{t+1}=Ap_t-p_t\frac{(Ap_t)^TAp_t}{p_t^TAp_t}-p_{t-1}\frac{(Ap_t)^TAp_{t-1}}{p_{t-1}^TAp_{t-1}}.$$
Each $p_{t+1}$ needs only a constant number of multiplications by $A$ and vector operations. So the whole basis costs $O(t)$ of each (p. 283).

Then $x_t=\sum_{i=0}^tp_i\frac{b^Tp_i}{p_i^TAp_i}$ costs $O(t)$ more operations. Only $t$ multiplications by $A$ are needed in total, since every term derives from the products $Ap_i$. So CG finds the A-norm-optimal $x_t$ in time $O(tn)$ plus $t$ multiplications by $A$ (p. 284).

**Caution (author):** the implemented CG rearranges this computation to keep vector norms small. The version presented here would fail in practice because the $p_i$ become too large (p. 284).

*Intuition note.* A-orthogonality makes the "best combination" problem split into independent one-number problems. The recurrence is short because $(Ap_t)^TAp_i=p_t^TA(Ap_i)$ vanishes for $i<t-1$. This is why CG is cheap.

### 35.4 How good is CG? (pp. 284–285)
- The author says CG is at least as good as Chebyshev iteration: for any number of iterations it finds a vector with smaller A-norm error (p. 284).
- It should never need more than $n$ iterations, since $x$ lies in the $n$th Krylov subspace (p. 284).
- Let $\lambda_1,\dots,\lambda_k$ be the *distinct* eigenvalues of $A$, and $q(x)=\prod_{i=1}^k(\lambda_i-x)/\prod_{i=1}^k\lambda_i$. Then $q$ has degree $k$, $q(0)=1$ and $q(\lambda_i)=0$ for all $i$. So CG *should* find the exact answer in $k-1$ iterations. This holds with infinite-precision arithmetic but not quite so well in practice (p. 284).
- Sparse $A$ (at most $cn$ nonzeros, $c$ constant; the author says this is not rigorous): a multiplication costs $O(n)$, so CG solves one system in $O(n^2)$ time. This is proportional to the time just to write down $A^{-1}$ (p. 284).
- The hypercube on $n$ vertices has $\log_2 n$ distinct eigenvalues, so CG needs only $\log_2 n$ iterations. CG also works well on graphs merely very close to the hypercube (pp. 284–285).
- In general CG is especially fast when eigenvalues form a few clusters or there are a few extreme eigenvalues. The author defers this to the next lecture (p. 285).

### 35.5 Laplacian systems, again (p. 285)
$L$ has no inverse, so we want a polynomial approximating the pseudoinverse. Exact solving would give $p(L)b=x$ with $b=Lx$, so $p(L)Lx=x$. This is reasonable only if $x\in\mathrm{span}(L)$, which for a connected graph only happens if $x\perp\mathbf 1$. So we want $p(L)L=\Pi$, the projection that kills constant vectors and is the identity on vectors orthogonal to them; $\Pi=\frac1nL_{K_n}$. A polynomial $\epsilon$-approximates the pseudoinverse if $\|p(L)L-\Pi\|\le\epsilon$.

### 35.6 Bounds on the diameter (pp. 285–286)
If $s,t$ are at distance greater than $d$, then $\chi_s^TL^d\chi_t=0$. If $L$ has $k$ distinct eigenvalues other than 0, there is a degree-$(k-1)$ polynomial $p$ with $Lp(L)=\Pi$ (p. 285).

**Theorem 35.6.1.** If $G$ is connected and $L$ has at most $k$ distinct nonzero eigenvalues, then $\mathrm{diam}(G)\le k$.
*Proof (p. 286).* Let $s,t$ be at distance $d=\mathrm{diam}$. Then $e_s^T\Pi e_t=-1/n$. The polynomial $Lp(L)=\Pi$ has zero constant term and degree $k$. If its degree were less than $d$, then $e_s^TLp(L)e_t=0\ne-1/n$. So $d\le k$.

*Approximate version (p. 286).* If $\|p(L)L-\Pi\|\le\epsilon$, then $e_s^T(p(L)L-\Pi)e_t\le\|e_s\|\,\|p(L)L-\Pi\|\,\|e_t\|\le\epsilon$. If $p(L)L$ has degree less than $d$, then $e_s^T(p(L)L-\Pi)e_t=e_s^T(-\Pi)e_t=1/n$. This is a contradiction when $\epsilon<1/n$.

**Theorem 35.6.2 (Chung–Faber–Manteuffel [CFM94]).** For connected $G$ with Laplacian eigenvalues $\lambda_2\le\dots\le\lambda_n$:
$$\mathrm{diam}(G)\le\Big(\tfrac12\sqrt{\lambda_n/\lambda_2}+1\Big)\ln 2n.$$
The author says this follows from the polynomials built from Chebyshev polynomials (p. 286).

*Intuition note.* A polynomial of degree $d$ in $L$ only links vertices within $d$ steps. So a polynomial in $L$ that equals $\Pi$ (or approximates it to error below $1/n$) must have degree at least the distance between any two vertices; this is why a fast polynomial solver implies small diameter (pp. 285–286).

## Toy example (ours)
Take $A=\mathrm{diag}(1,4)$ and $b=(1,1)^T$, so $x=A^{-1}b=(1,\tfrac14)$. There are $k=2$ distinct eigenvalues, so one iteration should suffice.
- $p_0=b=(1,1)$. $Ap_0=(1,4)$. $p_0^TAp_0=1+4=5$. $(Ap_0)^TAp_0=1+16=17$.
- $p_1=Ap_0-\tfrac{17}{5}p_0=(1-3.4,\,4-3.4)=(-2.4,\,0.6)$.
- Check: $Ap_1=(-2.4,2.4)$, so $p_0^TAp_1=-2.4+2.4=0$.
- $c_0=b^Tp_0/p_0^TAp_0=2/5$. $b^Tp_1=-1.8$. $p_1^TAp_1=5.76+4(0.36)=7.2$, so $c_1=-0.25$.
- $x_1=0.4(1,1)-0.25(-2.4,0.6)=(0.4+0.6,\ 0.4-0.15)=(1,0.25)=x$. ✓

Diameter check of Thm 35.6.1: the path on 3 vertices has Laplacian eigenvalues $0,1,3$, so $k=2$, and its diameter is 2 $\le2$.

## Concepts
- [[krylov-subspace-methods]] — iterates lie in span$\{b,Ab,\dots,A^tb\}$; CG picks the A-norm-best vector there (p. 282)
- [[matrix-norm-a-norm]] (new) — $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$, error measure for solvers (p. 280)
- [[loewner-order]] (new) — $X\preceq Y$ used to express $\epsilon$-approximation of $A^{-1}$ (p. 281)
- [[a-orthogonality]] (new) — $p_i^TAp_j=0$ for $i\ne j$; decouples the minimization (p. 282)
- [[conjugate-gradient]] (new) — builds an A-orthogonal basis by a three-term recurrence and minimizes A-norm error (p. 283)
- [[pseudoinverse]] — for a Laplacian, we want a polynomial in $L$ approximating it; exact solving would need $p(L)L=\Pi$ (p. 285)
- [[graph-laplacian]] — $L$; it sends constant vectors to zero, so it has no inverse (p. 285)
- [[graph-diameter]] (new) — largest distance between two vertices; bounded via eigenvalue counts (p. 285)
- [[power-iteration]] — applied to an approximate inverse for the smallest eigenvalue (p. 281)
- [[rayleigh-quotient]] — measures quality of the approximate eigenvector (p. 281)
- [[fiedler-vector]] — approximated via $Z$ (p. 281)
- [[chebyshev-iteration]] (new) — polynomial solver that CG matches or beats in A-norm (p. 284)

## Canonical instances
- [[hypercube-graph]] — $\log_2 n$ distinct eigenvalues, so CG needs only $\log_2 n$ iterations (p. 284)
- [[complete-graph-laplacian]] — $\Pi=\frac1nL_{K_n}$ (p. 285)

## Bridges (candidates)
- [structural-analogy] CG's A-orthogonal basis ↔ linear-algebra: Lanczos-type bases for Krylov subspaces — both build a basis of a Krylov subspace by a short recurrence.
- [structural-analogy] Diameter ≤ number of distinct eigenvalues ↔ network science: spectral gap and mixing speed — fast spectral convergence forces short paths.
- [structural-analogy] Decoupling by A-orthogonality ↔ PCA: diagonalizing a covariance matrix — a good basis removes cross terms.

## Questions this raises
- How does the CG error decrease when eigenvalues cluster, rather than being exactly $k$ distinct values (the next lecture, p. 285)?
- Why does finite-precision arithmetic break the "exactly $k-1$ iterations" claim (p. 284)?
- How are the Chebyshev-based polynomials turned into the $\ln 2n$ bound (p. 286)?
- How tight is Theorem 35.6.1? Which graphs have diameter exactly $k$?

## Reading notes
- Printed = pdf − 24 (pdf 304 = p. 280).
- Typos in the source: "Richardon" (p. 280); "the exploit" (p. 285). References "problem [?]" are unresolved (p. 281).
- Notation switches from $\chi_s$ (p. 285) to $e_s$ (p. 286) for the same indicator vectors.
- The inequality $e_s^T(p(L)L-\Pi)e_t\le\epsilon$ (p. 286) is written without absolute value.
- The text says "Lecture 8" for the pseudoinverse (p. 285), although this is a chapter.
- The $k-1$ iteration claim (p. 284) is stated without the step from $q$ to the Krylov subspace. The Chebyshev construction behind Thm 35.6.2 is not in these pages.
