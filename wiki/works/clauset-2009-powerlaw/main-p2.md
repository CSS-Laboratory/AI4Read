---
id: clauset-2009-powerlaw/main-p2
work: clauset-2009-powerlaw
unit: "paper, part 2/2 (end of Sec. 6 on real-world data, Sec. 7 Conclusions, Appendices A–D)"
pages: 23–43
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Power-law distributions in empirical data — part 2: results on 24 data sets, conclusions, appendices

## L0 — One line
Applied with proper maximum-likelihood fitting, goodness-of-fit and likelihood-ratio tests, only one of 24 data sets examined (word frequencies) appears to be a truly convincing power law, and the appendices give the mathematics behind those tools.

## L1 — The gist (≤ 120 words)
The authors apply their method to 24 data sets. Seventeen are statistically consistent with a power law, seven are firmly ruled out. Even among the consistent ones, log-normal or stretched-exponential fits are often equally plausible. Only word frequencies are clearly convincing. A straight line on a log-log plot is necessary, not sufficient, evidence. The appendices explain why regression fits are unreliable. They derive the maximum-likelihood estimators for continuous and discrete data, with their error properties, and the likelihood-ratio test. They also give recipes for generating power-law random numbers. This matters because many claimed power laws rest on weak evidence.

**Prerequisites:** likelihood and log-likelihood; central limit theorem; normal and exponential distributions; Taylor expansion; CDF and its inverse; p-values. Terms: x_min is the lower bound above which the power law is fitted; a power law with cut-off has an exponentially cut extreme tail; log-normal and stretched exponential are rival heavy-tailed families; the Hurwitz zeta function normalizes the discrete power law.

## L2 — Key ideas
- Applying the full pipeline to 24 data sets, 17 are consistent with a power law and 7 are ruled out by the goodness-of-fit p-value (p. 23).
- Fitted exponents often differ clearly from earlier ad hoc estimates, e.g. proteins 3.1 ± 0.3 versus a reported 2.44 (p. 23).
- Only word frequencies get the rating "good". Ten sets are "moderate", ten favour a power law with cut-off, three get "none" (pp. 26, 28–29).
- Log-normal and stretched exponential often cannot be told apart from a power law (inconclusive in most cases; log-normal vs power law extremely hard to separate). In such cases the authors say one must consider mechanistic or other non-statistical arguments (p. 26).
- Straight-line log-log behaviour is necessary but not sufficient. Whether a heavy tail is enough depends on the scientific goal (pp. 26, 30).
- Regression on logs gives biased slopes, invalid standard errors, uninformative r², and unnormalized fits (pp. 31–32).
- The continuous MLE is α̂ = 1 + n[Σ ln(xᵢ/x_min)]⁻¹, asymptotically Gaussian with variance (α−1)²/n. The discrete MLE needs a zeta-function equation, with a simple approximation for x_min ≳ 6 (pp. 33–37).
- The likelihood-ratio test gives a p-value for the sign of the log-ratio (the sign shows which model fits better), not for goodness of fit. Random power-law numbers come from inverting the CDF (pp. 37–40).

## L3 — Walkthrough

### 6 (continued). Data sets and results
**Data (pp. 23, 24–25).** The list continues with items m–x. These are US city populations, email address-book sizes, wildfire acres, solar-flare intensities, earthquake intensities, religious adherents, surnames, wealth of the richest Americans, paper citations, papers per mathematician, AOL web hits and web links (p. 23). Figs. 6.1 and 6.2 show each CDF with its maximum-likelihood power-law fit (pp. 24–25). Many sets are subsets of larger entities, and some sampling procedures may be biased. No bias correction was attempted (p. 23).

**Table 6.1 (p. 27)** lists n, mean, standard deviation, maximum, x̂_min, α̂, n_tail and the p-value. Examples:

| data set | x̂_min | α̂ | p |
|---|---|---|---|
| word use | 7 ± 2 | 1.95(2) | 0.49 |
| protein degree | 5 ± 2 | 3.1(3) | 0.31 |
| citations | 160 ± 35 | 3.16(6) | 0.20 |
| solar flares | 323 ± 89 | 1.79(2) | 1.00 |
| earthquakes | 0.794 ± 80.198 | 1.64(4) | 0.00 |

*Different exponents from ad hoc methods (p. 23).* The protein-network exponent has been reported as 2.44, but the authors find 3.1 ± 0.3. Citation data were reported as 2.9 or 2.5, but the maximum-likelihood value is 3.16 ± 0.06. The authors call these values incompatible.

*Goodness of fit (p. 23).* 17 of 24 data sets are consistent with a power law. The other seven are ruled out: HTTP connections, earthquakes, web links, fires, wealth, web hits, and the metabolic network. For HTTP and wealth the power law beats all the alternatives tested by likelihood ratio, so no tested form fits them well.

**Tables 6.2 (continuous) and 6.3 (discrete), pp. 28–29.** These give likelihood ratios (LR), their p-values, and a "support for power law" verdict. Positive LR favours the power law. For non-nested alternatives the table gives the normalized ratio n^{-1/2}ℛ/σ (Eq. C.6). For the cut-off alternative it gives the actual ratio (p. 28). Verdicts:
- *Good:* words only.
- *Moderate:* birds, blackouts, book sales, cities, religions, wars, citations, papers, proteins, terrorism.
- *With cut-off:* fires, flares, quakes, surnames, web hits, web links, Internet, calls, email, species.
- *None:* HTTP, wealth, metabolic.

Meaning of the verdicts (Table 6.2 caption, p. 28): "none" = probably not power-law distributed; "moderate" = a good fit but other plausible alternatives exist; "good" = a good fit and no alternative is plausible; "with cut-off" = the power law with exponential cut-off is clearly favoured over the pure power law, though some alternatives are also good fits.

Findings in the text (p. 26):
- The power law appears to be truly convincing only for words: an excellent fit and no alternative carries weight.
- The exponential is ruled out in all cases except blackouts, religions and email. There the power law is favoured over the exponential, but the p-value is too large to trust. Poisson is ruled out for every discrete set.
- Log-normal and stretched exponential are mostly inconclusive. Birds, books, cities, religions, wars, citations, papers, proteins and terrorism are plausible power laws but also plausible log-normals and stretched exponentials. The authors say it is then important to look at physical or theoretical factors and to consider whether a mechanistic or other non-statistical argument favours one form.
- Some conclusive cases exist. The stretched exponential is ruled out for book sales, calls and citations, but strongly favoured over the power law for fires and quakes. The log-normal is ruled out only for HTTP.
- The authors find log-normal versus power law extremely hard to separate. Over realistic ranges of x they are very closely equal, so it appears unlikely that any test could tell them apart unless the data set is extremely large (cf. their Section 5 synthetic tests).
- For almost a dozen sets (nine are named) the cut-off form is clearly favoured. For surnames it is only weakly favoured (p near the threshold). For the rest there is no statistical reason to prefer it.

*Intuition note.* The tests give evidence for or against a power law: they show whether it is rejected and whether rivals fit better. For many data sets the power law is plausible, but log-normals and stretched exponentials are plausible too (p. 26).

### 7. Conclusions (pp. 26, 30)
- Many fields study power laws, but principled methods have not taken root and hypotheses are often untested. Apparent power laws may sometimes be "wishful thinking" (p. 26).
- Judging by a roughly straight line on a log-log histogram is "a necessary but by no means sufficient condition" (p. 26).
- For many data sets the power-law hypothesis is statistically reasonable, though often other distributions (log-normal, stretched exponential) are compatible too. In the remaining cases it is incompatible with the data. The techniques are meant to give objective evidence for or against a power law (p. 30).
- The proposed techniques can in principle be extended to non-power-law distributions, but this is not done here (p. 30).
- In some instances, such as earthquakes, the power law is plausible only if one assumes an exponential cut-off that modifies the extreme tail (p. 30).
- For some goals a heavy tail may be enough. In Internet studies, quantifying the heavy tail may be enough for engineers (infrastructure needs, overload risk). If the goal is to infer mechanisms, the exact form may matter greatly. Non-parametric estimates may help, but are hard for heavy-tailed data (p. 30).
- **Ijiri–Simon and Mitzenmacher argue** that characterizing distributions is only part of the task: models must also be validated, and practical uses should be sought (p. 30).

### Appendix A. Linear regression and power laws (pp. 31–32)
The common method uses $\log p(x) = \alpha \log x + c$ \tag{A.1}
and fits a line to a histogram or rank-ordered CDF. The slope is α̂, and r² is read as fit quality (p. 31). Three problems:

- **A.1 Standard errors (p. 31).** The usual formula needs independent Gaussian noise in the dependent variable. The noise in the histogram frequencies is Gaussian (actually Poisson), but the noise in their logarithms is not. CDF values are Gaussian, but their logs are not, and adjacent values are strongly correlated because P(x) = P(x+1) + p(x). CDF fits are empirically more accurate (Sec. 3), not because their assumptions are more valid but because CDF fluctuations are smaller. The error estimate is typically a gross underestimate.
- **A.2 Validation (p. 32).** If the data are truly power law and n is large, a low r² is unlikely, so a low r² can reject the hypothesis. But non-power-law distributions, e.g. the log-normal, can give high r². In practice r² is rarely low whatever the distribution, so it has very little power as a test.
- **A.3 Validity (p. 32).** The CDF must equal 1 at x_min and the PDF must integrate to 1. Ordinary regression does not enforce this. Constrained methods exist but are little used in the power-law literature.

*Intuition note.* Regression on log-log plots breaks its own assumptions. A high r² can occur even when the data do not follow a power law, so it is not evidence for the power-law form (p. 31).

### Appendix B. Maximum likelihood estimators (pp. 32–37)
**B.1 Continuous data (pp. 32–33).** The estimator was first derived (to the authors' knowledge) by Muniruzzaman in 1957 and is equivalent to the Hill estimator. Density, for $x \ge x_{\min}$:
$$p(x)=\frac{\alpha-1}{x_{\min}}\left(\frac{x}{x_{\min}}\right)^{-\alpha}\tag{B.1}$$
The likelihood of n observations xᵢ ≥ x_min is
$$p(x\mid\alpha)=\prod_{i=1}^{n}\frac{\alpha-1}{x_{\min}}\left(\frac{x_i}{x_{\min}}\right)^{-\alpha}\tag{B.2}$$
The log-likelihood has its maximum at the same α:
$$\mathcal L=\ln p(x\mid\alpha)=\sum_{i=1}^n\Big[\ln(\alpha-1)-\ln x_{\min}-\alpha\ln\tfrac{x_i}{x_{\min}}\Big]=n\ln(\alpha-1)-n\ln x_{\min}-\alpha\sum_{i=1}^n\ln\frac{x_i}{x_{\min}}\tag{B.3}$$
Setting ∂ℒ/∂α = 0 gives
$$\hat\alpha=1+n\left[\sum_{i=1}^n\ln\frac{x_i}{x_{\min}}\right]^{-1}\tag{B.4}$$

**B.2 Formal results (pp. 33–34).**
- *Theorem B.1.* Under mild regularity conditions, for i.i.d. draws from a distribution with parameter α, α̂ → α almost surely as n → ∞ (proof cited, ref. [46]).
- *Proposition B.2 (Muniruzzaman).* The continuous-power-law MLE converges almost surely to the true α. Proof: ln(x/x_min) is exponentially distributed with rate α − 1. By the strong law of large numbers, (1/n)Σ ln(xᵢ/x_min) converges almost surely to its expectation (α−1)⁻¹ (p. 33). (Added step: then (B.4) gives α̂ → 1 + (α−1) = α.)
- *Theorem B.3.* If the MLE is consistent and, on an interval (α−ε, α+ε), the ratio
$$\frac{\partial^3\mathcal L(\alpha_1)/\partial\alpha^3}{\partial^2\mathcal L(\alpha_2)/\partial\alpha^2}\tag{B.5}$$
is bounded for all x, then asymptotically α̂ is Gaussian, centered on α, with variance 1/nI(α), where
$$I(\alpha)=-\mathbf E\left[\frac{\partial^2\log p(X\mid\alpha)}{\partial\alpha^2}\right]\tag{B.6}$$
is the Fisher information. Moreover ∂²ℒ(α̂)/∂α² → I(α) (p. 33).
- *Proposition B.4.* The MLE of the continuous power law is asymptotically Gaussian with variance (α−1)²/n. Proof: ∂²log ℒ/∂α² = −n(α−1)⁻² and ∂³log ℒ/∂α³ = 2n(α−1)⁻³. The ratio is then 2(α₂−1)²/(α₁−1)³ in magnitude, which is bounded near any α because α > 1 (p. 33). (Added step: the Fisher information is $I=(\alpha-1)^{-2}$, so $1/nI=(\alpha-1)^2/n$.)
- *Cramér–Rao inequality (p. 34).* Any unbiased estimator of α has variance at least 1/nI(α). The MLE attains this bound and is called asymptotically efficient.
- *Corrections (p. 34).* Prop. B.4 gives approximate standard errors and Gaussian confidence intervals that become exact as n grows. Corrections are O(1/n), while the leading terms are O(1/√n). The main text neglects them. In general the sampling distribution is found by bootstrapping.
- *Exact case (p. 34).* If x_min is known a priori or fixed by fiat, (α̂−1)/n has an inverse gamma distribution with shape n and scale α−1. Then α̂ has mean (nα−1)/(n−1) and standard deviation n(α−1)/[(n−1)√(n−2)], which differ from the large-n values by O(1/n).
- **Fig. B.2 (p. 35):** error from sample size decays as O(n⁻¹) and is below 1% of α when n ≳ 50 (α = 2, 2.5, 3; 100 repetitions).

*Intuition note.* The estimator depends only on the average log of x/x_min. Its error shrinks like 1/√n and is larger when α is larger, because (α−1)² grows.

**B.3 Discrete data (pp. 34–35).** Definition, with the Hurwitz zeta function ζ:
$$p(x)=\frac{x^{-\alpha}}{\zeta(\alpha,x_{\min})}\tag{B.7}$$
For x_min = 1 the MLE was derived by Seal and by Goldstein et al. Log-likelihood and its derivative:
$$\mathcal L=\ln\prod_{i=1}^n\frac{x_i^{-\alpha}}{\zeta(\alpha,x_{\min})}=-n\ln\zeta(\alpha,x_{\min})-\alpha\sum_{i=1}^n\ln x_i\tag{B.8}$$
$$\frac{-n}{\zeta(\alpha,x_{\min})}\frac{\partial}{\partial\alpha}\zeta(\alpha,x_{\min})-\sum_{i=1}^n\ln x_i=0\tag{B.9}$$
so α̂ solves
$$\frac{\zeta'(\hat\alpha,x_{\min})}{\zeta(\hat\alpha,x_{\min})}=-\frac1n\sum_{i=1}^n\ln x_i\tag{B.10}$$
This is solved numerically, or one maximizes (B.8) directly. Consistency and asymptotic efficiency can be proved by applying Theorems B.1 and B.3. The calculations are omitted (see ref. [7]).

**B.4 Approximate discrete estimator (p. 36).** Expand the integral of a smooth f over a unit interval:
$$\int_{x-1/2}^{x+1/2}f(t)\,dt=F(x+\tfrac12)-F(x-\tfrac12)=f(x)+\tfrac1{24}f''(x)+\dots\tag{B.11}$$
(Taylor series of F: the even-order terms F and F″ cancel, the odd terms double, and F′ = f gives f + f″/24 (added step); coefficients ½, 1/8, 1/48 as printed.) Summing over integer x:
$$\int_{x_{\min}-1/2}^{\infty}f(t)\,dt=\sum_{x=x_{\min}}^{\infty}f(x)+\frac1{24}\sum_{x=x_{\min}}^\infty f''(x)+\dots\tag{B.12}$$
For $f=x^{-\alpha}$:
$$\int_{x_{\min}-1/2}^\infty t^{-\alpha}dt=\frac{(x_{\min}-\frac12)^{-\alpha+1}}{\alpha-1}=\sum_{x}x^{-\alpha}+\frac{\alpha(\alpha+1)}{24}\sum_x x^{-\alpha-2}+\dots=\zeta(\alpha,x_{\min})\big[1+O(x_{\min}^{-2})\big]\tag{B.13}$$
using x⁻² ≤ x_min⁻² in the second sum. Hence
$$\zeta(\alpha,x_{\min})=\frac{(x_{\min}-\frac12)^{-\alpha+1}}{\alpha-1}\big[1+O(x_{\min}^{-2})\big]\tag{B.14}$$
$$\zeta'(\alpha,x_{\min})=-\frac{(x_{\min}-\frac12)^{-\alpha+1}}{\alpha-1}\Big[\frac1{\alpha-1}+\ln(x_{\min}-\tfrac12)\Big]\big[1+O(x_{\min}^{-2})\big]\tag{B.15}$$
$$\frac{\zeta'(\hat\alpha,x_{\min})}{\zeta(\hat\alpha,x_{\min})}=-\Big[\frac1{\hat\alpha-1}+\ln(x_{\min}-\tfrac12)\Big]\big[1+O(x_{\min}^{-2})\big]\tag{B.16}$$
Neglecting O(x_min⁻²) relative to O(1), and combining with (B.10) (added step: $\frac1{\hat\alpha-1}=\frac1n\sum\ln x_i-\ln(x_{\min}-\frac12)$):
$$\hat\alpha\simeq1+n\left[\sum_{i=1}^n\ln\frac{x_i}{x_{\min}-\frac12}\right]^{-1}\tag{B.17}$$
This equals the continuous MLE except for the −½ in the denominator. Numerical comparison with (B.10) shows it is a good approximation when x_min ≳ 6 (p. 37). **Fig. B.1 (p. 34):** the error decays as O(x_min⁻²) and falls below 1% of α for x_min ≳ 6.

*Skip path:* carry forward (B.4) for continuous data and (B.17) for discrete data with x_min ≳ 6.

### Appendix C. Likelihood ratio tests (pp. 37–38)
For two candidate densities p₁, p₂: $L_j=\prod_i p_j(x_i)$ \tag{C.1}, and
$$R=\frac{L_1}{L_2}=\prod_{i=1}^n\frac{p_1(x_i)}{p_2(x_i)}\tag{C.2}$$
$$\mathcal R=\sum_{i=1}^n\big[\ln p_1(x_i)-\ln p_2(x_i)\big]=\sum_{i=1}^n\big[\ell^{(1)}_i-\ell^{(2)}_i\big]\tag{C.3}$$
with $\ell_i^{(j)}=\ln p_j(x_i)$. Since the xᵢ are independent, so are the differences, and by the central limit theorem ℛ is normal for large n, with variance nσ². The variance is estimated by
$$\sigma^2=\frac1n\sum_{i=1}^n\Big[\big(\ell_i^{(1)}-\ell_i^{(2)}\big)-\big(\bar\ell^{(1)}-\bar\ell^{(2)}\big)\Big]^2\tag{C.4}$$
$$\bar\ell^{(1)}=\frac1n\sum_i\ell^{(1)}_i,\qquad\bar\ell^{(2)}=\frac1n\sum_i\ell^{(2)}_i\tag{C.5}$$
The worry is that the true expected log ratio is zero, so the observed sign comes only from fluctuations. The probability of a magnitude at least |ℛ| is
$$p=\frac1{\sqrt{2\pi n\sigma^2}}\Big[\int_{-\infty}^{-|\mathcal R|}e^{-t^2/2n\sigma^2}dt+\int_{|\mathcal R|}^\infty e^{-t^2/2n\sigma^2}dt\Big]=\big|\operatorname{erfc}(\mathcal R/\sqrt{2n}\,\sigma)\big|\tag{C.6}$$
$$\operatorname{erfc}(z)=1-\operatorname{erf}(z)=\frac2{\sqrt\pi}\int_z^\infty e^{-t^2}dt\tag{C.7}$$
- If p is small (say p < 0.1), the sign of ℛ can probably be trusted as showing which model fits better. This does not mean the winner is a good fit. If p is large, the test cannot discriminate (p. 38).
- Footnote 12: a small p is "good" here, since it makes the test trustworthy, but "bad" in the KS test, where it means a poor fit (p. 38).
- *Subtlety.* Both models are fitted to the same data. Vuong showed the results still hold if p₁ and p₂ come from distinct, non-nested families and estimation is by maximum likelihood within each family. Some additional technical conditions are said to hold for all models used here (p. 38).
- **C.1 Nested hypotheses (p. 38).** If the true distribution lies in the smaller family, both fits converge to it. The differences ℓ⁽¹⁾−ℓ⁽²⁾ and σ² then go to zero, the ratio |ℛ|/σ tends to 0/0, and the argument above fails. A refined analysis gives a chi-squared distribution for ℛ at large n. A small resulting p-value rules out the smaller family. Otherwise one can only say there is no evidence the larger family is needed, and it is not ruled out either.

*Intuition note.* The test asks whether the average per-point advantage of one model is large compared with its own scatter. The resulting p-value says how far to trust the sign, not whether either model is good.

### Appendix D. Generating power-law random numbers (pp. 38–41)
**Continuous (p. 39).** Take uniform r in [0,1). The densities relate by
$$p(x)=p(r)\frac{dr}{dx}=\frac{dr}{dx}\tag{D.1}$$
(since p(r) = 1). Integrating,
$$P(x)=\int_x^\infty p(x')dx'=\int_r^1dr'=1-r\tag{D.2}$$
$$x=P^{-1}(1-r)\tag{D.3}$$
For the power law, using P(x) from Eq. (2.6) of the main text,
$$x=x_{\min}(1-r)^{-1/(\alpha-1)}\tag{D.4}$$
(Added check: $P(x)=(x/x_{\min})^{-(\alpha-1)}=1-r$ gives (D.4).) The method needs a closed-form inverse of P, which does not exist for every distribution.

**Table D.1 (p. 40):**
- Exponential: $x=x_{\min}-\frac1\lambda\ln(1-r)$.
- Stretched exponential: $x=[x_{\min}^\beta-\frac1\lambda\ln(1-r)]^{1/\beta}$.
- Log-normal: $\rho=\sqrt{-2\sigma^2\ln(1-r_1)}$, $\theta=2\pi r_2$, $x_1=\exp(\rho\sin\theta)$, $x_2=\exp(\rho\cos\theta)$, giving two independent numbers from two uniforms.
- Power law with cut-off: no closed form. Draw an exponential variate, accept with probability $p=(x/x_{\min})^{-\alpha}$, else repeat.

**Discrete (pp. 39–40).** The equivalent condition is
$$P(x)=\sum_{x'=x}^\infty p(x')=1-r\tag{D.5}$$
P(x) (Eq. 2.7 of the main text) cannot be inverted in closed form. Instead:
1. Start with $x_2\leftarrow x_{\min}$.
2. Repeat $x_1\leftarrow x_2$, $x_2\leftarrow 2x_1$ until $P(x_2)<1-r$ ("doubling up").
3. Binary search inside the bracket until $k\le x<k+1$, then discard the fraction.

Zeta values can be slow, so the first few thousand may be precomputed, since tail values are needed rarely.

**Approximation (p. 40).** Generate continuous reals $y\ge x_{\min}-\frac12$ and round to the nearest integer:
$$x=\Big\lfloor(x_{\min}-\tfrac12)(1-r)^{-1/(\alpha-1)}+\tfrac12\Big\rfloor\tag{D.6}$$
The error is largest at x = x_min:
$$\Delta p=1-\Big(\frac{x_{\min}+\frac12}{x_{\min}-\frac12}\Big)^{-\alpha+1}-\frac{x_{\min}}{\zeta(\alpha,x_{\min})}\tag{D.7}$$
For α = 2.5 the error on p(x) is above 8% at x_min = 1, below 1% at x_min = 5, and below 0.2% at x_min = 10. Truncating (rounding down) is substantially poorer and should not be used.

**Table D.2 (p. 41).** For α = 2.5, x_min = 5 and 100 000 generated numbers, generated and theoretical CDFs agree to within small statistical fluctuations. Example at x = 10: continuous theory 0.354 vs generated 0.352. Discrete theory 0.328, generated 0.325, approximation 0.325. The approximate generator has somewhat larger errors but is adequate for many uses (p. 41).

## Toy example (ours, not from the text)
**Continuous MLE.** Take x_min = 1 and data 1, 2, 4, 8 (n = 4). Then ln(xᵢ/x_min) = 0, 0.693, 1.386, 2.079, with sum 4.159. By (B.4): α̂ = 1 + 4/4.159 = 1 + 0.962 = 1.962. By Prop. B.4 the standard error is (α̂−1)/√n = 0.962/2 = 0.48. So with four points the estimate is very uncertain.

**Generating a number.** For α = 2.5, x_min = 1, r = 0.75, (D.4) gives x = (0.25)^{−1/1.5} = 4^{2/3} = 2^{4/3} ≈ 2.52. Check: P(2.52) = 2.52^{−1.5} = 1/4.0 = 0.25 = 1 − r.

**Likelihood-ratio p-value.** Suppose n = 100, σ = 1, ℛ = 10. Then √(2n)σ = 14.14, the argument is 0.707, and erfc(0.707) = 1 − 0.683 = 0.317. Since p > 0.1, the sign of ℛ cannot be trusted.

## Concepts
- [[heavy-tail-power-law]] — here a distribution p(x) ∝ x^−α above x_min. Evidence beyond a straight log-log line is required (pp. 26, 31)
- [[maximum-likelihood-estimator]] (new) — α̂ maximizing the log-likelihood. For the continuous power law it is (B.4), equivalent to the Hill estimator (pp. 32–33)
- [[fisher-information-cramer-rao]] (new) — I(α) sets the lower bound 1/nI on the variance of unbiased estimators. The MLE attains it asymptotically (pp. 33–34)
- [[likelihood-ratio-test]] (new) — a test of the sign of ℛ against a null of zero expected value. The p-value measures trust in the sign, not goodness of fit (pp. 37–38)
- [[nested-vs-non-nested-models]] (new) — when the true distribution lies in the smaller of two nested families, ℛ becomes chi-squared rather than normal (p. 38)
- [[power-law-with-cutoff]] (new) — power law with a modified, exponentially cut extreme tail. Often favoured over the pure form in these data (pp. 26, 30)
- [[log-log-regression-pitfalls]] (new) — least-squares fits to log histograms or CDFs: biased slopes, wrong errors, uninformative r², unnormalized (pp. 31–32)
- [[inverse-transform-sampling]] (new) — generating x = P⁻¹(1−r) from uniform r. Discrete case by doubling and binary search (pp. 38–40)
- [[robustness-and-fragility]] — not used here. Skipped.

## Canonical instances
- [[word-frequency-moby-dick]] — the only "good" power law of 24 data sets (pp. 24, 29)
- [[citation-counts-1981]] — α̂ = 3.16 ± 0.06, incompatible with earlier 2.9 and 2.5 (p. 23)
- [[protein-interaction-degree]] — α̂ = 3.1 ± 0.3 versus reported 2.44 (p. 23)
- [[earthquake-intensities]] — power law ruled out; the stretched exponential is strongly favoured and the cut-off form helps (pp. 26, 28, 30)
- [[wealth-and-http-sizes]] — poor power-law fits that still beat the tested alternatives, so none fits well (pp. 23, 25)

## Bridges (candidates)
- [same-math] MLE of the power-law exponent (Hill estimator) ↔ extreme-value statistics: tail-index estimation — the text states the equivalence to Hill (p. 32).
- [same-math] Inverse-CDF sampling (D.3) ↔ simulation of any 1-D random variable — the same transformation.
- [structural-analogy] Likelihood-ratio test between non-nested models ↔ model selection in agent-based/many-model work — rival generative models compared on one data set.
- [metaphor] "Wishful thinking" about straight lines ↔ pattern-seeking in complexity science.

## Questions this raises
- If log-normal and power law are practically indistinguishable, which mechanisms should we use to choose between them?
- How should the x_min estimate and α̂ coupling corrections be handled in small samples?
- What does a "good" power-law rating imply when the data come from biased subsamples of larger systems?
- Can the same pipeline be extended to non-power-law alternatives, as the authors suggest?

## Reading notes
- This unit is part 2 of 2. It starts mid-Section 6 with data-set item (m) (p. 23) and ends at the reference list (p. 43). It covers the data-set results (Tables 6.1–6.3), Section 7, and Appendices A–D. Printed page = pdf page.
- Table 6.1 prints p = 0.05 for fires (not bold), yet the text lists fires among the seven data sets ruled out (pp. 23, 27).
- Prop. B.4 proof (p. 33): the ratio of the third to the second derivative is negative as computed (−2(α₂−1)²/(α₁−1)³). The paper prints it without the minus sign. This does not affect boundedness.
- Eq. (C.6) is printed as |erfc(ℛ/√(2n)σ)|. The integrals show the intended value is erfc(|ℛ|/√(2n)σ) (added step).
- Eq. (D.1) is printed as dr/dx, though r decreases as x increases. Taken as printed.
- Dot-like artifacts in the integrals (e.g. "t.") come from the text layer. In the page images the differentials appear with a dot-like mark (e.g. "ṭ" for dt); they are read here as ordinary differentials d.
- Eq. (A.1) is printed as log p(x) = α log x + c although p(x) ∼ x^−α (so the slope would be −α). Taken as printed (p. 31).
