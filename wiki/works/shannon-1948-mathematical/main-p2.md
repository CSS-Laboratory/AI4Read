---
id: shannon-1948-mathematical/main-p2
work: shannon-1948-mathematical
unit: paper (part 2/2) — end of Appendix 2, Appendices 3–4, Parts III–V (§§18–29), Acknowledgments, Appendices 5–7
pages: 29–55
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Shannon (1948), second half: continuous signals, the Gaussian channel, and the rate of a continuous source

## L0 — One line
Entropy, channel capacity and source rate carry over to continuous signals; the key results are that white noise, whose samples are Gaussian, has maximum entropy for a given power, that capacity is $W\log(1+P/N)$ with white Gaussian noise, and that a continuous source has a finite rate only relative to a chosen fidelity measure.

## L1 — The gist (≤ 120 words)
How do entropy, capacity and information rate work when messages and signals are continuous, such as speech and noise? Shannon defines continuous entropy by an integral. It depends on the coordinate system, but rates and capacities, which use differences of entropies, do not. White noise (Gaussian samples) has the largest entropy for a given power. With white Gaussian noise and average power limit $P$, the capacity of a band $W$ is $W\log\frac{P+N}{N}$. Bounds are given for other noises and for peak-power limits. A continuous source gets a finite rate only relative to a fidelity (distance) criterion. Its output can be sent over a channel if and only if this rate is at most the capacity. Appendices supply proofs.

**Prerequisites:** discrete entropy and channel capacity; integrals and densities; Lagrange multipliers; Gaussian distribution; Fourier bandwidth (frequency range); sample-space geometry (spheres, volume).

## L2 — Key ideas (5–10 bullets)
- Entropy of a density, $H=-\int p\log p\,dx$, shares most discrete properties but is relative to the coordinate system and can be negative. Rates and capacities use differences of entropies, so they are coordinate-free (pp. 35–38).
- Band-limited signals (substantially) limited to duration $T$ are points in a $2TW$-dimensional space. Ensembles of functions (sets of functions with a probability measure), not single functions, are the right objects for communication theory (pp. 33–35).
- For a given variance (or second moments) the Gaussian maximises entropy; white noise (independent Gaussian samples of equal variance, band-limited) therefore has the maximum entropy for a given power. This defines the "entropy power", the power of a white noise with the same entropy (pp. 36–39).
- Linear filters change entropy by $\frac1W\int\log|Y|^2$, and the entropy power of a sum is bounded (Theorems 14–15). This gives tools for noises that are not white (pp. 39–41).
- Capacity of a continuous channel is $C=\max\,[H(y)-H(n)]$ for independent additive noise (Theorem 16). With average power $P$ and white Gaussian noise $N$, $C=W\log\frac{P+N}{N}$ (Theorems 16–17, pp. 43–45).
- For arbitrary noise, $W\log\frac{P+N_1}{N_1}\le C\le W\log\frac{P+N}{N_1}$. For a peak-power limit only partial bounds are available (pp. 44–47).
- A continuous source has no finite exact rate. Given a fidelity measure $\rho$, the rate $R_1$ is the minimum of $R=\iint P\log\frac{P(x,y)}{P(x)P(y)}$ (the mutual information between source and output) at fixed average distortion. Delivery at fidelity $v_1$ is possible if $R_1\le C$ and not possible if $R_1>C$ (pp. 48–50).
- For a white-noise source under mean-square error, $R=W_1\log(Q/N)$. Other sources are bracketed by Theorem 23 (p. 51).
- Appendices: a mixed-source theorem, a constrained-rate maximisation giving capacity, and a general measure-theoretic definition of $R$. The last gives $R(x,v)\le R(x,y)$ for any processing of $y$ (pp. 30–31, 54).

## L3 — Walkthrough

### End of Appendix 2: uniqueness of $H=-K\sum p_i\log p_i$ (p. 29)
This part starts mid-proof. The conditions (2) and (3) it cites are in the earlier part.

Let $A(n)$ be the entropy of an equiprobable choice among $n$ possibilities. The proof shows $A(t)=K\log t$ with $K>0$.
- Similarly $A(t^n)=nA(t)$. For large $n$ choose $m$ with $s^m\le t^n<s^{m+1}$ (p. 29).
- Taking logs and dividing by $n\log s$: $\frac mn\le\frac{\log t}{\log s}\le\frac mn+\frac1n$, so $\left|\frac mn-\frac{\log t}{\log s}\right|<\epsilon$ (p. 29).
- Monotonicity of $A$ gives $mA(s)\le nA(t)\le(m+1)A(s)$. Dividing by $nA(s)$: $\left|\frac mn-\frac{A(t)}{A(s)}\right|<\epsilon$ (p. 29).
- Hence $\left|\frac{A(t)}{A(s)}-\frac{\log t}{\log s}\right|<2\epsilon$, so $A(t)=K\log t$. $K$ must be positive to satisfy (2) (p. 29).

Now take commensurable probabilities $p_i=n_i/\sum n_i$ with integer $n_i$. A choice among $\sum n_i$ equal options can be split into a choice among $n$ groups with probabilities $p_i$, then a choice within group $i$ among $n_i$. Using condition (3) again (p. 29):
$$K\log\sum n_i=H(p_1,\dots,p_n)+K\sum p_i\log n_i .$$
$$H=K\Big[\sum p_i\log\sum n_i-\sum p_i\log n_i\Big]=-K\sum p_i\log\frac{n_i}{\sum n_i}=-K\sum p_i\log p_i .$$
For incommensurable $p_i$, approximate by rationals; the same form holds by the continuity assumption. $K$ only fixes the unit of measure (p. 29).

*Intuition note.* Given continuity, the monotonic growth of the equal-choice entropy $A(n)$, and additivity under splitting a choice, the only possible formula is this one, up to the choice of unit.

### Appendix 3: theorems on ergodic sources (pp. 29–30)
- If one can go from any state with $P>0$ to any other along a path of probability $p>0$, the source is ergodic and the strong law of large numbers applies (p. 29).
- In a long sequence of length $N$, the path $p_{ij}$ is used about $P_ip_{ij}N$ times, where $P_i$ is the probability of being in state $i$. For large $N$, except on a small-probability set, the counts lie within $(P_ip_{ij}\pm\delta)N$ (p. 29).
- So nearly all sequences have probability $p=\prod p_{ij}^{(P_ip_{ij}\pm\delta)N}$ (p. 29).
- Hence $\frac{\log p}{N}=\sum(P_ip_{ij}\pm\delta)\log p_{ij}$, i.e. $\left|\frac{\log p}{N}-\sum P_ip_{ij}\log p_{ij}\right|<\eta$. This proves Theorem 3. Theorem 4 follows by bounding $n(q)$ with the range of $p$ in Theorem 3 (p. 30).
- Mixed (non-ergodic) case, $L=\sum p_iL_i$, component entropies $H_1\ge H_2\ge\dots\ge H_n$: $\lim_{N\to\infty}\frac{\log n(q)}{N}=\varphi(q)$, a decreasing step function with $\varphi(q)=H_s$ for $\sum_1^{s-1}\alpha_i<q<\sum_1^s\alpha_i$ (p. 30). The $\alpha_i$ are not defined in these pages.
- Theorems 5 and 6: $F_N$ decreases with $N$ because increasing $N$ adds a subscript to a conditional entropy. Substituting in the definition gives $F_N=NG_N-(N-1)G_{N-1}$. Summing over $N$ gives $G_N=\frac1N\sum_1^N F_n$. So $G_N\ge F_N$ and $G_N$ decreases. They approach the same limit, and by Theorem 3 $\lim G_N=H$ (p. 30).

### Appendix 4: maximising the rate under constraints (pp. 30–31)
Setting: finite-state constraints, drawn as a graph. Symbol $s$ going from state $i$ to $j$ has length $\ell^{(s)}_{ij}$. The question is which $P_i$ and $p^{(s)}_{ij}$ maximise the information rate (p. 30).
- The constraints define a discrete channel, so the maximum rate is at most its capacity $C$. Shannon shows $C$ is achieved by a proper choice of $P_i,p^{(s)}_{ij}$ (p. 30).
- Rate: $\dfrac{-\sum P_ip^{(s)}_{ij}\log p^{(s)}_{ij}}{\sum P_ip^{(s)}_{ij}\ell^{(s)}_{ij}}=\dfrac NM$ (p. 30).
- Put $\ell_{ij}=\sum_s\ell^{(s)}_{ij}$ (as printed). For a maximum, $p^{(s)}_{ij}=k\exp\ell^{(s)}_{ij}$ (as printed). The constraints are $\sum P_i=1$, $\sum_jp_{ij}=1$, $\sum P_i(p_{ij}-\delta_{ij})=0$. Maximise
$$U=\frac{-\sum P_ip_{ij}\log p_{ij}}{\sum P_ip_{ij}\ell_{ij}}+\lambda\sum_iP_i+\sum\mu_ip_{ij}+\sum\eta_jP_i(p_{ij}-\delta_{ij}),$$
$$\frac{\partial U}{\partial p_{ij}}=-\frac{MP_i(1+\log p_{ij})+NP_i\ell_{ij}}{M^2}+\lambda+\mu_i+\eta_iP_i=0 .$$
- Solving: $p_{ij}=A_iB_jD^{-\ell_{ij}}$. Since $\sum_jp_{ij}=1$, $A_i^{-1}=\sum_jB_jD^{-\ell_{ij}}$ and $p_{ij}=\dfrac{B_jD^{-\ell_{ij}}}{\sum_sB_sD^{-\ell_{is}}}$ (p. 31).
- The correct $D$ is the capacity $C$, and the $B_j$ solve $B_i=\sum_jB_jC^{-\ell_{ij}}$. Then $p_{ij}=\frac{B_j}{B_i}C^{-\ell_{ij}}$, and stationarity $\sum_iP_ip_{ij}=P_j$ becomes $\sum_i\frac{P_i}{B_i}C^{-\ell_{ij}}=\frac{P_j}{B_j}$. So if $\gamma_i$ satisfies $\sum\gamma_iC^{-\ell_{ij}}=\gamma_j$, take $P_i=B_i\gamma_i$. Both systems are solvable because $C$ satisfies $|C^{-\ell_{ij}}-\delta_{ij}|=0$ (p. 31).
- The rate becomes $C-\dfrac{\sum P_ip_{ij}\log\frac{B_j}{B_i}}{\sum P_ip_{ij}\ell_{ij}}$ (as printed, with $C$ standing for the rate). The numerator is $\sum_jP_j\log B_j-\sum_iP_i\log B_i=0$. So the rate is $C$; it can never be exceeded, so this is the maximum (p. 31).

*Skip path:* carry forward only "the optimal source for a constrained channel has rate $C$, using $p_{ij}=\frac{B_j}{B_i}C^{-\ell_{ij}}$".

*Intuition note.* The upper limit for a constrained channel is the rate you would get if all long blocks were equally likely, namely the capacity $C$. Shannon shows that a suitable choice of $P_i,p_{ij}$ reaches this limit.

### Part III: Mathematical preliminaries (pp. 32–40)
**Introduction (p. 32).** Continuous cases can largely be obtained as limits of discrete cases by cutting the continuum into many small regions. Some new effects appear. Shannon does not aim at full generality or rigor (this would need measure theory). He says a rigorous axiomatic formulation covering both cases appears possible, and the liberties taken can be justified in all cases of practical interest (p. 32).

#### 18. Sets and ensembles of functions (pp. 32–34)
- A *set of functions* is a collection of functions, usually of time. Examples: $f_\theta(t)=\sin(t+\theta)$; all functions with no frequency above $W$; all functions band-limited to $W$ and amplitude-limited to $A$; all English speech signals (p. 32).
- An *ensemble* is a set plus a probability measure. Example: $\sin(t+\theta)$ with a distribution $P(\theta)$ (p. 32).
- Further ensembles: a finite set $f_k$ with probabilities $p_k$; a finite-dimensional family $f(\alpha_1,\dots,\alpha_n;t)$ with distribution $p(\alpha_1,\dots,\alpha_n)$, for instance $\sum_{i=1}^na_i\sin i(\omega t+\theta_i)$ with normal independent amplitudes and independent uniform phases (p. 32).
- White noise band-limited to $W$ with average power $N$: $f(a_i,t)=\sum_{n=-\infty}^{\infty}a_n\frac{\sin\pi(2Wt-n)}{\pi(2Wt-n)}$ with $a_i$ independent normal, each with standard deviation $\sqrt N$ (p. 33).
- Shot noise: identical functions $f(t)$ placed at Poisson-distributed points $t_k$ and added, $\sum_kf(t+t_k)$. English speech with its frequency-of-use measure is another example (p. 33).
- **Stationary:** the ensemble is unchanged by shifting all functions in time. $\sin(t+\theta)$ with $\theta$ uniform on $[0,2\pi)$ is stationary: shifting by $t_1$ gives $\sin(t+\varphi)$ with $\varphi$ again uniform (p. 33).
- **Ergodic:** stationary, and no subset of probability other than 0 or 1 is itself stationary. $\sin(t+\theta)$ is ergodic. $a\sin(t+\theta)$ with $a$ normal and $\theta$ uniform is stationary but not ergodic, because the subset with $0<a<1$ is stationary (p. 33).
- Of the five examples given, 3 and 4 are ergodic and 5 "may perhaps" be (p. 33).
- Ergodic theorem (stated roughly): for an ergodic ensemble an average of any statistic over the ensemble equals, with probability 1, the time-average along one function. Each function is "typical" of the ensemble (p. 33).
- An operator $T$ maps ensemble $f_\alpha$ to $g_\alpha=Tf_\alpha$, with the induced measure. This models a filter, rectifier or modulator (p. 34).
- $T$ is *invariant* if shifting the input shifts the output by the same amount. If $T$ is invariant and the input is stationary, the output is stationary; likewise for ergodic (proved in Appendix 5). Filters and rectifiers are invariant. Modulation is not, but is invariant under shifts that are multiples of the carrier period (p. 34).
- Wiener showed that if a device is linear as well as invariant, Fourier analysis is the appropriate tool. Communication theory concerns operations on ensembles, not on single functions: a system is designed for the ensemble of speech functions (p. 34).

#### 19. Band-limited ensembles (pp. 34–35)
**Theorem 13.** If $f(t)$ contains no frequencies over $W$, then
$$f(t)=\sum_{-\infty}^{\infty}X_n\frac{\sin\pi(2Wt-n)}{\pi(2Wt-n)},\qquad X_n=f\!\left(\frac n{2W}\right)$$
(p. 34). The proof is cited from Shannon's 1949 paper (footnote 5), not given here.
- The $X_n$ are coordinates in an infinite-dimensional function space, one point per function. A function is "substantially limited" to a time $T$ if all $X_n$ outside that interval are zero; then all but $2TW$ coordinates vanish. So functions of band $W$ and duration $T$ are points of a $2TW$-dimensional space (p. 35).
- Functions with total energy $\le E$ form a sphere of radius $r=\sqrt{2WE}$ in this space. An ensemble is a probability density $p(x_1,\dots,x_n)$ there (p. 35).

*Intuition note.* A band-limited signal of duration $T$ is fully described by $2TW$ numbers. That turns continuous-time problems into finite-dimensional geometry.

#### 20. Entropy of a continuous distribution (pp. 35–38)
Definitions (p. 35):
$$H=-\int_{-\infty}^{\infty}p(x)\log p(x)\,dx,\qquad H=-\int\!\!\cdots\!\!\int p(x_1,\dots,x_n)\log p(x_1,\dots,x_n)\,dx_1\cdots dx_n .$$
$$H(x,y)=-\iint p(x,y)\log p(x,y)\,dx\,dy,\qquad H_x(y)=-\iint p(x,y)\log\frac{p(x,y)}{p(x)}\,dx\,dy,\qquad H_y(x)=-\iint p(x,y)\log\frac{p(x,y)}{p(y)}\,dx\,dy,$$
with $p(x)=\int p(x,y)dy$ and $p(y)=\int p(x,y)dx$. Continuous entropies have most (not all) properties of the discrete case:

1. If $x$ is confined to a volume $v$, $H(x)$ is maximal, equal to $\log v$, when $p$ is constant ($1/v$) there (p. 35).
2. $H(x,y)\le H(x)+H(y)$, with equality if (and only if) $x,y$ are independent, apart possibly from a set of probability zero (p. 36).
3. Averaging $p'(y)=\int a(x,y)p(x)dx$ with $\int a\,dx=\int a\,dy=1$ and $a\ge0$ gives entropy of $p'$ at least that of $p$ (p. 36).
4. $H(x,y)=H(x)+H_x(y)=H(y)+H_y(x)$ and $H_x(y)\le H(y)$ (p. 36).
5. Fixed standard deviation $\sigma$: maximum entropy is Gaussian. Maximise $-\int p\log p$ with $\sigma^2=\int px^2dx$, $1=\int p\,dx$. By the calculus of variations, maximise $\int[-p\log p+\lambda px^2+\mu p]dx$. The condition is $-1-\log p+\lambda x^2+\mu=0$. Adjusting the constants gives
$$p(x)=\frac1{\sqrt{2\pi}\sigma}e^{-(x^2/2\sigma^2)} .$$
In $n$ dimensions with second moments $A_{ij}=\int\!\cdots\!\int x_ix_jp\,dx_1\cdots dx_n$ fixed, the maximum (by a similar calculation) is the $n$-dimensional Gaussian with those moments (p. 36).

6. Entropy of a Gaussian (p. 37):
$$-\log p(x)=\log\sqrt{2\pi}\sigma+\frac{x^2}{2\sigma^2},$$
$$H(x)=\int p\log\sqrt{2\pi}\sigma\,dx+\int p\frac{x^2}{2\sigma^2}dx=\log\sqrt{2\pi}\sigma+\frac{\sigma^2}{2\sigma^2}=\log\sqrt{2\pi}\sigma+\log\sqrt e=\log\sqrt{2\pi e}\,\sigma .$$
For the $n$-dimensional Gaussian $p=\frac{|a_{ij}|^{1/2}}{(2\pi)^{n/2}}\exp\!\big(-\tfrac12\sum a_{ij}x_ix_j\big)$ ($a_{ij}$ is an $n\times n$ matrix), $H=\log(2\pi e)^{n/2}|a_{ij}|^{-1/2}$ (p. 37).

7. On a half line ($p=0$ for $x\le0$) with first moment $a=\int_0^\infty px\,dx$ fixed, the maximum is $p=\frac1ae^{-(x/a)}$, with entropy $\log ea$ (p. 37).
8. **Coordinate dependence.** Discrete entropy measures randomness absolutely; continuous entropy is relative to the coordinate system. Under a change to coordinates $y$ with Jacobian $J(x/y)$ (p. 37):
$$H(y)=-\int\!\!\cdots\!\!\int p(x)J\!\left(\tfrac xy\right)\log\Big[p(x)J\!\left(\tfrac xy\right)\Big]dy_1\cdots dy_n,\qquad H(y)=H(x)-\int\!\!\cdots\!\!\int p(x)\log J\!\left(\tfrac xy\right)dx_1\cdots dx_n .$$
The new entropy is the old one minus the expected log-Jacobian. Entropy measures randomness relative to a standard that gives equal weight to equal volume elements (p. 38).
   - Despite this, entropy is as important as in the discrete case, because information rate and capacity depend on a *difference* of two entropies, and both terms change by the same amount (p. 38).
   - Continuous entropy can be negative: the scale sets an arbitrary zero (a uniform distribution over unit volume). More confined distributions are negative. Rates and capacities are always non-negative (p. 38).
9. Linear map $y_j=\sum_ia_{ij}x_i$: the Jacobian is $|a_{ij}|^{-1}$ and $H(y)=H(x)+\log|a_{ij}|$. For a rotation (or any measure-preserving map) $J=1$ and $H(y)=H(x)$ (p. 38).

*Intuition note.* Rescaling a variable shifts its continuous entropy by a constant, like changing the unit of length. Only differences between two entropies in the same coordinates are meaningful, and capacity is such a difference.

#### 21. Entropy of an ensemble of functions (pp. 38–39)
- For an ergodic band-limited ensemble with density $p(x_1,\dots,x_n)$ over $n$ successive samples, the entropy per degree of freedom is $H'=-\lim_{n\to\infty}\frac1n\int\!\cdots\!\int p\log p\,dx_1\cdots dx_n$. The entropy per second is $H=2WH'$ since $n=2TW$ (p. 38).
- White thermal noise (Gaussian): $H'=\log\sqrt{2\pi eN}$ and $H=W\log2\pi eN$. For a given average power $N$, white noise has the maximum possible entropy, by the Gaussian maximising property (p. 38).
- Continuous analogue of the typical-sequence result: if $p$ is continuous in all $x_i$ for all $n$, then for large $n$ the quantity $\frac{\log p}{n}$ is within $\epsilon$ of $H'$ (printed without a minus sign; see Reading notes) for all samples except a set of probability less than $\delta$ (pp. 38–39).
- Volume statement: let $V_n(q)$ be the smallest volume containing probability $q$. Then $\lim_{n\to\infty}\frac{\log V_n(q)}n=H'$ provided $q\ne0,1$ (p. 39). So for large $n$ there is a well-defined volume of high probability (in the logarithmic sense), with roughly uniform density inside (p. 39).
- White noise: $p=(2\pi N)^{-n/2}\exp\!\big(-\frac1{2N}\sum x_i^2\big)$ has spherical symmetry. The high-probability region is a sphere of radius $\sqrt{nN}$. The probability of lying outside radius $\sqrt{n(N+\epsilon)}$ tends to zero, and $\frac1n\log$(volume) tends to $\log\sqrt{2\pi eN}$ (p. 39).
- **Entropy power.** The power of a white noise in the same band with the same entropy: $\overline N=\frac1{2\pi e}\exp2H'$. Geometrically, it is the squared radius of a sphere with the same volume as the high-probability region. Since white noise has maximum entropy for a given power, entropy power $\le$ actual power (p. 39).

#### 22. Entropy loss in linear filters (pp. 39–40)
**Theorem 14.** If an ensemble with entropy $H_1$ per degree of freedom in band $W$ passes through a filter with characteristic $Y(f)$, the output entropy is
$$H_2=H_1+\frac1W\int_W\log|Y(f)|^2\,df .$$
Proof sketch (p. 39): the filter is a linear coordinate change, diagonal in frequency components. The Jacobian (for $n$ sine and $n$ cosine components) is $J=\prod_{i=1}^n|Y(f_i)|^2$, the $f_i$ equally spaced in the band. In the limit it is $\exp\frac1W\int_W\log|Y(f)|^2df$. $J$ is constant, so its average is the same value; apply the coordinate-change result of §20. In entropy power: $\overline N_2=\overline N_1\exp\frac1W\int_W\log|Y|^2df$ (p. 39).
- The output entropy power is the input entropy power times the geometric mean (power) gain. In decibels, the output entropy power changes by the arithmetic mean dB gain over $W$ (p. 40).

**Table I** (ideal gains on $0\le\omega\le1$; impulse responses for $W=2\pi$, phase 0), copied from the image on p. 40:

| Gain | Entropy power factor | dB | Impulse response |
|---|---|---|---|
| $1-\omega$ | $1/e^2$ | $-8.69$ | $\frac{\sin^2(t/2)}{t^2/2}$ |
| $1-\omega^2$ | $(2/e)^4$ | $-5.33$ | $2\big[\frac{\sin t}{t^3}-\frac{\cos t}{t^2}\big]$ |
| $1-\omega^3$ | $0.411$ | $-3.87$ | $6\big[\frac{\cos t-1}{t^4}-\frac{\cos t}{2t^2}+\frac{\sin t}{t^3}\big]$ |
| $\sqrt{1-\omega^2}$ | $(2/e)^2$ | $-2.67$ | $\frac\pi2\frac{J_1(t)}t$ |
| flat, then linear fall to 0 over width $\alpha$ | $1/e^{2\alpha}$ | $-8.69\alpha$ | $\frac1{\alpha t^2}[\cos(1-\alpha)t-\cos t]$ |

- Other cases follow: the factor $1/e^2$ also applies to any gain obtained from $1-\omega$ by a measure-preserving transformation of the $\omega$ axis (for example $G=\omega$ or a sawtooth between 0 and 1). The reciprocal gain has the reciprocal factor (so $1/\omega$ has $e^2$). Raising the gain to a power raises the factor to that power (p. 40).

#### 23. Entropy of a sum of two ensembles (pp. 40–41)
- Adding ensembles gives the density as a convolution: $r(x_1,\dots,x_n)=\int\!\cdots\!\int p(y_1,\dots,y_n)q(x_1-y_1,\dots,x_n-y_n)dy_1\cdots dy_n$ (p. 41).
- **Theorem 15** (proved in Appendix 6). With average powers $N_1,N_2$ and entropy powers $\overline N_1,\overline N_2$, the entropy power of the sum satisfies $\overline N_1+\overline N_2\le\overline N_3\le N_1+N_2$ (p. 41).
- White Gaussian noise "absorbs" another ensemble: the entropy power of the sum is approximately the noise power plus the signal power, provided the signal power is small in a certain sense compared with the noise (p. 41).
- Argument: in $n$-dimensional function space the noise is a spherical Gaussian; the signal has second moments $a_{ij}$ about its centre of gravity (a positive definite $n\times n$ form), which can be rotated to diagonal form $b_{ii}$. Require each $b_{ii}$ small compared with $N$. The convolution is then approximately Gaussian with form $N+b_{ii}$, whose entropy power is
$$\Big[\prod(N+b_{ii})\Big]^{1/n}\doteq\Big[(N)^n+\sum b_{ii}(N)^{n-1}\Big]^{1/n}\doteq N+\frac1n\sum b_{ii}.$$
The last term is the signal power, the first the noise power (p. 41).

*Intuition note.* A small signal buried in large Gaussian noise adds its power almost exactly to the noise's entropy power. Adding independent noises never gives less entropy power than the sum of the entropy powers.

### Part IV: The continuous channel (pp. 41–47)

#### 24. Capacity of a continuous channel (pp. 41–43)
- Inputs and outputs are band-limited to $W$, so for time $T$ they are $2TW$ numbers. The input statistics are $P(x)=P(x_1,\dots,x_n)$; the noise is the conditional distribution $P_x(y)$ (pp. 41–42).
- Rate: $R=H(x)-H_y(x)$ (the equivocation is $H_y(x)$). Capacity $C$ is the maximum of $R$ over input ensembles. In a finite-dimensional approximation one maximises $-\int P(x)\log P(x)dx+\iint P(x,y)\log\frac{P(x,y)}{P(y)}dxdy$. This can be written as $\iint P(x,y)\log\frac{P(x,y)}{P(x)P(y)}dxdy$ (p. 42). Hence
$$C=\lim_{T\to\infty}\max_{P(x)}\frac1T\iint P(x,y)\log\frac{P(x,y)}{P(x)P(y)}\,dx\,dy .$$
- $R$ and $C$ are independent of the coordinate system: numerator and denominator of the log are multiplied by the same factors under any one-to-one change of $x,y$. This integral form is more general than $H(x)-H_y(x)$, which can be $\infty-\infty$ (for example if $x$ is limited to a surface of fewer than $n$ dimensions) (p. 42).
- With base-2 logs, $C$ is the maximum number of binary digits per second sendable with arbitrarily small equivocation, as in the discrete case. Argument: divide the spaces into small cells over which $P_x(y)$ is substantially constant. This gives a discrete channel, and the capacity is the limit of the discrete capacities (p. 42).
- Mathematically (Appendix 7): if $u$ is the message, $x$ the signal, $y$ the received signal and $v$ the recovered message, then $H(x)-H_y(x)\ge H(u)-H_v(u)$ whatever operations produce $x$ from $u$ and $v$ from $y$. So no coding or decoding lets the binary-digit rate exceed $C$. Conversely, under very general conditions one can transmit at rate $C$ with arbitrarily small equivocation or error frequency. For example this holds if, in a finite-dimensional approximation, $P(x,y)$ is continuous in both $x$ and $y$ except on a set of probability zero (p. 42).
- **Additive independent noise:** $P_x(y)=Q(y-x)$, so the noise has a definite entropy $H(n)$ independent of the signal (pp. 42–43).

**Theorem 16.** If signal and noise are independent and $y=x+n$, then
$$R=H(y)-H(n),\qquad C=\max_{P(x)}H(y)-H(n).$$
Proof (p. 43): $H(x,y)=H(x,n)$. Expanding the left side and using independence of $x$ and $n$: $H(y)+H_y(x)=H(x)+H(n)$. Hence $R=H(x)-H_y(x)=H(y)-H(n)$. Since $H(n)$ does not depend on $P(x)$, maximising $R$ means maximising $H(y)$, subject to any constraints on the transmitted ensemble (p. 43).

#### 25. Capacity with an average power limitation (pp. 43–45)
White thermal noise of power $N$, transmitted power at most $P$ (p. 43). The received power is $P+N$. The maximum $H(y)$ occurs when $y$ is also white noise, obtainable by transmitting white noise of power $P$. Then
$$H(y)=W\log2\pi e(P+N),\quad H(n)=W\log2\pi eN,\quad C=H(y)-H(n)=W\log\frac{P+N}{N}.$$

**Theorem 17.** The capacity of a channel of band $W$ perturbed by white thermal noise of power $N$, with average transmitter power limited to $P$, is $C=W\log\frac{P+N}{N}$ (p. 43). Meaning: with sufficiently involved encoding one can send binary digits at $W\log_2\frac{P+N}N$ bits per second with arbitrarily small error frequency. One cannot send faster by any encoding without a definite positive error frequency. To approach this rate the transmitted signals must approximate white noise in statistical properties (p. 43).

*Intuition note.* Informally (our gloss, not in the text): the signal-to-noise ratio sets how finely amplitudes can be told apart. The formula says each of the $2W$ numbers per second carries $\tfrac12\log(1+P/N)$ bits (our reading: $W\log$ per second divided by $2W$ samples).

Approaching the limit (p. 44):
- Build $M=2^s$ samples of white noise, each of duration $T$, numbered $0$ to $M-1$. The transmitter splits the message into groups of $s$ bits and sends the matching noise sample.
- The receiver knows the samples and picks the one with least R.M.S. discrepancy from the received signal. This amounts to choosing the most probable (a posteriori) signal.
- With $M(\epsilon,T)$ depending on the tolerable error frequency $\epsilon$, for almost all selections of samples $\lim_{\epsilon\to0}\lim_{T\to\infty}\frac{\log M(\epsilon,T)}T=W\log\frac{P+N}N$ (p. 44).
- Similar formulas were developed independently by Wiener, Tuller and Sullivan, with somewhat different interpretations (p. 44).

**Arbitrary noise.** The maximisation does not appear to be explicitly solvable, but bounds are available (p. 44).

**Theorem 18.** With average transmitter power $P$, average noise power $N$ and noise entropy power $N_1$:
$$W\log\frac{P+N_1}{N_1}\le C\le W\log\frac{P+N}{N_1}\qquad\text{(p. 44).}$$
Proof (pp. 44–45): the received power is $P+N$. The largest possible entropy at that power is $W\log2\pi e(P+N)$ (reached if the output were white). There may be no input ensemble that makes it so, but this bounds $H(y)$ above. So $C=\max H(y)-H(n)\le W\log2\pi e(P+N)-W\log2\pi eN_1$. For the lower bound, transmit white noise of power $P$. By Theorem 15 the received entropy power is at least $P+N_1$, so $\max H(y)\ge W\log2\pi e(P+N_1)$ and $C\ge W\log\frac{P+N_1}{N_1}$.
- As $P$ increases the bounds approach each other, giving the asymptotic rate $W\log\frac{P+N}{N_1}$. For white noise $N=N_1$ and $C=W\log(1+P/N)$ (p. 45).
- For Gaussian noise with non-flat spectrum $N(f)$, $N_1$ is the geometric mean: $N_1=\exp\frac1W\int_W\log N(f)\,df$ (p. 45).

**Theorem 19.** Write the capacity at power $P$ as $C=W\log\frac{P+N-\eta}{N_1}$. Then $\eta$ is monotonic decreasing as $P$ increases and tends to $0$ (p. 45).
Proof (p. 45): suppose at power $P_1$ the best signal distribution $p(x)$ added to noise $q(x)$ gives a received distribution of entropy power $P_1+N-\eta_1$. Add white noise of power $\Delta P$ to the signal. By Theorem 15 the received entropy is at least $W\log2\pi e(P_1+N-\eta_1+\Delta P)$. The maximising distribution must do at least as well, so $\eta$ decreases. For $\eta\to0$: use white-noise signals with large $P$; the received signal is then approximately white, with entropy power approaching $P+N$.

#### 26. Capacity with a peak power limitation (pp. 45–47)
The constraint is that every transmitted function satisfies $|f(t)|\le\sqrt S$. It works out less well than the average-power case. Shannon gets "a lower bound valid for all $S/N$, an 'asymptotic' upper bound (valid for large $S/N$) and an asymptotic value of $C$ for small $S/N$" (p. 45).

**Theorem 20** (white thermal noise power $N$, peak power $S$) (p. 46):
- $C\ge W\log\frac2{\pi e^3}\frac SN$.
- For sufficiently large $S/N$: $C\le W\log\frac{\frac2{\pi e}S+N}{N}(1+\epsilon)$, with $\epsilon$ arbitrarily small.
- As $S/N\to0$ (and provided the band $W$ starts at 0): $C\big/W\log(1+S/N)\to1$.

*Upper bound* (p. 46). For large $S/N$, maximising $H(y)$ is nearly maximising the transmitted entropy. Relax the constraint: limit power to $S$ only at sample points. The maximum entropy then occurs for independent samples uniformly distributed on $[-\sqrt S,+\sqrt S]$, with entropy $W\log4S$. The received entropy is below $W\log(4S+2\pi eN)(1+\epsilon)$, with $\epsilon\to0$ as $S/N\to\infty$. Subtracting the noise entropy $W\log2\pi eN$:
$$W\log(4S+2\pi eN)(1+\epsilon)-W\log2\pi eN=W\log\frac{\frac2{\pi e}S+N}{N}(1+\epsilon).$$

*Lower bound* (pp. 46–47). Pass the same ensemble through an ideal filter with triangular gain: unity at frequency 0, falling linearly to 0 at $W$.
- First show the output has peak power $S$ at all times. A pulse $\frac{\sin2\pi Wt}{2\pi Wt}$ becomes $\frac12\frac{\sin^2\pi Wt}{(\pi Wt)^2}$, which is never negative. The input is a sum of shifted pulses with coefficients $a$, $|a|\le\sqrt S$. The output is the sum of shifted non-negative functions with the same coefficients. Its largest positive value is reached when all $a=\sqrt S$. Then the input is the constant $\sqrt S$ and, since the filter has unit gain at DC, the output is also $\sqrt S$. So the peak power is $S$ (p. 46).
- By Theorem 14 the output entropy equals the input entropy plus the filter's mean log gain: $\int_0^W\log G^2df=\int_0^W\log\!\big(\frac{W-f}W\big)^2df=-2W$. So the output entropy is $W\log4S-2W=W\log\frac{4S}{e^2}$, and the capacity exceeds $W\log\frac2{\pi e^3}\frac SN$ (p. 47).

*Small $S/N$* (p. 47). Since $P\le S$: $C\le W\log(1+P/N)\le W\log(1+S/N)$. It suffices to find a peak-limited, band-limited ensemble with rate near $W\log(1+S/N)$. Take runs of $t$ equal samples, each run $+\sqrt S$ or $-\sqrt S$ with probability $\frac12$, passed through the triangular filter (unit DC gain). The output is peak-limited to $S$, and its average power is nearly $S$ for large $t$. The small-signal result of §23 applies if $\sqrt t\,S/N$ is sufficiently small, which holds for small enough $S/N$ after $t$ is chosen. Then the entropy power is as close as desired to $S+N$, and the rate to $W\log\frac{S+N}N$ (p. 47).

### Part V: The rate for a continuous source (pp. 47–51)

#### 27. Fidelity evaluation functions (pp. 47–49)
- A continuous quantity needs infinitely many binary digits for exact specification, so exact transmission needs infinite capacity and is impossible over a noisy channel. Shannon calls this evading the real issue: we want transmission only to within a tolerance. The question is whether a definite rate can be assigned for a given fidelity. A channel of smaller capacity than that rate would be insufficient (pp. 47–48).
- Setup: the source is described by density $P(x)$ over messages of duration $T$; the system by $P_x(y)$; the whole by $P(x,y)$. A fidelity criterion must at least give a simple ordering of systems, so it is a numerical function $v(P(x,y))$ (p. 48).
- Claim: under general, reasonable assumptions, $v(P(x,y))=\iint P(x,y)\rho(x,y)\,dx\,dy$. Assumptions: (1) source and system are ergodic; (2) the evaluation is "reasonable": a tentative evaluation $\rho(x,y)$ from one typical input/output pair approaches, with probability 1 as the duration grows, the exact evaluation based on $P(x,y)$. Then $\rho(x,y)\to v(P(x,y))=\iint P\rho\,dxdy$ as $T\to\infty$ for almost all $(x,y)$ in the high-probability region, using $\iint P\,dxdy=1$ (p. 48).
- $\rho$ is a "distance" measuring how undesirable it is to receive $y$ when $x$ was sent. It is not a metric in the strict sense (it need not be symmetric or satisfy the triangle inequality; footnote 9) (p. 48).
- Examples (p. 49): (1) R.M.S. criterion, $\rho=\frac1T\int_0^T[x(t)-y(t)]^2dt$, the squared Euclidean distance up to a constant; (2) frequency-weighted R.M.S.: pass $e(t)=x(t)-y(t)$ through a shaping filter $k$, $f(t)=\int e(\tau)k(t-\tau)d\tau$, $\rho=\frac1T\int_0^Tf(t)^2dt$; (3) absolute error, $\rho=\frac1T\int_0^T|x(t)-y(t)|dt$; (4) the ear and brain imply evaluations, e.g. an intelligibility criterion where $\rho$ is the relative frequency of wrongly interpreted words, which could in principle be found by experiment; (5) the discrete case, $\rho$ = fraction of symbols in $y$ differing from those in $x$.

#### 28. The rate for a source relative to a fidelity evaluation (pp. 49–50)
With $\rho$ continuous, the quality is $v=\iint\rho(x,y)P(x,y)dxdy$ and the information flow is $R=\iint P(x,y)\log\frac{P(x,y)}{P(x)P(y)}dxdy$. Define
$$R_1=\min_{P_x(y)}\iint P(x,y)\log\frac{P(x,y)}{P(x)P(y)}\,dx\,dy\quad\text{subject to}\quad v_1=\iint P(x,y)\rho(x,y)\,dx\,dy .$$
That is: among all systems with the required fidelity, take the one with the least rate (pp. 49–50).

**Theorem 21.** If a source has rate $R_1$ for fidelity $v_1$, its output can be encoded and sent over a channel of capacity $C$ with fidelity as near $v_1$ as desired provided $R_1\le C$. This is not possible if $R_1>C$ (p. 50).
- The negative part follows from the definition of $R_1$ and earlier results: otherwise more than $C$ bits per second could be sent (p. 50).
- The positive part is proved analogously to Theorem 11. Divide the $(x,y)$ space into small cells (a discrete case). Let $P_1(x,y)$ be the rate-minimising system. Choose at random $2^{(R_1+\epsilon)T}$ high-probability $y$'s. Each connects by a high-probability "fan" to a set of $x$'s (Fig. 10, in Part 1, not in these pages). For large $T$ almost all $x$'s are covered by the fans for almost all choices of the $y$'s (p. 50).
- The system: the chosen points get binary numbers. A message $x$ lies (probability $\to1$) in at least one fan; its number is sent with channel coding, which is possible since $R_1\le C$. The receiver reconstructs the corresponding $y$. The evaluation approaches $v_1$ as $T\to\infty$ (p. 50).
- The noise in the recovered message is produced by this quantizing at the transmitter, not by channel noise, somewhat like quantizing noise in PCM (p. 50).

#### 29. The calculation of rates (pp. 50–51)
- Rate is like capacity: $R$ is a *minimum* with $P(x)$ and $v_1$ fixed; $C$ is a *maximum* with $P_x(y)$ fixed and possibly constraints of the form $K=\iint P\lambda\,dxdy$ (p. 50).
- Lagrange's method: vary $\iint[P\log\frac{P(x,y)}{P(x)P(y)}+\mu P\rho+\nu(x)P]dxdy$. The first variation gives (printed with $\lambda$ for the multiplier; p. 51)
$$P_y(x)=B(x)e^{-\lambda\rho(x,y)},\qquad\int B(x)e^{-\lambda\rho(x,y)}dx=1,$$
with $\lambda$ chosen to give the required fidelity. With best encoding, $P_y(x)$ declines exponentially with the distance $\rho(x,y)$ (p. 51).
- If $\rho(x,y)=\rho(x-y)$, then $B$ is constant ($\alpha$) and $P_y(x)=\alpha e^{-\lambda\rho(x-y)}$. These formal solutions are "difficult to evaluate" and seem of little value; rates have been calculated only in a few very simple cases (p. 51).
- White-noise source, mean-square criterion with $N=\overline{(x-y)^2}$: $R=\min[H(x)-H_y(x)]=H(x)-\max H_y(x)$. The maximum of $H_y(x)$ occurs when $y-x$ is white noise, equal to $W_1\log2\pi eN$ ($W_1$ is the source bandwidth). So $R=W_1\log2\pi eQ-W_1\log2\pi eN=W_1\log\frac QN$, with $Q$ the average message power (p. 51).

**Theorem 22.** The rate for a white-noise source of power $Q$ and band $W_1$ relative to an R.M.S. fidelity measure is $R=W_1\log\frac QN$, where $N$ is the allowed mean square error (p. 51).

**Theorem 23.** For any source of band $W_1$, average power $Q$, entropy power $Q_1$ and allowed mean square error $N$:
$$W_1\log\frac{Q_1}{N}\le R\le W_1\log\frac QN\qquad\text{(p. 51).}$$
The lower bound holds because $\max H_y(x)$ for given $\overline{(x-y)^2}=N$ occurs in the white-noise case. The upper bound results from placing the points of the Theorem 21 proof at random in a sphere of radius $\sqrt{Q-N}$ instead of in the best way (p. 51).

*Intuition note.* To copy a source with error power $N$, you must pay $W_1\log(Q/N)$ bits per second (our reading: $\log(Q/N)$ per pair of samples): the more accuracy you want, the more bits. Among sources of the same power $Q$ and band, white noise costs the most (the upper bound of Theorem 23), since its entropy power equals its power.

### Acknowledgments (p. 52)
Shannon thanks colleagues Bode, Pierce, McMillan and Oliver, and credits Wiener's solution of filtering and prediction of stationary ensembles as an influence (p. 52).

### Appendix 5: invariant operators preserve stationarity and ergodicity (p. 52)
- Let $S_1$ be a measurable subset of the $g$ ensemble and $S_2$ the subset of the $f$ ensemble giving it: $S_1=TS_2$. Let $H^\lambda$ shift all functions by time $\lambda$. Since $T$ is invariant it commutes with $H^\lambda$: $H^\lambda S_1=TH^\lambda S_2$. Hence $m[H^\lambda S_1]=m[TH^\lambda S_2]=m[H^\lambda S_2]=m[S_2]=m[S_1]$. The second equality is the definition of measure in $g$-space, the third is stationarity of $f$, the last is the definition again. So the output is stationary (p. 52).
- Ergodicity: let $S_1$ be an $H^\lambda$-invariant subset of the $g$ ensemble and $S_2$ the set of $f$ mapping into it. Then $H^\lambda S_1=TH^\lambda S_2=S_1$, so $H^\lambda S_2\subseteq S_2$ for all $\lambda$. Since $m[H^\lambda S_2]=m[S_1]$ this implies $H^\lambda S_2=S_2$ for all $\lambda$ with $m[S_2]\ne0,1$. This contradicts ergodicity of the input, so such an $S_1$ does not exist (p. 52).

### Appendix 6: proof of Theorem 15 (pp. 52–53)
- Upper bound $\overline N_3\le N_1+N_2$: the maximum entropy for power $N_1+N_2$ occurs for white noise of that power, whose entropy power is $N_1+N_2$ (p. 52).
- Lower bound: ask which $p,q$ with entropy powers $\overline N_1,\overline N_2$ minimise the entropy $H_3=-\int r\log r$ of their convolution $r$, subject to $H_1,H_2$ fixed (p. 52). Minimise
$$U=-\int[r\log r+\lambda p\log p+\mu q\log q]dx,\qquad\delta U=-\int\{[1+\log r]\delta r+\lambda[1+\log p]\delta p+\mu[1+\log q]\delta q\}dx .$$
Varying $p$ at $x_i=s_i$ gives $\delta r=q(x_i-s_i)$ and $\delta U=-\int q(x_i-s_i)\log r(x_i)dx_i-\lambda\log p(s_i)=0$; similarly for $q$. The conditions for a minimum are (p. 53)
$$\int q(x_i-s_i)\log r(x_i)dx_i=-\lambda\log p(s_i),\qquad\int p(x_i-s_i)\log r(x_i)dx_i=-\mu\log q(s_i).$$
- Multiply the first by $p(s_i)$, the second by $q(s_i)$, and integrate over $s_i$: $H_3=-\lambda H_1$, $H_3=-\mu H_2$. Substituting: $H_1\int q(x_i-s_i)\log r\,dx_i=-H_3\log p(s_i)$ and $H_2\int p(x_i-s_i)\log r\,dx_i=-H_3\log q(s_i)$ (p. 53).
- Normal case: $p=\frac{|A_{ij}|^{n/2}}{(2\pi)^{n/2}}e^{-\frac12\sum A_{ij}x_ix_j}$, $q$ likewise with $B_{ij}$. Then $r$ is normal with form $C_{ij}$, and with inverse forms $a_{ij},b_{ij},c_{ij}$: $c_{ij}=a_{ij}+b_{ij}$ (all $n\times n$). Shannon states that the normals satisfy the minimising conditions if and only if $a_{ij}=Kb_{ij}$, and so give the minimum $H_3$ under the constraints (p. 53).
- Check: $\log r=\frac n2\log\frac1{2\pi}|C_{ij}|-\frac12\sum C_{ij}x_ix_j$, so $\int q(x_i-s_i)\log r\,dx_i=\frac n2\log\frac1{2\pi}|C_{ij}|-\frac12\sum C_{ij}s_is_j-\frac12\sum C_{ij}b_{ij}$. This should equal $\frac{H_3}{H_1}\big[\frac n2\log\frac1{2\pi}|A_{ij}|-\frac12\sum A_{ij}s_is_j\big]$, which requires $A_{ij}=\frac{H_1}{H_3}C_{ij}$. Then also $A_{ij}=\frac{H_1}{H_2}B_{ij}$, and both equations reduce to identities (p. 53).

### Appendix 7: a more general approach to the central definitions (pp. 54–55)
**General definition of $R$** (p. 54). Take a probability measure space of pairs $(x,y)$ (transmitted and received signals of long duration $T$). Partition $x$ and $y$ into non-overlapping measurable sets $X_i,Y_i$. $P(X_i)$ and $P(Y_i)$ are the measures of the strips over $X_i$ and $Y_i$, and $P(X_i,Y_i)$ is the measure of their intersection. Approximate
$$R_1=\frac1T\sum_iP(X_i,Y_i)\log\frac{P(X_i,Y_i)}{P(X_i)P(Y_i)} .$$
- Further subdivision never decreases $R_1$. Split $X_1=X_1'+X_1''$ with $P(Y_1)=a$, $P(X_1)=b+c$, $P(X_1')=b$, $P(X_1'')=c$, $P(X_1',Y_1)=d$, $P(X_1'',Y_1)=e$, $P(X_1,Y_1)=d+e$. The term $(d+e)\log\frac{d+e}{a(b+c)}$ is replaced by $d\log\frac d{ab}+e\log\frac e{ac}$. It is "easily shown" that $\big[\frac{d+e}{b+c}\big]^{d+e}\le\frac{d^de^e}{b^dc^e}$, so the sum increases (p. 54).
- So the subdivisions form a directed set with $R_1$ monotonically increasing under refinement. $R$ is defined as the least upper bound, written $R=\frac1T\iint P(x,y)\log\frac{P(x,y)}{P(x)P(y)}dxdy$. This includes the discrete and continuous cases and others (p. 54).
- Consequences: if $x$ and $u$ are in one-to-one correspondence, the rate from $u$ to $y$ equals that from $x$ to $y$. If $v$ is any function of $y$, $R(x,y)\ge R(x,v)$, since subdivisions of $y$ are finer than those for $v$. More generally if $y,v$ are statistically related, $R(x,v)\le R(x,y)$: any operation on the received signal, even a random one, does not increase $R$ (p. 54).

**Dimension rate** (pp. 54–55). The average number of dimensions per second needed to specify an ensemble member; in the band-limited case $2W$ numbers per second suffice. Let $\rho_T[f_\alpha(t),f_\beta(t)]$ measure the distance over time $T$ (e.g. R.M.S.). Let $N(\epsilon,\delta,T)$ be the least number of functions such that all ensemble elements, apart from a set of measure $\delta$, lie within distance $\epsilon$ of one of them. Define
$$\lambda=\lim_{\delta\to0}\lim_{\epsilon\to0}\lim_{T\to\infty}\frac{\log N(\epsilon,\delta,T)}{T\log\epsilon}.$$
This generalises measure-type definitions of dimension in topology and agrees with the intuitive dimension rate for simple ensembles (p. 55).

## Toy example (ours, not from the text)
Gaussian channel with $W=1000$ Hz, noise power $N=1$ (arbitrary units), signal power $P=3$.
1. Samples per second: $2W=2000$.
2. Entropy of a Gaussian per sample, using $H=\log_2\sqrt{2\pi e\,\sigma^2}$ with $2\pi e\approx17.08$. Received signal ($\sigma^2=P+N=4$): $\tfrac12\log_2(17.08\times4)=\tfrac12\log_2 68.32\approx\tfrac12(6.095)\approx3.05$ bits. Noise ($\sigma^2=1$): $\tfrac12\log_2 17.08\approx\tfrac12(4.095)\approx2.05$ bits.
3. Difference per sample: $3.05-2.05\approx1.00$ bit. Per second: $2000\times1=2000$ bits/s.
4. Check with Theorem 17: $C=W\log_2\frac{P+N}N=1000\log_2 4=1000\times2=2000$ bits/s. ✓.

Coordinate-dependence check: $x$ uniform on $[0,\tfrac12]$ has $H=\log_2\tfrac12=-1$ bit (negative). Let $y=2x$, uniform on $[0,1]$, $H(y)=0$. Property 9 gives $H(y)=H(x)+\log_2 2=-1+1=0$. ✓. The difference of two entropies computed in the same coordinates is unaffected by such rescaling.

## Concepts
- [[differential-entropy]] — $H=-\int p\log p\,dx$; relative to coordinates, can be negative, changes by $-E[\log J]$ under a change of variables (pp. 35, 37–38)
- [[channel-capacity]] — here $C=\lim\max\frac1T\iint P\log\frac{P(x,y)}{P(x)P(y)}$, coordinate-free; with independent additive noise $C=\max H(y)-H(n)$ (pp. 42–43)
- [[shannon-hartley-formula]] — Theorem 17: $C=W\log\frac{P+N}N$ for white thermal noise, band $W$, average power $P$ (p. 43)
- [[maximum-entropy-principle]] — Gaussian maximises entropy for fixed second moments; exponential for fixed mean on a half line; uniform on a bounded volume (pp. 35–37)
- [[mutual-information]] — appears as the integrand $\log\frac{P(x,y)}{P(x)P(y)}$ defining $R$; Appendix 7 defines it as a supremum over partitions (pp. 42, 54)
- [[typical-set-aep]] — continuous version: $\frac{\log p}n$ within $\epsilon$ of $H'$ as printed (see Reading notes) and $\lim\frac{\log V_n(q)}n=H'$ (pp. 38–39)
- [[rate-distortion-function]] — $R_1$: minimum $R$ over systems with average distortion $v_1$; the author calls it the rate of a source "for a given quality" (pp. 49–50)
- [[data-processing-inequality]] — $R(x,v)\le R(x,y)$ for any operation on $y$ (p. 54)
- [[noisy-channel-coding-theorem]] — continuous version: rate $C$ achievable under general conditions; higher rates not (p. 42, p. 43)
- [[entropy-power]] (new) — power of the white noise with the same entropy: $\overline N=\frac1{2\pi e}e^{2H'}$; at most the actual power (p. 39)
- [[ensemble-of-functions]] (new) — a set of functions with a probability measure; stationary and ergodic ensembles are the objects of study (pp. 32–33)
- [[band-limited-sampling]] (new) — Theorem 13: a signal with no frequencies above $W$ is fixed by samples every $\frac1{2W}$ s; $2TW$ dimensions (pp. 34–35)
- [[fidelity-criterion]] (new) — evaluation $v=\iint P\rho$ with a "distance" $\rho$, justified by ergodicity and "reasonableness" (pp. 48–49)
- [[dimension-rate]] (new) — $\lambda$, the average dimensions per second of an ensemble, by a triple limit (pp. 54–55)

## Canonical instances
- [[white-gaussian-noise-channel]] — capacity $W\log(P+N)/N$ with white-noise coding by random codebooks (pp. 43–44)
- [[gaussian-max-entropy]] — variational proof that the Gaussian has maximal entropy at fixed variance; entropy $\log\sqrt{2\pi e}\sigma$ (pp. 36–37)
- [[peak-power-limited-channel]] — Theorem 20, with a triangular filter keeping the peak power at $S$ (pp. 46–47)
- [[white-noise-source-rms-rate]] — Theorem 22: $R=W_1\log Q/N$ (p. 51)
- [[linear-filter-entropy-loss]] — Theorem 14 and Table I (pp. 39–40)

## Bridges (candidates)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints.
- [same-math] $R_1=\min$ of mutual information at fixed average distortion ↔ rate–distortion function $R(D)$: same optimisation; the exponential solution $P_y(x)=B(x)e^{-\lambda\rho}$ is its first-order condition.
- [same-math] Appendix 7: $R(x,v)\le R(x,y)$ ↔ data processing inequality.
- [structural-analogy] Coordinate-free capacity (difference of two entropies) ↔ KL divergence / mutual information as invariant under reparametrisation.
- [structural-analogy] Capacity limit on received information ↔ rational inattention: an agent's attention treated as a channel with a bit-rate ceiling.
- [metaphor] "Noise from quantizing at the transmitter, not channel noise" (p. 50) ↔ coarse-graining in survey or social data, where measurement resolution creates "noise".

## Questions this raises
- Why does the achievability of $W\log(1+P/N)$ require the signal to look like white noise? What happens to the optimal input when the noise spectrum is not flat (Theorem 18 only gives bounds)?
- How tight are Theorems 20 and 23 in the intermediate regimes, between small and large $S/N$, or for non-white sources?
- Can the "fidelity" function $\rho$ in §27 be chosen to reflect human perception (example 4), and how would the rate $R_1$ change?
- What does the ergodicity assumption buy in practice, and what fails for non-ergodic sources such as $a\sin(t+\theta)$?

## Reading notes
- **Where this part starts and ends.** It starts at the end of Appendix 2 (printed p. 29, mid-proof) and ends with Appendix 7 (p. 55). It covers Appendices 3–4, Parts III–V (§§18–29), the Acknowledgments and Appendices 5–7. Part 1 (pp. 1–28) is not included; the references to conditions (2) and (3), Theorem 11, Fig. 10, Theorems 3–6 and the definitions of $F_N,G_N,\alpha_i$ point back to it.
- **Page numbers:** printed = pdf (offset 0).
- **Text layer:** heavily garbled (symbols dropped). All equations were checked against the page images.
- **Probable printing slips (not corrected in the digest):**
  - p. 38: "$\left|\frac{\log p}{n}-H'\right|<\epsilon$" as printed. With the definition of $H'$ (leading minus sign), $-\frac{\log p}{n}$ would be expected.
  - p. 31: the rate line reads "$C-\ldots$"; here $C$ is used both as the base of $C^{-\ell_{ij}}$ and as the rate, so the term presumably means $\log C$.
  - p. 55: $\lambda=\lim\frac{\log N}{T\log\epsilon}$. For small $\epsilon$, $\log\epsilon<0$, so as printed the value looks negative; yet the text says the definition agrees with the intuitive dimension rate ($2W$ numbers per second in the band-limited case). Not corrected.
  - p. 50–51: the Lagrange multiplier is printed as $\mu$ in the variational expression and $\lambda$ in the resulting $P_y(x)$.
  - p. 34: "(see Appendix 5" has no closing parenthesis; p. 44: "in in" duplicated.
- The printed text writes $\log$ without a base; natural logarithms are implicit where $e$ appears (e.g. $\log\sqrt e=\tfrac12$), and base 2 gives bits (p. 42).
