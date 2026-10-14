---
id: spielman-2025-sagt/ch34-iterative
work: spielman-2025-sagt
unit: Chapter 34 — Iterative solvers for linear equations
pages: 272-279
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Iterative solvers for linear equations

## L0 — One line
Solving $Ax=b$ by repeated multiplication by $A$ costs a number of steps governed by the condition number $\kappa=\lambda_{\max}/\lambda_{\min}$. For Richardson iteration, about $\kappa\ln(1/\epsilon)$ steps are shown to suffice; Chebyshev polynomials give a guarantee of about $\sqrt\kappa\,\ln(1/\epsilon)$ steps.

## L1 — The gist (≤ 120 words)
Direct methods such as elimination are wasteful for sparse matrices. Iterative methods use only multiplications by $A$ and a few vector operations. The chapter assumes $A$ is symmetric and positive (semi)definite. Richardson iteration converges at a rate set by the eigenvalues of $A$, and about $\kappa\ln(1/\epsilon)$ steps suffice for relative error $\epsilon$. Reading the iterate as a polynomial in $A$ applied to $b$ turns the problem into polynomial design. Chebyshev polynomials give degree about $\sqrt\kappa\,\ln(1/\epsilon)$, a quadratic improvement. For the path-graph Laplacian (a matrix built from a graph), an argument indicates one cannot do much better than $\sqrt\kappa$; expander graphs are easy. The naive polynomial implementation fails in floating-point arithmetic.

**Prerequisites:** symmetric matrices and eigenvalues; matrix and operator norms; positive definiteness; Laplacian nullspace; $\cos$/$\cosh$ and complex exponentials.

## L2 — Key ideas
- Iterative solvers use only products with $A$. They approach the solution gradually, and for symmetric $A$ their running time is determined by eigenvalues (p. 272).
- Richardson iteration $x^t=(I-\alpha A)x^{t-1}+\alpha b$ has $x$ as a fixed point. It converges when $\|I-\alpha A\|<1$ (p. 273).
- The step $\alpha=2/(\lambda_n+\lambda_1)$ minimises $\|I-\alpha A\|$. About $(\lambda_n/2\lambda_1+1/2)\ln(1/\epsilon)$ iterations suffice for relative error $\epsilon$ (pp. 273–274).
- The iterate is $x^t=p_t(A)b$, a truncated series for $A^{-1}$. Accuracy $\epsilon$ is equivalent to $\|Ap_t(A)-I\|\le\epsilon$ (pp. 275–276).
- It therefore suffices to find a polynomial $q$ with $q(0)=1$ that is small on $[\lambda_{\min},\lambda_{\max}]$. Rescaled Chebyshev polynomials achieve $\epsilon\le 2(1+2/\sqrt\kappa)^{-t}$ (pp. 276–279).
- For Laplacians, work orthogonal to the all-1s vector, so $\lambda_2$ replaces $\lambda_1$. Expanders are easy; for the path-graph Laplacian an argument indicates one cannot do much better than $\sqrt\kappa$ (pp. 274, 279).
- The naive polynomial form of Chebyshev fails in double precision, e.g. on random positive definite matrices in 60 dimensions (p. 279).

## L3 — Walkthrough

**34.1 Why iterative methods (p. 272).** Direct methods (Gaussian elimination, inverse, LU) can be slow. Writing down the inverse takes $O(n^2)$ space and naive inversion $O(n^3)$ time, which is wasteful if $A$ has $O(n)$ non-zeros. Iterative methods only multiply by $A$ and do vector operations, and they give approximate solutions. Assume $A$ is positive (semi)definite.

**34.2 First-order Richardson iteration (pp. 273–274).** If $Ax=b$ then $\alpha Ax=\alpha b$, so $x=(I-\alpha A)x+\alpha b$. This gives
$$x^t=(I-\alpha A)x^{t-1}+\alpha b,\quad x^0=0.\tag{34.1}$$
(p. 273)

$A$ is symmetric, so $\|I-\alpha A\|=\max_i|1-\alpha\lambda_i|$, with $0<\lambda_1\le\dots\le\lambda_n$ (p. 273). This is minimized at $\alpha=2/(\lambda_n+\lambda_1)$. The extreme eigenvalues of $I-\alpha A$ are then $\pm\frac{\lambda_n-\lambda_1}{\lambda_n+\lambda_1}$, and the norm is $1-\frac{2\lambda_1}{\lambda_n+\lambda_1}$ (p. 273). For any $\alpha<2/(\lambda_n+\lambda_1)$ the norm is at most $1-\alpha\lambda_1$ (p. 273).

Error: $x-x^t=(I-\alpha A)(x-x^{t-1})$, so $x-x^t=(I-\alpha A)^tx$ (p. 274). Then
$$\|x-x^t\|\le\|I-\alpha A\|^t\|x\|\le\Big(1-\tfrac{2\lambda_1}{\lambda_n+\lambda_1}\Big)^t\|x\|\le e^{-2\lambda_1t/(\lambda_n+\lambda_1)}\|x\|.$$
(p. 274)

To get $\|x-x^t\|/\|x\|\le\epsilon$ it suffices to run $\frac{\lambda_n+\lambda_1}{2\lambda_1}\ln(1/\epsilon)=\big(\frac{\lambda_n}{2\lambda_1}+\frac12\big)\ln(1/\epsilon)$ iterations (p. 274). The ratio $\lambda_n/\lambda_1$ is the condition number $\kappa(A)$ for symmetric $A$. For general matrices it is the ratio of largest to smallest singular value (p. 274, footnote).

*Intuition note:* Each step multiplies the error by a matrix whose eigenvalues are $1-\alpha\lambda_i$. For $\alpha\le 2/(\lambda_n+\lambda_1)$ the direction with the smallest eigenvalue $\lambda_1$ shrinks slowest (factor at most $1-\alpha\lambda_1$), and the allowed $\alpha$ is limited by $\lambda_n$, so the ratio $\lambda_n/\lambda_1$ sets the number of steps.

**34.3 Expanders (p. 274).** A Laplacian is singular, with nullspace spanned by the constant vectors. Orthogonal to them the effective smallest eigenvalue is $\lambda_2$. For an $\epsilon$-expander the condition number $\lambda_n/\lambda_2$ is approximately $1+2\epsilon$, so these systems are solved very quickly. The reason: the Laplacian of an expander approximates that of a complete graph, which acts as a multiple of the identity orthogonal to constants. Gaussian elimination on expanders takes $\Omega(n^3)$ time and $\Omega(n^2)$ space [LRT79] (p. 274).

**34.4 Residual (p. 275).** The error $\|x-x^t\|$ is awkward because $x$ is unknown. Instead, $b-Ax^t=A(I-\alpha A)^tx=(I-\alpha A)^tAx=(I-\alpha A)^tb$. So with the right $\alpha$, $\|b-Ax^t\|/\|b\|\le e^{-2\lambda_1t/(\lambda_n+\lambda_1)}$ (p. 275).

**34.5 Polynomial view (pp. 275–276).** The iterate has the form $x^t=p_t(A)b$ with $p_t$ a polynomial of degree $t$. Unrolling (34.1): $x^1=\alpha b$, $x^2=(I-\alpha A)\alpha b+\alpha b$, $x^3=(I-\alpha A)^2\alpha b+(I-\alpha A)\alpha b+\alpha b$, and in general $x^t=\sum_i(I-\alpha A)^i\alpha b$ (p. 275). If the infinite sum converges,
$$\alpha\sum_{i=0}^\infty(I-\alpha A)^i=\alpha\big(I-(I-\alpha A)\big)^{-1}=\alpha(\alpha A)^{-1}=A^{-1}.$$
So Richardson truncates this series (p. 275).

Since $b=Ax$, $\|p_t(A)b-x\|\le\epsilon\|x\|$ is equivalent to $\|p_t(A)Ax-x\|\le\epsilon\|x\|$. This is equivalent to $\|Ap_t(A)-I\|\le\epsilon$ (p. 276).

**34.6 Better polynomials (p. 276).** $A$, $p_t(A)$ and $I$ commute, so $Ap_t(A)-I$ is symmetric and its norm is its largest absolute eigenvalue. It suffices that $|\lambda_ip_t(\lambda_i)-1|\le\epsilon$ for all eigenvalues. Define $q_t(x)=1-xp(x)$. It then suffices that $q_t$ has degree $t+1$, $q_t(0)=1$, and $|q_t(x)|\le\epsilon$ on $[\lambda_1,\lambda_n]$ (p. 276). The author says polynomials of degree $\ln(2/\epsilon)(\sqrt{\lambda_n/\lambda_1}+1)/2$ exist, a quadratic improvement in $\kappa$ over Richardson (p. 276).

**Theorem 34.6.1.** For every $t\ge1$ and $0<\lambda_{\min}\le\lambda_{\max}$ there is a polynomial $q_t$ with $q_t(0)=1$ and $|q_t(x)|\le\epsilon$ for $\lambda_{\min}\le x\le\lambda_{\max}$, where
$$\epsilon\le2(1+2/\sqrt\kappa)^{-t}\le2e^{-2t/\sqrt\kappa},\qquad\kappa=\lambda_{\max}/\lambda_{\min}.$$
(p. 276)

**34.7 Chebyshev polynomials (pp. 277–278).** They are as small as possible on $[-1,1]$ and grow quickly outside (p. 277). Definition: $T_0=1$, $T_1=x$, and $T_t(x)=2xT_{t-1}(x)-T_{t-2}(x)$ for $t\ge2$. Equivalently $\cos(t\theta)=T_t(\cos\theta)$ and $\cosh(t\theta)=T_t(\cosh\theta)$ (p. 277).

Check of the recurrence (p. 277): with $2x=e^\theta+e^{-\theta}$ the author expands $2xT_{t-1}-T_{t-2}=\frac12(e^\theta+e^{-\theta})(e^{(t-1)\theta}+e^{-(t-1)\theta})-\frac12(e^{(t-2)\theta}+e^{-(t-2)\theta})$. This equals $\frac12(e^{t\theta}+e^{-t\theta})+\frac12(e^{(t-2)\theta}+e^{-(t-2)\theta})-\frac12(e^{(t-2)\theta}+e^{-(t-2)\theta})$. The last two terms cancel, leaving $\frac12(e^{t\theta}+e^{-t\theta})$. (The printed first line reads $2T_{t-1}(x)$ with the factor $x$ missing, and it uses real exponentials although it says $x=\cos\theta$.)

Hence $T_t(x)=\cos(t\,\mathrm{acos}\,x)$ for $|x|\le1$ and $T_t(x)=\cosh(t\,\mathrm{acosh}\,x)$ for $x\ge1$, with $\mathrm{acosh}(x)=\ln(x+\sqrt{x^2-1})$ for $x\ge1$ (p. 277).

**Claim 34.7.1.** $|T_t(x)|\le1$ on $[-1,1]$: write $x=\cos\theta$, so $T_t(x)=\cos(t\theta)$ (p. 277).

**Claim 34.7.2.** For $\gamma>0$, $T_t(1+\gamma)\ge(1+\sqrt{2\gamma})^t/2$. Proof, with $x=1+\gamma$ (p. 278):
$$T_t(x)=\tfrac12\big(e^{t\,\mathrm{acosh}x}+e^{-t\,\mathrm{acosh}x}\big)\ge\tfrac12e^{t\,\mathrm{acosh}x}=\tfrac12\big(x+\sqrt{x^2-1}\big)^t=\tfrac12\big(1+\gamma+\sqrt{2\gamma+\gamma^2}\big)^t\ge\tfrac12(1+\sqrt{2\gamma})^t.$$

*Intuition note:* On $[-1,1]$ a Chebyshev polynomial is a cosine, so it oscillates between $-1$ and $1$. Just outside, it grows exponentially in $t$. That is exactly what we want: small on the eigenvalue interval, large (then normalized to 1) at 0.

**34.8 Proof of Theorem 34.6.1 (pp. 278–279).** Properties used: degree $t$; $T_t\in[-1,1]$ on $[-1,1]$; $T_t$ increasing for $x\ge1$; $T_t(1+\gamma)\ge(1+\sqrt{2\gamma})^t/2$ (p. 278). Map $[\lambda_{\min},\lambda_{\max}]$ to $[-1,1]$ by $l(x)=\frac{\lambda_{\max}+\lambda_{\min}-2x}{\lambda_{\max}-\lambda_{\min}}$. Then $l(\lambda_{\max})=-1$, $l(\lambda_{\min})=1$, and $l(0)=\frac{\lambda_{\max}+\lambda_{\min}}{\lambda_{\max}-\lambda_{\min}}$ (p. 278). Set $q_t(x)=T_t(l(x))/T_t(l(0))$, so $q_t(0)=1$ (p. 278).

On the interval $|T_t(l(x))|\le1$. The author states $l(0)\ge1+2/\kappa$ (p. 279). (added step: $l(0)=1+\frac{2\lambda_{\min}}{\lambda_{\max}-\lambda_{\min}}\ge1+2/\kappa$.) (added step: $\gamma=2/\kappa$ gives $\sqrt{2\gamma}=2/\sqrt\kappa$.) By properties 3 and 4, $T_t(l(0))\ge(1+2/\sqrt\kappa)^t/2$. So $|q_t(x)|\le2(1+2/\sqrt\kappa)^{-t}$ on the interval, and all eigenvalues of $q(A)$ have absolute value at most this (p. 279).

**34.9 Laplacian systems (p. 279).** The techniques apply unchanged if $b$ is in the span of $L$, i.e. $b$ is orthogonal to the all-1s vector and the graph is connected. Then $\lambda_1=0$ plays no role and $\lambda_2$ replaces it. Lower-bound argument for the path graph: $(Lx)(i)$ depends only on $x(i-1),x(i),x(i+1)$. So with a polynomial of degree at most $t$, $x^t(i)$ depends only on $b(j)$ with $i-t\le j\le i+t$. Hence degree of order $n$ is needed. Also $\sqrt{\lambda_n/\lambda_2}$ is of order $n$. So one should not expect a degree significantly below $\sqrt{\lambda_n/\lambda_2}$ (p. 279).

**34.10 Warning (p. 279).** The polynomial approach works only in infinite precision. In double precision it fails on random positive definite matrices in 60 dimensions. Textbook algorithms are mathematically identical in infinite precision but are implemented more carefully (p. 279).

## Toy example (ours)
Let $A=\mathrm{diag}(1,3)$, $b=(1,3)$, so $x=(1,1)$, $\lambda_1=1$, $\lambda_n=3$, $\kappa=3$.

*Richardson:* $\alpha=2/(3+1)=1/2$, $I-\alpha A=\mathrm{diag}(1/2,-1/2)$, $\alpha b=(0.5,1.5)$.
- $x^1=(0.5,1.5)$.
- $x^2=(0.25,-0.75)+(0.5,1.5)=(0.75,0.75)$.

The error is $(0.25,0.25)$ after two steps. The norm bound is $1-2\cdot1/4=1/2$ per step, and the error indeed halves each step: $(0.5,-0.5)\to(0.25,0.25)$.

*Chebyshev, $t=2$:* $l(x)=(4-2x)/2=2-x$, $l(0)=2$, $T_2(y)=2y^2-1$, $T_2(2)=7$. So $q_2(x)=(2(2-x)^2-1)/7$. At $x=1$: $(2-1)/7=1/7$; at $x=3$: $(2-1)/7=1/7$. Maximum error $1/7\approx0.143$, against $(1/2)^2=0.25$ for Richardson, whose polynomial is $(1-x/2)^2$ (added step: this is $1-xp_2(x)$ for Richardson).

## Concepts
- [[condition number]] — $\lambda_n/\lambda_1$ for symmetric $A$; ratio of extreme singular values in general; sets iteration counts (p. 274)
- [[richardson-iteration]] (new) — $x^t=(I-\alpha A)x^{t-1}+\alpha b$, with $x$ as fixed point (p. 273)
- [[polynomial-approximation-of-inverse]] (new) — $x^t=p_t(A)b$; $p_t(A)\approx A^{-1}$ when $\|Ap_t(A)-I\|$ is small (p. 275)
- [[chebyshev-polynomials]] (new) — $T_t$ with $T_t(\cos\theta)=\cos t\theta$; minimal on $[-1,1]$, rapid growth outside (p. 277)
- [[graph Laplacian]] — singular; solve orthogonal to the all-1s vector, so $\lambda_2$ plays the role of $\lambda_1$ (p. 279)
- [[numerical stability]] — the naive polynomial form of Chebyshev is unstable in finite precision (p. 279)

## Canonical instances
- [[path-graph-laplacian]] — locality of $L$ forces degree of order $n$ (p. 279)
- [[expander-laplacian-solve]] — condition number about $1+2\epsilon$; fast iterative solve versus $\Omega(n^3)$ elimination (p. 274)

## Bridges (candidates)
- [structural-analogy] Richardson convergence ↔ random walks on graphs: both are analysed through powers of a matrix with norm below 1 (the author notes the analogy to Chapter 10, p. 273)
- [same-math] truncated series $\alpha\sum(I-\alpha A)^i$ ↔ Neumann/geometric series for $(I-M)^{-1}$ — the same series as written on p. 275
- [structural-analogy] Chebyshev acceleration ↔ Krylov methods (Conjugate Gradient, announced for the next chapter): both are polynomial-in-$A$ solvers

## Questions this raises
- Why does Conjugate Gradient need no knowledge of $\lambda_{\min},\lambda_{\max}$, while Chebyshev needs them for the interval map $l$?
- Which finite-precision implementation makes Chebyshev stable, and why does the naive form fail so early (60 dimensions)?
- Can $\sqrt\kappa$ be beaten for matrices other than path Laplacians?

## Reading notes
- Printed page = pdf − 24 (pdf 296 = printed 272).
- Theorem 34.6.1 item 1 prints "$\lambda_{\min}\le x\le\lambda_{\min}$"; this is evidently a typo for $\lambda_{\max}$.
- In 34.5 the sum for $x^t$ is printed with upper limit $t$, but the listed $x^1,x^2,x^3$ imply upper limit $t-1$.
- In 34.6, $p_t$ has degree $t$ and $q_t=1-xp$ has degree $t+1$, yet 34.8 builds a degree-$t$ $q_t$. The source is loose about indexing.
- The second inequality in Theorem 34.6.1, $2(1+2/\sqrt\kappa)^{-t}\le2e^{-2t/\sqrt\kappa}$, appears to point the wrong way: $\ln(1+y)\le y$. Not corrected in the source.
- 34.9 refers to "the end of the last section" for the $\sqrt\kappa$ bound; this presumably means the bound proved at the end of 34.8.
- The unit metadata describe the source as an incomplete draft dated April 2, 2025; this is not visible on pages 272–279.
