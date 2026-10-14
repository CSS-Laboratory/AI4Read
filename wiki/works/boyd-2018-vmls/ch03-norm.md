---
id: boyd-2018-vmls/ch03-norm
work: boyd-2018-vmls
unit: "Chapter 3 — Norm and distance"
pages: 45–68
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Norm and distance

## L0 — One line
The Euclidean norm measures the size of a vector, and from it come distance, standard deviation, angle and correlation, with the Cauchy–Schwarz inequality keeping the correlation between −1 and 1.

## L1 — The gist (≤ 120 words)
How can we measure the size of a vector, how far apart two vectors are, how much a vector's entries vary, and how aligned two vectors are? The chapter defines the Euclidean norm. Distance is the norm of a difference. Standard deviation is the RMS (root-mean-square) value of the de-meaned vector (the vector minus its mean). The angle is the arccosine of aᵀb/(‖a‖‖b‖). The correlation coefficient is the cosine of the angle between de-meaned vectors, and the Cauchy–Schwarz inequality keeps it between −1 and 1. These tools support nearest-neighbour search, document comparison, and risk and return analysis. Choice of units matters when entries are different kinds of quantity. Operation counts are given in flops (arithmetic operations).

**Prerequisites:** vectors as lists of numbers; inner product aᵀb and its symmetry; the mean of a list; the cosine and arccosine; block (stacked) vectors; the all-ones vector **1**.

## L2 — Key ideas (5–10 bullets)
- The norm ‖x‖ = √(xᵀx) obeys four properties: homogeneity, triangle inequality, nonnegativity and definiteness. Any function with these four properties is a "general norm", but the book uses only the Euclidean one (p. 46).
- The RMS value ‖x‖/√n makes sizes comparable across dimensions. The Chebyshev inequality k/n ≤ (rms(x)/a)² limits how many entries can be large (pp. 46–48).
- Distance is dist(a,b) = ‖a−b‖. It gives feature distance, RMS prediction error and nearest neighbour. When entries are different kinds of quantity, the units change the distances (pp. 48–52).
- Standard deviation is the RMS value of the de-meaned vector, and rms² = avg² + std². Standardizing gives mean 0 and std 1 (pp. 52–56).
- Cauchy–Schwarz, |aᵀb| ≤ ‖a‖‖b‖, is proved by expanding ‖βa−αb‖² ≥ 0. It is then used to verify the triangle inequality (p. 57).
- The angle θ = arccos(aᵀb/(‖a‖‖b‖)) is symmetric and unchanged by positive scaling. The sign of aᵀb classifies angles as acute, orthogonal or obtuse (pp. 57–58).
- The correlation coefficient is the cosine of the angle between de-meaned vectors. It gives std(a+b)² = std(a)² + 2ρ std(a)std(b) + std(b)², and hence the case for hedging (pp. 60–62).
- Norm, distance, angle and correlation cost order n flops (arithmetic operations); nearest-neighbour search over k vectors costs 3kn flops (p. 63).

## L3 — Walkthrough

### 3.1 Norm
**Definition.** For an n-vector x, the Euclidean norm is $\|x\| = \sqrt{x_1^2 + \dots + x_n^2} = \sqrt{x^Tx}$ (p. 45). It is also written $\|x\|_2$. The book discourages the word "length" because it also means dimension (p. 45). Examples: $\|(2,-1,2)\| = \sqrt 9 = 3$ and $\|(0,-1)\| = 1$ (p. 45). For a 1-vector the norm is the absolute value (p. 45). "Small" and "large" depend on the application (p. 45).

**Properties** (x, y same size, β scalar) (p. 46):
- Nonnegative homogeneity: $\|\beta x\| = |\beta|\,\|x\|$.
- Triangle inequality: $\|x+y\| \le \|x\| + \|y\|$ (also called subadditivity).
- Nonnegativity: $\|x\| \ge 0$.
- Definiteness: $\|x\| = 0$ only if $x = 0$.

The last two together are called positive definiteness (p. 46). The first, third and fourth are easy to show from the definition. The author's example is definiteness: if $\|x\|=0$ then $x_1^2+\dots+x_n^2 = 0$. This is a sum of nonnegative numbers that equals zero, so each term is zero, so every $x_i = 0$ (p. 46). The triangle inequality is harder and is derived later via Cauchy–Schwarz (pp. 46, 57). Any real-valued function satisfying the four properties is a general norm. The book uses only the Euclidean norm and points to exercise 3.5 for others (p. 46).

**RMS value.** $\mathbf{rms}(x) = \sqrt{(x_1^2+\dots+x_n^2)/n} = \|x\|/\sqrt n$. The quantity under the root is the mean square $\mathbf{ms}(x)$. RMS suits comparing vectors of different dimension, since it indicates a "typical" $|x_i|$. For the all-ones n-vector, the norm is $\sqrt n$ but the RMS value is 1. If all entries equal α, the RMS value is $|\alpha|$ (p. 46).

**Norm of a sum.**
$$\|x+y\| = \sqrt{\|x\|^2 + 2x^Ty + \|y\|^2}\tag{3.1}$$
Derivation (p. 47): $\|x+y\|^2 = (x+y)^T(x+y)$ (definition); $= x^Tx + x^Ty + y^Tx + y^Ty$ (expand); $= \|x\|^2 + 2x^Ty + \|y\|^2$ (definition and $x^Ty = y^Tx$). Then take the square root.

**Block vectors.** For $d = (a,b,c)$: $\|d\|^2 = d^Td = a^Ta + b^Tb + c^Tc = \|a\|^2 + \|b\|^2 + \|c\|^2$. Equivalently $\|(a,b,c)\| = \|(\|a\|,\|b\|,\|c\|)\|$. The outer norm is of a 3-vector whose entries are the scalar norms (p. 47).

**Chebyshev inequality.** Suppose k entries of x satisfy $|x_i| \ge a > 0$. Then k entries have $x_i^2 \ge a^2$. The other $n-k$ squares are nonnegative, so $\|x\|^2 \ge ka^2$, giving $k \le \|x\|^2/a^2$ (p. 47).
- If $\|x\|^2/a^2 \ge n$ the bound says nothing, since $k \le n$ anyway (p. 47).
- If $a > \|x\|$, then $k < 1$, so $k = 0$. No entry can exceed the norm in magnitude (p. 47).
- In RMS form:
$$\frac kn \le \left(\frac{\mathbf{rms}(x)}{a}\right)^2\tag{3.2}$$
- Example: no more than $1/25 = 4\%$ of the entries can exceed the RMS value by more than a factor of 5 (p. 48).
- This partly justifies reading RMS as the size of a typical entry. A converse (at least one entry has $|x_i| \ge \mathbf{rms}(x)$) is exercise 3.8 (p. 48).

*Intuition note.* The norm adds up squared entries, so each large entry takes a share of the sum. Chebyshev turns this into a counting limit: the fraction of entries with |xᵢ| ≥ a is at most (rms(x)/a)², so for a given a, a small RMS value allows only a small fraction of entries that large.

### 3.2 Distance
**Definition.** $\mathbf{dist}(a,b) = \|a-b\|$. In 1, 2 and 3 dimensions it equals the usual distance between points (fig. 3.1). It is defined in any dimension. The RMS deviation between two n-vectors is $\|a-b\|/\sqrt n$ (p. 48). "Close" and "far" depend on the application (p. 48).

**Example (p. 49).** $u = (1.8, 2.0, -3.7, 4.7)$, $v = (0.6, 2.1, 1.9, -1.4)$, $w = (2.0, 1.9, -4.0, 4.6)$. Then $\|u-v\| = 8.368$, $\|u-w\| = 0.387$, $\|v-w\| = 8.533$. So u is much nearer to w than to v (p. 49).

**Triangle inequality, geometric meaning.** For vertices a, b, c, the side lengths are the distances between vertices. Geometric intuition says no side exceeds the sum of the other two:
$$\|a-c\| \le \|a-b\| + \|b-c\|\tag{3.3}$$
This follows from the triangle inequality: $\|a-c\| = \|(a-b)+(b-c)\| \le \|a-b\| + \|b-c\|$ (p. 49).

**Examples of use (p. 50).**
- *Feature distance:* $\|x-y\|$ for feature vectors, for example hospital patients.
- *RMS prediction error:* $\mathbf{rms}(y-\hat y)$ for a time series y and prediction $\hat y$. The prediction is good if this is small, say compared to $\mathbf{rms}(y)$.
- *Nearest neighbour:* $z_j$ is the nearest neighbour of x among $z_1,\dots,z_m$ if $\|x-z_j\| \le \|x-z_i\|$ for $i = 1,\dots,m$ (fig. 3.3). Generalizations such as k-nearest neighbours are used in many applications.
- *Document dissimilarity:* $\|x-y\|$ for word-count histograms. Table 3.1 uses a dictionary of 4423 words and five Wikipedia articles. Related articles are closer. For example Veterans Day–Memorial Day is 0.095 while Veterans Day–Super Bowl is 0.170 (pp. 50–51).

**Units for heterogeneous entries (pp. 51–52).** $\|x-y\|^2 = \sum_i (x_i-y_i)^2$, so, roughly speaking, all entries have equal status. This makes sense when entries are the same type of quantity in the same units. When entries are different quantities, units must be chosen with care: if we want the entries to have approximately equal status, their values should be of about the same magnitude, so units are often chosen so that typical values are similar in size. House example: with area in thousands of square feet, $x=(1.6,2)$, $y=(1.5,2)$, $z=(1.6,4)$. Then $\|x-y\|=0.1$, small compared with norms of about 2.5, and z is far from both. With area in square feet, $\tilde x=(1600,2)$, $\tilde y=(1500,2)$, $\tilde z=(1600,4)$. Now the distance between houses 1 and 3 is 2, tiny against norms of about 1600, while the distance between houses 1 and 2 is much larger. Area differences then dominate and bedroom count plays a much smaller role (p. 52).

*Intuition note.* Distance only compares numbers, not meanings. If one feature is written in huge units, it swamps the others, so scaling is a modelling choice.

### 3.3 Standard deviation
**De-meaned vector.** $\tilde x = x - \mathbf{avg}(x)\mathbf 1$; it has $\mathbf{avg}(\tilde x) = 0$, and it is zero if all entries of x are equal (p. 52).

**Definition.** std(x) is the RMS value of the de-meaned vector:
$$\mathbf{std}(x) = \sqrt{\frac{(x_1-\mathbf{avg}(x))^2 + \dots + (x_n-\mathbf{avg}(x))^2}{n}} = \frac{\|x - (\mathbf 1^Tx/n)\mathbf 1\|}{\sqrt n}\tag{3.4}$$
It is the RMS deviation between x and the vector with all entries $\mathbf{avg}(x)$. It is zero only when all entries are equal and small when entries are nearly equal (pp. 52–53).

Example: $x = (1,-2,3,2)$ has $\mathbf{avg}(x)=1$, $\tilde x = (0,-3,2,1)$, and the book gives $\mathbf{std}(x) = 1.872$ (p. 53). The book warns that another common definition divides by $\sqrt{n-1}$ instead of $\sqrt n$; this book always uses (3.4). It sometimes writes $\mu = \mathbf 1^Tx/n$ and $\sigma = \|x-\mu\mathbf 1\|/\sqrt n$ (p. 53).

**Average, RMS, standard deviation.**
$$\mathbf{rms}(x)^2 = \mathbf{avg}(x)^2 + \mathbf{std}(x)^2\tag{3.5}$$
Derivation (p. 53), with $m = \mathbf 1^Tx/n$:
$$\begin{aligned}\mathbf{std}(x)^2 &= (1/n)\|x - m\mathbf 1\|^2\\ &= (1/n)\big(x^Tx - 2x^T(m\mathbf 1) + (m\mathbf 1)^T(m\mathbf 1)\big)\\ &= (1/n)\big(x^Tx - (2/n)(\mathbf 1^Tx)^2 + n\,m^2\big)\\ &= (1/n)x^Tx - m^2\\ &= \mathbf{rms}(x)^2 - \mathbf{avg}(x)^2.\end{aligned}$$
Second line: expand the squared norm of a sum. Third line: move scalars to the front and use $\mathbf 1^T\mathbf 1 = n$ (p. 53). Rearranging gives (3.5).

*Intuition note.* The mean square of the entries splits into the square of the mean (the level) and the mean square fluctuation around it.

**Examples (p. 54).**
- *Mean return and risk:* for a vector of per-period returns, avg is the return and std is the (per-period) risk. A risk–return plot (fig. 3.4) compares investments. A desirable series has high mean and low risk.
- *Temperature:* the average and the std over a year. The author expects high average and low std in a tropical location, and the opposite at high latitude.

**Chebyshev for standard deviation (p. 54).** If k entries satisfy $|x_i - \mathbf{avg}(x)| \ge a$, then $k/n \le (\mathbf{std}(x)/a)^2$. This is only interesting for $a > \mathbf{std}(x)$. At most $1/9 = 11.1\%$ of entries deviate from the mean by 3 standard deviations or more. For $\alpha > 1$, at least a fraction $1 - 1/\alpha^2$ of entries lie within α standard deviations of the mean. Example: mean return 8%, risk 3%. (Added step: a loss $x_i \le 0$ means $|x_i - 8| \ge 8$.) So the fraction of loss periods is at most $(3/8)^2 = 14.1\%$. The same bound covers "loss or $x_i \ge 16\%$" together (p. 54).

**Properties (p. 54).** $\mathbf{std}(x + a\mathbf 1) = \mathbf{std}(x)$, and $\mathbf{std}(ax) = |a|\,\mathbf{std}(x)$.

**Standardization (p. 56).** $z = \frac{1}{\mathbf{std}(x)}(x - \mathbf{avg}(x)\mathbf 1)$ has mean zero and standard deviation one. Its entries are z-scores. For example, $z_4 = 1.4$ means $x_4$ is 1.4 standard deviations above the mean. In a hospital test example, $z_6 = -3.2$ means a very low value for patient 6, while $z_{22} = 0.3$ is close to the average (p. 56).

### 3.4 Angle
**Cauchy–Schwarz inequality.** For any n-vectors a, b:
$$|a^Tb| \le \|a\|\,\|b\|$$
Proof (pp. 56–57). If $a=0$ or $b=0$, both sides are zero. Otherwise let $\alpha = \|a\|$, $\beta = \|b\|$:
$$\begin{aligned}0 \le \|\beta a - \alpha b\|^2 &= \|\beta a\|^2 - 2(\beta a)^T(\alpha b) + \|\alpha b\|^2\\ &= \beta^2\|a\|^2 - 2\beta\alpha(a^Tb) + \alpha^2\|b\|^2\\ &= \|b\|^2\|a\|^2 - 2\|b\|\|a\|(a^Tb) + \|a\|^2\|b\|^2\\ &= 2\|a\|^2\|b\|^2 - 2\|a\|\|b\|(a^Tb).\end{aligned}$$
Dividing by $2\|a\|\|b\|$ gives $a^Tb \le \|a\|\|b\|$. Applying this to $-a$ and $b$ gives $-a^Tb \le \|a\|\|b\|$. Together these give the inequality (p. 57).

*Equality.* For nonzero a, b, equality occurs only if $\|\beta a - \alpha b\| = 0$, i.e. $\beta a = \alpha b$. So each is a positive multiple of the other. If either is zero, equality holds when one is a nonnegative multiple of the other. In all other cases the inequality is strict (p. 57).

**Triangle inequality verified (p. 57).** $\|a+b\|^2 = \|a\|^2 + 2a^Tb + \|b\|^2 \le \|a\|^2 + 2\|a\|\|b\| + \|b\|^2 = (\|a\|+\|b\|)^2$. The middle step uses Cauchy–Schwarz. Take square roots.

**Angle.** For nonzero a, b, $\theta = \angle(a,b) = \arccos\!\big(a^Tb/(\|a\|\|b\|)\big)$, with arccos taking values in $[0,\pi]$. Equivalently, θ is the unique number in $[0,\pi]$ with $a^Tb = \|a\|\|b\|\cos\theta$. In 2 or 3 dimensions it is the usual angle between displacements from a common point (p. 57). Example (p. 58): $a=(1,2,-1)$, $b=(2,0,-3)$ give $a^Tb = 5$, $\|a\| = \sqrt6$, $\|b\| = \sqrt{13}$, and
$$\arccos\!\Big(\tfrac{5}{\sqrt6\sqrt{13}}\Big) = \arccos(0.5661) = 0.9690\ \text{rad} = 55.52^\circ.$$
The angle is symmetric, $\angle(a,b) = \angle(b,a)$, and unchanged by positive scaling: $\angle(\alpha a, \beta b) = \angle(a,b)$ for $\alpha,\beta>0$ (p. 58).

**Classification by the sign of $a^Tb$ (nonzero a, b) (p. 58; fig. 3.6).**
- θ = 90° ⇔ $a^Tb = 0$: orthogonal, written $a\perp b$. By convention the zero vector is orthogonal to every vector.
- θ = 0 (i.e. $a^Tb = \|a\|\|b\|$): aligned; each is a positive multiple of the other.
- θ = 180° (i.e. $a^Tb = -\|a\|\|b\|$): anti-aligned; each is a negative multiple of the other.
- θ < 90° ⇔ $a^Tb > 0$: acute.
- θ > 90° ⇔ $a^Tb < 0$: obtuse.

**Examples (p. 58–59).**
- *Spherical distance:* for 3-vectors a, b on a sphere of radius R, the distance along the sphere is $R\angle(a,b)$ (fig. 3.7).
- *Document similarity via angles:* for word counts or histograms, $\angle(x,y)$ measures dissimilarity; counts and histograms give the same result. Table 3.2 gives angles for the five Wikipedia articles. Veterans Day–Memorial Day is 60.6°, Academy–Golden Globe is 58.7°, and most other pairs are 85.6° to 87.7° (p. 59).

**Norm of sum via angles.**
$$\|x+y\|^2 = \|x\|^2 + 2x^Ty + \|y\|^2 = \|x\|^2 + 2\|x\|\|y\|\cos\theta + \|y\|^2\tag{3.6}$$
- If $\theta = 0$ (aligned), $\|x+y\| = \|x\| + \|y\|$.
- If $\theta = 90^\circ$ (orthogonal), $\|x+y\|^2 = \|x\|^2 + \|y\|^2$. This is the Pythagorean theorem (p. 60).

**Correlation coefficient.** With $\tilde a = a - \mathbf{avg}(a)\mathbf 1$ and $\tilde b = b - \mathbf{avg}(b)\mathbf 1$, both assumed nonzero:
$$\rho = \frac{\tilde a^T\tilde b}{\|\tilde a\|\|\tilde b\|}\tag{3.7}$$
So $\rho = \cos\angle(\tilde a, \tilde b)$. With $u = \tilde a/\mathbf{std}(a)$ and $v = \tilde b/\mathbf{std}(b)$, and using $\|u\| = \|v\| = \sqrt n$:
$$\rho = u^Tv/n\tag{3.8}$$
Properties (p. 60):
- ρ is symmetric in a and b.
- Cauchy–Schwarz gives $-1 \le \rho \le 1$; it is sometimes written as a percentage.
- ρ = 0 means uncorrelated; by convention an all-equal vector is uncorrelated with every vector.
- High correlation (say 0.8) means entries of a and b are typically above their mean at many of the same indices.
- ρ = 1 occurs only if $\tilde a$ and $\tilde b$ are aligned (positive multiples).
- ρ = −1 occurs only if they are negative multiples.

Figure 3.8 shows pairs with ρ = 0.968, −0.988 and 0.004 (p. 61). Typical uses are time series such as returns on similar companies or rainfall at nearby places, where high correlation is expected (pp. 60, 62).

**Standard deviation of a sum.**
$$\mathbf{std}(a+b) = \sqrt{\mathbf{std}(a)^2 + 2\rho\,\mathbf{std}(a)\mathbf{std}(b) + \mathbf{std}(b)^2}\tag{3.9}$$
Derivation (p. 62): $\tilde a + \tilde b$ is the de-meaned version of $a+b$, so $\mathbf{std}(a+b)^2 = \|\tilde a+\tilde b\|^2/n$. By (3.6) and $\rho = \cos\angle(\tilde a,\tilde b)$:
$$n\,\mathbf{std}(a+b)^2 = \|\tilde a\|^2 + 2\rho\|\tilde a\|\|\tilde b\| + \|\tilde b\|^2 = n\,\mathbf{std}(a)^2 + 2\rho n\,\mathbf{std}(a)\mathbf{std}(b) + n\,\mathbf{std}(b)^2.$$
Divide by n and take the root. Special cases (p. 62):
- ρ = 1 gives $\mathbf{std}(a+b) = \mathbf{std}(a)+\mathbf{std}(b)$.
- The value decreases as ρ decreases.
- ρ = 0 gives $\sqrt{\mathbf{std}(a)^2+\mathbf{std}(b)^2}$, smaller than the sum unless one is zero.
- ρ = −1 gives $|\mathbf{std}(a)-\mathbf{std}(b)|$, as small as possible.

**Hedging (p. 62).** Let a, b be return series with the same mean μ, the same std σ, and correlation ρ. Let $c = (a+b)/2$ (50% in each asset). Then $\mathbf{avg}(c) = (\mathbf{avg}(a)+\mathbf{avg}(b))/2 = \mu$. By (3.9),
$$\mathbf{std}(c) = \frac{\sqrt{2\sigma^2 + 2\rho\sigma^2}}{2} = \sigma\sqrt{(1+\rho)/2}.$$
(Added step: this uses $\mathbf{std}(a/2) = \mathbf{std}(b/2) = \sigma/2$, from the scalar property on p. 54.) The blend's risk is never more than the original risk and is smaller when ρ is smaller. For uncorrelated returns it is a factor $1/\sqrt2 = 0.707$ smaller. For ρ near −1 it is much smaller. Investing in assets with uncorrelated or negatively correlated returns is called hedging, and it reduces risk (p. 62).

*Intuition note.* The correlation is the cosine between two "wiggle patterns". Two wiggles that cancel each other (low or negative ρ) give a sum that wiggles less, which is why mixing assets with low or negative ρ reduces risk.

**Units (p. 63).** For heterogeneous entries, units affect angle, standard deviation and correlation too. The rule of thumb is to choose units so that typical entries have similar sizes or ranges (p. 63).

### 3.5 Complexity (p. 63)
Flop counts (a "flop" is one basic arithmetic operation; the square root counts as one):

| Operation | Flops |
|---|---|
| norm, RMS | 2n |
| distance | 3n |
| angle | 6n |
| de-meaning | 2n |
| standard deviation (direct) | 4n |
| standard deviation via (3.5) | 3n |
| standardizing | 5n |
| correlation coefficient | 10n |

All are of order n. The efficient std method first computes avg (n flops) and RMS (2n flops), then $\mathbf{std}(x) = (\mathbf{rms}(x)^2 - \mathbf{avg}(x)^2)^{1/2}$. Nearest neighbour of x among k n-vectors: compute k distances (3kn flops) and then find the minimum with k−1 comparisons, which can be ignored. The total is 3kn flops, of order kn (p. 63).

### Exercises (pp. 64–68)
Exercises 3.1–3.28 cover Boolean-vector distance, block-vector RMS and average, the reverse triangle inequality, norm identities, 1- and ∞-norms, Taylor approximation of the norm, Chebyshev, nearest points, hedging and leveraging, auto-correlation, mean square difference, and weighted norms (pp. 64–68). The weighted norm is $\|x\|_w = \sqrt{w_1x_1^2+\dots+w_nx_n^2}$ with positive weights (p. 68).

## Toy example (ours, not from the text)
Take $a = (1,2,3)$ and $b = (1,3,2)$, so n = 3.
- Averages: $\mathbf{avg}(a) = 6/3 = 2$ and $\mathbf{avg}(b) = 2$. De-meaned: $\tilde a = (-1,0,1)$ and $\tilde b = (-1,1,0)$.
- Norms: $\|\tilde a\|^2 = 1+0+1 = 2$ and $\|\tilde b\|^2 = 1+1+0 = 2$. So $\mathbf{std}(a)^2 = \mathbf{std}(b)^2 = 2/3$, i.e. 0.8165 each.
- Check (3.5) for a: $\mathbf{rms}(a)^2 = (1+4+9)/3 = 14/3$ and $\mathbf{avg}(a)^2 + \mathbf{std}(a)^2 = 4 + 2/3 = 14/3$. ✓
- Correlation: $\tilde a^T\tilde b = (-1)(-1) + 0\cdot1 + 1\cdot0 = 1$, so $\rho = 1/(\sqrt2\sqrt2) = 1/2$. The angle between $\tilde a$ and $\tilde b$ is $\arccos(0.5) = 60^\circ$.
- Std of the sum by formula (3.9): $\sqrt{2/3 + 2(0.5)(2/3) + 2/3} = \sqrt{2} = 1.4142$.
- Direct check: $a+b = (2,5,5)$ has average 4, de-meaned $(-2,1,1)$, squared norm 6, so $\mathbf{std} = \sqrt{6/3} = \sqrt2$. ✓
- Hedging: $c = (a+b)/2 = (1, 2.5, 2.5)$ has average 2 and deviations $(-1, 0.5, 0.5)$. Its mean square is $(1+0.25+0.25)/3 = 0.5$, so $\mathbf{std}(c) = 0.7071$. The formula $\sigma\sqrt{(1+\rho)/2} = 0.8165\times\sqrt{0.75} = 0.7071$. ✓ Both assets have risk 0.8165, and the blend has less.

## Concepts
- [[norm]] — Euclidean norm √(xᵀx); four properties; the only norm used in the book (pp. 45–46)
- [[dot-inner-product]] — xᵀy; ties norm of a sum to angles via (3.1) and (3.6) (pp. 47, 60)
- [[orthogonality]] — aᵀb = 0, angle 90°; norm-squares then add (Pythagoras) (pp. 58, 60)
- [[cosine-similarity]] — aᵀb/(‖a‖‖b‖) = cos θ; the angle between vectors, usable for documents (pp. 57, 59)
- [[root-mean-square]] (new) — rms(x) = ‖x‖/√n; typical size of an entry (p. 46)
- [[euclidean-distance]] (new) — dist(a,b) = ‖a−b‖; RMS deviation is this divided by √n (p. 48)
- [[triangle-inequality]] (new) — ‖x+y‖ ≤ ‖x‖+‖y‖; the distance form is (3.3) (pp. 46, 49)
- [[cauchy-schwarz-inequality]] (new) — |aᵀb| ≤ ‖a‖‖b‖; bounds ρ in [−1,1] (pp. 56–57, 60)
- [[chebyshev-inequality]] (new) — k/n ≤ (rms(x)/a)² for the fraction of entries with |xᵢ| ≥ a (pp. 47–48)
- [[standard-deviation]] (new) — RMS value of the de-meaned vector, divisor n (not n−1) (pp. 52–53)
- [[standardization]] (new) — z = (x − avg(x)1)/std(x); mean 0, std 1; z-scores (p. 56)
- [[correlation-coefficient]] (new) — cosine of the angle between de-meaned vectors; ρ = uᵀv/n (p. 60)
- [[nearest-neighbor]] (new) — the zⱼ with smallest ‖x−zⱼ‖ among a collection (p. 50)
- [[flop-count]] (new) — number of arithmetic operations; norm 2n, correlation 10n (p. 63)

## Canonical instances
- [[wikipedia-word-histogram-distances]] — distances (table 3.1) and angles (table 3.2) between word histograms of five articles (pp. 51, 59)
- [[house-feature-units]] — area in thousands of sq ft versus sq ft changes which houses look "close" (pp. 51–52)
- [[risk-return-and-hedging]] — avg = return, std = risk; blending two assets with equal return and equal risk σ and correlation ρ gives risk σ√((1+ρ)/2) (pp. 54, 62)
- [[spherical-distance]] — distance along a sphere of radius R is R∠(a,b) (p. 58)

## Bridges (candidates)
- [structural-analogy] Cauchy–Schwarz ⇒ cos θ ∈ [−1,1] ↔ statistics: correlation coefficient lies in [−1,1] — the same inequality bounds both.
- [same-math] Correlation coefficient ρ = cos∠(ã, b̃) ↔ cosine similarity of centred data vectors — the same formula, applied to mean-removed vectors.
- [structural-analogy] ‖x+y‖² = ‖x‖² + 2‖x‖‖y‖cosθ + ‖y‖² ↔ std(a+b)² = std(a)² + 2ρ std(a)std(b) + std(b)²: the second is the first applied to de-meaned vectors, divided by n.
- [metaphor] Choice of units changing which houses are "close" ↔ feature scaling in nearest-neighbour methods (the chapter itself proposes weighted norms in ex. 3.28).

## Questions this raises
- When is angle a better dissimilarity than distance for documents, and how do the two relate when vectors are normalized (ex. 3.24)?
- Why divide by n here but by n−1 in other texts, and when does the difference matter?
- How could one choose the weights in a weighted norm in practice (ex. 3.28)?
- The nearest-neighbour search costs 3kn flops; can it be made cheaper for large k?

## Exercises worth doing
- Ex. 3.7 (p. 64) — Chebyshev inequality: maximum number of large entries, with an extremal example — difficulty: medium
- Ex. 3.12 (p. 65) — nearest point on a line and orthogonality of (p−x) to (a−b) — difficulty: medium
- Ex. 3.15 (p. 65) — consequences of (3.5): |avg| ≤ rms, std ≤ rms, and when equality holds — difficulty: easy
- Ex. 3.19 (p. 65) — acute, orthogonal and obtuse angles read from ‖a+b‖ versus √(‖a‖²+‖b‖²) — difficulty: medium
- Ex. 3.24 (p. 66) — distance versus angle nearest neighbour; equal for normalized vectors — difficulty: medium
- Ex. 3.27 (p. 67) — mean square difference equals 2 std(x)² — difficulty: hard

## Reading notes
- Printed page = pdf page − 10. The unit covers printed pp. 45–68 (pdf 55–78).
- For printed p. 63 (pdf 73) no page image was supplied; the text layer was used and looked clean.
- Misprint check (p. 53): the book prints std(1,−2,3,2) = 1.872. My computation gives √(14/4) = √3.5 = 1.8708, which rounds to 1.871.
- The Figure 3.6 caption (p. 59) spells "acute" as "accute".
- Hedging formula (p. 62): the text layer is ambiguous; the image shows the factor /2 outside the square root.
- Exercises are listed but solutions are not printed in these pages.
