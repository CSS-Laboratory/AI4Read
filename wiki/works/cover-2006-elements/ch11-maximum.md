---
id: cover-2006-elements/ch11-maximum
work: cover-2006-elements
unit: "11 Maximum Entropy and Spectral Estimation"
pages: 266-278
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Maximum Entropy and Spectral Estimation

## L0 — One line
Under moment constraints the entropy-maximizing density, whenever the multipliers can be chosen to meet the constraints, has the exponential form $e^{\lambda_0+\sum\lambda_i r_i(x)}$, and under autocorrelation constraints up to lag $p$ the maximum-entropy-rate process is the $p$th-order Gauss–Markov process (Burg).

## L1 — The gist (≤ 120 words)
Which distribution should we pick when we know only a few moments? The chapter answers with the maximum entropy principle. Theorem 11.1.1 shows, via $D(g\|f^*)\ge 0$, that when the multipliers $\lambda_i$ can be chosen to meet the constraints, the unique maximizer is $f^*=e^{\lambda_0+\sum\lambda_i r_i}$. Examples recover the uniform, exponential and normal laws. A cautionary example shows a supremum that is never attained. For processes whose autocorrelations $EX_iX_{i+k}$ are fixed for $k=0,\dots,p$, Burg's theorem says the maximum-entropy-rate process is Gauss–Markov of order $p$. Its parameters come from the Yule–Walker equations and give the maximum entropy spectral density (11.53), Burg's alternative to the periodogram method.

**Prerequisites:** differential entropy; relative entropy $D\ge0$; Lagrange multipliers; chain rule; Gaussian entropy $\tfrac12\log(2\pi e)^n|K|$; stationary processes, autocorrelation, Fourier transform; an autoregressive (Gauss–Markov) process is one where each $X_i$ is a linear combination of the $p$ previous values plus independent Gaussian noise.

## L2 — Key ideas (5–10 bullets)
- Maximizing $h(f)$ under moment constraints gives, when the multipliers $\lambda_i$ can be chosen to meet the constraints, the form $f^*=e^{\lambda_0+\sum\lambda_ir_i(x)}$. Calculus only suggests this form; the information inequality proves it, with uniqueness (pp. 267–268).
- Many standard laws are maximum entropy laws: uniform, exponential, normal, multivariate normal (pp. 268–270).
- Boltzmann's dice argument links counting microstates, Stirling's approximation and entropy. Chapter 12 is cited for the claim that the maximum entropy macrostate holds almost all the probability (pp. 268–269).
- The form can fail to be attained. With the first three moments fixed, the supremum is the normal's entropy but is only $\epsilon$-achievable (pp. 271–272).
- The periodogram does not converge to the true spectrum, and windowing has costs. Burg instead sets high-lag autocorrelations to maximize the entropy rate (pp. 272–273).
- The Gaussian entropy rate depends on the spectrum (11.39), and it matches the minimum mean squared prediction error given the infinite past (pp. 273–274).
- Burg's theorem: the max-entropy-rate process under lag $0..p$ constraints is an AR($p$) Gauss–Markov process, and the process is not assumed to be Gaussian, zero mean or wide-sense stationary (pp. 274–275).
- The Yule–Walker equations give $a_k,\sigma^2$ from $R(k)$, extend the autocorrelations to high lags and give the spectrum (11.53) (p. 276).

## L3 — Walkthrough

### Introduction (p. 266)
Physics: the velocity distribution of a gas at fixed temperature is the maximum entropy (Maxwell–Boltzmann) distribution. It corresponds to the macrostate, indexed by the empirical distribution, with the most microstates. The author says physics implicitly uses an AEP-like assumption that all microstates are equally probable (p. 266).

### 11.1 Maximum entropy distributions
**Problem (11.1).** Maximize $h(f)$ over densities with (1) $f\ge0$, with equality outside the support set $S$; (2) $\int_S f=1$; (3) $\int_S f(x)r_i(x)\,dx=\alpha_i$, $1\le i\le m$ (p. 266).

**Approach 1 (calculus).** $h$ is concave on a convex set. Form
$$J(f)=-\int f\ln f+\lambda_0\int f+\sum_{i=1}^m\lambda_i\int f r_i \tag{11.2}$$
and differentiate with respect to $f(x)$:
$$\frac{\partial J}{\partial f(x)}=-\ln f(x)-1+\lambda_0+\sum_{i=1}^m\lambda_i r_i(x). \tag{11.3}$$
Setting this to zero gives
$$f(x)=e^{\lambda_0-1+\sum_{i=1}^m\lambda_ir_i(x)},\quad x\in S, \tag{11.4}$$
with the $\lambda$'s chosen so the constraints hold. This only suggests the form. A proof by second variation is possible, but the information inequality is simpler (p. 267).

**Approach 2 / Theorem 11.1.1.** Let $f^*=f_\lambda=e^{\lambda_0+\sum\lambda_ir_i(x)}$, $x\in S$, with $\lambda_0,\dots,\lambda_m$ chosen so $f^*$ satisfies (11.1). Then $f^*$ uniquely maximizes $h(f)$ over all densities satisfying (11.1) (p. 267).

*Proof.* Let $g$ satisfy the constraints.
$$h(g)=-\int_S g\ln g \tag{11.5}$$
$$=-\int_S g\ln\frac{g}{f^*}f^* \tag{11.6}$$
$$=-D(g\|f^*)-\int_S g\ln f^* \tag{11.7}$$
$$\overset{(a)}{\le}-\int_S g\ln f^* \tag{11.8}$$
$$\overset{(b)}{=}-\int_S g\Big(\lambda_0+\sum\lambda_ir_i\Big) \tag{11.9}$$
$$\overset{(c)}{=}-\int_S f^*\Big(\lambda_0+\sum\lambda_ir_i\Big) \tag{11.10}$$
$$=-\int_S f^*\ln f^* \tag{11.11}$$
$$=h(f^*). \tag{11.12}$$
Step (a) is $D\ge0$. Step (b) is the definition of $f^*$. Step (c) holds because both $f^*$ and $g$ satisfy the constraints. Equality in (a) holds iff $g=f^*$ except on a set of measure 0, which gives uniqueness (pp. 267–268). The same approach holds for discrete entropies and multivariate distributions (p. 268).

*Intuition note.* The gap $h(f^*)-h(g)$ equals $D(g\|f^*)$. This is because $\ln f^*$ is linear in the constrained functions, so its average is the same under every $g$ that meets the constraints.

### 11.2 Examples
- **11.2.1 (1-D gas).** $EX=0$, $EX^2=\sigma^2$: the form $e^{\lambda_0+\lambda_1x+\lambda_2x^2}$ (11.13) is normal-shaped, so the maximizer is $\mathcal N(0,\sigma^2)$ (p. 268).
- **11.2.2.** Dice, no constraint: uniform, $p(x)=1/6$ (p. 268).
- **11.2.3 (Boltzmann's dice).** $n$ dice show a total of $n\alpha$ spots; what proportion shows face $i$? There are $\binom{n}{n_1,\dots,n_6}$ ways for macrostate $(n_1,\dots,n_6)$, each microstate having probability $1/6^n$. We maximize the count under $\sum_i i\,n_i=n\alpha$ (11.14) (p. 268). With the crude Stirling approximation $n!\approx(n/e)^n$:
$$\binom{n}{n_1,\dots,n_6}\approx\frac{(n/e)^n}{\prod_{i=1}^6(n_i/e)^{n_i}}=\prod_{i=1}^6\Big(\frac n{n_i}\Big)^{n_i}=e^{nH(n_1/n,\dots,n_6/n)} \tag{11.15–11.17}$$
So maximizing the count is almost equivalent to maximizing $H(p_1,\dots,p_6)$ under $\sum ip_i=\alpha$. By Theorem 11.1.1,
$$p_i^*=\frac{e^{\lambda i}}{\sum_{i=1}^6e^{\lambda i}} \tag{11.18}$$
with $\lambda$ chosen so $\sum ip_i^*=\alpha$. The most probable macrostate is $(np_1^*,\dots,np_6^*)$ (p. 269). The author says Chapter 12 will show that this reasoning and these approximations are essentially correct. For rational $\alpha$, as $n\to\infty$ along values with $n\alpha$ an integer,
$$\Pr\Big\{\Big|\tfrac{N_i}{n}-p_i^*\Big|<\epsilon,\ i=1,\dots,6\ \Big|\ \textstyle\sum_{i=1}^nX_i=n\alpha\Big\}\to1 \tag{11.19}$$
This is a promised result, not proved here (p. 269).
- **11.2.4.** $S=[a,b]$, no other constraint: uniform (p. 269).
- **11.2.5.** $S=[0,\infty)$, $EX=\mu$: $f(x)=\frac1\mu e^{-x/\mu}$, $x\ge0$ (11.20). Physical reading: the height of atmospheric molecules, with $E[mgX]$ fixed, gives $\lambda e^{-\lambda x}$. The author says the atmosphere does have this density (pp. 269–270).
- **11.2.6.** $S=(-\infty,\infty)$, $EX=\mu$: the entropy is infinite and no maximizer exists. Normals with growing variance show this (p. 270).
- **11.2.7.** $EX=\alpha_1$, $EX^2=\alpha_2$: $\mathcal N(\alpha_1,\alpha_2-\alpha_1^2)$ (p. 270).
- **11.2.8.** $S=\mathbb R^n$, $EX_iX_j=K_{ij}$: the density $e^{\lambda_0+\sum_{i,j}\lambda_{ij}x_ix_j}$ (11.21) has a quadratic exponent, so it is a zero-mean multivariate normal with covariance $K$ (11.22). Its entropy is $h(\mathcal N_n(0,K))=\tfrac12\log(2\pi e)^n|K|$ (11.23), as derived in Chapter 9 (p. 270).

### 11.3 An anomalous maximum entropy problem
The form (11.25) holds if suitable $\lambda_i$ exist (p. 271). Now impose $\int f=1$, $\int xf=\alpha_1$, $\int x^2f=\alpha_2$, $\int x^3f=\alpha_3$ over $(-\infty,\infty)$ (11.26–11.29). If a maximizer exists it has the form $e^{\lambda_0+\lambda_1x+\lambda_2x^2+\lambda_3x^3}$ (11.30). If $\lambda_3\ne0$, $\int f=\infty$, so $\lambda_3=0$. Then there are four equations and three unknowns, and in general the constants cannot be chosen (p. 271).

The explanation is that the entropy has an upper bound that is not attained. The first two moments alone give the normal. Adding the third constraint cannot raise the maximum. Small "wiggles" of the normal at very high $x$ fix the third moment, and further wiggles restore the first two moments, with little loss of entropy. So the bound can be approached arbitrarily closely (p. 271):
$$\sup h(f)=h(\mathcal N(0,\alpha_2-\alpha_1^2))=\tfrac12\ln2\pi e(\alpha_2-\alpha_1^2). \tag{11.31}$$
The maximum entropy may only be $\epsilon$-achievable (p. 272).

*Intuition note.* Piling a tiny amount of probability far out can set the third moment at almost no entropy cost. So no density meets the bound exactly, but some come as close as we like.

### 11.4 Spectrum estimation
For a stationary zero-mean process $\{X_i\}$ the autocorrelation is
$$R(k)=EX_iX_{i+k} \tag{11.32}$$
and the power spectral density is its Fourier transform
$$S(\lambda)=\sum_{m=-\infty}^{\infty}R(m)e^{-im\lambda},\quad-\pi<\lambda\le\pi. \tag{11.33}$$
The simplest estimate uses sample averages from a sample of length $n$:
$$\hat R(k)=\frac1{n-k}\sum_{i=1}^{n-k}X_iX_{i+k}. \tag{11.34}$$
Using all $\hat R(\cdot)$ in (11.33) gives the periodogram method, whose estimate does not converge to the true spectrum for large $n$ (p. 272). One reason is that high-lag estimates rest on few samples. Setting high-lag autocorrelations to 0 creates artifacts from the sudden cutoff. Windowing smooths this but reduces spectral resolution and can give negative spectral estimates (p. 272).

In the late 1960s Burg set the high-lag autocorrelations to values that make the fewest assumptions, i.e. that maximize the entropy rate. This is consistent with Jaynes's maximum entropy principle. Assuming a stationary Gaussian process, he found the maximizer is an autoregressive Gaussian process of suitable order. The method has proved useful where an autoregressive model can be assumed (e.g. linear predictive coding for speech) (p. 273).

### 11.5 Entropy rates of a Gaussian process
**Definition.** The differential entropy rate of $\{X_i\}$, $X_i\in\mathbb R$, is
$$h(\mathcal X)=\lim_{n\to\infty}\frac{h(X_1,\dots,X_n)}{n}\tag{11.35}$$
if the limit exists (p. 273). As in the discrete case, the limit exists for stationary processes and has two expressions (11.36–11.37). These two equations are blank in the text layer [unreadable p. 273]. Page 274 says the entropy rate is also $\lim h(X_n|X^{n-1})$ (p. 274).

For a stationary Gaussian process
$$h(X_1,\dots,X_n)=\tfrac12\log(2\pi e)^n|K^{(n)}|,\tag{11.38}$$
with $K^{(n)}$ Toeplitz (constant along diagonals): $K^{(n)}_{ij}=R(|i-j|)=E(X_i-EX_i)(X_j-EX_j)$ (p. 273). As $n\to\infty$ the eigenvalue density of $K^{(n)}$ tends to the spectrum of the process. Kolmogorov showed
$$h(\mathcal X)=\tfrac12\log2\pi e+\frac1{4\pi}\int_{-\pi}^{\pi}\log S(\lambda)\,d\lambda.\tag{11.39}$$
The entropy rate also equals $\lim h(X_n|X^{n-1})$. In the Gaussian case this conditional entropy is $\tfrac12\log2\pi e\sigma_\infty^2$, where $\sigma_\infty^2$ is the error variance of the best estimate of $X_n$ from the infinite past. Hence
$$\sigma_\infty^2=\frac1{2\pi e}2^{2h(\mathcal X)}\tag{11.40}$$
with $h(\mathcal X)$ from (11.39). The entropy rate corresponds to the minimum mean squared error of the best estimator given the infinite past (p. 274).

### 11.6 Burg's maximum entropy theorem
**Theorem 11.6.1.** The maximum entropy rate process $\{X_i\}$ satisfying
$$EX_iX_{i+k}=\alpha_k,\quad k=0,1,\dots,p,\ \text{for all }i\tag{11.41}$$
is the $p$th-order Gauss–Markov process
$$X_i=-\sum_{k=1}^pa_kX_{i-k}+Z_i,\tag{11.42}$$
with $Z_i$ i.i.d. $\mathcal N(0,\sigma^2)$ and $a_1,\dots,a_p,\sigma^2$ chosen to satisfy (11.41). **Remark:** $\{X_i\}$ is not assumed zero mean, Gaussian or wide-sense stationary (p. 274).

*Proof.* Let $X_1,\dots,X_n$ satisfy (11.41). Let $Z_1,\dots,Z_n$ be Gaussian with the same covariance matrix. The normal maximizes entropy under a covariance constraint, so
$$h(X_1,\dots,X_n)\le h(Z_1,\dots,Z_n)\tag{11.43}$$
$$=h(Z_1,\dots,Z_p)+\sum_{i=p+1}^nh(Z_i|Z_{i-1},\dots,Z_1)\tag{11.44}$$
$$\le h(Z_1,\dots,Z_p)+\sum_{i=p+1}^nh(Z_i|Z_{i-1},\dots,Z_{i-p}),\tag{11.45}$$
by the chain rule and "conditioning reduces entropy". Let $Z_i'$ be a $p$th-order Gauss–Markov process with the same distribution as $Z$ for all orders up to $p$ (existence is shown next, via Yule–Walker). The conditional entropy depends only on the $p$th-order distribution, so
$$h(X_1,\dots,X_n)\le h(Z_1',\dots,Z_p')+\sum_{i=p+1}^nh(Z_i'|Z_{i-1}',\dots,Z_{i-p}')\tag{11.46–11.47}$$
$$=h(Z_1',\dots,Z_n'),\tag{11.48}$$
the last step by $p$th-order Markovity of $\{Z_i'\}$ (p. 275). Dividing by $n$ and taking limits,
$$\overline{\lim}\frac1nh(X_1,\dots,X_n)\le\lim\frac1nh(Z_1',\dots,Z_n')=h^*,\tag{11.49}$$
$$h^*=\tfrac12\log2\pi e\sigma^2,\tag{11.50}$$
the entropy rate of the Gauss–Markov process. $\square$ (p. 275)

*Intuition note.* Entropy is bounded above first by the Gaussian with the same covariance, then by the order-$p$ Gauss–Markov process. The order-$p$ Gauss–Markov process with the given covariance constraints attains the final bound.

**Yule–Walker (existence and parameters).** Multiply (11.42) by $X_{i-l}$, take expectations and use $R(k)=R(-k)$:
$$R(0)=-\sum_{k=1}^pa_kR(-k)+\sigma^2\tag{11.51}$$
$$R(l)=-\sum_{k=1}^pa_kR(l-k),\quad l=1,2,\dots\tag{11.52}$$
There are $p+1$ equations in $p+1$ unknowns $a_1,\dots,a_p,\sigma^2$, so the parameters can be solved from the covariances. The Levinson and Durbin algorithms exploit the structure (with $a_0=1$). For $l>p$, (11.52) gives the Yule–Walker extension of the autocorrelations to high lags. The maximum entropy spectrum is
$$S(l)=\frac{\sigma^2}{|1+\sum_{k=1}^pa_ke^{-ikl}|^2}\tag{11.53}$$
This is the maximum entropy spectral density subject to $R(0),\dots,R(p)$ (p. 276).

**Choice of $p$.** Choose the $p$ that minimizes total description length in a two-stage description of the data (Rissanen, Barron), which is closely related to Kolmogorov complexity (p. 276).

### Summary and problems (pp. 277–278)
The chapter summary restates Theorem 11.1.1 (11.54) and the maximum entropy spectrum (11.55) (p. 277). The Historical Notes say the maximum entropy principle arose in nineteenth-century statistical mechanics, was advocated more broadly by Jaynes, and was applied to spectral estimation by Burg. They credit the information-theoretic proof of Burg's theorem to Choi and Cover (p. 278).

## Toy example (ours)
Faces $\{0,1,2\}$, required mean $EX=10/7$. The form $p_i\propto x^i$ with $x=e^\lambda$ gives $p=(1,x,x^2)/(1+x+x^2)$. Take $x=2$: $p^*=(1/7,2/7,4/7)$, mean $=(0+2+8)/7=10/7$ ✓.
Rival with the same mean: $q=(0,4/7,3/7)$, mean $=4/7+6/7=10/7$ ✓.
Entropies in bits, with $\log_27=2.8074$:
- $H(p^*)=\tfrac17(2.8074)+\tfrac27(1.8074)+\tfrac47(0.8074)=0.4010+0.5164+0.4614=1.3788$.
- $H(q)=\tfrac47(0.8074)+\tfrac37(1.2224)=0.4614+0.5239=0.9853$.

Gap $=0.3935$. Direct check: $D(q\|p^*)=\tfrac47\log_2 2+\tfrac37\log_2\tfrac34=0.5714-0.1779=0.3935$ ✓. This is the identity $h(f^*)-h(g)=D(g\|f^*)$ of Theorem 11.1.1, because $\log p^*_i=-\log7+i$ is linear in $i$.

## Concepts
- [[maximum-entropy-principle]] — choose the max-entropy distribution consistent with known constraints; here for moments and autocorrelations (p. 266)
- [[exponential-family-gibbs]] — the max-entropy solution has the form $e^{\lambda_0+\sum\lambda_ir_i}$ (p. 267)
- [[differential-entropy]] — $h(f)=-\int f\ln f$, concave in $f$; used throughout (p. 266)
- [[relative-entropy-kl]] — $D(g\|f^*)\ge0$ drives the proof of the theorem (p. 267)
- [[entropy-rate]] — here $\lim h(X^n)/n$ for real-valued processes (p. 273)
- [[chain-rule]] — used with "conditioning reduces entropy" in Burg's proof (p. 275)
- [[mdl]] — choosing $p$ by a two-stage description length (p. 276)
- [[power-spectral-density]] (new) — Fourier transform of the autocorrelation, $S(\lambda)$ (p. 272)
- [[yule-walker-equations]] (new) — linear equations (11.51–11.52) linking AR coefficients to autocorrelations (p. 276)
- [[burg-maximum-entropy-method]] (new) — spectral estimate from the max-entropy-rate process (p. 273)
- [[gauss-markov-ar-process]] (new) — $X_i=-\sum a_kX_{i-k}+Z_i$ with i.i.d. normal noise (p. 274)

## Canonical instances
- [[maxwell-boltzmann-gas]] — the velocity law as max entropy under a temperature constraint (p. 266)
- [[boltzmann-dice]] — counting macrostates leads to $p_i^*\propto e^{\lambda i}$ (p. 268)
- [[atmosphere-exponential-height]] — exponential density of molecule height (p. 270)
- [[third-moment-anomaly]] — a supremum that is not attained, via wiggles (p. 271)
- [[linear-predictive-coding-speech]] — AR modelling where Burg's method is useful (p. 273)

## Bridges (candidates)
- [same-math] Max-entropy form $e^{\lambda_0+\sum\lambda_ir_i}$ ↔ statistics: exponential family with sufficient statistics $r_i$ — same functional form.
- [same-math] Entropy rate ↔ prediction: (11.40) links entropy rate to minimum mean squared prediction error for Gaussian processes.
- [structural-analogy] Choosing $p$ by two-stage description length ↔ MDL / model selection — penalizing model complexity.
- [metaphor] Most-probable macrostate = most microstates ↔ typical-set counting (AEP).

## Questions this raises
- When do the multipliers $\lambda_i$ exist, and can the supremum be attained in general (cf. 11.3)?
- How is (11.19) proved in Chapter 12, and when does the max-entropy macrostate dominate the probability?
- What are (11.36–11.37), and how is (11.39) derived from the eigenvalue behavior of Toeplitz matrices?
- How well does a chosen $p$ perform when the data are not truly autoregressive?

## Exercises worth doing
- Ex. 1 (p. 277) — max entropy density with $EX$ and $E\ln X$ fixed on $x\ge0$; practice with the form (11.4) — difficulty: medium
- Ex. 2 (p. 277) — minimize $D(P\|Q)$ under constraints; generalizes Theorem 11.1.1 — difficulty: medium
- Ex. 3 (p. 277) — max entropy rate processes under second-moment and lag-1 constraints — difficulty: medium
- Ex. 4 (p. 278) — max entropy spectra for Ex. 3 — difficulty: medium
- Ex. 5 (p. 278) — max entropy joint distribution with given marginals — difficulty: easy
- Ex. 7 (p. 278) — every density is a max entropy density for the constraint $r=\ln f_0$ — difficulty: hard

## Reading notes
- The PDF is the 1991 first edition (Wiley copyright line on p. 266), not the 2006 second edition. Per the unit metadata, chapter numbering and content differ from the second edition (this cannot be checked from these pages).
- Printed page = pdf − 22.
- The text layer is heavily garbled in equations. I checked against images where provided. No page image was provided for printed p. 273 (pdf 295), only the text layer, so (11.36–11.37) on p. 273 are [unreadable p. 273].
- The text layer labels Example 11.2.5 as "11.2.8"; the image shows 11.2.5. (11.4) has $\lambda_0-1$ while Theorem 11.1.1 writes $\lambda_0$ (absorbing the $-1$).
- (11.31) in the image is $h(\mathcal N(0,\alpha_2-\alpha_1^2))$ although Example 11.2.7 gives mean $\alpha_1$. The source does not comment on this discrepancy.
- In (11.19), $N_i$ and $X_i$ are not defined on these pages (presumably counts and dice outcomes).
