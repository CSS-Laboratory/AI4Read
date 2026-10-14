---
id: boyd-2018-vmls/ch05-linear
work: boyd-2018-vmls
unit: Chapter 5 — Linear independence
pages: 89–104
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Linear independence

## L0 — One line
A list of vectors is linearly independent when only the all-zero coefficients combine them to zero; this makes coefficients unique, caps the list size at $n$ for $n$-vectors, and the Gram–Schmidt algorithm tests it.

## L1 — The gist (≤ 120 words)
The chapter asks: when is a list of vectors free of redundancy, and how can we test this? Answer: a list is independent if the only combination giving zero has all coefficients zero. Then every combination has unique coefficients. An independent list of $n$-vectors has at most $n$ members, and $n$ independent $n$-vectors form a basis: every $n$-vector is a unique combination of them. Orthonormal vectors (perpendicular, unit length) are automatically independent, and their coefficients are plain inner products. The Gram–Schmidt algorithm turns a list into orthonormal vectors, and it stops early exactly when a vector depends on earlier ones. It costs about $2nk^2$ flops. This matters because the book says independence will play an important role later.

**Prerequisites:** linear combinations; inner product, norm and orthogonality; proof by induction; the idea of a flop (one arithmetic operation).

## L2 — Key ideas
- **Dependence/independence.** Dependent means some non-trivial combination gives $0$. Equivalently, one vector is a combination of the others. Independent means only zero coefficients give $0$ (pp. 89–90).
- **Unique coefficients.** Independence holds if and only if every combination of the list has exactly one coefficient set (p. 91).
- **Independence-dimension inequality.** Any $n+1$ or more $n$-vectors are dependent, proved by induction on $n$ (pp. 91, 94–95).
- **Basis.** $n$ independent $n$-vectors form a basis, and every $n$-vector has a unique expansion in it. Example: any cash flow equals an initial payment plus one-period loans, and the first coefficient is its net present value, $c_1+c_2/(1+r)+\cdots$ (pp. 92–94).
- **Orthonormal vectors.** They are independent, and coefficients are $a_i^Tx$. So $x=\sum (a_i^Tx)a_i$ for an orthonormal basis (pp. 95–97).
- **Gram–Schmidt.** It subtracts multiples $(q_i^Ta_j)q_i$ of the earlier $q_i$ from $a_j$, then normalizes. A zero $\tilde q_j$ means $a_j$ depends on earlier vectors (pp. 97–100).
- **Uses of Gram–Schmidt.** It tests independence, tests whether $b$ is a linear combination of an independent list, and checks for a basis (p. 101).
- **Cost.** About $2nk^2$ flops (order $nk^2$); $2n^3$ for $k=n$. Modified Gram–Schmidt gives the same results with less round-off sensitivity (p. 102).

## L3 — Walkthrough

### 5.1 Linear dependence (pp. 89–91)
**Definition.** $n$-vectors $a_1,\dots,a_k$ ($k\ge1$) are *linearly dependent* if
$$\beta_1a_1+\cdots+\beta_ka_k=0$$
for some $\beta_i$ not all zero. Order does not matter (p. 89).

If $\beta_i\neq0$, we can solve for $a_i$:
$$a_i=(-\beta_1/\beta_i)a_1+\cdots+(-\beta_{i-1}/\beta_i)a_{i-1}+(-\beta_{i+1}/\beta_i)a_{i+1}+\cdots+(-\beta_k/\beta_i)a_k .$$
So at least one vector is a combination of the others. The converse also holds (p. 89). Dependence is a property of the collection, not of single vectors (p. 89).

**Definition.** The list is *linearly independent* if it is not dependent, i.e.
$$\beta_1a_1+\cdots+\beta_ka_k=0\tag{5.1}$$
holds only for $\beta_1=\cdots=\beta_k=0$ (pp. 89–90). It is generally not easy to see by inspection which case holds (p. 90).

**Examples (p. 90).**
- A single vector is dependent only if it is zero, and independent only if nonzero.
- Any list containing the zero vector is dependent.
- Two vectors are dependent if and only if one is a multiple of the other.
- $a_1=(0.2,-7.0,8.6)$, $a_2=(-0.1,2.0,-1.0)$, $a_3=(0.0,-1.0,2.2)$ are dependent, since $a_1+2a_2-3a_3=0$. For example $a_2=(-1/2)a_1+(3/2)a_3$.
- $a_1=(1,0,0)$, $a_2=(0,-1,1)$, $a_3=(-1,1,1)$ are independent. If $\sum\beta_ia_i=0$, then $\beta_1-\beta_3=0$, $-\beta_2+\beta_3=0$, $\beta_2+\beta_3=0$. Adding the last two gives $2\beta_3=0$. So $\beta_3=0$, then $\beta_1=0$ and $\beta_2=0$.
- The standard unit vectors $e_1,\dots,e_n$ are independent: $\beta_1e_1+\cdots+\beta_ne_n=(\beta_1,\dots,\beta_n)$.

**Unique coefficients (p. 91).** Suppose $a_1,\dots,a_k$ are independent and $x=\sum\beta_ia_i=\sum\gamma_ia_i$. Subtracting gives $0=\sum(\beta_i-\gamma_i)a_i$. Independence then forces $\beta_i=\gamma_i$. The converse holds: if every combination has only one coefficient set, the list is independent. So a list is independent if and only if the coefficients of any combination can be deduced (p. 91).

**Supersets and subsets (p. 91).** Adding vectors to a dependent list keeps it dependent. Any nonempty subset of an independent list is independent.

*Intuition note.* Independent means no vector is redundant: each brings a new direction. That is why a combination can be "read backwards" to recover its recipe.

### 5.2 Basis (pp. 91–95)
**Independence-dimension inequality.** If $n$-vectors $a_1,\dots,a_k$ are independent, then $k\le n$. Equivalently, any $n+1$ or more $n$-vectors are dependent. For instance, any three 2-vectors are dependent (Figure 5.1: $a_3$ is a combination $\gamma_1a_1+\gamma_2a_2$) (pp. 91–92). The proof comes after the basis discussion.

**Basis (p. 92).** A collection of $n$ independent $n$-vectors is a *basis*.

*Claim:* if $a_1,\dots,a_n$ is a basis, every $n$-vector $b$ is a combination of them.
1. By the inequality, $a_1,\dots,a_n,b$ are dependent: $\beta_1a_1+\cdots+\beta_na_n+\beta_{n+1}b=0$ with not all $\beta$ zero.
2. If $\beta_{n+1}=0$, independence of the $a_i$ gives $\beta_1=\cdots=\beta_n=0$. All $\beta$ would be zero, a contradiction.
3. So $\beta_{n+1}\neq0$, and $b=(-\beta_1/\beta_{n+1})a_1+\cdots+(-\beta_n/\beta_{n+1})a_n$.

With uniqueness from 5.1, any $n$-vector $b$ can be written in a unique way as a combination of a basis (p. 92). The *expansion* of $b$ is $b=\alpha_1a_1+\cdots+\alpha_na_n$, and the $\alpha_i$ are its *coefficients* (p. 92).

*Intuition note.* A basis has exactly enough independent vectors to reach every $n$-vector, and only one way to reach each. A basis acts like a coordinate system.

**Examples (p. 93).** $e_1,\dots,e_n$ are a basis, with $b=b_1e_1+\cdots+b_ne_n$. The vectors $a_1=(1.2,-2.6)$, $a_2=(-0.3,-3.7)$ are a basis. Then $b=(1,1)=0.6513a_1-0.7280a_2$, to 4 significant digits. Computing such coefficients is deferred to later (p. 93).

**Cash flows and single-period loans (pp. 93–94).** A cash flow is an $n$-vector (positive = cash in, negative = cash out). For per-period interest rate $r\ge0$, define
$$l_i=(0_{i-1},\,1,\,-(1+r),\,0_{n-i-1}),\quad i=1,\dots,n-1 .$$
This is a loan of \$1 in period $i$, repaid with interest in period $i+1$. Claim: $e_1,l_1,\dots,l_{n-1}$ are a basis.
1. Suppose $\beta_1e_1+\beta_2l_1+\cdots+\beta_nl_{n-1}=0$. The entries are $\beta_1+\beta_2,\ \beta_3-(1+r)\beta_2,\ \dots,\ \beta_n-(1+r)\beta_{n-1},\ -(1+r)\beta_n$.
2. The last entry gives $\beta_n=0$, since $1+r>0$.
3. Working upward gives $\beta_{n-1}=\cdots=\beta_2=0$. The first entry $\beta_1+\beta_2=0$ then gives $\beta_1=0$.

So the $n$ vectors are independent, hence a basis. Any cash flow can be replicated as $c=\alpha_1e_1+\alpha_2l_1+\cdots+\alpha_nl_{n-1}$. The first coefficient is
$$\alpha_1=c_1+\frac{c_2}{1+r}+\cdots+\frac{c_n}{(1+r)^{n-1}},$$
which is the net present value (NPV) of $c$. So any cash flow equals an income in period 1 equal to its NPV, plus a combination of one-period loans (p. 94). The other coefficients are left to exercise 5.3.

*Intuition note.* Each loan "shifts" money one period with interest. Triangular structure (last entry first) lets us solve for coefficients one by one.

**Proof of the independence-dimension inequality (p. 94–95).** Induction on $n$.
*Idea:* split off the last entry of each vector and reduce to dimension $n-1$.
- *Case $n=1$.* Independent 1-vectors need $a_1\neq0$. Then every $a_i=(a_i/a_1)a_1$ is a multiple of $a_1$, contradicting independence unless $k=1$.
- *Step.* Assume the claim for $n-1$, with $n\ge2$. Let $a_1,\dots,a_k$ be independent $n$-vectors. Partition $a_i=\binom{b_i}{\alpha_i}$ with $b_i$ an $(n-1)$-vector and $\alpha_i$ a scalar.
- *Case A: all $\alpha_i=0$.* Then $\sum\beta_ib_i=0$ if and only if $\sum\beta_ia_i=0$, which forces all $\beta_i=0$. So $b_1,\dots,b_k$ are independent, and the induction hypothesis gives $k\le n-1\le n$.
- *Case B: some $\alpha_j\neq0$.* Define $k-1$ vectors of length $n-1$:
$$c_i=b_i-\frac{\alpha_i}{\alpha_j}b_j\ (i=1,\dots,j-1),\qquad c_i=b_{i+1}-\frac{\alpha_{i+1}}{\alpha_j}b_j\ (i=j,\dots,k-1).$$
Suppose $\sum_{i=1}^{k-1}\beta_ic_i=0$. Then
$$\sum_{i=1}^{j-1}\beta_i\binom{b_i}{\alpha_i}+\gamma\binom{b_j}{\alpha_j}+\sum_{i=j+1}^{k}\beta_{i-1}\binom{b_i}{\alpha_i}=0\tag{5.2}$$
with $\gamma=-\frac1{\alpha_j}\big(\sum_{i=1}^{j-1}\beta_i\alpha_i+\sum_{i=j+1}^{k}\beta_{i-1}\alpha_i\big)$. (Added step: the top block of (5.2) is $\sum\beta_ic_i$ rewritten with the $b_j$ terms collected into $\gamma b_j$. The bottom entry is zero by the definition of $\gamma$.) The $a_i$ are independent, so all coefficients $\beta_i$ and $\gamma$ are zero. So $c_1,\dots,c_{k-1}$ are independent, and the induction hypothesis gives $k-1\le n-1$, so $k\le n$.

### 5.3 Orthonormal vectors (pp. 95–97)
**Definitions (p. 95).** A list is *orthogonal* if $a_i\perp a_j$ for $i\ne j$. It is *orthonormal* if also $\|a_i\|=1$. Equivalently, $a_i^Ta_j=1$ if $i=j$ and $0$ if $i\ne j$. Orthonormality is a property of the collection.

**Examples.** The $e_i$ are orthonormal. So are the 3-vectors
$$(0,0,-1),\quad \tfrac1{\sqrt2}(1,1,0),\quad \tfrac1{\sqrt2}(1,-1,0).\tag{5.3}$$

**Orthonormal implies independent (p. 96).** If $\sum\beta_ja_j=0$, take the inner product with $a_i$: $0=\sum_j\beta_j(a_i^Ta_j)=\beta_i$.

**Coefficients by inner products (p. 96).** If $x=\sum\beta_ja_j$ with $a_j$ orthonormal, the same argument gives $a_i^Tx=\beta_i$. So
$$x=(a_1^Tx)a_1+\cdots+(a_k^Tx)a_k.\tag{5.4}$$
Identity (5.4) holding for $y$ is a test that $y$ is a combination of $a_1,\dots,a_k$. Conversely, if $y$ is such a combination, (5.4) holds for $y$.

**Orthonormal basis (p. 96).** $n$ orthonormal $n$-vectors are independent, hence a basis (an *orthonormal basis*). For any $n$-vector $x$,
$$x=(a_1^Tx)a_1+\cdots+(a_n^Tx)a_n.\tag{5.5}$$
This is the *orthonormal expansion formula*. It holds because $x$ is a combination of a basis, so (5.4) applies.

**Example (pp. 96–97).** For $x=(1,2,3)$ and basis (5.3), the inner products are $-3$, $3/\sqrt2$, $-1/\sqrt2$. So $x=(-3)(0,0,-1)+\frac3{\sqrt2}\big(\tfrac1{\sqrt2}(1,1,0)\big)+\frac{-1}{\sqrt2}\big(\tfrac1{\sqrt2}(1,-1,0)\big)$.

*Intuition note.* With perpendicular unit vectors, each coefficient is just "how much of $x$ points along $a_i$". No equations need solving.

### 5.4 Gram–Schmidt algorithm (pp. 97–102)
**Purpose (p. 97).** It determines whether $n$-vectors $a_1,\dots,a_k$ are independent. If they are, it produces orthonormal $q_1,\dots,q_k$ where, for each $i$, $a_i$ is a combination of $q_1,\dots,q_i$ and $q_i$ is a combination of $a_1,\dots,a_i$. If $a_1,\dots,a_{j-1}$ are independent but $a_1,\dots,a_j$ are dependent, it detects this and stops. It finds the first vector that is a combination of the previous ones.

**Algorithm 5.1.** Given $n$-vectors $a_1,\dots,a_k$; for $i=1,\dots,k$:
1. *Orthogonalization:* $\tilde q_i=a_i-(q_1^Ta_i)q_1-\cdots-(q_{i-1}^Ta_i)q_{i-1}$.
2. *Test:* if $\tilde q_i=0$, quit.
3. *Normalization:* $q_i=\tilde q_i/\|\tilde q_i\|$.

For $i=1$, $\tilde q_1=a_1$. If it never quits, the $a$'s are independent. If it quits with $\tilde q_j=0$, they are dependent, and $a_j$ is a combination of $a_1,\dots,a_{j-1}$ (p. 97). Figure 5.3 shows two 2-vectors: $\tilde q_2$ is $a_2$ minus a multiple of $q_1$, namely $(q_1^Ta_2)q_1$, and is orthogonal to $q_1$ (p. 98).

**Analysis (p. 99).** Assume $a_1,\dots,a_k$ are independent. For each $i$ we show: (1) $\tilde q_i\neq0$; (2) $q_1,\dots,q_i$ are orthonormal; (3) $a_i$ is a combination of $q_1,\dots,q_i$; (4) $q_i$ is a combination of $a_1,\dots,a_i$. Induction:
- *$i=1$.* $a_1\neq0$ by independence, so $\tilde q_1\ne0$. A single unit vector is orthonormal. $a_1=\|\tilde q_1\|q_1$ and $q_1=(1/\|\tilde q_1\|)a_1$.
- *(1) for $i$.* If $\tilde q_i=0$, then $a_i$ is a combination of $q_1,\dots,q_{i-1}$. By hypothesis each of these is a combination of $a_1,\dots,a_{i-1}$. Then $a_i$ depends on $a_1,\dots,a_{i-1}$, a contradiction.
- *(2) for $i$.* For $j<i$, using step 1 and orthonormality of the earlier $q$'s: $q_j^T\tilde q_i=q_j^Ta_i-(q_1^Ta_i)(q_j^Tq_1)-\cdots-(q_{i-1}^Ta_i)(q_j^Tq_{i-1})=q_j^Ta_i-q_j^Ta_i=0$. Since $q_i=\tilde q_i/\|\tilde q_i\|$, $q_i\perp q_j$.
- *(3), (4).* $a_i=\tilde q_i+\sum_{j<i}(q_j^Ta_i)q_j=\sum_{j<i}(q_j^Ta_i)q_j+\|\tilde q_i\|q_i$. Also $\tilde q_i$ is a combination of $a_i,q_1,\dots,q_{i-1}$, and each earlier $q$ is a combination of $a_1,\dots,a_{i-1}$. So $q_i$ is a combination of $a_1,\dots,a_i$.

**Completion implies independence (pp. 99–100).** Suppose $\beta_1a_1+\cdots+\beta_ka_k=0$ (5.6) after a run with no early stop. Each of $a_1,\dots,a_{k-1}$ is a combination of $q_1,\dots,q_{k-1}$, so $q_k^Ta_1=\cdots=q_k^Ta_{k-1}=0$. Taking the inner product of (5.6) with $q_k$ gives $0=\beta_kq_k^Ta_k=\beta_k\|\tilde q_k\|$. Since $q_k^Ta_k=\|\tilde q_k\|\neq0$, $\beta_k=0$. Repeat the argument down to $\beta_1=0$.

**Early termination (p. 100).** If $\tilde q_j=0$, then $a_j=(q_1^Ta_j)q_1+\cdots+(q_{j-1}^Ta_j)q_{j-1}$. Each $q_i$ is a combination of $a_1,\dots,a_{j-1}$ (conclusion 4). So $a_j$ is a combination of $a_1,\dots,a_{j-1}$ (a combination of combinations; exercise 1.18). Thus $a_1,\dots,a_j$ are dependent, and so is the larger list $a_1,\dots,a_k$. Gram–Schmidt therefore decides dependence or independence.

**Example (pp. 100–101).** $a_1=(-1,1,-1,1)$, $a_2=(-1,3,-1,3)$, $a_3=(1,3,5,7)$.
- $i=1$: $\|\tilde q_1\|=2$, $q_1=(-1/2,1/2,-1/2,1/2)$.
- $i=2$: $q_1^Ta_2=4$, $\tilde q_2=a_2-4q_1=(1,1,1,1)$, $\|\tilde q_2\|=2$, $q_2=(1/2,1/2,1/2,1/2)$.
- $i=3$: $q_1^Ta_3=2$, $q_2^Ta_3=8$, $\tilde q_3=a_3-2q_1-8q_2=(-2,-2,2,2)$, $\|\tilde q_3\|=4$, $q_3=(-1/2,-1/2,1/2,1/2)$.

No early stop, so $a_1,a_2,a_3$ are independent.

**Uses (p. 101).**
- *Is $b$ a combination of independent $a_1,\dots,a_k$?* Run the algorithm on $a_1,\dots,a_k,b$. It cannot stop in the first $k$ steps, since the $a_i$ are assumed independent. It stops at step $k+1$ ($\tilde q_{k+1}=0$) if $b$ is a combination of them, and does not stop ($\tilde q_{k+1}\neq0$) otherwise.
- *Is $a_1,\dots,a_n$ ($n$-vectors) a basis?* Run the algorithm. Early stop means not a basis. Completion means a basis.

**Complexity (p. 102).** Iteration $i$, step 1:
- $i-1$ inner products of length-$n$ vectors: $(i-1)(2n-1)$ flops;
- $i-1$ scalar multiplications: $n(i-1)$ flops;
- $i-1$ vector subtractions: $n(i-1)$ flops.

The total is $(4n-1)(i-1)$. Step 3 takes about $2n$ flops for the norm plus $n$ divisions. So iteration $i$ costs $(4n-1)(i-1)+3n$. Summing over $i=1,\dots,k$, with $\sum_{i=1}^k(i-1)=1+\cdots+(k-1)=k(k-1)/2$ (5.7):
$$\sum_{i=1}^k\big((4n-1)(i-1)+3n\big)=(4n-1)\frac{k(k-1)}2+3nk\approx 2nk^2 .$$
The complexity is $2nk^2$ (order $nk^2$): linear in $n$, quadratic in $k$. For $k=n$ it is $2n^3$. For 1000 vectors of length 1000, about $2\times10^9$ flops, on the order of one second on a modern computer. Gauss's pairing argument for (5.7) with $k$ odd: pair first with last, second with second-to-last; each pair sums to $k$; there are $(k-1)/2$ pairs. The text calls the attribution to Gauss an anecdote ("famous anecdote alleges").

**Modified Gram–Schmidt (p. 102).** Typically used in practice. It gives the same results but is less sensitive to floating-point round-off. The book does not treat round-off.

## Toy example (ours)
Run Gram–Schmidt on $a_1=(1,1,0)$, $a_2=(1,0,1)$, $a_3=(2,1,1)$. Here $n=3$ and $k=3$.
- $i=1$: $\tilde q_1=a_1$, $\|\tilde q_1\|=\sqrt2$, $q_1=(1,1,0)/\sqrt2$.
- $i=2$: $q_1^Ta_2=1/\sqrt2$. Then $(q_1^Ta_2)q_1=\tfrac1{\sqrt2}\cdot\tfrac{(1,1,0)}{\sqrt2}=(1/2,1/2,0)$. So $\tilde q_2=(1,0,1)-(1/2,1/2,0)=(1/2,-1/2,1)$. Its norm is $\sqrt{1/4+1/4+1}=\sqrt{3/2}$, so $q_2=\tilde q_2/\sqrt{3/2}$.
- $i=3$: $q_1^Ta_3=(2+1+0)/\sqrt2=3/\sqrt2$, so $(q_1^Ta_3)q_1=(3/2,3/2,0)$. Also $\tilde q_2^Ta_3=1-1/2+1=3/2$, so $q_2^Ta_3=(3/2)/\sqrt{3/2}=\sqrt{3/2}$, and $(q_2^Ta_3)q_2=\tilde q_2=(1/2,-1/2,1)$. Then $\tilde q_3=(2,1,1)-(3/2,3/2,0)-(1/2,-1/2,1)=(0,0,0)$.

The algorithm quits at $i=3$: $a_1,a_2,a_3$ are dependent, with $a_3=a_1+a_2$, a combination of earlier vectors. As in the text, the first dependent vector is found.

## Concepts
- [[linear combination]] — weighted sum of vectors; coefficients may be unique or not (p. 89)
- [[linear independence]] — only all-zero coefficients give the zero vector, (5.1); equivalent to unique coefficients (pp. 89–91)
- [[basis]] — here, $n$ independent $n$-vectors; each $n$-vector has a unique expansion (p. 92)
- [[dimension]] — only hinted: the independence-dimension inequality ($k\le n$); no general definition given (p. 91)
- [[independence-dimension-inequality]] (new) — independent $n$-vectors number at most $n$ (p. 91)
- [[orthogonality]] — $a_i\perp a_j$ for $i\neq j$; used for orthogonal and orthonormal lists (p. 95)
- [[orthonormal basis / orthogonal matrix]] — only the orthonormal-basis part appears: orthonormal $n$-vectors form a basis (p. 96)
- [[orthonormal-expansion-formula]] (new) — $x=\sum(a_i^Tx)a_i$ (5.5) (p. 96)
- [[Gram–Schmidt and QR]] — only the Gram–Schmidt algorithm appears; QR is not mentioned (p. 97)
- [[net-present-value]] (new) — $c_1+c_2/(1+r)+\cdots$, shown to be the first expansion coefficient (p. 94)
- [[flop-count-complexity]] (new) — operation count; Gram–Schmidt is about $2nk^2$ (p. 102)

## Canonical instances
- [[standard-unit-vectors]] — $e_1,\dots,e_n$ are independent, orthonormal and a basis (pp. 90, 93, 95)
- [[single-period-loans-basis]] — $e_1,l_1,\dots,l_{n-1}$ are a basis for cash flows, and $\alpha_1$ is the NPV (pp. 93–94)
- [[orthonormal-basis-example-5-3]] — a 3-vector orthonormal basis used to expand $(1,2,3)$ (pp. 95–97)
- [[gram-schmidt-4-vector-example]] — three 4-vectors orthonormalized, with no early stop (pp. 100–101)

## Bridges (candidates)
- [structural-analogy] Unique coefficients in a basis ↔ linear-algebra: injectivity of a map $\beta\mapsto\sum\beta_ia_i$ — independence means this map never sends two coefficient lists to the same vector.
- [structural-analogy] Early stop of Gram–Schmidt ↔ rank: it finds the first vector that adds no new direction (canon link; rank is not stated in this unit).
- [metaphor] Expansion coefficients $a_i^Tx$ ↔ projection: each coefficient measures $x$'s alignment with $a_i$ (canon link; projection is not stated in this unit).
- [same-math] Orthonormal expansion $x=\sum(a_i^Tx)a_i$ ↔ linear-algebra: coordinates in an orthonormal basis (canon link; not stated in this unit).

## Questions this raises
- The text promises later methods to compute expansion coefficients in a general (non-orthonormal) basis, e.g. $0.6513$ and $-0.7280$ for $b=(1,1)$. How are they found?
- Gram–Schmidt checks independence exactly. How does round-off in floating point affect the zero test $\tilde q_i=0$? The text mentions only the modified algorithm.
- Is "at most $n$" the only constraint on independent lists? Can the same count be tied to a general definition of dimension?
- In data settings, with many more vectors than coordinates (exercise 5.2), what does exact dependence imply?

## Exercises worth doing
- Ex. 5.1 (p. 103) — stacking vectors: when does independence or dependence of the tops transfer to stacked vectors? — difficulty: easy
- Ex. 5.3 (p. 103) — find all coefficients of a cash flow in the loan basis; verify $\alpha_1$ is the NPV — difficulty: medium
- Ex. 5.5 (p. 103) — find $\gamma$ with $(a-\gamma b)\perp b$; this is the Gram–Schmidt orthogonalization step — difficulty: easy
- Ex. 5.6 (p. 103) — run Gram–Schmidt on $a_i$ with first $i$ entries one; is it a basis? — difficulty: medium
- Ex. 5.8 (p. 104) — what must be true after early termination at iteration 5? Tests the logic of the stopping rule — difficulty: medium
- Ex. 5.9 (p. 104) — scaling of running time with $n$ and $k$ via $2nk^2$ — difficulty: easy

## Reading notes
- Printed page = pdf − 10 (pdf 99 = printed 89). Printed numbers are given in the page labels.
- Page 99 reads "we subtract from $a_i$ a linear combination of $q_1,\dots,q_{i-1}$ that ensures $q_i\perp\tilde q_j$ for $j<i$". The intended statement seems to be $\tilde q_i\perp q_j$. This looks like a misprint, since the preceding computation shows $q_j^T\tilde q_i=0$.
- Page 93 prints "n standard unit n vectors" (missing hyphen).
- The text layer was garbled in the cash-flow vector, (5.2) and the Gram–Schmidt example; these were checked against the page images.
- Exercises 5.1–5.9 have no solutions printed here; none are solved above. Exercise 5.3 refers to NPV "defined on page 22", and the early-termination argument (p. 100) cites exercise 1.18; both are outside this unit.
