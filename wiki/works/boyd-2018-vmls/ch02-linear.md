---
id: boyd-2018-vmls/ch02-linear
work: boyd-2018-vmls
unit: Chapter 2 — Linear functions
pages: 29–44
fields: [linear-algebra]
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
# Linear functions (VMLS, Chapter 2)

## L0 — One line
A scalar-valued function of a vector is linear exactly when it is an inner product with one fixed vector, and affine functions (linear plus a constant) are the form taken by first-order Taylor approximations and regression models.

## L1 — The gist (≤ 120 words)
The chapter asks what it means for a function of a vector to be linear, and why that matters. Answer: a function $f:\mathbf R^n\to\mathbf R$ is linear if it satisfies superposition. This holds if and only if $f(x)=a^Tx$ for a unique $a$ whose entries are $f(e_i)$. Affine functions add a constant. Differentiable functions are approximated near a point by an affine function (first-order Taylor approximation). Regression models are affine functions of a feature vector. This matters because $n$ (or $n+1$) measurements fully determine a linear (or affine) function, and many real relationships are well approximated by such functions.

**Prerequisites:** vectors, scalar multiplication, inner product $a^Tx$, standard unit vectors $e_i$ and $x=x_1e_1+\dots+x_ne_n$ (identity 1.1), partial derivatives.

## L2 — Key ideas
- **Superposition defines linearity.** $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ for all vectors and scalars. It is equivalent to homogeneity plus additivity and extends to any number of terms (pp. 30–31).
- **Linear ⇔ inner product.** Every inner product with a fixed vector is linear. Every linear scalar function equals $a^Tx$ with $a=(f(e_1),\dots,f(e_n))$, and $a$ is unique (p. 31).
- **$n$ experiments suffice.** For a linear black box, $n$ calls at $e_1,\dots,e_n$ predict $f(x)$ for every $x$. The bridge-sag example shows this (pp. 31, 35).
- **Affine = linear + constant.** Affine functions satisfy superposition for all $\alpha,\beta$ with $\alpha+\beta=1$ (linear functions satisfy it for any $\alpha,\beta$). Conversely, any scalar function with this restricted property is affine, and the property gives a test for non-affinity. Formula (2.4) recovers $a$ and $b$ from $n+1$ values (pp. 32–33).
- **Maximum is not linear.** A counterexample with $n=2$ shows it fails superposition, even with $\alpha+\beta=1$, so it is not affine either (p. 32).
- **Taylor approximation is affine.** $\hat f(x)=f(z)+\nabla f(z)^T(x-z)$ is a very good approximation when all $x_i$ are near $z_i$ (p. 36).
- **Regression model.** $\hat y=x^T\beta+v$ is affine. Prepending a constant feature 1 turns it into a pure inner product, $\hat y=\tilde x^T\tilde\beta$ (p. 38).
- **Interpreting coefficients.** $\beta_i$ is the change in $\hat y$ per unit of feature $i$ with the others held fixed. In the house example, the text suggests $\beta_2$ may be negative because it measures the effect of adding a bedroom without adding area (pp. 38–41).

## L3 — Walkthrough

### 2.1 Linear functions
**Notation.** $f:\mathbf R^n\to\mathbf R$ maps an $n$-vector to a real number (scalar-valued). It can also be seen as a function of $n$ scalar arguments, $f(x)=f(x_1,\dots,x_n)$ (p. 29). Example: $f(x)=x_1+x_2-x_4^2$ on $\mathbf R^4$ ignores $x_3$. A function need not come from a formula. Example: the lift on an airplane as a function of angle of attack, air speed and air density (pp. 29–30).

**Inner product function.** For a fixed $n$-vector $a$,
$$f(x)=a^Tx=a_1x_1+\dots+a_nx_n \tag{2.1}$$
This is a weighted sum of the entries of $x$ with weights $a_i$ (p. 30).

**Superposition.** For (2.1), for all $x,y$ and scalars $\alpha,\beta$ (p. 30):
$$f(\alpha x+\beta y)=a^T(\alpha x+\beta y)=a^T(\alpha x)+a^T(\beta y)=\alpha(a^Tx)+\beta(a^Ty)=\alpha f(x)+\beta f(y).$$
A function with this property is called **linear**:
$$f(\alpha x+\beta y)=\alpha f(x)+\beta f(y). \tag{2.2}$$
The left side uses scalar–vector multiplication and vector addition. The right side uses ordinary scalar operations (p. 30). If $f$ is linear, superposition holds for any $k$ vectors: $f(\alpha_1x_1+\dots+\alpha_kx_k)=\alpha_1f(x_1)+\dots+\alpha_kf(x_k)$. The proof peels off one term at a time. Apply two-term superposition to $\alpha_1x_1+(1)(\alpha_2x_2+\dots+\alpha_kx_k)$, then repeat recursively (pp. 30–31).

Equivalent form: $f$ is linear if it has both properties (p. 31).
- **Homogeneity:** $f(\alpha x)=\alpha f(x)$.
- **Additivity:** $f(x+y)=f(x)+f(y)$.

**Inner product representation (converse).** If $f$ is linear, there is an $n$-vector $a$ with $f(x)=a^Tx$ for all $x$ (p. 31). Proof: write $x=x_1e_1+\dots+x_ne_n$ and use multi-term superposition:
$$f(x)=f(x_1e_1+\dots+x_ne_n)=x_1f(e_1)+\dots+x_nf(e_n)=a^Tx,\quad a=(f(e_1),\dots,f(e_n)).$$
So for any linear $f$,
$$f(x)=x_1f(e_1)+x_2f(e_2)+\dots+x_nf(e_n). \tag{2.3}$$
If $f$ is a subroutine or physical system, $n$ calls (or experiments) at $e_1,\dots,e_n$ let us predict $f(x)$ for any $x$ (p. 31).

**Uniqueness.** Suppose $f(x)=a^Tx$ and $f(x)=b^Tx$ for all $x$. Taking $x=e_i$ gives $f(e_i)=a^Te_i=a_i$ and $f(e_i)=b^Te_i=b_i$. So $a_i=b_i$ for every $i$, hence $a=b$ (p. 31).

*Intuition note.* A linear scalar function is completely determined by what it does to the $n$ unit vectors. Every input is a combination of those, and linearity carries the combination through the function.

**Examples** (p. 32):
- **Average:** $\mathbf{avg}(x)=(x_1+\dots+x_n)/n=a^Tx$ with $a=(1/n,\dots,1/n)=\mathbf 1/n$. It is linear.
- **Maximum:** $f(x)=\max\{x_1,\dots,x_n\}$ is not linear (except when $n=1$). Counterexample for $n=2$: $x=(1,-1)$, $y=(-1,1)$, $\alpha=\beta=1/2$. Then $f(\alpha x+\beta y)=f(0,0)=0\ne\alpha f(x)+\beta f(y)=1$.

**Affine functions.** A linear function plus a constant is **affine**. $f$ is affine if and only if $f(x)=a^Tx+b$ for some $n$-vector $a$ and scalar $b$ (the **offset**). Example: $f(x)=2.3-2x_1+1.3x_2-x_3$ has $b=2.3$ and $a=(-2,1.3,-1)$ (p. 32).

Affine functions satisfy $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ for all $x,y$ and all $\alpha,\beta$ with $\alpha+\beta=1$ (an affine combination). Linear functions satisfy it for any $\alpha,\beta$ (p. 32). Proof, using $\alpha+\beta=1$ in the second line:
$$f(\alpha x+\beta y)=a^T(\alpha x+\beta y)+b=\alpha a^Tx+\beta a^Ty+(\alpha+\beta)b=\alpha(a^Tx+b)+\beta(a^Ty+b)=\alpha f(x)+\beta f(y).$$
To show a function is not affine, find $x,y,\alpha,\beta$ with $\alpha+\beta=1$ where this equality fails. The maximum counterexample has $\alpha=\beta=1/2$, so the maximum function (with $n>1$) is not affine (p. 32).

The converse also holds: any scalar function satisfying the restricted superposition is affine (p. 33). For affine $f$ and any $x$,
$$f(x)=f(0)+x_1\big(f(e_1)-f(0)\big)+\dots+x_n\big(f(e_n)-f(0)\big). \tag{2.4}$$
(Proof is left to exercise 2.7.) So $n+1$ numbers $f(0),f(e_1),\dots,f(e_n)$ determine $f$. In $f(x)=a^Tx+b$ they give $a_i=f(e_i)-f(0)$ and $b=f(0)$ (p. 33).

Terminology: some contexts call affine functions "linear". For example, $f(x)=\alpha x+\beta$ with scalar $x$ has a line as its graph. For $\beta\ne0$ it is not linear in the standard sense. This book distinguishes the two (Figure 2.1: $f$ linear, $g$ affine but not linear) (p. 33).

*Intuition note.* In Figure 2.1 the linear $f$ passes through the origin, while the affine $g$ does not. (added step, not stated in the text: $f(0)=0$ follows from $\alpha=0$ in homogeneity, and subtracting $f(0)$ from an affine function leaves a linear one, which is why (2.4) looks like (2.3).)

**Civil engineering example.** Let $w$ be the $n$-vector of loads (metric tons) at $n$ bridge locations, and $s$ the sag (mm) at a specific point. For designed loads, the sag is very well approximated by a linear function, $s=c^Tw=c_1w_1+\dots+c_nw_n$ (p. 33). The $c_i$, in mm/ton, are called **compliances**: the sensitivity of sag to load at location $i$. The vector $c$ can be computed by solving a partial differential equation from the design. It can also be measured with (2.3): put a one-ton load $e_i$ at each location in turn, and the measured sag is $c_i$. Then predict the sag for other loadings and compare with measurements to check linearity (pp. 33, 35).

**Table 2.1** (p. 35). The three unit-load experiments give sags 0.12, 0.31, 0.26, so $c=(0.12,0.31,0.26)$. Check loads:
- $w=(0.5,1.1,0.3)$: predicted $0.06+0.341+0.078=0.479$; measured 0.481.
- $w=(1.5,0.8,1.2)$: predicted $0.18+0.248+0.312=0.740$; measured 0.736.

*Intuition note.* The model is built from only $n$ experiments and then tested on different loadings. Small prediction errors support the claim that the system is close to linear.

### 2.2 Taylor approximation
Many relations between $n$ variables and a scalar can be approximated by linear or affine functions, sometimes called a **model** to signal that it is only approximate (p. 35). Let $f$ be differentiable, meaning its partial derivatives exist. The first-order **Taylor approximation** of $f$ near the point $z$ is
$$\hat f(x)=f(z)+\frac{\partial f}{\partial x_1}(z)(x_1-z_1)+\dots+\frac{\partial f}{\partial x_n}(z)(x_n-z_n).$$
The hat marks an approximation. It is sometimes written $\hat f(x;z)$ (pp. 35–36). It is a very good approximation when all $x_i$ are near $z_i$. The first term is a constant. The other terms are the contributions to the approximate change from $f(z)$ due to changes $x_i-z_i$ (p. 36).

In inner product form:
$$\hat f(x)=f(z)+\nabla f(z)^T(x-z), \tag{2.5}$$
$$\nabla f(z)=\begin{bmatrix}\frac{\partial f}{\partial x_1}(z)\\ \vdots\\ \frac{\partial f}{\partial x_n}(z)\end{bmatrix}\ \text{(the gradient, an } n\text{-vector).} \tag{2.6}$$
Here $\hat f$ is affine in $x$ (sometimes called "linear approximation", although in general it is affine). Equivalently, $\hat f(x)=\nabla f(z)^Tx+\big(f(z)-\nabla f(z)^Tz\big)$, but (2.5) is easier to interpret (p. 36). Figure 2.3 (one variable): $\hat f$ is poor over the whole axis shown but very good for $x$ near $z$ (pp. 36–37).

**Example** (p. 36). $f(x)=x_1+\exp(x_2-x_1)$, $z=(1,2)$.
$$\nabla f(z)=\begin{bmatrix}1-\exp(z_2-z_1)\\ \exp(z_2-z_1)\end{bmatrix}=(-1.7183,\,2.7183),$$
$$\hat f(x)=3.7183+(-1.7183,2.7183)^T(x-(1,2))=3.7183-1.7183(x_1-1)+2.7183(x_2-2).$$
Table 2.2 (p. 37) gives $f$, $\hat f$ and the error $|\hat f-f|$ at five points:

| $x$ | $f(x)$ | $\hat f(x)$ | error |
|---|---|---|---|
| (1.00, 2.00) | 3.7183 | 3.7183 | 0.0000 |
| (0.96, 1.98) | 3.7332 | 3.7326 | 0.0005 |
| (1.10, 2.11) | 3.8456 | 3.8455 | 0.0001 |
| (0.85, 2.05) | 4.1701 | 4.1119 | 0.0582 |
| (1.25, 2.41) | 4.4399 | 4.4032 | 0.0367 |

*Intuition note.* Near $z$, a smooth function looks like a flat tilted plane. The gradient gives the tilt. In Table 2.2 the error is 0.0000 at $z$ itself and at most 0.0005 at the next two points, and larger (0.0582 and 0.0367) at the last two points.

### 2.3 Regression model
The **regression model** is the affine function
$$\hat y=x^T\beta+v, \tag{2.7}$$
with $\beta$ an $n$-vector and $v$ a scalar (p. 38).
- The entries of $x$ are the **regressors**.
- $\hat y$ is the **prediction** of a true value $y$ (the dependent variable, outcome, or label).
- $\beta$ is the weight (coefficient) vector.
- $v$ is the offset (intercept).
- Together, $\beta$ and $v$ are the **parameters**. Chapter 13 shows how to estimate them from data.

**Interpretation** (p. 38). $\beta_i$ is the amount by which $\hat y$ increases (if $\beta_i>0$) when feature $i$ increases by one, other features unchanged. If $\beta_i$ is small, $\hat y$ does not depend too strongly on feature $i$. $v$ is the value of $\hat y$ when all features are 0.

**Boolean features** (values 0 or 1) make the model very interpretable. Lifespan example: $x_1=1$ if male (0 if female), $x_2=1$ if type II diabetic, $x_3=1$ if smoker. Then $v$ is the estimated lifespan of a female nondiabetic nonsmoker. $\beta_1,\beta_2,\beta_3$ are the changes in estimated lifespan for being male, diabetic, or a smoker. In a model fit to real data all three coefficients would be negative (p. 38).

**Simplified notation** (p. 38). Stack $\tilde x=(1,x)$ with $n+1$ entries and $\tilde\beta=(v,\beta)$. Then
$$\hat y=x^T\beta+v=\begin{bmatrix}1\\x\end{bmatrix}^T\begin{bmatrix}v\\\beta\end{bmatrix}=\tilde x^T\tilde\beta. \tag{2.8}$$
Often the tildes are dropped and the first feature is assumed to be the constant 1.

**House price model** (pp. 39–41). $y$ is the selling price in thousands of dollars; $x_1$ is the area in 1000 sq ft; $x_2$ is the number of bedrooms. Parameters found by the methods of chapter 13 from 774 Sacramento sales:
$$\beta=(148.73,\,-18.85),\qquad v=54.40. \tag{2.9}$$
Table 2.3 (p. 39) lists five houses (area, beds, price $y$, prediction $\hat y$):

| House | $x_1$ | $x_2$ | $y$ | $\hat y$ |
|---|---|---|---|---|
| 1 | 0.846 | 1 | 115.00 | 161.37 |
| 2 | 1.324 | 2 | 234.50 | 213.61 |
| 3 | 1.150 | 3 | 198.00 | 168.88 |
| 4 | 3.037 | 4 | 528.00 | 430.67 |
| 5 | 3.984 | 5 | 572.50 | 552.66 |

Figure 2.4 (p. 40) is a scatter plot of predicted against actual price for all 774 houses. The model gives reasonable but not very accurate predictions (p. 39). Practical models use many more regressors and are much more accurate (p. 39).

Reading the parameters (p. 41):
- $\beta_1=148.73$: predicted price rises by 148.73 thousand dollars per extra 1000 sq ft, with the same number of bedrooms.
- $\beta_2=-18.85$: change in predicted price when a bedroom is added with total area held constant. The text says it might be negative because area is held fixed. If an added bedroom also adds more than around 127 sq ft, the model predicts a price increase.
- $v=54.40$: predicted price for a house with no area and no bedrooms, perhaps read as the lot value. The text calls these interpretations dubious for such a crude model.

*Intuition note.* Each coefficient answers "what changes if only this feature changes?". A coefficient can look odd, such as a negative bedroom effect, because it describes a change with the other feature (area) held fixed (p. 41).

## Toy example (ours, not from the text)
A black-box scalar function $f$ of 3-vectors is known to be linear. Experiments give $f(e_1)=2$, $f(e_2)=-1$, $f(e_3)=4$. By (2.3), $a=(2,-1,4)$.
- Predict $f(2,3,1)=2\cdot2+3\cdot(-1)+1\cdot4=4-3+4=5$.

Now let $g(x)=f(x)+1$ (affine, $b=1$). Then $g(0)=1$, $g(e_1)=3$, $g(e_2)=0$, $g(e_3)=5$. By (2.4):
- $g(2,3,1)=1+2(3-1)+3(0-1)+1(5-1)=1+4-3+4=6$.
- Direct check: $f(2,3,1)+1=6$. ✓.
- Recovered: $a_i=g(e_i)-g(0)=(2,-1,4)$ and $b=g(0)=1$.

Restricted superposition check for $g$ with $x=e_1$, $y=e_2$, $\alpha=\beta=1/2$: $g(\tfrac12,\tfrac12,0)=\tfrac12(2)+\tfrac12(-1)+1=1.5$, and $\tfrac12g(e_1)+\tfrac12g(e_2)=\tfrac12(3)+\tfrac12(0)=1.5$. ✓.

## Concepts
- [[linear-map-transformation]] — here a scalar-valued function satisfying superposition (2.2), equivalently homogeneity plus additivity (pp. 30–31)
- [[superposition]] (new) — $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$; the defining property of linearity (p. 30)
- [[dot-inner-product]] — $a^Tx$ is the weighted sum of the entries of $x$; every linear scalar function has this form with a unique $a$ (pp. 30–31)
- [[affine-function]] (new) — linear plus a constant, $a^Tx+b$; restricted superposition holds when $\alpha+\beta=1$ (linear functions satisfy it for any $\alpha,\beta$) (p. 32)
- [[affine-combination]] (new) — a linear combination whose coefficients sum to 1 (p. 32)
- [[taylor-approximation-first-order]] (new) — $\hat f(x)=f(z)+\nabla f(z)^T(x-z)$, an affine model near $z$ (p. 36)
- [[gradient]] (new) — $n$-vector of partial derivatives of $f$ at $z$ (p. 36)
- [[regression-model]] (new) — affine prediction $\hat y=x^T\beta+v$ from a feature vector (p. 38)
- [[linear-independence]] — not used in this unit.
- [[basis]] — the unit vectors $e_i$ are used to decompose $x$, though the word is not used (p. 31)

## Canonical instances
- [[bridge-sag-compliance]] (new) — linear model $s=c^Tw$ fitted with unit-load experiments (pp. 33, 35)
- [[max-function-not-linear]] (new) — counterexample to superposition for $\max$ (p. 32)
- [[taylor-exp-example]] (new) — $f(x)=x_1+\exp(x_2-x_1)$ approximated at $z=(1,2)$ (p. 36)
- [[house-price-regression]] (new) — Sacramento house-price model with negative bedroom coefficient (pp. 39–41)
- [[lifespan-boolean-regression]] (new) — Boolean features in a lifespan regression (p. 38)

## Bridges (candidates)
- [structural-analogy] Taylor approximation $\hat f(x)=f(z)+\nabla f(z)^T(x-z)$ ↔ calculus: tangent line / linearization of a function at a point — same idea in $n$ variables.
- [same-math] Regression prediction $\hat y=\tilde x^T\tilde\beta$ with a constant feature ↔ machine learning: linear model with bias absorbed into the weight vector.
- [structural-analogy] Determining $f$ from $f(e_i)$ ↔ matrix as transformation: columns of $A$ are the images of the basis vectors (the scalar case is a single row).
- [structural-analogy] "$n+1$ measurements fix an affine function" ↔ system identification / calibration of a sensor from reference inputs.

## Questions this raises
- How are the regression parameters $\beta$ and $v$ actually estimated from many observations (the text points to chapter 13)?
- For vector-valued linear functions, does the same unit-vector argument give a matrix instead of a vector $a$?
- How large can $\|x-z\|$ be before a Taylor model becomes poor, and what second-order terms would improve it?
- When features are strongly related, can the sign of a coefficient (such as $\beta_2<0$) still be trusted as a causal statement?

## Exercises worth doing
- Ex. 2.1 (p. 42) — decide linearity of spread, last-minus-first, median, odd/even average, extrapolation; give counterexamples — difficulty: easy
- Ex. 2.2 (p. 42) — fit the affine model $T=a^TP+b$ from four measurements and solve a constraint — difficulty: medium
- Ex. 2.4 (p. 43) — linearity from three values: "must", "could" or "cannot" be linear — difficulty: medium
- Ex. 2.5 (p. 43) — what an affine function's two values determine, and what they do not — difficulty: medium
- Ex. 2.7 (p. 43) — prove formula (2.4) for affine functions — difficulty: easy
- Ex. 2.9 (p. 43) — Taylor approximation of $x_1x_2$ at $(1,1)$ and its accuracy at four points — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (pdf 39 = printed 29). Unit covers printed pp. 29–44, including exercises 2.1–2.12 (pp. 42–44). The text of §2.3 ends on p. 41 and has no further sections in these pages.
- In the text layer, bold symbols lose their bold. In the Average example the image shows $a=(1/n,\dots,1/n)=\mathbf 1/n$, with $\mathbf 1$ the all-ones vector. The gradient matrix (2.6) and the regression stack (2.8) are garbled in the text layer. I used the images.
- The exercises are listed only; no solutions are printed in these pages.
- The Taylor example in Table 2.2 reports errors to four decimals. I did not recompute them.
