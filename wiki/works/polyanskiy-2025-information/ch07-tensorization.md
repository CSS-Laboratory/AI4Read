---
id: polyanskiy-2025-information/ch07-tensorization
work: polyanskiy-2025-information
unit: "Chapter 6 (listed as ch07 in the metadata): Tensorization and information rates"
pages: 106-114
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Tensorization and information rates

## L0 — One line
For memoryless channels and sources, the mutual information of long vectors is bounded by (channel) or bounds (source) the sum of single-letter terms (tensorization), and entropy and mutual information are extended to processes as per-symbol rates, which exist for stationary processes in the entropy case.

## L1 — The gist (≤ 120 words)
How can one optimise mutual information between long vectors without searching a huge space? For a memoryless channel, I(Xⁿ;Yⁿ) is at most the sum of the single-letter terms, and the sum is attained exactly when the outputs are independent. For a memoryless source the inequality reverses. This reduces n-dimensional problems to scalar ones, and symmetry can re-derive the Gaussian optimum. The chapter then defines entropy rate and mutual information rate. For stationary processes the entropy rate exists and is approached from above. For hidden Markov models it can be sandwiched from both sides. Processes that can be coupled with few symbol errors have close entropy rates. The mutual information rate of Gaussian processes is given by their spectral densities.

**Prerequisites:** mutual information, conditional entropy and chain rule; KL divergence; concavity and Jensen's inequality; Fano's inequality; Gaussian covariance matrices and determinants; Markov chains.

## L2 — Key ideas
- Memoryless channel: I(Xⁿ;Yⁿ) ≤ ΣI(Xᵢ;Yᵢ), with equality iff the output has independent components. The unconstrained capacity is therefore additive (p. 106).
- Memoryless source: I(Xⁿ;Y) ≥ ΣI(Xᵢ;Y). The minimising channel can be taken to be a product channel (pp. 106–107).
- Gaussian optimality can be derived by averaging over rotations, without explicit calculations (p. 108).
- For stationary processes the entropy rate exists. Both (1/n)H(Xⁿ) and H(Xₙ|Xⁿ⁻¹) decrease to it, so finite-n values give only upper bounds (pp. 109–110).
- For hidden Markov models, H(Xₙ|X₁ⁿ⁻¹,S₀) ≤ H(𝕏) ≤ H(Xₙ|X₁ⁿ⁻¹), and both bounds converge monotonically (p. 111).
- Fano's inequality tensorizes; for a finite alphabet and per-symbol error probability at most ε, the entropy rates differ by at most F_M(1−ε) (pp. 112–113).
- For independent stationary Gaussian processes, the mutual information rate I(𝕏;𝕏+ℕ) is an integral over their spectral densities (p. 114).

## L3 — Walkthrough

The chapter introduces tensorization (single-letterization), then entropy rate and mutual information rate. The author notes that the Ornstein-distance result is used later for ergodicity (Section 12.5*) and the Gaussian rate formula for colored-noise channels (Section 20.6*) (p. 106).

### 6.1 Tensorization of mutual information
**Theorem 6.1 (p. 106–107).**
(a) If the channel is memoryless, $P_{Y^n|X^n}=\prod P_{Y_i|X_i}$, then
$$I(X^n;Y^n)\le\sum_{i=1}^n I(X_i;Y_i)\tag{6.1}$$
with equality iff $P_{Y^n}=\prod P_{Y_i}$. Consequently the (unconstrained) capacity is additive for memoryless channels: $\max_{P_{X^n}} I(X^n;Y^n)=\sum_i \max_{P_{X_i}} I(X_i;Y_i)$.

(b) If the source is memoryless, $X_1\perp\!\!\!\perp\dots\perp\!\!\!\perp X_n$, then
$$I(X^n;Y)\ge\sum_{i=1}^n I(X_i;Y)\tag{6.2}$$
with equality iff $P_{X^n|Y}=\prod P_{X_i|Y}$, $P_Y$-a.s. Consequently $\min_{P_{Y^n|X^n}} I(X^n;Y^n)=\sum_i\min_{P_{Y_i|X_i}} I(X_i;Y_i)$.

*Proof.* (1) $I(X^n;Y^n)-\sum I(X_i;Y_i)=D(P_{Y^n|X^n}\|\prod P_{Y_i|X_i}|P_{X^n})-D(P_{Y^n}\|\prod P_{Y_i})$. (2) Swap the roles of X and Y: $I(X^n;Y)-\sum I(X_i;Y)=D(P_{X^n|Y}\|\prod P_{X_i|Y}|P_Y)-D(P_{X^n}\|\prod P_{X_i})$ (p. 107).
(added step) In (a) the first divergence is 0 for a product channel; in (b) the second is 0 for a product source. Non-negativity of the other divergence gives the sign and the equality case.

Consequences (p. 107): for a product channel, the input maximizing the mutual information is a product distribution. For a product source, the channel minimizing the mutual information is a product channel. This is *single-letterization*. For binary vectors it replaces optimisation over $2^n$-dimensional vectors and $2^n\times2^n$ matrices by scalar problems. The effect when quantities extend additively to tensor powers is called *tensorization*; the author gives a log-Sobolev inequality (Exercise I.65) as a famous example, and says the first part of the theorem shows that capacity tensorizes (p. 107).

**Example 6.1 (p. 107).**
- (6.1) fails for non-product channels. Take $X_1,X_2$ iid Ber(1/2), $Y_1=X_1+X_2$ (binary addition), $Y_2=X_1$. Then $I(X_1;Y_1)=I(X_2;Y_2)=0$ but $I(X^2;Y^2)=2$ bits.
- (6.1) can be strict: $Y_k=X_k=U\sim$ Ber(1/2). Then $I(X^n;Y^n)=1$ bit $<n=\sum I(X_k;Y_k)$.
- (6.2) can be strict: independent $X_i$, and $Y_1=X_2,\dots,Y_n=X_1$. Then each $I(X_k;Y_k)=0$ but $I(X^n;Y^n)=\sum H(X_i)>0$.

*Intuition note.* Independent inputs through independent channels carry information separately. Correlation between the inputs cannot push the total above the sum of the single-letter terms.

### 6.2* Gaussian capacity via orthogonal symmetry
Known (Theorem 5.11): $\max_{E[X^2]\le\sigma_X^2} I(X;X+Z)=\tfrac12\log(1+\sigma_X^2)$ for $Z\sim\mathcal N(0,1)$. Tensorization gives $\tfrac n2\log(1+\sigma_X^2)$ for $Z^n\sim\mathcal N(0,I_n)$ with $E\|X^n\|^2\le n\sigma_X^2$ (p. 108). The section solves the n-dimensional problem directly (p. 108):
1. By 6.1(a), $\max I(X^n;X^n+Z^n)=\max\sum_k I(X_k;X_k+Z_k)$ under $E\sum X_k^2\le n\sigma_X^2$.
2. Form $\bar P_X=\frac1n\sum_k P_{X_k}$. It satisfies the single-letter constraint $E[X^2]\le\sigma_X^2$. By concavity of $I$ in $P_X$, $I(\bar P_X;P_{Y|X})\ge\frac1n\sum_k I(P_{X_k},P_{Y|X})$. So the maximum ought to grow linearly in $n$: it equals $n\max_{P_X}I(X;X+Z)$.
3. For orthogonal $U\in O(n)$, $UZ^n\sim\mathcal N(0,I_n)$, so $I(P_{X^n},P_{Y^n|X^n})=I(P_{UX^n},P_{Y^n|X^n})$. Averaging over rotations can only increase $I$, so an optimal input can be chosen rotation-invariant.
4. By Theorem 5.9 the unique capacity-achieving output $P^*_{Y^n}$ is then rotation-invariant. By the equality case of (6.1) it has independent components. The only such distribution meeting the power constraint is isotropic Gaussian, so $P_Y^*=\mathcal N(0,1+\sigma_X^2)$.
5. The only $P_X$ with $P_{X+Z}=P_Y^*$ is $\mathcal N(0,\sigma_X^2)$ (argued with characteristic functions) (pp. 108–109).

The minimisation $\min_{P_N:E[N^2]=1}I(X_G;X_G+N)$ can be handled similarly, to show the minimiser is necessarily Gaussian (p. 109). The author says the idea of "going up in dimension" is from [333], only re-derives Theorem 5.11, but can also be employed for various non-convex differential entropy maximization problems [184] (p. 109).

*Intuition note.* Going up in dimension gives symmetry for free. Symmetry plus independence of components pins the optimal output distribution to the Gaussian.

### 6.3 Entropy rate
**Definition 6.2.** $H(\mathbb X)\triangleq\lim_{n\to\infty}\frac1nH(X^n)$, provided the limit exists (6.3). Stationarity is sufficient for existence: $(X_{t_1},\dots,X_{t_n})\overset d=(X_{t_1+k},\dots,X_{t_n+k})$ (p. 109).

**Theorem 6.3 (stationary $\mathbb X$) (p. 109).**
(a) $H(X_n|X^{n-1})\le H(X_{n-1}|X^{n-2})$. (b) $\frac1nH(X^n)\ge H(X_n|X^{n-1})$. (c) $\frac1nH(X^n)\le\frac1{n-1}H(X^{n-1})$. (d) $H(\mathbb X)$ exists and equals $\lim\frac1nH(X^n)=\lim H(X_n|X^{n-1})$, both converging from above. (e) If $\mathbb X$ extends to a two-sided stationary process and $H(X_1)<\infty$, then $H(\mathbb X)=H(X_1|X_{-\infty}^0)$.

*Proof (pp. 109–110).*
(a) More conditioning plus stationarity: $H(X_n|X^{n-1})\le H(X_n|X_2^{n-1})=H(X_{n-1}|X^{n-2})$.
(b) Chain rule: $\frac1nH(X^n)=\frac1n\sum H(X_i|X^{i-1})\ge H(X_n|X^{n-1})$ by (a).
(c) $H(X^n)=H(X^{n-1})+H(X_n|X^{n-1})\le H(X^{n-1})+\frac1nH(X^n)$ (by (b)); rearranging gives (c) (added step).
(d) By (c) the sequence decreases and is bounded below by 0, so it has a limit. By (a), $H(X_n|X^{n-1})\to H'$. The chain rule writes $\frac1nH(X^n)$ as a Cesàro mean of these terms, so $H'=H(\mathbb X)$.
(e) By (4.30), $H(X_1)-H(X_1|X_{-n}^0)=I(X_1;X_{-n}^0)\to I(X_1;X_{-\infty}^0)=H(X_1)-H(X_1|X_{-\infty}^0)$.

**Example 6.2 (p. 110).**
(a) iid: $H(\mathbb X)=H(X_1)$.
(b) Mixed source: flip a coin with bias $p$; set $\mathbb X=\mathbb Y$ on heads and $\mathbb Z$ on tails. Theorem 3.4(b) gives $0\le H(X^n)-(pH(Y^n)+\bar pH(Z^n))\le\log2$, so $H(\mathbb X)=pH(\mathbb Y)+\bar pH(\mathbb Z)$.
(c) Stationary Markov chain with kernel $K$ and invariant start $\mu$: $H(\mathbb X)=H(X_2|X_1)=\sum_{a,b}\mu(a)K(b|a)\log\frac1{K(b|a)}$. A $k$-th order Markov process has kernel $P_{X_n|X_{n-k}^{n-1}}$. The author says Shannon suggested these as models of language (large $k$), and that recent large language models largely verified this.

Both sequences converge from above, so finite $n$ gives only an upper bound on $H(\mathbb X)$; one cannot even rule out $H(\mathbb X)=0$ (p. 110).

**Definition 6.4 (HMM, p. 110).** A stationary Markov chain $\dots,S_0,S_1,\dots$ on $\mathcal S$ is observed through a stationary memoryless emission channel: given $S^\infty_{-\infty}$, each $X_i\sim P_{X|S=S_i}$ independently.

**Blackwell (p. 111).** The belief process $R_{s,n}=P[S_n=s|X_{-\infty}^{n-1}]$ is a stationary first-order Markov process. Its common law $\mu$ is the *Blackwell measure*, and
$H(\mathbb X)=\int_{\mathcal P(\mathcal S)}\mu(d\mathbf r)\,E_{s\sim\mathbf r}[H(P_{X|S=s})]$.

**Example 6.3 (Gilbert–Elliott, p. 111).** $\mathcal S=\{0,1\}$, $P[S_1\ne S_0|S_0]=\tau$, $X_i=\mathrm{BSC}_\delta(S_i)$. Then $\mu$ is supported on $[\tau,1-\tau]$ and is the law of $P[S_1=1|X_{-\infty}^0]$. The entropy rate is $H(\mathbb X)=\int_0^1\mu(dx)\,h(\delta\bar x+\bar\delta x)$, with $\bar x=1-x$. Also $\int f\,d\mu=\lim_n K^nf(1/2)$, where
$$Kg(x)=p(x)\,g\!\Big(\tfrac{x\bar\tau\bar\delta+\bar x\tau\delta}{p(x)}\Big)+\bar p(x)\,g\!\Big(\tfrac{x\bar\tau\delta+\bar x\tau\bar\delta}{\bar p(x)}\Big),\quad p(x)=1-\bar p(x)=\delta\bar x+\bar\delta x.$$
The updates are fractional-linear, yet $\mu$ is extremely complicated: it can be either absolutely continuous or singular (fractal-like). Understanding $H(\mathbb X)$ as a function of $(\tau,\delta)$ is a major open problem. With a BEC instead of a BSC the rate is much easier to compute (Exercise I.32).

**Proposition 6.5 (p. 111–112).** For an HMM,
$$H(X_n|X_1^{n-1},S_0)\le H(\mathbb X)\le H(X_n|X_1^{n-1}),\tag{6.4}$$
and both sides converge monotonically to $H(\mathbb X)$.

*Proof.* The upper bound is from 6.3. Lower bound: $H(\mathbb X)=H(X_n|X_{-\infty}^{n-1})\ge H(X_n|X_{-\infty}^{n-1},S_0)=H(X_n|X_1^{n-1},S_0)$, using the Markov property $X_{-\infty}^0\to S_0\to X_1^n$. Monotone: $H(X_{n+1}|X_1^n,S_0)=H(X_n|X_0^{n-1},S_{-1})\ge H(X_n|X_0^{n-1},S_{-1},S_0)=H(X_n|X_1^{n-1},S_0)$ (stationarity; more conditioning; Markov property $(S_{-1},X_0)\to S_0\to X_1^n$). Limit: by (4.30), $I(S_0;X_1^\infty)=\lim I(S_0;X_1^n)\le H(S_0)<\infty$, so $I(S_0;X_1^n)-I(S_0;X_1^{n-1})\to0$. By the chain rule this difference is $H(X_n|X_1^{n-1})-H(X_n|X_1^{n-1},S_0)$, so the gap in (6.4) vanishes.

*Intuition note.* Knowing the hidden state can only lower uncertainty, giving a lower bound. Adding more past observations tightens both bounds toward the same value.

### 6.4 Entropy and symbol (bit) error rate
Coupling means defining two processes on one probability space. Symbol error rate: $\frac1n\sum_j P[X_j\ne Y_j]\le\epsilon$ (6.5). The minimal such $\epsilon$ over couplings is *Ornstein's distance*. With Hamming distance $d_H(x^n,y^n)=\sum_j1\{x_j\ne y_j\}$ (6.6), this is $E[d_H(X^n,Y^n)]\le n\epsilon$ (p. 112).

**Proposition 6.6 (tensorized Fano).** For $X_i$ on a finite alphabet,
$$H(X^n|Y^n)\le nF_{|\mathcal X|}(1-\delta)=n(\delta\log(|\mathcal X|-1)+h(\delta)),\tag{6.7}$$
where $F_M$ is defined in (3.14) and $\delta=\frac1nE[d_H(X^n,Y^n)]=\frac1n\sum_jP[X_j\ne Y_j]$ (pp. 112–113).

*Proof (p. 113).* Apply (3.18) to the Markov chain $X_j\to Y^n\to Y_j$: $H(X_j|Y^n)\le F_M(P[X_j=Y_j])$ (6.8). Then $H(X^n|Y^n)\le\sum_jH(X_j|Y^n)$ (6.9) $\le\sum_jF_M(P[X_j=Y_j])$ (6.10) $\le nF_M\big(\frac1n\sum_jP[X_j=Y_j]\big)$ (6.11), by concavity of $F_M$ and Jensen.

**Corollary 6.7 (p. 113).** For two processes with entropy rates $H(\mathbb X)$ and $H(\mathbb Y)$: if $P[X_j\ne Y_j]\le\epsilon$ for every $j$ and $\mathbb X$ has alphabet size $M$, then $H(\mathbb X)-H(\mathbb Y)\le F_M(1-\epsilon)$. If both have alphabet size $M$, then $|H(\mathbb X)-H(\mathbb Y)|\le\epsilon\log M+h(\epsilon)\to0$ as $\epsilon\to0$. Proof: $H(X^n)\le H(X^n,Y^n)=H(Y^n)+H(X^n|Y^n)$, then apply (6.7); for the last statement recall the expression for $F_M$.

*Intuition note.* If two processes can be coupled to differ rarely, their per-symbol uncertainty must be nearly equal. Fano converts "rarely different" into "little leftover uncertainty".

### 6.5 Mutual information rate
**Definition 6.8.** $I(\mathbb X;\mathbb Y)=\lim_n\frac1nI(X^n;Y^n)$, provided the limit exists (p. 114).

**Example 6.4 (p. 114).** Let $\mathbb X,\mathbb N$ be independent stationary zero-mean Gaussian processes with absolutely summable autocovariances $c_X$, $c_N$ (so continuous spectral densities exist), $c_X(k)=E[X_1X_{k+1}]$, and $f_X(\omega)=\sum_kc_X(k)e^{i\omega k}$, $|\omega|\le\pi$. Assume $f_N\ge\delta>0$. From Example 3.5 (all matrices $n\times n$, Toeplitz):
$$I(X^n;X^n+N^n)=\tfrac12\log\frac{\det(\Sigma_{X^n}+\Sigma_{N^n})}{\det\Sigma_{N^n}}=\tfrac12\sum_{i=1}^n\log\sigma_i-\tfrac12\sum_{i=1}^n\log\lambda_i,$$
with $\sigma_i$, $\lambda_i$ the eigenvalues of $\Sigma_{Y^n}=\Sigma_{X^n}+\Sigma_{N^n}$ and $\Sigma_{N^n}$. Szegő's theorem gives
$$\tfrac1n\sum_i\log\sigma_i\to\tfrac1{2\pi}\int_{-\pi}^\pi\log f_Y(\omega)\,d\omega.\tag{6.12}$$
Since $c_Y=c_X+c_N$, $f_Y=f_X+f_N$. Applying Szegő also to the $\lambda_i$ (added step), the author's result is
$$\tfrac1nI(X^n;X^n+N^n)\to I(\mathbb X;\mathbb X+\mathbb N)=\tfrac1{4\pi}\int_{-\pi}^\pi\log\frac{f_X(\omega)+f_N(\omega)}{f_N(\omega)}\,d\omega.$$
Maximising over $f_X$ under a moment constraint gives the water-filling solution $f_X^*(\omega)=|T-f_N(\omega)|_+$ (Theorem 20.18) (p. 114).

*Intuition note.* Spectral density says how much "power" a process has at each frequency. The information rate integrates, over frequencies, the log of (signal plus noise power) divided by noise power, i.e. $\log(1+\text{signal-to-noise ratio})$ at each frequency.

## Toy example (ours)
Binary erasure channel, each use erases its input with probability 1/2, used twice ($n=2$): a memoryless channel.
- Product input, $X_1,X_2$ iid Ber(1/2): $H(X^2)=2$. Given $Y^2$, the uncertainty is the number of erased letters, on average 1. So $I(X^2;Y^2)=2-1=1$. Per letter, $I(X_i;Y_i)=1-\tfrac12=\tfrac12$, so the sum is 1. This is equality in (6.1).
- Correlated input $X_1=X_2=U$ fair: $H(X^2)=1$. Uncertainty remains only if both are erased (probability $\tfrac14$), then it is 1 bit. So $I(X^2;Y^2)=1-\tfrac14=\tfrac34$. Marginally each $X_i$ is still fair, so $\sum I(X_i;Y_i)=\tfrac12+\tfrac12=1$. Thus $\tfrac34<1$, strict in (6.1).
- Consistency with the equality case, for the correlated input: $P(Y_1=0,Y_2=0)=\tfrac12\cdot\tfrac14=\tfrac18$, while $P(Y_1=0)P(Y_2=0)=\tfrac14\cdot\tfrac14=\tfrac1{16}$. The outputs are dependent, so equality fails, as the theorem says.

## Concepts
- [[tensorization]] (new) — a quantity that extends additively to tensor powers (products); for mutual information, Theorem 6.1 gives the sum as a bound, with equality conditions (p. 107)
- [[single-letterization]] (new) — reducing a multi-letter optimisation to a one-letter one (p. 107)
- [[mutual-information]] — I(X;Y), here optimised over high-dimensional inputs and channels (p. 106)
- [[channel-capacity]] — max over inputs of mutual information; the unconstrained capacity is additive for memoryless channels (p. 106)
- [[chain-rule]] — used to turn $H(X^n)$ into a sum of conditional entropies (p. 109)
- [[entropy-rate]] — $\lim\frac1nH(X^n)$, when the limit exists (p. 109)
- [[stationary-process]] (new) — finite-dimensional laws invariant under time shifts (p. 109)
- [[hidden-markov-model]] (new) — Markov state process observed through a memoryless emission channel (p. 110)
- [[blackwell-measure]] (new) — law of the belief process $P[S_n=s|X_{-\infty}^{n-1}]$ of an HMM (p. 111)
- [[ornstein-distance]] (new) — minimal symbol error rate over couplings of two processes (p. 112)
- [[fanos-inequality]] — here tensorized to vectors (p. 112)
- [[mutual-information-rate]] (new) — $\lim\frac1nI(X^n;Y^n)$, provided the limit exists (p. 114)
- [[water-filling]] (new) — optimal spectral allocation $f_X^*=|T-f_N|_+$, only quoted here (p. 114)

## Canonical instances
- [[product-channel-counterexamples]] — Example 6.1: (6.1) fails for a non-product channel and can be strict; (6.2) can be strict (p. 107)
- [[gaussian-capacity-by-symmetry]] — rotation averaging forces Gaussian optimum (p. 108)
- [[gilbert-elliott-hmm]] — binary-state HMM with BSC emissions; entropy rate via a Blackwell measure that can be fractal-like (p. 111)
- [[gaussian-process-information-rate]] — Szegő-based formula, Example 6.4 (p. 114)

## Bridges (candidates)
- [structural-analogy] Additivity of capacity for memoryless channels ↔ information-theory: other per-letter optimisation arguments — both reduce a multi-letter problem to a single-letter one.
- [structural-analogy] Averaging over rotations to prove Gaussian extremality ↔ statistics: symmetry/invariance arguments for minimax or maximum-entropy solutions.
- [structural-analogy] Shannon's k-th order Markov language model (p. 110) ↔ language modelling: n-gram and neural language models.
- [same-math] Spectral-density formula for the information rate ↔ signal processing: log-determinant of Toeplitz covariances and Szegő's theorem.

## Questions this raises
- When the channel is not memoryless, what replaces tensorization for capacity?
- Since entropy estimates from finite $n$ are only upper bounds, how can one estimate the entropy rate of natural language reliably?
- How does the water-filling solution arise from the Gaussian-process rate formula (Theorem 20.18)?
- What other optimisation problems admit "going up in dimension" tricks (the author cites non-convex differential entropy problems, p. 109)?

## Reading notes
- The metadata names this unit ch07; the printed chapter is **Chapter 6**, sections 6.1–6.5. Printed = pdf − 25.
- The source contains no exercises, only pointers to Exercises I.31, I.32 and I.65.
- Example 6.2(b): the page shows $pH(Y^n)+\bar pH(Y^n)$ for the mixture; presumably the second term should be $H(Z^n)$. The next sentence, $H(\mathbb X)=pH(\mathbb Y)+\bar pH(\mathbb Z)$, supports this.
- The text layer of Example 6.1 and of the Markov example garbles some symbols. The images give $I(X^2;Y^2)=2$ bits and $H(X_n|X^{n-1})=H(X_n|X_{n-1})$.
- $F_M$ is defined in (3.14), outside these pages.
