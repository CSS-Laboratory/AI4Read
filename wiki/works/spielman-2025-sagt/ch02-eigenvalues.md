---
id: spielman-2025-sagt/ch02-eigenvalues
work: spielman-2025-sagt
unit: "Chapter 2 — Eigenvalues and Optimization: The Courant-Fischer Theorem"
pages: 21-28
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Eigenvalues and Optimization: The Courant-Fischer Theorem

## L0 — One line
The eigenvalues of a symmetric matrix are the optimal values of the Rayleigh quotient $x^TMx/x^Tx$, and optimizing it also proves the Spectral Theorem.

## L1 — The gist (≤ 120 words)
Why do eigenvalues matter? One reason is that they arise as solutions to natural optimization problems (p. 21). The Courant-Fischer Theorem says that for a symmetric matrix $M$, the largest eigenvalue is the maximum of the Rayleigh quotient, the smallest is its minimum, and every middle eigenvalue is a max-min (or min-max) over subspaces. The chapter proves the max-min form from the Spectral Theorem and says the other form is similar. It then reverses the direction: maximizing the Rayleigh quotient yields an eigenvector, and induction gives a self-contained proof of the Spectral Theorem. For non-symmetric matrices the analogue is the singular values, characterized by $\max u^TAv$.

**Prerequisites:** orthonormal bases; gradients; subspace dimension; rank, column space and null space; the Spectral Theorem as a statement (Theorem 1.3.1, referred to on p. 26).

## L2 — Key ideas
- The Rayleigh quotient of an eigenvector equals its eigenvalue (p. 21).
- Expanding $x$ in an orthonormal eigenbasis gives $x^TMx=\sum_i c_i^2\mu_i$ (Lemma 2.1.1, p. 23).
- Courant-Fischer: $\mu_k$ is a max-min over $k$-dimensional subspaces and a min-max over $(n-k+1)$-dimensional ones. The eigenvectors attain these optima under orthogonality constraints (pp. 21–22).
- The proof of the upper bound uses a dimension count: a $k$-dimensional $S$ and an $(n-k+1)$-dimensional $T$ must meet nontrivially (p. 24).
- A maximizer of the Rayleigh quotient exists (compactness) and must be an eigenvector (zero gradient) (Theorem 2.2.1, p. 25).
- For a unit eigenvector $\psi$ with $\mu\ne0$, subtracting $\mu\psi\psi^T$ lowers the rank by one, so induction gives $M=\sum\mu_i\psi_i\psi_i^T$ (pp. 26–27).
- For non-symmetric $A$, singular values replace eigenvalues; Theorem 2.3.2 is the analogue (pp. 27–28).

## L3 — Walkthrough

**Setup (p. 21).** The Rayleigh quotient of $x$ with respect to $M$ is
$$\frac{x^TMx}{x^Tx}.\tag{2.1}$$
If $M\psi=\mu\psi$, then $\frac{\psi^TM\psi}{\psi^T\psi}=\frac{\psi^T\mu\psi}{\psi^T\psi}=\mu$ (p. 21).

**Theorem 2.0.1 (Courant-Fischer).** Let $M$ be symmetric with eigenvalues $\mu_1\ge\dots\ge\mu_n$. Then $\mu_1=\max_{x\ne0}\frac{x^TMx}{x^Tx}$ and $\mu_n=\min_{x\ne0}\frac{x^TMx}{x^Tx}$. For $k\ge1$:
$$\mu_k=\max_{\substack{S\subseteq\mathbb R^n\\ \dim S=k}}\ \min_{\substack{x\in S\\x\ne0}}\frac{x^TMx}{x^Tx}=\min_{\substack{T\subseteq\mathbb R^n\\ \dim T=n-k+1}}\ \max_{\substack{x\in T\\x\ne0}}\frac{x^TMx}{x^Tx}.$$
The eigenvectors satisfy $\psi_1\in\arg\max_{\|x\|=1}x^TMx$ and $\psi_n\in\arg\min_{\|x\|=1}x^TMx$. For $2\le k\le n$:
$$\psi_k\in\arg\min_{\|x\|=1,\ x^T\psi_j=0\ (j>k)}x^TMx\quad\text{and}\quad\psi_k\in\arg\max_{\|x\|=1,\ x^T\psi_j=0\ (j<k)}x^TMx.\tag{2.2}$$
(pp. 21–22). The text also says the maximizers of the quotient are exactly the eigenvectors of the largest eigenvalue (p. 21).

*Intuition note.* Eigenvalues sort the "stretch" of $M$ from largest to smallest. The best a $k$-dimensional subspace can guarantee in its worst direction is exactly $\mu_k$.

**2.1 First proof.**
- Expansion: with an orthonormal eigenbasis $\psi_i$, every $x$ satisfies $x=\sum_i c_i\psi_i$, $c_i=\psi_i^Tx$ (2.3). Check: $\sum_i c_i\psi_i=\sum_i\psi_i\psi_i^Tx=\Psi\Psi^Tx=x$, using $\Psi\Psi^T=I$ for orthogonal $\Psi$ (p. 22).
- **Lemma 2.1.1.** If $x=\sum_ic_i\psi_i$, then $x^TMx=\sum_ic_i^2\mu_i$. Proof: $x^TMx=(\sum_ic_i\psi_i)^T(\sum_jc_j\mu_j\psi_j)=\sum_{i,j}c_ic_j\mu_j\psi_i^T\psi_j=\sum_ic_i^2\mu_i$, since $\psi_i^T\psi_j=0$ for $i\ne j$ and $1$ for $i=j$ (pp. 22–23).
- The author verifies only the max-min identity for $\mu_k$. He says $\mu_1,\mu_n$ are special cases and the other form is "similar" (p. 23).
- *Achievability.* Let $S=\mathrm{span}(\psi_1,\dots,\psi_k)$. For $x\in S$, $\frac{x^TMx}{x^Tx}=\frac{\sum_{i\le k}\mu_ic_i^2}{\sum_{i\le k}c_i^2}\ge\frac{\mu_k\sum c_i^2}{\sum c_i^2}=\mu_k$. So $\min_{x\in S}\ge\mu_k$ (pp. 23–24).
- *Upper bound.* Let $T=\mathrm{span}(\psi_k,\dots,\psi_n)$, of dimension $n-k+1$. Every $k$-dimensional $S$ meets $T$ in dimension at least 1. So $\min_{x\in S}\le\min_{x\in S\cap T}\le\max_{x\in T}$ of the quotient. For the maximizer $x=\sum_{i\ge k}c_i\psi_i$, Lemma 2.1.1 gives quotient $\le\mu_k$ (p. 24).
- Hence the max-min equals $\mu_k$. Since $\psi_k^TM\psi_k=\mu_k$ and $T=\{x:x^T\psi_j=0,\ j<k\}$, we get the arg max statement. The arg min statement follows from $S=\{x:x^T\psi_j=0,\ j>k\}$ (p. 24).

*Intuition note.* Any $k$-dimensional subspace must contain a direction lying inside the span of the bottom $n-k+1$ eigenvectors. That direction scores at most $\mu_k$, so no subspace can beat $\mu_k$.

**2.2 Spectral Theorem by optimization.**
- **Theorem 2.2.1.** If $M$ is symmetric and $x\ne0$ maximizes the Rayleigh quotient, then $Mx=\mu_1x$. The minimum is likewise achieved by eigenvectors of the smallest eigenvalue (p. 24).
- Proof, existence: the quotient is homogeneous, so unit vectors suffice. It is continuous on the closed, compact unit sphere, so a maximum is achieved (p. 25).
- Proof, eigenvector property: the gradient must vanish at a maximum. With $\nabla x^Tx=2x$ and $\nabla x^TMx=2Mx$,
$$\nabla\frac{x^TMx}{x^Tx}=\frac{(x^Tx)(2Mx)-(x^TMx)(2x)}{(x^Tx)^2}.$$
Setting this to zero requires $(x^Tx)Mx=(x^TMx)x$, so $Mx=\frac{x^TMx}{x^Tx}x$. This holds if and only if $x$ is an eigenvector whose eigenvalue equals its Rayleigh quotient. Since $x$ maximizes the quotient, that eigenvalue is the largest of $M$ (p. 25).
- **Corollary 2.2.2.** Every non-zero symmetric $M$ has at least one eigenvector with non-zero eigenvalue. First find $x$ with $x^TMx\ne0$: take $\delta_i$ if $M(i,i)\ne0$. Otherwise take $\delta_i+\delta_j$ with $M(i,j)\ne0$, giving $x^TMx=2M(i,j)$. If $x^TMx>0$, apply Theorem 2.2.1 to $M$. If $<0$, apply it to $-M$: an eigenvector with eigenvalue $\nu>0$ of $-M$ has eigenvalue $-\nu<0$ for $M$ (p. 25).
- **Theorem 2.2.3.** A real symmetric $M$ of rank $r$ has non-zero reals $\mu_1,\dots,\mu_r$ and orthonormal $\psi_1,\dots,\psi_r$ with
$$M=\sum_{i=1}^r\mu_i\psi_i\psi_i^T.\tag{2.4}$$
Multiplying on the right by $\psi_i$ gives $M\psi_i=\mu_i\psi_i$, so it is equivalent to Theorem 1.3.1 (p. 26).
- **Theorem 2.2.4.** The span (column space) of a symmetric $M$ is orthogonal to its null space. If $Mz=0$ and $y=Mx$, then $z^Ty=z^TMx=(z^TM)x=0$ by symmetry (p. 26).
- **Lemma 2.2.5.** Let $\psi$ be a unit eigenvector of symmetric $M$ with eigenvalue $\mu\ne0$, and $\widehat M=M-\mu\psi\psi^T$. Then null$(\widehat M)$ contains span$(\psi)$ and null$(M)$, and rank$(M)$ = rank$(\widehat M)+1$.
  - If $Mx=0$, then $x\perp\psi$ (as $\psi$ is in the span of $M$), so $\widehat Mx=0-\mu\psi\psi^Tx=0$.
  - $\widehat M\psi=\mu\psi-\mu\psi(\psi^T\psi)=0$ (unit vector).
  - By Theorem 2.2.4, $\psi\perp$ span$(\widehat M)$. With $M=\widehat M+\mu\psi\psi^T$, span$(M)$ = span$(\widehat M)$ plus $\psi$, one dimension larger (p. 26).
- *Proof of Theorem 2.2.3 (induction on rank).* Rank 0 is trivial. For rank $r+1$, Corollary 2.2.2 gives $\psi,\mu\ne0$. Lemma 2.2.5 gives rank$(\widehat M)=r$, so $\widehat M=\sum_{i\le r}\mu_i\psi_i\psi_i^T$. Set $\psi_{r+1}=\psi$, $\mu_{r+1}=\mu$. Orthogonality: each $\psi_i$ ($i\le r$) lies in span$(\widehat M)$, and $\psi_{r+1}$ lies in its null space (pp. 26–27).

*Intuition note.* Find an eigenvector with non-zero eigenvalue (a maximizer of the quotient for $M$ or for $-M$). Remove its contribution and repeat on what remains. Each removal lowers the rank by one, so after $r$ steps the process yields all $r$ eigenpairs with non-zero eigenvalue.

**2.3 Singular values for asymmetric matrices.** The Rayleigh characterization works only for symmetric matrices. For other $A$, the singular values and vectors are the square roots of eigenvalues, and the eigenvectors, of $AA^T$ and $A^TA$ (p. 27).
- **Definition 2.3.1.** $A=U\Sigma V^T$, with $U,V$ having orthonormal columns and $\Sigma$ diagonal with non-negative entries (p. 27).
- For $A$ of shape $m\times n$ and $r=\min(m,n)$: $U$ is $m\times r$, $\Sigma$ is $r\times r$, $V$ is $n\times r$. Then $A=\sum_{i=1}^r\sigma_iu_iv_i^T$ and $Av_i=\sigma_iu_i$ (p. 27).
- **Theorem 2.3.2.** $\sigma_1=\max_{\|u\|=\|v\|=1}u^TAv$, and
$$\sigma_k=\max_{\dim S=k,\ \dim T=k}\ \min_{u\in S,\,v\in T,\ \|u\|=\|v\|=1}u^TAv,$$
with $S\subseteq\mathbb R^m$, $T\subseteq\mathbb R^n$. The author says the techniques are similar to those above; the proof is left as an exercise (pp. 27–28).

## Toy example (ours)
Let $M=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. Eigenpairs: $\mu_1=3$, $\psi_1=\frac1{\sqrt2}(1,1)$; $\mu_2=1$, $\psi_2=\frac1{\sqrt2}(1,-1)$.
- Take $x=(1,0)$. Then $x^TMx=2$ and $x^Tx=1$, so the quotient is $2$, between $1$ and $3$.
- Lemma 2.1.1: $c_1=c_2=1/\sqrt2$, so $\sum c_i^2\mu_i=\tfrac12\cdot3+\tfrac12\cdot1=2$ ✓.
- $k=1$: the line $S=\mathrm{span}(1,0)$ gives min $=2\le3$. The line $\mathrm{span}(\psi_1)$ gives $3$, the maximum.
- $k=2$: $S=\mathbb R^2$, so max-min is the overall minimum, $1=\mu_2$ ✓.
- Deflation: $\widehat M=M-3\psi_1\psi_1^T=\begin{pmatrix}2&1\\1&2\end{pmatrix}-\tfrac32\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}.5&-.5\\-.5&.5\end{pmatrix}=1\cdot\psi_2\psi_2^T$. It has rank 1, one less than $M$ ✓.

## Concepts
- [[rayleigh-quotient]] — $x^TMx/x^Tx$; equals $\mu$ at an eigenvector (p. 21)
- [[courant-fischer-theorem]] (new) — eigenvalues as max-min / min-max of the Rayleigh quotient over subspaces (p. 21)
- [[spectral-theorem]] — symmetric $M=\sum\mu_i\psi_i\psi_i^T$ with orthonormal $\psi_i$; proved here by optimization (p. 26)
- [[orthonormal-basis]] — eigenbasis used to expand $x$ with $c_i=\psi_i^Tx$ (p. 22)
- [[eigenvector-eigenvalue]] — $M\psi=\mu\psi$ (p. 21)
- [[null-space]] — $\{z:Mz=0\}$; orthogonal to the span (column space) of a symmetric $M$ (p. 26)
- [[rank]] — here, the dimension of the span of $M$; drops by 1 under deflation (p. 26)
- [[singular-value-decomposition]] — $A=U\Sigma V^T$, $\sigma_i\ge0$ (p. 27)
- [[deflation-by-induction]] (new) — subtract $\mu\psi\psi^T$ to lower the rank by one (p. 26)

## Canonical instances
None named in this unit.

## Bridges (candidates)
- [same-math] Rayleigh quotient maximization ↔ PCA: choosing the direction of maximal variance of a covariance matrix.
- [structural-analogy] Courant-Fischer max-min over subspaces ↔ Eckart–Young / best low-rank approximation: both rank directions by singular or eigen values.
- [same-math] Theorem 2.3.2 ↔ SVD: $\sigma_1=\max u^TAv$ is the spectral norm of $A$.

## Questions this raises
- What goes wrong in Theorem 2.2.1 if $M$ is not symmetric?
- How does the Rayleigh quotient help for the graph Laplacian, whose "quadratic form" the text mentions (p. 22)?
- The text calls the proof of the min-max form "similar" (p. 23); how exactly does it go?
- How is the proof of Theorem 2.3.2 built from the Rayleigh tools?

## Exercises worth doing
- Ex. 1 (p. 28) — prove Theorem 2.3.2 (the text says techniques similar to the Courant-Fischer proof apply, p. 27) — difficulty: hard
- Ex. 2 (p. 28) — show that every greedy sequence $x_i$ (maximizing $x^TMx$ with $x_i\perp x_j$ for $j<i$) consists of eigenvectors — difficulty: medium

## Reading notes
- Printed page = pdf − 24.
- The sentence introducing Lemma 2.1.1 calls $x^TMx$ the "Laplacian quadratic form" (p. 22), though $M$ is any symmetric matrix.
- On p. 24, "$S\cap T$ is non-empty" presumably means "contains a non-zero vector". The text says its dimension is at least 1.
- p. 27 has a typo, "Courtant-Fischer".
- Theorem 2.0.1 says "for all $k\ge1$", while eigenvalues exist only for $k\le n$.
- Footnote 2 (p. 24) says the condition $x\ne0$ is often left unwritten but always intended.
- The author proves only one of the two equalities for $\mu_k$ and the arg max part of (2.2); he says the arg min part follows from $S=\{x:x^T\psi_j=0,\ j>k\}$ (p. 24).
- Text layer and images agree on the equations I checked.
