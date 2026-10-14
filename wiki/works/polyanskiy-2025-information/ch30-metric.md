---
id: polyanskiy-2025-information/ch30-metric
work: polyanskiy-2025-information
unit: "Chapter 27: Metric entropy (unit id ch30-metric)"
pages: "522–554"
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Metric entropy

## L0 — One line
The metric entropy of a set is the logarithm of the number of ε-balls needed to cover it (equivalently, of a maximal ε-separated packing); volume ratios bound it (giving order $\epsilon^{-d}$) for small ε in fixed dimension, and Gaussian-process, random-covering, small-ball and rate–distortion arguments handle the other regimes.

## L1 — The gist (≤ 120 words)
How many balls of radius ε cover a set Θ (covering number N), or how many points can be pairwise more than ε apart inside it (packing number M)? Their logarithm is the metric entropy. N and M sandwich each other. For a compact Θ in $\mathbb R^d$ with nonempty interior, volume ratios give N and M of order $\epsilon^{-d}$ for small ε, with constants depending on Θ and the norm. These bounds are loose in high dimension, for example for the ℓ1-ball measured in ℓ2. Other tools (Gaussian processes, random coverings, small-ball probabilities, rate–distortion) then apply. Smooth function classes on $[0,A]^d$ have log N of order $\epsilon^{-d/\beta}$. This links to rate–distortion, statistics, and Hilbert's 13th problem.

**Prerequisites:** norms and balls; volume scaling in $\mathbb R^d$; triangle inequality; Gaussian vectors; mutual information, Fano's inequality, binary entropy h; the rate–distortion function (Ch. 24–26 of the book).

## L2 — Key ideas
- **Covering vs packing.** N(Θ,d,ε) is the fewest ε-balls covering Θ. M(Θ,d,ε) is the most points of Θ pairwise more than ε apart. They satisfy $M(2\epsilon)\le N(\epsilon)\le M(\epsilon)$. So a lower bound on N (or an upper bound on M) from a "converse" turns into an achievability statement via a greedy construction (pp. 523–525).
- **Volume bound.** In $\mathbb R^d$ with any norm, $N$ and $M$ are bounded by ratios of volumes (Thm 27.3). For compact Θ with nonempty interior, $N\asymp M\asymp\epsilon^{-d}$ for small ε, with constants depending on Θ and the norm (pp. 525–527). The same argument with counting measure gives the Gilbert–Varshamov and Hamming bounds on Hamming space (p. 527).
- **Limits of volume.** Volume bounds are loose once ε scales with d. For the ℓ1-unit ball under ℓ2, volume gives the right order only for $\epsilon\lesssim 1/\sqrt d$. Thm 27.7 gives the full behaviour: $d\log\frac{e}{\epsilon^2 d}$ for $\epsilon\le 1/\sqrt d$ and $\epsilon^{-2}\log(e\epsilon^2 d)$ for $\epsilon\ge1/\sqrt d$ (pp. 528–530).
- **Tools beyond volume.** *Gaussian width* is $w(\Theta)=\mathbb E\sup_{\theta\in\Theta}\langle\theta,Z\rangle$, $Z\sim\mathcal N(0,I_d)$. *Sudakov minoration* says $w(\Theta)\gtrsim\sup_\epsilon\epsilon\sqrt{\log M(\epsilon)}$, with a dimension-free constant (p. 531). *Maurey's empirical method* covers the convex hull of a finite set T in an inner-product space by random averages, with a count that does not depend on the dimension (p. 534). A duality of Artstein–Milman–Szarek relates covering numbers of K and of the polar body (p. 535).
- **Hilbert ball.** The unit ball of $\ell_2(\mathbb R^\infty)$ is not compact, so it cannot have finite ε-nets for all ε in ℓ2. Under the metric $d_P$ induced by a distribution P with $\mathbb E\|X\|^2\le1$, however, $\log N\le c/\epsilon^2$ (Thm 27.11, pp. 532–533).
- **Smooth function classes.** For L-Lipschitz densities on $[0,A]$, $\log N=\Theta(1/\epsilon)$ in every $\|\cdot\|_p$, with sharp constant $LA/\epsilon$ (in $\log_2$) for the sup-norm as ε→0. For Hölder-β densities on $[0,A]^d$ it is $\Theta(\epsilon^{-d/\beta})$ (Thms 27.13–27.14, pp. 536–538).
- **Hilbert's 13th problem.** The text says the index d/β allows an impossibility proof by entropy comparison; Vitushkin proved the smooth version of Hilbert's conjecture. The text proves only a simple case: a 1-Lipschitz function of three variables that is not $g(h_1(x,y),h_2(y,z))$ with 1-Lipschitz g, h1, h2 (pp. 538–539).
- **Small-ball link.** Let $\phi(\epsilon)=\log\frac1{\mathbb P[\|X\|\le\epsilon]}$. For a Gaussian measure γ with RKHS unit ball K (the unit ball of the Hilbert space attached to γ), Thm 27.15 gives two-sided bounds on $\log N$ at shifted scales: $\phi(2\epsilon)-\log2\le\log N(\epsilon/\sqrt{2\phi(\epsilon/2)})\le2\phi(\epsilon/2)$. If $\phi(\epsilon)\asymp\phi(\epsilon/2)$, then approximately $\log N(\epsilon/\sqrt{\phi(\epsilon)})\asymp\phi(\epsilon)$. For power-log rates, (27.44) gives an equivalence of the two behaviours (pp. 540–541).
- **Rate–distortion link.** Let $\phi_{\mathcal X}$ be the worst case over source laws of the rate–distortion function. Then for $0<c<1/2$: $\phi_{\mathcal X}(\epsilon)\le\log N\le\log M\le\frac{\phi_{\mathcal X}(c\epsilon)+\log2}{1-2c}$. The upper comparison is at distortion $c\epsilon$ and uses Fano's inequality (Thm 27.16, p. 542). For the unit sphere this gives rate–distortion $\approx(d-1)\log\frac1\epsilon$, matching Cor. 27.4 (p. 543).

## L3 — Walkthrough

### 27.0 Introduction (p. 522)
The chapter treats worst-case (deterministic) quantization. The two key quantities are the covering number and the packing number. The author says Kolmogorov founded the theory, motivated by Hilbert's 13th problem (p. 522). Applications named: approximation theory, empirical processes, small-ball probability, statistics and learning (p. 522). Metric entropy will be used for statistical lower and upper bounds in Part VI (p. 522).

### 27.1 Covering and packing (pp. 522–525)
**Definition 27.1.** Let (V,d) be a metric space and Θ ⊂ V (pp. 522–523).
- $\{v_1,\dots,v_N\}\subset V$ is an *ε-covering* (ε-net) if $\Theta\subset\cup_i B(v_i,\epsilon)$, with $B(v,\epsilon)=\{u:d(u,v)\le\epsilon\}$ the closed ball. Equivalently, every θ ∈ Θ has some i with $d(\theta,v_i)\le\epsilon$.
- $\{\theta_1,\dots,\theta_M\}\subset\Theta$ is an *ε-packing* if $\min_{i\ne j}\|\theta_i-\theta_j\|>\epsilon$ (strict, "for convenience"). Equivalently, the balls $B(\theta_i,\epsilon/2)$ are disjoint.

$$N(\Theta,d,\epsilon)\triangleq\min\{n:\exists\ \epsilon\text{-covering of size }n\}\tag{27.1}$$
$$M(\Theta,d,\epsilon)\triangleq\max\{m:\exists\ \epsilon\text{-packing of size }m\}\tag{27.2}$$
with $\min\emptyset=\infty$ (p. 523).

Remarks (p. 523):
- As printed, N and M are "non-decreasing and right-continuous" in ε (this looks like a slip: larger ε needs fewer balls; see Reading notes), and non-decreasing in Θ under set inclusion.
- Θ is *totally bounded* (e.g. compact) if $N<\infty$ for all ε>0. In Euclidean spaces this is equivalent to Θ being bounded.
- $\log N$ and $\log M$ are the *metric entropy*; Kolmogorov–Tikhomirov call them ε-capacity and ε-entropy.
- The *entropy numbers* are $e_k(\Theta)=\inf\{\epsilon:N(\Theta,d,\epsilon)\le2^{k-1}\}$. In particular $e_1(\Theta)=\mathrm{rad}(\Theta)$.

**Remark 27.1 (p. 524).** N depends on the ambient space V, because covering points must lie in V. Let $N'$ be the covering number when the centres must lie in Θ. Then
$$N(\Theta,d,\epsilon)\le N'(\Theta,d,\epsilon)\le N(\Theta,d,\epsilon/2).\tag{27.3}$$
The left inequality is obvious. For the right one, take an $\epsilon/2$-covering $\{\theta_i\}$ and project each $\theta_i$ to $\theta_i'=\arg\min_{u\in\Theta}d(\theta_i,u)$. For θ ∈ Θ with $d(\theta,\theta_i)\le\epsilon/2$: $d(\theta,\theta_i')\le d(\theta,\theta_i)+d(\theta_i,\theta_i')\le2d(\theta,\theta_i)\le\epsilon$. $N'$ need not be monotone under set inclusion.

**Theorem 27.2 (Kolmogorov–Tikhomirov).**
$$M(\Theta,d,2\epsilon)\le N(\Theta,d,\epsilon)\le M(\Theta,d,\epsilon).\tag{27.4}$$
*Proof* (p. 524).
- *Right inequality.* Take a maximal packing $E=\{\theta_1,\dots,\theta_M\}$. Every θ ∈ Θ∖E has some i with $d(\theta,\theta_i)\le\epsilon$, otherwise θ could be added. So E is an ε-covering inside Θ, and $N\le M$.
- *Left inequality.* Suppose a 2ε-packing of size M and an ε-covering of size N with $M\ge N+1$. By pigeonhole, two distinct packing points lie in the same ε-ball $B(x_k,\epsilon)$. By the triangle inequality they are at distance ≤ 2ε, contradicting the packing property.

The right inequality corresponds to a *greedy construction*: keep adding points until none can be added (p. 525). Converses (lower bounds on N, upper bounds on M) are often easier than constructions. Combined with $N\le M$ they become achievability statements, like duality in optimization (p. 524 and fn. 3).

*Intuition note.* Covering and packing are two views of the same size, up to a factor 2 in ε. A maximal packing is automatically a covering, so one can bound whichever side is easier. Small-ε behaviour of N and M is therefore essentially the same.

### 27.2 Finite-dimensional space and volume bound (pp. 525–528)
**Theorem 27.3.** Let $\|\cdot\|$ be any norm on $\mathbb R^d$ and $B$ its unit ball. For any $\Theta\subset\mathbb R^d$,
$$\Big(\tfrac1\epsilon\Big)^d\frac{\mathrm{vol}(\Theta)}{\mathrm{vol}(B)}\overset{(a)}{\le}N\le M\overset{(b)}{\le}\frac{\mathrm{vol}(\Theta+\frac\epsilon2B)}{\mathrm{vol}(\frac\epsilon2B)}\overset{(c)}{\le}\Big(\tfrac3\epsilon\Big)^d\frac{\mathrm{vol}(\Theta)}{\mathrm{vol}(B)},$$
where (c) needs the extra condition that Θ is convex and contains $\epsilon B$ (p. 525).

*Proof* (p. 525).
- (a) Take an ε-covering. The union bound gives $\mathrm{vol}(\Theta)\le\sum_i\mathrm{vol}(B(\theta_i,\epsilon))=N\epsilon^d\mathrm{vol}(B)$, by translation invariance and scaling of volume.
- (b) Take an ε-packing in Θ. The balls $B(\theta_i,\epsilon/2)$ are disjoint and lie in $\Theta+\frac\epsilon2B$. Hence $\mathrm{vol}(\Theta+\frac\epsilon2B)\ge M\,\mathrm{vol}(\frac\epsilon2B)$.
- (c) Two facts. (1) If $\epsilon B\subset\Theta$ then $\Theta+\frac\epsilon2B\subset\Theta+\frac12\Theta$. (2) If Θ is convex then $\Theta+\frac12\Theta=\frac32\Theta$. For (2): each point of $\frac32\Theta$ is $\theta=\frac13\theta+\frac23\theta$ with $\frac13\theta\in\frac12\Theta$ and $\frac23\theta\in\Theta$, which gives "⊂ Θ+½Θ". Conversely, for $x=y+\frac12z$ with $y,z\in\Theta$, convexity gives $\frac23x=\frac23y+\frac13z\in\Theta$, so $x\in\frac32\Theta$.

**Remark 27.2.** Starting from $\Theta+\frac\epsilon2B\subset\cup_iB(\theta_i,\frac{3\epsilon}2)$ one gets
$$(2/3)^d\le\frac{N(\Theta,\|\cdot\|,\epsilon)}{\mathrm{vol}(\Theta+\frac\epsilon2B)/\mathrm{vol}(\epsilon B)}\le2^d.$$
So the volume of the fattened set determines the metric entropy up to constants depending only on d. This fattening reappears in §27.5 (p. 525).

**Corollary 27.4 (balls and spheres).** For ε<1, with B the unit ball and S the unit sphere,
$$\Big(\tfrac1\epsilon\Big)^d\le N(B,\|\cdot\|,\epsilon)\le\Big(1+\tfrac2\epsilon\Big)^d\tag{27.5}$$
$$\Big(\tfrac1{2\epsilon}\Big)^{d-1}\le N(S,\|\cdot\|,\epsilon)\le2d\Big(1+\tfrac1\epsilon\Big)^{d-1}\tag{27.6}$$
The left inequality in (27.6) needs $\|\cdot\|$ to be an absolute norm (invariant to sign changes of coordinates) (p. 526).

*Proof* (p. 526).
- *Balls.* (27.5) follows from Thm 27.3, since $B+\frac\epsilon2B=(1+\frac\epsilon2)B$.
- *Sphere, upper bound.* The source writes $N\le M\le\frac{\mathrm{vol}(S+\epsilon B)}{\mathrm{vol}(\epsilon B)}\le\frac{\mathrm{vol}((1+\epsilon)B)-\mathrm{vol}((1-\epsilon)B)}{\mathrm{vol}(\epsilon B)}$, using $S+\epsilon B\subset((1+\epsilon)B)\setminus((1-\epsilon)B)$. Then
$$\frac{(1+\epsilon)^d-(1-\epsilon)^d}{\epsilon^d}=\frac d{\epsilon^d}\int_{-\epsilon}^{\epsilon}(1+x)^{d-1}dx\le2d\Big(1+\frac1\epsilon\Big)^{d-1}.$$
- *Sphere, lower bound.* The sphere has zero volume, so (a) cannot be used. Let $\|x\|'=\|(x,0)\|$, a norm on $\mathbb R^{d-1}$. Every ε-packing of the unit $\|\cdot\|'$-ball induces an ε-packing of the unit sphere:
  1. For x with $\|(x,0)\|\le1$, set $f(y)=\|(x,y)\|$. For an absolute norm f is continuous and increasing, with $f(0)\le1$ and $f(\infty)=\infty$.
  2. By the mean value theorem there is $y_x$ with $\|(x,y_x)\|=1$.
  3. For a packing $\{x_i\}$ set $x_i'=(x_i,y_{x_i})$. Then $\|x_i'-x_j'\|\ge\|(x_i-x_j,0)\|=\|x_i-x_j\|'\ge\epsilon$.
  
  So $M(S,\|\cdot\|,\epsilon)\ge M(B',\|\cdot\|',\epsilon)$.
- *Finishing* (added step): $N(S,\epsilon)\ge M(S,2\epsilon)\ge M(B',2\epsilon)\ge N(B',2\epsilon)\ge(2\epsilon)^{-(d-1)}$ by (27.4) and (27.5).

**Remark 27.3** (pp. 526–527).
- (a) For any compact Θ with nonempty interior, for small ε,
$$N(\Theta,\|\cdot\|,\epsilon)\asymp M(\Theta,\|\cdot\|,\epsilon)\asymp\epsilon^{-d},\tag{27.7}$$
with constants depending on Θ and the norm. The sharp constant exists: $M(\Theta,\|\cdot\|,2\epsilon)=(\tau+o(1))\frac{\mathrm{vol}(\Theta)}{\mathrm{vol}(B)}\epsilon^{-d}$ for Θ of positive volume. Here τ depends only on the norm and d and is the maximal sphere-packing density. Computing τ is very hard and open except in special cases. For ℓ∞ and ℓ1 balls τ = 1, and for the ℓ2-ball in d = 2, $\tau=\pi/\sqrt{12}$ (fn. 4).
- (b) For a smooth manifold one may expect $(1/\epsilon)^{\dim}$, with dim the manifold's dimension rather than the ambient one. This holds in many situations, for example for O(d), U(d) and Grassmannians, with $\dim=d(d-1)/2$ for O(d). In general one may define $\lim_{\epsilon\to0}\frac{\log N}{\log(1/\epsilon)}$ as the Minkowski (box-counting) dimension. For fractal sets it can be non-integer, e.g. $\log_23$ for the Cantor set.
- (c) All norms on $\mathbb R^d$ are equivalent up to dimension-dependent factors, so (27.7) holds for any norm when d is fixed. It does not capture high dimensions where ε depends on d; see §27.3.

*Intuition note.* In fixed dimension a set with interior "looks like" a small cube, so you need about $\epsilon^{-d}$ balls. The constants hide the geometry of Θ and the norm.

**Hamming space.** $M(\mathbb F_2^d,r)\equiv M(\mathbb F_2^d,d_H,r)$ is the maximal number of binary codewords of length d with minimum distance r+1 (strict inequality in Def. 27.1) (p. 527).

**Theorem 27.5.** For any integer $1\le r\le d-1$,
$$\frac{2^d}{\sum_{i=0}^r\binom di}\le M(\mathbb F_2^d,r)\le\frac{2^d}{\sum_{i=0}^{\lfloor r/2\rfloor}\binom di}.\tag{27.8}$$
*Proof:* the argument of Thm 27.3 with $\mathbb R^d$ replaced by $\mathbb F_2^d$ and volume by counting measure (p. 527). The lower and upper bounds are the Gilbert–Varshamov and Hamming bounds.

For $r=\rho d$, $\rho\in(0,1)$, $d\to\infty$, using binomial asymptotics: $2^{d(1-h(\rho))+o(d)}\le M(\mathbb F_2^d,\rho d)\le2^{d(1-h(\rho/2))+o(d)}$ (pp. 527–528). The exact exponent is described as a major open question in coding theory. The best known upper bound is from McEliece–Rodemich–Rumsey–Welch via linear programming (p. 528). The covering problem is simpler and tight:
$$N(\mathbb F_2^d,\rho d)=2^{dR(\rho)+o(d)},\quad R(\rho)=(1-h(\rho))_+,\tag{27.9}$$
the rate–distortion function of Ber(1/2). It does not follow automatically from rate–distortion theory but can be shown by a similar argument (Exercise V.26) (p. 528).

**Theorem 27.6 (GV bound for Hamming spheres).** Let $S_k^d=\{x\in\mathbb F_2^d:w_H(x)=k\}$ (27.10). Then
$$M(S_k^d,r)\ge\frac{\binom dk}{\sum_{i=0}^r\binom di},\qquad\log M(S_k^d,k/2)\ge\frac k2\log\frac d{2ek}.\tag{27.11, 27.12}$$
*Proof.* (27.11) is the volume argument. For (27.12): for $r\le d/2$, $\sum_{i\le r}\binom di\le\exp(d\,h(r/d))$. Then use $h(x)\le x\log\frac ex$ and $\binom dk\ge(d/k)^k$ (p. 528).

### 27.3 Beyond the volume bound (pp. 528–535)
Volume methods give $\epsilon^{-d}$ as ε→0, but the author says one expects a critical threshold of ε depending on d, below which the exponential asymptotics is tight and above which the covering number can grow polynomially in d. This phenomenon is "not fully captured" by volume (p. 528).

**Case study: $M(B_1,\|\cdot\|_2,\epsilon)$**, the unit ℓ1-ball covered by ℓ2-balls (pp. 529–530). Norm equivalence $\|x\|_2\le\|x\|_1\le\sqrt d\|x\|_2$ is too loose for large d.
- Volumes: $\mathrm{vol}(B_q)=\frac{[2\Gamma(1+1/q)]^d}{\Gamma(1+d/q)}$ (27.13). So $\mathrm{vol}(B_1)=2^d/d!$ and $\mathrm{vol}(B_2)=\pi^{d/2}/\Gamma(1+d/2)$, and by Stirling
$$\mathrm{vol}(B_1)^{1/d}\asymp\tfrac1d,\qquad\mathrm{vol}(B_2)^{1/d}\asymp\tfrac1{\sqrt d}.\tag{27.14}$$
- Upper bound, for an absolute constant C, using $B_2\subset\sqrt dB_1$ (Cauchy–Schwarz):
$$M\le\frac{\mathrm{vol}(B_1+\frac\epsilon2B_2)}{\mathrm{vol}(\frac\epsilon2B_2)}\le\frac{\mathrm{vol}((1+\frac{\epsilon\sqrt d}2)B_1)}{\mathrm{vol}(\frac\epsilon2B_2)}\le\Big(C\big(1+\tfrac1{\epsilon\sqrt d}\big)\Big)^d.\tag{27.15}$$
The step is tight in the sense $\mathrm{vol}(B_1+\frac\epsilon2B_2)^{1/d}\gtrsim\max\{\frac1d,\frac\epsilon{\sqrt d}\}$.
- Lower bound, for an absolute constant c:
$$M\ge\frac{\mathrm{vol}(B_1)}{\mathrm{vol}(\epsilon B_2)}=\Big(\frac c{\epsilon\sqrt d}\Big)^d.\tag{27.16}$$
- Conclusion: for $\epsilon\le1/\sqrt d$, $M^{1/d}\asymp\frac1{\epsilon\sqrt d}$. For $\epsilon\gg1/\sqrt d$ the lower bound trivializes and the upper bound is loose, so another method is needed (p. 529).

**Theorem 27.7.** For $0<\epsilon<1$, $d\in\mathbb N$:
$$\log M(B_1,\|\cdot\|_2,\epsilon)\asymp\begin{cases}d\log\frac{e}{\epsilon^2d}&\epsilon\le\frac1{\sqrt d}\\[2pt]\frac1{\epsilon^2}\log(e\epsilon^2d)&\epsilon\ge\frac1{\sqrt d}\end{cases}$$
*Proof* (p. 530). The case $\epsilon\le1/\sqrt d$ is (27.15)–(27.16). Take $1/\sqrt d\le\epsilon<1$.
- *Upper bound (quantize each coordinate).* Assume ε<1/4 and fix δ<1.
  1. For θ ∈ B1 there is $x\in(\delta\mathbb Z^d)\cap B_1$ with $\|x-\theta\|_\infty\le\delta$.
  2. Then $\|x-\theta\|_2^2\le\|x-\theta\|_1\|x-\theta\|_\infty\le2\delta$.
  3. $x/\delta$ lies in $\mathcal Z=\{z\in\mathbb Z^d:\sum|z_i|\le k\}$ with $k=\lfloor1/\delta\rfloor$ (27.17). Each z has at most k nonzeros.
  4. Stars-and-bars plus signs give $|\mathcal Z|\le2^{k\wedge d}\binom{d-1+k}{k}$.
  5. Pick $\delta=\epsilon^2/2$. Then $N(B_1,\|\cdot\|_2,\epsilon)\le|\mathcal Z|\le(\frac{2e(d+k)}k)^k$.
  
  This also recovers the volume bound for $\epsilon\le1/\sqrt d$, where k ≤ d.
- *Lower bound.* $M(B_1,\|\cdot\|_2,\sqrt2)\ge2d$ from $\pm e_i$, so assume d ≥ 8 and $\epsilon>\frac1{4\sqrt d}$.
  1. Fix $1\le k\le d$. By (27.12) there is a k/2-packing $\{x_i\}\subset S_k^d$ with $\log M\ge\frac k2\log\frac d{2ek}$.
  2. Set $\theta_i=x_i/k\in B_1$. Then $\|\theta_i-\theta_j\|_2^2=\frac1{k^2}d_H(x_i,x_j)\ge\frac1{2k}$.
  3. Choosing $k=\lfloor1/\epsilon^2\rfloor\le d/8$ gives an $\epsilon/2$-packing of $B_1$ in ℓ2 of the claimed size.

The same elementary proof gives (Exercise V.27), for $1\le p<q\le\infty$, $\frac1s\triangleq\frac1p-\frac1q$:
$$\log M(B_p,\|\cdot\|_q,\epsilon)\asymp_{p,q}\begin{cases}d\log\frac e{\epsilon^sd}&\epsilon\le d^{-1/s}\\ \frac1{\epsilon^s}\log(e\epsilon^sd)&\epsilon\ge d^{-1/s}\end{cases}\tag{27.18}$$

*Intuition note.* Below scale $1/\sqrt d$ the ℓ1-ball behaves like a d-dimensional body: the entropy is $d\log\frac e{\epsilon^2d}$, which is about d times a log factor. Above it the entropy is about $\epsilon^{-2}$ up to a log, which is much smaller than the volume upper bound.

#### 27.3.1 Sudakov's minoration (pp. 530–532)
**Theorem 27.8.** The *Gaussian width* of $\Theta\subset\mathbb R^d$ is
$$w(\Theta)\triangleq\mathbb E\sup_{\theta\in\Theta}\langle\theta,Z\rangle,\quad Z\sim\mathcal N(0,I_d)\tag{27.19}$$
(to avoid measurability issues, read it as the sup over finite $T\subset\Theta$ of $\mathbb E\max_{\theta\in T}\langle\theta,Z\rangle$; fn. 8). Then
$$w(\Theta)\gtrsim\sup_{\epsilon>0}\epsilon\sqrt{\log M(\Theta,\|\cdot\|_2,\epsilon)}.\tag{27.20}$$
The constant is independent of the dimension. The text says Sudakov's bound is tight up to a $\log d$ factor (citing a reference), and the complementary Dudley chaining inequality is
$$w(\Theta)\lesssim\int_0^\infty\sqrt{\log M(\Theta,\|\cdot\|_2,\epsilon)}\,d\epsilon\tag{27.22}$$
(Exercise V.28) (p. 531).

*Corollary (Urysohn's inequality).* Applying the volume lower bound on M from Thm 27.3 to (27.20) and optimizing over ε,
$$w(\Theta)\gtrsim\sqrt d\Big(\frac{\mathrm{vol}(\Theta)}{\mathrm{vol}(B_2)}\Big)^{1/d}\asymp d\cdot\mathrm{vol}(\Theta)^{1/d}\tag{27.21}$$
(using (27.14)). A sharp form (cited from the literature) says balls minimize Gaussian width among symmetric convex bodies of equal volume (fn. 9) (p. 531).

**Lemma 27.9 (Slepian).** Let X and Y be Gaussian random vectors in $\mathbb R^n$. If $\mathbb E(Y_i-Y_j)^2\le\mathbb E(X_i-X_j)^2$ for all i, j, then $\mathbb E\max Y_i\le\mathbb E\max X_i$ (p. 531; proof cited, not given).

**Lemma 27.10.** For $Z_i\sim\mathcal N(0,1)$ (any dependence): $\mathbb E[\max_{i\in[n]}Z_i]\le\sqrt{2\log n}$ (27.23). If the $Z_i$ are i.i.d., $\mathbb E[\max Z_i]=\sqrt{2\log n}(1+o(1))$ (27.24) (p. 531).
*Proof* (p. 532).
- *Upper.* Let $T=\arg\max_jZ_j$. The $Z_j$ are 1-subgaussian, so by Exercise I.56, $|\mathbb E Z_T|\le\sqrt{2I(Z^n;T)}=\sqrt{2H(T)}\le\sqrt{2\log n}$.
- *Lower (i.i.d.).* For t>0,
$$\mathbb E\max Z_i\ge t\big(1-(1-\Phi^c(t))^n\big)+\mathbb E[Z_11\{Z_1<0\}1\{Z_2<0\}\cdots1\{Z_n<0\}],$$
with $\Phi^c(t)=\mathbb P[Z_1\ge t]$. The second term is $2^{-(n-1)}\mathbb E[Z_11\{Z_1<0\}]=o(1)$. By $\Phi^c(t)\ge\frac t{1+t^2}\varphi(t)$ (Exercise V.25), choosing $t=\sqrt{(2-\eta)\log n}$ for small η>0 gives $\Phi^c(t)=\omega(1/n)$. Hence $\mathbb E\max Z_i\ge\sqrt{(2-\eta)\log n}\,(1+o(1))$. Since η is arbitrary, (27.24) follows.

*Proof of Theorem 27.8* (p. 532). Take an optimal ε-packing $\{\theta_1,\dots,\theta_M\}$. Let $X_i=\langle\theta_i,Z\rangle$ and $Y_i\overset{iid}\sim\mathcal N(0,\epsilon^2/2)$. Then $\mathbb E(X_i-X_j)^2=\|\theta_i-\theta_j\|_2^2\ge\epsilon^2=\mathbb E(Y_i-Y_j)^2$. So, by Lemma 27.9 and 27.10,
$$\mathbb E\sup_\theta\langle\theta,Z\rangle\ge\mathbb E\max X_i\ge\mathbb E\max Y_i\asymp\epsilon\sqrt{\log M}.$$

*Application to $B_1$* (p. 532). By duality $w(B_1)=\mathbb E\|Z\|_\infty\le\sqrt{2\log d}$. So
$$\log M(B_1,\|\cdot\|_2,\epsilon)\lesssim\frac{\log d}{\epsilon^2}.\tag{27.25}$$
For $\epsilon\gtrsim1/\sqrt d$ this is much tighter than (27.15) and almost optimal compared with $\frac{\log(d\epsilon^2)}{\epsilon^2}$. For $\epsilon\asymp1/\sqrt d$ it gives $d\log d$, whereas the correct behaviour is order d. Maurey's method (below) fixes this.

*Intuition note.* Sudakov says a set containing many well-separated points must have a large expected Gaussian maximum, because the points' random projections are at least as spread out as independent Gaussians. For the ℓ1-ball the Gaussian width is only about $\sqrt{\log d}$, which forces a small packing number at coarse scales.

#### 27.3.2 Hilbert ball has metric entropy $1/\epsilon^2$ (pp. 532–534)
Take $B_2=\{x\in\mathbb R^\infty:\sum x_i^2\le1\}$. In ℓ2 it is not compact and cannot have finite ε-nets for all ε. Instead fix a distribution P on $B_2$ with $\mathbb E_P\|X\|_2^2\le1$ and define
$$d_P(\theta,\theta')\triangleq\sqrt{\mathbb E_{X\sim P}|\langle\theta-\theta',X\rangle|^2}.$$
This metric analyzes the complexity of linear functions $\theta\mapsto\langle\theta,X\rangle$ and has learning-theory applications (p. 533).

**Theorem 27.11.** For a universal constant c and all ε>0: $\log N(B_2,d_P,\epsilon)\le c/\epsilon^2$ (p. 533).
*Proof* (p. 533).
1. *Reduction to finite dimension.* Pick n with $\mathbb E[\sum_{j>n}X_j^2]\le\epsilon^2/4$. Let $\tilde\theta$ be θ with coordinates j>n zeroed. By Cauchy–Schwarz $d_P(\theta,\tilde\theta)\le\epsilon/2$. So any ε/2-covering of $\tilde B_2$ is an ε-covering of $B_2$.
2. *Matrix form.* $d_P(\theta,\theta')^2=(\theta-\theta')^\top\Sigma(\theta-\theta')$ with $\Sigma=\mathbb E[XX^\top]\succeq0$. Let $D=\sqrt\Sigma$ and $V=D(B_2)$. Then $d_P(\theta,\theta')=\|D\theta-D\theta'\|_2$.
3. *Sudakov.* $\log M(V,\|\cdot\|_2,\epsilon)\le\frac c{\epsilon^2}\mathbb E[\sup_{v\in V}\langle v,Z\rangle]$ as printed (see Reading notes).
4. *Ellipsoid supremum.* $\mathbb E\sup_{v\in V}\langle v,Z\rangle=\mathbb E\sup_{\theta\in B_2}\langle D\theta,Z\rangle=\mathbb E\|DZ\|_2\le\sqrt{\mathbb E\|DZ\|_2^2}=\sqrt{\mathrm{tr}\,\Sigma}\le1$.

**Consequence for empirical processes** (p. 533). The standard bound is $\mathbb E\sup_\theta(\mathbb E f_\theta-\hat{\mathbb E}_nf_\theta)\lesssim\mathbb E\big[\inf_{\delta>0}\delta+\int_\delta^\infty\sqrt{\frac{\log N(\Theta,d_{\hat P_n},\epsilon)}n}\,d\epsilon\big]$. When entropy behaves as $\epsilon^{-p}$ this yields rate $n^{-\min(1/p,1/2)}$, except p = 2, where the bound yields $n^{-1/2}\log n$. The Hilbert ball is thus "precisely at the phase transition" from parametric to nonparametric rate. As a sanity check (p. 534), for $P_X$ on the unit ball with $\mathbb E X=0$ and Θ = B, the bound gives $\mathbb E\|\bar X_n\|\lesssim\sqrt{\log n/n}$, while a direct calculation gives $\mathbb E\|\bar X_n\|\le\frac1{\sqrt n}$.

*Intuition note.* In the metric $d_P$ the Hilbert ball has entropy at most $c/\epsilon^2$ whatever the distribution P. The reason is that the Gaussian width of the image ellipsoid is at most $\sqrt{\mathrm{tr}\,\Sigma}\le1$. This is the borderline case between parametric and nonparametric rates.

#### 27.3.3 Maurey's empirical method (pp. 534–535)
A probabilistic way to build a covering, with applications to approximation theory and neural nets (p. 534).

**Theorem 27.12.** Let H be an inner-product space with $\|x\|=\sqrt{\langle x,x\rangle}$. Let $T\subset H$ be a finite set with radius $r=\mathrm{rad}(T)=\inf_{y\in H}\sup_{x\in T}\|x-y\|$, and $\mathrm{co}(T)$ its convex hull. For $0<\epsilon\le r$:
$$N(\mathrm{co}(T),\|\cdot\|,\epsilon)\le\binom{|T|+\lceil r^2/\epsilon^2\rceil-2}{\lceil r^2/\epsilon^2\rceil-1}.\tag{27.26}$$
*Proof* (p. 534). Let $T=\{t_1,\dots,t_m\}$ and let c be the Chebyshev center, $r=\max_i\|c-t_i\|$. For $n\in\mathbb Z_+$ set $\mathcal Z=\{\frac1{n+1}(c+\sum_in_it_i):n_i\in\mathbb Z_+,\sum n_i=n\}$.
1. For $x=\sum x_it_i\in\mathrm{co}(T)$ ($x_i\ge0$, $\sum x_i=1$), let Z take value $t_i$ with probability $x_i$, so $\mathbb EZ=x$. Let $Z_0=c$ and $Z_1,\dots,Z_n$ be i.i.d. copies of Z, and $\bar Z=\frac1{n+1}\sum_{i=0}^nZ_i\in\mathcal Z$.
2. The cross terms vanish, giving
$$\mathbb E\|\bar Z-x\|^2=\frac{\|c-x\|^2+n\mathbb E\|Z-x\|^2}{(n+1)^2}\le\frac{r^2}{n+1}.$$
This uses $\|c-x\|\le\sum x_i\|c-t_i\|\le r$ and $\mathbb E\|Z-x\|^2\le\mathbb E\|Z-c\|^2\le r^2$.
3. Set $n=\lceil r^2/\epsilon^2\rceil-1$, so $r^2/(n+1)\le\epsilon^2$. Some $z\in\mathcal Z$ has $\|z-x\|\le\epsilon$, so $\mathcal Z$ is an ε-covering of $\mathrm{co}(T)$.
4. Counting as in (27.17): $|\mathcal Z|\le\binom{n+m-1}n$, which is the right side of (27.26).

**Application.** $B_1=\mathrm{co}(T)$ with $T=\{\pm e_1,\dots,\pm e_d,0\}$, rad(T) = 1. So
$$N(B_1,\|\cdot\|_2,\epsilon)\le\binom{2d+\lceil\epsilon^{-2}\rceil-1}{\lceil\epsilon^{-2}\rceil-1}.\tag{27.27}$$
This recovers the optimal upper bound of Thm 27.7 at both small and large scales (p. 535).

*Intuition note.* Any point of the hull is a mixture of points of T. An average of about $r^2/\epsilon^2$ random draws from that mixture lands within ε in expectation. So only the number of draws matters, not the dimension.

#### 27.3.4 Duality of metric entropy (p. 535)
For $K,T\subset\mathbb R^d$ define $N(K,T)=\min\{N:\exists x_1,\dots,x_N,\ K\subset\cup_i(T+x_i)\}$. Then $N(K,\|\cdot\|,\epsilon)=N(K,\epsilon B)$. The result of Artstein–Milman–Szarek (called "deep", stated without proof): there are absolute constants α, β such that for any symmetric convex body K (compact convex, nonempty interior, K = −K),
$$\frac1\beta\log N\Big(B_2,\frac\epsilon\alpha K^\circ\Big)\le\log N(K,\epsilon B_2)\le\log N(B_2,\alpha\epsilon K^\circ),\tag{27.28}$$
with polar body $K^\circ=\{y:\sup_{x\in K}\langle x,y\rangle\le1\}$. Example: for $p<2<q$, $\frac1p+\frac1q=1$, $B_p^\circ=B_q$, so $N(B_p,\|\cdot\|_2,\epsilon)$ and $N(B_2,\|\cdot\|_q,\epsilon)$ behave essentially the same, as (27.18) confirms.

### 27.4 Infinite-dimensional space: smooth functions (pp. 535–539)
In infinite-dimensional spaces metric entropy can grow arbitrarily fast (cited from [250]). The example is $\mathcal F(A,L)$, all L-Lipschitz probability densities on $[0,A]$ (p. 535).

**Theorem 27.13.** For constants $L,A>0$ and $p\in[1,\infty]$:
$$\log N(\mathcal F(A,L),\|\cdot\|_p,\epsilon)=\Theta(1/\epsilon).\tag{27.29}$$
For the sup-norm, as ε→0,
$$\log_2N(\mathcal F(A,L),\|\cdot\|_\infty,\epsilon)=\frac{LA}\epsilon(1+o(1)).\tag{27.30}$$
*Proof* (pp. 536–538).
- *Scaling.* Replacing f(x) by $\frac1{\sqrt L}f(x/\sqrt L)$ gives $N(\mathcal F(A,L),\|\cdot\|_p,\epsilon)=N(\mathcal F(\sqrt LA,1),\|\cdot\|_p,L^{\frac{1-p}{2p}}\epsilon)$ (27.31). It suffices to treat $\mathcal F(A)=\mathcal F(A,1)$. Any such f is bounded: $f(x)\ge(f(0)-x)_+$ and $\int f=1$ give $f(0)\le\max\{A,\frac A2+\frac1A\}\triangleq m$.
- *Plan.* By Thm 27.2 it suffices to show $N(\mathcal F(A),\|\cdot\|_\infty,\epsilon)\le\frac C\epsilon2^{A/\epsilon}$ (27.32) and $M(\mathcal F(A),\|\cdot\|_1,\epsilon)\ge2^{c/\epsilon}$ (27.33), with constants depending on A.
- *Packing (27.33).* Perturb the uniform density.
  1. Define the tent $T(x)=x1\{x\le\epsilon\}+(2\epsilon-x)1\{x\ge\epsilon\}+\frac1A$ on $[0,2\epsilon]$, zero elsewhere. Let $n=\lceil\frac A{4\epsilon}\rceil$, $a=2n\epsilon$.
  2. For $y\in\{0,1\}^n$ set $f_y(x)=\sum_{i=1}^ny_iT(x-2(i-1)\epsilon)$ on $[0,a]$, extended linearly on $[a,A]$ so that $\int_0^Af_y=1$ (Fig. 27.2). For small ε, $\int_0^af_y=\frac12+O(\epsilon)$, so the slope of the extension is $O(\epsilon)$ and $f_y\in\mathcal F(A)$.
  3. $\|f_y-f_z\|_1=\epsilon^2d_H(y,z)$. By Thm 27.5 there is an $n/2$-packing $\mathcal Y\subset\{0,1\}^n$ with $|\mathcal Y|\ge2^{cn}$. Then $\{f_y\}$ is an $\frac{n\epsilon^2}2$-packing in $L_1$, and $\frac{n\epsilon^2}2=\Theta(\epsilon)$.
- *Covering (27.32).*
  1. Let $J=\lceil m/\epsilon\rceil$, $n=\lceil A/\epsilon\rceil$, $x_k=k\epsilon$. Let $\mathcal G$ be all lattice paths (grid ε) with n steps of slope ±1, starting at $(0,j\epsilon)$, $j\in\{0,\dots,J\}$. There are at most $(J+1)2^n=O(\frac1\epsilon2^{A/\epsilon})$ of them.
  2. Claim: each $f\in\mathcal F(A)$ is within ε in sup-norm of some $g\in\mathcal G$. By induction, suppose $|f-g|\le\epsilon$ on $[0,x_k]$. Since $|f(x_k)-g(x_k)|\le\epsilon$ and f is 1-Lipschitz, $f(x_{k+1})\in[g(x_k),g(x_k)+2\epsilon]$ or $[g(x_k)-2\epsilon,g(x_k)]$. Extend g upward or downward accordingly, and $|f-g|\le\epsilon$ holds on $I_k$.
- *Sharp sup-norm constant.* The upper bound follows from (27.32) and the scaling (27.31). (Added step: for p=∞ the scaling replaces A by $\sqrt LA$ and ε by $\epsilon/\sqrt L$, so $A'/\epsilon'=LA/\epsilon$.) For the lower bound, use Thm 27.2 to turn it into a 2ε-packing and prove
$$M(\mathcal F(A),\|\cdot\|_\infty,2\epsilon)\ge\Omega(\epsilon^{3/2}2^{a/\epsilon})\tag{27.34}$$
for any a<A. Choose b with $\frac1A<b<\frac1A+\frac{(A-a)^2}{2A}$, and set $a'=\epsilon\lfloor a/\epsilon\rfloor$, $b'=\epsilon\lfloor b/\epsilon\rfloor$. Take densities f where on $[0,a']$ f is a lattice path from $(0,b')$ to $(a',b')$ staying in $[b',b'+\epsilon^{1/3}]$ (Fig. 27.3), and on $[a',A]$ f is a linear extension with $\int_0^Af=1$. This is feasible because $\int_0^{a'}f=ab+o(1)$ and by the choice of b. Two distinct paths differ at some first subinterval, so the family is a 2ε-packing in sup-norm. Counting paths uses the random-walk fact (cited): a symmetric walk returns to zero in n steps and stays in $[0,n^{1+c}]$ with probability $\Theta(n^{-3/2})$. Since a<A is arbitrary, the lower bound of (27.30) follows.

*Intuition note.* A Lipschitz density can be described, to accuracy ε, by one up/down choice per grid step of width ε. That is about $A/\epsilon$ binary choices, i.e. entropy proportional to $1/\epsilon$. This is a polynomial growth in 1/ε, in contrast to the $d\log\frac1\epsilon$ of a finite-dimensional ball.

**Theorem 27.14 (Birman–Solomjak).** Fix positive constants A, L and $d\in\mathbb N$. Let $\beta=\ell+\alpha$ with $\ell\in\mathbb Z_+$, $\alpha\in(0,1]$. Let $\mathcal F_\beta(A,L)$ be the ℓ-times continuously differentiable densities on $[0,A]^d$ whose ℓth derivative is (L,α)-Hölder: $\|D^{(\ell)}f(x)-D^{(\ell)}f(y)\|_\infty\le L\|x-y\|_\infty^\alpha$. Then for $1\le p\le\infty$,
$$\log N(\mathcal F_\beta(A,L),\|\cdot\|_p,\epsilon)=\Theta\big(\epsilon^{-d/\beta}\big).\tag{27.35}$$
The entropy grows more slowly when the dimension decreases or the smoothness increases. For very smooth classes it can be subpolynomial in 1/ε. Example (Vitushkin, cited): analytic functions on the unit complex disk D that extend analytically to rD with r>1 have sup-norm entropy $\Theta((\log\frac1\epsilon)^2)$ (p. 538).

**Hilbert's 13th problem** (pp. 538–539). Hilbert conjectured in 1900 that some functions of several variables cannot be written as a superposition of finitely many functions of fewer variables. Kolmogorov and Arnold disproved this in the 1950s, showing every continuous function of d variables can be built from sums and superpositions of single-variable functions. Their construction does not work if the constituent functions must have specified smoothness. For smooth functions the conjecture was resolved positively by Vitushkin: there are functions of d variables in the β-Hölder class that are not finitely many superpositions of functions of d′ variables in the β′-Hölder class, provided $d/\beta>d'/\beta'$. His proof is "highly involved". Kolmogorov later gave a much simplified proof using the $\|\cdot\|_\infty$-version of Thm 27.14. The index d/β measures complexity, which allows an entropy-comparison impossibility proof. The text proves only this simpler version:
- Claim: some 1-Lipschitz f(x,y,z) on $[0,1]^3$ is not $g(h_1(x,y),h_2(y,z))$ with g, h1, h2 1-Lipschitz on $[0,1]^2$.
- Suppose it were. Use an ε-covering of cardinality $\exp(O(\epsilon^{-2}))$ of 1-Lipschitz functions on $[0,1]^2$ to approximate g, h1, h2. Superposition then gives an O(ε)-covering of 1-Lipschitz functions on $[0,1]^3$ of cardinality $\exp(O(\epsilon^{-2}))$.
- But any such covering must have size $\exp(\Omega(\epsilon^{-3}))$, a contradiction.

*Intuition note.* If a class of 3-variable functions were built from 2-variable pieces, its entropy would be at most that of the pieces ($\epsilon^{-2}$), yet it is of order $\epsilon^{-3}$. Entropy counts therefore rule out the representation.

### 27.5 Metric entropy and small-ball probability (pp. 539–541)
The *small-ball function* of a random variable X in a real separable Banach space is $\phi(\epsilon)\triangleq\log\frac1{\mathbb P[\|X\|\le\epsilon]}$ as ε→0. Examples: for $X\sim\mathcal N(0,I_d)$ in ℓ2, $\phi(\epsilon)\asymp d\log\frac1\epsilon$ (Exercise III.16); for standard Brownian motion on [0,1] in sup-norm, $\phi(\epsilon)\asymp\epsilon^{-2}$ (27.36) (Exercise V.30). Footnote 16 cites the sharp constant $\lim\epsilon^2\phi(\epsilon)=\pi^2/8$ (p. 539).

*Link via volume.* There is no translation-invariant analogue of Lebesgue measure in infinite dimensions, so one uses a Gaussian measure γ. The volume argument adapts to a non-translation-invariant measure γ:
$$\frac{\gamma(\Theta+B(0,\epsilon))}{\max_{\theta\in V}\gamma(B(\theta,2\epsilon))}\le N\le M\le\frac{\gamma(\Theta+B(0,\epsilon/2))}{\min_{\theta\in\Theta}\gamma(B(\theta,\epsilon/2))}.\tag{27.37}$$
Small-ball probabilities appear naturally here (p. 539).

*RKHS.* Let γ be a zero-mean Gaussian measure on V with $\mathbb E\|X\|^2<\infty$. Let H ⊂ V be the reproducing kernel Hilbert space generated by γ and K its unit ball (precise definition cited; fn. 11 gives the Mercer description) (pp. 539–540). Examples:
- γ = N(0,Σ): $K=\{\Sigma^{1/2}x:\|x\|_2\le1\}$ (27.38), a rescaled Euclidean ball with $\langle x,y\rangle_H=x^\top\Sigma^{-1}y$.
- Standard Brownian motion on [0,1]: $K=\{f(t)=\int_0^tf'(s)ds:\|f'\|_2\le1\}$ (27.39), with $\langle f,g\rangle_H=\int_0^1f'g'$.

**Theorem 27.15 (Kuelbs–Li).** For all ε>0, with $N(\epsilon)\equiv N(K,\|\cdot\|,\epsilon)$:
$$\phi(2\epsilon)-\log2\le\log N\Big(\frac\epsilon{\sqrt{2\phi(\epsilon/2)}}\Big)\le2\phi(\epsilon/2).\tag{27.40}$$
*Proof* (pp. 540–541). Claim: for any λ>0,
$$\phi(2\epsilon)+\log\Phi\big(\lambda+\Phi^{-1}(e^{-\phi(\epsilon)})\big)\le\log N(\lambda K,\epsilon)\le\log M(\lambda K,\epsilon)\le\frac{\lambda^2}2+\phi(\epsilon/2).\tag{27.41}$$
- *Deducing (27.40).* Take $\lambda=\sqrt{2\phi(\epsilon/2)}$ and use $N(\lambda K,\epsilon)=N(K,\epsilon/\lambda)$. The tail bound $\Phi(-t)\le e^{-t^2/2}$ (Exercise V.25) gives $\Phi^{-1}(e^{-\phi(\epsilon)})\ge-\sqrt{2\phi(\epsilon)}\ge-\lambda$, so $\Phi(\Phi^{-1}(e^{-\phi(\epsilon)})+\lambda)\ge\Phi(0)=\frac12$. (Added step: $\phi(\epsilon)\le\phi(\epsilon/2)$, since $\phi$ is non-increasing in ε.) The upper side is $\lambda^2/2+\phi(\epsilon/2)=2\phi(\epsilon/2)$.
- *Proof of (27.41), finite dimensions only* (the source says the results are dimension-free and extend). For $Z\sim\gamma=\mathcal N(0,\Sigma)$, applying (27.37) to λK gives
$$\frac{\gamma(\lambda K+B(0,\epsilon))}{\max_\theta\gamma(B(\theta,2\epsilon))}\le N(\lambda K,\epsilon)\le M(\lambda K,\epsilon)\le\frac1{\min_{\theta\in\lambda K}\gamma(B(\theta,\epsilon/2))}.\tag{27.42}$$
  - *Upper bound.* For symmetric A = −A and θ ∈ λK, by change of measure $\gamma(\theta+A)=e^{-\frac12\theta^\top\Sigma^{-1}\theta}\mathbb E[e^{\langle\Sigma^{-1}\theta,Z\rangle}1\{Z\in A\}]\ge e^{-\lambda^2/2}\mathbb P[Z\in A]$. This uses $\theta^\top\Sigma^{-1}\theta\le\lambda^2$ and Jensen: $\mathbb E[e^{\langle\Sigma^{-1}\theta,Z\rangle}|Z\in A]\ge e^{\langle\Sigma^{-1}\theta,\mathbb E[Z|Z\in A]\rangle}=1$, since $\mathbb E[Z|Z\in A]=0$ by symmetry. Take $A=B(0,\epsilon/2)$.
  - *Lower bound.* Anderson's lemma (Lemma 28.10) gives $\gamma(B(\theta,2\epsilon))\le\gamma(B(0,2\epsilon))$. For the numerator use the Gaussian isoperimetric inequality $\gamma(A+\lambda K)\ge\Phi(\Phi^{-1}(\gamma(A))+\lambda)$ (27.43) with $A=B(0,\epsilon)$.

**Consequences** (p. 541). If $\phi(\epsilon)\asymp\phi(\epsilon/2)$, then approximately $\log N\big(\frac\epsilon{\sqrt{\phi(\epsilon)}}\big)\asymp\phi(\epsilon)$. Unconditionally (cited), for fixed α>0, β∈ℝ:
$$\phi(\epsilon)\asymp\epsilon^{-\alpha}\Big(\log\frac1\epsilon\Big)^\beta\iff\log N(\epsilon)\asymp\epsilon^{-\frac{2\alpha}{2+\alpha}}\Big(\log\frac1\epsilon\Big)^{\frac{2\beta}{2+\alpha}}.\tag{27.44}$$
Example: the unit ball (27.39) for Brownian motion is similar to a Sobolev ball. With (27.36) (α = 2, β = 0) and (27.44), $\log N(\epsilon)\asymp\frac1\epsilon$, recovering the Sobolev-ball entropy of [420]. This coincides with the Lipschitz-ball entropy of §27.4, even though the latter bounds the derivative everywhere and this ball bounds it only in $L_2$.

*Intuition note.* The RKHS unit ball K at scale $\epsilon/\sqrt{2\phi(\epsilon/2)}$ has entropy squeezed between small-ball quantities at scales 2ε and ε/2. The Gaussian isoperimetric inequality and a change of measure are what turn Gaussian mass into covering numbers.

### 27.6 Metric entropy and rate–distortion theory (pp. 542–544)
The metric entropy is non-probabilistic, but the rate–distortion function for the "least favorable" source behaves similarly. For a metric space $(\mathcal X,d)$ and an $\mathcal X$-valued X,
$$\phi_X(\epsilon)=\inf_{P_{\hat X|X}:\,\mathbb E[d(X,\hat X)]\le\epsilon}I(X;\hat X),\qquad\phi_{\mathcal X}(\epsilon)=\sup_{P_X\in\mathcal P(\mathcal X)}\phi_X(\epsilon).\tag{27.45, 27.46}$$

**Theorem 27.16.** For any $0<c<1/2$:
$$\phi_{\mathcal X}(\epsilon)\le\log N(\mathcal X,d,\epsilon)\le\log M(\mathcal X,d,\epsilon)\le\frac{\phi_{\mathcal X}(c\epsilon)+\log2}{1-2c}.\tag{27.47}$$
*Proof* (p. 542).
- *Left.* Fix an ε-covering of size N and let $\hat X$ be the closest covering point to X. Then $d(X,\hat X)\le\epsilon$ a.s., so $\phi_X(\epsilon)\le I(X;\hat X)\le\log N$. Optimize over $P_X$.
- *Right.* Let X be uniform on a maximal ε-packing (size M). Take any $P_{\hat X|X}$ with $\mathbb E[d(X,\hat X)]\le c\epsilon$.
  1. Let $\tilde X$ be the closest packing point to $\hat X$, so $X\to\hat X\to\tilde X$ is a Markov chain.
  2. $d(X,\tilde X)\le d(\hat X,\tilde X)+d(\hat X,X)\le2d(\hat X,X)$, so $\mathbb E[d(X,\tilde X)]\le2c\epsilon$.
  3. Either $X=\tilde X$ or $d(X,\tilde X)>\epsilon$, so $\mathbb P[X\ne\tilde X]\le2c$.
  4. Fano's inequality gives $\mathbb P[X\ne\tilde X]\ge1-\frac{I(X;\hat X)+\log2}{\log M}$.
  5. Hence $I(X;\hat X)\ge(1-2c)\log M-\log2$.

The lower bound is a "Bayesian" argument (worst case ≥ average case); the upper bound was shown in [241] via a dual representation, and the text gives the Fano proof (p. 542).

**Remark 27.4** (pp. 542–543). (a) With distortion a power of the metric, $\phi_{X,r}(\epsilon)=\inf_{\mathbb E[d(X,\hat X)^r]\le\epsilon^r}I(X;\hat X)$, (27.47) continues to hold with $1-2c$ replaced by $1-(2c)^r$. This is useful for second-moment constraints. (b) The older "ε-entropy" uses $d(X,\hat X)\le\epsilon$ with probability one. One might conjecture its maximum equals $\log N$, but this need not be true (counterexample cited).

*Maximizing over sources.* $P_X\mapsto\phi_X(D)$ is in general neither convex nor concave (fn. 15 points to the binary source of Thm 26.1). For certain spaces a symmetry argument (Exercise V.24) shows the uniform distribution maximizes the rate–distortion function at every distortion level (p. 543):
- Hamming space with Hamming distortion: $\mathrm{Ber}(\frac12)^d$.
- Unit sphere $S^{d-1}$ with Euclidean distance: $\mathrm{Unif}(S^{d-1})$.
- O(d) or U(d) with Frobenius norm: Haar measure; similarly for Grassmannians.

**Theorem 27.17.** Let θ be uniform on $S^{d-1}$. For $0<\epsilon<1$ and a universal constant C,
$$(d-1)\log\frac1\epsilon-C\le\inf_{P_{\hat\theta|\theta}:\mathbb E\|\hat\theta-\theta\|_2^2\le\epsilon^2}I(\theta;\hat\theta)\le(d-1)\log\Big(1+\frac1\epsilon\Big)+\log(2d).$$
The entries of θ are dependent, so single-letterization (Thm 24.8) cannot be used directly. Instead use $\theta\overset d=Z/\|Z\|_2$ for $Z\sim\mathcal N(0,I_d)$ to relate to Gaussian rate–distortion (Thm 26.2). The lower bound matches the metric entropy of spheres in Cor. 27.4. By similar reductions (cited), the metric entropy of O(d) and U(d) scales as $\frac{d(d-1)}2\log\frac1\epsilon$ and $d^2\log\frac1\epsilon$, with pre-log factors commensurate with their degrees of freedom. These were obtained by Szarek by a volume argument with Haar measure; the information-theoretic route is "more elementary" (p. 544).

*Proof* (p. 544).
- *Upper bound.* From Thm 27.16 with Remark 27.4(a) and the sphere bound of Cor. 27.4.
- *Lower bound.*
  1. Let $Z\sim\mathcal N(0,I_d)$, $\theta=Z/\|Z\|$, $A=\|Z\|$. Then θ ~ Unif and $A\sim\chi_d$ are independent. Fix $P_{\hat\theta|\theta}$ with $\mathbb E\|\hat\theta-\theta\|^2\le\epsilon^2$.
  2. Since Var(A) ≤ 1, the Shannon lower bound (Thm 26.3) shows A's rate–distortion function is majorized by the standard Gaussian's. So for each δ ∈ (0,1) there is $P_{\hat A|A}$ with $\mathbb E(\hat A-A)^2\le\delta^2$, $I(A;\hat A)\le\log\frac1\delta$, $\mathbb E A=\mathbb E\hat A$.
  3. Set $\hat Z=\hat A\hat\theta$. Then $I(Z;\hat Z)=I(\theta,A;\hat Z)\le I(\theta,A;\hat\theta,\hat A)=I(\theta;\hat\theta)+I(A;\hat A)$.
  4. $\mathbb E\hat A^2\le d+\delta^2+2\delta\le d+3\delta$; $|\mathbb E\hat A(\hat A-A)|\le2\delta$; $\mathbb E\|Z-\hat Z\|^2\le d\epsilon^2+7\delta\epsilon+\delta$. With δ = ε this is ≤ $(d+8)\epsilon^2$.
  5. Thm 24.8 with Thm 26.2: $I(Z;\hat Z)\ge\frac d2\log\frac d{(d+8)\epsilon^2}$.
  6. (Added step, using $\log(1+x)\le x\log e$.) $\frac d2\log\frac d{(d+8)\epsilon^2}\ge d\log\frac1\epsilon-4\log e$. Subtracting $I(A;\hat A)\le\log\frac1\epsilon$ gives $I(\theta;\hat\theta)\ge(d-1)\log\frac1\epsilon-4\log e$.

Footnote 14 notes a parallelism, observed by Donoho, between Sobolev-ball entropy and rate–distortion of smooth Gaussian processes. It cannot be formalized with Thm 27.16 because it is unclear whether the Gaussian rate–distortion function is maximal.

*Intuition note.* Describing a worst-case point of a set to accuracy cε costs, in bits, about as much as the log covering number, up to the stated factor $1/(1-2c)$ and the $+\log2$ term. So information-theoretic tools (here, Fano) can bound metric entropy. Applied to the sphere, they reproduce the geometric answer $(d-1)\log\frac1\epsilon$.

### Exercises for Part V (pp. 545–553)
The pages after §27.6 print Exercises V.1–V.30 for the whole of Part V. Those tied to this chapter are listed under "Exercises worth doing". Solutions are not printed.

## Toy example (ours)
Take Θ = [0,1] ⊂ ℝ with d(x,y) = |x−y|, ε = 0.2, and B = [−1,1] (vol 2).
- **Covering number.** A closed ball of radius 0.2 has length 0.4, and 3 such balls cover [0,1] (2 balls cover only length 0.8). So N(ε) = 3, e.g. centres 0.2, 0.6, 1.0 (balls [0,0.4], [0.4,0.8], [0.8,1.2]).
- **Packing number.** Points with pairwise gaps > 0.2: {0, 0.21, 0.42, 0.63, 0.84} works (gaps 0.21, and 0.84+0.21 = 1.05 > 1). Six points would need five gaps > 0.2, i.e. span > 1. So M(0.2) = 5.
- **Sandwich (27.4).** M(2ε) = M(0.4): gaps > 0.4 allow {0, 0.41, 0.82}; four points would need span > 1.2. So M(0.4) = 3. Then 3 = M(2ε) ≤ N(ε) = 3 ≤ M(ε) = 5. ✓
- **Greedy.** The greedy packing {0, 0.21, …, 0.84} is also a 0.2-covering: consecutive gaps are 0.21, so interior points are within 0.105 of a centre, and 1 − 0.84 = 0.16 ≤ 0.2. This is a 5-point covering, consistent with N = 3 ≤ 5.
- **Volume bounds.** (a): $(1/\epsilon)^d\mathrm{vol}(\Theta)/\mathrm{vol}(B)=5\cdot1/2=2.5\le N=3$. ✓ (b): $\Theta+\frac\epsilon2B=[-0.1,1.1]$ has length 1.2, $\mathrm{vol}(\frac\epsilon2B)=0.2$, ratio 6 ≥ M = 5. ✓ (Part (c) is not applicable: Θ does not contain εB.)

## Concepts
- [[covering-number]] (new) — fewest ε-balls (centres anywhere in V) whose union contains Θ; N(Θ,d,ε) (p. 523)
- [[packing-number]] (new) — most points of Θ pairwise more than ε apart; M(Θ,d,ε) (p. 523)
- [[metric-entropy]] (new) — log N or log M; called ε-capacity and ε-entropy in Kolmogorov–Tikhomirov (p. 523)
- [[entropy-numbers]] (new) — $e_k(\Theta)=\inf\{\epsilon:N\le2^{k-1}\}$, essentially an inverse of metric entropy; $e_1=\mathrm{rad}(\Theta)$ (p. 523)
- [[volume-bound]] (new) — N and M bounded by volume ratios, e.g. $(1/\epsilon)^d\mathrm{vol}(\Theta)/\mathrm{vol}(B)\le N$ (p. 525)
- [[minkowski-dimension]] (new) — $\lim_{\epsilon\to0}\log N/\log(1/\epsilon)$; can be non-integer for fractals (p. 527)
- [[gilbert-varshamov-bound]] (new) — lower bound on packing number of Hamming space via counting measure; upper side is the Hamming bound (p. 527)
- [[gaussian-width]] (new) — $w(\Theta)=\mathbb E\sup_\theta\langle\theta,Z\rangle$, $Z\sim\mathcal N(0,I_d)$ (p. 530)
- [[sudakov-minoration]] (new) — $w(\Theta)\gtrsim\sup_\epsilon\epsilon\sqrt{\log M(\epsilon)}$, dimension-free constant (p. 531)
- [[maurey-empirical-method]] (new) — cover a convex hull by averages of random draws from the generating set (p. 534)
- [[small-ball-probability]] (new) — $\phi(\epsilon)=\log\frac1{\mathbb P[\|X\|\le\epsilon]}$ (p. 539)
- [[rkhs-unit-ball]] (new) — unit ball K of the Hilbert space attached to a Gaussian measure; $\Sigma^{1/2}B_2$ for N(0,Σ) (p. 540)
- [[rate-distortion-function]] — here $\phi_X(\epsilon)=\inf I(X;\hat X)$ s.t. $\mathbb E\,d(X,\hat X)\le\epsilon$, and its worst case over $P_X$ (p. 542)
- [[fano-inequality]] — used to lower-bound mutual information by $(1-2c)\log M-\log2$ (p. 542)
- [[mutual-information]] — used in $|\mathbb E Z_T|\le\sqrt{2I(Z^n;T)}$ and in rate–distortion (pp. 532, 542)

## Canonical instances
- [[hamming-space-packing]] — GV/Hamming bounds and $N=2^{dR(\rho)+o(d)}$ (pp. 527–528)
- [[l1-ball-in-l2]] — $\log M(B_1,\|\cdot\|_2,\epsilon)$ with a phase change at $\epsilon\asymp1/\sqrt d$ (pp. 529–530)
- [[hilbert-ball-dP]] — $\log N\le c/\epsilon^2$ in the metric $d_P$ (p. 533)
- [[lipschitz-density-class]] — $\log N=\Theta(1/\epsilon)$, sharp sup-norm constant $LA/\epsilon$ (pp. 536–538)
- [[hilbert-13th-problem]] — impossibility of superposition by entropy comparison (pp. 538–539)
- [[brownian-motion-small-ball]] — $\phi(\epsilon)\asymp\epsilon^{-2}$, so $\log N\asymp1/\epsilon$ for the RKHS ball (pp. 539, 541)
- [[sphere-rate-distortion]] — uniform on $S^{d-1}$: rate–distortion $\approx(d-1)\log\frac1\epsilon$ (p. 543)

## Bridges (candidates)
- [same-math] Hamming packing bound via counting measure ↔ coding theory: Gilbert–Varshamov and Hamming bounds — the proof of Thm 27.5 is the volume argument of Thm 27.3 with counting measure.
- [structural-analogy] Metric entropy $\log N(\epsilon)$ ↔ rate–distortion: Thm 27.16 compares worst-case rate–distortion at distortion cε (plus $\log2$, factor $1/(1-2c)$) with $\log N$; it is a comparison, not an equality.
- [structural-analogy] Hilbert ball at entropy $\epsilon^{-2}$ ↔ statistics: the empirical-process bound gives a parametric-to-nonparametric transition at p = 2 (p. 533).
- [structural-analogy] Greedy maximal packing is a covering ↔ optimization duality: converse proofs turn into achievability (footnote 3, p. 524).

## Questions this raises
- Thm 27.16 compares worst-case rate–distortion with metric entropy only up to a shift cε and $\log2$. When is the shift harmless for the exact exponents?
- Is the Gaussian rate–distortion function maximal among sources in the parallelism with Sobolev-ball entropy (fn. 14), and can this be proved?
- Dudley's integral (27.22) and Sudakov (27.20) differ by up to a $\log d$ factor. For which sets is each tight?
- The exact exponent of the Hamming-space packing number is open (p. 528). What does the contrast with the easy covering formula (27.9) say about packing versus covering?

## Exercises worth doing
These are exercises from the end-of-Part-V list (pp. 545–553) that relate to this chapter.
- Ex. V.26 (p. 551) — prove $N(\mathbb F_2^n,d_H,Dn)=2^{n(1-h(D))_++o(n)}$ using volume bound and probabilistic construction — difficulty: medium
- Ex. V.27 (p. 552) — prove (27.18), covering $\ell_p$-balls with $\ell_q$-balls; what happens for p>q? — difficulty: hard
- Ex. V.28 (p. 552) — prove Dudley's chaining inequality via multi-scale coverings — difficulty: hard
- Ex. V.29 (pp. 552–553) — bound the operator norm of a Gaussian matrix with ε-nets and Sudakov, getting $\mathbb E\|A\|\asymp\sqrt n+\sqrt m$ — difficulty: medium
- Ex. V.30 (p. 553) — small-ball probability of Brownian motion, $\phi(\epsilon)\asymp\epsilon^{-2}$ — difficulty: medium
- Ex. V.24 (p. 551) — the uniform distribution maximizes the rate–distortion function under group symmetry — difficulty: hard

## Reading notes
- **Page offset:** the page labels give printed numbers, which equal pdf − 25 (pdf 547 = printed 522). The unit id says "ch30", but the printed chapter number is 27. Pages 545–553 are "Exercises for Part V" (all of Part V, not only this chapter). Printed p. 554 is blank.
- **OCR:** the text layer garbles ≍, ≲ and ≳, sub/superscripts and some fractions. I read them from the page images.
- **Misprints and oddities:**
  - p. 523: the packing definition writes $\{B(\theta_i,\epsilon/2):j\in[M]\}$, with an index mismatch.
  - p. 523: the remark says N and M are "non-decreasing" in ε; they decrease as ε grows (larger balls need fewer), as (27.4) also implies, so this looks like a slip.
  - p. 526: the sphere is defined as $\{x:\|x\|\le1\}$, the same as the ball; it should be $=1$.
  - p. 526: for the sphere upper bound, the displayed chain begins with $\mathrm{vol}(S+\epsilon B)/\mathrm{vol}(\epsilon B)$, whereas Thm 27.3(b) as stated has $\epsilon/2$. Applying (b) literally with the same steps would give base $1+2/\epsilon$ instead of $1+1/\epsilon$. I report (27.6) as printed and did not resolve this.
  - p. 528: the exponent "$2^{d(1-h(\rho)+o(d))}$" has $o(d)$ inside the parentheses; I read it as $2^{d(1-h(\rho))+o(d)}$.
  - p. 533: Sudakov (27.20) literally gives $\mathbb E[\sup]^2$ on the right of the bound in step 3 of Thm 27.11, but the page prints it without the square. Since $\mathbb E\sup\le1$, the conclusion $c/\epsilon^2$ is unaffected.
  - p. 544: the last displayed line reads $(d-1)\log\frac1{\epsilon^2}-4\log e$ in the image (the text layer shows "log 2" with 1 and ε stacked). That is a factor 2 off from the theorem's $(d-1)\log\frac1\epsilon$ and from the derivation above it, so it looks like a misprint. The step 6 version in L3 is my (added step) derivation consistent with the theorem.
  - p. 540, fn. 11: the basis is named $\{\phi_k\}$ in one place and $\psi_k$ elsewhere in the same sentence.
- **Cited but not proved here:** Slepian's lemma, Anderson's lemma, the Gaussian isoperimetric inequality, the Artstein–Milman–Szarek duality, the Birman–Solomjak theorem, the unconditional equivalence (27.44), the sharp packing constant τ, and the random-walk estimate used for (27.34).
