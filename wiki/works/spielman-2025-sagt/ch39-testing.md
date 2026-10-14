---
id: spielman-2025-sagt/ch39-testing
work: spielman-2025-sagt
unit: Chapter 39 — Testing Isomorphism of Graphs with Distinct Eigenvalues
pages: 307-316
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Testing Isomorphism of Graphs with Distinct Eigenvalues

## L0 — One line
If all eigenvalues of a graph have multiplicity 1, eigenvectors are fixed up to sign, so its automorphism group is isomorphic to a subspace of $(\mathbb Z/2)^n$, and the chapter's algorithm finds a basis of it in polynomial time using Gaussian elimination.

## L1 — The gist (≤ 120 words)
How can we test whether two graphs are isomorphic, using eigenvalues and eigenvectors? Assume all eigenvalues are distinct. Then an isomorphism must map eigenvectors to eigenvectors up to sign, so the problem becomes finding diagonal $\pm1$ matrices $S$ with $\Pi\Psi=\Phi S$. The algorithm splits the vertices into "balanced" classes using sign patterns of products of eigenvectors. On a balanced class, the allowed sign choices form a subspace over $\mathbb Z/2$, computed by linear algebra. Gluing the classes gives the whole automorphism group, in polynomial time. This is the Leighton–Miller idea, a special case of a stronger published result. The chapter is marked as needing editing.

**Prerequisites:** spectral decomposition of symmetric matrices; permutation matrices; groups and subgroups; vector spaces over $\mathbb Z/2$ and Gaussian elimination; orthogonal matrices.

## L2 — Key ideas
- Graphs are isomorphic iff $\Pi A\Pi^T=B$ for a permutation matrix $\Pi$ (p. 308).
- With distinct eigenvalues, $\Pi A\Pi^T=B$ iff $\Pi\Psi=\Phi S$ for a diagonal $\pm1$ matrix $S$ (Lemma 39.3.1, p. 309).
- The automorphism group is commutative and isomorphic to a subspace of $(\mathbb Z/2)^n$, so the goal is to output a basis (p. 310).
- Vertices are split into classes that are unions of orbits. An eigenvector product with unequal counts of $x$ and $-x$ on a class can split it, if both parts are non-empty (pp. 311–312).
- On a balanced class $C$, $|C|=2^{|Q|}$ and every other eigenvector is a constant times a product of eigenvectors in the base $Q$ (Cor. 39.9.4, eq. 39.1, p. 314).
- Finding a base and the group structure is linear algebra mod 2 (p. 315).
- At most $n$ splits happen, so the algorithm is polynomial. An open question remains: is every balanced class an orbit? (pp. 312, 316)

## L3 — Walkthrough

### 39.1 Introduction (p. 307)
The chapter presents an algorithm of Leighton and Miller for graphs whose eigenvalues all have multiplicity 1. It was never published. The result is technically subsumed by Babai–Grigoriev–Mount, who handle multiplicities bounded by a constant. The author presents the weaker result for simplicity. The fastest algorithm known until recently took time $2^{O(\sqrt{n\log n})}$. Babai recently announced $2^{(\log n)^{O(1)}}$. The author says isomorphism seems easy in almost all practical instances (p. 307).

### 39.2 Graph isomorphism (pp. 307–308)
$G=(V,E)$ and $H=(V,F)$ are isomorphic if some permutation $\pi$ of $V$ satisfies $(a,b)\in E\iff(\pi(a),\pi(b))\in F$. The permutation matrix has $\Pi(a,b)=1$ if $\pi(a)=b$, else 0, and $(\Pi\psi)(a)=\psi(\pi(a))$. The author flags that permutation and inverse are easy to confuse (footnote 1). With adjacency matrices $A,B$: isomorphic iff $\Pi A\Pi^T=B$ for some permutation matrix $\Pi$ (p. 308).

### 39.3 Using eigenvalues and eigenvectors (pp. 308–309)
Isomorphic graphs have the same eigenvalues. Different eigenvalues imply non-isomorphic. The converse fails: many non-isomorphic pairs share eigenvalues (p. 308). From here on, $A$ and $B$ have the same eigenvalues, all of multiplicity 1.

Write $A=\Psi\Lambda\Psi^T$ and $B=\Phi\Lambda\Phi^T$ ($\Psi,\Phi$: $n\times n$ orthonormal; $\Lambda$: $n\times n$ diagonal). If $\Pi$ is an isomorphism then $\Pi\Psi\Lambda\Psi^T\Pi^T=\Phi\Lambda\Phi^T$. Eigenvectors are fixed only up to sign, so this gives $\Pi\Psi=\Phi S$ with $S$ diagonal $\pm1$ (p. 308).

**Lemma 39.3.1.** Let $A=\Psi\Lambda\Psi^T$ and $B=\Phi\Lambda\Phi^T$ with $\Lambda$ diagonal with distinct entries and $\Psi,\Phi$ orthogonal. A permutation matrix satisfies $\Pi A\Pi^T=B$ iff there is a diagonal $\pm1$ matrix $S$ with $\Pi\Psi=\Phi S$ (p. 309).

*Proof (p. 309).* ($\Rightarrow$) Expanding,
$$\Phi\Lambda\Phi^T=\sum_i \phi_i\lambda_i\phi_i^T=\sum_i(\Pi\psi_i)\lambda_i(\psi_i^T\Pi^T),$$
which implies $\phi_i\phi_i^T=(\Pi\psi_i)(\Pi\psi_i)^T$ for all $i$, hence $\phi_i=\pm\Pi\psi_i$. ($\Leftarrow$) If $\Pi\Psi=\Phi S$ then
$$\Pi A\Pi^T=\Pi\Psi\Lambda\Psi^T\Pi^T=\Phi S\Lambda S\Phi^T=\Phi\Lambda SS\Phi^T=\Phi\Lambda\Phi^T=B,$$
because diagonal matrices commute and $S^2=I$.

*Intuition note.* Because eigenvectors are fixed only up to sign, an isomorphism must send each $\psi_i$ to $\pm\phi_i$, so what remains to find is one sign per eigenvector: the diagonal matrix $S$.

Let $\mathcal S$ be the set of diagonal $\pm1$ matrices. Row $a$ of $\Psi$ is $v_a=(\psi_1(a),\dots,\psi_n(a))$. Rows of $\Phi$ are $u_a$. We seek $S\in\mathcal S$ with $\{v_a\}_{a\in V}=\{u_aS\}_{a\in V}$, a problem about vectors (p. 309).

### 39.4 An easy case (pp. 309–310)
Call $\psi_i$ *helpful* if $|\psi_i(a)|\ne|\psi_i(b)|$ for all $a\ne b$. Any isomorphism sends $\psi_i$ to $\pm\phi_i$. If the sets of absolute values of $\psi_i$ and $\phi_i$ agree, map each $a$ to the $b$ with $|\psi_i(a)|=|\phi_i(b)|$ (p. 309). If $\psi_i(a)\ne\psi_i(b)$ for all $a\ne b$ and the sign can be chosen canonically, one vector fixes the isomorphism. Example: if the entries do not sum to zero, make the sum positive. Unless $\psi_i$ and $-\psi_i$ have exactly the same set of values, a canonical sign exists. Even with no canonical sign, the vector leaves at most two choices for the isomorphism (p. 310).

### 39.5 All the automorphisms (p. 310)
An automorphism is an isomorphism of a graph with itself. These form a group $\mathsf{aut}(G)$. Let $\mathcal A\subseteq\mathcal S$ be the corresponding sign matrices. $\mathcal A$ is a group isomorphic to $\mathsf{aut}(G)$. By Lemma 39.3.1, $\Pi=\Psi S\Psi^T$ and $S=\Psi^T\Pi\Psi$. Since diagonal matrices commute,
$$\Pi_1\Pi_2=\Psi S_1\Psi^T\Psi S_2\Psi^T=\Psi S_1S_2\Psi^T=\Psi S_2S_1\Psi^T=\Psi S_2\Psi^T\Psi S_1\Psi^T=\Pi_2\Pi_1 .$$
So $\mathsf{aut}(G)$ is commutative and isomorphic to a subgroup of $\mathcal S$.

Define $f:\mathcal S\to(\mathbb Z/2)^n$ by $S(i,i)=(-1)^{t(i)}$, $t=f(S)$. It is an invertible group homomorphism, $f(S_1S_2)=f(S_1)+f(S_2)$ (the author leaves both checks to the reader). Subgroups of $\mathcal S$ thus correspond to subspaces of $(\mathbb Z/2)^n$. The goal for this chapter is to give a basis of the subspace for $\mathsf{aut}(G)$, not to list all automorphisms. The author will probably leave the slight extension to finding isomorphisms for homework (p. 310).

### 39.6 Equivalence classes of vertices (pp. 310–311)
The orbit of $a$ is the set of $b$ with $v_aS=v_b$ for some $S\in\mathcal A$. Orbits partition $V$. A partition is *valid* if every class is a union of orbits. The algorithm builds a valid partition and splits classes until each is an orbit (p. 311). Later the author says the algorithm will partition the vertices into balanced classes, and does not know whether every balanced class is an orbit (p. 312).

$\mathcal A$ stabilizes every orbit. The author does not yet see how to build the stabilizer of each orbit directly. Instead, for each class $C_j$ of a particular valid partition, compute $\mathcal A_j\subseteq\mathcal S$, the subgroup stabilizing $C_j$. $\mathcal A_j$ acts transitively on $C_j$. $\mathcal A\subseteq\mathcal A_j$, and $\mathcal A$ equals the intersection of all $\mathcal A_j$ (p. 311).

Each $\mathcal A_j$ maps to a subspace of $(\mathbb Z/2)^n$, described by a basis. To get $\mathcal A$: take a basis of each nullspace, span them, and take the nullspace of that span. All of this uses Gaussian elimination (p. 311).

### 39.7 The first partition (p. 311)
If $|\psi_i(a)|\ne|\psi_i(b)|$ for some $i$, no $S$ has $v_aS=v_b$. So grouping vertices by their absolute values in all eigenvectors gives a valid partition, the starting point.

### 39.8 Unbalanced vectors (pp. 311–312)
$\psi_i$ is *unbalanced* if for some $x$, $|\{a:\psi_i(a)=x\}|\ne|\{a:\psi_i(a)=-x\}|$. Then $S(i,i)$ must be $1$ for every automorphism matrix $S\in\mathcal A$, since $S(i,i)=-1$ would need a bijection between sets of different sizes (p. 311). Vertices with value $x$ and with value $-x$ lie in different orbits.

Two extensions (p. 312):
1. *On a class $C$:* use counts within $C$. For a class of a valid partition, split $C$ into $C_0=\{a\in C:\psi_i(a)=x\}$ and $C_1=\{a\in C:\psi_i(a)=-x\}$. The resulting partition is again valid; it is only useful if both parts are non-empty.
2. *Products:* for $R\subseteq\{1,\dots,n\}$, $\psi_R(a)=\prod_{i\in R}\psi_i(a)$. If $\psi_R$ is unbalanced on $C$ (same count condition), it splits $C$ the same way.

A vector is *balanced* if not unbalanced. A set $C$ is *balanced* if every non-constant product of eigenvectors is balanced on $C$. Orbits are balanced. The algorithm partitions $V$ into balanced classes. **Open question (author):** is every balanced class an orbit of $\mathcal A$? The author does not know (p. 312).

### 39.9 Structure of balanced classes (pp. 312–315)
Let $C$ be balanced. A set $Q$ of eigenvectors is *independent on $C$* if every non-empty product of eigenvectors from $Q$ is balanced on $C$. So none is zero or constant on $C$. Define the $|C|\times 2^{|Q|}$ matrix $M_{C,Q}$, rows indexed by $a\in C$ and columns by $R\subseteq Q$, with
$$M_{C,Q}(a,R)=\operatorname{sgn}(\psi_R(a)),\qquad \operatorname{sgn}(x)=1,\,-1,\,0\ \text{for } x>0,\,<0,\,=0 .$$

**Lemma 39.9.1.** If $Q$ is independent on $C$, the columns of $M_{C,Q}$ are orthogonal (p. 313).
*Proof.* Take $R_1\ne R_2$ and let $R_0$ be their symmetric difference. Then $M(a,R_1)M(a,R_2)=\prod_{R_1}\operatorname{sgn}\psi_i(a)\prod_{R_2}\operatorname{sgn}\psi_i(a)=\prod_{R_0}\operatorname{sgn}\psi_i(a)=M(a,R_0)$. $\psi_{R_0}$ is balanced on $C$, so $M(a,R_0)$ is positive for half the $a\in C$ and negative for the other half. Hence $M(:,R_1)^TM(:,R_2)=\sum_a M(a,R_0)=0$.

**Lemma 39.9.2.** If $C$ is balanced and $Q$ is a maximal independent set on $C$, then for all $a,b\in C$ some $i\in Q$ has $\psi_i(a)\ne\psi_i(b)$ (p. 313).
*Proof.* Suppose $\psi_h(a)=\psi_h(b)$ for all $h\in Q$. The author takes some eigenvector $i$ with $\psi_i(a)\ne\psi_i(b)$. For $R\subseteq Q$, $\psi_R(a)=\psi_R(b)$, so $\psi_{R\cup\{i\}}(a)\ne\psi_{R\cup\{i\}}(b)$. So $\psi_{R\cup\{i\}}$ is not constant on $C$, hence balanced. Then $Q\cup\{i\}$ would be independent, contradicting maximality.

**Lemma 39.9.3.** Under the same hypotheses, the rows of $M_{C,Q}$ are orthogonal (pp. 313–314).
*Proof.* For $a\ne b$ in $C$, the author takes $i\in Q$ with $\psi_i(a)=-\psi_i(b)$ (from Lemma 39.9.2). Pair each $R\subseteq Q-\{i\}$ with $R\cup\{i\}$:
$$\sum_{R\subseteq Q}\operatorname{sgn}(\psi_R(a)\psi_R(b))=\sum_{R\subseteq Q-\{i\}}\Big[\operatorname{sgn}(\psi_R(a)\psi_R(b))+\operatorname{sgn}(\psi_R(a)\psi_R(b))\operatorname{sgn}(\psi_i(a)\psi_i(b))\Big]=\sum_{R\subseteq Q-\{i\}}\big[\operatorname{sgn}(\psi_R(a)\psi_R(b))-\operatorname{sgn}(\psi_R(a)\psi_R(b))\big]=0 .$$

**Corollary 39.9.4.** For balanced $C$, $|C|$ is a power of 2, and any independent $Q$ has $|Q|\le\log_2|C|$ (p. 314).
*Proof.* For maximal $Q$, rows and columns of $M_{C,Q}$ are both orthogonal, so it is square: $|C|=2^{|Q|}$. For any independent $Q$, the $2^{|Q|}$ orthogonal columns live in $|C|$ dimensions, so $2^{|Q|}\le|C|$. (The text's proof opens "Let $C$ be an orbit", though the statement is for balanced $C$.)

*Intuition note.* On a balanced class, every non-empty product of eigenvectors from $Q$ is positive on exactly half the vertices and negative on the other half (like fair coin flips; our image). For a base $Q$, the table $M_{C,Q}$ of signs of these products has orthogonal rows and columns, so it is square, which forces $|C|=2^{|Q|}$.

**Structure.** A maximal independent set $Q$ is a *base* for $C$. Every other eigenvector $j$ is constant on $C$, or becomes constant after multiplying by $\psi_R$ for some $R\subseteq Q$. In both cases
$$\psi_j(a)=\gamma\prod_{i\in R}\psi_i(a)\quad\text{for all }a\in C,\ \text{some constant }\gamma. \tag{39.1}$$
Let $v_a(Q)$ be $v_a$ restricted to coordinates in $Q$. By Lemma 39.9.2 the $2^{|Q|}$ restrictions are distinct, so each of the $2^{|Q|}$ sign patterns occurs exactly once. For any diagonal $\pm1$ matrix $S_Q$, $\{v_a(Q)S_Q\}=\{v_a(Q)\}$ (p. 314).

So the subgroup of $\mathcal S$ stabilizing $C$ has free diagonal entries on $Q$, and every other diagonal entry is a product of those. Apply $f$ and let $B$ be an $n\times\log_2|C|$ matrix whose columns are a basis of the subspace. Any $\log_2|C|$ independent rows of $B$ form a basis of the row space and correspond to a base (pp. 314–315).

### 39.10 Algorithms (pp. 315–316)
*Finding a base.* Go through eigenvectors in order, building $Q$. For $\psi_i$, test whether $\psi_i(a)=\gamma\prod_{h\in Q}\psi_h(a)^{y_h}$ with $y_h\in\{0,1\}$ for all $a\in C_j$. The author says this holds iff $\operatorname{sgn}\psi_i(a)=\prod_h\operatorname{sgn}\psi_h(a)^{y_h}$. Write $\psi_i(a)=(-1)^{B(i,a)}$ with $B$ over $\mathbb Z/2$ (a different $B$ from the adjacency matrix). The condition is
$$B(i,a)=\sum_{h\in Q}y_hB(h,a)\quad\text{for all }a\in C_j,$$
solvable mod 2 in polynomial time. If a solution exists, record the product as part of the structure of $\mathcal A_j$. Otherwise add $i$ to $Q$ (p. 315).

*Detecting unbalanced classes.* Each time $\psi_i$ is added to $Q$, check every product of vectors in $Q$ for imbalance on $C_j$. There are at most $2^{|Q|}\le|C_j|$ products, none constant. Any unbalanced one splits $C_j$ in two (p. 315).

*Whole algorithm (p. 316).* Compute the absolute-value partition (39.7). Process classes one by one: either split the class, or find it balanced and compute its group. After a split, refine and restart. There are at most $n$ splits, so the running time is polynomial. Finally combine the groups as at the end of 39.6.

## Toy example (ours, not from the text)
Let $C=\{a_1,\dots,a_4\}$ and suppose the restrictions of three eigenvectors to $C$ give rows
$v_{a_1}=(\tfrac12,\tfrac12,\tfrac12)$, $v_{a_2}=(\tfrac12,-\tfrac12,-\tfrac12)$, $v_{a_3}=(-\tfrac12,\tfrac12,-\tfrac12)$, $v_{a_4}=(-\tfrac12,-\tfrac12,\tfrac12)$.
Take $Q=\{1,2\}$. Columns of $M_{C,Q}$ for $R=\emptyset,\{1\},\{2\},\{1,2\}$:
rows $a_1$: $(1,1,1,1)$; $a_2$: $(1,1,-1,-1)$; $a_3$: $(1,-1,1,-1)$; $a_4$: $(1,-1,-1,1)$.
Check: col$_\emptyset\cdot$col$_1=1+1-1-1=0$; col$_1\cdot$col$_2=1-1-1+1=0$. The matrix is $4\times4$, so $|C|=4=2^2$.
Eigenvector 3 satisfies $\psi_3=2\psi_1\psi_2$ on $C$, as in (39.1) with $\gamma=2$: at $a_2$, $2\cdot\tfrac12\cdot(-\tfrac12)=-\tfrac12$ ✓; at $a_3$, $-\tfrac12$ ✓; at $a_4$, $2\cdot\tfrac14=\tfrac12$ ✓.
Sign choices: $S=\mathrm{diag}(1,-1,-1)$ sends $v_{a_1}$ to $(\tfrac12,-\tfrac12,-\tfrac12)=v_{a_2}$, and the row set is preserved. But $\mathrm{diag}(1,1,-1)$ sends $v_{a_1}$ to $(\tfrac12,\tfrac12,-\tfrac12)$, which is not a row. Over $\mathbb Z/2$ the allowed $t$ satisfy $t_3=t_1+t_2$, a subspace with basis $(1,0,1),(0,1,1)$ of size $2^2=|C|$.

## Concepts
- [[graph-isomorphism]] (new) — a vertex permutation preserving edges; equivalently $\Pi A\Pi^T=B$ (p. 308)
- [[permutation-matrix]] (new) — $\Pi(a,b)=1$ iff $\pi(a)=b$ (p. 308)
- [[adjacency matrix]] — the matrix used here to encode graphs (p. 307)
- [[diagonalization]] — $A=\Psi\Lambda\Psi^T$; distinct eigenvalues fix eigenvectors up to sign (p. 308)
- [[orthonormal basis / orthogonal matrix]] — $\Psi,\Phi$ in the lemma (p. 309)
- [[automorphism-group]] (new) — isomorphisms of a graph to itself; commutative here and embeds in $\{\pm1\}^n\cong(\mathbb Z/2)^n$ (p. 310)
- [[orbit-and-valid-partition]] (new) — orbit: images of a vertex under the group; valid partition: classes are unions of orbits (p. 311)
- [[balanced-class]] (new) — a vertex set on which every non-constant eigenvector product has equal counts of $x$ and $-x$ (p. 312)
- [[base-of-balanced-class]] (new) — a maximal set $Q$ of independent eigenvectors on $C$; $|C|=2^{|Q|}$ (p. 314)
- [[null space (kernel)]] — nullspaces mod 2 are used to intersect the subgroups $\mathcal A_j$ (p. 311)

## Canonical instances
- [[leighton-miller-isomorphism-test]] — the Leighton–Miller algorithm for graphs with distinct eigenvalues (p. 307); the automorphism-group computation runs in polynomial time (p. 316)
- [[sign-pattern-matrix-M]] — the $\pm1$ matrix showing a balanced class has size $2^{|Q|}$ (pp. 313–314)

## Bridges (candidates)
- [same-math] Solving $B(i,a)=\sum y_hB(h,a)$ over $\mathbb Z/2$ ↔ linear algebra: Gaussian elimination in a finite field — literally the same elimination.
- [structural-analogy] Columns of $M_{C,Q}$, an orthogonal $\pm1$ matrix on subsets of $Q$ ↔ Hadamard/Walsh-type matrices (canon link; not stated in this unit).
- [structural-analogy] Cospectral non-isomorphic graphs ↔ limits of spectral invariants; the text defers them to the next lecture (p. 308).

## Questions this raises
- Is every balanced class an orbit of $\mathcal A$? The author does not know (p. 312).
- How does the method turn into finding isomorphisms $G\to H$, not only automorphisms (the homework extension, p. 310)?
- What breaks when eigenvalues repeat, so that eigenvectors are no longer fixed up to sign?
- What do the "tricky" non-isomorphic graphs with equal eigenvalues look like (promised for the next lecture, p. 308)?

## Reading notes
- Printed page = pdf − 24. The running header reads "CHAPTER 39. TESTING ISOMORPHISM OF GRAPHS WITH DISTINCT EIGENVALUES". The first page carries a red banner "This Chapter Needs Editing".
- Footnote 2 (p. 311) reads $v_aS=b_b$; presumably $v_b$ is meant.
- Section 39.8 defines $C_0,C_1$ but then says "$C_1$ and $C_2$" (p. 312).
- The proof of Corollary 39.9.4 starts "Let $C$ be an orbit", while the statement concerns balanced $C$ (p. 314).
- Lemma 39.9.3's proof uses $\psi_i(a)=-\psi_i(b)$, while Lemma 39.9.2 gives only $\ne$. This seems to rely on equal absolute values within a class (39.7); the text does not say so.
- In the paragraph after Corollary 39.9.4, "$a\ne b$ in $Q$" (p. 314) presumably means $a,b\in C$.
- $B$ denotes the adjacency matrix of $H$ (p. 308), a $\mathbb Z/2$ matrix with $\psi_i(a)=(-1)^{B(i,a)}$ (p. 315), and the $n\times\log_2|C|$ basis matrix (p. 315). These are three different uses.
- The unit contains no exercises. The author leaves some checks to the reader ("You should check…", p. 310).
