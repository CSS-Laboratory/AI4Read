---
id: stone-2022-information/ch08-rate
work: stone-2022-information
unit: 8 Rate Distortion Theory
pages: 173-194
fields: [information-theory]
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
# Rate Distortion Theory

## L0 — One line
If some distortion D is tolerated, the minimum number of bits per element needed to represent a source is the rate distortion function R(D), the smallest mutual information I(X; X̂) over encodings that meet D.

## L1 — The gist (≤ 120 words)
Ordinary information theory assumes the channel capacity is enough (in principle) to send a source without error. This chapter asks what happens if we allow fewer bits than the source entropy. Answer: low distortion needs a high rate, and a low rate forces high distortion. The rate distortion function R(D) gives the lowest rate for each distortion level. It equals the minimum of I(X; X̂) over conditional distributions p(x̂|x) with expected distortion ≤ D. The chapter gives closed forms for binary and Gaussian sources, shows that stochastic encoding beats one-bit quantisation, and works through an image example. It then reviews applications: reaction-time trade-offs, perception, evolution, and bacterial gradient climbing.

**Prerequisites:** entropy; mutual information; conditional entropy; Gaussian variance; the noisy-channel coding theorem; correlation.

## L2 — Key ideas (5–10 bullets)
- Representing a signal cheaply with high fidelity is impossible; information is the "currency" paid for fidelity (p. 173).
- Equivocation $E=H(X|\hat X)$ obeys $H(X|\hat X)\ge H(X)-C$. The text's rate equivocation function $R(E)=H(X)-E$ is a straight line of slope −1 (pp. 174–175).
- R(D) is the smallest rate for which (R, D) is achievable. The rate distortion theorem says $R(D)=R^I(D)=\min I(X;\hat X)$ over $p(\hat x|x)$ with $E[d]\le D$ (pp. 179–180).
- Binary source, Hamming distortion: $R(D)=H(p)-H(D)$ for $D\le\min\{p,1-p\}$, else 0 (p. 181).
- Gaussian source, squared error: $R(D)=\tfrac12\log(\sigma^2/D)$, so $D(R)=\sigma^2/2^{2R}$ and each extra bit cuts distortion by a factor of 4 (pp. 182–183).
- At R = 1 bit, a deterministic two-level quantiser gives D ≈ 0.36σ². A stochastic encoding $\hat x=(1-D/\sigma^2)x+\eta$ reaches the bound 0.25σ² (pp. 184–186).
- In the 64→4 grey-level image example, R = 1.933 bits against a Gaussian-ideal 1.810 bits at the same D (pp. 186–189).
- The theory is applied to human speed–accuracy trade-offs, perceptual generalisation, evolution, and bacterial gradient climbing (pp. 190–194).

## L3 — Walkthrough

### 8.1 Introduction (pp. 173–176)
- Setting: the input is an iid vector $\mathbf X=(X_1,\dots,X_n)$ with $H(\mathbf X)=nH(X)$ (Eq. 8.1), and the output is $\hat{\mathbf X}$ (Eq. 8.2). Error-free transmission needs rate $R=H(X)$ bits/element, so $C\ge R$ (p. 173).
- If distortion D is tolerated, the rate and capacity can be below H(X). Uncertainty about X given X̂ is measured by the **equivocation** $E=H(X|\hat X)$ (p. 174).
- The noisy channel coding theorem gives the lower bound
$$H(X|\hat X)\ \ge\ H(X)-C \text{ bits},\tag{8.3}$$
  with C equal to a particular rate R (p. 174). Shannon (1949), quoted: transmitting at C + E forces equivocation of at least E; "Nature takes payment by requiring just that much uncertainty" (p. 174).
- Notation: "R ≈ C" abbreviates "R → C as n → ∞" (p. 174).
- **Rate equivocation function** (the author says it is unique to this text): the smallest rate needed for a given E.
$$R(E)=H(X)-H(X|\hat X)\tag{8.4}$$
$$\phantom{R(E)}=H(X)-E\text{ bits}\tag{8.5}$$
  It is linear with slope −1 (Fig. 8.1, p. 175).
- Rate distortion theory is usually stated with distortion D. The text says there is a one-to-one mapping between distortion and equivocation, so either can be used (p. 175).
- R(D) is the smallest rate for distortion D (example: mean squared error $E[(X-\hat X)^2]$, Fig. 8.2). The **distortion rate function** D(R) is the smallest D for a given R (p. 176).
- **Key point:** the theory specifies the smallest rate needed to recover the input with distortion no greater than D (p. 176).

*Intuition note.* Every bit you refuse to send leaves at least one bit of doubt about the input. Fidelity can only be bought with information.

### 8.2 Informal summary (pp. 176–177)
- The question: given n iid variables with entropy nH(X), how accurately can X be represented as X̂? Accuracy has two parameters: rate R (average bits per element) and expected distortion D (p. 176).
- Low distortion at high rate, or high distortion at low rate, but never low distortion at low rate. This gives two lower limits, R(D) and D(R) (pp. 176–177).

### 8.3 Rate distortion theory (pp. 177–181)
- **Ordinary information theory.** A message s is encoded as $\mathbf x=(x_1,\dots,x_n)$ (Eq. 8.6), e.g. by Huffman coding. Simplifying assumption: $nH(X)=H(S)$ exactly, with $m=2^n$ possible vectors $\mathbf x\in\{\mathbf x_1,\dots,\mathbf x_m\}$ (Eq. 8.7). Source coding guarantees error-free reception if capacity suffices. The new question: what if H(X) exceeds capacity, i.e. we allocate fewer than H(X) bits per element? (p. 177)
- **Framework (Fig. 8.3).** A lossy x-encoder maps $w=f_n(\mathbf x)$ (Eq. 8.8). The codeword has entropy H(W), so
$$R=H(W)/n\text{ bits}\tag{8.9}$$
  The number of codewords is $\hat m=2^{nR}$, $w\in\{1,\dots,\hat m\}$ (Eq. 8.10), with $\hat m<m$ if $R<H(X)$. A w-decoder gives $\hat{\mathbf x}=g_n(w)$ (Eq. 8.11), so $\hat{\mathbf x}=g_n(f_n(\mathbf x))$ (Eq. 8.12). Typically $\hat m<m$, so each output corresponds to more than one input (pp. 178–179).
- A **rate distortion code** $(f_n,g_n)$, written $(2^{nR},n)$, has an encoding function, a decoding function and a distortion D (p. 179).
- Per-element distortion measure d. Vector distortion and the squared-error case:
$$d(\mathbf x,\hat{\mathbf x})=\frac1n\sum_{i=1}^n d(x_i,\hat x_i)\tag{8.13}$$
$$d(\mathbf x,\hat{\mathbf x})=\frac1n\sum_{i=1}^n (x_i-\hat x_i)^2\tag{8.14}$$
  Mean distortion over all vectors:
$$D=\sum_{j=1}^m p(\mathbf x_j)\,d(\mathbf x_j,\hat{\mathbf x}_j)\tag{8.15}$$
- A pair (R, D) is **achievable** for source p(x) and measure d if a code exists that yields it. R(D) is the smallest R at each D such that (R, D) is achievable. This is often stated with the infimum of rates; Shannon proved the two statements equivalent here (pp. 179–180).
- In practice R(D) and D(R) are obtained with the Blahut–Arimoto algorithm, which the book does not cover (p. 180).
- **Information rate distortion function:**
$$R^I(D)=\min_{p(\hat x|x):\,E[d(x,\hat x)]\le D} I(X;\hat X)\text{ bits}\tag{8.16}$$
$$E[d(x,\hat x)]=\sum_x\sum_{\hat x}p(\hat x|x)\,p(x)\,d(x,\hat x)\tag{8.17}$$
  In words: pick the p(x̂|x) with the smallest mutual information among those with expected distortion ≤ D (p. 180).
- **Theorem (rate distortion):**
$$R(D)=R^I(D)\text{ bits}\tag{8.18}$$
  Roughly, the information needed about X to get X̂ with distortion D must be at least I(X; X̂). The source coding theorem is the special case of zero distortion. The **converse** states that distortion below D is not achievable if R < R(D). Proofs are in the references (pp. 180–181).
- **Why minimise over p(x̂|x)?** Since $p(x,\hat x)=p(\hat x|x)p(x)$ and p(x) is fixed, varying the joint (Eq. 8.19) is the same as varying the conditional (Eq. 8.16) (p. 181).

*Intuition note.* Among all ways of corrupting X into X̂ that stay within the distortion budget, choose the one that leaves X̂ knowing as little about X as possible. That minimum mutual information is the bit cost.

### 8.4 The binary rate distortion function (p. 181)
- For a binary vector with P(element = 1) = p, Hamming distortion ($d=0$ if $x=\hat x$, else 1; Eq. 8.20) and $D=E[d(X,\hat X)]$, "it can be shown" that
$$R(D)=\begin{cases}H(p)-H(D)\text{ bits}&0\le D\le\min\{p,1-p\}\\ 0\text{ bits}&D>\min\{p,1-p\}\end{cases}\tag{8.21}$$
- Fig. 8.4 shows p = 0.5. R(0) = 1 bit, as expected for a noiseless binary variable (p. 181).

### 8.5 The Gaussian rate distortion function (pp. 182–184)
- For $x\sim\mathcal N(0,\sigma^2)$ and squared error (Eqs. 8.22–8.23, $D=E[d(\mathbf X,\hat{\mathbf X})]$), "it can be shown" that
$$R(D)=\begin{cases}\tfrac12\log\frac{\sigma^2}{D}&0\le D\le\sigma^2\\0&D>\sigma^2\end{cases}\tag{8.24}$$
  With σ² = 1, $R=\tfrac12\log(1/D)$ (Fig. 8.5). R → ∞ as D → 0, since the exact value of a real variable carries infinite information (p. 182).
- The pairs defined by R(D) are achievable only if X and X̂ (hence X − X̂) are Gaussian (p. 183).
- Rearranging gives
$$D(R)=\sigma^2/2^{2R}\tag{8.25}$$
  Each extra bit divides the mean distortion by $2^2=4$. With R = 1 bit, the smallest mean squared error is $0.25\sigma^2$ (p. 183).
- **Inverse channel.** Write $\mathbf X=\hat{\mathbf X}+\eta$ (Eq. 8.26), with compression noise $\eta=\mathbf X-\hat{\mathbf X}$. If $x\sim\mathcal N(0,P+N)$ and $\hat x\sim\mathcal N(0,P)$, then
$$I(X,\hat X)=\tfrac12\log\frac{P+N}{N}\tag{8.27}$$
  with $N=\mathrm{var}(X-\hat X)=D$. Since $R=I=\tfrac12\log\frac{\sigma^2}{D}$,
$$\tfrac12\log\frac{\sigma^2}{D}=\tfrac12\log\frac{P+N}{N}\tag{8.28}$$
  where $\sigma^2=P+N$ is the output variance and N = D is the variance of the compression noise (pp. 183–184).

*Intuition note.* Compression behaves like a noisy channel whose noise power equals the distortion. Rate then depends on the signal-to-noise ratio, as in a Gaussian channel.

### 8.6 Deterministic versus stochastic encoding (pp. 184–186)
- **Deterministic, R = 1 bit** (single Gaussian scalar). "It can be shown" the best two-level quantiser is
$$\hat X=\begin{cases}\sigma\sqrt{2/\pi}\approx0.8\sigma&x\ge0\\-\sigma\sqrt{2/\pi}\approx-0.8\sigma&x<0\end{cases}\tag{8.29}$$
  with mean distortion
$$D=(1-2/\pi)\sigma^2\approx0.36\sigma^2\tag{8.30}$$
  This exceeds the theoretical minimum $0.25\sigma^2$ at R = 1 (p. 184).
- **Stochastic encoding** can reach the R(D) bound even for n = 1. Use $\hat x=kx+\eta$ (Eq. 8.31) with $x\sim\mathcal N(0,\sigma^2)$, so X, X̂ and X − X̂ are Gaussian (pp. 184–185).
- With correlation ρ between X and X̂ (from Eq. 7.45), $R(\rho)=\tfrac12\log\frac1{1-\rho^2}$ (8.32). Also $R(D)=\tfrac12\log\frac{\sigma^2}{D}$ (8.33). Setting $R(\rho)=R(D)$ and solving gives
$$\rho_D^2=1-D/\sigma^2\tag{8.34}$$
  (added step: $\frac1{1-\rho^2}=\frac{\sigma^2}{D}$ gives $1-\rho^2=D/\sigma^2$.) Hence
$$R(\rho_D)=\tfrac12\log\frac1{1-\rho_D^2}\text{ bits},\qquad D(\rho_D)=\sigma^2(1-\rho_D^2)\tag{8.35, 8.36}$$
  The correlation (Eq. 8.37) depends only on p(X̂|X), because p(X) is fixed. The task is to find the p(X̂|X) giving the optimal pair (p. 185).
- "Without going into details," the optimal encoding is
$$\hat X\sim\mathcal N\big(x(1-D/\sigma^2),\ D(1-D/\sigma^2)\big)\tag{8.38}$$
  So Eq. 8.31 becomes
$$\hat x=(1-D/\sigma^2)x+\eta,\quad \eta\sim\mathcal N\big(0,D(1-D/\sigma^2)\big)\tag{8.39}$$
  With D = 0.25σ², this distortion is achieved with R = 1 bit, better than the deterministic 0.36σ². As n → ∞, the measured average distortion approaches 0.25σ² (p. 186).

*Intuition note.* Adding noise on purpose, with a gain below 1, gives a one-bit description that is closer on average to the original than hard thresholding. Hard thresholding is the best deterministic two-level rule, yet still falls short of the bound at n = 1.

### 8.7 Image compression example (pp. 186–189)
- Picture with 64 grey-levels, assumed iid. $H(x)=5.845$ bits (8.40); grey-level variance σ² = 258 (p. 186).
- Quantise into 4 levels: levels 1–16 → 8, 17–32 → 24, and similarly for the other two ranges. $H(\hat x)=1.933$ bits (Fig. 8.6). The x → w → x̂ steps of Fig. 8.3 are bypassed (p. 186).
- The mapping is deterministic, so $H(\hat x|x)=0$. Then $R=I(x;\hat x)=H(\hat x)-H(\hat x|x)=H(\hat x)=\sum_{i=1}^4p(\hat x_i)\log\frac1{p(\hat x_i)}=1.933$ bits (8.41–8.43). Distortion = variance of the difference image, $d(\mathbf x,\hat{\mathbf x})=20.97$ (8.44; $H(x-\hat x)=3.996$ bits) (p. 188).
- **Comparison under Gaussian assumptions** (p(x̂), p(x), and the errors Gaussian; expected = measured distortion D = 20.97):
$$R(D)=0.5\log(258/20.97)=1.810\text{ bits}\tag{8.45}$$
$$D(R)=\sigma^2/2^{2R}=258/2^{2\times1.933}=17.69\tag{8.46}$$
  The code's R = 1.933 bits is only a little above 1.810. The measured D = 20.97 is "about 20%" above 17.69 (Fig. 8.7). The near-optimality is unsurprising because the distributions are (loosely) approximately Gaussian (p. 189).
- Naive codes can be reasonably efficient (Shannon). Still, small gains near the Shannon limit can be worth millions of dollars; the Mars Rover sends about 800 bits/s against about 50 million for wifi (p. 189).

### 8.8 Applications (pp. 190–194)
- **Speed–accuracy trade-off** (Soukoreff & MacKenzie 2009; p. 190). They re-analysed published data from 18 participants. Each participant's data was an n × n confusion matrix of entries p(x̂ⱼ|xᵢ), combined with reaction times. They derived a linear relation between information rate R and equivocation E, both in bits/s. The best-fit line was $R=-0.696\,E+8.56$ bits/s. Linearity was confirmed, but the slope −0.696 differs from the predicted −1. This means throughput falls more slowly with equivocation than the theory predicts.
- **Perception** (Sims 2018; pp. 191–192). He analysed nine published experiments. Each point (R, D) on R(D) corresponds to an exponential generalisation curve $G(x,\hat x)=e^{sL(x,\hat x)}$. Here L is an observer-defined loss with $D=E[L]$, and $s=d\log G/dL<0$ (stated as $s=dR/dD$, the slope of R(D) at that point). Pipeline: confusion matrix M → (Bayes) L → (Blahut–Arimoto) $p(\hat x|x)^*$ → $(R^*,D^*,s)$ → G. Shepard's empirical generalisation function is $G_E=\{p(\hat x|x)p(x|\hat x)/[p(\hat x|\hat x)p(x|x)]\}^{1/2}$. Sims found $G_E$ points lie close to the predicted curve across colour, loudness, taste, line length, vocal consonants, vibrotactile patterns and musical timbre. The author says $G_E$ can thus be explained as minimising perceptual error over a finite-capacity channel. Frank (2018) showed the exponential form is a necessary consequence of perceptual invariance.
- **Speculation (author):** perceptual compression might be estimated by splitting confusion-matrix noise into compression noise $\eta_c$ and intrinsic noise $\eta_i$, giving var(x̂)/var(η_c) (p. 192).
- **Evolution** (Marzen & DeDeo 2017). R(D) rises quickly with environmental complexity, then levels off at a D-dependent value. They concluded selection should give "poised perception", i.e. apparatus just adequate for survival (pp. 192–193).
- **Image quality** (Blau & Michaeli 2018). Forcing p(x̂) close to p(x) (e.g. by KL distance) substantially improves perceived quality at the same R (Fig. 8.8: 8 bits/image, D₂ > D₁). Such gains "seem to be unique to stochastic encoders" (p. 193).
- **Bacteria** (Mattingly et al. 2021). *E. coli* climb gradients by changing run durations. A distortion rate function was built with R = information acquired (transfer entropy, bits/s) and the ordinate the theoretical maximum climbing speed D(R). Measured information rates were 0 to 0.04 bits/s depending on gradient steepness (Fig. 8.9). At 0.04 bits/s a bacterium climbs at 24% of its normal speed of 22.6 µm/s (p. 194).

### 8.9 Summary (p. 194)
Information theory assumes capacity suffices (in principle). Rate distortion theory assumes it rarely does, so error must be tolerated. It gives no "free lunch", but it specifies the lowest information price for a given distortion.

## Toy example (ours)
Gaussian source with σ² = 4, one bit (R = 1).
- Bound: $D(1)=4/2^{2}=1$. Check: $R(1)=\tfrac12\log_2(4/1)=1$.
- Deterministic quantiser (8.30): $D=(1-2/\pi)\times4\approx0.3634\times4=1.45$, worse than 1.
- Stochastic (8.39) with D = 1: gain $k=1-D/\sigma^2=0.75$; noise variance $D(1-D/\sigma^2)=0.75$. So $\hat x=0.75x+\eta$.
- Check (added step): $E[(x-\hat x)^2]=\mathrm{var}(0.25x-\eta)=0.0625\times4+0.75=1.0$. Also $\rho^2=\mathrm{cov}^2/(\mathrm{var}\,x\,\mathrm{var}\,\hat x)=3^2/(4\times3)=0.75=1-D/\sigma^2$, which matches (8.34).

## Concepts
- [[rate–distortion function]] — smallest rate R for each distortion D; equals $\min I(X;\hat X)$ over $p(\hat x|x)$ with $E[d]\le D$ (pp. 179–180)
- [[mutual information I(X;Y)]] — the quantity minimised in $R^I(D)$ (p. 180)
- [[joint and conditional entropy]] — equivocation $E=H(X|\hat X)$ used as the uncertainty measure (p. 174)
- [[noisy-channel coding theorem]] — gives the bound $H(X|\hat X)\ge H(X)-C$ (p. 174)
- [[source coding theorem]] — the zero-distortion special case of the rate distortion theorem (p. 180)
- [[channel capacity]] — identified with a rate R in this chapter (p. 174)
- [[transfer entropy]] — information measure used for bacteria in Sec. 8.8 (p. 194)
- [[equivocation]] (new) — $H(X|\hat X)$, uncertainty about input given distorted output (p. 174)
- [[rate-equivocation-function]] (new) — the author's $R(E)=H(X)-E$, a line of slope −1 (p. 175)
- [[distortion-measure]] (new) — per-element cost d(x, x̂), e.g. Hamming or squared error (pp. 179, 181)
- [[stochastic-encoding]] (new) — random encoding p(x̂|x) that can reach R(D) even for n = 1 (p. 184)
- [[blahut-arimoto-algorithm]] (new) — practical numerical method for R(D) and D(R) (p. 180)

## Canonical instances
- [[binary-rate-distortion]] — $R(D)=H(p)-H(D)$ with Hamming distortion (p. 181)
- [[gaussian-rate-distortion]] — $R(D)=\tfrac12\log(\sigma^2/D)$; one extra bit divides D by 4 (pp. 182–183)
- [[one-bit-gaussian-quantiser]] — deterministic 0.36σ² versus stochastic 0.25σ² (pp. 184–186)
- [[image-grey-level-quantisation]] — 64→4 levels, R = 1.933 versus 1.810 bits (pp. 186–189)
- [[speed-accuracy-tradeoff]] — fitted line R = −0.696E + 8.56 (p. 190)
- [[ecoli-chemotaxis-information]] — up to 0.04 bits/s gives 24% of swimming speed (p. 194)

## Bridges (candidates)
- [structural-analogy] Gaussian compression noise var(X−X̂) = D ↔ information-theory: Gaussian channel noise N in $\tfrac12\log\frac{P+N}{N}$ — the chapter equates the two expressions (Eq. 8.28).
- [structural-analogy] Bounded perception capacity ↔ behavioural economics/rational inattention: agents with limited information capacity — the chapter models perception as a finite-capacity channel.
- [metaphor] Speed–accuracy trade-off ↔ rate–distortion trade-off — fast, low-bit responses are less accurate.

## Questions this raises
- Why do Gaussian sources need Gaussian X̂ for the bound to be achieved, and what changes for non-Gaussian data?
- How does a different distortion measure (e.g. loss weighted by consequence, as in Sims) change R(D)?
- What explains the measured slope −0.696 rather than −1 in the speed–accuracy data?
- How can a stochastic encoder raise perceived quality at no extra rate (Blau & Michaeli)?

## Reading notes
- Printed = pdf − 16 (pdf 189 = p. 173). Page images agree with the text layer on all equations used.
- p. 177: the text says channel capacity "C = nH(X) bits/element", which looks inconsistent with p. 173 (C = R = H(X) bits/element). I flag it, not resolve it.
- Eq. 8.38 is printed as $\hat X\sim\mathcal N(x(1-D/\sigma^2),\dots)$; the mean contains x, so it is a conditional distribution given x.
- The Gaussian-ideal comparison in 8.7 treats the measured values as if Gaussian (the author says "very loosely speaking").
- Fig. 8.9 has no printed axis label other than speed and information rate; values quoted are from the text.
- Derivation details for Eqs. 8.21, 8.24, 8.29 and 8.38 are not given in the unit ("it can be shown"); only for the rate distortion theorem does the author point to references for proofs (pp. 180–181).
