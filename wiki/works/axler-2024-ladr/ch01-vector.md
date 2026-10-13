---
id: axler-2024-ladr/ch01-vector
work: axler-2024-ladr
unit: "1 Vector Spaces"
pages: 1-26
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Vector Spaces (Axler, Chapter 1)

## L0 — One line
A vector space is any set with addition and scalar multiplication obeying a short list of algebraic rules; subspaces, sums and direct sums are the basic ways to build and split such spaces.

## L1 — The gist (≤ 120 words)
The chapter asks what structure of $\mathbf{R}^n$ and $\mathbf{C}^n$ is really needed to do linear algebra. Axler starts with complex numbers, then $\mathbf{F}^n$ ($\mathbf{F}$ is $\mathbf{R}$ or $\mathbf{C}$). He abstracts the properties of $\mathbf{F}^n$ into the definition of a vector space. Examples include sequences and function spaces. From the rules he proves that the zero vector and additive inverses are unique, and that $0v=0$, $a0=0$ and $(-1)v=-v$. A subset is a subspace if it contains 0 and is closed under addition and scalar multiplication. Sums of subspaces are the smallest subspaces containing the summands. A sum is direct when every vector has exactly one decomposition. For two subspaces, this holds iff they meet only in $\{0\}$.

**Prerequisites:** sets, functions, subsets; real-number arithmetic; reading "for all / there exists" statements; proofs by chaining equalities.

## L2 — Key ideas (5–10 bullets)
- Complex numbers are pairs $(a,b)=a+bi$ with $i^2=-1$. They obey the same field-type rules as real numbers (1.3). The book works over $\mathbf{F}\in\{\mathbf{R},\mathbf{C}\}$, so each theorem covers both (p. 2–4).
- $\mathbf{F}^n$ is the set of length-$n$ lists, with coordinatewise addition and scalar multiplication. It generalizes the plane and space, and pictures in $\mathbf{R}^2$ only aid intuition (p. 6–9).
- A vector space is a set with an addition and a scalar multiplication satisfying commutativity, associativity, additive identity, additive inverse, multiplicative identity and distributivity (1.20). Elements may be lists, sequences, functions or other objects (p. 12–14).
- The rules alone force uniqueness of $0$ and of inverses, and $0v=0$, $a0=0$, $(-1)v=-v$ (1.26–1.32). The distributive property is the only rule linking addition to scalar multiplication (p. 14–16).
- Subspace test (1.34): a subset $U$ of $V$ is a subspace iff $0\in U$ and $U$ is closed under addition and scalar multiplication. This yields many examples, including calculus ones (p. 18–19).
- The sum $V_1+\cdots+V_m$ is the smallest subspace containing every $V_k$ (1.40). It plays the role that union plays for subsets (p. 19–21).
- A sum is direct when each vector has a unique decomposition. Equivalently, $0$ has only the trivial decomposition (1.45) (p. 21–23).
- For two subspaces: $U+W$ is direct iff $U\cap W=\{0\}$ (1.46). For three or more, pairwise intersections $\{0\}$ are not enough (Example 1.44) (p. 22–24).

## L3 — Walkthrough

### 1A $\mathbf{R}^n$ and $\mathbf{C}^n$

**Complex numbers.** Complex numbers were invented to take square roots of negative numbers: assume a square root of $-1$, called $i$, obeying the usual arithmetic (p. 2).

*Definition 1.1.* A complex number is an ordered pair $(a,b)$ with $a,b\in\mathbf{R}$, written $a+bi$. $\mathbf{C}=\{a+bi : a,b\in\mathbf{R}\}$. For $a,b,c,d\in\mathbf{R}$ (p. 2):
$$(a+bi)+(c+di)=(a+c)+(b+d)i,$$
$$(a+bi)(c+di)=(ac-bd)+(ad+bc)i.$$
A real $a$ is identified with $a+0i$, so $\mathbf{R}\subseteq\mathbf{C}$. The product formula comes from pretending $i^2=-1$ and using ordinary arithmetic. One can then check $i^2=-1$. The author says not to memorize it (p. 2).

*Example 1.2.* $(2+3i)(4+5i)=2\cdot4+2\cdot5i+3i\cdot4+(3i)(5i)=8+10i+12i-15=-7+22i$ (p. 2).

*1.3 Properties of complex arithmetic* (p. 3), for $\alpha,\beta,\lambda\in\mathbf{C}$:
- commutativity: $\alpha+\beta=\beta+\alpha$, $\alpha\beta=\beta\alpha$;
- associativity: $(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)$, $(\alpha\beta)\lambda=\alpha(\beta\lambda)$;
- identities: $\lambda+0=\lambda$, $\lambda 1=\lambda$;
- additive inverse: for every $\alpha$ there is a unique $\beta$ with $\alpha+\beta=0$;
- multiplicative inverse: for every $\alpha\ne0$ there is a unique $\beta$ with $\alpha\beta=1$;
- distributivity: $\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$.

These follow from real-number properties and the definitions. Example 1.4 proves commutativity of multiplication. With $\alpha=a+bi$, $\beta=c+di$: $\alpha\beta=(ac-bd)+(ad+bc)i$ and $\beta\alpha=(ca-db)+(cb+da)i$. These are equal by commutativity of real addition and multiplication (p. 3). The other proofs are exercises.

*Definition 1.5.* $-\alpha$ is the unique number with $\alpha+(-\alpha)=0$. Subtraction: $\beta-\alpha=\beta+(-\alpha)$. For $\alpha\neq0$, $1/\alpha$ is the unique number with $\alpha(1/\alpha)=1$. Division: $\beta/\alpha=\beta(1/\alpha)$ (p. 4).

*Notation 1.6.* $\mathbf{F}$ stands for $\mathbf{R}$ or $\mathbf{C}$. A theorem about $\mathbf{F}$ holds for both. Elements of $\mathbf{F}$ are called scalars. For $\alpha\in\mathbf{F}$ and positive integer $m$, $\alpha^m$ is the product of $m$ copies of $\alpha$. Hence $(\alpha^m)^n=\alpha^{mn}$ and $(\alpha\beta)^m=\alpha^m\beta^m$ (p. 4).

> **Intuition note.** The rules in 1.3 are what let us calculate with scalars as with ordinary numbers. Because $\mathbf{R}$ and $\mathbf{C}$ share them, one proof can serve both.

**Lists.** $\mathbf{R}^2=\{(x,y):x,y\in\mathbf{R}\}$ (a plane) and $\mathbf{R}^3=\{(x,y,z):x,y,z\in\mathbf{R}\}$ (space) (1.7, p. 5).

*Definition 1.8.* A list of length $n$ ($n$ a nonnegative integer) is an ordered collection of $n$ elements. Two lists are equal iff they have the same length and the same elements in the same order. Every list has finite length, so $(x_1,x_2,\dots)$ is not a list. The empty list $( )$ is a list of length 0, allowed so that theorems have no trivial exceptions (p. 5).

Lists differ from sets: order and repetition matter for lists, not for sets (1.9). $(3,5)\ne(5,3)$ but $\{3,5\}=\{5,3\}$. $(4,4)\ne(4,4,4)$ but $\{4,4\}=\{4,4,4\}=\{4\}$ (p. 5).

**$\mathbf{F}^n$.** Fix a positive integer $n$ (1.10).

*Definition 1.11.* $\mathbf{F}^n=\{(x_1,\dots,x_n):x_k\in\mathbf{F}\text{ for }k=1,\dots,n\}$. $x_k$ is the $k$th coordinate. For $\mathbf{F}=\mathbf{R}$ and $n=2,3$ this agrees with 1.7. Example 1.12: $\mathbf{C}^4$ is the set of lists of four complex numbers (p. 6).

For $n\ge4$ we cannot visualize $\mathbf{R}^n$, but algebra works as easily as in $\mathbf{R}^2$ (p. 6).

*Definition 1.13.* Addition in $\mathbf{F}^n$:
$$(x_1,\dots,x_n)+(y_1,\dots,y_n)=(x_1+y_1,\dots,x_n+y_n).$$

*1.14 Commutativity of addition in $\mathbf{F}^n$.* If $x,y\in\mathbf{F}^n$ then $x+y=y+x$.
Proof (p. 7): write $x=(x_1,\dots,x_n)$, $y=(y_1,\dots,y_n)$.
$$x+y=(x_1+y_1,\dots,x_n+y_n)=(y_1+x_1,\dots,y_n+x_n)=y+x.$$
The first and last equalities use the definition of addition. The middle one uses commutativity in $\mathbf{F}$. The author advises using single letters and avoiding explicit coordinates when possible (p. 7).

*Notation 1.15.* $0=(0,\dots,0)\in\mathbf{F}^n$. The symbol $0$ has two meanings, a list and a number. Context decides (Example 1.16: in $x+0=x$ the $0$ is the list) (p. 7).

**Pictures in $\mathbf{R}^2$** (p. 8). A point $(x,y)$ can be seen as an arrow from the origin to $(x,y)$, called a vector. An arrow moved parallel to itself is the same vector. To add $x$ and $y$, move $y$ so its start is at the end of $x$. The sum is the arrow from the start of $x$ to the end of $y$. The author warns that pictures are aids, not substitutes. Elements of high-dimensional spaces are rigorously defined, for example $(2,-3,17,\pi,\sqrt2)\in\mathbf{R}^5$. Models with variables $x_1,\dots,x_{5000}$ live in $\mathbf{R}^{5000}$, which is handled algebraically (p. 8).

*Definition 1.17.* For $x\in\mathbf{F}^n$, the additive inverse $-x$ satisfies $x+(-x)=0$. So $-x=(-x_1,\dots,-x_n)$. In $\mathbf{R}^2$, $-x$ has the same length as $x$ and the opposite direction (p. 9).

Coordinatewise multiplication of two vectors is possible but "not useful for our purposes". Scalar multiplication is central instead (p. 9).

*Definition 1.18.* For $\lambda\in\mathbf{F}$: $\lambda(x_1,\dots,x_n)=(\lambda x_1,\dots,\lambda x_n)$. In $\mathbf{R}^2$ with $\lambda>0$, $\lambda x$ points the same way as $x$ and has $\lambda$ times its length. With $\lambda<0$, it points the opposite way with length $|\lambda|$ times that of $x$ (p. 9). Scalar multiplication takes a scalar and a vector and gives a vector. The dot product takes two vectors and gives a scalar, and it returns in Chapter 6 (p. 9).

> **Intuition note.** In $\mathbf{F}^n$ everything is done one coordinate at a time. Adding is "tip to tail" and scaling is stretching or flipping. The abstract definition in 1B keeps just these behaviours.

**Digression on fields** (p. 10). A field is a set containing at least two distinct elements $0$ and $1$, with addition and multiplication satisfying all properties in 1.3. Examples: $\mathbf{R}$, $\mathbf{C}$, the rationals, and $\{0,1\}$ with $1+1=0$. The book deals only with $\mathbf{R}$ and $\mathbf{C}$. Many definitions, theorems and proofs work without change for arbitrary fields; if you prefer, you can think of $\mathbf{F}$ as an arbitrary field throughout much of the book, except in the inner-product chapters (6 and 7). Where a result assumes $\mathbf{F}=\mathbf{C}$, one can probably assume instead that $\mathbf{F}$ is algebraically closed, meaning every nonconstant polynomial over $\mathbf{F}$ has a zero. A few results need $1+1\ne0$ (p. 10).

### 1B Definition of Vector Space

The definition is motivated by $\mathbf{F}^n$: addition is commutative and associative and has an identity. Every element has an inverse. Scalar multiplication is associative, and 1 acts as expected. Distributive properties link the two operations (p. 12).

*Definition 1.19.* An addition on a set $V$ is a function assigning $u+v\in V$ to each pair $u,v\in V$. A scalar multiplication on $V$ assigns $\lambda v\in V$ to each $\lambda\in\mathbf{F}$ and $v\in V$ (p. 12).

*Definition 1.20 (vector space).* A set $V$ with an addition and a scalar multiplication such that (p. 12):
- commutativity: $u+v=v+u$ for all $u,v\in V$;
- associativity: $(u+v)+w=u+(v+w)$ and $(ab)v=a(bv)$ for all $u,v,w\in V$ and $a,b\in\mathbf{F}$;
- additive identity: there is $0\in V$ with $v+0=v$ for all $v\in V$;
- additive inverse: for each $v\in V$ there is $w\in V$ with $v+w=0$;
- multiplicative identity: $1v=v$ for all $v\in V$;
- distributive properties: $a(u+v)=au+av$ and $(a+b)v=av+bv$.

Elements of $V$ are called vectors or points (1.21). Since scalar multiplication depends on $\mathbf{F}$, we say "vector space over $\mathbf{F}$". Over $\mathbf{R}$ it is a real vector space, over $\mathbf{C}$ a complex vector space (1.22). $\mathbf{F}^n$ is a vector space over $\mathbf{F}$ (to be verified by the reader). $\{0\}$ is the simplest vector space (p. 13).

*Example 1.23 ($\mathbf{F}^\infty$).* The set of all sequences $(x_1,x_2,\dots)$ of elements of $\mathbf{F}$, with termwise addition and scalar multiplication. It is a vector space over $\mathbf{F}$ (to be verified), and its additive identity is the all-zeros sequence (p. 13).

*Notation 1.24 ($\mathbf{F}^S$).* For a set $S$, $\mathbf{F}^S$ is the set of functions $S\to\mathbf{F}$, with $(f+g)(x)=f(x)+g(x)$ and $(\lambda f)(x)=\lambda f(x)$ for all $x\in S$. For example, $\mathbf{R}^{[0,1]}$ is the set of real-valued functions on $[0,1]$ (p. 13–14).

*Example 1.25.* For nonempty $S$, $\mathbf{F}^S$ is a vector space over $\mathbf{F}$. Its additive identity is the function $0(x)=0$. The additive inverse of $f$ is $(-f)(x)=-f(x)$ (p. 14).

$\mathbf{F}^n$ is $\mathbf{F}^{\{1,\dots,n\}}$, since $(x_1,\dots,x_n)$ is a function $x$ with $x(k)=x_k$. Likewise $\mathbf{F}^\infty=\mathbf{F}^{\{1,2,\dots\}}$. In general, vector-space elements may be lists, functions, or "weird objects" (p. 14).

> **Intuition note.** The definition says nothing about arrows or coordinates, only about how to add and scale. So anything with those two operations obeying the rules, such as a function space, gets all the theorems proved here.

*1.26 Unique additive identity.* A vector space has a unique additive identity.
Proof: if $0$ and $0'$ are identities, then $0'=0'+0=0+0'=0$. The first equality uses that $0$ is an identity, the second is commutativity, and the third uses that $0'$ is an identity (p. 14).

*1.27 Unique additive inverse.* Every element has a unique additive inverse.
Proof: let $w,w'$ both be inverses of $v$. Then $w=w+0=w+(v+w')=(w+v)+w'=0+w'=w'$ (p. 15).

*Notation 1.28.* $-v$ is the additive inverse of $v$, and $w-v:=w+(-v)$. *Notation 1.29:* from now on $V$ denotes a vector space over $\mathbf{F}$ (p. 15).

*1.30 The number 0 times a vector.* $0v=0$ for every $v\in V$ (scalar $0$ on the left, vector $0$ on the right).
Proof: $0v=(0+0)v=0v+0v$. Adding the additive inverse of $0v$ to both sides gives $0=0v$ (p. 15). The distributive property must be used, because it is the only rule connecting addition and scalar multiplication (p. 15).

*1.31 A number times the vector 0.* $a0=0$ for every $a\in\mathbf{F}$.
Proof: $a0=a(0+0)=a0+a0$. Adding the inverse of $a0$ to both sides gives $0=a0$ (p. 16).

*1.32 The number $-1$ times a vector.* $(-1)v=-v$ for every $v\in V$.
Proof: $v+(-1)v=1v+(-1)v=(1+(-1))v=0v=0$. So $(-1)v$ is the additive inverse of $v$ (p. 16). (added step: uniqueness of the inverse is 1.27.)

> **Intuition note.** From the rules in the definition alone you can derive facts that look obvious in $\mathbb{R}^n$, such as "zero times anything is zero". Each proof is a short chain of rule applications.

### 1C Subspaces

*Definition 1.33.* A subset $U$ of $V$ is a subspace of $V$ if $U$ is also a vector space with the same additive identity, addition and scalar multiplication as on $V$ (p. 18).

*1.34 Conditions for a subspace.* A subset $U$ of $V$ is a subspace iff (i) $0\in U$; (ii) $u,w\in U\Rightarrow u+w\in U$; (iii) $a\in\mathbf{F}$, $u\in U\Rightarrow au\in U$.
Proof (p. 18):
- ($\Rightarrow$) holds by the definition of vector space.
- ($\Leftarrow$) Condition (i) puts the identity of $V$ in $U$. Conditions (ii) and (iii) make the operations well defined on $U$. For $u\in U$, $-u=(-1)u$ (by 1.32) lies in $U$ by (iii), so inverses exist in $U$. The remaining rules (associativity, commutativity and so on) hold on $U$ because they hold on $V$.

Condition (i) can be replaced by "$U$ is nonempty", since multiplying a member by $0$ gives $0\in U$. Usually the quickest way to show nonemptiness is to show $0\in U$ (p. 18).

*Example 1.35* (p. 19; the reader verifies):
- (a) For $b\in\mathbf{F}$, $\{(x_1,x_2,x_3,x_4)\in\mathbf{F}^4: x_3=5x_4+b\}$ is a subspace iff $b=0$.
- (b) The continuous real functions on $[0,1]$ form a subspace of $\mathbf{R}^{[0,1]}$.
- (c) The differentiable real functions on $\mathbf{R}$ form a subspace of $\mathbf{R}^{\mathbf{R}}$.
- (d) The differentiable real functions $f$ on $(0,3)$ with $f'(2)=b$ form a subspace of $\mathbf{R}^{(0,3)}$ iff $b=0$.
- (e) The sequences of complex numbers with limit 0 form a subspace of $\mathbf{C}^\infty$.

Checking (b) uses "a sum of continuous functions is continuous". Checking (d) uses $(cf)'=cf'$ (p. 19).

$\{0\}$ is the smallest subspace of $V$ and $V$ the largest. The empty set is not a subspace, since a subspace must contain an additive identity (p. 19). The author states that the subspaces of $\mathbf{R}^2$ are precisely $\{0\}$, lines through the origin, and $\mathbf{R}^2$. Those of $\mathbf{R}^3$ are precisely $\{0\}$, lines through the origin, planes through the origin, and $\mathbf{R}^3$. Showing these are subspaces is straightforward. Showing there are no others is deferred to the next chapter (p. 19).

> **Intuition note.** A subspace is a flat piece of $V$ through the origin that you cannot escape by adding or scaling. In Example 1.35(a), the shift $b\ne0$ pushes the set off the origin.

**Sums of subspaces.** The union of subspaces is rarely a subspace (Exercise 12), so sums are used instead (p. 19).

*Definition 1.36.* For subspaces $V_1,\dots,V_m$ of $V$:
$$V_1+\cdots+V_m=\{v_1+\cdots+v_m : v_1\in V_1,\dots,v_m\in V_m\}.$$

*Example 1.37.* In $\mathbf{F}^3$, with $U=\{(x,0,0):x\in\mathbf{F}\}$ and $W=\{(0,y,0):y\in\mathbf{F}\}$, $U+W=\{(x,y,0):x,y\in\mathbf{F}\}$ (p. 20).

*Example 1.38.* In $\mathbf{F}^4$, let $U=\{(x,x,y,y):x,y\in\mathbf{F}\}$ and $W=\{(x,x,x,y):x,y\in\mathbf{F}\}$ (p. 20).
- Take $(a,a,b,b)\in U$ and $(c,c,c,d)\in W$. The sum is $(a+c,\,a+c,\,b+c,\,b+d)$, whose first two coordinates are equal. So
$$U+W\subseteq\{(x,x,y,z)\in\mathbf{F}^4: x,y,z\in\mathbf{F}\}.\tag{1.39}$$
- Conversely, for $x,y,z\in\mathbf{F}$: $(x,x,y,z)=(x,x,y,y)+(0,0,0,z-y)$. The first vector is in $U$ and the second is in $W$. Hence equality holds: $U+W$ is the set of vectors whose first two coordinates are equal.

*1.40 Sum of subspaces is the smallest containing subspace.* $V_1+\cdots+V_m$ is the smallest subspace of $V$ containing $V_1,\dots,V_m$.
Proof (p. 21):
- The sum contains $0$ and is closed under addition and scalar multiplication (left to the reader), so it is a subspace by 1.34.
- Each $V_k$ lies in the sum (take sums where all but one $v_j$ are $0$).
- Any subspace containing all the $V_k$ contains all finite sums of their elements, hence contains the sum.

Sums of subspaces are analogous to unions of subsets (smallest containing object) (p. 21).

> **Intuition note.** The sum is everything you can reach by taking one piece from each subspace and adding. Nothing smaller works, and nothing larger is needed.

**Direct sums.**

*Definition 1.41.* $V_1+\cdots+V_m$ is a direct sum if each element can be written in only one way as $v_1+\cdots+v_m$ with $v_k\in V_k$. Then it is written $V_1\oplus\cdots\oplus V_m$ (p. 21).

*Example 1.42.* With $U=\{(x,y,0)\}$ and $W=\{(0,0,z)\}$, $\mathbf{F}^3=U\oplus W$ (p. 21).

*Example 1.43.* Let $V_k$ be the vectors in $\mathbf{F}^n$ whose coordinates are all $0$ except possibly the $k$th. For example $V_2=\{(0,x,0,\dots,0)\}$. Then $\mathbf{F}^n=V_1\oplus\cdots\oplus V_n$ (p. 22).

*Example 1.44 (a sum that is not direct).* In $\mathbf{F}^3$ let $V_1=\{(x,y,0)\}$, $V_2=\{(0,0,z)\}$, $V_3=\{(0,y,y)\}$. Then $\mathbf{F}^3=V_1+V_2+V_3$, because $(x,y,z)=(x,y,0)+(0,0,z)+(0,0,0)$. But it is not direct, since
$$(0,0,0)=(0,1,0)+(0,0,1)+(0,-1,-1)=(0,0,0)+(0,0,0)+(0,0,0),$$
with the three summands in $V_1,V_2,V_3$ respectively in both lines (p. 22).

*1.45 Condition for a direct sum.* $V_1+\cdots+V_m$ is a direct sum iff the only way to write $0=v_1+\cdots+v_m$ with $v_k\in V_k$ is $v_k=0$ for all $k$.
Proof (p. 23):
- ($\Rightarrow$) is immediate from the definition.
- ($\Leftarrow$) Let $v=v_1+\cdots+v_m=u_1+\cdots+u_m$ with $v_k,u_k\in V_k$. Subtracting gives $0=(v_1-u_1)+\cdots+(v_m-u_m)$ with $v_k-u_k\in V_k$. By hypothesis each $v_k-u_k=0$, so $v_k=u_k$.

*1.46 Direct sum of two subspaces.* For subspaces $U,W$ of $V$: $U+W$ is a direct sum $\iff U\cap W=\{0\}$.
Proof (p. 23):
- ($\Rightarrow$) If $v\in U\cap W$, then $0=v+(-v)$ with $v\in U$, $-v\in W$. By uniqueness of the representation of $0$, $v=0$.
- ($\Leftarrow$) Suppose $u\in U$, $w\in W$, $0=u+w$. Then $u=-w\in W$, so $u\in U\cap W=\{0\}$. Thus $u=0$, hence $w=0$. By 1.45 the sum is direct.

The two-subspace test does not extend to more subspaces. In 1.44, $V_1\cap V_2=V_1\cap V_3=V_2\cap V_3=\{0\}$, yet the sum is not direct (p. 24). Direct sums are analogous to disjoint unions of subsets. Two subspaces can never be disjoint, since both contain $0$. For two subspaces, disjointness is replaced by "intersection equals $\{0\}$" (p. 24).

> **Intuition note.** "Direct" means the pieces do not duplicate each other, so each vector splits in exactly one way (for two pieces this means they overlap only in $\{0\}$; for more pieces, pairwise overlap tests are not enough, see 1.44). Checking that $0$ splits only trivially is enough, because two different splittings of $v$ would give a nontrivial splitting of $0$ by subtraction.

## Toy example
*(Our own, not from the text.)* Work in $\mathbf{R}^2$. Let $U=\{(t,0):t\in\mathbf{R}\}$ (the x-axis) and $W=\{(s,s):s\in\mathbf{R}\}$ (the line $y=x$).

1. Both are subspaces by 1.34. Each contains $(0,0)$. $(t,0)+(t',0)=(t+t',0)\in U$ and $a(t,0)=(at,0)\in U$. The same checks work for $W$.
2. Intersection: $(t,0)=(s,s)$ forces $s=0$ (second coordinate) and $t=s=0$. So $U\cap W=\{(0,0)\}$.
3. By 1.46, $U+W$ is direct. It equals $\mathbf{R}^2$: a general $(p,q)=(p-q,0)+(q,q)$. Check: $(p-q+q,\;0+q)=(p,q)$.
4. For $(3,5)$: $(3-5,0)+(5,5)=(-2,0)+(5,5)=(3,5)$. The decomposition is unique. If $(3,5)=(t,0)+(s,s)$, then $s=5$ and $t+5=3$, so $t=-2$.
5. Non-subspace: $\{(x,y):y=x+1\}$ lacks $(0,0)$, as in 1.35(a) with $b\neq0$.
6. Non-direct triple: take $V_1=U$, $V_2=\{(0,y)\}$, $V_3=W$. Pairwise intersections are $\{(0,0)\}$. For example, $V_1\cap V_3=\{(0,0)\}$ as above. Yet $(0,0)=(1,0)+(0,1)+(-1,-1)$, since $(1,0)+(0,1)=(1,1)$ and $(1,1)+(-1,-1)=(0,0)$. The summands lie in $V_1,V_2,V_3$ respectively and are not all $0$. So the sum is not direct, as in 1.44.

## Concepts
- [[vector-space]] (new) — a set with addition and scalar multiplication over $\mathbf{F}$ satisfying the six rule-groups of 1.20; elements may be lists, sequences or functions (p. 12–14)
- [[vector]] — an element of a vector space; in $\mathbf{R}^2$ also seen as an arrow from the origin (p. 8, 12)
- [[field]] (new) — a set with $0\ne1$, addition and multiplication satisfying 1.3; here $\mathbf{F}$ is $\mathbf{R}$ or $\mathbf{C}$ (p. 4, 10)
- [[scalar]] (new) — an element of $\mathbf{F}$, a "number" as opposed to a vector (p. 4)
- [[complex-numbers]] (new) — pairs $a+bi$ with $i^2=-1$ and the operations of 1.1 (p. 2)
- [[list]] (new) — ordered, finite-length collection; order and repetition matter, unlike sets (p. 5)
- [[subspace]] (new) — subset that is itself a vector space under the same operations; test: $0$, closure under $+$ and scalar multiplication (p. 18)
- [[sum-of-subspaces]] (new) — all sums $v_1+\cdots+v_m$ with $v_k\in V_k$; the smallest subspace containing every $V_k$ (p. 19, 21)
- [[direct-sum]] (new) — a sum in which every vector has exactly one decomposition; for two subspaces, iff intersection is $\{0\}$ (p. 21–23)
- [[additive-identity-and-inverse]] (new) — the unique $0$ and unique $-v$ in any vector space (p. 14–15)
- [[function-space]] (new) — $\mathbf{F}^S$, functions $S\to\mathbf{F}$ with pointwise operations (p. 13–14)

## Canonical instances
- [[instance-Fn]] — $\mathbf{F}^n$ with coordinatewise operations, the model for the abstract definition (p. 6–9, 13)
- [[instance-F-infinity]] — sequence space $\mathbf{F}^\infty$ (p. 13)
- [[instance-FS]] — function space $\mathbf{F}^S$, including $\mathbf{R}^{[0,1]}$ and $\mathbf{R}^{\mathbf{R}}$ (p. 13–14)
- [[instance-subspace-examples-1.35]] — continuous, differentiable and null-limit sequences as subspaces (p. 19)
- [[instance-nondirect-sum-1.44]] — three subspaces of $\mathbf{F}^3$ with pairwise trivial intersection but non-unique decomposition of $0$ (p. 22, 24)
- [[instance-sum-F4-1.38]] — $U+W$ computed by double inclusion (p. 20)

## Bridges (candidates)
- [structural-analogy] Direct sum (unique decomposition) ↔ linear independence (canon link; not stated in this unit): both say that "nothing is redundant", via uniqueness of the representation of $0$.
- [structural-analogy] Sum of subspaces = smallest containing subspace ↔ span (canon link; not stated in this unit): both are "everything reachable by adding".
- [same-math] Function space $\mathbf{F}^S$ ↔ data as vectors in applied settings: a dataset indexed by a finite set $S$ is literally an element of $\mathbf{F}^S$, as $\mathbf{F}^n$ is $\mathbf{F}^{\{1..n\}}$ (p. 14).
- [structural-analogy] Subspace/sum/direct sum ↔ subset/union/disjoint union (the author's own analogy, p. 21, 24).

## Questions this raises
- If the subspaces of $\mathbf{R}^2$ and $\mathbf{R}^3$ are only the listed ones (p. 19), how is that proved with the tools of Chapter 2?
- For three or more subspaces, what condition on the subspaces replaces "pairwise intersections are $\{0\}$"?
- Can every subspace $U$ of $V$ be paired with a $W$ such that $V=U\oplus W$ (see Exercises 1C.20–22)? Is $W$ unique (Exercise 1C.23)?
- Which theorems here really need $\mathbf{F}=\mathbf{R}$ or $\mathbf{C}$, and which hold for any field (p. 10)?

## Exercises worth doing
- Ex. 1B.4 (p. 16) — which vector-space rule the empty set fails; shows why a vector space has at least one element — easy
- Ex. 1B.5 (p. 16) — replacing the additive-inverse axiom by $0v=0$; teaches how axioms interlock — medium
- Ex. 1B.8 (p. 17) — complexification $V_{\mathbf{C}}$ of a real vector space; building a complex vector space from a real one, generalizing $\mathbf{C}^n$ from $\mathbf{R}^n$ — medium
- Ex. 1C.12 (p. 25) — union of two subspaces is a subspace iff one contains the other; explains why sums replace unions — medium
- Ex. 1C.23 (p. 26) — complements are not unique; the book's hint is to experiment in $\mathbf{F}^2$ — medium
- Ex. 1C.24 (p. 26) — $\mathbf{R}^{\mathbf{R}}=V_e\oplus V_o$ (even and odd functions); a direct sum in a function space — hard

## Reading notes
- Printed page = pdf page − 14 (the first page of the chapter is the 15th page of the PDF). Printed page numbers are visible in the page images.
- The text layer shows math italics as garbled glyphs, so every formula here was read from the page images.
- The running header on printed p. 22 reads "≈ 7π" in the image where a page number would be expected. It sits where the page number would be, and the mathematics on the page is unaffected. The page is printed 22 by sequence.
- The "Digression on Fields" statements about arbitrary fields and algebraically closed fields are hedged in the source ("probably", "if you prefer") and are kept hedged above.
- Proofs the author leaves to the reader (1.3 other than 1.4, verification that $\mathbf{F}^n$, $\mathbf{F}^\infty$ and $\mathbf{F}^S$ are vector spaces, parts of 1.35 and 1.40) are not worked out in the source or here.
