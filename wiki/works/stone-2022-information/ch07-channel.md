---
id: stone-2022-information/ch07-channel
work: stone-2022-information
unit: "7 Channel Capacity: Continuous"
pages: 153-172
fields: [information-theory]
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
# Channel Capacity: Continuous

## L0 — One line
For a Gaussian channel, capacity $C=\tfrac12\log(1+P/N)$ per value is reached by a Gaussian input; for a bounded-range channel with negligible noise, the best input is uniform, obtained by encoding with the cdf of the message distribution.

## L1 — The gist (≤ 120 words)
Which input distribution $p(X)$ maximises the information a noisy continuous channel carries? Because $I=H(Y)-H(\eta)$ and the noise entropy is fixed, one must maximise the output entropy. With fixed output variance, a Gaussian input gives a Gaussian output and capacity $\tfrac12\log(1+P/N)$ bits per value. Long codewords make errors fall quickly with message length when rate is below capacity. With a bounded output range, the output should be uniform; if noise is negligible, this is achieved by encoding messages with the cdf (cumulative distribution function) of their own distribution. The chapter also links mutual information to correlation for Gaussian variables.

**Prerequisites:** entropy and mutual information; differential entropy of a Gaussian and the max-entropy results (Sec. 5.5–5.6); variance; cdf and change of variables for densities.

## L2 — Key ideas (5–10 bullets)
- Capacity is $\max_{p(X)}[H(Y)-H(\eta)]$. The noise entropy is fixed, so the task is to maximise output entropy (p. 155).
- Gaussian channel: Gaussian input, noise and output give $C=\tfrac12\log(1+P/N)$ bits per value. This is an informal proof, and signal power has diminishing returns (pp. 155–157).
- $2^C=\sigma_y/\sigma_\eta$ is the number of inputs one output value can discriminate. Noise effectively discretises the output (pp. 157–158).
- For codewords of length $n$, $m=2^{nC}$ inputs are discriminable. Per watt of power expended, increasing $n$ beats increasing $P$; the author infers the same for bandwidth, which the book does not cover (p. 160).
- Below capacity ($R<C$), the error probability from Eq. 7.40 falls towards zero as $n$ grows. Shannon's theorem proves good codewords exist but does not say how to find them (pp. 161, 164).
- For Gaussian variables, $I=\tfrac12\log\frac1{1-\rho^2}$. Large correlation cannot coexist with zero mutual information, but large mutual information can coexist with zero correlation (e.g. if not Gaussian) (pp. 165–166).
- Fixed-range channel: with negligible noise, the best input is uniform. To carry as much information as possible (with negligible noise), the encoding function must be the cdf of $p_s(S)$ (pp. 167–172).

## L3 — Walkthrough

### 7.1–7.2 Introduction and capacity
Capacity is $C=\max_{p(X)} I(X,Y)$ (7.1), with $I=H(Y)-H(Y|X)$ (7.2), so $C=\max_{p(X)}H(Y)-H(Y|X)$ (7.3) (p. 153). Two constraints are studied: (1) output with fixed variance and infinite range, such as a loudspeaker signal (power equals variance); (2) output with finite range, such as a photoreceptor between 0 and 5 volts (p. 154).

### 7.3 The Gaussian channel
A Gaussian channel has Gaussian noise. Noise is $\eta=Y-X$ (7.4), and $H(Y|X)=H(\eta)$, so $I=H(Y)-H(\eta)$ (7.6) and
$$C=\max_{p(X)} H(Y)-H(\eta).\tag{7.7}$$
(pp. 154–155)

**Argument (informal).** The noise entropy is a fixed property of the channel, so only $H(Y)$ can be raised. For fixed variance, the maximum-entropy distribution is Gaussian (Sec. 5.6). A sum of independent Gaussians is Gaussian and $Y=X+\eta$, so $p(X)$ should be Gaussian. Then $I(X,Y)=H(Y)-H(\eta)=C$ (7.8–7.9). The author calls this an informal proof of Shannon's continuous noisy-channel coding theorem for Gaussian channels (p. 155).

**Derivation.** With $H(\eta)=\tfrac12\log 2\pi e v_\eta$ (7.10) and $H(X)=\tfrac12\log 2\pi e v_x$ (7.11), independence gives $v_y=v_x+v_\eta$ (7.12). So
$$H(Y)=\tfrac12\log 2\pi e v_y=\tfrac12\log 2\pi e(v_x+v_\eta)\tag{7.13–7.14}$$
(p. 156). If signal and noise variances are equal, output variance is twice input variance (p. 156). Then
$$C=\tfrac12\log 2\pi e(v_x+v_\eta)-\tfrac12\log 2\pi e v_\eta\tag{7.15}$$
$$=\tfrac12\log\frac{v_x+v_\eta}{v_\eta}\tag{7.16}$$
$$=\tfrac12\log\Big(1+\frac{v_x}{v_\eta}\Big).\tag{7.17}$$
Setting power $P=v_x$ and noise power $N=v_\eta$ (proportionality constant 1):
$$C=\tfrac12\log\Big(1+\frac PN\Big)\text{ bits},\tag{7.18}$$
where $P/N$ is the signal-to-noise ratio (SNR) (p. 156).

Equivalent forms: $C=\tfrac12\log\frac{v_x+v_\eta}{v_\eta}=\tfrac12\log\frac{v_y}{v_\eta}=\log\frac{\sigma_y}{\sigma_\eta}$ (7.19–7.21) (p. 157). Figure 7.1: sampling at 1,000 values/s gives $C=500\log(1+P/N)$ bits/s. With noise power fixed, more signal power has diminishing returns (p. 157).

For continuous variables one "symbol" is one input value, so $C$ is in bits per transmitted value. The number of equiprobable inputs discriminable from one output value is
$$m=2^C=\sigma_y/\sigma_\eta\tag{7.22–7.23}$$
(pp. 157–158). **Key point:** noise effectively discretises a continuous Gaussian output into a discrete distribution. The proof assumes very long codewords (p. 158).

*Intuition note.* Noise blurs each output by about $\sigma_\eta$. The output spreads over about $\sigma_y$, so about $\sigma_y/\sigma_\eta$ distinguishable "slots" fit. More SNR gives more slots, but only logarithmically in bits.

**Long messages.** Take $\mathbf x=(x_1,\dots,x_n)$ (7.24) and $\mathbf y=\mathbf x+\boldsymbol\eta$, with $y_i=x_i+\eta_i$ (7.25–7.29). Each of these vectors is $n$ values long. With zero means, $v_x=\frac1n\sum x_i^2$, $v_\eta=\frac1n\sum\eta_i^2$, $v_y=\frac1n\sum y_i^2$ (7.30), with $P=v_x$ and $N=v_\eta$ (p. 159). Shannon's theorem rests on a counting argument. If the $n$ values are Gaussian with variance $v_x$ and the noise is Gaussian with variance $v_\eta$, the maximum number of equiprobable input vectors reliably discriminable from outputs is
$$m=2^{nC}=\Big(\frac{\sigma_y}{\sigma_\eta}\Big)^n,\tag{7.31}$$
so each output gives $\log m=nC=n\log\frac{\sigma_y}{\sigma_\eta}$ bits (7.32–7.34) (p. 159).

**Author's example.** $v_x=15$, $v_\eta=1$, so $v_y=16$, $\sigma_y=4$, $C=2$ bits per value. For $n=4$: $nC=4\log4=8$ bits, so $m=2^8=256$ (7.35–7.38). The author says that in practice $n$ would be much larger (pp. 159–160).

**Power versus length.** $nC=\frac n2\log(1+P/N)$ (7.39). Doubling $n$ doubles the power needed and doubles the information. Doubling $P$ raises information but does not double it (Figure 7.1). So given the choice, increase $n$. The author infers the same for bandwidth versus power, though bandwidth is not covered in the book (p. 160).

### 7.4 Error rates
Informal theorem: if a source has entropy $R$, it can be encoded and sent over a continuous noisy channel of capacity $C$ with error rate approaching zero as $n\to\infty$, provided $R<C$ (p. 161). For any continuous channel, Shannon gave
$$P(error)\approx\Phi\!\left(\sqrt n\Big(\frac{2P(P+N)}{N(P+2N)}\Big)^{1/2}(R-C)\right),\tag{7.40}$$
where $\Phi$ is the Gaussian cdf. Since $R<C$, $R-C<0$. For fixed $P$ and $N$ the argument shrinks in proportion to $\sqrt n$, so the error probability falls towards zero (p. 161). Figure 7.2 uses $R/C=0.99$; error approaches zero for $n$ above about 4,000 (p. 162).

*Intuition note.* Even with source rate at 99% of capacity, the error probability approaches zero as messages get longer (Figure 7.2 plots $n$ up to 4,000).

### 7.5 Using a Gaussian channel
A non-Gaussian signal such as a voice could be transformed to a Gaussian one before sending (p. 162). The author answers the objection that reading a continuous output would need infinite accuracy by noting that no instrument reads it with 100% accuracy. Instrument (voltmeter) noise adds to channel noise, and the combined noise lowers the number of discriminable inputs (pp. 162–163). A codebook has $m$ rows, each a codeword $\mathbf x_i$ of $n$ values and a message $s_i$. With $C=2$ and $n=20$, $m=2^{nC}=2^{40}\approx10^{12}$ messages (7.41–7.42) (p. 163). Short codewords would have high error rates; longer ones fix this. The hardest part is finding $m$ discriminable codewords: Shannon's theorem says they exist but not how to find them. Practical methods that approach $2^{nC}$ messages with negligible error do exist but are beyond the book's scope (p. 164).

### 7.6 Mutual information and correlation
Correlation coefficient: $\rho=\dfrac{E[(x_j-\bar x)(y_j-\bar y)]}{\sigma_x\sigma_y}$ (7.43), estimated by $\hat\rho=\frac{1}{n\sigma_x\sigma_y}\sum_{j=1}^n(x_j-\bar x)(y_j-\bar y)$ (7.44) (pp. 164–165). For Gaussian $X,Y$ with correlation $\rho$:
$$I(X,Y)=0.5\log\frac1{1-\rho^2}\text{ bits},\tag{7.45}$$
$$\rho=\sqrt{1-2^{-2I(X,Y)}}.\tag{7.46}$$
Figure 7.4: $\rho=0.866$ gives $I=1$ bit. As $\rho\to1$, $I\to\infty$ (Figure 7.5) (p. 165). Correlation can be viewed as a special version of mutual information. $X,Y$ can have large $I$ and zero correlation (for example if not Gaussian), but not large correlation with zero $I$ (p. 166).

### 7.7 The fixed-range channel
**Informal solution.** With bounded output, the maximum-entropy output is uniform (Sec. 5.6). So the input distribution should complement the known noise form to make the output uniform (p. 166).

**Second problem.** Messages $S\sim p_s(S)$ are encoded by a continuous $g$ as $x=g(s)$ (7.48), with $y=x+\eta$ (7.47) and $y=g(s)+\eta$ (7.49). Unique mapping makes $g$ monotonic (p. 167). Assume negligible noise, so $I=H(Y)$ and
$$\frac{\partial I}{\partial g(S)}=\frac{\partial H(Y)}{\partial g(S)}=0\tag{7.50–7.51}$$
at the maximum. So the best $g$ makes $p(Y)$ uniform (p. 167). The author notes the notation $\partial/\partial g(S)$ is an abuse. In practice $g$ may be a sigmoid, such as a Gaussian cdf with steepness $\sigma$: $g(s)=\frac1{\sigma\sqrt{2\pi}}\int_{-\infty}^s e^{-(t-\mu)^2/2\sigma^2}dt$ (7.52), so the derivative is taken with respect to $\sigma$ (p. 168). **Key point:** with negligible noise, maximising $I$ means finding $g$ that makes $p(X)$ uniform (p. 168).

**Entropy of a transformed variable.** With $\eta\approx0$: $y\approx g(s)$ (7.53–7.55), and $H(Y)=H(X)+H(\eta)\approx H(X)$ (7.56–7.57) (p. 169). Using $p_x(x)=p_s(s)/|dg/ds|$ (7.58; Sec. 5.5; slope is positive because $g$ is a cdf), define $f(s)=dx/ds=dg/ds$ (7.59–7.60), so $p_x(x)=p_s(s)/f(s)$ (7.61) (pp. 169–170). Then, using $H(X)=\int p_x\log\frac1{p_x}dx$ (7.62) and $dx=f(s)\,ds$:
$$H(X)=\int \frac{p_s}{f}\Big(\log\frac{f}{p_s}\Big)f\,ds\tag{7.63}$$
$$=\int p_s(s)\log\frac{f(s)}{p_s(s)}ds\tag{7.64}$$
$$=\int p_s\log\frac1{p_s}ds+\int p_s\log f\,ds\tag{7.65}$$
$$=H(S)+E[\log f(s)].\tag{7.66}$$
The author describes this as $H(S)$ plus the mean slope of $g$, and says it tallies with Eq. 5.23 (p. 171).

*Intuition note.* $H(S)$ is fixed by the messages, so only the shape of $g$ can change $H(X)$. Where $g$ is steep it spreads probability out; where flat it piles it up.

**Best encoding.** $H(X)$ is maximal when $p_x$ is uniform, so $\frac1{p_x}=\frac{f(s)}{p_s(s)}$ (7.67) must be constant. Both are densities (area one), so this holds only if $p_s=f$ (p. 171). Then $g(s)=\int_{-\infty}^s f(t)dt$ (7.68) equals $g^*(s)=\int_{-\infty}^s p_s(t)dt$ (7.69). **Conclusion:** to carry as much information as possible, $g$ must be the cdf of $p_s(S)$ (p. 172), under this section's negligible-noise assumption (p. 167). Figure 7.6 shows a Gaussian $S$ mapped to uniform $X$ (p. 170).

### 7.8 Summary
Continuous entropy and information are abstract measures of quantities like energy and power. The author says they remain well defined if tied to their physical interpretation (p. 172).

## Toy example (ours)
**Part A.** Gaussian channel with $P=3$, $N=1$: $v_y=4$, $\sigma_y=2$, $\sigma_\eta=1$. $C=\tfrac12\log_2(1+3)=\tfrac12\cdot2=1$ bit, and $m=2^C=2=\sigma_y/\sigma_\eta$. For $n=10$: $nC=10$ bits, $m=2^{10}=1024$. Doubling $n$ to 20 gives 20 bits. Doubling $P$ to 6 gives $C=\tfrac12\log_2 7\approx1.40$ bits, so $10\times1.40=14.0$ bits, not 20.

**Part B.** If $p_s(s)=2s$ on $[0,1]$, then $g^*(s)=\int_0^s2t\,dt=s^2$. Then $f=2s$ and $p_x=p_s/f=1$: $X$ is uniform on $[0,1]$, as the cdf rule predicts.

## Concepts
- [[channel capacity]] — $\max_{p(X)}I(X,Y)$; here $\max H(Y)-H(\eta)$ (pp. 153, 155)
- [[noisy channel]] — here an additive channel $Y=X+\eta$ (p. 154)
- [[mutual information I(X;Y)]] — $H(Y)-H(Y|X)$; for Gaussians, $\tfrac12\log\frac1{1-\rho^2}$ (pp. 153, 165)
- [[differential entropy]] — Gaussian entropy $\tfrac12\log2\pi ev$, used for noise, input and output (p. 155)
- [[maximum entropy principle]] — fixed variance gives Gaussian; bounded range gives uniform (pp. 155, 166)
- [[noisy-channel coding theorem]] — here the informal Gaussian proof and the error formula (pp. 155, 161)
- [[Shannon–Hartley formula]] — close relative: $C=\tfrac12\log(1+P/N)$ per value, which the author calls Shannon's well-known equation. The bandwidth form $W\log_2(1+S/N)$ is not stated here (p. 156)
- [[signal-to-noise-ratio]] (new) — $P/N$, ratio of signal variance to noise variance (p. 156)
- [[correlation-coefficient]] (new) — $\rho$ of Eq. 7.43 (p. 164)
- [[codebook]] (new) — table of $m$ codewords of length $n$, each tied to a message (p. 163)
- [[cdf-encoding]] (new) — encoding $g$ equal to the cdf of $p_s$, giving uniform inputs (p. 172)

## Canonical instances
- [[loudspeaker-vs-photoreceptor]] — fixed-variance versus bounded-range channels (p. 154)
- [[voltmeter-noise]] — reading noise merges with channel noise (pp. 162–163)
- [[gaussian-codebook-n20]] — $n=20$, $C=2$, $2^{40}\approx10^{12}$ messages (p. 163)
- [[height-weight-correlation]] — example of correlated variables (p. 164)
- [[gaussian-to-uniform-encoding]] — Figure 7.6 (p. 170)

## Bridges (candidates)
- [structural-analogy] Capacity grows only as $\log(1+\mathrm{SNR})$ ↔ economics: diminishing returns to a single input — one logarithmic form, but the source makes no such link.
- [same-math] $\rho=\sqrt{1-2^{-2I}}$ for Gaussians ↔ statistics: correlation coefficient — the same bivariate Gaussian quantity expressed two ways.
- [structural-analogy] Encoding with the cdf to get a uniform output ↔ statistics: probability integral transform — same change-of-variables idea.

## Questions this raises
- Eq. 7.31 is argued by counting. How are the Gaussian codewords chosen and shown to be discriminable?
- What happens to capacity if the noise is not Gaussian, or if the input power is limited but the output is bounded?
- How does the cdf rule change when noise is not negligible?
- How does the per-value $C$ become capacity per second via bandwidth?

## Reading notes
- Printed page = pdf − 16.
- The chapter has no exercises.
- Figure 7.2 caption gives $P=10$, $N=1$, $C=1$ bit. Eq. 7.18 gives $\tfrac12\log_2 11\approx1.73$ bits for these values (our calculation), so the caption seems inconsistent with 7.18. The $R=0.99$, $C=1$ values are used for the plot.
- Eq. 7.56 is written as an equality, then approximated in 7.57.
- Section 7.7 calls $E[\log f(s)]$ the "mean value of the slope"; the formula is the mean of the log-slope.
- Text and image agree on equations; no OCR problems affected the math.
