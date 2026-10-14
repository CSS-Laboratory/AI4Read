---
id: jaynes-2003-probability/ch07-central-p2
work: jaynes-2003-probability
unit: "7 The central, Gaussian or normal distribution (part 2/2: end of §7.13 to §7.27.1)"
pages: 220-242
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The central, Gaussian or normal distribution (part 2/2)

## L0 — One line
Gaussians stay Gaussian under convolution (the density of a sum of independent variables; means and variances add), and this stability, with its maximum-entropy character, motivates calling it the "central" distribution; Jaynes also asks what a Gaussian form in data can and cannot show.

## L1 — The gist (≤ 120 words)
Why does the Gaussian deserve its central place, and what follows from its stability? Jaynes lists five stability properties and proves the convolution law. The Cauchy law turns out to be the one distribution whose sample mean has the same law as one observation. He applies the √N cancellation of independent errors to rounding errors, and reads Galton's reversion and Einstein's diffusion as equilibrium between spreading and counter-drift. He then turns to evolution, economics and Laplace's Jupiter–Saturn solution. Splitting a non-Gaussian density into Gaussians is ill-posed as inversion and must be treated as Bayesian inference. He closes by criticising the names "normal" and "Gaussian".

**Prerequisites:** integration and Gaussian integrals; Fourier transform and convolution; expectation and variance; basic Bayesian inference (priors, nuisance parameters); entropy as a measure of uncertainty; sample mean.

## L2 — Key ideas (5–10 bullets)
- The Gaussian's special status rests on five stability properties (A–E): power-limit, product, convolution, Fourier transform, and maximum entropy at fixed variance (pp. 220–221).
- Convolution law: two Gaussians convolve to a Gaussian whose mean and variance are the sums of the originals (p. 221).
- Only the Cauchy law has a sample mean distributed like a single observation; the editor calls this derivation the only known exception to the CLT (pp. 222, 224).
- For N independent rounding errors the net error should tend to grow only like √N, not N. For 100 roughly equal terms, a virtual certainty of four-figure accuracy in the sum then needs only three-figure accuracy in the terms (pp. 225–226).
- Galton's reversion rate $a=\pm\sqrt{1-\sigma_2^2/\sigma_1^2}$ is a stability condition: systematic reversion balances random spreading. Jaynes sees the same structure in Einstein's $D=\lambda kT$ (pp. 227–229).
- Jaynes treats individual variation ("noise") as the engine of change in evolution, and, tentatively, in economics; he also calls thermal fluctuations the engine of irreversible processes in physics (pp. 230–233).
- Resolving a density into Gaussians is unstable and non-unique as an inversion problem, so it needs prior information and Bayesian inference (pp. 236–240).
- Terminology: "normal" suggests a value judgment and "Gaussian" misattributes credit. Jaynes tentatively proposes "central distribution" and reads "central limit theorem" as a limit toward the central distribution (pp. 240–242).

## L3 — Walkthrough

### 7.13 (end): nuisance parameters
- **Jaynes's claim:** including a relevant but uninteresting parameter in the model and integrating it out can improve the extraction of information, often by orders of magnitude. It forewarns the robot of a possible complication (p. 220).
- In hazard and safety estimation, ignoring prior information (engineering design, chemistry of an additive) can make danger grossly over- or underestimated. Random experiments are inefficient ("so to speak", we learn only like the square root of the number of trials), and rational conclusions cannot be drawn from them unless the prior information is also taken into account (p. 220).
- The proper job of a random experiment is to guard against completely unexpected bad effects, about which prior information gave no warning (p. 220).

### 7.14 More general properties
- **Jaynes's objection to Gauss's derivation:** it rests on intuition. Why must the best location estimate be linear in the data? If the sampling law is not Gaussian, the best estimate will not be the sample mean; it could take many other forms (p. 220).
- Jaynes (anticipating later chapters) says the Gaussian's position comes from four properties that have nothing to do with probability or inference, plus a fifth that does (p. 220):
  - (A) A smooth function with a single rounded maximum, raised to higher and higher powers, goes into a Gaussian.
  - (B) The product of two Gaussians is a Gaussian.
  - (C) The convolution of two Gaussians is a Gaussian.
  - (D) The Fourier transform of a Gaussian is a Gaussian.
  - (E) A Gaussian has higher entropy than any other distribution with the same variance. Hence any operation that discards information but conserves variance leads "inexorably" closer to a Gaussian. The central limit theorem is the best-known example, with convolution as the operation (p. 221).
- (A) and (E) explain why the form is approached. (B), (C), (D) explain why it is preserved once attained (p. 221).

> *Intuition note.* Some operations push distributions toward the Gaussian shape, and others leave it unchanged once it is reached. Together they make it a kind of equilibrium shape.

### 7.15 Convolution of Gaussians
- With weight $w\equiv1/\sigma^2$ (p. 221):
$$\varphi(x-\mu|\sigma)\equiv\frac1\sigma\varphi\!\left(\frac{x-\mu}{\sigma}\right)=\sqrt{\frac1{2\pi\sigma^2}}\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\}=\sqrt{\frac w{2\pi}}\exp\Big\{-\frac w2(x-\mu)^2\Big\}\tag{7.46}$$
- The product of two such functions (p. 221):
$$\varphi(x-\mu_1|\sigma_1)\varphi(y-x-\mu_2|\sigma_2)=\frac1{2\pi\sigma_1\sigma_2}\exp\Big\{-\frac12\Big[\Big(\frac{x-\mu_1}{\sigma_1}\Big)^2+\Big(\frac{y-x-\mu_2}{\sigma_2}\Big)^2\Big]\Big\}\tag{7.47}$$
- The quadratic form is rearranged to show the dependence on $x$ (p. 221):
$$\Big(\frac{x-\mu_1}{\sigma_1}\Big)^2+\Big(\frac{y-x-\mu_2}{\sigma_2}\Big)^2=(w_1+w_2)(x-\hat x)^2+\frac{w_1w_2}{w_1+w_2}(y-\mu_1-\mu_2)^2\tag{7.48}$$
with $\hat x\equiv(w_1\mu_1+w_2y-w_2\mu_2)/(w_1+w_2)$.
- The product is Gaussian in $x$. Integrating $x$ out gives the **convolution law** (p. 221):
$$\int_{-\infty}^\infty dx\,\varphi(x-\mu_1|\sigma_1)\varphi(y-x-\mu_2|\sigma_2)=\varphi(y-\mu|\sigma),\quad \mu\equiv\mu_1+\mu_2,\ \sigma^2\equiv\sigma_1^2+\sigma_2^2\tag{7.49}$$
- (added step) The leftover $y$-factor in (7.48) has weight $w_1w_2/(w_1+w_2)=1/(\sigma_1^2+\sigma_2^2)$, which is why the variances add.

> *Intuition note.* Adding two independent Gaussian quantities gives a Gaussian whose mean is the sum of the means and whose variance is the sum of the variances. Standard deviations do not add; their squares do.

### 7.16 The central limit theorem
- Jaynes asks whether non-Gaussian distributions also have parameters additive under convolution; this leads to cumulants (Appendix C, not in this unit) (p. 222).
- **Editor's Exercise 7.5 (editor's voice):** the editor says Jaynes does not derive the CLT here. He derives "the only known exception" to it, and in Appendix C comes close to the CLT itself (p. 222).
- The editor defines $\phi(\alpha)=\int f(x)e^{i\alpha x}dx$ (7.50). A repeated convolution is $h_n(y)=f*\cdots*f=\frac1{2\pi}\int d\alpha\,\phi(\alpha)^n e^{-i\alpha y}$ (7.51). Using cumulants, $[\phi(\alpha)]^n=\exp\{n(C_0+\alpha C_1-\alpha^2C_2/2+\cdots)\}$ (7.52). Dropping cumulants above $C_2$ gives (7.53) a Gaussian with mean $n\langle x\rangle$ and variance $n\sigma^2$ (p. 222). The editor asks for the conditions under which this is a good approximation (p. 222).
- **Jaynes's setup.** For probability distributions, $f_i\ge0$, $\int f_i=1$ and $Z_i=1$. The transforms $\mathcal F_i(\alpha)=\int dx\,f_i(x)e^{i\alpha x}$ (7.54) converge absolutely for real $\alpha$. This holds even with discontinuities or delta-functions, so the derivation covers the discrete, continuous or mixed case (pp. 222–223).
- For $y=x_1+x_2$ with $f_i(x_i)=p(x_i|I)$ (7.55) (p. 223):
$$P(y'\le y|I)=\int dx_1f_1(x_1)\int_{-\infty}^{y-x_1}dx_2f_2(x_2)\tag{7.56}$$
$$f(y)=\Big[\tfrac{d}{dy}P(y'\le y|I)\Big]_{y=y'}=\int dx_1f_1(x_1)f_2(y-x_1)\tag{7.57}$$
- This is the convolution $f_1*f_2$. By induction, $g(z)=\int dy\,f(y)f_3(z-y)=f_1*f_2*f_3$ (7.58), and the density of a sum of $n$ variables is $h_n=f_1*\cdots*f_n$ (p. 223).
- With the characteristic function $\varphi_k(\alpha)=\langle e^{i\alpha x}\rangle=\int dx\,f_k e^{i\alpha x}$ (7.59) and inverse $f_k(x)=\frac1{2\pi}\int d\alpha\,\varphi_ke^{-i\alpha x}$ (7.60) (p. 223):
$$h_n(q)=\frac1{2\pi}\int d\alpha\,\varphi_1(\alpha)\cdots\varphi_n(\alpha)e^{-i\alpha q}\tag{7.61}$$
$$h_n(q)=\frac1{2\pi}\int d\alpha\,[\varphi(\alpha)]^ne^{-i\alpha q}\quad(\text{identical }f_i)\tag{7.62}$$
- For the mean $\bar x=q/n$ (p. 224):
$$p(\bar x)=nh_n(n\bar x)=\frac n{2\pi}\int d\alpha\,[\varphi(\alpha)e^{-i\alpha\bar x}]^n\tag{7.63}$$
- **Which distributions have $\bar x$ distributed like a single $x$?** With $\varphi(\alpha)=\int dx\,p(x|I)e^{i\alpha x}$ (7.64), the mean of $n$ observations has characteristic function $\varphi^n(n^{-1}\alpha)$. Jaynes says the necessary and sufficient condition for $x$ and $\bar x$ to have the same distribution is that $\varphi^n(n^{-1}\alpha)=\varphi(\alpha)$ (p. 224). He says it is easy to prove that only one distribution has this property (p. 224).
- Substituting $\alpha'=n^{-1}\alpha$ gives
$$n\log\varphi(\alpha)=\log\varphi(n\alpha),\ -\infty<\alpha<\infty,\ n=1,2,3,\dots\tag{7.65}$$
- Jaynes says this "evidently" requires a linear relation on the positive real line:
$$\log\varphi(\alpha)=C\alpha,\quad 0\le\alpha<\infty\tag{7.66}$$
with $C$ complex (p. 224).
- Writing $C=-k+i\theta$ and imposing $\varphi(-\alpha)=\varphi^*(\alpha)$ (p. 224):
$$\varphi(\alpha)=\exp\{i\alpha\theta-k|\alpha|\},\ -\infty<\theta<\infty,\ 0<k<\infty\tag{7.67}$$
$$p(x|I)=\frac1{2\pi}\int d\alpha\,e^{-k|\alpha|}e^{i\alpha(\theta-x)}=\frac1\pi\Big[\frac k{k^2+(x-\theta)^2}\Big]\tag{7.68}$$
the Cauchy distribution with median $\theta$ and quartiles $\theta\pm k$.

> *Intuition note.* The Cauchy law is the single case where averaging $n$ observations does not sharpen the distribution at all. The editor calls what Jaynes derives here the only known exception to the central limit theorem (p. 222).

### 7.17 Accuracy of computations
- **Setting.** Programmers should not run double precision (16 decimal places) when the result does not need it. In probability calculations we seldom need more than three-figure accuracy in final results, so aiming at four figures is well on the safe side (pp. 224–225).
- Consider $S\equiv\sum_{n=1}^Na_n$ with positive terms of order unity (7.69). Each $a_n$ is digitized to increment $\epsilon$ (e.g. $10^{-6}$, or $2^{-16}=1/65\,536$), with error $e_n\in(-\epsilon/2,\epsilon/2]$. The maximum possible total error is $N\epsilon/2$ (p. 225).
- **Jaynes's point:** this maximum is enormously unlikely for large $N$, which Jaynes says Euler failed to see. The errors are almost certain to be positive and negative roughly equally often, so the net error should tend to grow only as $\sqrt N$. The CLT expresses a combinatorial fact: most error vectors show about the same cancellation (p. 225).
- A rectangular error law on $(-\epsilon/2,\epsilon/2)$ gives the expected squared error per term (p. 225):
$$\frac1\epsilon\int_{-\epsilon/2}^{\epsilon/2}dx\,x^2=\frac{\epsilon^2}{12}\tag{7.70}$$
- By the CLT, $S$ tends to a Gaussian with variance $N\epsilon^2/12$, centred near $N$. The net error exceeds $\epsilon\sqrt N=\sqrt{12}=3.46$ standard deviations with probability
$$2[1-\Phi(3.46)]\simeq0.0006\tag{7.71}$$
- Since $\Phi(2.58)=0.995$, the chance of exceeding $0.74\,\epsilon\sqrt N=2.58$ standard deviations is about 1% (p. 225).
- For 99% or greater probability of four-figure accuracy, require $0.74\,\epsilon\sqrt N\le10^{-4}N$, i.e.
$$\epsilon\le1.35\times10^{-4}\sqrt N\tag{7.72}$$
- For $N=100$ roughly equal terms, a virtual certainty of four-figure accuracy in the sum needs only three-figure accuracy in the individual terms (p. 226).
- **Proviso:** this holds only when the errors $e_n$ are logically independent. If knowing $e_1$ tells us anything about another $e_n$, the CLT no longer applies. Jaynes says this is almost never a serious limit in practice, because the $a_n$ differ among themselves by amounts large compared with $\epsilon$ (p. 226).
- **Jaynes's criticism of orthodox advice:** McClave and Benson (1988) say to keep twice as many decimal places in $s^2$ as in $s$. Jaynes argues from $\delta s/s=\tfrac12\delta(s^2)/s^2$ that four significant figures in $s^2$ determine $s$ to somewhat better than four. He says their extra factor $n/(n-1)$ makes "a joke" of four-figure pretensions at $n=100$ (p. 227).

> *Intuition note.* Independent rounding errors partly cancel, so a sum is more accurate than the worst case suggests. If the errors are correlated, this analysis no longer applies, and the error may be much larger (Ex. 7.7).

### 7.18 Galton's discovery
- Written with scale changes $x\to ax$, $\sigma_1\to a\sigma_1$, (7.49) becomes (p. 227)
$$\int dx\,\varphi(x|\sigma_1)\varphi(y-ax|\sigma_2)=\varphi(y|\sigma),\quad\sigma=\sqrt{a^2\sigma_1^2+\sigma_2^2}\tag{7.73, 7.74}$$
- Galton (1886) used the language of frequency. Jaynes argues (anticipating Chapter 9) that probability then gives distributions substantially equal to the frequencies (p. 227).
- Heights of adult English males were fitted by a Gaussian (7.75) with $\mu=68.1$ in and $\sigma=2.6$ in. Galton defined the "midparent" height $h_{\rm mid}\equiv\frac12(h_{\rm father}+1.08\,h_{\rm mother})$ (7.76), using the ratio 1.08 of male to female average height (p. 227).
- He collected data on 928 adults born of 205 midparents. Children of tall parents tend to be tall but show a spread smaller than the whole population's $\sigma$ (p. 228).
- **Reversion.** Children of tall parents are taller than average but less tall than their parents, and vice versa. For a stable population, the systematic reversion must exactly balance the random spreading (p. 228).
- Let the population have $\varphi(x|\sigma_1)$ and children of midparents at deviation $x$ have $\varphi[(y-ax)|\sigma_2]$. The next generation is given by (7.73). Stability requires $\sigma=\sigma_1$, so
$$a=\pm\sqrt{1-\sigma_2^2/\sigma_1^2}\tag{7.77}$$
- So $a$ need not be positive: negative $a$ gives alternation between generations, but still equilibrium (p. 228).
- If $|a|>1$, equilibrium would need $\sigma_2^2<0$, so the population would explode. At $\sigma_2=0$, $|a|=1$, each sub-population breeds true; an economist might call $a=1$ a "unit root" situation, with no reversion and no spreading (p. 228).
- **Einstein.** Jaynes says Einstein (1905) saw the same mechanism. The Boltzmann distribution $\exp\{-E/kT\}$, with $E=u+mv^2/2$, is Gaussian in velocities. A particle at $x$ at $t=0$ has, at time $t$, the conditional probability to be at $y$ (p. 229):
$$p(y|xt)\propto\exp\{-(y-x)^2/4Dt\}\tag{7.78}$$
from random drift alone. External forces $F=-\nabla u$ counter this, like Galton's reversion (p. 229).
- Jaynes calls (7.77), although the details are quite different, the "logical equivalent" of Einstein's $D=\lambda kT$ ($D$ diffusion coefficient, $\lambda$ mobility). Both express equilibrium as a balance of random spreading and systematic counter-drift (p. 229).

> *Intuition note.* In each generation the pull toward the mean removes spread and fresh randomness adds it back. The total spread stays fixed exactly when the two effects are equal.

### 7.19 Population dynamics and Darwinian evolution
- If $a$ does not satisfy (7.77), the height distribution drifts. If short people have fewer children, the mean height drifts upward. **Jaynes asks** whether this is the mechanism of Darwinian evolution, and notes that Galton was Darwin's cousin (pp. 229–230).
- Laplace and Gauss, as astronomers, treated telescope vagaries as "errors" to be eliminated. A telescope maker would see the errors as the object of study: "one man's 'noise' is another man's 'signal'" (p. 230).
- *Biometrika* (1901) was founded by Pearson and Weldon. **Weldon's editorial** (reported by Jaynes): differences between individuals are the starting point of Darwin's theory, and the first step in studying a selective process must be an estimate of the frequency of individuals showing any degree of abnormality (p. 230).
- Jaynes's reading: individual variation is "the engine" of evolutionary change, since natural selection has nothing to operate on without it. So, to demonstrate the mechanism of evolution at its source, it is the frequency distribution of individual variations that must be studied (p. 230).
- Footnote: average height has risen in developed nations. Jaynes notes that nutrition is the usual explanation, but that taller people having more or longer-lived children would give the same drift, with more research needed (p. 230).

### 7.20 Evolution of humming-birds and flowers
- **Jaynes's scenario** (p. 231): long-beaked mutants reach nectar in deep flowers and prosper. Deep-flower mutants are preferentially visited, so their pollen goes to flowers of the same type. Each type's success raises the other's: a positive feedback. Over millions of years this yields apparently "designed" symbiosis.
- Short-beaked birds persist because birds patronizing deep flowers leave the shallow flowers for them. With independent breeding, further mutations may eventually make two species (pp. 231–232).
- The role of "noise" as engine was perceived independently by Einstein. Thermal fluctuations drive irreversible processes, as in the fluctuation-dissipation theorems (derived in Chapter 11 from maximum entropy). The Nyquist law was the first such theorem (p. 232).
- **Jaynes's views on the second law:** natural selection is a different process from the second law. He argues that appeals to the second law to explain evolution are unnecessary, and that the second law would work against evolution. Footnote 24 argues that primordial soup has higher entropy than living matter (p. 232).
- Human intervention can suspend or reverse natural selection (wars, medicine, dog breeding), but can hardly affect the second law. Whether a mutation helps depends on the environment, so the same mutations can give different creatures in Brazil and Finland (pp. 232–233).

### 7.21 Application to economics
- **Jaynes's speculation:** the analogy between equilibrium in physics and biology "surely has other important implications" for economics. The "turbulence" of individual variation (Keynes's "animal spirits") probably drives macroeconomic change toward Adam Smith's equilibrium (p. 233).
- Disturbances (wars, droughts, taxes, tariffs, reserve requirements) act on about the same time scale as the approach to equilibrium, so equilibrium is never attained (p. 233).
- Independent small decisions should average out by the $\sqrt N$ rule. Jaynes says a slight common influence might pull many agents into phase, producing large organized waves, which could then reinforce themselves by positive feedback (p. 233).
- He suggests macroeconomies may be inherently unstable for reasons unrelated to capitalism or socialism, and that "contrarians may be necessary for a stable economy". A wise government might prevent phase locking, as with suspending stock-market trading (pp. 233–234).

### 7.22 The great inequality of Jupiter and Saturn
- Halley (1676) noted that Jupiter's mean motion (30.35 deg/yr) was accelerating and Saturn's (12.22 deg/yr) decelerating. Jupiter seemed to be drifting toward the Sun (p. 234).
- Euler faced 75 inconsistent equations for 8 unknowns, giving $\binom{75}{8}\simeq1.69\times10^{10}$ possible choices of eight equations (7.79). He estimated two parameters and gave up on the rest (p. 234).
- Laplace estimated the parameters well enough to show the drift was not secular. The observations covered a fraction of a cycle of an oscillation with period about 880 years, caused by a near resonance (p. 235):
$$2\times(\text{period of Saturn})\simeq5\times(\text{period of Jupiter})\tag{7.80}$$
$$2\times\frac{360}{12.22}=58.92\text{ yr},\quad5\times\frac{360}{30.35}=59.32\text{ yr}\tag{7.81}$$
- In Halley's time the difference was about 0.66% and decreasing. Jupiter has since reversed its drift, as Laplace predicted. The first half-cycle observed by man will be completed about 2012 (p. 235).
- Footnote 27: Jaynes says his algorithm of Chapter 19 effectively takes a weighted average over all such estimates, with probability-optimal weights (p. 234).

### 7.23 Resolution of distributions into Gaussians
- Jaynes suggests a Gaussian frequency distribution may be loose evidence (far from proof) that some equilibrium has been reached (p. 235).
- **Quetelet's two errors (Jaynes's account):** (1) a normal distribution means a homogeneous population; (2) departures from normality signal inhomogeneity needing explanation. Galton corrected the first: a Gaussian of width $\sigma$ can arise from overlapping narrower Gaussians (via (7.73)). Such subpopulations are in general merely "mathematical artifacts like the sine waves in a Fourier transform", with no individual significance unless shown to be real, as Galton did by measuring widths (p. 235).
- The second assumption is not actually wrong (except in a nitpicking sense) but is ambiguous without extra prior information (p. 235).
- **The problem:** given $g(y)$, find $f(x)\ge0$ with
$$\int dx\,\varphi(y-x|\sigma)f(x)=g(y),\quad-\infty\le y\le\infty\tag{7.82}$$
- For Gaussian $g$, many mixtures give the same $g$, so uniqueness is not expected in general. It may hold if the kernel width $\sigma$ is specified (p. 236).

### 7.24 Hermite polynomial solutions
- The rescaled Hermite polynomials are defined by the generating function (p. 236):
$$\frac{\varphi(x-a)}{\varphi(x)}=\exp\{xa-a^2/2\}=\sum_{n=0}^\infty R_n(x)\frac{a^n}{n!}\tag{7.83}$$
$$R_n(x)=\frac{d^n}{da^n}\big[\exp\{xa-a^2/2\}\big]_{a=0}=(-1)^n e^{x^2/2}\frac{d^n}{dx^n}e^{-x^2/2}\tag{7.84}$$
- The first few are $R_0=1$, $R_1=x$, $R_2=x^2-1$, $R_3=x^3-3x$, $R_4=x^4-6x^2+3$. The conventional $H_n(x)=2^{n/2}R_n(x\sqrt2)$ (p. 236).
- Orthogonality and a key property (p. 236):
$$\int dx\,R_m(x)R_n(x)\varphi(x)=n!\,\delta_{mn}\tag{7.85}$$
$$\int dx\,\varphi(y-x)R_n(x)=y^n\tag{7.86}$$
- If $g(y)=\sum a_ny^n$ (7.87), then a formal solution of (7.82) is (p. 237)
$$f(x)=\sum_na_n\sigma^nR_n(x/\sigma)\tag{7.88}$$
- Since the coefficient of $x^n$ in $R_n$ is unity, (7.87) and (7.88) converge equally well. For $g$ a polynomial or entire function (power series with infinite radius of convergence), the equation has the unique solution (7.88) (p. 237).
- Expanding (7.83) in powers of $x$ gives, with $M=(n-1)/2$ for odd $n$ and $M=n/2$ for even $n$,
$$R_n(x/\sigma)=\sum_{m=0}^M(-1)^m\frac{n!}{2^mm!(n-2m)!}(x/\sigma)^{n-2m}\tag{7.89}$$
$$\frac{n!}{(n-2m)!}(x/\sigma)^{n-2m}=\sigma^{2m-n}\frac{d^{2m}}{dx^{2m}}x^n\tag{7.90}$$
- Hence
$$f(x)=\sum_{m=0}^\infty\frac{(-1)^m\sigma^{2m}}{2^mm!}\frac{d^{2m}}{dx^{2m}}g(x)=g(x)-\frac{\sigma^2}{2}g''(x)+\frac{\sigma^4}{8}g''''(x)-\cdots\tag{7.91}$$
- For a very smooth $g$, the first two or three terms are a good approximation. As $\sigma\to0$, $f\to g$. The first two terms resemble "edge detection". The larger $\sigma$, the more the fine structure of $g$ matters (p. 237).
- **Open issues:** is $f$ non-negative when $g$ is? Is the solution stable? What if $g$ is only piecewise continuous, e.g. rectangular? (p. 237).

> *Intuition note.* Undoing the Gaussian smoothing means alternately subtracting and adding even-order derivatives of $g$. Small $\sigma$ needs few derivatives. Wide kernels need ever finer detail of $g$, which makes the problem delicate.

### 7.25 Fourier transform relations
- With $\mathcal F(k)\equiv\int dx\,f(x)e^{ikx}$ (7.92), (7.82) becomes (p. 238):
$$\exp\{-k^2\sigma^2/2\}\,\mathcal F(k)=\mathcal G(k)\tag{7.93}$$
- If $g$ is piecewise continuous, the Riemann–Lebesgue lemma gives $\mathcal G\sim1/k$ as $k\to\infty$. Then $\mathcal F$ must blow up like $\exp\{+k^2\sigma^2/2\}/k$. If $g$ is continuous with discontinuous first derivatives (e.g. triangular), $\mathcal G\sim k^{-2}$, which is about as bad (p. 238).
- A discontinuity in any derivative of $g$ means no acceptable $f$. This agrees with (7.91), where the formal solution degenerates into high derivatives of a delta-function (p. 238).
- A non-negative $f$ may be a sum of delta-functions (the real goal of Quetelet and Galton). Then $\mathcal F$ does not fall off, so $\mathcal G$ must fall off as $\exp\{-k^2\sigma^2/2\}$. For a positive mixture function $f$, $g$ must be at least as smooth as a Gaussian of width $\sigma$ (p. 238).
- **Practical difficulty:** an empirical $g$ is known only at finitely many approximate points $g_i$. Many analytic functions fit, and because of the instability they give greatly different $f(x)$ (p. 238).
- **Conclusion:** finding the mixture is not a conventional inversion problem. It "is itself a problem of inference", needing probability theory, which can generate a hierarchy of subproblems at different levels (p. 238).

### 7.26 There is hope after all
- Treating (7.82) as Bayesian inference rather than inversion has nearly realised Quetelet's goal. Sivia and Carlile (1992) resolved noisy data into as many as nine Gaussian components (molecular excitation lines) with a Bayesian program (p. 239).
- **Jaynes's claim:** this is a "generalized inverse" problem with no deductive solution, only inferential ones. Specifying the prior information turns an ill-posed problem into a Bayesian exercise (p. 239).
- Footnote 29: Jaynes says a commercial curve-fitting program for resolving Gaussians would degenerate into unstable nonsense as noise increases, while a Bayesian program returns the best resolution without instability and relaxes to the prior estimates when the data are useless (p. 239).
- **Clues toward Exercise 7.9's conjecture:** for $\sigma\to0$, $f\to g$, so for sufficiently small $\sigma$, $f$ is non-negative if $g$ is. For $\sigma\to\infty$, if $f\ge0$ the integral in (7.82) must be at least as broad as the kernel, so $g$ with structure finer than $\sigma$ allows no non-negative $f$. It is not obvious whether any solution exists then. The exercise conjectures an upper bound $\sigma_{\max}$ (p. 239).
- The original goal was ambiguous. A smooth non-Gaussian can arise from many superpositions of Gaussians of different widths. A set of subpopulations found mathematically would have little biological significance unless prior information points to Gaussians of that width as real. The caveat also applies to the Bayesian solution, but Sivia and Carlile had such information (p. 240).

### 7.27 Comments — 7.27.1 Terminology again
- **Origin of "normal".** Pearson (1920) claimed to have introduced it; Seal (1967) attributes it to Galton; neither gives a reference, so Jaynes says a new historical study would be needed. Gauss (1823) called $X'X\hat\beta=X'y$ the "normal equations" and the density ellipsoid the "normal surface". Jaynes presumes "normal" here meant "perpendicular" (p. 240).
- **Objection (Jaynes, noting that Pearson observes it too):** colloquial "normal" implies a value judgment, and it is the Gaussian that is "abnormal", with unique properties. Confidence intervals happen to work with it, which misled workers about other distributions (pp. 240–241).
- "Gaussian" fits Stigler's law of eponymy. Jaynes says Laplace noted its fundamental nature when Gauss was six, and de Moivre found the distribution before Laplace was born. Gauss's 1809 derivation made his name stick (p. 241).
- **Proposal:** "central distribution", since it is the equilibrium toward which others gravitate under many operations and which is maintained under more. Example: Boltzmann (1870s) argued that collisions bring a gas to a Gaussian velocity distribution, and Kennard (1938) showed it is maintained in any conservative force field (p. 241).
- Jaynes keeps using "Gaussian" (no value judgment, and familiar to both statisticians and scientists). It appears to him that emotionally loaded names ("unbiased", "admissible") are a major cause of confusion in the field (p. 241).
- **Maximum entropy.** The Boltzmann distribution is Gaussian (Maxwellian) in velocities. If a transformation discards information but leaves certain quantities invariant, then, under very general conditions, repeating it drives the distribution to maximum entropy subject to those constraints (pp. 241–242).
- The CLT is a special case, with convolution conserving first and second moments. Pólya (1920) intended "central" to modify "theorem", but students read it as "central limit". Jaynes says Pólya's choice of words appears after all fortunate, since "central limit" can mean a limit toward the central distribution (p. 242).

## Toy example (ours, not from the text)
Galton-type stability with 3-4-5 numbers. Let parent deviations be $N(0,\sigma_1^2)$ with $\sigma_1=5$ and children $y|x\sim N(ax,\sigma_2^2)$ with $\sigma_2=3$. By (7.74), the child variance is $\sigma^2=a^2\sigma_1^2+\sigma_2^2$.
- Stability needs $\sigma=\sigma_1$: $a^2=1-9/25=16/25$, so $a=\pm0.8$.
- Check: $0.8^2\cdot25+9=16+9=25$, so $\sigma=5$ ✓.
- With $a=1$ (no reversion): $25+9=34$, $\sigma\approx5.83$, so spread grows each generation.
- With $a=0.5$: $6.25+9=15.25$, $\sigma\approx3.91$, so spread shrinks.
- Check of (7.72): for $N=100$, $\epsilon\le1.35\times10^{-4}\times10=1.35\times10^{-3}$. This is three-figure accuracy for terms of order 1.

## Concepts
- [[convolution]] (new) — density of a sum of independent variables, $f_1*f_2=\int dx_1f_1(x_1)f_2(y-x_1)$ (p. 223)
- [[characteristic-function]] (new) — $\langle e^{i\alpha x}\rangle$; convolution becomes multiplication (p. 223)
- [[central-limit-theorem]] (new) — sums of many independent terms tend to a Gaussian. Here the editor shows how it follows from cumulants (p. 222)
- [[cauchy-distribution]] (new) — the one law whose sample mean has the same law as one observation (p. 224)
- [[maximum entropy principle]] — here, the Gaussian has maximum entropy at fixed variance, so information-discarding operations that conserve variance approach it (p. 221)
- [[nuisance-parameter]] (new) — relevant but uninteresting parameter, included in the model and integrated out (p. 220)
- [[regression-to-the-mean]] (new) — Galton's "reversion", the systematic counter-drift balancing spreading (p. 228)
- [[gaussian-mixture-inverse-problem]] (new) — solving $\int\varphi(y-x|\sigma)f(x)dx=g(y)$ for $f$; ill-posed as inversion, treated as inference (p. 236)
- [[hermite-polynomials]] (new) — $R_n$ with $\int\varphi(y-x)R_n(x)dx=y^n$ (p. 236)
- [[Prior distribution]] — prior information is essential in the Gaussian-resolution problem and in safety estimation (pp. 220, 239–240)

## Canonical instances
- [[rounding-error-sum]] — $\sqrt N$ cancellation lets four-figure sums use three-figure terms (p. 226)
- [[galton-heights]] — reversion and spread in heights; $a=\pm\sqrt{1-\sigma_2^2/\sigma_1^2}$ (p. 228)
- [[einstein-diffusion]] — $D=\lambda kT$ as balance of spreading and drift (p. 229)
- [[jupiter-saturn-great-inequality]] — 880-year near-resonance oscillation resolved by Laplace (p. 235)
- [[sivia-carlile-gaussian-lines]] — Bayesian resolution of up to nine Gaussian components (p. 239)

## Bridges (candidates)
- [same-math] Gaussian convolution: variances add ↔ Bayesian: Gaussian prior × Gaussian noise gives a Gaussian marginal with summed variances — both are (7.49).
- [structural-analogy] Galton's reversion vs. spreading balance ↔ Bayesian: partial pooling/shrinkage toward the population mean — both pull individuals to the mean while the population keeps a fixed spread.
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law.
- [structural-analogy] Mixture-of-Gaussians resolution as an ill-posed inverse problem ↔ Bayesian: hierarchical models and regularizing priors — prior information selects among many consistent decompositions.
- [metaphor] Phase-locking of agents into waves ↔ physics: positive-feedback oscillation — Jaynes's hedged economic analogy.

## Questions this raises
- Under what conditions on the $f_i$ is the cumulant truncation (7.53) a good approximation, and does it hold for ratios of probabilities (the editor's questions)?
- For which $g$ does a non-negative $f$ exist for $\sigma<\sigma_{\max}$, and is "non-negative iff $\sigma<\sigma_{\max}$" true (Exercise 7.9)?
- What prior information would one assign in a Bayesian mixture analysis so that the component widths are meaningful?
- How would the error analysis change if the rounding errors were positively correlated?

## Exercises worth doing
- Editor's Ex. 7.5 (p. 222) — fill in the cumulant derivation of the CLT and its validity conditions — difficulty: medium
- Ex. 7.6 (p. 226) — generalise the rounding-error analysis to a Fourier series with signed terms — difficulty: medium
- Ex. 7.7 (p. 226) — how positive correlation between rounding errors breaks the $\sqrt N$ rule — difficulty: hard
- Ex. 7.8 (p. 229) — reformulate Galton's four-variable problem (father, mother, son, daughter) — difficulty: hard
- Ex. 7.9 (p. 239) — prove or disprove a $\sigma_{\max}$ bound for non-negative mixing function — difficulty: hard

## Reading notes
- **Scope:** this part starts mid-paragraph on p. 220 (nuisance-parameter discussion); the preceding section heading is not on these pages, but the next heading is §7.14, so it is presumably §7.13. It ends at the end of §7.27.1 (p. 242); no further heading appears on these pages. Printed = pdf − 30.
- **Misprints and printing issues visible in the images:**
  - (7.51): the integration variable is printed $dy\,\phi(y)^n$, where $d\alpha\,\phi(\alpha)^n$ is clearly meant.
  - (7.53): the last line prints $(y-n\langle x\rangle x)^2$, where $(y-n\langle x\rangle)^2$ is evidently meant.
  - (7.52): printed $\alpha C_1$ without a factor $i$. I copied it as printed, and Appendix C is not in this unit to check.
  - p. 226 refers to "Exercise 7.5" (generalisation) and "Exercise 7.6" (proviso), but the printed exercises are 7.6 and 7.7. Exercise 7.5 is the editor's CLT exercise.
  - p. 239: "Section 7.2.5" is cited but is not in these pages.
  - p. 234: the sentence saying the problem was solved in 1787 by one born "that same year" is ambiguous: Laplace is printed as 1749–1827, so the phrase does not match 1787. I do not resolve this.
  - (7.81): $5\times360/30.35$ computes to about 59.31, printed 59.32. This is probably a rounding difference.
- The text layer for several equations (7.46–7.48, 7.52–7.53) was garbled. I checked these against the page images.
- Editor's material (Exercise 7.5) is the editor's voice, not Jaynes's. Editorial remarks such as the statement that Jaynes did not actually derive the CLT in §7.16 are the editor's.
