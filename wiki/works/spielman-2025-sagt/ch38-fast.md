---
id: spielman-2025-sagt/ch38-fast
work: spielman-2025-sagt
unit: "Chapter 38 — Fast Laplacian Solvers by Sparsification"
pages: 300–306
fields: [linear-algebra]
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
# Fast Laplacian Solvers by Sparsification

## L0 — One line
Writing $(I-B)^{-1}$ in a symmetric squaring form lets us recurse, and sparsifying at each level keeps matrices sparse, so Laplacian and M-matrix systems can be solved in nearly linear time (in a sketch that assumes good sparsifiers exist).

## L1 — The gist (≤ 120 words)
The chapter asks how to solve $Mx=b$ for Laplacians and their M-matrix submatrices in nearly linear time. The answer is a recursive chain of matrices. Each matrix in the chain has its eigenvalue bound squared compared with the previous one, so about $\log_2(1/\kappa)$ levels suffice. The squared matrices could be dense. After each squaring step we replace the result by a sparse spectral approximation. A symmetric inverse formula lets approximations be substituted level by level, and the errors add up. The result is a solver costing $O(n(\log_2(1/\kappa))^3)$ in this sketch, assuming sparsifiers exist. Efficient construction and improvements are only mentioned.

**Prerequisites:** Loewner order ($\preceq$) on symmetric matrices; Laplacians and M-matrices; geometric/Neumann series; eigenvalues of $D^{-1}A$.

## L2 — Key ideas
- Approximation is redefined as $A\approx_\epsilon B \iff e^{-\epsilon}A\preceq B\preceq e^{\epsilon}A$, so the errors of chained approximations add (p. 300).
- It suffices to solve in $I-B$ with $B=D^{-1/2}AD^{-1/2}$, whose eigenvalues have absolute value $<1$ (p. 301).
- The product form $\prod (I+B^{2^j})$ needs only $O(\log\kappa^{-1})$ factors for a good approximation. But its factors are probably dense, and approximation is not preserved by products (p. 302).
- In the symmetric identity (38.3) only the middle inverse $(I-B^2)^{-1}$ needs approximating; the author says one can show that $M_1\approx_\epsilon I-B^2$ then gives an $\epsilon$-approximation of $(I-B)^{-1}$ (p. 302).
- $(\alpha,\beta)$-pairs measure progress; squaring maps an $(\alpha,\alpha)$-pair to an $(\alpha^2,0)$-pair (pp. 303–304).
- Sparsification degrades the pair only mildly (Lemma 38.5.4), so every level can stay sparse (p. 304).
- Setting $\epsilon\approx 1/\log_2\kappa^{-1}$ keeps total error constant; the cost is $O(n(\log_2 1/\kappa)^3)$ (p. 306).

## L3 — Walkthrough

**38.1–38.2 Overview and approximation.** Target time is $O(m\log^c(n\kappa^{-1})\log\epsilon^{-1})$, from [PS14] (p. 300). Here $A\approx_\epsilon B$ means $e^{-\epsilon}A\preceq B\preceq e^{\epsilon}A$. It is symmetric, and $e^\epsilon\approx 1+\epsilon$ for small $\epsilon$. Also $A\approx_\alpha B,\ B\approx_\beta C\Rightarrow A\approx_{\alpha+\beta}C$ (p. 300).

**38.3 The idea.** An (symmetric) M-matrix has $M=L+X$, with $L$ a Laplacian and $X$ a nonzero nonnegative diagonal matrix. A symmetric M-matrix is also defined directly as a matrix with nonpositive off-diagonals and $M\mathbf 1\ge0$, $M\mathbf 1\ne 0$; the source says every M-matrix can be written as $X+L$. Submatrices of $L_G$ on $S$ with $G(S)$ connected are examples. Solving in Laplacians and in symmetric M-matrices is algorithmically equivalent (p. 301). If $\widehat L\approx_\epsilon L$, then $X+\widehat L\approx_\epsilon X+L$ (the author calls this easy) (p. 301).

Write $M=D-A$, $D$ positive diagonal, $A\ge0$. By Lemma 7.3.1 ($X$ has a nonzero entry and $L$ is connected) $M$ is nonsingular; nonsingular and PSD give $D-A\succ0$, which is the same as $D\succ A$ (38.1). Perron–Frobenius gives $D\succ -A$ (38.2). With $B=D^{-1/2}AD^{-1/2}$, $M$ becomes $I-B$ after scaling. Then (38.1)–(38.2) imply all eigenvalues of $B$ have absolute value $<1$ (p. 301).

The series $(I-B)^{-1}=\sum B^i$ needs at least $1/\kappa$ terms if the top eigenvalue is $1-\kappa$. The product form $\sum_i B^i=\prod (I+B^{2^j})$ has few terms. For example, $(I+B)(I+B^2)(I+B^4)=(I+B+B^2+B^3)(I+B^4)$ (p. 301–302). About $O(\log\kappa^{-1})$ factors suffice. But the factors are probably dense. Sparsifying them separately fails: $A\approx_\epsilon\widehat A$ and $B\approx_\epsilon\widehat B$ need not make $\widehat A\widehat B$ a good approximation of $AB$: it could be a very poor one, and the product is not necessarily symmetric, so approximation is not even defined for it (p. 302).

*Intuition note.* The product form needs only $O(\log\kappa^{-1})$ factors, compared with at least $1/\kappa$ terms in the sum. The trouble is that approximating the factors one by one need not give a good approximation of the product.

**38.4 A symmetric expansion.** From $(I-B)(I+B)=I-B^2$ we get $(I-B)^{-1}=(I+B)(I-B^2)^{-1}$. Repeating gives $(I+B)(I+B^2)(I-B^4)^{-1}$ (p. 302). The symmetric version is
$$(I-B)^{-1}=\tfrac12 I+\tfrac12 (I+B)(I-B^2)^{-1}(I+B).\tag{38.3}$$
Check (multiply by $I-B$): $(I+B)(I-B^2)^{-1}(I+B)(I-B)=(I+B)(I-B^2)^{-1}(I-B^2)=I+B$. Hence $\tfrac12[I+(I+B)(I-B^2)^{-1}(I+B)](I-B)=\tfrac12[(I-B)+(I+B)]=I$ (p. 302).

If $M_1\approx_\epsilon I-B^2$, then $(I-B)^{-1}\approx_\epsilon\tfrac12[I+(I+B)M_1^{-1}(I+B)]$ (the author says "you can show"). $M_1$ is built recursively (p. 302).

*Intuition note.* Only the middle inverse is replaced by an approximation, and it is flanked by $(I+B)$ on both sides. The author states, without proof, that the result is again an $\epsilon$-approximation.

**38.5 $D$ and $A$.** The analog of (38.3) is
$$(D-A)^{-1}=\tfrac12\left[D^{-1}+(I+D^{-1}A)(D-AD^{-1}A)^{-1}(I+AD^{-1})\right].\tag{38.4}$$
*Lemma 38.5.1.* If $D-A$ is an M-matrix, so is $M_1=D-AD^{-1}A$. Proof: off-diagonals are symmetric and nonpositive. With $d=D\mathbf 1$, $a=A\mathbf 1$: $(D-AD^{-1}A)\mathbf 1=d-AD^{-1}a\ge d-A\mathbf 1=d-a$, which is nonnegative and nonzero (p. 303).

*Definition.* $(D,A)$ is an $(\alpha,\beta)$-pair if $D$ is positive diagonal, $A\ge0$ (diagonal allowed), $\alpha D\succeq A$ and $\beta D\succeq -A$. The initial matrix gives a $(1-\kappa,1-\kappa)$-pair for some $\kappa>0$. The goal is a $(1/4,1/4)$-pair (p. 303).

*Lemma 38.5.2.* A $(1/4,1/4)$-pair gives $M\approx_{1/3}D$. Proof: $D-A\preceq\tfrac54D\le e^{1/4}D$ and $D-A\succeq\tfrac34D\ge e^{-1/3}D$ (pp. 303–304).

*Lemma 38.5.3.* An $(\alpha,\alpha)$-pair $(D,A)$ gives an $(\alpha^2,0)$-pair $(D,AD^{-1}A)$. Proof: the hypothesis says eigenvalues of $D^{-1}A$ have absolute value $\le\alpha$ (Lecture 14, Lemma 3.1). The eigenvalues of $D^{-1}AD^{-1}A$ are their squares, so lie in $[0,\alpha^2]$ (p. 304). So about $\log\kappa^{-1}+2$ squarings turn a $(1-\kappa,1-\kappa)$-pair into a $(1/4,0)$-pair (p. 304).

*Lemma 38.5.4.* Let $\epsilon\le1/3$. If (a) $(D,A)$ is a $(1-\kappa,0)$-pair, (b) $D-A\approx_\epsilon\widehat D-\widehat A$, (c) $D\approx_\epsilon\widehat D$, then $(\widehat D,\widehat A)$ is a $(1-\kappa e^{-2\epsilon},3\epsilon)$-pair (p. 304). Proof: $(1-\kappa)D\succeq A\iff D-A\succeq\kappa D$. Then $\widehat D-\widehat A\succeq e^{-\epsilon}(D-A)\succeq e^{-\epsilon}\kappa D\succeq e^{-2\epsilon}\kappa\widehat D$. Other side: $e^{2\epsilon}\widehat D\succeq e^\epsilon D\succeq e^\epsilon(D-A)\succeq\widehat D-\widehat A$. For $\epsilon\le1/3$, $3\epsilon\ge e^{2\epsilon}-1$, so $3\epsilon\widehat D\succeq(e^{2\epsilon}-1)\widehat D\succeq-\widehat A$ (p. 304).

*Sparsification meets the lemma (p. 305).* Let $C$ be the diagonal of $A$, $L$ the Laplacian of the graph with adjacency $A-C$, and $X+L=D-A$. Take a sparse $\epsilon$-approximation $\widetilde L=\widetilde D-\widetilde A$ ($\widetilde A$ zero diagonal). The diagonals of $L,\widetilde L$ approximate each other. Set $\widehat D=\widetilde D+C$, $\widehat A=\widetilde A+C$; "you can now check" the lemma's requirements. Diagonals are kept because removing $C$ would make $\beta$ worse (p. 305).

**38.6 Sketch of the construction.** Start with $(D_0,A_0)$, a $(1-\kappa_0,1-\kappa_0)$-pair. $D_0-A_0D_0^{-1}A_0$ is an M-matrix and $(D_0,A_0D_0^{-1}A_0)$ is a $((1-\kappa_0)^2,0)$-pair. Define $1-\kappa_1=(1-\kappa_0)^2$ ($\kappa_1\approx2\kappa_0$). Lemma 38.5.4 gives a $(1-\kappa_1e^{-2\epsilon},3\epsilon)$-pair $(D_1,A_1)$ with $D_1-A_1\approx_\epsilon D_0-A_0D_0^{-1}A_0$ and $A_1$ having $O(n/\epsilon^2)$ nonzeros. Inductively, $M_i=D_i-A_i$ has $O(n/\epsilon^2)$ nonzeros and $M_i\approx_\epsilon D_i-A_{i-1}D_{i-1}^{-1}A_{i-1}$. For $k=2+\log_2 1/\kappa$ and $\epsilon$ near zero, $(D_k,A_k)$ is a $(1/4,1/4)$-pair (p. 305).

Applying (38.4) at each level gives $(D_i-A_i)^{-1}=\tfrac12D_i^{-1}+\tfrac12(I+D_i^{-1}A_i)(D_i-A_iD_i^{-1}A_i)^{-1}(I+A_iD_i^{-1})\approx_\epsilon\tfrac12D_i^{-1}+\tfrac12(I+D_i^{-1}A_i)(D_{i+1}-A_{i+1})^{-1}(I+A_iD_i^{-1})$ for $0\le i<k$ (p. 305). At the end, $(D_k-A_k)^{-1}\approx_{1/3}D_k^{-1}$ (p. 306). Substituting through gives accuracy $1/3+k\epsilon$. Setting $k\epsilon=1/3$, the page then writes $\epsilon=1/(2+\log_2\kappa^{-1})$ (p. 306; see Reading notes for the factor-3 mismatch). The dominant cost is multiplying vectors by $2k$ matrices with $O(n/\epsilon^2)$ entries: $O(n(\log_2(1/\kappa))^3)$ (p. 306).

*Intuition note.* Each level squares the eigenvalue bound, and sparsification changes the pair parameters only slightly (a factor $e^{-2\epsilon}$ on $\kappa$, and a $3\epsilon$ term). About $\log(1/\kappa)$ levels with error $\epsilon\sim1/\log$ each give constant total error.

**38.7 Efficiency.** The sketch assumed sparsifiers exist. Building them fast needs (1) quick approximation of effective resistances for the sampling algorithm of Lecture 17, and (2) not forming $AD^{-1}A$ before sparsifying it, since that could take too long. Instead, write it as a product of cliques with succinct descriptions and sum their approximations (p. 306).

**38.8 Improvements.** The fastest known solvers run in $O(m\sqrt{\log n}\log\epsilon^{-1})$ [CKM+14]. The author says this algorithm can be substantially improved by combining it with Cholesky factorization, which gives an efficient parallel algorithm. The same combination also proves existence of an approximate inverse for every M-matrix with a linear number of nonzeros [LPS15] (p. 306).

## Toy example (ours)
Scalars ($1\times1$ matrices), $D=2$, $A=1$, so $B=A/D=\tfrac12$ and $(D-A)^{-1}=1$.
- (38.3): $\tfrac12+\tfrac12\cdot\frac{(1.5)^2}{1-0.25}=\tfrac12+\tfrac12\cdot\frac{2.25}{0.75}=\tfrac12+\tfrac32=2=(1-\tfrac12)^{-1}$ ✓.
- (38.4): $\tfrac12\left[\tfrac12+1.5\cdot\frac{1}{2-0.5}\cdot1.5\right]=\tfrac12[0.5+1.5]=1$ ✓.
- Product form: $(1.5)(1.25)(1.0625)=1.9921875\approx2$ after three factors.
- Squaring: $A/D=\tfrac12\to AD^{-1}A/D=\tfrac14\to\tfrac1{16}$ (here $AD^{-1}A=0.5$; squaring again gives $0.5\cdot0.5\cdot0.5=0.125$, and $0.125/2=\tfrac1{16}$), already below $1/4$ after two squarings.

## Concepts
- [[positive (semi)definite matrix]] — the order $X\succeq Y$ means $X-Y$ is PSD; used to define $\approx_\epsilon$ (p. 300)
- [[graph Laplacian]] — $L$ in $M=L+X$ (p. 301)
- [[condition number]] — $\kappa$ is the condition number in the running time (p. 300); it also appears as the gap in the top eigenvalue $1-\kappa$ of $B$ (p. 301)
- [[Perron–Frobenius theorem]] — used to show $D\succ-A$ (p. 301)
- [[adjacency matrix]] — $A-C$ is the adjacency matrix of the graph whose Laplacian is $L$ (p. 305)
- [[eigenvector / eigenvalue]] — eigenvalues of $D^{-1}A$ control pairs (p. 304)
- [[spectral-approximation]] (new) — $A\approx_\epsilon B$: $e^{-\epsilon}A\preceq B\preceq e^\epsilon A$, errors add (p. 300)
- [[m-matrix]] (new) — symmetric, nonpositive off-diagonals, $M\mathbf 1\ge0$ and $\ne0$ (p. 301)
- [[alpha-beta-pair]] (new) — $\alpha D\succeq A$, $\beta D\succeq-A$ (p. 303)
- [[spectral-sparsification]] (new) — replacing a matrix by a sparse $\epsilon$-approximation (pp. 302, 305)

## Canonical instances
- [[squaring-chain-solver]] — recursive chain of squared, sparsified M-matrices (p. 305)
- [[symmetric-inverse-identity]] — (38.3)/(38.4) (pp. 302–303)

## Bridges (candidates)
- [structural-analogy] Repeated squaring $\prod(I+B^{2^j})$ ↔ fast exponentiation: both use $\log$ many squarings to cover $2^k$ terms.
- [structural-analogy] Chain of approximate inverses ↔ multigrid / preconditioning: each level is a cheaper matrix used inside the next.
- [structural-analogy] $B=D^{-1/2}AD^{-1/2}$ ↔ graph theory: normalized adjacency matrix — similar form, but here $D$ need not be the degree matrix and $A$ may have diagonal entries.

## Questions this raises
- Why is approximating $I-B^2$ (a product) safe, whereas approximating $B^2$'s factors separately is not?
- How are effective resistances approximated quickly enough (Lecture 17 sampling)?
- How does Cholesky combine with this chain to improve the time?

## Reading notes
- Printed = pdf − 24. The chapter carries the heading "This Chapter Needs Editing" (p. 300).
- Misprint: the product on p. 301 is shown with $j\ge1$, but the expansion that follows (starting with $I+B$) corresponds to $j\ge0$.
- Lemma 38.5.4 says "$\widehat D-\widehat A$ is a pair"; the pair is $(\widehat D,\widehat A)$.
- p. 305: $X$ is not visibly included in the definitions of $\widehat D,\widehat A$; the check is left to the reader.
- p. 306: with $k=2+\log_2\kappa^{-1}$, $k\epsilon=1/3$ would give $\epsilon=1/(3k)$, not the printed $1/(2+\log_2\kappa^{-1})$ (a factor of 3 differs).
- The long display on p. 305 is cut off at the right margin in the image; the digest completes its last factor $(I+A_iD_i^{-1})$ by analogy with (38.4).
