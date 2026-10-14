---
id: jaynes-2003-probability/ch17-principles-p1
work: jaynes-2003-probability
unit: "17 Principles and pathology of orthodox statistics (part 1/2) — §§17.1–17.6 (up to Eq. 17.69 and Editor's Exercise 17.3)"
pages: 509–530
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Principles and pathology of orthodox statistics (part 1/2)

## L0 — One line
In simple problems, orthodox sampling-theory tools (unbiased estimators, tail-area significance tests, pre-filtering) waste, ignore or distort information, whereas Bayes' theorem has all the relevant information available; the Cramér–Rao bound turns out to be tied to maximum-entropy distributions.

## L1 — The gist (≤ 120 words)
Jaynes asks when and how orthodox results differ from Bayesian ones, and what that costs in practice. He argues that any estimator that is not a sufficient statistic discards information. Jaynes claims insisting on zero bias costs about half the data in variance estimation (an editor's footnote disputes the calculation). Unbiased estimators can be absurd in the Poisson problem. The Cramér–Rao equality condition leads back to maximum-entropy distributions. Fisher's periodogram test misses an obvious 20-year cycle in Central Park temperatures, and a moving average distorts that cycle. He then sets up a Bayesian model of the same data. The point: judge methods by what they do with the information in the data and prior knowledge.

**Prerequisites:** expectation and variance; Gaussian and Poisson distributions; Schwarz inequality; discrete Fourier transform; Bayes' theorem with nuisance parameters; maximum-entropy distributions (Jaynes ch. 11). Terms used below: unbiased = correct on average over repeated samples; sufficient statistic = a summary that keeps all the information about the parameter; tail-area test = a test that computes a P-value only under a null hypothesis; periodogram = squared size of the Fourier transform of the data, divided by n; moving average = replacing each value by a weighted average of recent values; nuisance parameter = an unknown parameter we are not interested in and integrate out.

## L2 — Key ideas
- An estimator that is not a sufficient statistic loses information. Bayes' theorem has all possible estimators available at once, so, when no sufficient statistic exists, it is able to choose the optimal estimator for the data in hand (p. 510).
- Mean-square error is bias² plus sampling variance, two terms on an equal footing. Removing bias with $M_2=\frac{n}{n-1}m_2$ raises the variance term. Among multiples of $m_2$, the best has $c=n/(n+1)$ for Gaussian data (pp. 511–513).
- Jaynes claims the unbiased estimator needs about 203 observations to match 100 for the biased one. The editor's footnote says (17.16) was miscalculated, so this claim is doubtful (p. 513 and fn. 2).
- Bias is not invariant under reparametrization. In the Poisson problem the unique unbiased estimators of $l^2$, $l^3$, $e^{-l}$ are absurd or contradict logic, and none exists for $1/l$; the Bayes estimates are well-behaved (pp. 515–517).
- The Cramér–Rao bound follows from the Schwarz inequality. Equality holds exactly when $p(x|\alpha)$ has the maximum-entropy (exponential) form, which is also the Pitman–Koopman condition for sufficiency (pp. 518–520).
- Fisher's peak/mean periodogram test uses only probabilities under a "no periodicity" null. It calls the obvious Central Park 20-year cycle not significant (pp. 521, 523–526).
- A 10-year moving average multiplies the Fourier transform of the data by $W(\omega)$. It erases a 10-year cycle and shrinks and shifts a 20-year one (pp. 521–523).
- The Bayesian model $y_t=\mu+A\cos\omega t+B\sin\omega t+e_t$ has four data sums as sufficient statistics. Weak priors suffice and nuisance parameters are integrated out (pp. 527–530).

## L3 — Walkthrough

### Introduction (p. 509)
- The epigraph is Wiener (1948). Likelihood "tricks" appear to avoid Bayes' law but transfer the responsibility for using it to the statistician or end user (p. 509).
- Jaynes says orthodox objections to Bayes were philosophical, never about actual results. He promises to be fair: he will acknowledge good orthodox results and complain only when a result "insults our intelligence" (p. 509).
- His questions: in what circumstances do orthodox and Bayesian results differ, and with what practical consequences? Cox's theorems supply all the ideology needed (p. 509).

### 17.1 Information loss (pp. 510–511)
- Orthodoxy is, in Jaynes's view, a loose collection of ad hoc devices that often disagree with each other (p. 510).
- **Setup:** estimate $\theta$ from $D=\{x_1,\dots,x_n\}$, a point in $\mathbb R^n$. Orthodoxy picks one estimator $b(D)$ before seeing the data. Fixing the value of $b$ puts the sample on a manifold of dimension $n-1$. $D$ itself also says where on that manifold the sample lies (p. 510).
- If position on the manifold is irrelevant to $\theta$, $b$ is a sufficient statistic (it carries all the information about $\theta$). Then, barring cogent prior information, the orthodox method is pragmatically satisfactory. Otherwise $D$ carries information about $\theta$ that $b(D)$ does not (p. 510).
- Given $D$, all candidate estimators $b_1,b_2,\dots$ are known. So Bayes' theorem uses the information of all estimators simultaneously and, if there is no sufficient statistic, is able to choose the optimal estimator for this data set (p. 510).
- If the estimator is not sufficient, its sampling distribution is irrelevant, since different data sets would lead to different estimators (Chapters 8, 13). The same holds for hypothesis tests; Jaynes expects the Bayesian procedure to be more accurate or reliable (p. 510).
- Camps: Neyman–Pearson (unbiased estimators, confidence intervals, decision-theoretic tests; Simon, Lehmann, Middleton). Fisherian (maximum likelihood, ANOVA, randomization, tail-area tests, fiducial probability, conditioning on ancillary statistics). Jaynes states that conditioning on ancillary statistics is mathematically equivalent to Bayes' theorem without prior information (pp. 510–511).

> **Intuition note.** A single pre-chosen summary of the data is like looking at a photo through a keyhole. Bayes' theorem looks at the whole photo. The keyhole is harmless only when the summary is sufficient.

### 17.2 Unbiased estimators (pp. 511–516)
- **Definition (unbiased).** For a sampling distribution $p(x|\alpha)$ and estimator $\beta(D)$:
$$\langle\beta\rangle=E(\beta)=\int dx_1\cdots dx_n\,\beta(x_1,\dots,x_n)\,p(x_1\cdots x_n|\alpha)=\alpha.\tag{17.1}$$
- **Mean-square error** (from Eq. 13.20), the sum of squared bias and the variance of the sampling distribution of $\beta$ (p. 511):
$$\langle(\beta-\alpha)^2\rangle=(\langle\beta\rangle-\alpha)^2+\operatorname{var}(\beta),\qquad \operatorname{var}(\beta)=\langle\beta^2\rangle-\langle\beta\rangle^2.\tag{17.2}$$
  Jaynes assumes the needed moments exist, so the problem here is logical, not mathematical, pathology. The two terms are on equal footing; unbiasedness removes one term but need not minimize the total (p. 511).
- **Cramér's example:** estimate the variance $\mu_2$ of $p(x_1|\mu_2)$ from $n>1$ independent observations, with $\langle x_1\rangle=0$ by a change of variables (p. 511):
$$\mu_2=\langle x_1^2\rangle-\langle x_1\rangle^2=\langle x_1^2\rangle.\tag{17.3}$$
  The variance of the sample is
$$m_2\equiv\overline{x^2}-\overline{x}^2=\frac1n\sum_{i=1}^n x_i^2-\Big[\frac1n\sum_{i=1}^n x_i\Big]^2,\tag{17.4}$$
$$\langle m_2\rangle=\frac{n-1}{n}\mu_2,\tag{17.5}$$
  so $m_2$ has negative bias. The orthodox correction, now usually called "sample variance", is
$$M_2\equiv\frac{n}{n-1}m_2.\tag{17.6}$$
  For $n=1$, $m_2=0$ (pp. 511–513).
- **Cost of the correction.** $M_2$ removes the term $(\langle m_2\rangle-\mu_2)^2=\mu_2^2/n^2$ but multiplies $\operatorname{var}(m_2)$ by $[n/(n-1)]^2$. Jaynes says this seems clearly worse, at least for large $n$ (p. 512).
- **Best multiple.** Take $\beta=c\,m_2$ (17.7). Then
$$\langle(cm_2-\mu_2)^2\rangle=c^2\langle m_2^2\rangle-2c\langle m_2\rangle\mu_2+\mu_2^2=\langle(m_2-\mu_2)^2\rangle-\langle m_2^2\rangle(\hat c-1)^2+\langle m_2^2\rangle(c-\hat c)^2,\tag{17.8}$$
$$\hat c\equiv\frac{\mu_2\langle m_2\rangle}{\langle m_2^2\rangle}.\tag{17.9}$$
  So $c=\hat c$ is best in this class, and $\hat\beta\equiv\hat c\,m_2$ gains $\langle m_2^2\rangle(\hat c-1)^2$ over $m_2$ (p. 512). (added step: the first line expands the square; the second completes the square in $c$.)
- Fourth central moment and second moment of $m_2$:
$$\langle m_2^2\rangle=n^{-3}(n-1)\big[(n^2-2n+3)\mu_2^2+(n-1)\mu_4\big],\tag{17.10}$$
$$\mu_4\equiv\langle(x_1-\langle x_1\rangle)^4\rangle=\langle x_1^4\rangle.\tag{17.11}$$
  Then, with $K\equiv\mu_4/\mu_2^2\ge1$,
$$\hat c=\frac{n^2}{n^2-2n+3+(n-1)K}.\tag{17.12}$$
  $\hat c$ decreases with $K$. If $K\ge2$, then $\hat c<1$ for all $n$, so instead of removing the bias one should increase it (p. 513).
- **Gaussian case:** $K=3$, so
$$\hat c=\frac{n}{n+1}\tag{17.13}$$
  and Jaynes says the bias should be approximately doubled. (added step: the bias of $\hat\beta$ is $\frac{n}{n+1}\cdot\frac{n-1}{n}\mu_2-\mu_2=-\frac{2}{n+1}\mu_2$, versus $-\mu_2/n$ for $m_2$.) Errors (p. 513):
$$\langle(\hat\beta-\mu_2)^2\rangle=\frac{2\mu_2^2}{n+1},\tag{17.14}$$
$$c=\frac{n}{n-1},\qquad\langle(M_2-\mu_2)^2\rangle=\mu_2^2\Big[\frac{2}{n+1}+\frac2n\Big].\tag{17.15, 17.16}$$
  Jaynes concludes this is over twice the error of $\hat\beta$, and that with $M_2$ one needs $n=203$ to match $\hat\beta$ at $n=100$. He says half the data are effectively thrown away, and more so if tails are wider ($K>3$) (pp. 513–514).
- **Caution (editor's footnote 2, p. 513):** the editor says Jaynes mistakenly computed (17.16); the correct value is $\langle(M_2-\mu_2)^2\rangle=2\mu_2^2/(n-1)$. (added step: relative to (17.14) this ratio is $(n+1)/(n-1)$, close to 1 for large $n$, so the "twice", "203 vs 100" and "half the data" claims do not follow from the footnote's value.) Jaynes's own text does not retract them.
- **Footnote 1 (p. 513).** In Bayesian theory a single observation could inform $\mu_2$ if $\mu_2$ is correlated in the prior with another parameter about which one observation is informative.
- **Why the bias fixation?** Jaynes suspects a "psychosemantic trap": the word "bias" sounds reprehensible. Calling it "component of error orthogonal to the variance" would show the two are equal partners in the Pythagorean (17.2). Valavanis (1959) advocates discarding practically all data if needed to remove bias. Chernoff and Moses's telephone-cable example: overestimating costs excess cable, underestimating may be a financial disaster, so an unbiased estimate would be foolhardy and a Wald-type decision theory is needed (p. 514).
- **The long-run-average defense.** The belief is that the mean of $N$ estimates converges to $\langle\beta\rangle$. Jaynes says this is almost never justified: systematic error, and measurements lacking the independence the limit theorems need. In economics there are no true "asymptotic sampling properties", as the population is finite and changing (pp. 514–515). What matters is the actual state of knowledge; to reject it as "subjective" is to destroy useful results, "for human information is all we have" (p. 515).
- Many biased estimators, including $\hat\beta$, also converge to the truth, and faster. The relevant question is how rapidly, not whether (p. 515).
- **Fisher's invariance argument** (Eq. 6.94): the square of an unbiased estimate of $\alpha$ is not an unbiased estimate of $\alpha^2$. For $\alpha^k$ the conclusions can differ arbitrarily, so two people choosing different $k$ get different answers from the same data. Footnote 5 notes that the posterior-mean criterion has the same ambiguity; it disappears once the loss function is transformed with the parameter (Chapter 13) (p. 515).
- **Footnote 3 (p. 514).** In the Bayesian version, with brackets as posterior expectations, $\langle(\beta-\alpha)^2\rangle=(\beta-\langle\alpha\rangle)^2+\operatorname{var}(\alpha)$. Here $\operatorname{var}(\alpha)$ does not depend on $\beta$, so the optimum over all estimators is $\beta=\langle\alpha\rangle$.
- **Limits of the argument.** $\hat\beta$ is best only within the class (17.7). Whether some other function of the data does better remains open; orthodoxy compares guesses but gives no way to find the best estimator (p. 515). The Bayesian procedure builds the optimal estimator for any data set and loss, with a proof of optimality over all estimators, and without reference to bias (p. 516). Exercise 17.1 asks about this (p. 516).

> **Intuition note.** Total error is what matters, and bias and variance are just two parts of it. Trading a little bias for a larger drop in variance can lower the total. Here that trade pushes the multiplier below the "unbiased" $n/(n-1)$.

### 17.3 Pathology of an unbiased estimate (pp. 516–518)
- Poisson: $p(n|l)=e^{-l}l^n/n!$, $\langle n\rangle=l$ (17.17). Unbiasedness of $f(n)$ for $l$ requires
$$\sum_{n=0}^\infty e^{-l}\frac{l^n}{n!}f(n)=l,\tag{17.18}$$
  and matching Taylor coefficients gives the unique solution
$$f(n)=\frac{d^n}{dl^n}\{l\,e^{l}\}\Big|_{l=0}=n.\tag{17.19}$$
  For a function $g(l)$ the unique unbiased estimator is
$$f(n)=\frac{d^n}{dl^n}\{e^{l}g(l)\}\Big|_{l=0}.\tag{17.20}$$
- For $l^2$:
$$f(n)=\begin{cases}0 & n=0,1\\ n(n-1)& n>1\end{cases}\tag{17.21}$$
  which is absurd for $n=1$. For $l^3$ it is absurd for $n=1,2$. Observing $n=2$ gives the estimate $l^3=0$, yet $l^3=0$ would make $n=2$ impossible (p. 517).
- For $e^{-l}$ the only unbiased estimator is
$$f(n)=\begin{cases}1&n=0\\0&n>0\end{cases}\tag{17.22}$$
  absurd for all $n>0$. For $1/l$ no unbiased estimator exists. Jaynes: unbiased estimators can conflict with deductive logic for all data sets (p. 517).
- **Remedy.** With a uniform prior the posterior mean of $g(l)$ is
$$\langle g(l)\rangle=\frac1{n!}\int_0^\infty dl\,e^{-l}l^n g(l).\tag{17.23}$$
  The Bayes estimate of $1/l$ is $1/n$ (added step: $\frac1{n!}\int e^{-l}l^{n-1}dl=\frac{(n-1)!}{n!}$, valid for $n\ge1$; for $n=0$ the integral diverges). The Bayes estimate of $e^{-l}$ is
$$f(n)=2^{-(n+1)}.\tag{17.24}$$
  (added step: $\frac1{n!}\int e^{-2l}l^n\,dl=2^{-(n+1)}$.) Why not $e^{-n}$? Two reasons (p. 517):
  1. The posterior is skewed:
$$P(l>n)=\int_n^\infty dl\,e^{-l}\frac{l^n}{n!}=e^{-n}\sum_{m=0}^n\frac{n^m}{m!},\tag{17.25}$$
     falling from 1 at $n=0$ to $1/2$ as $n\to\infty$. So $l>n$ is always more likely than $l<n$.
  2. $e^{-l}$ varies fast, so the integral $\int e^{-2l}l^n\,dl$ is dominated by about $n/2\pm\sqrt n/2$, and $e^{-n/2}$ is closer than $e^{-n}$. (17.24) is the balance of these two effects (pp. 517–518).
- Exercise 17.2 (truncated Poisson, 17.26) is on p. 518. Kendall and Stuart (1961) noted other pathologies but did not examine the Bayesian results, which Jaynes says handle all of them easily (p. 518).

> **Intuition note.** Unbiasedness only demands correct averages over all possible data. It does not demand a sensible answer for the data actually seen. Bayes' theorem conditions on the observed $n$, and in these examples its answers do not contradict the data.

### 17.4 The fundamental inequality of the sampling variance (pp. 518–520)
- The bound (Cramér, Rao, Darmois, Fréchet and others) is almost the only connected theory orthodoxy has to guide it (p. 518). Let
$$u(x,\alpha)\equiv\frac{\partial\log p(x|\alpha)}{\partial\alpha}.\tag{17.27}$$
- **Schwarz inequality:** with $(f,g)\equiv\int dx\,f g$, $(f,g)^2\le(f,f)(g,g)$, with equality iff $f=qg$ ($q$ independent of $x$, possibly depending on $\alpha$) (p. 518, proof in fn. 7). Take
$$f\equiv u\sqrt{p(x|\alpha)},\qquad g\equiv[\beta(x)-\langle\beta\rangle]\sqrt{p(x|\alpha)}.\tag{17.28}$$
  Then $(f,g)=\langle\beta u\rangle-\langle\beta\rangle\langle u\rangle=\langle\beta u\rangle$, because $\langle u\rangle=\partial_\alpha\!\int dx\,p=0$; $(f,f)=\operatorname{var}(u)$; $(g,g)=\operatorname{var}(\beta)$. Hence
$$\langle\beta u\rangle\le\sqrt{\operatorname{var}(\beta)\operatorname{var}(u)}.\tag{17.29}$$
  Also $\langle\beta u\rangle=d\langle\beta\rangle/d\alpha=1+b'(\alpha)$ with bias $b=\langle\beta\rangle-\alpha$ (pp. 518–519), so
$$\operatorname{var}(\beta)\ge\frac{[1+b'(\alpha)]^2}{\int dx\,(\partial\log p(x|\alpha)/\partial\alpha)^2\,p(x|\alpha)}.\tag{17.30}$$
  (The image prints the denominator integral with $d\alpha$, an apparent misprint for $dx$; see Reading notes.)
- **Equality condition.** Substituting (17.27) into $f=qg$ and defining $l(\alpha)$ by $q=-\partial l/\partial\alpha$:
$$\frac{\partial\log p(x|\alpha)}{\partial\alpha}=-l'(\alpha)[\beta(x)-\langle\beta\rangle],\tag{17.31}$$
$$\log p(x|\alpha)=-l(\alpha)\beta(x)+\int dl\,\langle\beta\rangle+\text{const}.\tag{17.32}$$
  Write the integral as $-\log Z(\alpha)$ and the constant (independent of $\alpha$, may depend on $x$) as $\log m(x)$. Then equality in (17.30) holds iff
$$p(x|\alpha)=\frac{m(x)}{Z(l)}\exp\{-l(\alpha)\beta(x)\},\tag{17.33}$$
$$Z(l)=\int dx\,m(x)\exp\{-l\beta(x)\},\qquad\langle\beta\rangle=-\frac{\partial\log Z}{\partial l}.\tag{17.34, 17.35}$$
  Jaynes recognizes this as the maximum-entropy distribution of Chapter 11 with constraint fixing $\langle\beta(x)\rangle$; (17.35) is identical with (11.60). For vector $\alpha,\beta$ the exponent becomes $-\sum_i l_i(\alpha)\beta_i(x)$, as in (11.43) (p. 519).
- **Unity of principles.** Sufficiency can be defined through Shannon entropy (Chapter 14). The Pitman–Koopman theorem says a sufficient statistic exists iff the sampling distribution has the form (17.32) (pp. 519–520). So assigning sampling distributions by maximum entropy yields distributions that are best both for sampling theory (minimum possible variance) and for Bayes (only one function of the data is needed) (p. 520).
- A maximum-entropy distribution built from constraints fixing $\langle\beta_1\rangle,\dots,\langle\beta_k\rangle$ has $k$ sufficient statistics, namely $\beta_1(x),\dots,\beta_k(x)$ evaluated on the observed data. Jaynes cites (1978, Eq. B82) and leaves the proof as an exercise (p. 520).
- **If $p(x|\alpha)$ lacks form (17.33):** if it is continuous in $\alpha$, the bound cannot be attained and Jaynes says there seems to be no theory for the correct lower bound or for an estimator achieving it. For unbiased $\beta$, Fisher called the ratio of the bound to $\operatorname{var}(\beta)$ the *efficiency*; efficiency 1 is an "efficient" or UMV estimator. Efficiency is even more parameter-dependent than unbiasedness (fn. 8). If $p$ has discontinuities, Cramér finds estimators beating the bound. Jaynes calls this a mathematical error: a limit of continuous functions would add a delta-function term that restores the inequality (Appendix B) (p. 520).

> **Intuition note.** The bound can be reached only for a very special family of distributions, the exponential (maximum-entropy) form. For these, one number $\beta(x)$ per constraint holds all the information about the parameter. For other continuous families, the bound cannot be attained.

### 17.5 Periodicity: the weather in Central Park (pp. 520–526)
- **Problem.** Does data over time show periodicity? It is controversial whether this is a significance-test or parameter-estimation problem; schools reach opposite conclusions (p. 521).
- **Example (Bloomfield 1976, p. 110):** mean January temperatures over about 100 years. A cycle of roughly 20 years, peak-to-peak about $4^\circ$F against noise of about $0.5^\circ$F, is, Jaynes says, evident to the eye. Bloomfield, using a Fisher significance test, concludes there is no significant evidence of periodicity (p. 521).

#### 17.5.1 The folly of pre-filtering data (pp. 521–523)
- The plotted data were pre-filtered by a 10-year moving average. For raw data $y_1,\dots,y_n$ the discrete Fourier transform is
$$Y(\omega)\equiv\sum_{t=1}^n y_t e^{i\omega t},\tag{17.36}$$
  periodic in $\omega$ with period $2\pi$. The values at $n$ Nyquist frequencies
$$\omega_k\equiv 2\pi k/n,\quad 0\le k<n\tag{17.37}$$
  contain all the information. By orthogonality, $n^{-1}\sum_k e^{i\omega_k(s-t)}=\delta_{st}$, and the data are recovered by
$$\frac1n\sum_{k=1}^nY(\omega_k)e^{-i\omega_kt}=y_t,\quad1\le t\le n.\tag{17.38}$$
- **Moving average** with weights $w_s$ (zero-padding convention in fn. 10, which makes all formulas exact):
$$z_t\equiv\sum_{s=0}^{m-1}y_{t-s}w_s,\tag{17.39}$$
$$Z(\omega)=\sum_t z_te^{i\omega t}=W(\omega)Y(\omega),\qquad W(\omega)\equiv\sum_{s=0}^{m-1}w_se^{i\omega s}.\tag{17.40, 17.41}$$
  This is the convolution theorem (p. 522). For uniform weights $w_s=1/m$ (17.42):
$$W(\omega)=\frac1m\sum_{s=0}^{m-1}e^{-i\omega s}=\exp\Big\{-i\frac\omega2(m-1)\Big\}\frac{\sin(m\omega/2)}{m\sin(\omega/2)}.\tag{17.43}$$
  For $m=10$:
$$W(2\pi/10)=0,\qquad W(2\pi/20)=0.639\,e^{-9\pi i/20}.\tag{17.44}$$
- **Consequences** (p. 522). A 10-year average completely wipes out evidence of a 10-year cycle. It cuts the amplitude of a 20-year cycle by the factor 0.639 and shifts its phase by $9\pi/20=1.41$ rad. Because $|W|$ is decreasing at $\omega=2\pi/20$, the peak of $Z$ lies at a lower frequency than the true peak of $Y$. Jaynes infers the raw amplitude was about $4/0.639=6.3^\circ$F, nearly $90^\circ$ out of phase with the graph, and the true frequency somewhat higher than the graph suggests.
- Pre-filtering only makes graphs look prettier; for computer analysis it discards or distorts information. A 10-year period (cf. sunspots) could be wiped out (pp. 522–523).
- **Fisher's test.** Periodogram:
$$P(\omega)\equiv\frac1n|Y(\omega)|^2=\frac1n\sum_{t,s}y_ty_se^{i\omega(t-s)},\tag{17.45}$$
  with $P(0)=(\sum y_t)^2/n=n\bar y^2$ and
$$\langle P(\omega_k)\rangle_{av}=\frac1n\sum_{k=1}^nP(\omega_k)=\overline{y^2}.\tag{17.46}$$
  Test statistic and P-value:
$$q=\frac{P(\omega_k)_{\max}}{P(\omega_k)_{av}},\tag{17.47}$$
$$P\equiv p(q>q_0|H_0)=\int_{q_0}^\infty dq\,p(q|H_0),\tag{17.48}$$
  where $H_0$ says the data are Gaussian white noise. If $P>0.05$, periodicity is rejected as "not significant at the 5% level" (p. 523).
- **Jaynes's critique** (pp. 523–524):
  - The test uses only probabilities conditional on $H_0$. It takes no note of the probability of the data if a periodicity is present, nor of prior information. Jaynes asks (a rhetorical question) how one can test any hypothesis rationally without specifying (1) the hypothesis, (2) the alternatives and (3) the prior information, and says that until this is done no definite, well-posed question has been asked.
  - $H_0$ treats the data as a stationary Gaussian process with no periodic term, so even a second cycle of a wave would be pure chance. Real interest in periodicity concerns a repeating physical influence, so $H_1$ is "quite unrelated" to $H_0$.
  - Procedure: invent a null denying the effect, then argue against it without reference to $H_1$. If $H_0$ is rejected, so are probabilities conditional on $H_0$: "Orthodox logic saws off its own limb." (p. 524)
  - Jeffreys (1939): "An hypothesis that may be true is rejected because it has failed to predict observable results that have not occurred." (p. 524)
  - Footnote 14 reports that an historical study suggested the culprit behind this style of reasoning was the physicist Schuster (1897), who invented the periodogram. Jaynes says the information is in the *shape* of the periodogram, not its sampling distribution.
- **Prior information** (pp. 524–525). Possible mechanism: the sunspot cycle (about 11 years, perhaps a rectified 22-year cycle) changes charged-particle flux, ion concentration, raindrop nuclei, cloud cover and temperature. Jaynes says he does not claim to firmly believe it is the dominant mechanism, only that it is conceivable, does not violate known physics, and has a magnitude that is hard to estimate theoretically. It prepares us not to be surprised by a cycle in Central Park, and suggests July temperatures might show even better evidence. Fn. 13: an apparent periodicity can be checked for reproducibility, which a physicist can usually do and an economist usually cannot.
- Jaynes says a person trained only in orthodox statistics would not hesitate to treat astronomical, atmospheric and weather data as independent; a scientist with prior knowledge of astrophysics and meteorology would not. If journals reject first mild evidence for failing a 5% test "in itself", the confirmatory observations will, in all probability, never be made, and an important discovery could be delayed by a century (p. 525).
- **Feller's account** (II, pp. 76–77; pp. 525–526). Expand $y_t=\sum_{j=1}^n(A_j\cos\omega_jt+B_j\sin\omega_jt)$ (17.49). Feller's "old wrong way": assume $A_j,B_j\sim N(0,\sigma)$ iid, so each $R_j^2=A_j^2+B_j^2$ is exponential with mean $2\sigma^2$, and call a large $R_j$ a "hidden periodicity". Feller, following Fisher, says the maximum of $n$ observations does not have the distribution of one. Feller's 'right' quantities are $V_j=R_j^2/\sum_iR_i^2$ (17.50), distributed like the $n$ segments cut from $(0,1)$ by $n-1$ random points; covering theorems give $P(\text{all }V_j<a)$. Jaynes replies: both "old wrong" and "new right" sampling distributions are irrelevant, because prior information and the likelihood function are not mentioned. He says Feller apparently doubted the sunspot periodicity, which, Jaynes says, no responsible scientist has doubted for over a century (p. 526). Fn. 16: "iid" is another form of the mind projection fallacy, since each coefficient is a definite number known from the data.
- Fisher's test fails to detect the evident Central Park cycle. Jaynes cites Jaynes (1976) on Crow, Davis and Maxfield (1960): the eyeball is a more reliable indicator than an orthodox equal-tails test, and the Bayesian test confirms quantitatively what the eye sees (p. 526).

> **Intuition note.** A moving average multiplies each frequency component by a known factor, which can be zero or small. Information at those frequencies is gone for good. The Fisher test also asks whether the data look like pure noise, rather than how well a cycle explains the data.

### 17.6 A Bayesian analysis (pp. 527–530)
- **Model.** Possible periodic term $A\cos\omega t+B\sin\omega t$ (17.51), $|\omega|\le\pi$. Irregular components $e_t$ are uncontrollable and unpredictable, so a Gaussian sampling distribution with parameters $(\mu,\sigma)$ is assigned (Chapter 7). $\mu$ and $\sigma$ are nuisance parameters, to be integrated out (p. 527):
$$y_t=\mu+A\cos\omega t+B\sin\omega t+e_t,\quad1\le t\le n,\tag{17.52}$$
$$p(e_1\cdots e_n|\mu\sigma I)=\Big(\frac1{2\pi\sigma^2}\Big)^{n/2}\exp\Big\{-\frac1{2\sigma^2}\sum_te_t^2\Big\},\tag{17.53}$$
$$p(y_1\cdots y_n|\mu\sigma I)=\Big(\frac1{2\pi\sigma^2}\Big)^{n/2}\exp\Big\{-\frac Q{2\sigma^2}\Big\},\tag{17.54}$$
$$Q(A,B,\omega)\equiv\sum_t(y_t-\mu-A\cos\omega t-B\sin\omega t)^2,\tag{17.55}$$
$$Q=n\Big[\overline{y^2}-2\bar y\mu+\mu^2-2A\overline{y_t\cos\omega t}-2B\overline{y_t\sin\omega t}+2\mu A\overline{\cos\omega t}+2\mu B\overline{\sin\omega t}+2AB\overline{\cos\omega t\sin\omega t}+A^2\overline{\cos^2\omega t}+B^2\overline{\sin^2\omega t}\Big],\tag{17.56}$$
  overbars being averages over $t$ (p. 528).
- Of the nine sums, four involve the data ($\overline{y^2},\bar y,\overline{y_t\cos\omega t},\overline{y_t\sin\omega t}$). These are the jointly sufficient statistics for all five parameters; the other five can be computed beforehand. The extra detail is all relevant, and the exact solution is easy for a computer (p. 528).
- **Priors** (pp. 528–530). $A,B<200^\circ$F, since otherwise New York City would not exist; this alone gives proper priors. The phase $\theta=\tan^{-1}(B/A)$ gets a uniform prior. By Chapter 6 Exercise 6.6, further prior information narrowing the range makes a numerically negligible difference unless it cuts the range to something like $30^\circ$F. A Herschel-type argument gives
$$p(AB|I)=\frac1{2\pi\delta^2}\exp\Big\{-\frac{A^2+B^2}{2\delta^2}\Big\},\quad\delta\sim100^\circ\text{F}.\tag{17.57}$$
- **General Bayes** (p. 529):
$$p(AB\omega\mu\sigma|DI)=p(AB\omega\mu\sigma|I)\frac{p(D|AB\omega\mu\sigma I)}{p(D|I)},\tag{17.58}$$
$$p(AB\omega|DI)=\int d\mu\int d\sigma\,p(AB\omega\mu\sigma|DI).\tag{17.59}$$
  Factoring the prior, $p(AB\omega\mu\sigma|I)=p(AB\omega|I)\,p(\mu\sigma|AB\omega I)$ (17.60), gives
$$p(AB\omega|DI)=C\,p(AB\omega|I)\,L^*(A,B,\omega),\tag{17.61}$$
$$L^*(A,B,\omega)\equiv\int d\mu\int d\sigma\,p(\mu\sigma|AB\omega I)\,p(D|AB\omega\mu\sigma I).\tag{17.62}$$
  Knowing the periodic parameters says nothing about $(\mu,\sigma)$, so
$$p(\mu\sigma|AB\omega I)=p(\mu\sigma|I).\tag{17.63}$$
- **Prior for $(\mu,\sigma)$.** Both are below $200^\circ$F; $\sigma$ is not as small as $10^{-6\circ}$F (real thermometers). Gaussian in $\mu$ (location parameter), truncated Jeffreys prior in $\sigma$ (the uniquely uninformative prior for a scale parameter, Chapter 12); $\alpha,b\sim100^\circ$F, $a\simeq10^{-6}$:
$$p(\mu\sigma|I)\propto\frac1{\sigma\sqrt{2\pi\alpha^2}}\exp\{-\mu^2/2\alpha^2\},\quad a\le\sigma\le b.\tag{17.64}$$
  Jaynes expects most of this care to prove unnecessary (p. 530).
- **Quasi-likelihood:**
$$L^*(A,B,\omega)=\int_{-\infty}^\infty d\mu\,e^{-\mu^2/2\alpha^2}\int_a^b\frac{d\sigma}{\sigma^{n+1}}e^{-Q/2\sigma^2}.\tag{17.65}$$
  For $n>0$ the $\sigma$-integral converges at both ends, so the finite limits are unnecessary:
$$\int_0^\infty\frac{d\sigma}{\sigma^{n+1}}e^{-Q/2\sigma^2}=\frac12\frac{(n/2-1)!}{(Q/2)^{n/2}}.\tag{17.66}$$
  Do the $\mu$-integral first, writing
$$Q=n[s^2+(\mu-\bar d)^2].\tag{17.67}$$
  The part ends here. Editor's Exercise 17.3 (p. 530) asks for $s^2=\overline{d^2}-\bar d^2$ (17.68) with effective data $d_i=y_i-A\cos\omega t_i-B\sin\omega t_i$ (17.69), the marginals $p(AB\omega|DI)$ and $p(\omega|DI)$, and a way to decide whether a resonance exists.

> **Intuition note.** The Bayesian model puts a periodic term plus noise in the likelihood. The data enter only through four averages. Priors are generous (scales of order 100 °F, with $A,B<200$ °F) but proper, and integrating out $\mu$ and $\sigma$ leaves a posterior over $(A,B,\omega)$.

## Toy example (ours, not from the text)
Poisson counts, one observation $n=1$.
- Unbiased estimator of $l^2$ from (17.21): $f(1)=0$. Check unbiasedness at $l=1$: $\langle n(n-1)\rangle=e^{-1}\sum_{n\ge2}\frac{n(n-1)}{n!}=e^{-1}\sum_{n\ge2}\frac1{(n-2)!}=e^{-1}\cdot e=1=l^2$. ✓.
- Yet an estimate of $l^2=0$ means $l=0$, where $p(1|0)=e^{0}\cdot0^1/1!=0$. The data would be impossible.
- Bayes (uniform prior, 17.23): $\langle l^2\rangle=\frac1{1!}\int_0^\infty e^{-l}l^{1+2}dl=3!=6$. Posterior mean of $l$ is $\frac1{1!}\int e^{-l}l^2\,dl=2$. Bayes estimate of $e^{-l}$ is $2^{-(1+1)}=0.25$, while the unbiased rule (17.22) gives 0.
- Result: unbiasedness over repeated samples can produce a value the observed data rule out. Conditioning on the observed $n$ does not do so in this example.

## Concepts
- [[frequentist-vs-bayesian-inference]] — here: orthodox sampling-theory methods compared with Bayes on actual results and on information use (p. 509)
- [[bayes-theorem]] — has available all the information in the data and, jointly, in all possible estimators (p. 510)
- [[likelihood]] — the evidence of the data as a function of the parameters; not used by the orthodox tail-area test (p. 523) or by Feller's sampling distributions (p. 526)
- [[posterior-distribution]] — gives the optimal estimator under quadratic loss as its mean (p. 514, fn. 3)
- [[prior-distribution]] — can encode weak facts (e.g. "New York exists") and still be proper (p. 528)
- [[coxs-theorem]] — supplies all the ideology Jaynes needs (p. 509)
- [[maximum-entropy-principle]] — the distributions attaining the Cramér–Rao equality, (17.33), have the maximum-entropy form (p. 519)
- [[exponential-family-gibbs-distribution]] — form (17.33), $m(x)e^{-l\beta(x)}/Z$ (p. 519)
- [[sufficient-statistic]] (new) — statistic after which position on the data manifold is irrelevant to $\theta$; exists iff the form (17.32) holds (pp. 510, 520)
- [[unbiased-estimator]] (new) — $\langle\beta\rangle=\alpha$ over the sampling distribution (17.1); not reparametrization-invariant (pp. 511, 515)
- [[bias-variance-decomposition]] (new) — (17.2), the two terms are equal partners in squared error (p. 511)
- [[cramer-rao-bound]] (new) — (17.30), the Schwarz inequality applied to score and estimator (p. 519)
- [[efficiency-umv-estimator]] (new) — ratio of the bound to $\operatorname{var}(\beta)$ for unbiased $\beta$ (p. 520)
- [[tail-area-significance-test]] (new) — P-value computed only under a null hypothesis (p. 523)
- [[periodogram-and-prefiltering]] (new) — $P(\omega)=|Y|^2/n$; a moving average multiplies the Fourier transform by $W(\omega)$ (pp. 522–523)
- [[nuisance-parameter]] (new) — parameter integrated out (here $\mu,\sigma$) (p. 527)

## Canonical instances
- [[cramer-variance-estimation]] — $M_2$ vs $\hat c\,m_2$; $\hat c=n/(n+1)$ for Gaussian data (p. 513)
- [[poisson-unbiased-pathology]] — unbiased estimates absurd for $l^2$, $l^3$, $e^{-l}$; none for $1/l$; Bayes gives $2^{-(n+1)}$ (pp. 516–517)
- [[telephone-cable-problem]] — unbiased estimate foolhardy under asymmetric loss (p. 514)
- [[central-park-january-temperatures]] — evident 20-year cycle missed by Fisher's test, distorted by the 10-year average (pp. 521–522)
- [[feller-hidden-periodicities]] — max of $R_j^2$ and covering theorems (p. 526)

## Bridges (candidates)
- [same-math] bias–variance split (17.2) ↔ machine learning: expected squared-error decomposition — same decomposition for squared loss.
- [same-math] Cramér–Rao equality condition ↔ information-theory: exponential family from MaxEnt — Jaynes shows (17.33) is the Chapter 11 form.
- [same-math] moving average ↔ signal processing: convolution theorem, low-pass filter — $Z=WY$ is literally the convolution theorem.
- [structural-analogy] 10-year averaging as irreversible information loss ↔ information-theory: data-processing inequality — canon link; not stated in this unit.
- [structural-analogy] weak proper priors preventing numerical crashes ↔ machine learning: regularization.

## Questions this raises
- Does the footnote's corrected variance $2\mu_2^2/(n-1)$ change the "half the data" argument, and what remains of it?
- Since $\hat c=n/(n+1)$ is best only among multiples of $m_2$, what is the Bayesian estimator of $\mu_2$ under quadratic loss?
- How does the Bayesian posterior for $\omega$ behave when no periodicity exists (Editor's Exercise 17.3d)?
- When is a weak, proper prior truly harmless, and when does the range ("30°F" criterion) matter?

## Exercises worth doing
- Ex. 17.1 (p. 516) — whether sampling theory has an optimal finite-sample estimator, and whether $\hat\beta$ can be beaten — difficulty: hard
- Ex. 17.2 (p. 518) — pathology of unbiased estimators for the truncated Poisson (17.26) — difficulty: medium
- Unnumbered (p. 520) — prove that a maximum-entropy distribution's sufficient statistics are the data images of its constraints — difficulty: hard
- Editor's Ex. 17.3(a)–(b) (p. 530) — complete the square to get $s^2$, then integrate out $\mu,\sigma$ for $p(AB\omega|DI)$ — difficulty: medium
- Editor's Ex. 17.3(c)–(d) (p. 530) — derive $p(\omega|DI)$, and ask how to test whether a resonance is present — difficulty: hard

## Reading notes
- Printed pages 509–530 (pdf 539–560; printed = pdf − 30). This is part 1 of Chapter 17: it starts at the chapter opening and §17.1, and ends mid-§17.6 after Eq. (17.69) and Editor's Exercise 17.3 (split at the page boundary, not a section boundary).
- Editor's footnote 2 (p. 513): (17.16) is said to be miscalculated; the correct value is $2\mu_2^2/(n-1)$. The text keeps the claims of twice the error and of 203 versus 100 observations. I report both and have not resolved it.
- Apparent misprints in the images: the denominator of (17.30) shows $\int d\alpha$ where $dx$ is meant; the text before (17.29) and Eq. (17.32) write $p(x|a)$ for $p(x|\alpha)$; on p. 520 "the lower bound (17.28)" refers to (17.30); (17.43) uses $e^{-i\omega s}$ while the definition (17.41) uses $e^{+i\omega s}$ (the stated phase $-9\pi/20$ in 17.44 matches the minus sign); Editor's Ex. 17.3 has "integral over $u$" for $\mu$ and omits the index in $\sin(\omega t)$ in (17.69); (17.38) sums $k=1..n$ while (17.37) uses $0\le k<n$ (equivalent by periodicity).
- Jaynes uses "orthodoxian(s)" for orthodox statisticians; his statements of motive ("we suspect…") are his opinions, not demonstrated facts.
