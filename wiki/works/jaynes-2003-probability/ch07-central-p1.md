---
id: jaynes-2003-probability/ch07-central-p1
work: jaynes-2003-probability
unit: "7 The central, Gaussian or normal distribution (part 1/2): §§7.1–7.13"
pages: 198–219
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# The central, Gaussian or normal distribution (part 1/2)

## L0 — One line
Jaynes argues that Gaussian error laws are used because they describe a state of knowledge (roughly: only the first two moments of the noise are known), not because real error frequencies are Gaussian, and that they succeed because with them the actual error frequencies become irrelevant to the inference.

## L1 — The gist (≤ 120 words)
Why do Gaussian sampling distributions work so well in inference when real error frequencies are almost never Gaussian? Jaynes reviews three historical derivations (Herschel–Maxwell, Gauss, Landon). He then argues that a Gaussian assignment describes what we know about the noise, namely its general magnitude. Under it, the error of the estimate depends on the actual data errors only through their mean and mean square. The arithmetic mean also gives the largest error cancellation among linear estimators with identical independent errors. Frequencies in imagined data sets are mostly irrelevant. Probability as logic uses the information we have and does not invent information we lack. Nuisance parameters let the data estimate what we do not know.

**Prerequisites:** conditional probability and Bayes' theorem; expectation and variance; maximum likelihood; partial derivatives and Taylor expansion; convolution; the idea of maximum entropy (stated only, proved later in the book). Terms used above: a sampling distribution is the probability of the data given the parameters; a nuisance parameter is an unknown parameter we do not care about; error cancellation means positive and negative errors offsetting in an average.

## L2 — Key ideas (5–10 bullets)
- **Herschel–Maxwell:** independence of orthogonal errors plus rotational independence uniquely force a circular Gaussian. The argument uses only geometry, not probability theory (pp. 200–201).
- **Gauss:** requiring the maximum-likelihood location estimate to equal the arithmetic mean is a necessary and sufficient condition for the Gaussian error law (p. 202); Bernoulli had taken for granted that using the mean implied equal probability for all errors (p. 204).
- **Landon:** if adding small independent increments must keep the functional form of the noise distribution, the diffusion equation gives a Gaussian. This works for any increment distribution with zero mean and small second moment (pp. 205–206).
- **Why ubiquitous use:** the Gaussian is the maximum-entropy choice when only the first two moments are known. Without further information, no other error law is justified (pp. 208–210).
- **Why success:** if the estimate is the arithmetic mean (which the Gaussian leads to when there is no important prior information), its actual error is the mean of the actual errors, however those errors are distributed (pp. 213–214).
- **Error cancellation:** equal weights minimise $\langle\Delta^2\rangle$ among linear estimators (weights $\ge0$, summing to 1) with independent, identically distributed (iid) errors. With no important prior information, the Gaussian leads to the sample mean, and Gauss proved it is the only law that does (p. 214).
- **Frequencies are mostly irrelevant:** the data themselves reveal the error distribution up to a translation. The likelihood matters, not the pre-data expected frequencies (pp. 215–216).
- **Probability as logic is conservative:** it spreads probability over everything the information allows. It cannot mislead (assign high probability to a false conclusion) unless it is given false information (p. 218).
- **Nuisance parameters** (unknown parameters we do not care about), such as the error scale $\sigma$, are integrated out. This uses all information in the data about them (p. 219).

## L3 — Walkthrough

### Opening (pp. 198–199)
De Morgan (1838) was puzzled that Gaussian error-law methods succeed even where the law is implausible as a statement of actual frequencies. Barnard (1983) repeated the question. Feller denounced Gaussian error laws because real error frequencies are almost never Gaussian (p. 198). Jaynes claims he can explain both (1) the "inevitably ubiquitous use" and (2) the ubiquitous success. The key is to think of distributions by their "demonstrable information content" and not by imagined frequencies (p. 198).

### 7.1 The gravitating phenomenon (pp. 199–200)
Jaynes says there seems to be a central distribution toward which all others gravitate under a very wide variety of operations, and which, once attained, stays stable under an even wider variety (p. 199):
$$\varphi(x)\equiv\frac{1}{\sqrt{2\pi}}\exp\Big\{-\frac{x^2}{2}\Big\}\tag{7.1}$$
Examples cited: the binomial or beta sampling distribution becomes Gaussian for many trials (Ch. 4), and posteriors become Gaussian as data accumulate (Ch. 6) (p. 199). The cumulative Gaussian is
$$\Phi(x)\equiv\int_{-\infty}^{x}dt\,\varphi(t)=\int_{-\infty}^{0}dt\,\varphi(t)+\int_{0}^{x}dt\,\varphi(t)=\tfrac12\,[1+\mathrm{erf}(x)]\tag{7.2}$$
Jaynes says "Gaussian" and "normal" are misleading names and prefers "the central distribution". Outside probability, any $\exp\{-ax^2\}$ is called a Gaussian function (p. 200 and fn. 1).

### 7.2 The Herschel–Maxwell derivation (pp. 200–201)
Let $x$, $y$ be star-position errors in the east–west and north–south directions. Herschel made two postulates that seemed intuitively required by conditions of geometrical homogeneity.
- **(P1)** Knowing $x$ tells nothing about $y$, so
$$\rho(x,y)\,dx\,dy=f(x)dx\times f(y)dy\tag{7.3}$$
In polar coordinates ($x=r\cos\theta$, $y=r\sin\theta$):
$$\rho(x,y)\,dx\,dy=g(r,\theta)\,r\,dr\,d\theta\tag{7.4}$$
- **(P2)** The probability is independent of angle: $g(r,\theta)=g(r)$.

Then (7.3) and (7.4) give
$$f(x)f(y)=g\big(\sqrt{x^2+y^2}\big)\tag{7.5}$$
Setting $y=0$ gives $g(x)=f(x)f(0)$, so
$$\log\Big[\frac{f(x)}{f(0)}\Big]+\log\Big[\frac{f(y)}{f(0)}\Big]=\log\Big[\frac{f(\sqrt{x^2+y^2})}{f(0)}\Big]\tag{7.6}$$
A function of $x$ plus a function of $y$ is a function only of $x^2+y^2$. Jaynes says the only possibility is $\log[f(x)/f(0)]=ax^2$. Normalizability requires $a<0$, and normalization fixes $f(0)$ (p. 201):
$$f(x)=\sqrt{\frac{\alpha}{\pi}}\exp\{-\alpha x^2\},\qquad \alpha>0\tag{7.7}$$
$$\rho(x,y)=\frac{\alpha}{\pi}\exp\{-\alpha(x^2+y^2)\}\tag{7.8}$$
Maxwell (1860) gave the three-dimensional version, $\rho(v_x,v_y,v_z)\propto\exp\{-\alpha(v_x^2+v_y^2+v_z^2)\}$, the Maxwellian velocity law (p. 201). The argument is "beautiful" because two qualitative conditions, incompatible in general, become compatible for one quantitative distribution. Einstein used the same kind of argument for the Lorentz transformation. The argument does not use probability theory, only geometric invariance (p. 201).

*Intuition note.* Independence in two perpendicular directions and no preferred direction fit together only for the Gaussian. The result is a fact about functions, not about data.

### 7.3 The Gauss derivation (p. 202)
Estimate a location parameter $\theta$ from $n+1$ observations $x_0,\dots,x_n$ by maximum likelihood. The sampling distribution factors, $p(x_0,\dots,x_n|\theta)=f(x_0|\theta)\cdots f(x_n|\theta)$, so the likelihood equation is
$$\sum_{i=0}^{n}\frac{\partial}{\partial\theta}\log f(x_i|\theta)=0\tag{7.9}$$
Writing
$$\log f(x|\theta)=g(\theta-x)=g(u)\tag{7.10}$$
the estimate $\hat\theta$ satisfies
$$\sum_i g'(\hat\theta-x_i)=0\tag{7.11}$$
Intuition suggests the arithmetic mean
$$\hat\theta=\bar x=\frac1{n+1}\sum_{i=0}^{n}x_i\tag{7.12}$$
but (7.11) and (7.12) are in general incompatible. Consider a special sample
$$x_0=(n+1)u,\quad x_1=\dots=x_n=0,\quad(-\infty<u<\infty)\tag{7.13}$$
Then $\hat\theta=u$ and $\hat\theta-x_0=-nu$, so (7.11) becomes $g'(-nu)+ng'(u)=0$ for $n=1,2,3,\dots$. The case $n=1$ shows $g'$ is antisymmetric, $g'(-u)=-g'(u)$, so
$$g'(nu)=n\,g'(u),\qquad(-\infty<u<\infty),\ n=1,2,3,\dots\tag{7.14}$$
Jaynes says "evidently" the only possibility is linear:
$$g'(u)=au,\qquad g(u)=\tfrac12au^2+b\tag{7.15}$$
Normalizability requires $a<0$, and normalization fixes $b$:
$$f(x|\theta)=\sqrt{\frac{\alpha}{2\pi}}\exp\Big\{-\tfrac12\alpha(x-\theta)^2\Big\},\qquad0<\alpha<\infty\tag{7.16}$$
Since (7.16) was derived assuming the special sample (7.13), this shows thus far only that (7.16) is *necessary* for MLE = sample mean. Conversely, if (7.16) holds, the likelihood equation (7.9) always has the unique solution (7.12). So (7.16) is necessary and sufficient for the agreement, and the scale $\alpha$ is free (p. 202).

*(added step)* With $g'(u)=au$, (7.11) reads $a\sum_i(\hat\theta-x_i)=0$, which gives $\hat\theta=\bar x$ for any sample.

*Intuition note.* Demanding that the maximum-likelihood estimate equal the sample mean (for a location parameter with factorizing sampling distribution) fixes the shape of the error law. Gauss thus showed that this agreement holds exactly for Gaussian errors.

### 7.4 Historical importance of Gauss's result (pp. 203–204)
- Gauss (1809) made the derivation almost in passing. Laplace saw its merit and publicised it, which is why the name "Gaussian" stuck (p. 203).
- De Moivre (1733) had found the distribution accidentally but made no use of it (p. 203).
- Euler (1749) tried the "Great Inequality of Jupiter and Saturn". He had 75 observations over 164 years (1582–1745) and eight orbital parameters. He failed to grasp that combining observations makes errors tend to cancel, and thought it would "multiply the errors" (p. 203). Practical astronomers (Hipparchus, Tycho Brahe) already averaged data (p. 203).
- Footnote 4: if positive and negative errors are equally likely, ten errors all having the same sign has probability $(0.5)^9\simeq0.002$ (p. 203).
- **Daniel Bernoulli (1777):** he argued that using the arithmetic mean treats all places on the target as equally liable to be hit. Jaynes comments that Bernoulli took for granted that equal weights imply equal probability for all errors, which a short calculation would have refuted (p. 204).
- Gauss then proved that
$$\text{(maximum likelihood estimate)}=\text{(arithmetic mean)}\tag{7.17}$$
uniquely determines the Gaussian error law, rather than a uniform one (p. 204).
- Laplace (1783) derived the Gaussian as a limit of the binomial but kept trying $f(x)\propto\exp\{-a|x|\}$. Using only the qualitative principle that combining observations improves accuracy, he solved the Jupiter–Saturn problem in 1787. After seeing Gauss's derivation (1810, 1812) he gave the central limit theorem (p. 204).

### 7.5 The Landon derivation (pp. 205–207)
Landon (1941), an electrical engineer, observed that noise voltage from very different sources "cannot be distinguished one from the other by any known test" (p. 205). He reasoned that such a universal distribution should be fixed theoretically. He imagined a hierarchy $p(v|\sigma)$ with one scale parameter $\sigma^2$, the expected square of the noise voltage. Adding a small independent increment $\epsilon$ (with distribution $q(\epsilon)d\epsilon$, small compared with $\sigma$) should, the stability of the noise seems to imply, only move the distribution up the hierarchy, keeping its functional form (p. 205).

By the sum and product rules, the new distribution of $v'=v+\epsilon$ is a convolution:
$$f(v')=\int d\epsilon\;p(v'-\epsilon|\sigma)\,q(\epsilon)\tag{7.18}$$
Expanding in powers of $\epsilon$ and dropping the prime:
$$f(v)=p(v|\sigma)-\frac{\partial p}{\partial v}\int d\epsilon\,\epsilon\,q(\epsilon)+\frac12\frac{\partial^2p}{\partial v^2}\int d\epsilon\,\epsilon^2q(\epsilon)+\cdots\tag{7.19}$$
With $p\equiv p(v|\sigma)$:
$$f(v)=p-\langle\epsilon\rangle\frac{\partial p}{\partial v}+\frac12\langle\epsilon^2\rangle\frac{\partial^2p}{\partial v^2}+\cdots\tag{7.20}$$
Assume increments are as likely to be positive as negative, $\langle\epsilon\rangle=0$ (p. 206). Then $\langle v^2\rangle$ rises to $\sigma^2+\langle\epsilon^2\rangle$. Landon's invariance requires $f$ to be the same family at the new scale:
$$f(v)=p+\langle\epsilon^2\rangle\frac{\partial p}{\partial\sigma^2}\tag{7.21}$$
Comparing (7.20) and (7.21) gives the diffusion equation
$$\frac{\partial p}{\partial\sigma^2}=\frac12\frac{\partial^2p}{\partial v^2}\tag{7.22}$$
Its solution with initial condition $p(v|\sigma=0)=\delta(v)$ is
$$p(v|\sigma)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big\{-\frac{v^2}{2\sigma^2}\Big\}\tag{7.23}$$
Jaynes calls this, in spirit, an incremental version of the central limit theorem. It is how noise is built in nature, by many small increments, and once Gaussian it stays Gaussian. The form is independent of $q(\epsilon)$ because only $\langle\epsilon^2\rangle$ matters, and its magnitude only sets how far up the $\sigma^2$ hierarchy we move (pp. 206–207). Time-dependent questions distinguish sources: second-order correlations $\langle\epsilon(t)\epsilon(t')\rangle$ relate to the power spectrum, and fourth-order correlations give still more detail. Fourth-order correlations differ between sources even though the sources compared have the same Gaussian point distribution and the same power spectrum (p. 207 and fn. 8). Footnote 7 says Landon had in effect discovered the Fokker–Planck equation (p. 206).

*Intuition note.* Many small independent zero-mean kicks add variance but, to second order, wash out every other detail of the kicks. So the one-time distribution looks Gaussian whatever the kicks were.

**Exercise 7.1** and **7.2** appear here (p. 207); see Exercises section.

### 7.6 Why the ubiquitous use of Gaussian distributions? (pp. 207–210)
Jaynes says this needs almost no mathematics, only a reorientation toward probability as logic (p. 207). A scientist rarely knows the error frequency distribution; typically he knows only the general magnitude. For example, a physicist usually knows the mean square error from the Nyquist thermal fluctuation law, $\langle V^2\rangle=4kTR\,\Delta f$ (fn. 9) (p. 208). If he assigns only the first two moments and imposes no further constraints, then according to the maximum entropy principle (Chapter 11, not derived here) a Gaussian fit to those moments "represent[s] most honestly his state of knowledge" (p. 208).

Points of logic (pp. 208–209):
- This describes knowledge about the *past samples* of noise. It never includes the noise in the measurement about to be made. Carrying past knowledge forward to the next measurement is an inductive inference that may or may not be justified, and honesty requires us to recognize this (p. 208).
- Common sense says fine details of past noise are irrelevant for future fine details, but coarse features such as mean square values may persist. The probability assignment should then have maximum entropy subject to constraints from the coarse features we expect to be reproducible (p. 208).
- Using a Gaussian tells the robot: the only thing known is the first two moments, so assume nothing else (p. 208). With further information (a fourth moment, an upper bound) one assigns a generalized, maximum-entropy distribution (fn. 10).
- Probability theory as logic does not conflict with orthodox theory if we really have perfect frequency knowledge and nothing else. It keeps working with whatever information we have (p. 209).

Where noise knowledge is cruder, or σ is unknown, the Gaussian form is still expected for reasons given later (the central limit theorem). A Gaussian with σ as a nuisance parameter is then a sound starting point, and as Bretthorst shows, often the safest one (p. 209). A defective apparatus may produce noise well above the Nyquist value (p. 209).

Bayes' theorem automatically uses whatever the data say about the noise. So Bayesian inferences with a Gaussian sampling distribution "could be improved upon only by one who had additional information" about the actual errors beyond the first two moments and beyond what the data show (p. 210). With no such information there is no justification, and "no principle", for choosing a different law. Hence the use was "ubiquitous by default" (p. 210). Jaynes concludes the main reason is that error frequencies are unknown, not that they are Gaussian. "Normality" is "a valid description of our state of knowledge", not a physical assumption (p. 210). Jaynes says 95% of his analysis in this book can be conducted with a Gaussian sampling distribution. Special priors, such as pure digitizing errors or a hard upper bound, are exceptions, and even then the Gaussian result is usually near the exact one (p. 210).

**Exercise 7.3** appears here (p. 209).

### 7.7 Why the ubiquitous success? (pp. 210–211)
"Success" means that for nearly two centuries the Gaussian has been easier to use and more accurate than any suggested alternative (p. 210). Whether one inference succeeds depends on the estimator and on the actual errors in the one data set. The frequency distribution of errors in other data sets is irrelevant unless (a) it is actually known, not just imagined, and (b) it tells something about our data set that we would not otherwise know. Jaynes says he has never seen a real problem meeting these conditions (pp. 210–211). Feller thought the assigned sampling distribution must match actual frequencies for estimates to be satisfactory. Jaynes agrees that for a *fixed* estimator the long-run variability of the estimate is determined by the actual error frequencies, if such exist. But Jaynes says that, to the best of his knowledge, orthodoxy never attempted to show that the *assigned* distribution must equal that frequency distribution (p. 211).

### 7.8 What estimator should we use? (pp. 211–213)
Orthodoxy would use the maximum likelihood estimator, and a Bayesian might too if the prior is essentially constant over the high-likelihood region. Jaynes says there is no proof that it gives the most accurate estimates, and he says there are two big gaps in the logic here (p. 211). The scientist's job (Keynes) is the one real case with one real data set (p. 211). By Gauss's result (7.24), MLE = arithmetic mean uniquely determines the Gaussian, so for non-Gaussian laws the two estimators differ (p. 212). For iid sampling,
$$p(x_1\cdots x_n|\mu I)=\prod_{i=1}^{n}f(x_i-\mu)\tag{7.25}$$
Bayesian analysis gives the optimal estimate for each data set. Examples: the posterior mean minimises expected squared error, and the posterior median minimises absolute error. For non-Gaussian sampling the estimator is typically $\sum w_iy_i$ with weights depending on the data configuration $(y_i-y_j)$, hence nonlinear in the observations (p. 212). Footnote 12 suggests the Cauchy law
$$p(y_i|\mu I)=\frac1\pi\Big[\frac1{1+(y_i-\mu)^2}\Big]\tag{7.26}$$
as an instructive case. Footnote 11 says an estimator proven best over all data sets in the long run may be poor for a particular data set, and Bayes' theorem chooses the right estimator per data set (p. 212).

Now the orthodox set-up, with true value $\mu_0$ and $n$ observations:
$$y_i=\mu_0+e_i,\qquad(1\le i\le n)\tag{7.27}$$
Assign independent Gaussian errors:
$$p(D|\mu_0\sigma I)=\Big(\frac{1}{2\pi\sigma^2}\Big)^{n/2}\exp\Big\{-\frac{\sum(y_i-\mu_0)^2}{2\sigma^2}\Big\}\tag{7.28}$$
$$\sum_{i=1}^{n}(y_i-\mu_0)^2=n\big[(\mu_0-\bar y)^2+s^2\big]\tag{7.29}$$
$$\bar y\equiv\frac1n\sum y_i=\mu_0+\bar e,\qquad s^2\equiv\overline{y^2}-\bar y^{\,2}=\overline{e^2}-\bar e^{\,2}\tag{7.30}$$
These are the only data properties in the likelihood, the *sufficient statistics*. So only the first two moments of the errors,
$$\bar e=\frac1n\sum_ie_i,\qquad\overline{e^2}=\frac1n\sum_ie_i^2\tag{7.31}$$
can matter for the error of the estimate. If $\mu$ is estimated by the arithmetic mean, the actual error is
$$\Delta\equiv\bar y-\mu_0=\bar e\tag{7.32}$$
This is the average of the *actual* errors, not an average over a distribution. It holds however the $e_i$ are distributed, even if all the error sits in $e_1$ (p. 213).

*Intuition note.* With a Gaussian assignment, the final error of the sample-mean estimate is just the average of the errors actually present. No assumption about their histogram can change that.

### 7.9 Error cancellation (pp. 213–215)
Estimate $\mu$ by a linear combination
$$(\mu)_{\rm est}=\sum_{i=1}^{n}w_iy_i,\qquad\sum w_i=1,\ w_i\ge0\tag{7.33}$$
Then
$$\Delta^2=[(\mu)_{\rm est}-\mu_0]^2=\Big(\sum_iw_ie_i\Big)^2=\sum_{i,j=1}^{n}w_iw_je_ie_j\tag{7.34}$$
$$\langle\Delta^2\rangle=\sum_{i,j}w_iw_j\langle e_ie_j\rangle\tag{7.35}$$
With identical independent errors, $\langle e_ie_j\rangle=\sigma^2\delta_{ij}$:
$$\langle\Delta^2\rangle=\sigma^2\sum_iw_i^2\tag{7.36}$$
Set $w_i=n^{-1}+q_i$ with $\sum q_i=0$:
$$\langle\Delta^2\rangle=\sigma^2\sum_i\Big(\frac1{n^2}+\frac{2q_i}{n}+q_i^2\Big)=\sigma^2\Big(\frac1n+\sum_iq_i^2\Big)\tag{7.37}$$
This reaches its absolute minimum
$$\langle\Delta^2\rangle_{\min}=\frac{\sigma^2}{n}\tag{7.38}$$
if and only if all $q_i=0$ (p. 214). So uniform weights, i.e. the arithmetic mean, give the smallest expected squared error and "maximum possible opportunity" for error cancellation. The result is independent of $p(e_i|I)$, but highly cogent prior information about $\mu$ would modify it somewhat (p. 214). With no important prior information, the Gaussian leads to the arithmetic mean, and since Gauss proved it is the only law that does, among sampling distributions that estimate $\mu$ by the mean the Gaussian is "uniquely determined as the one that gives maximum error cancellation" (p. 214).

Jaynes's summary (p. 214–215): assigning an independent Gaussian to additive noise does not make the error frequencies correctly represented, but makes them irrelevant in two respects. (1) Aspects of the noise beyond $\bar e$ and $\overline{e^2}$ contribute nothing to the estimates or their accuracy. (2) The estimate is more accurate than from any other sampling distribution that estimates a location parameter by a linear combination of the observations.

De Groot and Goel (1980) found that "Only normal distributions have linear posterior expectations". So the case of other laws giving linear estimates may be empty. Their work suggests, but in Jaynes's view does not prove, that the answer to "what sampling distributions estimate a location parameter linearly?" is again Gaussian. Note (7.38) is a risk over the sampling distribution, whereas they use posterior expectations (p. 215).

**Exercise 7.4** appears here (p. 215).

*Intuition note.* Averaging $n$ independent errors of variance $\sigma^2$ gives variance $\sigma^2/n$. Any unequal weighting concentrates weight on fewer errors and cancels less.

### 7.10 The near irrelevance of sampling frequency distributions (pp. 215–216)
A sampling distribution $f(y|\theta)$ gives the expected frequency of events *before the data are known*. But with fixed parameters and additive noise $y_i=f(x_i)+e_i$, the errors' distribution is known from the data up to a uniform translation: $e_i-e_j=y_i-y_j$, so $e_i=y_i-e_0$ with $e_0$ unknown (p. 215–216). So whether the errors look Gaussian is known from the data, and any pre-data frequency expectation is rendered irrelevant. What matters is the likelihood (p. 216). Any error vector with the same first moment $\bar e$ gives the same estimate of $\mu$. Any with the same first two moments gives the same estimates of $\mu$ and $\sigma$ and the same accuracy claims (p. 216). What matters is whether the Gaussian law correctly describes our *prior information* about the errors in the data set, not whether it describes limiting frequencies (p. 216). The only case where one should, or even could, do something different is when we have additional prior information about the errors beyond the first two moments. Example: for digitizing errors with interval $\delta$, $|e_i|\le\delta/2$. If $\delta<\sigma$, a truncated distribution will "almost surely" give more accurate estimates of $\mu$ (Section 7.17, in the later part) (p. 216).

### 7.11 The remarkable efficiency of information transfer (pp. 216–218)
The distribution $p(e|\alpha\beta)$ with maximum entropy $H=-\int de\,p(e)\log p(e)$ subject to
$$\langle e\rangle=\alpha,\qquad\langle e^2\rangle=\alpha^2+\beta^2\tag{7.41}$$
is the Gaussian
$$p(e|\alpha\beta)=\frac1{\sqrt{2\pi\beta^2}}\exp\Big\{-\frac{(e-\alpha)^2}{2\beta^2}\Big\}\tag{7.42}$$
Prior information fixing only the first two moments therefore determines the Gaussian. Inferences then depend on the noise only through the first two moments of the actual errors, the properties for which we specified information (p. 217). Jaynes says it is a general theorem, to be found when studying maximum entropy, that any sampling distribution assigned by maximum entropy leads to inferences depending only on the information used as constraints. Footnote 15 says (Chapter 8) the class of sampling distributions with sufficient statistics is precisely the class generated by maximum entropy (p. 217).

Probability as logic uses all the information it has and avoids assuming what it lacks. Calculations need not relate probabilities to frequencies, though they may (p. 217 and fn. 16). Introducing error frequencies as ad hoc assumptions when we have no information about them injects arbitrary, and therefore almost certainly false, information (p. 217). The theory is "safe and conservative": it spreads probability over all conditions allowed by the information. Vague information yields posteriors wide enough to include the true value, and it cannot mislead us, in the sense of assigning a high probability to a false conclusion, unless given false information (p. 218). Two failure modes:
- Assuming errors far smaller than actual gives false accuracy claims and "hallucination" of noise artifacts as effects. De Morgan: attributing to the moon's motion "all the tremors which she gets from a shaky telescope" (p. 218).
- Assuming errors far larger gives overly conservative accuracy claims and "blunt perception" (p. 218).

Using the true mean and mean square errors gives maximum protection against both (p. 218).

### 7.12 Other sampling distributions (p. 218)
In rare cases another law expresses our knowledge better. If the error is $e=\alpha\cos\theta$ with $\theta$ unknown, then
$$p(e|I)=\big(\pi\sqrt{\alpha^2-e^2}\big)^{-1},\qquad e^2<\alpha^2.$$
It has a sharp upper bound and may give appreciably better estimates than the Gaussian. If $e=\alpha\tan\theta$ with $\theta$ unknown, the Cauchy law
$$p(e|I)=\pi^{-1}\alpha/(\alpha^2+e^2)$$
results. Jaynes says orthodoxy calls this "pathological", but it causes no difficulty in Bayesian analysis (p. 218).

### 7.13 Nuisance parameters as safety devices (p. 219)
If the error magnitude $\sigma$ is unknown, assigning an arbitrary value is "dangerous folly". Assign a prior $p(\sigma|I)$ over reasonable values. The joint posterior is
$$p(\mu\sigma|DI)=p(\mu\sigma|I)\frac{p(D|\mu\sigma I)}{p(D|I)}\tag{7.43}$$
The product rule rearranges this:
$$p(\mu\sigma|DI)=p(\sigma|I)\,p(\mu|\sigma I)\frac{p(D|\sigma I)\,p(\mu|\sigma DI)}{p(D|I)\,p(\mu|\sigma I)}=p(\mu|\sigma DI)\,p(\sigma|DI)\tag{7.44}$$
Integrating out $\sigma$:
$$p(\mu|DI)=\int d\sigma\;p(\mu|\sigma DI)\,p(\sigma|DI)\tag{7.45}$$
This is an average of the conditional posteriors weighted by what is known about $\sigma$. No relevant information is thrown away: the nuisance parameter is estimated from all evidence. If the data fix $\sigma=\sigma_0$ accurately, $p(\sigma|DI)\to\delta(\sigma-\sigma_0)$ and $p(\mu|DI)\to p(\mu|\sigma_0DI)$ (p. 219). It is up to us to include in the model all parameters that affect the data. Omitting one "cripples" the robot, and the marginalization paradox (Ch. 15) and data pooling paradox (Ch. 8) show what can happen (p. 219).

*Intuition note.* Treating σ as unknown and averaging over it is an honest way to handle ignorance. If the data determine σ very accurately, the answer approaches the known-σ answer.

## Toy example (ours, not from the text)
**Setup.** True $\mu_0=10$, $n=4$. Two possible error vectors, with very different "histograms":
- A: $e=(3,-1,0,0)$, so $y=(13,9,10,10)$.
- B: $e=(0.5,0.5,0.5,0.5)$, so $y=(10.5,10.5,10.5,10.5)$.

**Mean estimate.** A: $\bar y=42/4=10.5$. B: $\bar y=42/4=10.5$. Both give $\Delta=0.5$, which equals $\bar e$: A has $\bar e=2/4=0.5$, B has $\bar e=2/4=0.5$ (7.32). The estimate is the same although the error distributions differ.

**Second moments.**
- A: $\overline{e^2}=(9+1+0+0)/4=2.5$, so $s^2=2.5-0.5^2=2.25$. Direct check: deviations from 10.5 are $2.5,-1.5,-0.5,-0.5$, squares $6.25+2.25+0.25+0.25=9$, and $9/4=2.25$ ✓.
- B: $\overline{e^2}=0.25$, so $s^2=0.25-0.25=0$.

Only $\bar e$ and $\overline{e^2}$ enter the Gaussian likelihood (7.29).

**Error cancellation (7.36)–(7.37), with $\sigma^2=1$.** Uniform $w=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$: $\sum w_i^2=4\cdot\tfrac1{16}=0.25$, so $\langle\Delta^2\rangle=0.25=\sigma^2/n$. Take $w=(0.7,0.1,0.1,0.1)$, so $q=(0.45,-0.15,-0.15,-0.15)$ and $\sum q_i=0$ ✓. Then $\sum w_i^2=0.49+3(0.01)=0.52$. Via (7.37): $\sum q_i^2=0.2025+3(0.0225)=0.27$ and $\tfrac14+0.27=0.52$ ✓. So unequal weights give $0.52>0.25$ as expected squared error. For sample A alone these weights give an error of $0.7(3)+0.1(-1)=2.0$, versus $0.5$ for the mean; this is one sample, the theorem is about expectation.

## Concepts
- [[gaussian-distribution]] (new) — the "central distribution" $\varphi(x)$; here treated as a description of knowledge, not of frequencies (pp. 199, 210)
- [[central-limit-theorem]] (new) — sums of many small contributions approach the Gaussian; here only cited and described, not proved (p. 199)
- [[maximum-entropy-principle]] — given only $\langle e\rangle$ and $\langle e^2\rangle$, the maximum-entropy density is Gaussian; theorem is deferred to Ch. 11 (pp. 208, 216–217)
- [[probability-as-extended-logic]] — probabilities represent information; unknown circumstances must not enter inferences (pp. 207, 217)
- [[likelihood]] — after the data are in, what remains significant for inference is the likelihood function (p. 216)
- [[sufficient-statistics]] (new) — data summaries that alone enter the likelihood; with Gaussian errors, $\bar y$ and $s^2$ (p. 213)
- [[error-cancellation]] (new) — averaging lets errors offset one another; $\langle\Delta^2\rangle=\sigma^2\sum w_i^2$ is minimal at $w_i=1/n$ (p. 214)
- [[incremental-invariance-landon]] (new) — requiring the noise distribution to keep its form when small increments are added gives the diffusion equation (pp. 205–206)
- [[nuisance-parameter-marginalization]] (new) — integrate out an uninteresting parameter such as $\sigma$, weighted by its posterior (p. 219)
- [[frequentist-vs-bayesian-inference]] — contrast: long-run frequencies of estimators and imagined data sets versus inference from the one data set at hand (pp. 210–212)
- [[posterior-distribution]] — posterior mean minimises expected squared error, median expected absolute error (p. 212)
- [[prior-distribution]] — the prior $p(\sigma|I)$ states the range of plausible error scales (p. 219)
- [[fisher-sufficiency-note]] (new) — footnote claims sampling distributions with sufficient statistics are exactly those generated by maximum entropy (Ch. 8) (p. 217, fn. 15)

## Canonical instances
- [[herschel-star-position-errors]] — orthogonal independence plus rotational invariance gives the circular Gaussian (p. 200–201)
- [[maxwell-velocity-distribution]] — 3-D version of the same argument (p. 201)
- [[euler-jupiter-saturn]] — Euler failed to see error cancellation: 75 observations, eight parameters (p. 203)
- [[bernoulli-archer]] — Bernoulli's argument that using the mean treats all places on the target alike; Jaynes says he took this to imply equal probability for all errors (p. 204)
- [[landon-noise-hierarchy]] — electrical noise built by successive small increments (p. 205)
- [[nyquist-thermal-noise]] — mean square noise voltage $4kTR\Delta f$ (p. 208, fn. 9)
- [[digitizing-error-bound]] — error $|e_i|\le\delta/2$ justifies a truncated sampling law (p. 216)
- [[cauchy-sampling-distribution]] — arises if $e=\alpha\tan\theta$; gives nonlinear estimators (pp. 212, 218)
- [[shaky-telescope-moon]] — de Morgan's image of confusing noise with real signal (p. 218)

## Bridges (candidates)
- [same-math] Landon's equation (7.22), $\partial p/\partial\sigma^2=\tfrac12\partial^2p/\partial v^2$ ↔ physics: the diffusion equation, with variance playing the role of time (pp. 206–207)
- [same-math] Exercise 7.4's weights (7.39)–(7.40) ↔ statistics: minimum-variance linear combination under a known covariance matrix (p. 215)
- [structural-analogy] Gaussian as maximum entropy under fixed mean and variance ↔ information-theory: the maximum-entropy principle and exponential families (pp. 216–217)
- [structural-analogy] Integrating out $\sigma$ as a nuisance parameter ↔ Bayesian: hierarchical models averaging over group-level uncertainty (p. 219)
- [metaphor] Gaussian as a "gravitating" attractor under many operations ↔ dynamical systems: a stable fixed point (p. 199)

## Questions this raises
- Jaynes says (7.14) "evidently" forces linearity. Which regularity condition (e.g. continuity) is needed to rule out pathological solutions of $g'(nu)=ng'(u)$ (p. 202)?
- When is the claim that the Gaussian is the most "honest" assignment justified, given the inductive step from past noise samples to future noise (p. 208)?
- If sampling distributions with linear estimates are only Gaussian (de Groot–Goel), is Jaynes's error-cancellation argument in 7.9 complete, or does it cover an empty case (p. 215)?
- How wrong is a Gaussian analysis when real errors are bounded, such as the cosine-form errors in 7.12 (p. 218)?

## Exercises worth doing
- Ex. 7.1 (p. 207) — show the Gaussian (7.23) becomes exact after $n$ small increments as $n\to\infty$, $\langle\epsilon^2\rangle\to0$, $n\langle\epsilon^2\rangle\to$ const.; the incremental central limit theorem — difficulty: medium
- Ex. 7.2 (p. 207) — drop $\langle\epsilon\rangle=0$ to get a Fokker–Planck equation with a drift; suggest an application — difficulty: medium
- Ex. 7.3 (p. 209) — show that with a huge amount of frequency data and no other information, $p(e|I)\to f(e)$, and state the exact conditions — difficulty: hard
- Ex. 7.4 (p. 215) — derive the optimal weights (7.39) and the minimum (7.40) for a general covariance matrix — difficulty: medium

## Reading notes
- This is part 1 of a two-part split of Chapter 7. It starts at the chapter opening (printed p. 198) and ends at the end of §7.13 (printed p. 219). The split falls at a section boundary. Printed page = pdf − 30.
- Text-layer equations were garbled in places; all equations here were checked against the page images.
- In (7.2) the image shows a stray comma and "+" in the middle line ("$\int_{-\infty}^0 dt\,\varphi(t),+\int_0^x dt\,\varphi(t)$"). The text states $\Phi(x)=\tfrac12[1+\mathrm{erf}(x)]$ with no definition of erf in these pages, so the exact argument convention of erf is not given here.
- (7.25) writes the data as $x_i$, while the text right after it and (7.27) on use $y_i$; this is a notation shift in the source.
- Footnote texts (fn. 8 on Maxwell demons and Hanbury Brown–Twiss, fn. 9 on Nyquist units) were read but only summarised where relevant.
- Several results are explicitly deferred to later chapters (maximum entropy, Chs. 8, 11, 15; §7.17); these pages state them without proof.
