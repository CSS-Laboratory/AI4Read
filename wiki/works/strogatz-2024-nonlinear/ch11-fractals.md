---
id: strogatz-2024-nonlinear/ch11-fractals
work: strogatz-2024-nonlinear
unit: "11 Fractals"
pages: 405–428
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Fractals (Strogatz, Ch. 11)

## L0 — One line
Fractals are shapes with fine structure at arbitrarily small scales, and non-integer "dimensions" (similarity, box, correlation) measure how that structure scales, which gives tools for describing strange attractors.

## L1 — The gist (≤ 120 words)
Strange attractors, such as the Lorenz attractor, have very peculiar geometry. How can we describe it? The chapter builds the tools. It first reviews countable and uncountable sets, then studies the Cantor set and the von Koch curve. Dimension is generalised step by step: similarity dimension (exactly self-similar sets), box dimension (sets that need not be self-similar), and pointwise and correlation dimensions (points from a simulated trajectory). Numerical examples give a correlation dimension of about 2.05 for the Lorenz attractor. For the logistic map at the onset of chaos, the correlation dimension is about 0.50. Multifractals are mentioned as the case where one number is not enough. These ideas are used in Chapter 12.

**Prerequisites:** logarithms and power laws; geometric series; the idea of a limit; decimal digits and place value; what a map or trajectory is.

## L2 — Key ideas
- Fractals have fine structure at arbitrarily small scales and usually some self-similarity, which may be exact, approximate or statistical (p. 405).
- Two infinite sets have the same size if they can be paired one-to-one. The integers and positive rationals are countable; the reals in [0,1] are not (Cantor's diagonal argument) (pp. 406–408).
- The Cantor set has measure zero (it can be covered by intervals of arbitrarily small total length) but uncountably many points; the uncountability is shown by describing it as exactly the set of numbers whose base-3 expansion has no 1's and then applying the diagonal argument (pp. 409–411).
- Similarity dimension copes with the von Koch paradox (infinite length, yet apparently no area): $d=\ln m/\ln r$ gives $\ln 4/\ln 3\approx1.26$ (pp. 412–414).
- A topological Cantor set is a closed set that is totally disconnected (no connected pieces except single points) and has no isolated points (every point has other points of the set arbitrarily close). Its definition does not mention self-similarity or dimension, and topological features are more robust than geometric ones (p. 415).
- Box dimension $d=\lim_{\varepsilon\to0}\ln N(\varepsilon)/\ln(1/\varepsilon)$ works without self-similarity, but it is rarely used in practice because it is costly to compute (pp. 416–418).
- The correlation dimension is a more efficient estimator that has become standard for attractors. It is read from the slope of $\ln C(\varepsilon)$ against $\ln\varepsilon$ in a scaling region (a middle range of $\varepsilon$ where a straight line fits), and $d_{\rm corr}\le d_{\rm box}$ (pp. 418–419).
- Where scaling varies from place to place (multifractals), a spectrum $f(\alpha)$ is needed instead of a single number (p. 422).

## L3 — Walkthrough

### 11.0 Introduction (p. 405)
Lorenz solutions settle onto a strange attractor. Lorenz thought its geometry must be like an "infinite complex of surfaces." Fractals are complex shapes with fine structure at arbitrarily small scales, usually with some self-similarity. Self-similarity means a magnified small part resembles the whole; it may be exact, approximate or statistical. The chapter's goals are modest: get to know the simplest fractals and the notions of fractal dimension, to be used in Chapter 12 (p. 405).

### 11.1 Countable and Uncountable Sets (pp. 406–408)
**Definitions.** Two sets have the same *cardinality* (number of elements) if an invertible mapping pairs each $x\in X$ with exactly one $y\in Y$ (a *one-to-one correspondence*). A set that can be put in one-to-one correspondence with $\mathbb N=\{1,2,3,\dots\}$ is *countable*; otherwise it is *uncountable* (p. 406). Equivalently, $X$ is countable if it can be written as a list $\{x_1,x_2,\dots\}$ in which every element appears at some finite position (p. 406).

- **Ex. 11.1.1.** Even numbers: pair $n$ with $2n$ (1↔2, 2↔4, …). So there are exactly as many even numbers as natural numbers (p. 406).
- **Ex. 11.1.2.** Integers: list $0,1,-1,2,-2,3,-3,\dots$ by increasing absolute value. Every integer appears eventually (p. 406).
- **Ex. 11.1.3.** Positive rationals. Wrong way: list $1/1,1/2,1/3,\dots$; this never finishes the $1/n$'s, so $2/3$ is never reached. Right way: make a table whose $pq$-th entry is $p/q$ and count by the weaving path of Fig. 11.1.1. Any $p/q$ is reached after finitely many steps (p. 407).
- **Ex. 11.1.4.** The reals in $(0,1)$ are uncountable (proof by contradiction). Suppose they were listed as decimals $x_i=0.x_{i1}x_{i2}x_{i3}\dots$. Build $r$ whose $n$th digit $\bar x_{nn}$ is any digit other than $x_{nn}$. Then $r=0.\bar x_{11}\bar x_{22}\bar x_{33}\dots$ differs from $x_n$ in the $n$th place, so it is not on the list. Every list is incomplete (pp. 407–408). This is Cantor's *diagonal argument*: $r$ changes the diagonal entries of the digit matrix $[x_{ij}]$ (p. 408).

*Intuition note.* "Countable" means you can number the elements so that none is missed. The diagonal trick shows that any numbering of the reals misses some real, so the reals are a strictly bigger infinity.

### 11.2 Cantor Set (pp. 408–411)
**Construction.** Start with $S_0=[0,1]$. Remove the open middle third $(\tfrac13,\tfrac23)$, keeping the endpoints; this gives $S_1$. Remove the open middle thirds of those two intervals to get $S_2$, and so on. The limit $C=S_\infty$ is the *Cantor set* (p. 408).

**Fractal properties** (p. 409):
1. $C$ has structure at arbitrarily small scales. A smooth curve under magnification becomes featureless.
2. $C$ is self-similar. The left part of $C$ (in $[0,\tfrac13]$), enlarged 3 times, gives $C$. Each of the four intervals of $S_2$ holds a copy scaled by 9. Exact self-similarity is found only in the simplest fractals; more general ones are only approximately self-similar.
3. Its dimension is not an integer: $\ln2/\ln3\approx0.63$ (shown in 11.3).

Two further properties are not fractal properties as such (p. 409).

- **Ex. 11.2.1 (measure zero).** Each $S_n$ covers $C$. The length of $S_n$ is $L_n=(2/3)^n$ ($L_0=1$, $L_1=2/3$, $L_2=(2/3)^2$). Since $L_n\to0$, the total length of $C$ is zero (p. 409).
- **Ex. 11.2.2 (characterisation).** $C$ consists of all $c\in[0,1]$ with no 1's in the base-3 expansion. Write $x=\frac{a_1}{3}+\frac{a_2}{3^2}+\frac{a_3}{3^3}+\dots=.a_1a_2a_3\dots$, with digits $a_n\in\{0,1,2\}$. Digit $a_1$ says whether $x$ lies in the left, middle or right third of $[0,1]$; $a_2$ refines this within that piece (Fig. 11.2.2). Removing the middle third removed all points with $a_1=1$. The second stage removed those with $a_2=1$, and so on (p. 410).
- **Endpoint subtlety.** $\tfrac13=.1000\ldots=.02222\ldots$. So every point of $C$ can be written with only 0's and 2's (p. 411).
- **Ex. 11.2.3 (uncountable).** Suppose $\{c_1,c_2,\dots\}$ lists all of $C$, with $c_{ij}$ the $j$th base-3 digit of $c_i$. Define $c=\bar c_{11}\bar c_{22}\dots$, where the bar swaps 0 and 2. Then $c$ uses only 0's and 2's, so $c\in C$, but it differs from every $c_n$ in the $n$th digit. This is a contradiction (p. 411).

*Intuition note.* The Cantor set has total length zero, yet it is uncountable, like the reals in [0,1]. Zero length and uncountably many points can coexist.

### 11.3 Dimension of Self-Similar Fractals (pp. 411–415)
**A paradox.** Dimension might be defined as the minimum number of coordinates needed to specify a point, e.g. arc length for a curve (p. 411). The von Koch curve $K$ is built by replacing the middle third of each segment of $S_{n-1}$ with the other two sides of an equilateral triangle (Fig. 11.3.1). If $S_0$ has length $L_0$, then $S_1$ has four segments of length $\tfrac13L_0$, so $L_1=\tfrac43L_0$ and $L_n=(\tfrac43)^nL_0\to\infty$. The arc length between any two points of $K$ is also infinite, so arc length cannot locate points (p. 412). So $K$ seems more than one-dimensional, yet it has no "area", so its dimension should lie between 1 and 2 (p. 412).

**Similarity dimension.** For a square scaled down by $r$, it takes $r^2$ copies to rebuild it ($m=4$ for $r=2$, $m=9$ for $r=3$). For a cube it takes $r^3$. The exponents reflect dimension (p. 413). Definition: if a self-similar set is made of $m$ copies of itself scaled down by factor $r$, its *similarity dimension* $d$ satisfies
$$m=r^d,\qquad d=\frac{\ln m}{\ln r}.$$
- **Ex. 11.3.1.** Cantor set: $m=2$, $r=3$, so $d=\ln2/\ln3\approx0.63$ (p. 414).
- **Ex. 11.3.2.** Von Koch curve: $m=4$ pieces, each scaled by $r=3$, so $d=\ln4/\ln3\approx1.26$ (p. 414). This is consistent with the intuition that it lies between 1 and 2.

**More general Cantor sets.** *Even-fifths Cantor set:* divide an interval into five equal pieces, delete the 2nd and 4th, and repeat. Scaling $S_n$ by 5 gives one third of $S_{n+1}$. Taking $n\to\infty$, $S_\infty$ is three copies of itself scaled by 5: $m=3$, $r=5$, $d=\ln3/\ln5$ (Ex. 11.3.3, p. 415).

**Topological Cantor set** (p. 415). A closed set $S$ is a topological Cantor set if:
1. $S$ is *totally disconnected*: it contains no connected subsets other than single points. For subsets of the line this means it contains no intervals.
2. $S$ has no *isolated points*: for any $p\in S$ and any $\varepsilon>0$ there is another $q\in S$ within distance $\varepsilon$ of $p$.

Property 1 says points are spread apart, property 2 says they are packed together; this is the paradoxical aspect. The definition says nothing about self-similarity or dimension, which are geometric, not topological. Topological features are more robust: continuously deforming a self-similar Cantor set can destroy self-similarity, but properties 1 and 2 persist. Cross sections of strange attractors are often topological Cantor sets, though not necessarily self-similar (p. 415).

*Intuition note.* Similarity dimension asks: if I shrink by $r$, how many copies fill the original? Squares give $r^2$, cubes $r^3$; the Cantor set needs only $2$ when $r=3$, so its "exponent" is below 1.

### 11.4 Box Dimension (pp. 416–418)
All definitions share the idea of measuring at scale $\varepsilon$, ignoring irregularities smaller than $\varepsilon$, and then letting $\varepsilon\to0$ (p. 416).

**Definition.** Let $S\subset\mathbb R^D$ and let $N(\varepsilon)$ be the minimum number of $D$-dimensional cubes of side $\varepsilon$ needed to cover $S$. For a smooth curve of length $L$, $N(\varepsilon)\propto L/\varepsilon$; for a planar region of area $A$ bounded by a smooth curve, $N(\varepsilon)\propto A/\varepsilon^2$. The key observation is that the dimension equals the exponent $d$ in $N(\varepsilon)\propto1/\varepsilon^d$. This power law holds for most fractals, with non-integer $d$. $d$ is the *capacity* or *box dimension*:
$$d=\lim_{\varepsilon\to0}\frac{\ln N(\varepsilon)}{\ln(1/\varepsilon)},\quad\text{if the limit exists.}$$

- **Ex. 11.4.1 (Cantor set).** $S_n$ has $2^n$ intervals of length $(1/3)^n$. With $\varepsilon=(1/3)^n$, $N=2^n$. Then $d=\lim \frac{\ln 2^n}{\ln 3^n}=\frac{n\ln2}{n\ln3}=\frac{\ln2}{\ln3}$, matching the similarity dimension (p. 417). Trick: using the discrete sequence $\varepsilon=(1/3)^n$ is allowed. For other $\varepsilon$ the cover is slightly wasteful, but the limit of $d$ is the same (p. 417).
- **Ex. 11.4.2 (not self-similar).** Divide a square into nine equal squares and discard one at random. Repeat on each of the eight remaining squares. $S_1$ is covered with no waste by $N=8$ squares of side $\tfrac13$, $S_2$ by $8^2$ squares of side $(\tfrac13)^2$, and generally $N=8^n$ at $\varepsilon=(\tfrac13)^n$. So $d=\frac{n\ln8}{n\ln3}=\frac{\ln8}{\ln3}$ (p. 417).

**Critique** (pp. 417–418). A minimal cover is hard to find. An equivalent method uses a square mesh of side $\varepsilon$ and counts occupied boxes. Even so, box dimension is rarely used in practice because it needs too much storage and computer time. It also has mathematical drawbacks: the rationals in $[0,1]$ have box dimension 1 (Falconer 1990, cited), though they are only countably many. The *Hausdorff dimension* (the most important alternative, per Falconer) covers the set with small sets of varying sizes. It has nicer mathematical properties but is even harder to compute numerically (p. 418).

### 11.5 Pointwise and Correlation Dimensions (pp. 418–423)
**Setup.** Generate many points $\{\mathbf x_i,\ i=1,\dots,n\}$ on a strange attractor by running the system for a long time, after discarding the initial transient. Almost all trajectories on a strange attractor have the same long-term statistics, so one very long trajectory suffices (p. 418). Grassberger and Procaccia (1983) proposed the standard efficient approach. Fix $\mathbf x\in A$ and let $N_{\mathbf x}(\varepsilon)$ be the number of points of $A$ in a ball of radius $\varepsilon$ about $\mathbf x$. Most of those points come from other parts of the trajectory passing close to $\mathbf x$, so $N_{\mathbf x}(\varepsilon)$ measures how often a typical trajectory visits that neighbourhood (pp. 418–419).

**Definitions** (p. 419). As $\varepsilon$ grows, $N_{\mathbf x}(\varepsilon)$ typically follows $N_{\mathbf x}(\varepsilon)\propto\varepsilon^d$; $d$ is the *pointwise dimension* at $\mathbf x$. It can depend significantly on $\mathbf x$ and is smaller in rarefied regions. Averaging $N_{\mathbf x}(\varepsilon)$ over many $\mathbf x$ gives $C(\varepsilon)$, found empirically to scale as $C(\varepsilon)\propto\varepsilon^d$; $d$ is the *correlation dimension*. It accounts for the density of points, while box dimension weights all occupied boxes equally. In general $d_{\rm correlation}\le d_{\rm box}$, though they are usually very close (p. 419).

**Estimation.** Plot $\log C(\varepsilon)$ against $\log\varepsilon$; the slope is $d$. The power law holds only in the *scaling region*, (minimum separation of points on $A$) $\ll\varepsilon\ll$ (diameter of $A$). At large $\varepsilon$ the balls engulf the attractor and $C$ saturates; at tiny $\varepsilon$ each ball holds only $\mathbf x$ itself (Fig. 11.5.2, p. 419).

- **Ex. 11.5.1 (Lorenz).** Parameters $r=28$, $\sigma=10$, $b=8/3$. Grassberger and Procaccia found $d_{\rm corr}=2.05\pm0.01$, an excellent fit except at large $\varepsilon$ (saturation). They used Runge–Kutta integration, time step 0.25, 15,000 points. Convergence was rapid: a few thousand points gave the dimension to within $\pm5$ percent (p. 420).
- **Ex. 11.5.2 (logistic map at onset of chaos).** Map: $x_{n+1}=rx_n(1-x_n)$ at $r=r_\infty=3.5699456\dots$. The attractor looks like a $2^n$-cycle for $n\gg1$ (Fig. 11.5.4, built from superstable $2^n$-cycles). As $n\to\infty$ it approaches a topological Cantor set with gaps of various sizes. It is not strictly self-similar, because gaps scale by different factors at different locations (some "wishbones" in the orbit diagram are wider than others) (p. 421). One trajectory of 30,000 points from $x_0=\tfrac12$ gave $d_{\rm corr}=0.500\pm0.005$. This is smaller than $d_{\rm box}\approx0.538$ (Grassberger 1981), as expected (pp. 421–422). The deviation from a straight line at very small $\varepsilon$ is attributed by Grassberger and Procaccia to residual correlations among the $x_n$ on a single trajectory. These would be negligible for a strongly chaotic map but are visible at the onset of chaos. More points or several trajectories could extend the scaling region (p. 422).

**Multifractals** (p. 422). In the logistic attractor the scaling varies from place to place, unlike the uniform factor $\tfrac13$ of the middle-thirds Cantor set. One number cannot completely characterise it; some kind of distribution function is needed. Such sets are *multifractals*. Let $S_\alpha$ be the subset of $A$ with pointwise dimension $\alpha$, and $f(\alpha)$ the (fractal) dimension of $S_\alpha$. $f(\alpha)$ is the *multifractal spectrum* (spectrum of scaling indices; Halsey et al. 1986). Typical values of $\alpha$ give a large $S_\alpha$; unusual values give a small one. The graph of $f(\alpha)$ is typically a hump (Fig. 11.5.6), and its maximum is the box dimension. For systems at the onset of chaos, the universal quantity in the universality theory of Section 10.6 becomes the function $f(\alpha)$, giving more information and more stringent tests. The predictions have been checked experimentally with striking success (Glazier and Libchaber 1988, cited). A rigorous mathematical theory of multifractals is still lacking (pp. 422–423).

*Intuition note.* A fractal's dimension is read as a slope on a log–log plot of "how many neighbours within $\varepsilon$". It is trustworthy only where the line is straight, because data are limited at both ends. When different parts of the set scale differently, one slope is not enough.

## Toy example (ours, not from the text)
Take $[0,1]$ and cut it into 4 equal pieces. Keep pieces 1 and 4, delete the middle two, and repeat on each kept piece.
- Similarity dimension: 2 copies, each scaled down by $r=4$. So $m=2$, $r=4$, $d=\ln2/\ln4=\ln2/(2\ln2)=0.5$.
- Box dimension check: $S_n$ has $2^n$ intervals of length $4^{-n}$. Take $\varepsilon=4^{-n}$, so $N=2^n$. Then $d=\frac{\ln2^n}{\ln4^n}=\frac{n\ln2}{2n\ln2}=0.5$. The two agree.
- Length of $S_n$: $2^n\cdot4^{-n}=(1/2)^n\to0$, so the set has measure zero. Numerically: $S_1$ has length $0.5$, $S_2$ has $0.25$, $S_3$ has $0.125$.
- Digits: the set contains exactly the numbers with only digits 0 and 3 in base 4, so the diagonal argument (swap 0↔3) shows it is uncountable.

## Concepts
- [[countable-uncountable-sets]] (new) — a set is countable if it can be listed in a sequence; the reals in [0,1] cannot (p. 406)
- [[diagonal-argument]] (new) — build a number differing from the $n$th listed one in the $n$th digit, so it is not on the list (p. 408)
- [[strange-attractor-fractal]] — fractal: fine structure at arbitrarily small scales, usually with some self-similarity; used here to describe strange attractors (p. 405)
- [[cantor-set]] (new) — limit of repeatedly deleting open middle thirds; equals the numbers with no 1's in base 3 (pp. 408–410)
- [[topological-cantor-set]] (new) — closed, totally disconnected set with no isolated points (p. 415)
- [[similarity-dimension]] (new) — $d=\ln m/\ln r$ for a set made of $m$ copies scaled by $r$ (p. 413)
- [[box-dimension]] (new) — $d=\lim\ln N(\varepsilon)/\ln(1/\varepsilon)$ from covering by boxes of side $\varepsilon$ (p. 416)
- [[correlation-dimension]] (new) — scaling exponent of the average ball count $C(\varepsilon)\propto\varepsilon^d$; accounts for point density; $\le d_{\rm box}$ (p. 419)
- [[pointwise-dimension]] (new) — local scaling exponent of $N_{\mathbf x}(\varepsilon)$ at one point (p. 419)
- [[multifractal]] (new) — set whose local scaling varies, described by the spectrum $f(\alpha)$ (p. 422)
- [[scale-invariance]] — here self-similarity of fractals, exact in the Cantor set and approximate in general (p. 409)
- [[universality]] — at the onset of chaos, multifractals make the universal quantity a function $f(\alpha)$ (pp. 422–423)
- [[heavy-tail-power-law]] — here a power law $N(\varepsilon)\propto\varepsilon^{-d}$ in the covering count (p. 416)

## Canonical instances
- [[middle-thirds-cantor-set]] — measure zero, uncountable, dimension $\ln2/\ln3$ (pp. 408–417)
- [[von-koch-curve]] — infinite length, similarity dimension $\ln4/\ln3$ (pp. 411–414)
- [[even-fifths-cantor-set]] — dimension $\ln3/\ln5$ (p. 415)
- [[random-square-removal-fractal]] — not self-similar; box dimension $\ln8/\ln3$ (p. 417)
- [[lorenz-attractor]] — correlation dimension about 2.05 (p. 420)
- [[logistic-map-onset-of-chaos]] — non-self-similar Cantor-like attractor; $d_{\rm corr}\approx0.500<d_{\rm box}\approx0.538$ (pp. 420–422)

## Bridges (candidates)
- [structural-analogy] box-counting exponent $N(\varepsilon)\propto\varepsilon^{-d}$ ↔ complex-systems: heavy-tail/power-law scaling — both read an exponent as a slope on a log–log plot.
- [structural-analogy] scaling region of $C(\varepsilon)$ (power law only between two scales) ↔ complex-systems: fitting power laws to finite empirical data — straight lines hold only over a limited range.
- [structural-analogy] multifractal spectrum $f(\alpha)$ ↔ complex-systems: universality at critical points — a function, not one number, is the universal quantity.

## Questions this raises
- Why does the correlation dimension of the logistic attractor at $r_\infty$ differ from its box dimension, and how large can such gaps be in general?
- How do these dimensions relate to the geometry of strange attractors in Chapter 12 (the text promises this link)?
- What would a statistical estimate of dimension look like for noisy experimental data, where the scaling region is short?
- Can random fractals, whose construction depends on coin flips, have a well-defined box dimension? (The text poses this in Exercise 11.4.8.)

## Exercises worth doing
- Ex. 11.1.1 (p. 423) — why the diagonal argument does not make the rationals uncountable — difficulty: medium
- Ex. 11.2.5 (p. 424) — base-3 expansion of 1/2, a one-to-one map from the Cantor set to [0,1], and a non-endpoint point of $C$ — difficulty: medium
- Ex. 11.3.2 (p. 425) — similarity dimension of the generalized Cantor set with middle fraction $a$ removed — difficulty: easy
- Ex. 11.3.10 (p. 426) — a "fat fractal" (a topological Cantor set with positive measure); the text links it to the logistic map's chaotic parameters (Farmer 1985) — difficulty: hard
- Ex. 11.4.6 (p. 427) — strange repeller of the tent map: escaping points, box dimension, positive Liapunov exponent — difficulty: hard
- Ex. 11.4.9 (p. 428) — box dimension of "fractal cheese" with random holes — difficulty: medium

## Reading notes
- Printed page = pdf − 19 (pdf 424 = printed 405). Citations use printed numbers.
- The text layer lost many symbols (∈, ≈, →, ∞, ≤, Greek letters); I checked these against the page images. Example: $d_{\rm correlation}\le d_{\rm box}$ is printed with "≤" in the image.
- Figure 11.5.3 and 11.5.5 are reproduced from Grassberger and Procaccia (1983), with their own axis notation (ℓ for $\varepsilon$, ν for $d$). The figures carry labels ν = 2.05 ± .01 and ν = 0.500 ± .005, matching the text.
- Statements about Hausdorff dimension, the box dimension of the rationals, and the multifractal and universality results are reported as the author cites them (Falconer, Halsey et al., Glazier and Libchaber); they are not proved in the chapter.
- Exercise 11.3.9 is printed as "Delete the central cube on each face, along with the central cube."
