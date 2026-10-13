---
id: axler-2024-ladr/ch02-finite
work: axler-2024-ladr
unit: "2 Finite-Dimensional Vector Spaces"
pages: 27-50
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Finite-Dimensional Vector Spaces

## L0 — One line
In a vector space that some finite list spans, all bases (independent spanning lists) have the same length, so "dimension" is well defined, and dimensions obey $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$.

## L1 — The gist (≤ 120 words)
The chapter asks how to measure the "size" of a vector space. Its answer starts from span (all linear combinations of a list) and linear independence (no redundancy). The linear dependence lemma lets you delete a redundant vector without changing the span. This gives the key inequality: an independent list is never longer than a spanning list. Hence every basis of a finite-dimensional space has the same length, called the dimension. Every spanning list contains a basis, and every independent list (in a finite-dimensional space) extends to one. A list of length $\dim V$ is a basis if it is independent, or if it spans. The chapter ends with a dimension formula for a sum of two subspaces.

**Prerequisites:** vector space axioms and subspaces; sum and direct sum of subspaces (Ch. 1, incl. the criterion 1.46 cited in the proof of 2.33); solving small linear systems.

## L2 — Key ideas (5–10 bullets)
- A linear combination is $a_1v_1+\dots+a_mv_m$. The span is the set of all of them, and it is the smallest subspace containing the list (2.4, 2.6, p. 29).
- Linear independence means the only combination equal to $0$ has all scalars $0$. Equivalently, each vector in the span has exactly one representation (p. 32).
- Linear dependence lemma: in a dependent list, some vector lies in the span of the previous ones, and deleting it leaves the span unchanged (2.19, p. 33).
- An independent list is never longer than a spanning list (2.22, p. 35). Consequences: subspaces of finite-dimensional spaces are finite-dimensional (2.25, p. 36), and any two bases have the same length (2.34, p. 44).
- A list is a basis iff every vector is written uniquely in terms of it (2.28, p. 39). Spanning lists reduce to bases (2.30, p. 40). Independent lists in a finite-dimensional space extend to bases (2.32, p. 41). Every subspace $U$ of a finite-dimensional $V$ has a complement $W$ with $V=U\oplus W$ (2.33, p. 42).
- Dimension is the length of any basis (2.35, p. 44). If $U\subseteq V$ then $\dim U\le\dim V$, and equal dimensions force $U=V$ (2.37, 2.39, p. 45).
- If a list has length $\dim V$, you need check only independence or only spanning (2.38, 2.42, pp. 45–46).
- $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$ (2.43, p. 47). It is analogous to counting elements of a union of finite sets (table, p. 48).

## L3 — Walkthrough

Standing assumptions: $\mathbf F$ denotes $\mathbf R$ or $\mathbf C$; $V$ is a vector space over $\mathbf F$ (p. 27). Chapter plan: span → independence → basis → dimension → dimension of a sum (p. 27).

### 2A Span and Linear Independence

**Lists.** Lists of vectors are usually written without surrounding parentheses, e.g. $(4,1,6),(9,5,7)$ is a list of length two in $\mathbf R^3$ (2.1, p. 28). Every list has finite length (p. 30).

**Linear combinations and span.**
- A *linear combination* of $v_1,\dots,v_m$ is a vector $a_1v_1+\dots+a_mv_m$ with $a_1,\dots,a_m\in\mathbf F$ (2.2, p. 28).
- Example 2.3: $(17,-4,2)=6(2,1,-3)+5(1,-2,4)$. But $(17,-4,5)$ is not a linear combination of $(2,1,-3),(1,-2,4)$, because the system $17=2a_1+a_2$, $-4=a_1-2a_2$, $5=-3a_1+4a_2$ has no solution (p. 28).
- *Span*: $\operatorname{span}(v_1,\dots,v_m)=\{a_1v_1+\dots+a_mv_m: a_1,\dots,a_m\in\mathbf F\}$. The span of the empty list is $\{0\}$ (2.4, p. 29). So $(17,-4,2)\in$ the span of the two vectors above and $(17,-4,5)\notin$ it (2.5, p. 29).
- **2.6 (span is the smallest containing subspace).** The span of a list in $V$ is the smallest subspace of $V$ containing all vectors of the list (p. 29). Key steps:
  - $0=0v_1+\dots+0v_m$, so $0$ is in the span.
  - Closed under addition: $(a_1v_1+\dots+a_mv_m)+(c_1v_1+\dots+c_mv_m)=(a_1+c_1)v_1+\dots+(a_m+c_m)v_m$.
  - Closed under scaling: $\lambda(a_1v_1+\dots+a_mv_m)=\lambda a_1v_1+\dots+\lambda a_mv_m$. So the span is a subspace (by 1.34).
  - Each $v_k$ is in the span (take $a_k=1$, others $0$). Any subspace containing every $v_k$ is closed under scaling and addition, so it contains the span.
- The list *spans* $V$ if its span equals $V$ (2.7, p. 29).
- Example 2.8: the list $(1,0,\dots,0),(0,1,0,\dots,0),\dots,(0,\dots,0,1)$ spans $\mathbf F^n$, since $(x_1,\dots,x_n)=x_1(1,0,\dots,0)+\dots+x_n(0,\dots,0,1)$ (p. 30).

**Finite-dimensional spaces.**
- *Finite-dimensional*: some list of vectors in the space spans it (2.9, p. 30). So $\mathbf F^n$ is finite-dimensional for every positive integer $n$ (p. 30).
- $\mathcal P(\mathbf F)$ is the set of functions $p(z)=a_0+a_1z+\dots+a_mz^m$ with coefficients in $\mathbf F$ (2.10, p. 30). It is a vector space and a subspace of $\mathbf F^{\mathbf F}$ (p. 30).
- The coefficients are uniquely determined by the polynomial (the author defers the proof to 4.8), so the degree is well defined (p. 30).
- *Degree* $m$: $p(z)=a_0+\dots+a_mz^m$ for all $z$ with $a_m\neq0$. The zero polynomial has degree $-\infty$ (2.11, p. 31).
- $\mathcal P_m(\mathbf F)$ is the set of polynomials of degree at most $m$ (2.12). Then $\mathcal P_m(\mathbf F)=\operatorname{span}(1,z,\dots,z^m)$, so it is finite-dimensional (p. 31).
- *Infinite-dimensional* means not finite-dimensional (2.13, p. 31).
- Example 2.14: $\mathcal P(\mathbf F)$ is infinite-dimensional. For any list of polynomials, let $m$ be the highest degree in it. Every polynomial in the span has degree at most $m$, so $z^{m+1}$ is not in the span. Hence no list spans (p. 31).

**Linear independence.** Motivation (pp. 31–32):
- Suppose $v=a_1v_1+\dots+a_mv_m=c_1v_1+\dots+c_mv_m$.
- Subtracting gives $0=(a_1-c_1)v_1+\dots+(a_m-c_m)v_m$.
- If the only way to write $0$ is with all scalars $0$, then each $a_k=c_k$, so the representation is unique.

*Definition 2.15 (linearly independent)* (p. 32):
- The list $v_1,\dots,v_m$ is linearly independent if $a_1v_1+\dots+a_mv_m=0$ forces $a_1=\dots=a_m=0$.
- The empty list is declared linearly independent.
- The reasoning above shows: the list is linearly independent iff each vector in its span has exactly one representation (p. 32).

Examples 2.16 (p. 32):
- (a) $(1,0,0,0),(0,1,0,0),(0,0,1,0)$ is independent in $\mathbf F^4$: if $a_1(1,0,0,0)+a_2(0,1,0,0)+a_3(0,0,1,0)=0$, then $(a_1,a_2,a_3,0)=(0,0,0,0)$, so $a_1=a_2=a_3=0$.
- (b) $1,z,\dots,z^m$ is independent in $\mathcal P(\mathbf F)$, because a polynomial that is zero for all $z$ has all coefficients $0$ (follows from 4.8).
- (c) A list of length one is independent iff its vector is not $0$.
- (d) A list of length two is independent iff neither vector is a scalar multiple of the other.

Removing vectors from an independent list leaves an independent list (p. 33).

*Definition 2.17 (linearly dependent)*: not independent. Equivalently, there exist $a_1,\dots,a_m$, not all $0$, with $a_1v_1+\dots+a_mv_m=0$ (p. 33).

Examples 2.18 (p. 33):
- $(2,3,1),(1,-1,2),(7,3,8)$ is dependent in $\mathbf F^3$: $2(2,3,1)+3(1,-1,2)+(-1)(7,3,8)=(0,0,0)$.
- $(2,3,1),(1,-1,2),(7,3,c)$ is dependent iff $c=8$ (the author says to verify).
- If some vector in a list is a linear combination of the others, the list is dependent (move that vector to the other side, where it gets coefficient $-1$).
- Every list containing $0$ is dependent.

**2.19 Linear dependence lemma.** Suppose $v_1,\dots,v_m$ is linearly dependent in $V$. Then there is $k\in\{1,\dots,m\}$ with $v_k\in\operatorname{span}(v_1,\dots,v_{k-1})$. Furthermore, if $k$ satisfies this and the $k$th term is removed, the span of the remaining list equals $\operatorname{span}(v_1,\dots,v_m)$ (p. 33). Proof (pp. 33–34):
- By dependence, there are $a_1,\dots,a_m$, not all $0$, with $a_1v_1+\dots+a_mv_m=0$.
- Let $k$ be the largest index with $a_k\ne0$. Then $v_k=-\frac{a_1}{a_k}v_1-\dots-\frac{a_{k-1}}{a_k}v_{k-1}$, so $v_k\in\operatorname{span}(v_1,\dots,v_{k-1})$.
- Now let $k$ be any index with $v_k=b_1v_1+\dots+b_{k-1}v_{k-1}$ (2.20).
- Take $u=c_1v_1+\dots+c_mv_m$ in the span. Substituting 2.20 for $v_k$ expresses $u$ using the list without $v_k$. So removing $v_k$ does not change the span.

Special case: if $k=1$, the condition means $v_1=0$, since $\operatorname{span}()=\{0\}$. The author says parts of the proof need modification then. He also says the book will not flag such trivial cases again; the reader should check them (p. 34).

*Intuition note.* If a list is redundant, some vector adds nothing beyond the earlier ones. You can throw it away and lose nothing.

Example 2.21 (p. 34): in $\mathbf R^3$ take $(1,2,3),(6,5,4),(15,16,17),(8,9,7)$. The list is dependent, so some $k$ works. To find the smallest $k$:
- $k=1$ works iff the first vector is $0$. It is not, so no.
- $k=2$ works iff $(6,5,4)=c(1,2,3)$ for some $c$. No such $c$ exists, so no.
- $k=3$ works iff $(15,16,17)=a(1,2,3)+b(6,5,4)$ is solvable. It is, with $a=3,\ b=2$. So $k=3$ is the smallest.

**2.22 Length of independent list $\le$ length of spanning list.** In a finite-dimensional vector space, every linearly independent list has length at most the length of every spanning list (p. 35). Proof: let $u_1,\dots,u_m$ be independent and $w_1,\dots,w_n$ span $V$. Show $m\le n$ via $m$ steps, each adding one $u$ and removing one $w$.
- *Step 1.* Let $B$ be $w_1,\dots,w_n$. The list $u_1,w_1,\dots,w_n$ is dependent, since $u_1$ is a combination of the $w$'s. By 2.19, some vector in it is in the span of the earlier ones. That vector is not $u_1$, since $u_1\neq0$ by independence. So a $w$ can be removed. The new list $B$ (length $n$) contains $u_1$ and remaining $w$'s and still spans $V$.
- *Step $k$ ($k=2,\dots,m$).* $B$ spans, so $u_k\in\operatorname{span}B$. Adjoin $u_k$ to $B$ just after $u_1,\dots,u_{k-1}$. The list of length $n+1$ is dependent. By 2.19 some vector is in the span of the earlier ones. It cannot be a $u$, because $u_1,\dots,u_k$ is independent. So it is a $w$, which can be removed. The new $B$ has length $n$ and still spans.
- After step $m$ all $u$'s have been added, and each step removed a $w$. So there are at least as many $w$'s as $u$'s (p. 35).

*Skip path:* carry forward only the statement 2.22; it is cited in the proofs of 2.25, 2.34 and 2.37.

*Intuition note.* A spanning list is a supply of "directions", and an independent list uses up distinct directions. You cannot use more independent directions than the supply contains.

Examples without computation (p. 36):
- 2.23: $(1,0,0),(0,1,0),(0,0,1)$ spans $\mathbf R^3$, so no list of length greater than three is independent in $\mathbf R^3$. For instance $(1,2,3),(4,5,8),(9,6,7),(-3,2,8)$ is not independent.
- 2.24: $(1,0,0,0),\dots,(0,0,0,1)$ is independent in $\mathbf R^4$, so no list of length less than four spans $\mathbf R^4$. For instance $(1,2,3,-5),(4,5,8,3),(9,6,7,-1)$ does not span.

**2.25 Finite-dimensional subspaces.** Every subspace of a finite-dimensional vector space is finite-dimensional (p. 36). The author introduces it as confirming an intuition. Proof: let $V$ be finite-dimensional and $U\subseteq V$ a subspace.
- Step 1: if $U=\{0\}$, done. Otherwise pick a nonzero $u_1\in U$.
- Step $k$: if $U=\operatorname{span}(u_1,\dots,u_{k-1})$, done. Otherwise pick $u_k\in U$ with $u_k\notin\operatorname{span}(u_1,\dots,u_{k-1})$.
- As long as the process runs, no vector is in the span of the previous ones, so the list is independent (by 2.19). An independent list cannot be longer than a spanning list of $V$ (2.22). So the process stops, and $U$ is spanned by a finite list.

**Exercises 2A** are listed at the end (p. 37–38).

### 2B Bases

**Definition 2.26.** A *basis* of $V$ is a list of vectors in $V$ that is linearly independent and spans $V$ (p. 39).

Examples 2.27 (p. 39):
- (a) The standard basis of $\mathbf F^n$ is $(1,0,\dots,0),\dots,(0,\dots,0,1)$.
- (b) $(1,2),(3,5)$ is a basis of $\mathbf F^2$. Its length equals that of the standard basis. The author says the next section shows this is no coincidence.
- (c) $(1,2,-4),(7,-5,6)$ is independent in $\mathbf F^3$ but not a basis, because it does not span.
- (d) $(1,2),(3,5),(4,13)$ spans $\mathbf F^2$ but is not a basis, because it is dependent.
- (e) $(1,1,0),(0,0,1)$ is a basis of $\{(x,x,y)\in\mathbf F^3: x,y\in\mathbf F\}$.
- (f) $(1,-1,0),(1,0,-1)$ is a basis of $\{(x,y,z)\in\mathbf F^3: x+y+z=0\}$.
- (g) $1,z,\dots,z^m$ is the standard basis of $\mathcal P_m(\mathbf F)$.
- $\mathbf F^2$ has many bases, e.g. $(7,5),(-4,9)$ and $(1,2),(3,5)$ (p. 39).

**2.28 Criterion for basis.** A list $v_1,\dots,v_n$ is a basis of $V$ iff every $v\in V$ can be written uniquely as $v=a_1v_1+\dots+a_nv_n$ with $a_1,\dots,a_n\in\mathbf F$ (2.29) (p. 39). Proof (p. 40):
- ($\Rightarrow$) Spanning gives existence. If also $v=c_1v_1+\dots+c_nv_n$, subtracting gives $0=\sum(a_k-c_k)v_k$. Independence gives $a_k=c_k$.
- ($\Leftarrow$) Existence for every $v$ means the list spans. If $0=a_1v_1+\dots+a_nv_n$, uniqueness of the representation of $v=0$ (which also has all scalars $0$) forces all $a_k=0$. So the list is independent, hence a basis.

*Intuition note.* A basis is a coordinate system. Every vector gets exactly one list of coordinates, $(a_1,\dots,a_n)$.

**2.30 Every spanning list contains a basis.** Every spanning list in a vector space can be reduced to a basis (p. 40). Proof: start with $B=v_1,\dots,v_n$, which spans $V$.
- Step 1: delete $v_1$ if $v_1=0$.
- Step $k$: delete $v_k$ if $v_k\in\operatorname{span}(v_1,\dots,v_{k-1})$.
- After step $n$ the list $B$ still spans, because only vectors already in the span of previous ones were discarded. No vector in $B$ is in the span of the previous ones, so $B$ is independent by 2.19. Hence $B$ is a basis (pp. 40–41).
- Example (p. 40): applying the procedure to $(1,2),(3,6),(4,7),(5,9)$ removes the second and fourth vectors, leaving the basis $(1,2),(4,7)$ of $\mathbf F^2$.

**2.31.** Every finite-dimensional vector space has a basis (a spanning list exists by definition, and 2.30 reduces it) (p. 41).

**2.32 Every independent list extends to a basis.** Every linearly independent list in a finite-dimensional space can be extended to a basis (p. 41). Proof:
- Let $u_1,\dots,u_m$ be independent and $w_1,\dots,w_n$ span $V$. Then $u_1,\dots,u_m,w_1,\dots,w_n$ spans $V$.
- Apply the procedure of 2.30. No $u$ is deleted, because the $u$'s are independent. The result is a basis consisting of the $u$'s and some of the $w$'s.
- Example in $\mathbf F^3$: from the independent list $(2,3,4),(9,6,8)$, using the standard basis for the $w$'s, the procedure gives the basis $(2,3,4),(9,6,8),(0,1,0)$ (p. 41).

**2.33 Every subspace is part of a direct sum equal to $V$.** If $V$ is finite-dimensional and $U$ is a subspace, there is a subspace $W$ with $V=U\oplus W$ (p. 42). Proof:
- $U$ is finite-dimensional (2.25), so it has a basis $u_1,\dots,u_m$ (2.31). It is independent in $V$, so it extends to a basis $u_1,\dots,u_m,w_1,\dots,w_n$ of $V$ (2.32). Let $W=\operatorname{span}(w_1,\dots,w_n)$.
- By 1.46 (Ch. 1, cited), it suffices to show $V=U+W$ and $U\cap W=\{0\}$.
- $V=U+W$: any $v=\underbrace{a_1u_1+\dots+a_mu_m}_{u}+\underbrace{b_1w_1+\dots+b_nw_n}_{w}$.
- $U\cap W=\{0\}$: if $v$ lies in both, $a_1u_1+\dots+a_mu_m-b_1w_1-\dots-b_nw_n=0$. Independence of the full list gives all scalars $0$, so $v=0$.
- The author remarks that with more advanced tools the result can be proved without assuming $V$ finite-dimensional (p. 41).

### 2C Dimension

**Motivation.** The standard basis of $\mathbf F^n$ has length $n$, so a natural definition of dimension is "length of a basis". That makes sense only if all bases of a space have the same length (p. 44).

**2.34 Basis length does not depend on basis.** Any two bases of a finite-dimensional space have the same length (p. 44). Proof: let $B_1,B_2$ be bases. $B_1$ is independent and $B_2$ spans, so $\operatorname{length}B_1\le\operatorname{length}B_2$ (2.22). Swapping roles gives the reverse inequality.

**Definition 2.35.** The *dimension* of a finite-dimensional vector space is the length of any basis; it is written $\dim V$ (p. 44).

Examples 2.36 (p. 44):
- $\dim\mathbf F^n=n$.
- $\dim\mathcal P_m(\mathbf F)=m+1$.
- For $U=\{(x,x,y):x,y\in\mathbf F\}$, $\dim U=2$, with basis $(1,1,0),(0,0,1)$.
- For $U=\{(x,y,z):x+y+z=0\}$, $\dim U=2$, with basis $(1,-1,0),(1,0,-1)$.

**The field matters.** The real vector space $\mathbf R^2$ has dimension two. The complex vector space $\mathbf C$ has dimension one. As sets $\mathbf R^2$ can be identified with $\mathbf C$. So the choice of $\mathbf F$ cannot be neglected (margin note, p. 45).

**2.37 Dimension of a subspace.** If $V$ is finite-dimensional and $U$ is a subspace of $V$, then $\dim U\le\dim V$ (p. 45). Proof: a basis of $U$ is an independent list in $V$ and a basis of $V$ is a spanning list. Apply 2.22.

**2.38 Independent list of the right length is a basis.** If $V$ is finite-dimensional, every independent list in $V$ of length $\dim V$ is a basis (p. 45). Proof: with $\dim V=n$, extend the list to a basis (2.32). Every basis has length $n$, so nothing was added.

**2.39 Subspace of full dimension is the whole space.** If $V$ is finite-dimensional, $U$ a subspace and $\dim U=\dim V$, then $U=V$ (p. 45). Proof: a basis $u_1,\dots,u_n$ of $U$ is an independent list in $V$ of length $\dim V$, so it is a basis of $V$ (2.38). So every vector of $V$ is a combination of the $u$'s, hence lies in $U$.

Examples (p. 46):
- 2.40: $(5,7),(4,3)$ is independent in $\mathbf F^2$ (neither is a multiple of the other), and $\dim\mathbf F^2=2$. So by 2.38 it is a basis, with no need to check spanning.
- 2.41: let $U=\{p\in\mathcal P_3(\mathbf R):p'(5)=0\}$.
  - The polynomials $1,(x-5)^2,(x-5)^3$ are in $U$.
  - Suppose $a+b(x-5)^2+c(x-5)^3=0$ for all $x$. The left side has a $cx^3$ term and the right side has no $x^3$ term, so $c=0$. Then the $bx^2$ term forces $b=0$, and then $a=0$. So the list is independent in $U$ and $3\le\dim U$.
  - By 2.37, $3\le\dim U\le\dim\mathcal P_3(\mathbf R)=4$.
  - The polynomial $x$ is not in $U$ (its derivative is the constant function $1$). So $U\ne\mathcal P_3(\mathbf R)$, and $\dim U\ne4$ by 2.39. Hence $\dim U=3$.
  - Thus $1,(x-5)^2,(x-5)^3$ has length $\dim U$ and is a basis of $U$ (2.38).

**2.42 Spanning list of the right length is a basis.** If $V$ is finite-dimensional, every list that spans $V$ and has length $\dim V$ is a basis (p. 46). Proof: reduce it to a basis (2.30). Every basis has length $n=\dim V$, so no vector is deleted.

*Intuition note.* With the right number of vectors, "no redundancy" and "reaches everywhere" imply each other. So you only need to check one.

**2.43 Dimension of a sum.** If $V_1,V_2$ are subspaces of a finite-dimensional vector space, then
$$\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2).$$
The author compares it with: the size of a union of two finite sets is the sum of sizes minus the size of the intersection (p. 47). Proof:
- Let $v_1,\dots,v_m$ be a basis of $V_1\cap V_2$. It is independent in $V_1$, so extend it to a basis $v_1,\dots,v_m,u_1,\dots,u_j$ of $V_1$; thus $\dim V_1=m+j$.
- Extend $v_1,\dots,v_m$ to a basis $v_1,\dots,v_m,w_1,\dots,w_k$ of $V_2$; thus $\dim V_2=m+k$.
- Claim: the list
$$v_1,\dots,v_m,u_1,\dots,u_j,w_1,\dots,w_k\tag{2.44}$$
  is a basis of $V_1+V_2$. Given the claim, $\dim(V_1+V_2)=m+j+k=(m+j)+(m+k)-m=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$.
- Spanning: the list lies in $V_1\cup V_2\subseteq V_1+V_2$. Its span contains $V_1$ and $V_2$, hence equals $V_1+V_2$.
- Independence: suppose $a_1v_1+\dots+a_mv_m+b_1u_1+\dots+b_ju_j+c_1w_1+\dots+c_kw_k=0$. Rewrite it as
$$c_1w_1+\dots+c_kw_k=-a_1v_1-\dots-a_mv_m-b_1u_1-\dots-b_ju_j.\tag{2.45}$$
  - The right side is in $V_1$, so $c_1w_1+\dots+c_kw_k\in V_1$. The $w$'s are in $V_2$, so it lies in $V_1\cap V_2$.
  - Hence $c_1w_1+\dots+c_kw_k=d_1v_1+\dots+d_mv_m$ for some scalars $d_i$.
  - The list $v_1,\dots,v_m,w_1,\dots,w_k$ is independent, so all $c$'s (and $d$'s) are $0$.
  - Then 2.45 becomes $a_1v_1+\dots+a_mv_m+b_1u_1+\dots+b_ju_j=0$. The list $v_1,\dots,v_m,u_1,\dots,u_j$ is independent, so all $a$'s and $b$'s are $0$.

*Intuition note.* Adding the dimensions counts the shared part twice. Subtracting $\dim(V_1\cap V_2)$ corrects for that, as in counting the elements of a union.

**Set–vector space analogy (table, p. 48).** For a finite set $S$, $\#S$ is the number of elements.

| sets | vector spaces |
|---|---|
| finite set $S$ | finite-dimensional $V$ |
| $\#S$ | $\dim V$ |
| union $S_1\cup S_2$ is the smallest subset containing $S_1,S_2$ | sum $V_1+V_2$ is the smallest subspace containing $V_1,V_2$ |
| $\#(S_1\cup S_2)=\#S_1+\#S_2-\#(S_1\cap S_2)$ | $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$ |
| $\#(S_1\cup S_2)=\#S_1+\#S_2\iff S_1\cap S_2=\emptyset$ | $\dim(V_1+V_2)=\dim V_1+\dim V_2\iff V_1\cap V_2=\{0\}$ |
| $S_1\cup\dots\cup S_m$ disjoint union $\iff \#(\cup S_i)=\sum\#S_i$ | $V_1+\dots+V_m$ direct sum $\iff \dim(\sum V_i)=\sum\dim V_i$ |

The proof of the last row is deferred to 3.94 (p. 48). The author says the reader should find set-results analogous to Exercises 2C.12–18 (p. 48).

## Toy example (ours, not from the text)
Work in $\mathbf R^3$. Let $V_1=\operatorname{span}((1,0,0),(0,1,0))$ and $V_2=\operatorname{span}((0,1,0),(0,0,1))$.

1. Intersection: $(a,b,0)=(0,c,d)$ forces $a=0$ and $d=0$. So $V_1\cap V_2=\{(0,b,0)\}$ with basis $v_1=(0,1,0)$, and $m=1$.
2. Extend to bases: $V_1$ has basis $v_1,u_1$ with $u_1=(1,0,0)$, so $\dim V_1=2$ and $j=1$. $V_2$ has basis $v_1,w_1$ with $w_1=(0,0,1)$, so $\dim V_2=2$ and $k=1$.
3. List 2.44 is $(0,1,0),(1,0,0),(0,0,1)$. It is the standard basis of $\mathbf R^3$ in another order, so it is independent and spans $V_1+V_2=\mathbf R^3$. Thus $\dim(V_1+V_2)=m+j+k=3$.
4. Formula check: $\dim V_1+\dim V_2-\dim(V_1\cap V_2)=2+2-1=3$. ✓.
5. Contrast: if $V_2'=\operatorname{span}((0,0,1))$, then $V_1\cap V_2'=\{0\}$ and $\dim(V_1+V_2')=2+1-0=3$, a direct sum.

## Concepts
- [[linear combination]] — a sum $a_1v_1+\dots+a_mv_m$ of scalar multiples of a list (p. 28)
- [[span]] — the set of all linear combinations of a list; the smallest subspace containing it; span of empty list is $\{0\}$ (p. 29)
- [[linear independence]] — only the all-zero scalars give the zero combination; equivalently, representations in the span are unique (p. 32)
- [[linear dependence lemma]] (new) — in a dependent list some vector is in the span of earlier ones; deleting it keeps the span (p. 33)
- [[finite-dimensional vector space]] (new) — a space spanned by some (finite) list (p. 30)
- [[basis]] — a list that is independent and spans; gives unique coordinates (pp. 39–40)
- [[dimension]] — the length of any basis; well defined by 2.34 (p. 44)
- [[standard basis]] (new) — $(1,0,\dots,0),\dots,(0,\dots,0,1)$ for $\mathbf F^n$; $1,z,\dots,z^m$ for $\mathcal P_m(\mathbf F)$ (p. 39)
- [[polynomial space P_m(F)]] (new) — polynomials of degree at most $m$; $\dim=m+1$ (pp. 31, 44)
- [[direct sum complement]] (new) — each subspace $U$ of a finite-dimensional $V$ has $W$ with $V=U\oplus W$ (p. 42)
- [[dimension of a sum]] (new) — $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$ (p. 47)

## Canonical instances
- [[example-span-17-4-2]] — $(17,-4,2)$ is in, and $(17,-4,5)$ is not in, the span of $(2,1,-3),(1,-2,4)$ (p. 28)
- [[example-P-infinite-dimensional]] — $\mathcal P(\mathbf F)$ has no spanning list, as $z^{m+1}$ escapes (p. 31)
- [[example-dependence-lemma-smallest-k]] — $(15,16,17)=3(1,2,3)+2(6,5,4)$, giving $k=3$ (p. 34)
- [[example-reduce-spanning-list]] — $(1,2),(3,6),(4,7),(5,9)$ reduces to $(1,2),(4,7)$ (p. 40)
- [[example-basis-of-P3-derivative-condition]] — $1,(x-5)^2,(x-5)^3$ is a basis of $\{p\in\mathcal P_3(\mathbf R):p'(5)=0\}$ (p. 46)
- [[example-R2-vs-C-dimension]] — $\mathbf R^2$ has dimension 2 over $\mathbf R$ but $\mathbf C$ has dimension 1 over $\mathbf C$ (p. 45)

## Bridges (candidates)
- [structural-analogy] $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$ ↔ combinatorics: inclusion–exclusion for two finite sets — the author's own table (p. 48) pairs them, but the two are different mathematics.
- [structural-analogy] basis and unique coordinates (2.28) ↔ linear-algebra canon: change of basis — a basis gives the coordinates that the canon's change-of-basis acts on.
- [metaphor] linear independence ("no vector is redundant") ↔ statistics/data: redundant, collinear features — an informal way to think about dependent lists.
- [structural-analogy] reducing a spanning list to a basis (2.30) ↔ numerical methods: a greedy, left-to-right procedure that keeps only vectors outside the span of earlier ones — compare with Gram–Schmidt in the canon.

## Questions this raises
- 2.22 shows independent lists are at most as long as spanning lists, but is $\dim U<\dim V$ whenever $U\ne V$? (2.39 gives the answer for finite-dimensional $V$.)
- How does $\dim$ change when linear maps are applied? (The author refers forward to 3.94 for the direct-sum dimension statement.)
- Does a basis exist in an infinite-dimensional space? (The text says 2.33 can be proved without finiteness using more advanced tools.)
- Is there an analogue of 2.43 for three subspaces? (Exercises 2C.19–20 explore this.)

## Exercises worth doing
- Ex. 2A.13 (p. 38) — adjoining $w$ keeps independence iff $w\notin\operatorname{span}$; the engine behind 2.25 and 2.32 — difficulty: medium
- Ex. 2A.17 (p. 38) — $V$ is infinite-dimensional iff it has an independent sequence $v_1,v_2,\dots$; a clean criterion — difficulty: medium
- Ex. 2B.10 (p. 43) — bases of $U$ and $W$ combine to a basis of $V$ when $V=U\oplus W$ — difficulty: medium
- Ex. 2C.12 (p. 49) — dimension counting forces a sum to be direct; applies 2.43 — difficulty: easy
- Ex. 2C.13 (p. 49) — two 5-dimensional subspaces of $\mathbf R^9$ must meet nontrivially; uses 2.43 — difficulty: easy
- Ex. 2C.19 (p. 50) — guess the three-subspace formula by analogy with sets, then test it — difficulty: hard

## Reading notes
- Printed page = pdf page − 14 (pdf 41 = printed 27).
- The text layer renders italic math symbols as unreadable glyphs and loses some equations (e.g. the underbraces in the proof of 2.33). All math here was checked against the page images.
- No misprints were found in these pages. Section 2C's table (p. 48) is reproduced from the image.
- Results cited but not in this unit: 1.34 (cited to show a span is a subspace) and 1.46 (cited as the criterion for $V=U\oplus W$) from Ch. 1; 4.8 (a polynomial is determined by its coefficients) from Ch. 4; 3.94 (dimension of direct sums) from Ch. 3.
- The unit ends with a Mary Shelley epigraph (p. 50). Chapter-opening notes about the Institute for Advanced Study and Halmos's 1942 book are on p. 27. Neither is used here.
