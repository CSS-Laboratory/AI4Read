---
id: clauset-2009-powerlaw/main-p1
work: clauset-2009-powerlaw
unit: "paper (part 1/2): Sections 1–5 and the start of Section 6"
pages: 1–22
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Power-Law Distributions in Empirical Data (part 1: method, tests, and start of applications)

## L0 — One line
The paper proposes a three-step recipe for recognising a power law: fit $x_{\min}$ and $\alpha$ by maximum likelihood plus Kolmogorov–Smirnov (KS) minimisation, test plausibility with a Monte Carlo $p$-value, and compare the fit with alternative distributions by a likelihood ratio test. A straight line on a log-log plot is not enough.

## L1 — The gist (≤ 120 words)
Power-law claims are often made by fitting a straight line to a log-log histogram. This can give badly biased exponents, and it does not say whether a power law is a good model at all. This part builds a recipe. Estimate $x_{\min}$ and $\alpha$ by maximum likelihood and KS minimisation. Test plausibility with a Monte Carlo $p$-value. Compare against alternative distributions with a likelihood ratio test. Synthetic tests support the individual steps and show that regression methods can mislead. It matters because a roughly straight log-log plot is necessary but not sufficient evidence. The part ends where the 24 real data sets are introduced.

**Prerequisites:** probability densities and CDFs; logarithms and log-log plots; likelihood and maximum-likelihood estimation; $p$-values and hypothesis testing; simple Monte Carlo sampling.

## L2 — Key ideas
- Power-law behaviour usually holds only above some $x_{\min}$ (the "tail"). Fitting needs both $\alpha$ and $x_{\min}$, and we can rarely be certain a quantity is power-law distributed; we can only say the data are consistent with it (p. 2).
- In the synthetic tests, least-squares fits on log-log histograms were significantly biased. CDF fits were the possible exception: biased for discrete data but reasonably good for continuous data. Where an estimate was biased, its error bar gave no warning. Maximum likelihood estimators (MLEs) were accurate when the estimator matched the data type, discrete or continuous (pp. 5, 8).
- The paper recommends choosing $\hat x_{\min}$ by minimising the KS distance between data and fitted power law. The alternative based on the Bayesian information criterion (BIC) tended to underestimate $x_{\min}$ (pp. 11–13).
- Fitting always returns some power law. Plausibility needs a goodness-of-fit $p$-value from synthetic data sets, each re-fitted on its own (pp. 14–17).
- A large $p$ does not prove a power law. Other distributions may fit equally well, and small $n$ makes rejection hard (pp. 17–18).
- A likelihood ratio test with Vuong's $p$-value compares two models and also says when the data cannot decide. Using $p$ greatly lowers misclassification (pp. 19–22).
- Tests can rule out specific alternatives but cannot show absolutely that the power law is correct; the researcher must supply reasonable hypotheses (pp. 18–19).

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 1–2)
- Power laws are hard to detect because of large fluctuations in the tail (large but rare events) and because the range of power-law behaviour is hard to identify (p. 1).
- Least-squares fitting can give substantially inaccurate parameters, and even when accurate it does not tell whether data obey a power law at all (p. 1).
- The proposed framework combines maximum-likelihood fitting with goodness-of-fit tests (KS statistic) and likelihood ratios. It is tested on synthetic data and on 24 real data sets (p. 1).
- Motivation: many quantities cluster around a typical value, so mean and standard deviation describe them. Adult male height is about 180 cm, with extremes about a factor of two from the mean. Quantities such as city populations, earthquake intensities and power-outage sizes are *thought* to follow power laws and are not described well by averages (pp. 1–2).
- Example: the 2000 US Census mean city/town population is 8226. This is not useful, because a significant fraction of people live in cities several orders of magnitude larger (p. 2).
- Definition: $x$ obeys a power law if drawn from
$$p(x)\propto x^{-\alpha}\tag{1.1}$$
with $\alpha$ the *exponent* or *scaling parameter*. It typically lies in $2<\alpha<3$, with occasional exceptions (p. 2).
- Few empirical phenomena obey a power law for all $x$; more often the power law applies only above $x_{\min}$, and then the authors say the tail of the distribution follows a power law (p. 2).
- The authors say we can rarely, if ever, be certain data are power-law drawn; we can say they are consistent with it and sometimes rule out competitors (p. 2).
- Claims about the data sets: several cannot reasonably be considered power laws; for others the power-law hypothesis appears to be a good one, or at least is not firmly ruled out (p. 2).

### 2. Definitions (pp. 2–4)
- **Continuous case.** The density satisfies
$$p(x)\,\Delta x=\Pr(x\le X<x+\Delta x)=Cx^{-\alpha}\Delta x \tag{2.1}$$
The density diverges as $x\to0$, so a lower bound $x_{\min}$ is needed. For $\alpha>1$ (p. 2):
$$p(x)=\frac{\alpha-1}{x_{\min}}\left(\frac{x}{x_{\min}}\right)^{-\alpha}\tag{2.2}$$
- **Discrete case** (integers only):
$$p(x)=\Pr(X=x)=Cx^{-\alpha}\tag{2.3}$$
$$p(x)=\frac{x^{-\alpha}}{\zeta(\alpha,x_{\min})}\tag{2.4}$$
$$\zeta(\alpha,x_{\min})=\sum_{n=0}^{\infty}(n+x_{\min})^{-\alpha}\tag{2.5}$$
The last is the generalized (Hurwitz) zeta function (p. 3).
- **CDF.** Here $P(x)=\Pr(X\ge x)$ is the *complementary* cumulative distribution function. In the continuous and discrete cases (p. 3):
$$P(x)=\int_x^\infty p(x')\,dx'=\left(\frac{x}{x_{\min}}\right)^{-\alpha+1}\tag{2.6}$$
$$P(x)=\frac{\zeta(\alpha,x)}{\zeta(\alpha,x_{\min})}\tag{2.7}$$
- **Table 2.1** (p. 4) gives $p(x)=Cf(x)$, normalised on $x\ge x_{\min}$:

| type | name | $f(x)$ | $C$ |
|---|---|---|---|
| cont. | power law | $x^{-\alpha}$ | $(\alpha-1)x_{\min}^{\alpha-1}$ |
| cont. | power law with cutoff | $x^{-\alpha}e^{-\lambda x}$ | $\lambda^{1-\alpha}/\Gamma(1-\alpha,\lambda x_{\min})$ |
| cont. | exponential | $e^{-\lambda x}$ | $\lambda e^{\lambda x_{\min}}$ |
| cont. | stretched exponential | $x^{\beta-1}e^{-\lambda x^{\beta}}$ | $\beta\lambda e^{\lambda x_{\min}^{\beta}}$ |
| cont. | log-normal | $\frac1x\exp\!\big[-\frac{(\ln x-\mu)^2}{2\sigma^2}\big]$ | $\sqrt{\tfrac{2}{\pi\sigma^2}}\big[\operatorname{erfc}\big(\tfrac{\ln x_{\min}-\mu}{\sqrt2\sigma}\big)\big]^{-1}$ |
| disc. | power law | $x^{-\alpha}$ | $1/\zeta(\alpha,x_{\min})$ |
| disc. | Yule | $\Gamma(x)/\Gamma(x+\alpha)$ | $(\alpha-1)\,\Gamma(x_{\min}+\alpha-1)/\Gamma(x_{\min})$ |
| disc. | exponential | $e^{-\lambda x}$ | $(1-e^{-\lambda})e^{\lambda x_{\min}}$ |
| disc. | Poisson | $\mu^x/x!$ | $\big[e^{\mu}-\sum_{k=0}^{x_{\min}-1}\mu^k/k!\big]^{-1}$ |

- **Continuous approximation of discrete data.** Several approximations exist; some are reasonable and others are not. Treating integers as continuous power-law values *rounded to the nearest integer* is relatively reliable. Truncation (rounding down), or assuming discrete and continuous probabilities are proportional, give poor results and should be avoided (p. 4).

### Box 1: the recipe (p. 3)
1. Estimate $x_{\min}$ and $\alpha$ (Section 3).
2. Compute a goodness-of-fit $p$-value (Section 4). If $p>0.1$ the power law is plausible; otherwise it is rejected.
3. Compare with alternatives by a likelihood ratio test (Section 5). If the ratio is significantly different from zero, its sign says which model is favoured.

Step 3 could be replaced by Bayesian, cross-validation or minimum-description-length methods, which are not described here (p. 3).

### 3. Fitting power laws to empirical data (pp. 4–14)
- **Common practice.** Taking logs of (1.1) gives $\ln p(x)=-\alpha\ln x+\text{constant}$, a straight line on a doubly logarithmic plot. The usual method is a least-squares fit to the log of a histogram, with $\alpha$ read off as the absolute slope. This goes back to Pareto. The authors say it produces significant systematic errors under relatively common conditions (details in Appendix A, not in this part), so, the authors conclude, its results cannot be trusted (pp. 4–5).

*Note on a printed slip:* the source writes "$\ln p(x)=\alpha\ln x+$ constant" (p. 4). Given $p\propto x^{-\alpha}$, the slope is $-\alpha$; the authors then use the absolute slope.

#### 3.1 Estimating the scaling parameter (pp. 5–7)
- Assume $x_{\min}$ is known for now. Maximum likelihood is the method of choice for fitting such models; it provably gives accurate estimates in the limit of large samples (p. 5).
- **Continuous MLE** (hatted symbols are estimates), with $x_i\ge x_{\min}$, $i=1\dots n$ (p. 5):
$$\hat\alpha=1+n\left[\sum_{i=1}^{n}\ln\frac{x_i}{x_{\min}}\right]^{-1}\tag{3.1}$$
This equals the Hill estimator, which is asymptotically normal and consistent. The standard error, from the width of the likelihood maximum, is
$$\sigma=\frac{\hat\alpha-1}{\sqrt n}+O(1/n)\tag{3.2}$$
with a positive higher-order correction (p. 5).
- The authors assume $\alpha>1$: distributions with $\alpha\le1$ are not normalisable. A bounded range would need different estimators (p. 5).
- **Discrete MLE.** For $x_{\min}=1$, $\hat\alpha$ solves
$$\frac{\zeta'(\hat\alpha)}{\zeta(\hat\alpha)}=-\frac1n\sum_{i=1}^n\ln x_i\tag{3.3}$$
For $x_{\min}>1$ the zetas become generalized zetas, with the prime meaning differentiation in the first argument:
$$\frac{\zeta'(\hat\alpha,x_{\min})}{\zeta(\hat\alpha,x_{\min})}=-\frac1n\sum_{i=1}^n\ln x_i\tag{3.4}$$
This is solved numerically. Alternatively, maximise the log-likelihood directly (pp. 5–6):
$$\mathcal L(\alpha)=-n\ln\zeta(\alpha,x_{\min})-\alpha\sum_{i=1}^n\ln x_i\tag{3.5}$$
- **Discrete standard error.** Use a quadratic approximation of the log-likelihood at its maximum and take the standard deviation of the resulting Gaussian:
$$\sigma=\frac{1}{\sqrt{n\left[\dfrac{\zeta''(\hat\alpha,x_{\min})}{\zeta(\hat\alpha,x_{\min})}-\left(\dfrac{\zeta'(\hat\alpha,x_{\min})}{\zeta(\hat\alpha,x_{\min})}\right)^{2}\right]}}\tag{3.6}$$
Eq. (3.2) gives roughly similar results for reasonably large $n$ and $x_{\min}$ (p. 6).
- **Approximate discrete estimator** (from the rounding approximation; derivation in Appendix B, not in this part):
$$\hat\alpha\simeq1+n\left[\sum_{i=1}^n\ln\frac{x_i}{x_{\min}-\tfrac12}\right]^{-1}\tag{3.7}$$
In the authors' experiments it is accurate to about 1% or better provided $x_{\min}\gtrsim6$ (p. 6).
- Applying the continuous MLE (3.1) to discrete data is "significantly less accurate" than (3.7) and no easier, so they see no reason to use it. Footnote 2: its error decays as $O(x_{\min}^{-1})$, versus $O(x_{\min}^{-2})$ for (3.7). Typical $\alpha$ needs $x_{\min}\gtrsim100$ for 1% accuracy with (3.1), versus $x_{\min}\gtrsim6$ for (3.7) (pp. 6–7).

*Intuition note.* Eq. (3.1) uses only the average of $\ln(x_i/x_{\min})$. A heavier tail means larger logs and a smaller $\hat\alpha$. The standard error shrinks like $1/\sqrt n$.

#### 3.2 Performance of the estimators (pp. 7–8)
- The MLE gives no warning if the data are not power-law distributed; it only returns the best power-law fit (p. 7).
- Test: synthetic continuous and discrete data, $\alpha=2.5$, $x_{\min}=1$, $n=10\,000$. Estimates were $\hat\alpha=2.50(2)$ (continuous) and $2.49(2)$ (discrete), with the digit in parentheses the uncertainty in the last digit (p. 7).
- Plots show $P(x)$ rather than $p(x)$, since the visual form of the CDF is more robust to finite-sample fluctuations, especially in the tail (pp. 7–8).
- **Table 3.1** (LS = least squares on the log of the probability; PDF binned with constant width 0.1 or up to 500 logarithmic bins; CDF from a constant-width histogram or from rank-frequency; p. 8):

| method | notes | est. $\alpha$ (discrete) | est. $\alpha$ (continuous) |
|---|---|---|---|
| LS + PDF | const. width | 1.5(1) | 1.39(5) |
| LS + CDF | const. width | 2.37(2) | 2.480(4) |
| LS + PDF | log. width | 1.5(1) | 1.19(2) |
| LS + CDF | rank-freq. | 2.570(6) | 2.4869(3) |
| cont. MLE | – | 4.46(3) | **2.50(2)** |
| disc. MLE | – | **2.49(2)** | 2.19(1) |

  - Bold marks the accurate estimates. For the discrete MLE on continuous data, the non-integer part was discarded (p. 8).
  - The regression methods are significantly biased. The possible exception (the text says 'except perhaps') is the CDF fits, which are biased for discrete data but do reasonably well for continuous data. Where biased, the error estimate gives no warning (p. 8).
  - Fig. 3.2 caption: as $\alpha$ varies, among the four methods plotted only the discrete MLE is accurate for discrete data and only the continuous MLE for continuous data (p. 9).
- **Finite samples.** The MLEs are guaranteed unbiased only as $n\to\infty$. For finite $n$ the bias decays as $O(n^{-1})$ while the statistical error decays as $O(n^{-1/2})$. A rule of thumb is $n\gtrsim50$ for reliable estimates, about 1% accuracy in the Fig. B.2 examples. Small samples also make it hard to rule out alternatives, and a power law may look good even when the data are not power-law (p. 8).

#### 3.3 Estimating the lower bound $x_{\min}$ (pp. 9–13)
- Samples below $x_{\min}$ are discarded before estimating $\alpha$, so that only data for which the power-law model is valid remain. If $x_{\min}$ is too low, $\hat\alpha$ is biased. If it is too high, legitimate data are thrown away, which raises statistical error and finite-size bias (p. 9).
- Fig. 3.3: mean $\hat\alpha$ over 5000 data sets ($n=2500$, test distribution (3.10), $\alpha=2.5$, true $x_{\min}=100$) versus assumed $x_{\min}$. It is accurate at the true value, deviates rapidly below it and more slowly above it. Erring a little high is probably acceptable; too low could be severe (pp. 9–10).
- Common approaches are visual: find where the plot becomes straight, or where $\hat\alpha(\hat x_{\min})$ is stable. These are subjective and noise-sensitive. Two objective methods are reviewed (p. 10).
- **Method 1: BIC (Handcock–Jones; discrete data only).**
  - Below $\hat x_{\min}$, each of the $\hat x_{\min}-1$ values $k$ gets its own probability $p_k$, whose MLE is the fraction of observations equal to $k$ (p. 10).
  - Plain likelihood cannot be maximised over $x_{\min}$, since the parameter count changes and likelihood would grow as $x_{\min}\to\infty$. Instead, maximise the marginal likelihood (evidence): the likelihood integrated over parameter values. Schwarz showed that for large $n$ it is approximated by (pp. 10–11)
$$\ln\Pr(x\mid x_{\min})\simeq\mathcal L-\tfrac12x_{\min}\ln n\tag{3.8}$$
  - Here $\mathcal L$ is the maximum conventional log-likelihood. This is a Bayesian information criterion (BIC), and the maximiser over $x_{\min}$ is $\hat x_{\min}$ (p. 11).
  - Weaknesses: $x_{\min}-1$ parameters below $x_{\min}$ may be excessive, so BIC tends to underestimate $x_{\min}$. It is also unclear how to generalise BIC to continuous data (p. 11).
- **Method 2: KS minimisation (Clauset et al.; discrete or continuous).** Choose the $\hat x_{\min}$ that makes the data and best-fit power law as similar as possible above $\hat x_{\min}$. Too high a choice shrinks the data and fluctuations dominate; too low a choice leaves a genuine model mismatch. The KS statistic is
$$D=\max_{x\ge x_{\min}}|S(x)-P(x)|\tag{3.9}$$
where $S(x)$ is the empirical CDF of observations $\ge x_{\min}$ and $P(x)$ is the CDF of the best-fit power law for $x\ge x_{\min}$. $\hat x_{\min}$ is the $x_{\min}$ minimising $D$ (p. 11).
- For right-skewed data, most of the data and CDF range lie near $x_{\min}$, so the method is especially sensitive to deviations there (p. 12).

*Intuition note.* BIC penalises extra parameters so that a flexible below-$x_{\min}$ model does not always win. KS minimisation instead asks above which cut-off the tail looks most like the fitted power law, with no parameter-count issue.

#### 3.4 Tests of the $x_{\min}$ estimates (pp. 12–14)
- Test distribution, $\alpha=2.5$ (power law above $x_{\min}$, exponential below, continuous slope at $x_{\min}$; a challenging test):
$$p(x)=\begin{cases}C(x/x_{\min})^{-\alpha}&x\ge x_{\min}\\ Ce^{-\alpha(x/x_{\min}-1)}&x<x_{\min}\end{cases}\tag{3.10}$$
- Fig. 3.4b ($n=50\,000$, discrete): KS recovers the true $x_{\min}$ well; BIC tends to underestimate it. Continuous data behave similarly, with KS slightly more conservative (larger $\hat x_{\min}$). **Recommendation: use KS for general applications** (pp. 12–13).
- Results depend mainly on the tail size $n_{\rm tail}$. About 1000 or more tail observations gave good results here, but this depends on how sharply the non-power-law part departs. A more pronounced departure should make it easier (p. 13).
- For $p(x)=C(x+k)^{-\alpha}$ there is no $x_{\min}$ above which it is exactly a power law. KS gives estimates of $\alpha$ that "appear to be asymptotically consistent" ($\hat\alpha\to\alpha$ as $n\to\infty$). Rigorous guarantees remain an open question (p. 13).
- KS is relatively insensitive at the extremes of $x$ (the CDFs tend to 0 and 1). The reweighted version is
$$D^*=\max_{x\ge\hat x_{\min}}\frac{|S(x)-P(x)|}{\sqrt{P(x)(1-P(x))}}\tag{3.11}$$
The reweighted KS and Kuiper statistics give results very similar to standard KS. Anderson–Darling is highly conservative: $\hat x_{\min}$ too large by an order of magnitude or more. That reduces tail observations and hence the ability to validate the model (p. 13).
- **Uncertainty by bootstrap.** Generate a surrogate set of $n$ points drawn uniformly at random from the original data. Estimate $x_{\min}$ and $\alpha$ for it. Repeat (say 1000 times) and take the standard deviation of the estimates (pp. 13–14).

#### 3.5 Other techniques (p. 14)
- The statistics literature considers $p(x)\propto L(x)x^{-\alpha}$ (3.12) with $L$ slowly varying ($L(cx)/L(x)\to1$ for large $x$). Finding where $x^{-\alpha}$ dominates is tricky with limited dynamic range or if $|L(x)-L(\infty)|$ decays only a little faster than $x^{-\alpha}$. A common visual technique is the Hill plot ($\hat\alpha$ versus $x_{\min}$). Finance often just uses the largest $\sqrt n$ or $n/10$ observations (p. 14).
- The authors claim the KS method gives estimates at least as good, is simple and cheap enough to be a base for the $p$-value calculation, and yields a simple remaining functional form that can be tested for agreement (p. 14).

### 4. Testing the power-law hypothesis (pp. 14–18)
- Fitting says nothing about plausibility: a power law can always be fitted whatever the true distribution (p. 14).
- **Fig. 4.1a.** Three samples with $n=100$ and $x_{\min}=15$ (power law $\alpha=2.5$; log-normal $\mu=0.3$, $\sigma=2.0$; exponential $\lambda=0.125$) all look roughly straight on log-log axes. Straightness is "a necessary but not sufficient condition" (p. 15).
- Even data truly drawn from a power law will always deviate somewhat from the exact form because of random sampling. The task is to separate them from deviations caused by a non-power-law source (p. 15).
- Idea: sample many synthetic power-law data sets and measure their KS distances from the power-law form. If the empirical distance is much larger than typical synthetic ones, the power law is not plausible. Cautions: the result depends on the distance measure, and a non-power-law process may by chance produce a power-law-looking set. That chance dwindles with increasing $n$ (p. 15).

#### 4.1 Goodness-of-fit tests (pp. 15–18)
- The **$p$-value** is the fraction of synthetic distances larger than the empirical distance. $p$ near 1: the difference is attributable to fluctuation alone. $p$ small: the model is not plausible (p. 15).
- Footnote 7: the KS distribution is known for a *fixed* underlying distribution. It cannot be used here because the model is fitted to each data set. Hence the Monte Carlo procedure (pp. 15–16).
- **Procedure** (pp. 16–17):
  1. Fit the empirical data (Section 3) and compute the KS statistic.
  2. Generate many synthetic sets with $\hat\alpha$ and $\hat x_{\min}$ of the best fit.
  3. Fit each synthetic set *separately to its own* power law and compute its KS statistic relative to *that* fit, not relative to the generating distribution.
  4. $p$ = fraction of synthetic KS values larger than the empirical value.
  - Step 3 ensures the same calculation is done on real and synthetic data, "a crucial requirement" for an unbiased $p$ (p. 17).
- **Semiparametric generation.** Let $n_{\rm tail}$ be the number of observations $\ge x_{\min}$ out of $n$ in total. For each of $n$ points, with probability $n_{\rm tail}/n$ draw from a power law with $\hat\alpha$ and $x\ge x_{\min}$. Otherwise pick uniformly at random one observed element with $x<x_{\min}$. The synthetic set follows a power law above $x_{\min}$ and has the observed distribution below (p. 17).
- **Number of synthetic sets.** To have $p$ accurate to about $\epsilon$, use at least $\tfrac14\epsilon^{-2}$ sets. For $\epsilon=0.01$ (two decimal digits) this is about 2500. The paper's applications used 1000 to 10 000 (p. 17).
- **Decision rule.** The authors take a conservative choice: reject the power law if $p\le0.1$. The more lenient $p\le0.05$ would let through candidates with a very small chance of following a power law. The rule must depend on the investigator's judgment (p. 17). Footnote 8: unlike experiments that quote a $p$-value for a null model, here the model to be verified is the hypothesis tested, so high $p$ is "good" (p. 17).
- A large $p$ does not necessarily mean the power law is correct, for at least two reasons. Other distributions may match equally well or better. And for small $n$ the data may follow a power law closely even if it is the wrong model. This is not a deficiency of the method; it is genuinely harder to rule the power law out with little data (pp. 17–18).

*Intuition note.* The $p$-value asks: if the data really were a power law with these fitted parameters, how often would a random data set look at least this far from its own best-fit power law? Because every synthetic set is re-fitted, the test accounts for the fact that we fitted the parameters.

#### 4.2 Performance of the goodness-of-fit test (p. 18)
- Fig. 4.1b: average $p$ versus $n$ for the three distributions. For $n\lesssim100$ all three have $p$ above 0.1, so the power law is not ruled out; there is not enough data. For larger $n$ the $p$-values of the log-normal and exponential data fall towards zero while the power-law data stay above the threshold (pp. 16, 18).
- Because the fit uses only the tail above $x_{\min}$, a larger $x_{\min}$ means fewer usable points and a larger total $n$ needed to reject. Fig. 4.1c shows the $n$ needed to reach $p=0.1$ for log-normal and exponential data as a function of $x_{\min}$ (p. 18).

### 5. Alternative distributions (pp. 18–22)
- One could compute a $p$-value for a competing distribution (e.g. the exponential, fitted with the analogue of Section 3, using the same Monte Carlo test). If the power law's $p$ is high and the competitors' are small, the competition is ruled out and the case for the power law is strengthened, though not proven (p. 18).
- Not every alternative can be tested. With enough parameters some family will almost always fit better. Statistical tests rule out specific hypotheses, but "it is up to the researcher to decide what a reasonable hypothesis is in the first place" (p. 19).

#### 5.1 Direct comparison: the likelihood ratio test (pp. 19–20)
- Normally a goodness-of-fit test has already been run for the power law: if it fails, the work is done; if it passes, the main concern is whether another distribution fits better. The likelihood ratio test computes the likelihood of the data under both models. $R$, the log of the ratio, is positive or negative depending on which is better, and zero for a tie (p. 19).
- The sign of $R$ alone is not definitive because of statistical fluctuation. If the true expected value of $R$ is near zero, the sign can flip. To judge, one needs its standard deviation $\sigma$, estimated by Vuong's method. This gives a $p$-value for the sign of $R$ (p. 19).
- Small $p$ (say $p<0.1$): the sign is a reliable indicator of the better model. Large $p$: the test favours neither model. This is an advantage: it can say when the data are insufficient. The goodness-of-fit test gives no equivalent indication (pp. 19–20).
- Footnote 10: if one extrapolates a fit far into the tail (e.g. frequencies of major earthquakes), conclusions from different fitted forms can differ enormously even when they are indistinguishable in the observed range. Footnote 11: the Bayesian approach of Ref. [60] is essentially equivalent to the likelihood ratio test but lacks a $p$-value to show when results are significant (p. 20).
- Technical details are in Appendix C (not in this part).

#### 5.2 Nested hypotheses (p. 20)
- Distributions are *nested* if one family is a subset of the other, e.g. power law and power law with exponential cutoff. The larger family always fits at least as well, so a slightly modified likelihood ratio test is needed (Appendix C) (p. 20).

#### 5.3 Performance of the likelihood ratio test (pp. 20–22)
- Synthetic data: continuous power law ($\alpha=2.5$, $x_{\min}=1$) and a log-normal ($\mu=0.3$, $\sigma=2$) constrained to positive $x$. For each of 1000 repetitions, estimate $x_{\min}$, compute the ratio above $x_{\min}$ and its $p$-value. The normalised ratio $n^{-1/2}R/\sigma$ is used; the $p$-value follows from it via Eq. (C.6) (pp. 20–21).
- Fig. 5.1: the normalised ratio becomes increasingly positive with $n$ for true power-law data, and increasingly negative for log-normal data (p. 21).
- If classification uses only the sign of $R$, misclassification (Fig. 5.2a) falls with $n$ but is "uncomfortably large" for moderate $n$. Using $p$ with three outcomes (power law, log-normal, undecided) gives misclassification of a few parts per thousand even for modest $n$ (Fig. 5.2b). The caption counts errors with the wrong sign and $p<0.05$. So $p$ effectively flags insufficient data (pp. 21–22).

*Intuition note.* The likelihood ratio compares two fitted models directly. Dividing by its estimated fluctuation size turns the question of which is bigger into the question of whether the difference is bigger than noise, and "undecided" becomes a legitimate answer.

### 6. Applications to real-world data (start; p. 22)
- The methods are applied to 24 data sets whose distributions have been conjectured to be power laws. Results will show some consistent with a power law, some not, and some marginal (p. 22).
- Data sets listed on p. 22 (a–l; the list continues beyond this part):
  - (a) word frequencies in *Moby Dick*.
  - (b) protein degrees in the yeast interaction network.
  - (c) metabolite degrees in the *E. coli* metabolic network.
  - (d) node degrees of the Internet at the autonomous-system level, May 2006.
  - (e) calls received per AT&T long-distance customer in one day.
  - (f) intensity of wars 1816–1980 (battle deaths per 10 000 of the combined populations).
  - (g) deaths per terrorist attack worldwide, Feb 1968–Jun 2006.
  - (h) bytes received per web (HTTP) request over 24 hours in June 1996.
  - (i) species per genus of mammals.
  - (j) bird sightings per species in the 2003 North American Breeding Bird Survey.
  - (k) customers affected by US blackouts, 1984–2002.
  - (l) copies sold of bestselling US books, 1895–1965.

## Toy example (ours, not from the text)
Take a tiny continuous data set with $x_{\min}=1$ and $x=\{1,2,4,8\}$, $n=4$. This is far below the paper's rule of thumb $n\gtrsim50$, so it only shows the arithmetic.

*Fit with Eq. (3.1).*
- $\sum\ln x_i=0+0.6931+1.3863+2.0794=4.1589$ (this equals $6\ln2$).
- $\hat\alpha=1+4/4.1589=1+0.9618=1.9618$.
- Standard error from (3.2): $\sigma\approx0.9618/\sqrt4=0.481$ (leading term only).

*Log-likelihoods* (continuous power law: $\ln p=\ln(\alpha-1)-\alpha\ln x$ when $x_{\min}=1$):
- $\mathcal L_{PL}=4\ln(0.9618)-1.9618\times4.1589=-0.1558-8.1589=-8.3147$. (Added step: $\hat\alpha\sum\ln x_i=\sum\ln x_i+n=8.1589$.)
- Compare with an exponential, $\ln p=\ln\lambda+\lambda x_{\min}-\lambda x$. (Added step: setting the derivative to zero gives $\hat\lambda=n/\sum(x_i-x_{\min})=4/11=0.3636$.)
- $\mathcal L_{\exp}=4\ln(0.3636)-\hat\lambda\sum(x_i-1)=4(-1.0116)-0.3636\times11=-4.0464-4.0000=-8.0464$.

*Ratio.* $R=\mathcal L_{PL}-\mathcal L_{\exp}=-0.268$.

The sign mildly favours the exponential. With four points a difference of 0.27 is very small, so one should not trust the sign without Vuong's $p$-value, which we do not compute here. This is the paper's point in Section 5.1: the sign of $R$ alone can mislead when the true $R$ is near zero or data are scarce.

## Concepts
- [[heavy tail / power law]] — distribution with $p(x)\propto x^{-\alpha}$, usually only above $x_{\min}$; typically $2<\alpha<3$ (pp. 2–3)
- [[maximum-likelihood-estimation]] (new) — choose parameters maximising the data's likelihood; here MLEs (3.1)–(3.7) for $\alpha$ (p. 5)
- [[x-min-estimation-ks]] (new) — pick $x_{\min}$ minimising KS distance between tail data and fitted power law (p. 11)
- [[ks-statistic]] (new) — max absolute difference between empirical and model CDFs, Eq. (3.9) (p. 11)
- [[complementary-cdf]] (new) — $P(x)=\Pr(X\ge x)$, the preferred plotting form (pp. 3, 7–8)
- [[bayesian-information-criterion]] (new) — approximate log marginal likelihood $\mathcal L-\tfrac12 k\ln n$; used for $x_{\min}$ with $k=x_{\min}$ (p. 11)
- [[goodness-of-fit-p-value]] (new) — fraction of synthetic KS distances exceeding the empirical one; high $p$ means plausible (pp. 15–17)
- [[likelihood-ratio-test]] (new) — compare two fitted models by $R$, the log likelihood ratio, with Vuong's $p$-value for its sign (p. 19)
- [[nested-models]] (new) — one family a subset of another, so the larger always fits at least as well (p. 20)
- [[bootstrap-uncertainty]] (new) — resample the data, refit, and use the spread of estimates as uncertainty (pp. 13–14)

## Canonical instances
- [[city-size-distribution]] (new) — US city populations; mean 8226 is uninformative (pp. 1–2)
- [[synthetic-power-law-test]] (new) — $\alpha=2.5$, $n=10\,000$ test of MLE versus regression (Table 3.1) (pp. 7–8)
- [[three-lookalike-cdfs]] (new) — power law, log-normal and exponential samples that all look straight on log-log axes (pp. 15–16)
- [[moby-dick-word-frequency]] (new) — word counts in *Moby Dick*, first of the 24 data sets (p. 22)
- [[internet-degree-distribution]] (new) — autonomous-system node degrees, May 2006 (p. 22)
- [[terrorism-severity]] (new) — deaths per attack, 1968–2006 (p. 22)

## Bridges (candidates)
- [same-math] Eq. (3.1) ↔ statistics/extreme value: the Hill estimator; the text states the equivalence (p. 5)
- [structural-analogy] Monte Carlo $p$-value with refitting ↔ parametric bootstrap: simulate from the fitted model, repeat the same fit on each simulation
- [structural-analogy] $x_{\min}$ choice (BIC versus KS) ↔ model selection: penalised likelihood versus distance-to-model
- [metaphor] Non-typical, hard-to-summarise distributions as "often a sign of complex underlying processes" (p. 1) ↔ complex systems: heavy tails as signatures of generative mechanisms
- [structural-analogy] Unreliable sign of $R$ near zero ↔ significance testing: effect size versus noise

## Questions this raises
- How large can the bias of log-log regression be, and under what "relatively common conditions" does it arise (Appendix A, promised on p. 5)?
- If the KS method gives consistent $\alpha$ for $C(x+k)^{-\alpha}$, can rigorous performance guarantees be proved (p. 13)?
- How should the likelihood ratio test change for nested models such as power law versus power law with cutoff (Appendix C)?
- Which of the 24 data sets survive the full recipe, and which are marginal (Section 6 continues beyond this part)?

## Reading notes
- **Part boundaries.** This part starts at the title page/abstract (printed p. 1) and ends on printed p. 22, partway through the list of 24 data sets, at item (l). Section 6 continues in the next part. The appendices are not on these pages, so claims here that rely on Appendices A–C (bias of regression; derivation of (3.7); likelihood ratio details; Eq. C.6) are only referenced, not derived.
- **Page numbers.** Printed = pdf for all pages here (no offset).
- **Source slips seen** (the images match the text layer):
  - p. 5: "cannot not be trusted".
  - p. 19: "competing the distribution".
  - p. 21: "increasing positive".
  - p. 16: the footnote says "Monto Carlo".
  - p. 4: "$\ln p(x)=\alpha\ln x+$ constant" has the wrong sign of the slope, while $p\propto x^{-\alpha}$ gives $-\alpha$; the author then speaks of the "absolute slope".
- **$p$-threshold wording.** Section 5.1 says "say $p<0.1$" for the Vuong test (p. 19). The Fig. 5.2b caption uses $p<0.05$ (p. 21). These pages do not reconcile them.
- **Fig. 5.2b panel.** The curve falls from about 0.010 at $n=10$ to roughly 0.001–0.003 for large $n$, consistent with the text's "a few parts per thousand" (p. 22).
- **Table 2.1.** The text layer was garbled. It was reconstructed from the page image.
