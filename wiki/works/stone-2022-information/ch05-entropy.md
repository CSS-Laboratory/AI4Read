---
id: stone-2022-information/ch05-entropy
work: stone-2022-information
unit: 5 Entropy of Continuous Variables
pages: 113-134
fields: [information-theory]
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
# Entropy of Continuous Variables

## L0 — One line
The entropy of a continuous variable is infinite, so we use differential entropy, which drops the infinite term and must be read together with the measurement precision.

## L1 — The gist (≤ 120 words)
How can Shannon's discrete entropy be extended to continuous variables such as height? Discretising into histogram bins of width Δx gives an entropy that grows without limit as Δx shrinks. Dropping the constant infinite term gives differential entropy. It can be estimated from data by subtracting log(1/Δx), and it can be zero or negative. Under three different constraints, the entropy-maximising distributions are uniform (fixed range), exponential (positive, fixed mean) and Gaussian (fixed variance). The chapter ends with fractional bits: after H bits, residual uncertainty is 2^(−H). This matters because estimates of continuous entropy must be interpreted together with the bin width or measurement noise.

**Prerequisites:** discrete entropy as average surprisal; histograms and probability density; logarithm rules; derivatives; mean and variance.

## L2 — Key ideas (5–10 bullets)
- Discretising a continuous variable with bin width Δx gives H(X^Δ) = (differential part) + log(1/Δx). This diverges as Δx → 0 (p. 116).
- Differential entropy H_dif(X) = E[log(1/p(X))] drops the infinite term. It is estimated from a histogram as H(X^Δ) − log(1/Δx) (pp. 117–118).
- Entropy estimated from relative frequencies (the maximum likelihood estimate, MLE: the observed proportion used as the probability) tends to be too small (p. 120).
- Under a monotonic map Y = g(X), H_dif(Y) = H_dif(X) + E[log|dY/dX|]. Scaling by c adds log|c|, and adding a constant changes nothing (pp. 121–123).
- Maximum-entropy distributions: uniform for a fixed range, exponential for positive values with a fixed mean, Gaussian for a fixed variance. Entropies are log a, log(eμ) and ½ log(2πeσ²) (pp. 124–128).
- A signal with fixed variance (power) carries as much information as possible only if it is Gaussian, so an efficient power-limited signal should look like noise (p. 129).
- Differential entropy alone sets no limit on information. Measurement noise does, by making the variable effectively discrete (pp. 129–130).
- A fraction of a bit is defined by the residual uncertainty (the fraction of the original uncertainty range that remains after receiving H bits), U = 2^(−H) (p. 132).

## L3 — Walkthrough

### 5.1 Introduction (p. 113)
In many cases results for discrete variables extend easily to continuous ones, but information theory is not one of those cases (p. 113). The author reports that Shannon derived continuous entropy from the discrete definition. He also reports that MacKay calls the defining equation "illegal" (p. 113). The chapter follows the historical route: a naive definition that gives infinities, then definitions that can be computed (p. 113).

### 5.2 The Trouble With Entropy (pp. 114–117)
Entropy needs the probability of each value. For a continuous variable this is its probability density function (pdf), here called its *distribution* (p. 114). Build a histogram with bin width Δx. The entropy of the discretised variable $X^\Delta$ is the average surprisal of its bins (p. 114):

$$H(X^\Delta)=\sum_i (\text{prob } X \text{ in } i\text{th bin})\log\frac{1}{\text{prob } X \text{ in } i\text{th bin}} \tag{5.1}$$

Bin $i$ with $n_i$ values has area $a_i=n_i\Delta x$ (5.2). The probability is $a_i/A$ (5.3), with $A=\sum_i a_i$ (5.4). So $P_i=a_i/A$ (5.5), and $\sum_i P_i=1$ (5.6) (p. 115). A bin of height $p(x_i)$ and width Δx has

$$P_i=p(x_i)\,\Delta x \tag{5.7}$$

Hence (p. 116)

$$H(X^\Delta)=\sum_i P_i\log\frac1{P_i} \tag{5.8}$$

$$H(X^\Delta)=\sum_i p(x_i)\Delta x\,\log\frac{1}{p(x_i)\Delta x} \tag{5.9}$$

Split the logarithm:

$$\log\frac{1}{p(x_i)\Delta x}=\log\frac1{p(x_i)}+\log\frac1{\Delta x} \tag{5.10}$$

Then $H(X^\Delta)=\big[\sum_i p(x_i)\Delta x\log\frac1{p(x_i)}\big]+\big[\log\frac1{\Delta x}\sum_i P_i\big]$. Using (5.6):

$$H(X^\Delta)=\Big[\sum_i p(x_i)\,\Delta x\log\frac1{p(x_i)}\Big]+\log\frac1{\Delta x} \tag{5.11}$$

As Δx → 0, the first term becomes an integral and the second diverges:

$$H(X)=\Big[\int_{x=-\infty}^{\infty}p(x)\log\frac1{p(x)}\,dx\Big]+\infty \tag{5.12}$$

So the entropy of a continuous variable is infinite (p. 116). It increases with measurement precision, which sets the bin width (p. 116). The author's example: a table width given with precision ±0.1 inch carries more information than the same width given with precision ±1 inch (p. 117). So bin width must be taken into account when comparing entropies of different continuous variables (p. 117). Quantities that are differences of entropies, such as mutual information, avoid the infinity (the author defers this to Section 6.4) (p. 117).

*Intuition note.* Finer measurement precision adds information to each measurement, so as Δx → 0 the total grows without limit. Only the $\log(1/\Delta x)$ term diverges; the other term becomes the integral (p. 116).

### 5.3 Differential Entropy (pp. 117–119)
Equation 5.12 is true but unhelpful, because all distributions would have the same (infinite) entropy (p. 117). **Differential entropy** keeps only the "interesting" integral (p. 117):

$$H_{dif}(X)=\int_{x=-\infty}^{\infty}p(x)\log\frac1{p(x)}\,dx=\mathrm{E}[\log(1/p(X))] \tag{5.13}$$

**Estimating it from data.** Build a histogram, assuming it approximates an underlying continuous distribution (p. 118). Then

$$H_{dif}(X^\Delta)\approx\sum_i p(x_i)\Delta x\log\frac1{p(x_i)} \tag{5.14}$$

Substituting $P_i=p(x_i)\Delta x$:

$$H_{dif}(X^\Delta)\approx\sum_i P_i\log\frac{\Delta x}{P_i} \tag{5.15}$$

$$=\sum_i P_i\log\frac1{P_i}+\sum_iP_i\log\Delta x \tag{5.16}$$

$$=\Big[\sum_iP_i\log\frac1{P_i}\Big]-\log\frac1{\Delta x} \tag{5.17}$$

The bracket is $H(X^\Delta)$ from (5.8). So

$$H_{dif}(X)\approx H(X^\Delta)-\log\frac1{\Delta x} \tag{5.18}$$

Equivalently (substituting 5.14 into 5.11):

$$H(X^\Delta)\approx H_{dif}(X)+\log\frac1{\Delta x} \tag{5.19}$$

**Figure 5.2 example** (p. 119): 1 million samples from a Gaussian with σ = 1, whose differential entropy is 2.05 bits (Eq. 5.47). The values are:

| Bin width Δx | $H_{dif}(X^\Delta)$ | $H(X^\Delta)$ |
|---|---|---|
| 1 | 2.104 | 2.104 |
| 0.5 | 2.062 | 3.062 |
| 0.1 | 2.047 | 5.369 |

The author says the estimate is good for the "reasonable" bin widths 0.5 and 0.1 (p. 118). H(X^Δ) rises as bins narrow, while H_dif(X^Δ) stays near 2.05 (p. 119). An alternative is to fit a parametric function (e.g. a Gaussian) and use its analytic entropy. This is related to kernel estimation methods (p. 119).

*Intuition note.* Estimated entropy = (shape information) + (precision bonus log(1/Δx)). Subtracting the bonus leaves a number that does not depend on how finely you binned, apart from estimation error.

### 5.4 Under-Estimating Entropy (p. 120)
The author says this section can be skipped by readers unfamiliar with Bayes' rule. Estimating probabilities by relative frequency gives biased entropy estimates, for discrete or continuous X. With $m$ values, $P_i$ is the true probability and $\hat P_i$ the relative frequency (the maximum likelihood estimate, MLE). Then

$$H(X)=\sum_{i=1}^m P_i\log\frac1{P_i} \tag{5.20}$$

$$H_{MLE}(X)=\sum_{i=1}^m \hat P_i\log\frac1{\hat P_i} \tag{5.21}$$

Each $\hat P_i$ implicitly assumes a uniform prior on the $P_i$. Because entropy is a logarithmic function of $P_i$, this imposes a non-uniform prior on entropy, which the author calls an unwarranted assumption here (p. 120). It "can be shown" that $H_{MLE}$ tends to be smaller than the true entropy. This bias is reduced by using a uniform prior for entropy (p. 120).

### 5.5 Properties of Differential Entropy (pp. 121–123)
Let $y=g(x)$ (5.22). If $g$ is monotonic, then "it can be shown" that

$$H_{dif}(Y)=H_{dif}(X)+\mathrm{E}[\log|dY/dX|] \tag{5.23}$$

(The text gives no derivation.) A discrete variable's entropy depends only on the number of values and their probabilities. Doubling all die values changes the range but not the entropy. A continuous variable's entropy does depend on the range (p. 121).

**Multiplying by a constant.** If $Y=cX$, then $dY/dX=c$ (5.24) and $\mathrm{E}[\log|dY/dX|]=\log|c|$ (5.25). So

$$H_{dif}(Y)=H_{dif}(X)+\log|c|\ \text{bits} \tag{5.26}$$

For $Y=2X$: $dY/dX=2$ (5.27), $\mathrm{E}[\log|dY/dX|]=1$ (5.28), and $H_{dif}(Y)=H_{dif}(X)+1$ bit (5.29) (p. 122). Y is fully determined by X, yet has one more bit. The author calls this an apparent paradox tied to the difficulty of defining continuous entropy. With a fixed bin width, doubling the range doubles the number of bins, giving one more bit (p. 122).

**Adding a constant.** If $Y=X+c$, then $dY/dX=1$ (5.30–5.31) and $\mathrm{E}[\log|dY/dX|]=0$ (5.32) (p. 123). So $H_{dif}(Y)=H_{dif}(X)$ (5.33): shifting does not change entropy (p. 123).

### 5.6 Maximum Entropy Distributions (pp. 123–129)
**Why they matter.** Entropy equates to information, so a maximum-entropy distribution gives each value as much information as possible (p. 123). To send a quantity S through a channel, encode it as a variable X with a maximum-entropy distribution (p. 123). The author notes the fly's eye does this (Section 9.6) (p. 123).

**Discrete example.** Encoding a pair-of-dice outcome S (2–12) as plain binary numbers gives a far from uniform mix of 0s and 1s. Huffman coding gives almost equal proportions of 0s and 1s. The uniform distribution over {0,1} has maximum entropy, so Huffman coding implicitly encodes iid data as a maximum-entropy distribution. This fits with it giving almost one bit per binary digit (pp. 123–124).

For continuous variables, the maximum-entropy distribution is not necessarily uniform. Three constraints are considered (p. 124):
1. fixed upper and lower bounds → uniform;
2. fixed mean, values ≥ 0 → exponential;
3. fixed variance (e.g. power) → Gaussian.

**Uniform.** For $X\sim U(0,a)$ (5.35), the area must be one, so $p(x)\,a=1$:

$$p(x)=1/a \tag{5.34}$$

and zero elsewhere (p. 125). Then, since $\log(1/p)=\log a$ is constant,

$$H_{dif}(X)=\int_{x=0}^{a}p(x)\log a\,dx \tag{5.36}$$

$$=\log a\ \text{bits} \tag{5.37}$$

If the range grows from $a$ to $b=2a$ (i.e. $Y=2X$): $H_{dif}(Y)=\log b$ (5.38) $=\log 2a$ (5.39) $=\log a+1$ bits (5.40). This matches the discrete rule that doubling the number of outcomes adds one bit (p. 125). "It can be shown" that no distribution with fixed bounds has larger entropy than the uniform one (p. 126).

*Oddity:* differential entropy can be zero or negative. If $a=1$, $H_{dif}=0$. If $a=0.5$, $H_{dif}=-1$. The author suggests reading it relative to the $a=1$ case: $a=2$ is one bit larger, $a=0.5$ is one bit smaller (p. 126).

**Exponential.** One parameter, the mean μ (p. 126):

$$p(x)=\begin{cases}\frac1\mu e^{-x/\mu}& x\ge0\\0&x<0\end{cases}\tag{5.41}$$

Written $X\sim\exp(\mu)$ (5.42). "It can be shown" that

$$H_{dif}(X)=\log e\mu\ \text{bits} \tag{5.43}$$

For μ = 1 this is 1.44 bits (Fig. 5.4). If all we know is that X is positive with mean μ, the maximum-entropy distribution is the exponential (p. 127).

**Gaussian.** Parameters: mean μ and variance $v=\sigma^2$ (p. 127):

$$p(x)=\frac1{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}} \tag{5.44}$$

with variance $v=\mathrm{E}[(x-\mu)^2]$ (5.45) and notation $X\sim N(\mu,v)$ (5.46) (pp. 127–128). "It can be shown" that

$$H_{dif}(X)=\tfrac12\log 2\pi e\sigma^2 \tag{5.47}$$

$$=\tfrac12\log2\pi e+\log\sigma \tag{5.48}$$

$$=2.05+\log\sigma\ \text{bits} \tag{5.49}$$

So σ = 1 gives 2.05 bits. For fixed variance σ² (equated with power in physics), no distribution has larger entropy than the Gaussian (p. 128).

*Intuition note.* The constraint decides the winner. Fix the range and you get a flat density. Fix only the mean of a positive variable and you get a decaying one. Fix only the variance and you get the bell curve. In each case the variable is otherwise free to vary (p. 124).

**Why information looks like pure noise** (p. 129). Physical systems usually have a power limit, which corresponds to a limit on signal variance. The author states that a fixed-variance signal carries as much information as possible only if Gaussian. So a power-limited quantity (e.g. a telephone voice) should be recoded to be Gaussian. Noise is usually a mixture of unwanted signals, and the central limit theorem says such mixtures tend to be Gaussian. So Gaussian signal plus Gaussian noise gives a Gaussian measurement. A neurophysiologist who sees recordings that look like pure Gaussian noise should not complain, since this is what Shannon would predict of an efficient power-limited system (p. 129).

### 5.7 Making Sense of Differential Entropy (pp. 129–130)
Considered alone, the entropy of a continuous variable tells us almost nothing. It sets no limit on how much information the variable can convey, because each value can convey infinite information. For a discrete variable, entropy fixes that amount precisely (pp. 129–130). Measurement noise does set a strict upper limit. In effect it divides the variable into a finite number of discrete intervals, and the number of intervals increases as noise decreases (p. 130). Details are deferred to Section 7.3. Key point: noise turns a continuous variable into one with $m$ discriminable values, and $m$ decreases as noise increases (p. 130).

### 5.8 What is Half a Bit of Information? (pp. 130–134)
Take a variable with a uniform distribution and no knowledge of its value. Initial uncertainty is 1 (100%). One bit halves the uncertainty range. For an 8-sided die (entropy 3 bits), 2 bits reduce uncertainty by $2^2=4$, leaving 2 of the 8 values (p. 130). Residual uncertainty (a term the author says is unique to the book) after receiving $H$ bits is

$$U=2^{-H} \tag{5.50}$$

For H = 1: $U=2^{-1}=1/2$ (5.51–5.52). The recipe works for fractions, e.g. H = ½ (p. 132):

$$U=2^{-1/2}=0.71 \tag{5.53–5.54}$$

Two half bits: $U_1=0.71$, $U_2=0.71\times U_1=0.5$ (5.55–5.56), the same as one bit (p. 133). A quarter bit: $U=2^{-1/4}=0.84$ (5.57–5.58) (p. 133).

**The uncertain table length** (pp. 133–134). The table length is uniform on 0–10 feet. "Less than 5 feet" halves the range (1 bit, U = 0.5). "Less than 2.5 feet" gives another bit (U = 0.25). "Less than 7.1 feet" gives $U=7.1/10=0.71$, which is half a bit, since these numbers were chosen to match Eq. 5.54 (p. 134). Key point: U = 1 falls to $2^{-0.5}=0.71$ after half a bit and to $2^{-H}$ after $H$ bits (p. 134).

### 5.9 Summary (p. 134)
Continuous entropy is infinite because a continuous value is implicitly specified with infinite precision. This need not hurt in practice if we account for measurement precision when estimating differential entropy. Three maximum-entropy distributions were found, and the Gaussian is indistinguishable from pure noise. Fractional bits were explained through residual uncertainty (p. 134).

## Toy example (our own)
Let $X\sim U(0,4)$, so $p(x)=1/4$ and $H_{dif}(X)=\log_2 4=2$ bits (Eq. 5.37).
- Bins of width Δx = 0.5: 4/0.5 = 8 bins, each $P_i=1/8$. $H(X^\Delta)=8\times\frac18\log_2 8=3$ bits. Eq. 5.18: $3-\log_2(1/0.5)=3-1=2$ ✓.
- Bins of width Δx = 0.25: 16 bins, each $P_i=1/16$. $H(X^\Delta)=\log_2 16=4$. Then $4-\log_2(1/0.25)=4-2=2$ ✓.
- Halving the bin width added one bit to $H(X^\Delta)$ but left $H_{dif}$ unchanged.
- Scaling: $Y=2X\sim U(0,8)$, so $H_{dif}(Y)=\log_2 8=3=2+\log_2 2$ ✓ (Eq. 5.26).

## Concepts
- [[differential-entropy]] — $E[\log 1/p(X)]$, the entropy of a continuous variable with the infinite term dropped; can be negative (p. 117, p. 126)
- [[entropy]] — here, average surprisal of histogram bins; infinite for a continuous variable as bin width → 0 (p. 114, p. 116)
- [[bin-width-dependence]] (new) — discretised entropy equals $H_{dif}+\log(1/\Delta x)$, so entropies are comparable only at equal precision (p. 119)
- [[maximum-entropy-principle]] — choose the distribution with largest entropy under a given constraint; here uniform, exponential or Gaussian (p. 124)
- [[mle-entropy-bias]] (new) — entropy from relative frequencies tends to be smaller than the true entropy (p. 120)
- [[residual-uncertainty]] (new) — $U=2^{-H}$, fraction of original uncertainty left after $H$ bits (p. 131–132)
- [[bit]] — extended to fractions: half a bit shrinks uncertainty by a factor 0.71 (p. 132)
- [[noisy-channel]] — noise limits information per continuous value, making it effectively discrete (p. 130; canon link, not developed here)

## Canonical instances
- [[human-height-histogram]] — 5,000 height values binned to show how entropy depends on bin width (p. 114)
- [[gaussian-bin-width-experiment]] — 1 million Gaussian samples; $H$ and $H_{dif}$ at three bin widths (p. 119)
- [[huffman-dice-maxent]] — Huffman code for two dice gives near-uniform 0s and 1s (p. 123)
- [[neural-recording-as-noise]] — an efficient power-limited signal looks like Gaussian noise (p. 129)
- [[uncertain-table-length]] — uniform 0–10 ft; "under 7.1 ft" is half a bit (p. 133)

## Bridges (candidates)
- [structural-analogy] Bin-width dependence of $H(X^\Delta)$ ↔ measurement precision in statistics: the same data give different entropy at different resolutions.
- [same-math] Max-entropy under fixed variance gives Gaussian ↔ exponential-family / Gibbs form of MaxEnt solutions (canon link; not stated in this unit).
- [metaphor] "Information looks like noise" ↔ compression: well-compressed data look random.

## Questions this raises
- Differential entropy changes under rescaling and depends on bin width; which quantities avoid this (the author says differences of entropies, such as mutual information, avoid the infinity; Section 6.4)?
- How exactly does measurement noise fix the number of discriminable values $m$ (Section 7.3)?
- How large is the MLE entropy bias for a given sample size and number of bins?
- Can we practically recode a real signal to be Gaussian?

## Reading notes
- Printed pages 113–134 = pdf 129–150 (printed = pdf − 16).
- No exercises in this unit.
- Figure 5.1 caption uses δx, but the text uses Δx. Section 5.6 text has "variancev" (missing space).
- The text rounds the Gaussian entropy to 2.05 bits; Fig. 5.2(d) prints 2.047.
- Equations 5.23, 5.43 and 5.47 are stated without derivation ("it can be shown"; ref. 56 is cited for 5.43 and 5.47). Maximum-entropy claims are also given without proof. I have not supplied proofs.
- The Fig. 5.2 caption says "variance of one", while the text says standard deviation one. These are equivalent for σ = 1.
