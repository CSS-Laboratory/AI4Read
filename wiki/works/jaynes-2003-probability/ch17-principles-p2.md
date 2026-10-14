---
id: jaynes-2003-probability/ch17-principles-p2
work: jaynes-2003-probability
unit: "Chapter 17, Principles and pathology of orthodox statistics (part 2/2: §§17.7–17.12)"
pages: 531–552
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
# Principles and pathology of orthodox statistics, part 2: randomization, missing data, trend and seasonality

## L0 — One line
Jaynes argues that, in the examples he gives, orthodox methods either lose information or reach Bayesian results only by a much longer route, and that integrating out nuisance parameters (parameters we must model but do not want to estimate) is the clean way to handle trend and seasonality.

## L1 — The gist (≤ 120 words)
The question is whether orthodox (sampling-theory) methods ever beat Bayesian ones. Jaynes argues through examples that they do not. In his Monte Carlo example a uniform grid beats random points. Missing data need no special treatment in Bayes' rule. For a sinusoid plus a linear trend, integrating out the trend gives the same estimate that orthodox detrending reaches only after an infinite chain of mutual corrections. He then states the general Gaussian solution in matrix form. He concludes that orthodox methods were satisfactory for the simple problems Fisher treated, where they match Bayes. Evading Bayes' theorem leads to the same final results with much more work. Only Bayesian methods, he says, handle harder problems without losing information.

**Prerequisites:** Gaussian likelihoods and completing the square; marginalizing a joint density; least squares; matrix inverse and block matrices; geometric (Neumann) series for matrices.

## L2 — Key ideas
- **Randomization is inferior.** In the Monte Carlo example, a uniform grid with n points reaches the probable error that random sampling reaches with about 3000 points when n = 100. Jaynes proposes, as a general principle that is perhaps not quite a theorem, that a better nonrandomized method exists but needs more thinking (p. 532).
- **Bayes has built-in safety.** The log-likelihood is a sum over the actual data, so a spread-out data set gives a wide posterior. An orthodox accuracy claim from one statistic ignores the data range and averages over data sets never observed (p. 533).
- **Missing data is not a problem for Bayes.** The same sum of log-likelihoods works over whatever data exist, with no new sample space or ad hoc imputation (pp. 533–534).
- **Nuisance parameters are integrated out, not subtracted.** Bayesian "detrending" integrates the trend rate out of the joint posterior and leaves the data untouched. Orthodox detrending and seasonal adjustment alter the data and can destroy information (pp. 535–537).
- **The Bayes estimate is independent of the true trend rate.** The orthodox least-squares estimate from detrended data is biased by any error in the trend estimate (pp. 538–540).
- **Fully improved orthodoxy converges to the Bayes estimate.** Iterating the orthodox A↔B corrections forever gives the Bayesian marginal estimates (pp. 541–543).
- **The general Gaussian case is a short matrix recipe.** It allows Gaussian noise that is not white, correlated parameter priors, general basis functions and unevenly spaced times (pp. 545–549).
- **Orthodoxy was satisfactory for Fisher's simple problems.** These had few parameters, a sufficient statistic, no important prior information and no nuisance parameters; where these fail, Jaynes says only Bayesian methods keep the relevant information (p. 550). Jaynes also criticizes Bayesians who keep "random variable" language (pp. 550–552).

## L3 — Walkthrough

### 17.7 The folly of randomization (pp. 531–532)
**Setup.** We want $\theta \equiv \int_0^1 dx\, f(x)$ \tag{17.70}, with $f$ living in the unit square. Pick $n$ random points $(x,y)$ and count the number $r$ with $y \le f(x)$. The estimate is $(\theta)_{est}=r/n$ (p. 531).

**Random (Monte Carlo) version.** The sampling distribution of $r$ is taken as binomial:
$$p(r|n\theta)=\binom{n}{r}\theta^r(1-\theta)^{n-r}\tag{17.71}$$
with (mean) ± (standard deviation) $\theta \pm \sqrt{\theta(1-\theta)/n}$ \tag{17.72}. The probable error is then
$$(\theta)_{est}=\frac rn \pm\sqrt{\frac{r(n-r)}{n^3}}.\tag{17.73}$$
Example: true $\theta=1/2$, $n=100$, observed $r=43$ gives $0.43\pm\sqrt{0.43\times0.57/n}=0.43\pm0.05$ \tag{17.74}. This is an accuracy of about 11.5%. The error improves only as $1/\sqrt n$ (p. 531).

**Nonrandom grid version.** Divide the square into $\sqrt n$ steps each way and put one point at each grid point. The maximum error per step is
$$[\text{error in } f(x)]\times[\text{step width}]=\frac1{2\sqrt n}\times\frac1{\sqrt n}=\frac1{2n}\tag{17.75}$$
so the maximum possible error in the integral is
$$[\text{number of steps}]\times[\text{max error per step}]=\frac{1}{2\sqrt n}.\tag{17.76}$$
For $\theta\simeq0.5$ the Monte Carlo *probable* error is about the grid's *maximum possible* error (p. 531, 532).

**The grid's probable error.** The central limit theorem is applied with a rectangular error distribution in each step. The mean square error per step is printed as
$$\sqrt n\int_0^{\sqrt n}dx\left(x-\frac1{2\sqrt n}\right)^2=\frac1{12n^2}\tag{17.77}$$
(see Reading notes on the printed limit). If step errors are independent, the total mean square error is
$$(\text{mean square error per step})\times(\text{number of steps})=\frac{1}{12\,n^{3/2}}\tag{17.78}$$
and the probable error is about
$$\pm\frac{1}{\sqrt{12}\,n^{3/4}}.\tag{17.79}$$
Numbers (p. 532):
- $n=100$: Monte Carlo 0.05; grid 0.00913 (less than one-fifth as much).
- $n=1000$: Monte Carlo 0.0158; grid 0.00162 (about one-tenth).
- The grid at $n=100$ matches Monte Carlo at $n=3000$.

Jaynes says this fits the italicized statement after (17.16) and cites Royall and Cumberland (1981) as a similar case by non-Bayesian authors (p. 532).

*Intuition note.* Random points can leave gaps and clumps (our gloss). A regular grid covers the square evenly, and its error shrinks like $n^{-3/4}$ in this example instead of $n^{-1/2}$. The comparison rests on the stated assumptions (rectangular, independent step errors).

### 17.8 Fisher: common sense at Rothamsted (p. 532)
Jaynes proposes a general principle: "Whenever there is a randomized way of doing something, there is a nonrandomized way that yields better results from the same data, but requires more thinking." He says it may not quite be a theorem, but he is confident it will be confirmed whenever one is willing to do the extra thinking (p. 532).

**17.8.1 The Bayesian safety device (pp. 532–533).** Jaynes says Bayesian methods are not only more powerful but also safer: they have automatic safeguards against over-optimistic or over-pessimistic conclusions (p. 532). For parameter estimation, with or without a sufficient statistic (a summary of the data that carries all the information about the parameter),
$$\log L(\alpha)=\sum_{i=1}^n\log p(x_i|\alpha)=n\,\overline{\log p(x_i|\alpha)}\tag{17.80}$$
is an average of individual-point log-likelihoods, spread over the full range of the data. So a bad (spread-out) data set gives a wide posterior, which is the warning (p. 533).

For a location parameter, $p(x|\alpha)=h(x-\alpha)$, with an uninformative prior, the posterior width is essentially
$$(\text{range of the data})+(\text{width of individual likelihoods}).\tag{17.81}$$
A sharply concentrated data set gives a posterior whose width approaches a lower bound set by the single-point likelihood and $n$ (p. 533).

**Orthodox contrast.** The accuracy claim is the width of the sampling distribution of the chosen estimator. It takes no note of the data range, so one statistic claims the same accuracy for large or small range. It also expresses variability over other data sets that might have been obtained but were not. Jaynes calls these unobserved sets "a figment of our imagination" and asks what test could decide between two conjectures about them (p. 533).

### 17.9 Missing data (pp. 533–534)
For Bayes this problem "does not exist". With data $\{x_i\}$ at times $i\in T$,
$$\log L(\theta)=\sum_{i\in T}\log p(x_i|\theta)\tag{17.82}$$
sums over whatever data we have. Regular or irregular spacing makes no difference, and one program handles any set $\{x_i;t_i\}$ (p. 533).

**Orthodox contrast.** Estimation goes through the sampling distribution of a statistic $\theta^*(x_i)$. Jaynes describes two ways to deal with missing data (p. 534):
1. Reconsider the whole problem: each kind of missing or extra data may require a new sample space, a new statistic $\theta^{**}$ and a new sampling distribution $p(\theta^{**}|\theta)$.
2. Invent an ad hoc imputation of the missing values, which is logically unjustified and ambiguous (he cites Little and Rubin 1987).

He adds that some who moved to the Bayesian camp kept adding such ad hoc "corrections" to Bayesian or maximum-entropy methods. In his view this gives a worse inference by a bigger computation (p. 534).

**Magnification.** When orthodox and Bayesian answers differ by a small amount, look for an extreme problem where the difference becomes large or qualitative. Common sense can then judge, as in the chi-squared test of Chapter 9 (p. 534).

### 17.10 Trend and seasonality in time series (pp. 534–545)
Real series are seldom stationary; trend is the commonest nonstationarity. Jaynes tells a story, "perhaps apocryphal", of a researcher who found a correlation between Church of England membership and suicides. He explains it by the growing English population, and blames the tendency to jump from correlation to causation. He also notes contaminated data (Halley, Chapter 9) and says the key to dealing with it is the useful role of **nuisance parameters** (parameters we must include but do not want to estimate) (p. 535).

**17.10.1 Orthodox methods (pp. 535–536).** The traditional devices are ad hoc: "detrending" and "seasonal adjustment" in economics, "filtering" in engineering. Detrending assumes $y(t)=x(t)+Bt+e(t)$, estimates the trend and subtracts it. He notes that many writers have observed that detrending may introduce spurious artifacts, and that it may even destroy the data's relevance. He also says that most obtainable economic series are nearly useless because of irreversible seasonal adjustment. He wants researchers to have raw data, free of any "destructive mutilation". Engineers use high-pass and band-rejection filters. Choosing the best realizable filter is a hard and basically indeterminate problem, though intuition has found filters usable when the contamination is known in advance (pp. 535–536).

**17.10.2 The Bayesian method (pp. 536–539).** The rule is to calculate the probability of whatever is unknown and of interest, conditional on whatever is known. We do not remove trend or season from the data, because the "true" trend or seasonal term cannot be known and any assumption about it is necessarily somewhat arbitrary and so almost certain to inject false information into the adjusted series. We remove their effect from the *final conclusions* and leave the data intact (p. 536).

*Model.* Take a single sinusoid and a linear trend, with $\omega$ known (for monthly data with a yearly cycle, $\omega=2\pi/12=0.524$):
$$y(t)=A\,s(t)+Bt+e(t),\qquad s_t\equiv\sin\omega t\tag{17.83}$$
Data are $y=(y_1,\dots,y_N)$ at $t=1,\dots,N$. Noise is assigned independent Gaussian, $e_t\sim N(0,\sigma)$:
$$p(y|AB\sigma)=\left(\frac1{2\pi\sigma^2}\right)^{N/2}\exp\Big\{-\frac N{2\sigma^2}Q(A,B)\Big\}\tag{17.84}$$
$$Q(A,B)\equiv\frac1N\sum_t(y_t-As_t-Bt)^2=\overline{y^2}+A^2\overline{s^2}+B^2\overline{t^2}-2A\,\overline{sy}-2B\,\overline{ty}+2AB\,\overline{st}\tag{17.85}$$
$$\overline{y^2}\equiv\frac1N\sum_{t=1}^N y_t^2,\qquad \overline{sy}\equiv\frac1N\sum_{t=1}^N s_ty_t\tag{17.86}$$
Overbars denote sample averages (p. 537).

Three averages $(\overline{s^2},\overline{t^2},\overline{st})$ are fixed by the experimental design. Approximately $\overline{s^2}\simeq 1/2$ and $\overline{t^2}\simeq N^2/3$ \tag{17.87}, with relative errors $O(1/N)$. $\overline{st}$ is highly variable, of order $1/\omega$ because of cancellation. The data enter only through $(\overline{y^2},\overline{sy},\overline{ty})$, the jointly sufficient statistics (p. 537).

*Marginalizing.* To estimate $A$ with $B$ as nuisance, find $p(AB|DI)$ \tag{17.88} and integrate out $B$:
$$p(A|DI)=\int dB\,p(AB|DI)\tag{17.89}$$
This is "Bayesian detrending". Integrating out $A$ instead would be "Bayesian seasonal adjustment" (p. 537).

For diffuse priors (prior densities not varying appreciably over the region of high likelihood):
$$\int_{-\infty}^{\infty}dB\exp\Big\{-\frac{NQ(A,B)}{2\sigma^2}\Big\}=(\text{const.})\exp\Big\{-\frac N{2\sigma^2}\Big[\frac{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}{\overline{t^2}}\Big](A-\hat A)^2\Big\}\tag{17.90}$$
$$\hat A\equiv\frac{\overline{t^2}\,\overline{sy}-\overline{st}\,\overline{ty}}{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}\tag{17.91}$$
with const. independent of $A$. The posterior (mean) ± (standard deviation) of $A$, whatever $B$ is, is
$$(A)_{est}=\hat A\pm\sigma\sqrt{\frac{\overline{t^2}}{N[\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}]}}=\hat A\pm\frac{\sigma}{\sqrt{N\overline{s^2}(1-r^2)}}\tag{17.92}$$
$$r\equiv\frac{\overline{st}}{\sqrt{\overline{s^2}\,\overline{t^2}}}\tag{17.93}$$
$r$ is the correlation coefficient of $s$ and $t$ (p. 538).

Jaynes notes that some orthodox writers object that a parameter is not a "random variable" and that the prior is arbitrary. For him the prior represents real, relevant prior information, so he proposes to compare actual performance instead (p. 538).

*Relation to detrending.* The joint posterior factors two ways:
$$p(AB|DI)=p(A|DI)\,p(B|ADI)\tag{17.94}$$
$$p(AB|DI)=p(A|BDI)\,p(B|DI)\tag{17.95}$$
so
$$p(A|DI)=\int dB\,p(A|BDI)\,p(B|DI)\tag{17.96}$$
is a weighted average of the conditionals $p(A|BDI)$ \tag{17.97}. For known $B$,
$$p(A|BDI)\propto\exp\Big\{-\frac{N\overline{s^2}}{2\sigma^2}(A-A^*)^2\Big\},\qquad A^*\equiv\frac{\overline{sy}-B\,\overline{st}}{\overline{s^2}}\tag{17.98, 17.99}$$
$A^*$ is the ordinary least-squares fit of $As(t)$ to detrended data $y(t)_{det}\equiv y(t)-Bt$:
$$A^*=\frac{\overline{(sy)_{det}}}{\overline{s^2}}\tag{17.100}$$
Any error in the orthodoxian's trend estimate biases his $A$. The Bayesian value averages over all $B$ weighted by $p(B|DI)$. If $p(B|DI)$ has one sharp peak at $B^*$, the two agree when the orthodoxian also uses $B^*$. If $B$ is poorly determined, the Bayes estimate is "more conservative" while the orthodox estimate can vary widely (p. 539). Jaynes notes that the Bayes estimate is implicitly based on quadratic loss, and that an orthodoxian judges estimates by a different criterion (p. 539).

*Intuition note.* Instead of guessing the trend once and subtracting it, the Bayesian averages the answer over all plausible trends. The data stay untouched. If the trend is poorly determined, the Bayes estimate is more conservative (p. 539).

**17.10.3 Comparison of Bayesian and orthodox estimates (pp. 540–541).** Take the viewpoint of someone who knows the true $A_0,B_0$ but not the noise. The data are $y_t=A_0s_t+B_0t+e_t$ \tag{17.101}, so
$$\overline{sy}=A_0\overline{s^2}+B_0\overline{st}+\overline{se}\tag{17.102}$$
$$\overline{ty}=A_0\overline{st}+B_0\overline{t^2}+\overline{te}\tag{17.103}$$
Only $\overline{se},\overline{te}$ vary with the noise. Substituting into (17.91):
$$(\hat A)_{Bayes}=A_0+\frac{\overline{t^2}\,\overline{se}-\overline{st}\,\overline{te}}{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}\tag{17.104}$$
$B_0$ cancels, so the Bayes estimate removes the trend effect entirely from the conclusions. The unknown noise still causes some error, and (17.104) says exactly how much (p. 540).

The orthodox least-squares estimator (17.100) with detrending by any estimate $\hat B$ gives
$$(\hat A)_{orthodox}=A_0+\frac{\overline{se}+(B_0-\hat B)\overline{st}}{\overline{s^2}}\tag{17.105}$$
so any error in $\hat B$ enters. With the usual choice $\hat B=\overline{ty}/\overline{t^2}$ \tag{17.106}:
$$(\hat A)_{orthodox}=A_0+\frac{\overline{t^2}\,\overline{se}-\overline{ty}\,\overline{st}+B_0\overline{t^2}\,\overline{st}}{\overline{t^2}\,\overline{s^2}}=(1-r^2)A_0+\frac{\overline{se}}{\overline{s^2}}\tag{17.107}$$
(last equality as printed; see Reading notes). This is also independent of $B_0$ (p. 541).

**Orthodox view:** this estimator has a negative bias, since $\overline{se}$ is "on the average" zero, and one might "correct" it by a multiplying factor as in (17.6). Jaynes replies that it is far from clear the optimum is found merely by rescaling least squares. He then imagines the orthodoxian granting that (17.104) is unbiased; even so, Jaynes says, it would not follow that the Bayesian solution is the best possible one. He suspects a strongly anti-Bayesian reader would reject any such suggestion and try to repair (17.107) orthodoxly (p. 541).

**17.10.4 An improved orthodox estimate (pp. 541–544).**
Start with the seasonal-only estimate $\hat A^{(0)}=\overline{sy}/\overline{s^2}$ \tag{17.108}. Detrend with $\hat B$: $(y_t)_{det}\equiv y_t-\hat Bt$ \tag{17.109}, using the regression estimate $\hat B^{(0)}=\overline{ty}/\overline{t^2}$ \tag{17.110}. This gives the conventional result
$$\hat A^{(1)}=\frac{\overline{sy}-\overline{st}\,\hat B^{(0)}}{\overline{s^2}}=\frac{\overline{t^2}\,\overline{sy}-\overline{st}\,\overline{ty}}{\overline{t^2}\,\overline{s^2}}\tag{17.111}$$
But $A$ and $B$ enter on the same footing. If $A$ should be estimated from detrended data, $B$ should be estimated from decyclized data $y_t-\hat A^{(0)}s_t$:
$$\hat B^{(1)}=\frac{\overline{ty}-\overline{st}\,\hat A^{(0)}}{\overline{t^2}}=\frac{\overline{s^2}\,\overline{ty}-\overline{st}\,\overline{sy}}{\overline{t^2}\,\overline{s^2}}\tag{17.112}$$
Then
$$\hat A^{(2)}=\frac{\overline{sy}-\overline{st}\,\hat B^{(1)}}{\overline{s^2}}\tag{17.113}$$
$$\hat B^{(2)}=\frac{\overline{ty}-\overline{st}\,\hat A^{(1)}}{\overline{t^2}}\tag{17.114}$$
The sequence continues forever (p. 542). Does the sequence converge, and can the limit be found directly?

Define $V_n\equiv(\hat A^{(n)},\hat B^{(n)})^T$ \tag{17.115}, a $2\times1$ vector. From (17.111)–(17.113):
$$V_{n+1}=V_0+MV_n\tag{17.116}$$
$$M=\begin{pmatrix}0&-\overline{st}/\overline{s^2}\\ -\overline{st}/\overline{t^2}&0\end{pmatrix}\tag{17.117}$$
(lower-left sign: see Reading notes). Then
$$V_n=(1+M+M^2+\cdots+M^n)V_0\tag{17.118}$$
By the Schwartz inequality, $\overline{st}^{\,2}\le\overline{s^2}\,\overline{t^2}$, the eigenvalues of $M$ are less than unity (p. 543). As $n\to\infty$,
$$V_\infty=(I-M)^{-1}V_0\tag{17.119}$$
$$(I-M)^{-1}=\frac1{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}\begin{pmatrix}\overline{t^2}\,\overline{s^2}&-\overline{t^2}\,\overline{st}\\-\overline{s^2}\,\overline{st}&\overline{t^2}\,\overline{s^2}\end{pmatrix}\tag{17.120}$$
$$\hat A^{(\infty)}=\frac{\overline{t^2}\,\overline{s^2}\hat A^{(0)}-\overline{t^2}\,\overline{st}\,\hat B^{(0)}}{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}=\frac{\overline{t^2}\,\overline{sy}-\overline{st}\,\overline{ty}}{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}\tag{17.121}$$
$$\hat B^{(\infty)}=\frac{\overline{s^2}\,\overline{ty}-\overline{st}\,\overline{sy}}{\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}}\tag{17.122}$$
(numerator as corrected; see Reading notes). (17.121) is exactly the Bayes estimate (17.91), computed far more easily. (17.122) is the Bayes estimate found by integrating out $A$ from (17.88) (p. 543).

Jaynes concludes (pp. 543–544):
- This repeats the Chapter 13 finding: an orthodoxian who thinks his problem through to the end is obliged to use the Bayesian mathematical algorithm, whatever his rationale.
- Integrating out a nuisance parameter sums an infinite series of mutual updatings. To the best of his knowledge no orthodox writer has noticed this.
- The result is not limited to trend and seasonal parameters; he says it "will generalize effortlessly".
- In the long run, attempts to evade Bayes' theorem give the same final results and merely require about an order of magnitude more work (p. 544).

*Intuition note.* Alternately estimating $A$ given $B$ and $B$ given $A$ is a fixed-point iteration, and the Bayesian marginal answer is its fixed point. Integrating out the nuisance parameter reaches that point in one step.

**17.10.5 The orthodox criterion of performance (pp. 544–545).** Orthodoxy judges accuracy by the sampling distribution of the estimator; Bayes judges it by the posterior pdf (p. 544). In both (17.104) and (17.107), the noise terms combine into
$$\overline{ge}\equiv\frac1N\sum_{t=1}^Ng_te_t\tag{17.123}$$
$$E(\overline{ge})=\frac1N\sum_tg_tE(e_t)=0\tag{17.124}$$
$$E[(\overline{ge})^2]=\frac1N\sum g_tg_{t'}E(e_te_{t'})=\overline{g^2}\sigma^2\tag{17.125}$$
using $E(e_te_{t'})=\sigma^2\delta(t,t')$. Hence $(\overline{ge})_{est}=0\pm\sigma\sqrt{\overline{g^2}}$ \tag{17.126} (as printed). For the Bayes estimator (17.104):
$$g_t=\frac{\overline{t^2}\,s_t-\overline{st}\,t}{\overline{t^2}\,\overline{s^2}-\overline{st}^{\,2}}\tag{17.127}$$
and "after some algebra"
$$\overline{g^2}=\frac{\overline{t^2}\,[\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}]}{\overline{s^2}(1-r^2)}\tag{17.128}$$
(as printed). The printed sampling (mean) ± (standard deviation) is
$$\tilde A\pm\sigma\sqrt{\hat N\overline{s^2}(1-r^2)}\ \text{(Bayes, 17.129)};\qquad (1-r^2)\tilde A\pm\sigma\sqrt{\frac{1-r^2}{N\overline{s^2}}}\ \text{(orthodox, 17.130)}.$$
The text gives no further comment on these two results (p. 545).

### 17.11 The general case (pp. 545–549)
The data need not be uniformly spaced. The Gaussian noise need not be stationary or white (uncorrelated). The parameter priors need not be independent. Jaynes says the programs are not appreciably harder to write if the general formulas are in view (p. 545).

**Model.** $y_{t_i}=T(t_i)+F(t_i)+e(t_i)$, $1\le i\le N$ \tag{17.131}. $T$ is a trend, not necessarily linear. $F$ is periodic, not necessarily sinusoidal. $e$ is irregular. Expand
$$T(t)=\sum\gamma_k\Phi_k(t)\tag{17.132}$$
in linearly independent functions (for example Legendre polynomials), and
$$F(t)=\sum[A_k\cos(kt)+B_k\sin(kt)]\tag{17.133}$$
The joint likelihood is
$$L(\gamma,A,B,\sigma)=\Big(\frac1{2\pi\sigma^2}\Big)^{N/2}\exp\Big\{-\frac1{2\sigma^2}\sum_{i=1}^N[y_i-T(t_i)-F(t_i)]^2\Big\}\tag{17.134}$$
(p. 545). The quadratic form is
$$Q(\alpha_k,\gamma_j)\equiv\sum_{i=1}^N\Big[y_i-\sum_{j=1}^r\gamma_jT_j(t_i)-\sum_{k=1}^m\alpha_kF_k(t_i)\Big]^2\tag{17.135}$$
For seasonal adjustment $m=12$, $\{\alpha\}=\{A_0,\dots,A_6,B_1,\dots,B_5\}$ \tag{17.136}, and $F_k(t)=\cos(k\omega t)$ for $0\le k\le6$, $\sin([k-6]\omega t)$ for $7\le k\le12$ \tag{17.137} (p. 546).

Combine into $q\equiv(\alpha_1,\dots,\alpha_m,\gamma_1,\dots,\gamma_r)$, of dimension $n=m+r$ \tag{17.138}, with $G_k=F_k$ for $1\le k\le m$ and $G_k=T_k$ for $m<k\le n$ \tag{17.139}. Then
$$y(t)=\sum_{j=1}^nq_jG_j(t)+e(t)\tag{17.140}$$
$$y_i=\sum_jq_jG_j(t_i)+e(t_i)\tag{17.141}$$
$$y=qG+e\tag{17.142}$$
The noise has joint prior
$$p(e_1\cdots e_N)=\frac{\sqrt{\det K}}{(2\pi)^{N/2}}\exp\{-\tfrac12e^TKe\}\tag{17.143}$$
where $K^{-1}$ is the $(N\times N)$ noise prior covariance matrix. For stationary white noise $K^{-1}=\sigma^2\delta_{ij}$ \tag{17.144}. The sampling pdf is
$$p(y_1\cdots y_N|qKI)=\frac{\sqrt{\det K}}{(2\pi)^{N/2}}\exp\{-\tfrac12(y-qG)^TK(y-qG)\}\tag{17.145}$$
(p. 546). The parameter prior is
$$p(q_1\cdots q_n|I)=\frac{\sqrt{\det L}}{(2\pi)^{n/2}}\exp\{-\tfrac12(q-q_0)^TL(q-q_0)\}\tag{17.146}$$
with $L^{-1}$ the $(n\times n)$ prior covariance and $q_0$ the prior estimates. Almost always $L$ is diagonal, $L_{ij}=\sigma_j^2\delta_{ij}$ \tag{17.147}, and $q_0=0$ (p. 547).

**Posterior (Gaussian completion).** The joint posterior is
$$p(q|yI)=\frac{\exp\{-Q/2\}}{\int dq_1\cdots dq_n\exp\{-Q/2\}}\tag{17.148}$$
$$Q\equiv(y-Gq)^TK(y-Gq)+(q-q_0)^TL(q-q_0)\tag{17.149}$$
which expands into eight terms \tag{17.150}:
$$Q=y^TKy-y^TKGq-q^TG^TKy+q^TG^TKGq+q^TLq-q^TLq_0-q_0^TLq+q_0^TLq_0$$
Write $Q=(q-\hat q)^TM(q-\hat q)+Q_0$ \tag{17.151} with $Q_0$ independent of $q$. Matching coefficients in $q$ (the equality must be an identity in $q$):
$$M=G^TKG+L,\quad M\hat q=G^TKy+Lq_0,\quad \hat q^TM\hat q+Q_0=y^TKy+q_0^TLq_0\tag{17.152}$$
$$\hat q=M^{-1}[G^TKy+Lq_0]\tag{17.153}$$
$$Q_0=y^TKy+q_0^TLq_0-\hat q^TM\hat q\tag{17.154}$$
$$p(q_1\cdots q_n|yKLI)=\frac{\sqrt{\det M}}{(2\pi)^{n/2}}\exp\{-\tfrac12(q-\hat q)^TM(q-\hat q)\}\tag{17.155}$$
(p. 547).

**Marginal for the interesting parameters.** $q_1,\dots,q_m$ are the seasonal amplitudes; $q_{m+1},\dots,q_n$ are trend nuisance parameters. Integrating out the latter:
$$p(q_1\cdots q_m|yKLI)=\int dq_{m+1}\cdots dq_n\,p(q_1\cdots q_n|yKLI)=\frac{\sqrt{\det M}}{(2\pi)^{n/2}}\frac{(2\pi)^{(n-m)/2}}{\sqrt{\det W}}\exp\{-\tfrac12(u-\hat u)^TU(u-\hat u)\}=\frac{\sqrt{\det U}}{(2\pi)^{m/2}}\exp\{-\tfrac12(u-\hat u)^TU(u-\hat u)\}\tag{17.156}$$
The text says $U,V,W,u$ are defined by equations whose numbers are left blank; the Editor's Exercise 17.4 asks the reader to define them. Because both forms are normalized,
$$\det(M)=\det(W)\det(U)\tag{17.157}$$
"a remarkable theorem not at all obvious from the definitions except in the case $V=0$". Jaynes calls this an example of probabilistic reasoning proving a purely mathematical theorem (p. 548).

**Computation rules (p. 548).** $K^{-1}$ is the $(N\times N)$ noise covariance, $L^{-1}$ is $(n\times n)$, and $F$ is the $(N\times n)$ matrix of model functions.
1. $M\equiv F^TKF+L$ \tag{17.158}, $(n\times n)$, in block form $M=\begin{pmatrix}U_0&V\\V^T&W_0\end{pmatrix}$ \tag{17.159}.
2. $U\equiv U_0-VW_0^{-1}V^T$ $(m\times m)$ \tag{17.160}; $W\equiv W_0-V^TU_0^{-1}V$ $(r\times r)$ \tag{17.161}.

These depend only on the model, so they can be computed before the data. Given $y$ $(N\times1)$ and $q_0$ $(n\times1)$:
$$\hat q=M^{-1}[F^TKy+Lq_0]\tag{17.162}$$
(p. 549). The first $m$ components are the interesting ones. The inverse has the same block form,
$$M^{-1}=\begin{pmatrix}U^{-1}&-U_0VW^{-1}\\-W_0V^TU^{-1}&W^{-1}\end{pmatrix}\tag{17.163}$$
(as printed), with $W\equiv W_0-V^TU_0^{-1}V$ \tag{17.164}. $F^T$ has the same block form in its rows \tag{17.165} (indices garbled in print). For $q_0=0$,
$$\hat q=RKy,\qquad R\equiv U^{-1}G-U_0^{-1}VW^{-1}T\tag{17.166, 17.167}$$
where $R$ is the reduced $(m\times N)$ matrix and $U^{-1}$ is the joint posterior covariance of $\{q_1,\dots,q_m\}$. $R$ and $U^{-1}$ can be computed before the data are available (p. 549).

*Intuition note.* Summing the quadratic forms and completing the square gives a Gaussian whose precision matrix is $M$. Dropping the trend parameters just means taking the Schur complement $U$.

The editor's Exercise 17.5 (p. 549) notes that Jaynes never finished this section and asks about $p(S(t)|yKLI)$ for $S(t)=\sum_{k=1}^mq_kG_k(t)$ \tag{17.168}.

### 17.12 Comments (pp. 550–552)
**Where orthodoxy suffices.** Sampling theory worked for the simple problems of Fisher in the 1930s. These had (a) few parameters, (b) sufficient statistics, (c) no important prior information, (d) no nuisance parameters. When all hold and $n\ge30$ ("say"), orthodox and Bayesian methods are essentially equivalent. Where these conditions fail, only Bayesian methods have the analytical apparatus to keep the relevant information (p. 550).

**Jaynes's charges against orthodoxy (pp. 550–551):**
- It claims to be "objective" and calls Bayes "subjective", yet it ignores prior information and works with unobservable limiting frequencies and imagined data sets.
- If there is no sufficient statistic, its accuracy claim ignores relevant evidence. Fisher's remedy of conditioning on ancillary statistics (a term the text does not define here) gives the same estimate that Bayes with a noninformative prior gives by a shorter calculation (p. 550). It is seldom possible, and where possible it is equivalent to Bayes' theorem (Chapter 8; Jeffreys for the Student $t$; Jaynes 1976 for the Cauchy) (p. 551).
- No failure of Bayesian methods has been found, and optimality theorems lead one to expect this (p. 550).
- The Gaussian case, where orthodoxy does best, dominated history and distorted the picture (pp. 550–551).
- Linear regression with both variables in error of unknown variance defeats sampling theory, because each new data point brings a new nuisance parameter. Kempthorne and Folks (1971) write 16 regression models and give up with "It is all very difficult" (p. 551).
- Jaynes says that leaving the Gaussian case opens a Pandora's box of anomalies, contradictions, absurd results and technical difficulties beyond sampling theory; several examples were already noted by Kendall and Stuart (1961) (p. 551).
- The quality of an estimate cannot be judged merely from the estimator's sampling distribution. That works only in simple Gaussian cases, by symmetry (p. 551).
- He says the orthodox literature invariably fails to recognize that all these difficulties are resolved by uniform application of the single Bayesian method. Once the Bayesian answer is known, one can often see how some ad hoc device acceptable to orthodoxy might have found it. He promises later chapters on the regression problem and on Cauchy sampling problems (p. 551).

**Criticism of Bayesians.** Much Bayesian writing keeps orthodox baggage, such as "random variable" and "$\theta$ is supposed uniformly distributed". In Jaynes's view $\theta$ is an unknown constant. What is distributed is our state of knowledge about it; calling $\theta$ "distributed" is, for him, another instance of the mind projection fallacy. Most real applications have no "random variables" or "true distribution", yet probability as logic applies (p. 552).

**Other remarks (p. 552).** Bayesian posterior probabilities or odds ratios tell quantitatively how strong the evidence is, using all evidence at hand. Savage (1962) reaches the Bayesian algorithm by a long argument using only sampling probabilities; Jaynes derives it from first principles. He urges jettisoning tradition and authority. Signs of hope: Bretthorst (1988) on magnetic resonance data, Zellner in econometrics, Lusted (1968) on Bayesian diagnosis, Cheeseman (1988) on expert systems. Osler: "Medicine is a science of uncertainty and an art of probability" (p. 552).

## Toy example (ours, not from the text)
Take $\overline{s^2}=1$, $\overline{t^2}=1$, $\overline{st}=0.5$ (so $r=0.5/\sqrt{1\cdot1}=0.5$). Suppose the data give $\overline{sy}=1$, $\overline{ty}=0$.

*Closed form (17.91), (17.122):* denominator $\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2}=1-0.25=0.75$.
- $\hat A=(1\cdot1-0.5\cdot0)/0.75=1.3333$.
- $\hat B=(1\cdot0-0.5\cdot1)/0.75=-0.6667$.

*Orthodox iteration (17.111)–(17.114):* $V_0=(\overline{sy}/\overline{s^2},\ \overline{ty}/\overline{t^2})=(1,0)$. Each step uses $A_{n+1}=1-0.5B_n$ and $B_{n+1}=0-0.5A_n$.
- $V_1=(1-0,\,-0.5)=(1,-0.5)$.
- $V_2=(1+0.25,\,-0.5)=(1.25,-0.5)$.
- $V_3=(1.25,\,-0.625)$.
- $V_4=(1+0.3125,\,-0.625)=(1.3125,-0.625)$.

The iterates approach $(1.3333,-0.6667)$. Check the fixed point: $1-0.5(-0.6667)=1.3333$ and $-0.5(1.3333)=-0.6667$. ✓.

*Posterior sd of $A$ (17.92)* with $N=10$, $\sigma=1$: $1/\sqrt{10\cdot1\cdot0.75}=1/\sqrt{7.5}\approx0.365$.

## Concepts
- [[nuisance-parameter]] (new) — a parameter we must model but do not want to estimate; Bayes integrates it out (p. 535, 537)
- [[marginalization]] (new) — integrate the joint posterior over unwanted parameters, e.g. $p(A|DI)=\int dB\,p(AB|DI)$ (p. 537)
- [[bayes-theorem]] — the single method Jaynes says resolves orthodox difficulties (pp. 533, 551)
- [[likelihood]] — here $\log L$ as a sum over the actual data points (p. 533)
- [[posterior-distribution]] — here its width reflects data range, unlike the orthodox sampling-based accuracy claim (p. 533)
- [[prior-distribution]] — for Jaynes it carries real prior information that orthodoxy ignores (p. 538)
- [[frequentist-vs-bayesian-inference]] — here "orthodox" means sampling theory, judging estimators by their sampling distribution (p. 533)
- [[monte-carlo-integration]] — estimating an integral by random points; here shown beaten by a grid (pp. 531–532)
- [[sufficient-statistic]] (new) — a data summary carrying all information about the parameters; $(\overline{y^2},\overline{sy},\overline{ty})$ here (p. 537)
- [[ancillary-statistic]] (new) — conditioning on it is Fisher's remedy; Jaynes says it is equivalent to Bayes when possible (p. 551)
- [[magnification]] (new) — test methods on an extreme problem where a small difference becomes obvious (p. 534)
- [[mind-projection-fallacy]] (new) — Jaynes's label for the persistent error of speaking as if $\theta$ were "distributed" when only our knowledge of $\theta$ is (p. 552; the text does not define the term further)
- [[probability-as-extended-logic]] — Jaynes's approach of applying probability theory directly as logic (pp. 533, 536, 552)

## Canonical instances
- [[grid-vs-monte-carlo]] (new) — grid with $n=100$ has the probable error of Monte Carlo with about 3000 points (p. 532)
- [[church-suicide-spurious-correlation]] (new) — both grow with population; correlation does not imply causation (p. 535)
- [[sinusoid-plus-trend-model]] (new) — $y=As+Bt+e$ solved fully by Bayes and orthodox methods (pp. 536–543)
- [[kempthorne-folks-regression]] (new) — 16 regression models for one inference problem (p. 551)

## Bridges (candidates)
- [same-math] Bayesian marginalization of $B$ and Gaussian completion with Schur complements ↔ linear algebra: the block-determinant identity $\det M=\det W_0\det U$ with $U$ the Schur complement (p. 548; see Reading notes on (17.157)).
- [same-math] Orthodox back-and-forth A↔B updating ↔ numerical linear algebra: Jacobi-type fixed-point iteration with a Neumann series $(I-M)^{-1}$ (p. 543).
- [structural-analogy] Detrending in order to estimate $A$ ↔ causal inference: regression adjustment for a confounder vs integrating over it. The spurious growth correlation (p. 535) is a common-cause pattern.
- [metaphor] Orthodox "averaging over unobserved data sets" ↔ information theory: ignoring the actual sequence's configuration, as in the typical-set picture (pp. 533, 551).

## Questions this raises
- When is the grid's $n^{-3/4}$ rate in §17.7 valid? What happens when $f$ is not smooth, or the dimension is high?
- Does the iterative A↔B equivalence extend to non-Gaussian likelihoods or to a general number of parameters? What replaces $M$ then?
- How does one compute $p(S(t)|yKLI)$ for the seasonal function itself, not just its amplitudes (Editor's Ex. 17.5)?
- How much does the diffuse-prior assumption behind (17.90) matter when the trend is poorly determined by the data?

## Exercises worth doing
- Editor's Ex. 17.4 (p. 548) — define $U,V,W,u$ by expanding the exponent of (17.155) in block form; builds Schur-complement fluency — difficulty: medium.
- Editor's Ex. 17.5 (p. 549) — posterior of the seasonal *function* $S(t)=\sum q_kG_k(t)$ via change of variables and marginalization — difficulty: hard.

## Reading notes
- **Scope.** This is the second half of Chapter 17. The unit starts at §17.7 (printed p. 531) and ends at the end of the chapter (printed p. 552, with footnotes 20–21). The split is at a section boundary. Page offset: printed = pdf − 30.
- **(17.77).** As printed, the integral has upper limit $\sqrt n$ and prefactor $\sqrt n$. By my check this does not give $1/(12n^2)$ as written. With limit $1/\sqrt n$ the integral alone gives $1/(12n)$, and a factor (step width)$^2=1/n$ gives $1/(12n^2)$. The value $1/(12n^2)$ is what (17.78)–(17.79) and the numbers use.
- **(17.107).** The last equality as printed reads $(1-r^2)A_0+\overline{se}/\overline{s^2}$. By my check, substituting (17.102)–(17.103) into the middle expression also leaves a term $-\overline{st}\,\overline{te}/(\overline{t^2}\,\overline{s^2})$. The printed (17.130) matches that fuller form.
- **(17.117).** The image shows the lower-left entry of $M$ as $+\overline{st}/\overline{t^2}$. (17.112), (17.114) and (17.120) imply $-\overline{st}/\overline{t^2}$, which I used (added step: this makes $\det(I-M)=1-r^2$, matching (17.120)).
- **(17.122).** The image prints the numerator as $\overline{s^2}\,\overline{ty}-\overline{ty}\,\overline{sy}$. This should be $\overline{st}\,\overline{sy}$, by (17.112) and the second row of (17.120).
- **(17.125)–(17.130).** The factors of $N$ look inconsistent. (17.125) has $1/N$ rather than $1/N^2$. (17.129) is printed as $\tilde A\pm\sigma\sqrt{\hat N\overline{s^2}(1-r^2)}$, which should presumably be $\sigma/\sqrt{N\overline{s^2}(1-r^2)}$ (the sd of (17.92)). $\tilde A$ is not defined on these pages (presumably $A_0$).
- **(17.128).** The printed form looks dimensionally off. My check gives $\overline{g^2}=\overline{t^2}/(\overline{s^2}\,\overline{t^2}-\overline{st}^{\,2})=1/(\overline{s^2}(1-r^2))$.
- **(17.147).** $L_{ij}=\sigma_j^2\delta_{ij}$ conflicts with $L^{-1}$ being the prior covariance (p. 547).
- **(17.163).** The off-diagonal blocks are printed without inverses ($-U_0VW^{-1}$, $-W_0V^TU^{-1}$); I would expect $U_0^{-1}$ and $W_0^{-1}$. (17.167) does show $U_0^{-1}$.
- **(17.165).** The index structure is garbled in print.
- **(17.157).** With $W$ defined as the Schur complement in (17.161), $\det M=\det W\det U$ would hold only for $V=0$. By my check the identity valid for any $V$ is $\det M=\det W_0\det U$, so the $W$ in (17.156)–(17.157) presumably means $W_0$.
- **Notation.** The matrix of model functions is called $G$ in (17.152) and $F$ in (17.158); (17.156) leaves $U,V,W,u$ undefined, as the editor notes.
- **(17.133).** It omits $\omega$ in the arguments, unlike (17.137).
- **Editor.** The boxed exercises are by the editor, not Jaynes.
