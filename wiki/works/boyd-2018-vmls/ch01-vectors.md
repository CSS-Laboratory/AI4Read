---
id: boyd-2018-vmls/ch01-vectors
work: boyd-2018-vmls
unit: "Chapter 1 — Vectors"
pages: 3–28
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Vectors (Boyd & Vandenberghe, Ch. 1)

## L0 — One line
A vector is an ordered list of numbers, and four operations (addition, scaling, linear combination, inner product) already turn lists of numbers into a working language for positions, portfolios, images, text and cash flows, at a cost of order n flops (floating point operations) per operation.

## L1 — The gist (≤ 120 words)
This chapter introduces vectors, which are ordered lists of numbers, and their basic operations: addition, multiplication by a number, linear combinations (scaled vectors added together) and the inner product (multiply matching entries, then add). It shows that these simple operations take concrete meanings in many settings, such as positions, colors, portfolios, images, word counts and cash flows. For example, the inner product of a price vector and a quantity vector is a total cost. The chapter also counts the arithmetic cost in flops (floating point operations, i.e. single additions or multiplications): addition and scaling take about n flops, the inner product about 2n, and sparse vectors (many zero entries) need fewer. It ends with exercises.

**Prerequisites:** high-school algebra (sums, indices, simple equations); the idea of a function and of a coordinate plane. No matrices are needed.

## L2 — Key ideas (5–10 bullets)
- A vector is an ordered finite list of numbers. Its size is the number of entries, and two vectors are equal exactly when the sizes match and every entry matches (p. 3).
- Special vectors: the zero vector, the unit vectors $e_i$, the ones vector $\mathbf 1$, block (stacked) vectors and slices. The same symbol can mean different things (overloading), so context must fix the size (pp. 4–5).
- Addition and scalar multiplication act entry by entry. Their algebraic laws (commutative, associative, distributive) can be derived by checking one entry at a time; the book shows this for commutativity of addition (pp. 11–16).
- A linear combination $\beta_1a_1+\dots+\beta_ma_m$ is the central construction. Every vector is a linear combination of unit vectors, and the special cases (sum, average, affine, convex) are named by conditions on the coefficients (p. 17).
- Lines and segments between two vectors are affine and convex combinations $(1-\theta)a+\theta b$, and the idea also makes sense in high dimension, e.g. 100 (p. 18).
- The inner product $a^Tb=\sum a_ib_i$ is commutative, compatible with scaling and distributive over addition. With special vectors it gives sums, averages, picks of entries, counts, costs, expected values, polynomial values and discounted totals (pp. 19–22).
- Complexity is counted in flops: $n$ for scaling and addition, $2n-1$ (simplified to $2n$) for the inner product. Flop counts are only rough predictors of time (pp. 22–24).
- For sparse vectors the flop count is bounded in terms of the number of nonzero entries: $\mathbf{nnz}(x)$ for scaling, at most $\min\{\mathbf{nnz}(x),\mathbf{nnz}(y)\}$ for a sum and twice that for an inner product. It is zero for a sum or inner product when the nonzero patterns do not overlap (p. 24).

## L3 — Walkthrough

### 1.1 Vectors (pp. 3–11)

**Definition and notation.**
- A *vector* is an ordered finite list of numbers, written as a column (square or round brackets) or as $(-1.1, 0.0, 3.6, -7.2)$ (p. 3).
- The values are the *elements* (entries, coefficients, components). The *size* (dimension, length) is their number. A vector of size $n$ is an *$n$-vector*, and a 1-vector is treated as the same thing as a number (p. 3).
- The $i$th entry of $a$ is $a_i$, with $i=1,\dots,n$ (p. 3).
- $a=b$ means same size and $a_1=b_1,\dots,a_n=b_n$ (p. 3).
- The entries are *scalars*. The book focuses on real scalars ("real vectors"). $\mathbf R$ is the set of reals, and $a\in\mathbf R^n$ means $a$ is a real $n$-vector (p. 4).

**Block (stacked) vectors and subvectors (p. 4).**
- Stacking $b$ ($m$-vector), $c$ ($n$-vector), $d$ ($p$-vector) gives the $(m+n+p)$-vector $a=(b,c,d)$. Scalars can be stacked too: for a 3-vector $a$, $(1,a)$ is a 4-vector.
- *Colon notation*: $a_{r:s}=(a_r,\dots,a_s)$ has size $s-r+1$. So $b=a_{1:m}$, $c=a_{(m+1):(m+n)}$, $d=a_{(m+n+1):(m+n+p)}$. For $z=(1,-1,2,0)$, $z_{2:3}=(-1,2)$.
- The author notes that notation for vectors vs. scalars (Greek letters, bold, arrows) is not standardized, so the reader should be prepared to figure out what is what (p. 4).

**Indexing (p. 5).**
- Vectors are indexed from 1 to $n$ here, unlike many programming languages (from 0 to $n-1$).
- $a_i$ can mean the $i$th entry of a vector $a$ (a number) or the $i$th vector in a list $a_1,\dots,a_k$. Context decides. The $j$th entry of $a_i$ is written $(a_i)_j$.

**Special vectors (p. 5).**
- *Zero vector*: all entries zero, written $0_n$ or just $0$. The size comes from context. Using one symbol for objects of different sizes is called *overloading*.
- *Unit vector* $e_i$: entry $i$ is one, all others zero:
$$(e_i)_j=\begin{cases}1 & j=i\\ 0 & j\neq i.\end{cases}$$
Here $e_i$ is the $i$th unit vector, not the $i$th entry of a vector $e$.
- *Ones vector* $\mathbf 1_n$ (or $\mathbf 1$): all entries one.

**Sparsity (p. 6).** A vector is *sparse* if many of its entries are zero. Its *sparsity pattern* is the set of indices of the nonzero entries. $\mathbf{nnz}(x)$ is the number of nonzero entries. Unit vectors are sparse, and the zero vector is the sparsest possible.

**Examples of what vectors represent (pp. 6–10).** An $n$-vector can hold $n$ similar or very different quantities (p. 6).
- *Location/displacement*: a 2- or 3-vector gives coordinates of a point, or is drawn as an arrow for a displacement, velocity or acceleration (Fig. 1.1, p. 6).
- *Color*: RGB intensities, often in $[0,1]$. $(0,0,0)$ is black, $(0,1,0)$ bright pure green, $(1,0.5,0.5)$ a pink (Fig. 1.2, pp. 6–7).
- *Quantities*: amounts of $n$ resources. Negative entries mean owed or consumed. A *bill of materials* gives the amounts required for a product or task (p. 7).
- *Portfolio*: $s_i$ = shares of asset $i$. $(100,50,20)$ is 100, 50 and 20 shares of assets 1–3. Negative entries are short positions. Dollar values or fractions can be used instead (p. 7).
- *Values across a population*: e.g. blood pressure $b_i$ of patient $i$ (p. 7).
- *Proportions*: nonnegative entries adding to one. This can be read as a mixture recipe, an allocation or probabilities. The uniform mixture of four outcomes is $(1/4,1/4,1/4,1/4)$ (p. 7).
- *Time series/signal*: values at different times, called *samples*. Audio uses equally spaced times (typically 48000 or 44100 per second). Lines joining plotted points carry no information (Fig. 1.3, hourly Los Angeles temperature, 48-vector, p. 8).
- *Daily return*: $(-0.022,+0.014,+0.004)$ means $-2.2\%$, $+1.4\%$, $+0.4\%$ on three trading days. The index counts trading days, so the samples are not evenly spaced in time (p. 8).
- *Cash flow*: positive entries are payments to the entity, negative ones payments by it. $(1000,-10,-10,-10,-1010)$ is a one-year $1000 loan with 1% interest paid each quarter (p. 8).
- *Images*: an $M\times N$ monochrome image is a vector of length $MN$ (grayscale 0 = black, 1 = white), ordered row- or column-wise. Fig. 1.4 shows an 8×8 image as a 64-vector $(0.65, 0.05, 0.20,\dots,0.28,0.00,0.90)$. A color image has length $3MN$ (p. 9).
- *Video*: $K$ monochrome images give a vector of length $KMN$ (p. 9).
- *Word count and histogram*: entry $i$ counts dictionary word $i$ in a document (e.g. $(25,2,0)$). The histogram version gives fractions, so $x_5=0.003$ means 0.3% of words are word 5. Variants of a word are often merged (*stemming*). Very common words (*stop words*) and very rare words are often excluded (pp. 9–10, Fig. 1.5).
- *Customer purchases* $p_i$ (quantity or dollar value of item $i$), with many entries expected to be zero unless $n$ is small (p. 10).
- *Occurrence/subsets*: $o_i\in\{0,1\}$ says whether event $i$ occurred, or whether object $i$ is in a subset. Such vectors are called *Boolean* (p. 10).
- *Feature vector*: $n$ different quantities about one object, e.g. a 6-vector of age, height, weight, blood pressure, temperature, gender (coded 0/1) (p. 10).
- *Entry labels*: a separate list of labels can say what each entry means, e.g. ticker symbols (AAPL, INTC, AMZN) for the portfolio $(100,50,20)$ (p. 11).

> *Intuition note.* In an application each entry of a vector has a meaning, and it is common to keep a separate list of labels saying what each entry stands for; in some cases (such as images) known conventions fix the meaning and order. The same vector operations are then used with very different meanings.

### 1.2 Vector addition (pp. 11–14)

**Definition.**
- Two vectors of the *same size* are added entry by entry, giving the *sum*. Subtraction works the same way and gives the *difference*. The symbol $+$ is overloaded (scalars vs. vectors) (p. 11).
- Examples: $(0,7,3)+(1,2,0)=(1,9,3)$ and $(1,9)-(1,1)=(0,8)$ (p. 11).

**Properties (p. 11).** For vectors $a,b,c$ of the same size:
- $a+b=b+a$ (commutative);
- $(a+b)+c=a+(b+c)$ (associative), so $a+b+c$ is unambiguous;
- $a+0=0+a=a$;
- $a-a=0$.

**Proof method (pp. 11–12).** Each property is shown by working on the $i$th entry. For commutativity, the $i$th entry of $a+b$ is $a_i+b_i$, and that of $b+a$ is $b_i+a_i$. These are equal for every $i$, so $a+b=b+a$ by the definition of vector equality. The authors recommend deriving a few such properties, but not all.

**Interpretations (pp. 12–14).**
- *Displacements*: $a+b$ is the net displacement ("first $a$, then $b$"), and the order does not matter (Fig. 1.6). If $p$ is a position and $a$ a displacement, $p+a$ is the displaced position (Fig. 1.7). For two points, $p-q$ is the displacement from $q$ to $p$ (Fig. 1.8).
- *Word counts*: $a+b$ is the count vector of the two documents combined. $a-b$ says how many more times each word appears in the first document than in the second.
- *Bill of materials*: $q_1+\dots+q_N$ is the bill of materials for completing all $N$ tasks.
- *Market clearing*: $q_i$ lists goods produced (positive) or consumed (negative) by agent $i$; e.g. $(q_5)_4=-3.2$ means agent 5 consumes 3.2 units of resource 4. The sum $s=q_1+\dots+q_N$ is the net surplus (or shortfall). If $s=0$ the market is *closed* and *clears* (p. 14).
- *Audio*: $a+b$ is perceived as both signals at once. *Feature differences*: $d=f-g$ compares two items, e.g. $d_7=0$ means equal in feature 7. *Time series*: e.g. daily profits of two stores add to total profit (monthly rainfall in Fig. 1.9, p. 15). *Portfolio trading*: new portfolio $=s+b$, where $b$ is the trade vector (buys positive, sells negative).

**Computer-language warning (p. 14).** Some languages add a scalar to every entry of a vector, or use $+$ for concatenation, e.g. $(1,2)+(3,4,5)=(1,2,3,4,5)$. The book uses neither. Mathematical notation must be kept separate from software syntax.

### 1.3 Scalar-vector multiplication (pp. 15–19)

**Definition (p. 15).** Multiply every entry by the scalar: $(-2)(1,9,6)=(-2,-18,-12)$. Writing the scalar on the right, $(1,9,6)(1.5)=(1.5,13.5,9)$, means the same thing. $a/2$ means $(1/2)a$. $(-1)a$ is written $-a$. $0\,a=0$ (scalar zero on the left, zero vector on the right).

**Properties (pp. 15–16).** $\alpha a=a\alpha$, and also:
- $(\beta\gamma)a=\beta(\gamma a)$ (associative). We can therefore write $\beta\gamma a$.
- $(\beta+\gamma)a=\beta a+\gamma a$ (left-distributive). The left $+$ adds scalars and the right $+$ adds vectors. Scalar multiplication has higher precedence than addition.
- $a(\beta+\gamma)=a\beta+a\gamma$ (right-distributive).
- $\beta(a+b)=\beta a+\beta b$.

**Examples (p. 16).**
- *Displacement*: $\beta a$ with $\beta>0$ points the same way as $a$ with magnitude scaled by $\beta$. With $\beta<0$ it points the opposite way, scaled by $|\beta|$ (Fig. 1.10, p. 17).
- *Materials*: producing $\alpha\ge0$ units of a product needs $\alpha q$.
- *Audio*: $\beta a$ is the same signal with volume changed by the factor $|\beta|$; $\beta=\pm1/2$ is quieter.

**Linear combinations (p. 17).**
- For $n$-vectors $a_1,\dots,a_m$ and scalars $\beta_1,\dots,\beta_m$, the $n$-vector $\beta_1a_1+\dots+\beta_ma_m$ is a *linear combination*. The $\beta_i$ are its *coefficients*.
- Any $n$-vector $b$ is a linear combination of the standard unit vectors, with its own entries as coefficients:
$$b=b_1e_1+\dots+b_ne_n.\tag{1.1}$$
Example: $(-1,3,5)=(-1)(1,0,0)+3(0,1,0)+5(0,0,1)$.
- Special cases: all $\beta_i=1$ gives the *sum*, and all $\beta_i=1/m$ gives the *average*. If $\beta_1+\dots+\beta_m=1$ the combination is *affine*. If in addition all coefficients are nonnegative it is *convex* (also called a *mixture* or *weighted average*) (p. 17).

> *Intuition note.* A linear combination is "scale each ingredient, then add". Equation (1.1) says the unit vectors are enough ingredients to build every vector of that size. The affine and convex cases are the "recipe adds up to 100%" cases.

**Examples of linear combinations (p. 18).**
- *Displacements*: the sum of scaled displacements, e.g. $b=0.75a_1+1.5a_2$ (Fig. 1.11).
- *Audio mixing*: simultaneous tracks $a_1,\dots,a_m$; the mix $\sum\beta_ia_i$ has relative loudness $|\beta_i|$.
- *Cash flow replication*: with $c_1=(1,-1.1,0)$ (a $1 loan from period 1 to 2 at 10% interest) and $c_2=(0,1,-1.1)$, we get
$$d=c_1+1.1c_2=(1,0,-1.21),$$
a two-period $1 loan with compounded 10% interest. (Added step: $1.1c_2=(0,1.1,-1.21)$, and adding $c_1$ gives $(1,0,-1.21)$.) The two-period loan is "replicated" from two one-period loans.
- *Line and segment*: for different $n$-vectors $a,b$, the affine combination $c=(1-\theta)a+\theta b$ lies on the line through $a$ and $b$. For $0\le\theta\le1$ it is convex and lies on the segment between them. This agrees with ordinary geometry for $n=2,3$, and also makes sense for $n=100$ (Fig. 1.12, p. 19, which shows $\theta=-0.4,\,0.4,\,1.2$).

### 1.4 Inner product (pp. 19–22)

**Definition (p. 19).** For $n$-vectors,
$$a^Tb=a_1b_1+a_2b_2+\dots+a_nb_n .$$
- Other notations the book does not use: $\langle a,b\rangle$, $\langle a|b\rangle$, $(a,b)$, $a\cdot b$. In this book $(a,b)$ is the stacked vector of length $2n$.
- The reason for the superscript T is deferred to chapter 6. The outer product comes in §10.1.
- Example: $(-1,2,2)^T(1,0,-3)=(-1)(1)+(2)(0)+(2)(-3)=-7$. For $n=1$ it is ordinary multiplication.

**Properties (p. 19).** For same-size $a,b,c$ and scalar $\gamma$:
- $a^Tb=b^Ta$;
- $(\gamma a)^Tb=\gamma(a^Tb)$;
- $(a+b)^Tc=a^Tc+b^Tc$.

Combining them gives, e.g., $a^T(b+\gamma c)=a^Tb+\gamma a^Tc$, and
$$(a+b)^T(c+d)=a^Tc+a^Td+b^Tc+b^Td,$$
which is analogous to expanding a product of sums. On the left the two $+$ are vector additions; on the right the three $+$ are scalar additions (pp. 19–20).

**General examples (p. 20).**
- $e_i^Ta=a_i$ (picks out entry $i$).
- $\mathbf 1^Ta=a_1+\dots+a_n$ (sum).
- $(\mathbf 1/n)^Ta=(a_1+\dots+a_n)/n$ is the average, written $\mathbf{avg}(x)$ (traditionally $\mu$).
- $a^Ta=a_1^2+\dots+a_n^2$ (sum of squares).
- If $b$ has entries in $\{0,1\}$, $b^Ta$ is the sum of the entries of $a$ where $b_i=1$.

**Block vectors (p. 20).** If the blocks *conform* (corresponding blocks have the same sizes), $a^Tb=a_1^Tb_1+\dots+a_k^Tb_k$.

**Applications (pp. 20–22).**
- *Co-occurrence*: for 0/1 vectors, $a^Tb$ counts indices where both are 1, i.e. the size of the intersection of the two subsets. With $a=(0,1,1,1,1,1,1)$ and $b=(1,0,1,0,1,0,0)$ (Fig. 1.13): $a^Tb=2$, namely objects 3 and 5.
- *Weights, features, score*: $w^Tf$ is a weighted sum of features. A credit score is one example.
- *Price-quantity*: $p^Tq$ is the total cost.
- *Speed-time*: $s^Tt$ is the total distance when speeds $s_i$ are constant on segments taking times $t_i$.
- *Expected value*: if $p$ is nonnegative with entries summing to one (probabilities of $n$ outcomes) and $f_i$ is the value if outcome $i$ occurs, $f^Tp$ is the expected value.
- *Polynomial evaluation*: for $p(x)=c_1+c_2x+\dots+c_nx^{n-1}$ and $z=(1,t,t^2,\dots,t^{n-1})$, we have $c^Tz=p(t)$.
- *Discounted total*: with cash flow $c$ and $d=(1,1/(1+r),\dots,1/(1+r)^{n-1})$, $r\ge0$,
$$d^Tc=c_1+\frac{c_2}{1+r}+\dots+\frac{c_n}{(1+r)^{n-1}}$$
is the net present value (NPV) at interest rate $r$ (p. 22).
- *Portfolio value*: $p^Ts$ (prices times shares, with shorts negative).
- *Portfolio return*: $r_i=(p_i^{\rm final}-p_i^{\rm initial})/p_i^{\rm initial}$. If $h$ holds dollar values, $r^Th$ is the total return in dollars. If $w$ holds fractional dollar holdings, $r^Tw$ is the fractional return. Example: $r^Tw=0.09$ means 9%, i.e. $900 on $10000 invested.
- *Sentiment*: $x$ is a word histogram, $w_i=1$ for positive words, $-1$ for negative, $0$ for neutral. $w^Tx$ is a crude sentiment measure.

> *Intuition note.* The inner product multiplies matching entries and adds. Choosing the second vector chooses the question being asked: all ones gives a sum, a unit vector picks one entry, 0/1 weights select a subset, and prices give a cost.

### 1.5 Complexity of vector computations (pp. 22–24)

**Computer representation (p. 23).**
- Reals are stored in *floating point* format using 64 bits (8 bytes). Numbers in applications can be approximated to about 10 digits, which is good enough for almost all practical applications. Integers are stored exactly.
- An $n$-vector needs $8n$ bytes, and vectors with millions or billions of entries are easily stored. Sparse vectors are stored by keeping the indices and values of the nonzero entries.
- Each floating point operation rounds the result to the nearest floating point number. This causes *round-off error*, studied in numerical analysis and ignored in this book. Two sides of a mathematical identity may therefore differ slightly on a computer.

**Flops (p. 23).**
- Time estimates come from counting floating point operations (*flops*). Speed is given in Gflop/s, typically 1–10 but varying by orders of magnitude.
- Such estimates are very crude, "not meant to be more accurate than a factor of ten or so" (p. 23). So gross approximations (such as ignoring a factor of 2) are acceptable.
- In this book, the *complexity* of an operation is the number of flops required by a specific method, as a function of input size. Small terms are dropped. This differs from theoretical computer science, where complexity refers to the best possible method.

**Vector operations (p. 24).**
- Scalar multiplication $ax$: $n$ flops. Addition $x+y$: $n$ flops. Inner product $x^Ty$: $n$ multiplications and $n-1$ additions, i.e. $2n-1$ flops, simplified to $2n$.
- A 1 Gflop/s computer should take about a thousandth of a second for an inner product of two vectors of size one million (about $2\times10^6$ flops; added step), though the actual time may differ by a factor of 10.
- The *order* of a computation drops constants multiplying powers of the dimension. All three operations are of order $n$, so an input 10 times bigger should take around 10 times longer.

**Sparse vectors (p. 24).**
- $ax$ needs $\mathbf{nnz}(x)$ flops.
- $x+y$ needs no more than $\min\{\mathbf{nnz}(x),\mathbf{nnz}(y)\}$ flops. If the sparsity patterns do not overlap, it needs zero flops.
- $x^Ty$ needs no more than $2\min\{\mathbf{nnz}(x),\mathbf{nnz}(y)\}$ flops. If the patterns do not overlap, it needs zero flops, because $x^Ty=0$.

> *Intuition note.* Counting flops is a quick way to see how cost grows with size. Here the cost is of order $n$, so an input 10 times bigger should take around 10 times longer. Arithmetic on zero entries can be skipped, so sparse vectors need fewer flops.

### Exercises (pp. 25–28)
Twenty exercises (1.1–1.20) on notation, modelling with inner products, linear combinations of cash flows, the auto-regressive model and storage/flop counts. They are listed under "Exercises worth doing" below. The source does not print solutions.

## Toy example (ours, not from the text)
Let $n=3$, price vector $p=(2,3,5)$ (dollars per unit), quantity vector $q=(4,0,1)$, and 0/1 vector $o=(1,0,1)$.

1. Total cost: $p^Tq=2\cdot4+3\cdot0+5\cdot1=8+0+5=13$.
2. Pick out entry 2: $e_2=(0,1,0)$, so $e_2^Tp=0\cdot2+1\cdot3+0\cdot5=3=p_2$.
3. Sum and average of $p$: $\mathbf 1^Tp=2+3+5=10$. Then $(\mathbf 1/3)^Tp=10/3\approx3.33$.
4. Selective sum: $o^Tp=2+0+5=7$ (the prices of items 1 and 3).
5. A convex combination: $0.25p+0.75q=(0.5,0.75,1.25)+(3,0,0.75)=(3.5,0.75,2)$. The coefficients $0.25+0.75=1$ and are nonnegative.
6. Flops for $p^Tq$: 3 multiplications and 2 additions $=2n-1=5$ flops, simplified to $2n=6$.
7. Sparse case: $p=(2,3,5)$ has 3 nonzeros and $q=(4,0,1)$ has 2. The bound $2\min\{3,2\}=4$ flops suffices, since only indices 1 and 3 need multiplying (2 multiplications, 1 addition).

## Concepts
- [[vector]] — ordered finite list of numbers; an $n$-vector has size $n$ (p. 3)
- [[linear combination]] — $\beta_1a_1+\dots+\beta_ma_m$ with scalar coefficients (p. 17)
- [[dot (inner) product]] — $a^Tb=\sum a_ib_i$, called inner or dot product here (p. 19)
- [[affine-convex-combination]] (new) — coefficients sum to 1 (affine); also nonnegative (convex, mixture, weighted average) (p. 17)
- [[standard-unit-vector]] (new) — $e_i$: one in entry $i$, zero elsewhere; $e_i^Ta=a_i$ (pp. 5, 20)
- [[sparse-vector]] (new) — many entries zero; $\mathbf{nnz}(x)$ counts the nonzeros (p. 6)
- [[block-vector]] (new) — vector built by stacking vectors; colon notation gives slices (p. 4)
- [[flop-count-complexity]] (new) — number of floating point operations of a specific method, simplified to leading order (pp. 23–24)
- [[orthogonality]] — not defined in this unit; only the sparse non-overlapping case $x^Ty=0$ appears (p. 24)

## Canonical instances
- [[rgb-color-vector]] (new) — a 3-vector as a color (pp. 6–7)
- [[word-count-vector]] (new) — document as counts or histogram over a dictionary; sentiment via $w^Tx$ (pp. 9–10, 22)
- [[portfolio-vector]] (new) — holdings per asset, trade vector, value $p^Ts$, return $r^Tw$ (pp. 7, 14, 22)
- [[cash-flow-replication]] (new) — two-period loan $=c_1+1.1c_2$ (p. 18)
- [[net-present-value]] (new) — $d^Tc$ as discounted total (p. 22)
- [[image-as-vector]] (new) — $M\times N$ pixels as a length-$MN$ vector (p. 9)
- [[market-clearing]] (new) — sum of agents' vectors equals zero (p. 14)
- [[polynomial-evaluation-inner-product]] (new) — $c^Tz=p(t)$ (p. 21)

## Bridges (candidates)
- [structural-analogy] $e_i^Ta=a_i$ and $b=\sum b_ie_i$ ↔ basis and coordinates: unit vectors play the role of a coordinate system.
- [same-math] $f^Tp$ for probabilities $p$ ↔ probability: expected value $E[f]=\sum p_if_i$.
- [structural-analogy] sparsity pattern of a vector ↔ network science: the set of neighbors of a node in an adjacency row.
- [same-math] $a^Ta=\sum a_i^2$ ↔ norm: squared Euclidean length of a vector (the norm is not defined in this unit).
- [structural-analogy] word-count vectors and $a^Tb$ for 0/1 occurrence vectors ↔ text analysis/set similarity: overlap counts between documents or subsets.

## Questions this raises
- The inner product of 0/1 vectors counts co-occurrences. How do we turn that raw count into a similarity that does not grow with document length?
- What does it mean geometrically when $a^Tb=0$ for non-sparse vectors (the text only treats the non-overlapping sparse case)?
- The lines $(1-\theta)a+\theta b$ work in dimension 100. Which familiar geometric ideas break down or survive in high dimension?
- If a flop count is only reliable to a factor of 2–10, what else (memory, hardware) dominates real running time?

## Exercises worth doing
- Ex. 1.6 (p. 26) — express the vector of differences using slices; builds fluency with colon notation — difficulty: easy
- Ex. 1.10 (p. 26) — find the weight vector $w$ so that a weighted course score equals $w^Tr$; practice with scaling inner products — difficulty: medium
- Ex. 1.14 (p. 27) — interpret a long-only portfolio that is neutral to a sector; links the inner product with nonnegativity — difficulty: medium
- Ex. 1.15 (p. 27) — choose a cheapest supplier, and test the "split the order" claim with inner products — difficulty: medium
- Ex. 1.18 (p. 27) — show that a linear combination of linear combinations is a linear combination ($m=k=2$) — difficulty: easy
- Ex. 1.20 (p. 28) — bytes and flops for 100 vectors of length $10^5$; practice with the complexity rules — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (e.g. pdf 13 is printed p. 3). All citations use printed pages.
- The text layer loses matrix brackets and some symbols; the page images were used to check the examples and the formulas for $d$ and $d^Tc$.
- Wording slip on p. 10: in "Occurrence or subsets" the vector is named $o$, but the sentence on Boolean vectors says "the vector $a$". Also p. 20 "picks out the $i$th element $a$" lacks "of".
- Possible inconsistency in the source: p. 23 says flop-based time estimates are accurate only to a factor of about ten; p. 24 says flop counts are not expected to predict time better than a factor of 2 (as a reason for dropping the factor 2).
- The sparse bounds on p. 24 (e.g. $x+y$ "no more than $\min\{\mathbf{nnz}(x),\mathbf{nnz}(y)\}$ flops") are reported as printed.
- Exercises 1.1–1.20 are printed with no solutions. Fig. 1.5 (p. 10) shows a short italic sentence about word count vectors, the dictionary (word, in, number, horse, the, document) and the count vector (3, 2, 1, 0, 4, 2); all of it is legible in the page image.
