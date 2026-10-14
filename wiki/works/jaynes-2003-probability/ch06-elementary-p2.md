---
id: jaynes-2003-probability/ch06-elementary-p2
work: jaynes-2003-probability
unit: "6 Elementary parameter estimation (part 2/2): §6.11 end – §6.23"
pages: 177-197
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
# Elementary parameter estimation, part 2: qualitative priors, Jeffreys prior, taxicab problem

## L0 — One line
Vague but smooth priors barely change an estimate, whereas even one qualitative fact (a common hidden source) can change it a lot and tighten it; so data never "speak for themselves."

## L1 — The gist (≤ 120 words)
Two robots estimate particle numbers from counts of a counter with efficiency $\phi=0.1$. Mr A knows nothing about the source. Mr B knows it is a fixed source of unknown strength. With the first interval's count they agree; once a second interval is counted, B's qualitative knowledge makes the intervals informative about each other, so his estimates move and his error shrinks. A uniform prior, a cutoff $N$, and Jeffreys' $1/s$ prior give nearly the same answers. A rectangular-distribution ("taxicab") problem shows that Bayesian analysis stays sensible for tiny $n$. The unit ends by arguing against Fisher's "let the data speak" maxim.

**Prerequisites:** Bayes' theorem; Poisson and binomial distributions; summing series; mean, mode (most probable value) and variance; Gamma-type integrals $\int s^k e^{-as}\,ds$; basic limits.

## L2 — Key ideas (5–10 bullets)
- Mr A's prior is only a smooth, roughly flat description of ignorance. Its upper cutoff $N$ and its details at large $n_1$ make a negligible difference to his conclusions, because the likelihood is concentrated near $n_1\approx 100$ (pp. 178–180).
- Jeffreys' $1/s$ prior, instead of a flat one, lowers the mode (most probable value) and the mean of $n_1$ by 9 each (mode 100→91, mean 109→100). That is under 10% with 10 counts. Rule of thumb: one extra power of the parameter in the prior has about the effect of one more data point (pp. 181–183).
- Mr B's knowledge of a common source $s$ opens a second inference route $c_2\to n_2\to s\to n_1$. His posterior for $n_1$ is, up to normalization, the product of the two routes' distributions, and his error falls (pp. 184–187).
- Chebyshev's inequality turns standard deviations into guaranteed probability intervals. With enough extra counts $m\to\infty$, Mr B's posterior for $n_k$ approaches the known-source Poisson result (pp. 186, 188–190).
- Posteriors tend to Gaussian as data accumulate, since a single-peaked function raised to a high power becomes Gaussian (p. 189).
- In the rectangular-distribution problem, $p(\alpha|DI)\propto\alpha^{-n}$ on $[\alpha_0,\alpha_1]$. The cases $n=1$ and $n=0$ follow from the general formula, by a limit for $n=1$ and direct substitution for $n=0$, because the formula is an entire function of $n$ (pp. 191–194).
- Jaynes's claim: with proper priors and no logical contradiction, Bayesian analysis has no pathological small-sample cases. Jaynes thinks Mr B's results appear beyond the reach of orthodox methods, which do not allow integrating out a nuisance parameter (an unwanted unknown such as $s$) with a prior (pp. 193, 195).
- Jaynes argues that the data cannot speak for themselves. Maximum likelihood (picking the parameter value that makes the data most probable), if not supplemented with prior information, favours the "sure thing" hypothesis, and mechanism and plausibility must come from prior information (pp. 195–197).

## L3 — Walkthrough

### End of §6.11 and Exercise 6.5 (p. 177)
The preceding material (outside this unit) showed that, as with inversion of urn distributions, simple prior information can change the conclusions a lot (p. 177). Exercise 6.5 asks for a dead-time generalization: two or more particles within a short interval $\Delta t$ give at most one count (p. 177).

### 6.12 Effects of qualitative prior information (pp. 177–178)
- Two robots have different prior information. Mr A knows nothing about the hidden source: it could be an accelerator switched arbitrarily, or little men moving radioactive samples. Mr B knows one more qualitative fact: the source is a long-lived radioactive sample in a fixed position. He does not know its strength (pp. 177–178).
- Both know the source is not infinitely strong, and both know $\phi=0.1$. They want $n_1$, the number of particles, from counts. In the first second $c_1=10$ (p. 178).
- Fig. 6.2 shows the structure. For A, each pair $n_i\to c_i$ is logically independent. For B, a common source strength $s$ points to every $n_i$, so $n_2$ becomes relevant to $n_1$ (p. 177).
- Bayes for A:
$$p(n_1|\phi c_1 I_A)=p(n_1|I_A)\frac{p(c_1|\phi n_1 I_A)}{p(c_1|\phi I_A)}=\frac{p(n_1|I_A)\,p(c_1|\phi n_1 I_A)}{p(c_1|\phi I_A)}\tag{6.103}$$
$$p(c_1|\phi I_A)=\sum_{n_1}p(c_1|\phi n_1 I_A)\,p(n_1|I_A)\tag{6.104}$$
- The difficulty: what is $p(n_1|I_A)$? Theories that treat probability as a physical fact give A no basis for a "true" prior (p. 178).

### 6.13 Choice of a prior (pp. 178–179)
- Jaynes: there is no "objectively true" probability. The prior describes A's own state of knowledge, on which A is the authority. General principles come in Chapters 11–12 (p. 178).
- A's prior should avoid structure (oscillations, jumps), which would imply detailed information he lacks. This is not a formal principle, so the result is not unique. Jeffreys (1939) noted that it need not be: "almost any" prior smooth in the region of high likelihood gives substantially the same conclusions (p. 178).
- Footnote 11: a prior can make a large difference only by modulating the likelihood near its peak, not its tails (p. 178).
- A takes a uniform prior up to a large finite $N$:
$$p(n_1|I_A)=\begin{cases}1/N & 0\le n_1<N\\ 0 & N\le n_1\end{cases}\tag{6.105}$$
- $N$ is ad hoc. $N\sim10^{60}$ would vaporize the galaxy, so A knows $N$ is far smaller. If conclusions depended strongly on $N$, A would have to think harder, but they will not (p. 179).

### 6.14 On with the calculation! (pp. 179–181)
- The $1/N$ cancels:
$$p(n_1|\phi c_1 I_A)=\begin{cases}A\,p(c_1|\phi n_1)& 0\le n_1<N\\0& N\le n_1\end{cases}\tag{6.106}$$
$$A^{-1}=\sum_{n_1=0}^{N-1}p(c_1|\phi n_1)\tag{6.107}$$
- The likelihood peaks at $n_1=c_1/\phi=100$ (from (6.100), an earlier result). For $n_1\phi\gg c_1$ it falls like $n_1^{c_1}(1-\phi)^{n_1}\simeq n_1^{c_1}\exp\{-n_1\phi\}$. So if $N$ is a few hundred, the sum is almost the same as the sum to infinity (p. 179).
- Jaynes passes to $N\to\infty$ after applying Bayes. This is not because $N$ is believed infinite, but because it simplifies the algebra without affecting the result. Tool:
$$\sum_{m=0}^{\infty}\binom{m+a}{m}m^n x^m=\Big(x\frac{d}{dx}\Big)^n\frac{1}{(1-x)^{a+1}},\quad |x|<1\tag{6.108}$$
- Normalization, with $m=n_1-c_1$ and $p(c_1|\phi n_1)=\binom{n_1}{c_1}\phi^{c_1}(1-\phi)^{n_1-c_1}$ (the binomial form implied by (6.112)):
$$A^{-1}\simeq\sum_{n_1}p(c_1|\phi n_1)=\phi^{c}\sum_{m=0}^\infty\binom{m+c}{m}(1-\phi)^m=\phi^{c}\Big\{\frac{1}{[1-(1-\phi)]^{c+1}}\Big\}=\frac1\phi\tag{6.109}$$
- **Exercise 6.6** (p. 180) defines the tail $S(N)=\sum_{n_1\ge N}p(c_1|\phi n_1)$ and states that $\delta=S(N)/S(0)\simeq e^{-N\phi}(N\phi)^{c_1}/c_1!$ for $N\phi\gg1$. For $\phi=0.1$, $c_1=10$, an upper limit below about 270 is needed to matter at one part in $10^4$. Behaviour at $n_1\ge340$ matters below one part in $10^6$, and at $n_1\ge400$ below $10^{8}$.
- Jaynes: ferocious arguments over prior range look silly. Its pragmatic consequences are usually strictly nil at finite decimal accuracy. If prior information did encroach on $n_1<270$, it would matter, "as it should be" (p. 180).
- Result:
$$p(n_1|\phi c_1 I_A)=\phi\,p(c_1|\phi n_1)=\binom{n_1}{c_1}\phi^{c_1+1}(1-\phi)^{n_1-c_1}\tag{6.112}$$
- A's mode equals the maximum-likelihood estimate:
$$(\hat n_1)_A=c_1/\phi=100\tag{6.113}$$
- Posterior mean, with $m=n_1-c_1-1$ in the sum:
$$\langle n_1\rangle_A-c_1=\sum_{n_1=c_1}^\infty(n_1-c_1)p(n_1|\phi c_1I_A)=\phi^{c_1+1}(1-\phi)(c_1+1)\sum_{n_1}\binom{n_1}{n_1-c_1-1}(1-\phi)^{n_1-c_1-1}\tag{6.114}$$
By (6.108),
$$\sum_{m=0}^\infty\binom{m+c_1+1}{m}(1-\phi)^m=\frac{1}{\phi^{2+c_1}}\tag{6.115}$$
$$\langle n_1\rangle_A=c_1+(c_1+1)\frac{1-\phi}{\phi}=\frac{c_1+1-\phi}{\phi}=109\tag{6.116}$$
- Mr B (p. 181): he knows a fixed $s$ and some upper limit $S_0$, and takes $s$ uniform on $[0,S_0)$ (the page prints $\theta$ where $\phi$ is presumably meant):
$$p(n_1|\theta I_B)=\int_0^\infty ds\,p(n_1|s)p(s|\theta I_B)=\frac1{S_0}\int_0^{S_0}ds\,\frac{s^{n_1}e^{-s}}{n_1!}\tag{6.117}$$
- If $n_1\ll S_0$ the integral is about 1, so
$$p(n_1|\theta I_B)=p(s|\theta I_B)=1/S_0=\text{const.},\quad n_1<S_0\tag{6.118}$$
- Unless $S_0$ is below about 300, B's extra knowledge does not help with only $c_1$:
$$p(n_1|c_1I_B)=p(n_1|\phi c_1I_A)=\phi\,p(c_1|\phi n_1)\tag{6.119}$$

*Intuition note.* The likelihood from 10 counts is concentrated around $n_1\approx100$. A prior that is flat there cannot be told apart from one that is flat to 300 or to $10^{10}$, since the tail beyond that carries almost no weight.

### 6.15 The Jeffreys prior (pp. 181–183)
- Jeffreys (1939) proposed that complete ignorance of a positive continuous variable is expressed by a prior uniform in its logarithm:
$$p(s|I_J)\propto 1/s,\quad 0\le s<\infty\tag{6.120}$$
- It cannot be normalized, but here all integrals converge. Jaynes: in almost all cases it can be approached as a limit of proper priors. If no proper posterior results, the robot is warning that the data are too uninformative about very large or very small $s$ to justify any definite conclusion (p. 182).
- Jeffreys' justification is invariance: a uniform density in $s$ is not uniform in $t=s^2$, but the $1/s$ rule says the same thing for $s$ or any power $s^m$ (p. 182).
- Jaynes (author's view, promised for later): in Chapter 12 transformation groups, and then marginalization theory, will derive the rule uniquely for a scale parameter. He calls it "the only correct way" to express complete ignorance of a scale parameter. The open question is whether $s$ is a scale parameter here, and he just tests the rule (p. 182).
- Results:
$$p(n_1|I_J)=\frac1{n_1},\quad p(c_1|I_J)=\frac1{c_1},\quad p(n_1|\phi c_1I_J)=\frac{c_1}{n_1}p(c_1|\phi n_1)\tag{6.121}$$
$$(\hat n_1)_J=\frac{c_1-1+\phi}{\phi}=91,\qquad\langle n_1\rangle_J=\frac{c_1}{\phi}=100\tag{6.122}$$
(the page prints "$c$" for $c_1$ in the second formula). The Jeffreys prior lowers both mode and mean by nine, bringing the mean back to the maximum-likelihood value (p. 182).
- Even a drastic prior change with meagre data moved the result by under 10%, which is small against the inevitable probable error (pp. 182–183).
- **Rule of thumb** (p. 183): changing the prior by one power of $\alpha$ has about the effect of one more data point. The likelihood has relative width about $1/\sqrt n$, and one more power adds a small slope near the maximum. With $n$ effective independent observations, the inevitable fractional error is about $1/\sqrt n$, while the prior change shifts the estimate by about $1/n$. With 10 counts the shift is just under 10%. With 100 counts the error is about 10% and the prior-induced difference under 1%.
- Footnote 12: the $1/\sqrt n$ rule fails for estimating a discontinuity's location and for strongly correlated data (p. 183).
- Jaynes: for principle these questions matter (Chapter 12); in practice the Jeffreys prior is a small refinement mattering only for very small samples (p. 183). Footnote 13: this is "most definitely not true" if a prior describes a definite piece of prior knowledge (p. 183).

*Intuition note.* Changing a vague prior shifts the posterior by an amount comparable to adding one observation. That is small once there are many data.

### 6.16 The point of it all (pp. 183–186)
- Second second: $c_2=16$. A sees no relation between intervals, so
$$(\hat n_2)_A=c_2/\phi=160,\quad\langle n_2\rangle_A=\frac{c_2+1-\phi}{\phi}=169\tag{6.123, 6.124}$$
and his estimate of $n_1$ is unchanged (p. 184).
- For B, $c_2$ is relevant to $n_1$:
$$p(n_1|\phi c_2c_1I_B)=p(n_1|\phi c_1I_B)\frac{p(c_2|\phi n_1I_B)}{p(c_2|\phi c_1I_B)}\tag{6.125}$$
The denominator is a normalizer. Resolving $c_2$ over $s$:
$$p(c_2|\phi n_1I_B)=\int_0^\infty ds\,p(c_2|\phi sI_B)\,p(s|\phi n_1I_B)\tag{6.126}$$
(the intermediate steps of (6.126) use $p(c_2|s\phi n_1I_B)=p(c_2|\phi sI_B)$, since $s$ screens off $n_1$). With $n_1\ll S_0$ and (6.118),
$$p(s|\phi n_1I_B)=p(s|\phi I_B)\frac{p(n_1|\phi sI_B)}{p(n_1|\phi I_B)}=p(n_1|\phi s),\quad n_1\ll S_0\tag{6.127}$$
Using the Poisson forms (6.86), (6.84):
$$p(c_2|\phi n_1I_B)=\int_0^\infty ds\Big[\frac{e^{-s\phi}(s\phi)^{c_2}}{c_2!}\Big]\Big[\frac{e^{-s}s^{n_1}}{n_1!}\Big]=\binom{n_1+c_2}{c_2}\frac{\phi^{c_2}}{(1+\phi)^{n_1+c_2+1}}\tag{6.128}$$
- Putting (6.119) and (6.128) into (6.125), and summing for the normalizer, gives the result (not a binomial distribution):
$$p(n_1|\phi c_2c_1I_B)=\binom{n_1+c_2}{c_1+c_2}\Big(\frac{2\phi}{1+\phi}\Big)^{c_1+c_2+1}\Big(\frac{1-\phi}{1+\phi}\Big)^{n_1-c_1}\tag{6.129}$$
- Direct resolution over $s$ gives the same answer, because $p(s|\phi c_2c_1I_B)\propto p(c_2|\phi sI_B)p(c_1|\phi sI_B)$. Jaynes calls this a severe consistency test of the rules (pp. 184–185):
$$p(n_1|\phi c_2c_1I_B)=\int_0^\infty ds\,p(n_1|\phi sc_1I_B)\,p(s|\phi c_2c_1I_B)\tag{6.130}$$
- Mode: set the ratio of neighbours to 1,
$$\frac{p(n_1|\phi c_2c_1I_B)}{p(n_1-1|\phi c_2c_1I_B)}=\frac{n_1+c_2}{n_1-c_1}\frac{1-\phi}{1+\phi}=1\tag{6.131}$$
which gives (the author's algebra, checked)
$$(\hat n_1)_B=\frac{c_1}{\phi}+(c_2-c_1)\frac{1-\phi}{2\phi}=\frac{c_1+c_2}{2\phi}+\frac{c_1-c_2}{2}=127\tag{6.132}$$
(added step: this equals $[c_1(1+\phi)+c_2(1-\phi)]/(2\phi)$.)
- Mean:
$$\langle n_1\rangle_B=\frac{c_1+1-\phi}{\phi}+(c_2-c_1-1)\frac{1-\phi}{2\phi}=\frac{c_1+c_2+1-\phi}{2\phi}+\frac{c_1-c_2}{2}=131.5\tag{6.133}$$
By symmetry for $n_2$: $(\hat n_2)_B=133$, $\langle n_2\rangle_B=137.5$ (6.134). Both estimates rise, and the mode–mean gap halves, suggesting a narrower posterior (p. 185).
- Why (p. 185): $c_1$ and $c_2$ together estimate $s$, which bears on $n_1$. B has two routes: $c_1\to n_1$ directly, and $c_2\to n_2\to s\to n_1$. By the second route alone (if $c_1$ were unknown):
$$p(n_1|\phi c_2I_B)=\int_0^\infty ds\,p(n_1|s)p(s|c_2I_B)=\frac{\phi^{c_2+1}}{c_2!(1+\phi)^{c_2+1}}\frac{(n_1+c_2)!}{n_1!(1+\phi)^{n_1}}\tag{6.135}$$
- B's final distribution is, up to normalization, the product of the two routes' distributions, because $p(c_1c_2|\phi n_1)=p(c_1|\phi n_1)p(c_2|\phi n_1)$:
$$p(n_1|\phi c_1c_2I_B)=(\text{const.})\times p(n_1|\phi c_1I_B)\,p(n_1|\phi c_2I_B)\tag{6.136}$$
The second route acts as a correction factor on the direct route (pp. 185–186). Jaynes conjectures that more counts $c_3,\dots,c_m$ might approach the known-source accuracy, and checks it below (p. 186).

*Intuition note.* B's qualitative fact lets every other interval inform him about $s$, and $s$ informs him about $n_1$. A has no such link, so A learns nothing about $n_1$ from $c_2$.

### 6.17 Interval estimation (p. 186)
- The ideal is the whole distributions (6.137), with statements like "90% lies in $\alpha<n_1<\beta$". Jaynes settles for standard deviations.
- **Chebyshev**: for any distribution with standard deviation $\sigma$, the probability $P$ within $\langle n_1\rangle\pm t\sigma$ satisfies
$$P\ge1-\frac{1}{t^2}\tag{6.139}$$
It says nothing for $t\le1$. For any distribution with finite $\langle n\rangle$ and $\langle n^2\rangle$, at least 3/4 lies within $\pm2\sigma$ and at least 8/9 within $\pm3\sigma$.
- Footnote 14 proof: with $y=x-\langle x\rangle$,
$$a^2(1-P)=a^2p(|y|>a)=a^2\int_{|y|>a}dx\,p(x)\le\int_{|y|>a}dx\,y^2p(x)\le\int_{-\infty}^\infty dx\,y^2p(x)=\sigma^2\tag{6.138}$$
and $a=t\sigma$ gives $t^2(1-P)\le1$. It includes discrete cases via delta-functions (p. 186).

### 6.18 Calculation of variance (pp. 186–188)
- Moments follow from (6.108). The variances are:
$$\mathrm{var}(n_1|\phi c_1I_A)=\frac{(c_1+1)(1-\phi)}{\phi^2}\tag{6.140}$$
$$\mathrm{var}(n_1|\phi c_2c_1I_B)=\frac{(c_1+c_2+1)(1-\phi^2)}{4\phi^2}\tag{6.141}$$
$$\mathrm{var}(n_1|\phi c_1I_J)=\frac{c_1(1-\phi)}{\phi^2}\tag{6.142}$$
- Table 6.1 (p. 187), as printed:

| | | Problem 1 $n_1$ | Problem 2 $n_1$ | Problem 2 $n_2$ |
|---|---|---|---|---|
| A | most probable | 100 | 100 | 160 |
| | mean ± s.d. | 109 ± 31 | 109 ± 31 | 169 ± 39 |
| B | most probable | 100 | 127 | 133 |
| | mean ± s.d. | 109 ± 31 | 131.5 ± 25.9 | 137.5 ± 25.9 |
| Jeffreys | most probable | 91 | 121.5 | 127.5 |
| | mean ± s.d. | 100 ± 30 | 127 ± 25.4 | 133 ± 25.4 |

- Jaynes: B's extra information changes his estimates considerably and appreciably cuts his probable error. Even purely qualitative prior information with no link to frequencies can greatly alter conclusions. Virtually every real problem of scientific inference has qualitative prior information of more or less this kind, so any method that fails to take prior information into account is capable of misleading us, in a potentially dangerous way; a reasonable result in one problem is no guarantee for the next (p. 187).
- If B knew only $c_2$ (route of (6.135)):
$$\hat n_1=c_2/\phi=160\tag{6.143}$$
$$\text{mean}\pm\text{s.d.}=\frac{c_2+1}{\phi}\pm\frac{\sqrt{(c_2+1)(\phi+1)}}{\phi}=170\pm43.3\tag{6.144}$$
This is slightly worse than A's direct route for equal counts, since the factor $(1-\phi)$ in (6.140) becomes $(1+\phi)$. At low efficiency the two routes are about equally reliable. At $\phi\simeq1$ the direct route is far more reliable (p. 188).

### 6.19 Generalization and asymptotic forms (pp. 188–190)
- With $s$ known, the Poisson distribution (6.89) has standard deviation $\sqrt{s(1-\phi)}=10.8$ for $s=130$. B's current s.d. is about 2.5 times that (p. 188).
- For $1\le k\le m$, since given $s$ the other $c_i$ ($i\ne k$) are irrelevant to $n_k$:
$$p(n_k|\phi c_1\cdots c_mI_B)=\int_0^\infty ds\,p(n_k|\phi sc_kI_B)\,p(s|\phi c_1\cdots c_mI_B)\tag{6.145}$$
$$p(s|\phi c_1\cdots c_mI_B)=p(s|\phi I_B)\frac{p(c_1\cdots c_m|\phi sI_B)}{p(c_1\cdots c_m|\phi I_B)}=(\text{const.})\,p(s|\phi I_B)\,p(c_1|\phi sI_B)\cdots p(c_m|\phi sI_B)\tag{6.146}$$
Using (6.86) and normalizing, with $c\equiv c_1+\cdots+c_m$:
$$p(s|\phi c_1\cdots c_mI_B)=\frac{(m\phi)^{c+1}}{c!}s^c\exp\{-ms\phi\}\tag{6.147}$$
$$\hat s=\frac{c}{m\phi},\quad\langle s\rangle=\frac{c+1}{m\phi},\quad\mathrm{var}(s)=\langle s^2\rangle-\langle s\rangle^2=\frac{c+1}{m^2\phi^2}=\frac{\langle s\rangle}{m\phi}\tag{6.148}$$
- As $m\to\infty$ the posterior sharpens, and it appears to approach a delta-function,
$$p(s|\phi c_1\cdots c_mI_B)\to\delta(s-s'),\qquad s'\equiv\lim_{m\to\infty}\frac{c_1+\cdots+c_m}{m\phi}\tag{6.149, 6.150}$$
- Expanding $\log$ of (6.147) about $\hat s$ to quadratic order gives a Gaussian, valid for all $s$ in the sense that the difference is small everywhere (the ratio is not near 1 everywhere):
$$p(s|\phi c_1\cdots c_mI_B)\to A\exp\Big\{-\frac{c(s-\hat s)^2}{2\hat s^2}\Big\}\tag{6.151}$$
$$(s)_{\rm est}=\hat s\Big(1\pm\frac1{\sqrt c}\Big)\quad(c\to\infty)\tag{6.152}$$
Jaynes: posteriors generally become Gaussian as data grow, since a single-peaked function raised to a high power becomes Gaussian (p. 189).
- Inserting (6.89) and (6.147):
$$p(n_k|\phi c_1\cdots c_mI_B)=\int_0^\infty ds\,\frac{e^{-s(1-\phi)}[s(1-\phi)]^{n_k-c_k}}{(n_k-c_k)!}\frac{(m\phi)^{c+1}}{c!}s^c e^{-ms\phi}\tag{6.153}$$
$$p(n_k|c_1\cdots c_mI_B)=\frac{(n_k-c_k+c)!}{(n_k-c_k)!\,c!}\frac{(m\phi)^{c+1}(1-\phi)^{n_k-c_k}}{(1+m\phi-\phi)^{n_k-c_k+c+1}}\tag{6.154}$$
This generalizes (6.135). As $m,c\to\infty$ with $c/m\phi\to s'$ it tends to the Poisson distribution (6.89):
$$p(n_k|c_1\cdots c_mI_B)\to\frac{e^{-s'(1-\phi)}}{(n_k-c_k)!}[s'(1-\phi)]^{n_k-c_k}\tag{6.155}$$
So B's s.d. can fall from 26 to 10.8 (A: 31). For finite $m$, with $\langle s\rangle=(c+1)/m\phi$:
$$\langle n_k\rangle=c_k+\langle s\rangle(1-\phi),\qquad\hat n_k=c_k+\hat s(1-\phi)\tag{6.156, 6.157}$$
- B's revised estimates in problem 2 stay within A's error range. Jaynes says no theorem guarantees this. If $c_2=80$, B's estimate would fall far outside A's limits, and B's common sense would make him doubt $I_B$. That would be one of the "something else" hypotheses at about $-100$ db from Chapter 4, revived by unexpected evidence (p. 190).
- Exercise 6.7 asks for the conclusions translated into the disease-incidence scenario, with advice on when the model fits (p. 190).

*Intuition note.* More intervals pin down $s$, and then $n_k$ is known up to its own Poisson scatter about $c_k+s(1-\phi)$. Knowing $s$ exactly is the limit of B's learning.

### 6.20 Rectangular sampling distribution (pp. 190–192)
- The taxicab problem: you see taxi number 27 in an unknown town. Most people guess $N_{\rm est}=2\times27=54$ but few can justify it. The model is $N$ cabs numbered $1,\dots,N$, with each equally likely to be seen, so $N\ge27$ deductively. Jaynes says orthodoxy has no way to deal with it (p. 190).
- Jaynes studies the continuous version (more than one taxi in view) and leaves the discrete one as an unnumbered exercise: write the parallel solution and state the exact relationship between the two (p. 191). Data $D=\{x_1,\dots,x_n\}$, with width $\alpha$ to estimate:
$$p(x_i|\alpha I)=\begin{cases}\alpha^{-1}&0\le x_i\le\alpha<\infty\\0&\text{otherwise}\end{cases}\tag{6.158}$$
$$p(D|\alpha I)=\prod_ip(x_i|\alpha I)=\alpha^{-n},\quad0\le\{x_1,\dots,x_n\}\le\alpha\tag{6.159}$$
(outside the stated inequalities the left side is zero).
- Posterior:
$$p(\alpha|DI)=p(\alpha|I)\frac{p(D|\alpha I)}{p(D|I)}\tag{6.160}$$
- A proper prior and bounded likelihood give a proper posterior, provided the data do not contradict the other information. If some $x_i<0$, the model is deductively wrong and the robot "crashes" (p. 191).
- Data may fit the model but contradict other prior information. With the proper prior
$$p(\alpha|I)=(\alpha_1-\alpha_{00})^{-1},\quad\alpha_{00}\le\alpha\le\alpha_1\tag{6.161}$$
any $x_i>\alpha_1$ gives a contradiction. Jaynes then supposes the data are consistent with all the prior information (p. 192; footnote 15 calls the sharp bounds an ideal limiting case, like perfect triangles in geometry).
- Normalizer, with $x_{\max}=\max\{x_1,\dots,x_n\}$:
$$p(D|I)=\int_Rd\alpha\,(\alpha_1-\alpha_{00})^{-1}\alpha^{-n},\qquad R=\{\alpha_{00}\le\alpha\le\alpha_1,\ x_{\max}\le\alpha\le\alpha_1\}\tag{6.162, 6.163}$$
If $x_{\max}\le\alpha_{00}$ only the first condition matters, and the data values are irrelevant (only $n$ matters). If $\alpha_{00}\le x_{\max}$ the data supersede $\alpha_{00}$.
- With $(\alpha_1-\alpha_{00})$ cancelling, for $n>1$:
$$p(\alpha|DI)=\frac{(n-1)\alpha^{-n}}{\alpha_0^{1-n}-\alpha_1^{1-n}},\quad\alpha_0\le\alpha\le\alpha_1,\ n>1\tag{6.164}$$
with $\alpha_0\equiv\max(\alpha_{00},x_{\max})$ (p. 192).

### 6.21 Small samples (pp. 192–193)
- Jaynes: orthodox statistics can give pathologies at small $n$ (e.g. an estimator outside the parameter space), which are passed over rather than read as errors. Bayesian analysis, with proper priors and no logical contradiction, has no pathological cases (pp. 192–193).
- At $n=1$, (6.164) looks like $0/0$. Repeating the derivation gives
$$p(\alpha|DI)=\frac{\alpha^{-1}}{\log(\alpha_1/\alpha_0)},\quad\alpha_0\le\alpha\le\alpha_1,\ n=1\tag{6.165}$$
- At $n=0$, $D$ is "no data", $p(D|\alpha I)=p(D|I)=1$, and the posterior is the prior:
$$p(\alpha|DI)=p(\alpha|I),\quad n=0\tag{6.166}$$

### 6.22 Mathematical trickery (pp. 193–194)
- Both results already lie inside (6.164). In the real problem $n$ is a non-negative integer, but the expression is defined for complex $n$ and, for $\alpha_1<\infty$, is an entire function of $n$. So we may evaluate at $n=1$ by a limit:
$$\frac{n-1}{\alpha_0^{1-n}-\alpha_1^{1-n}}=\frac{n-1}{\exp\{-(n-1)\log\alpha_0\}-\exp\{-(n-1)\log\alpha_1\}}=\frac{n-1}{[1-(n-1)\log\alpha_0+\cdots]-[1-(n-1)\log\alpha_1+\cdots]}\to\frac{1}{\log(\alpha_1/\alpha_0)}\tag{6.167}$$
- At $n=0$ it reduces to (6.166), since then $\alpha_0=\alpha_{00}$. Moments and percentiles are also entire in $n$, so limits can replace $(0/0)$ or $(\infty/\infty)$ forms, giving the same results as repeating the calculation (p. 194).
- Moments for $\alpha_1<\infty$:
$$\langle\alpha^m\rangle=\frac{n-1}{\alpha_0^{1-n}-\alpha_1^{1-n}}\int_{\alpha_0}^{\alpha_1}d\alpha\,\alpha^{m-n}=\frac{n-1}{n-m-1}\frac{\alpha_0^{1+m-n}-\alpha_1^{1+m-n}}{\alpha_0^{1-n}-\alpha_1^{1-n}}\tag{6.168}$$
and, taking limits as in (6.167),
$$\langle\alpha^m\rangle=\begin{cases}\dfrac{\alpha_1^m-\alpha_0^m}{m\log(\alpha_1/\alpha_0)}&n=1\\[2mm]\dfrac{(n-1)\log(\alpha_1/\alpha_0)}{\alpha_0^{1-n}-\alpha_1^{1-n}}&m=n-1\end{cases}\tag{6.169}$$
- Footnote 17: any expression analytic in a parameter can be exploited by treating the number (e.g. 2 or $\pi$) as a variable, differentiating, then setting it back (p. 194).
- Exercises 6.8 and 6.9 ask for explicit estimates and accuracies, and for what survives as $\alpha_1\to\infty$ (p. 194).

*Intuition note.* The formula for general $n$ is a smooth function of $n$, so the odd small cases ($n=1$, $n=0$) need no special treatment: a limit gives them. The posterior is always confined to $[\alpha_0,\alpha_1]$.

### 6.23 Comments (pp. 195–197)
- Jaynes (author's view): Mr B's results (6.129), (6.152) need prior and posterior probabilities and integration over a nuisance parameter. He writes that it appears to him that they are beyond the reach of orthodox methods (p. 195).
- **Bertrand (1889)**, quoted (p. 195): St Malo's tides and deaths, and northwest winds and shipwrecks, have identical data patterns. We would accept the wind's influence as certain, but common sense demands more evidence before even considering the tide plausible. Bertrand concludes the prior probability of the cause must be taken into account.
- **Fisher's maxim** (reported, criticised by Jaynes): "Let the data speak for themselves!" Jaynes says the data cannot, and never have in any real inference problem (p. 195).
- Maximum likelihood alone leads to the "sure thing" hypothesis $H_S$, under which every detail of the data was inevitable. It has $p(D|H_S)=1$, the highest likelihood. Only its very low prior justifies rejecting it (p. 195; footnote 18, children's explanations).
- Specifying a model only fixes the parameter space. Without a prior over it, one cannot include information on likely parameter values (p. 196).
- Jaynes thinks Fisher managed because his problems had little important prior information and plenty of data. He believes Fisher's ideology would have changed had he faced cogent prior information and sparse data (p. 196).
- Gould's Aysheaia example (p. 196): two paleontologists classified the same fossil oppositely. Jaynes uses it against Fisher's maxim: the reversal reflects different presuppositions, since the data had not changed.
- Mechanism (p. 196): only prior information says whether a hypothesis is a possible physical mechanism. A hypothesis of invisible elves has the same likelihood as a real one but no credence.
- Jaynes (p. 197): accumulated prior information gives the mature person the stability to reject fantasies. Today's disputes over causal effects (policy, courts) are hampered because orthodox testimony has no place for prior information. Jaynes notes that Bertrand's insight appeared the year before Fisher was born, and that progress has not always been forward. The chapter "begins and ends with a glance back at Fisher" (p. 197).

## Toy example (ours, not from the text)
Take $\phi=0.5$, $c_1=2$, $c_2=4$, and use the book's formulas.
- **Mr A**: mode $c_1/\phi=2/0.5=4$. Mean $(c_1+1-\phi)/\phi=2.5/0.5=5$. Variance $(c_1+1)(1-\phi)/\phi^2=3\times0.5/0.25=6$, s.d. $\approx2.45$.
- **Mr B** (6.132): mode $=\frac{c_1+c_2}{2\phi}+\frac{c_1-c_2}2=\frac{6}{1}-1=5$. Check (6.131): $\frac{5+4}{5-2}\cdot\frac{0.5}{1.5}=3\times\frac13=1$. (The text's convention of setting the neighbour ratio to 1 means $p(5)=p(4)$ here.)
- B's mean (6.133): $\frac{2+4+1-0.5}{1}+\frac{2-4}{2}=6.5-1=5.5$. Variance (6.141): $\frac{7\times(1-0.25)}{4\times0.25}=\frac{5.25}{1}=5.25$, s.d. $\approx2.29$.

B's mode moves from 4 to 5, toward $c_2/\phi=8$, and his s.d. falls from 2.45 to 2.29. A cannot move, because for him $c_2$ is irrelevant to $n_1$.

## Concepts
- [[bayes-theorem]] — posterior ∝ prior × likelihood, applied here to $n_1$, $s$ and $\alpha$ (p. 178)
- [[prior-distribution]] — a description of the robot's own state of knowledge, not an "objectively true" probability (p. 178)
- [[likelihood]] — $p(c_1|\phi n_1)$ has its maximum at $c_1/\phi$ and falls off for larger $n_1$; a prior can make a large difference only by modulating it near the peak, not its tails (pp. 179, 178 fn. 11)
- [[posterior-distribution]] — the full answer; summarized by mode, mean and s.d. (pp. 180–187)
- [[jeffreys-prior]] (new) — $p(s)\propto1/s$, uniform in $\log s$; expresses complete ignorance of a scale parameter, per Jaynes (pp. 181–182)
- [[improper-prior]] (new) — a prior that cannot be normalized, can be used directly when the integrals converge; in almost all cases it can be approached as a limit of proper priors (p. 182)
- [[nuisance-parameter-marginalization]] (new) — integrating out $s$ with a prior, as in (6.117), (6.128), (6.145) (pp. 181, 184, 188, 195)
- [[qualitative-prior-information]] (new) — non-numerical knowledge (e.g. a fixed source) that changes which variables are relevant to each other (pp. 177, 187)
- [[chebyshev-inequality]] (new) — $P\ge1-1/t^2$ for $\langle n\rangle\pm t\sigma$, for any distribution with finite variance (p. 186)
- [[asymptotic-normality-of-posterior]] (new) — a single-peaked posterior becomes Gaussian as data accumulate (p. 189)
- [[sure-thing-hypothesis]] (new) — $H_S$ with $p(D|H_S)=1$, the maximum-likelihood hypothesis, rejected only through its prior (p. 195)
- [[frequentist-vs-bayesian]] — here "orthodox" statistics is criticised for lacking priors and nuisance integration (pp. 192, 195–196)
- [[bayesian-occams-razor]] (loose link) — low prior credence, not likelihood, rejects $H_S$ (p. 195)

## Canonical instances
- [[particle-counter-two-robots]] — Mr A vs Mr B with counter efficiency $\phi=0.1$ and counts 10, 16 (pp. 177–190)
- [[taxicab-problem]] — estimating the number of cabs from number 27; rectangular sampling distribution (pp. 190–194)
- [[st-malo-tides-and-shipwrecks]] — Bertrand's identical-data, different-prior example (p. 195)
- [[aysheaia-fossil]] — Gould's example of differing prior presuppositions (p. 196)

## Bridges (candidates)
- [structural-analogy] Fig. 6.2(b), a common source $s$ pointing to every $n_i$ ↔ bayesian: causal DAG fork, where conditioning on the common cause blocks the link between the others
- [structural-analogy] B's use of other intervals to estimate $s$, which then sharpens each $n_k$ ↔ bayesian: partial pooling in hierarchical models
- [structural-analogy] B's posterior as a product of two routes' distributions (6.136) ↔ information-theory: combining independent evidence by adding log-likelihoods (bits)
- [metaphor] $H_S$ with likelihood 1 ↔ information-theory: a model that memorizes the data (overfitting) and is penalised by description length (MDL)
- [structural-analogy] Posterior becoming Gaussian with width about $1/\sqrt c$ ↔ information-theory: Fisher information as local curvature of log-likelihood

## Questions this raises
- What exactly is the "exact relationship" between the discrete taxicab problem and the continuous rectangular one, and which estimate replaces the intuitive $2\times27$?
- How, in Chapter 12, do transformation groups derive $1/s$ for a scale parameter, and when is $s$ truly one?
- How should B detect that $I_B$ (a fixed source) is wrong, for example when $c_2=80$? What formal test does the "something else" hypothesis need?
- How do the results change when the dead-time effect of Exercise 6.5 is included?

## Exercises worth doing
- Ex. 6.5 (p. 177) — include dead-time effects in the estimate of $n$ — difficulty: hard
- Ex. 6.6 (p. 180) — show how little the prior cutoff $N$ matters (tail ratio $\delta$) — difficulty: medium
- Ex. 6.7 (p. 190) — translate the conclusions to a disease-incidence setting, including when the model fits — difficulty: medium
- Ex. 6.8 (p. 194) — explicit estimates and accuracies for the rectangular problem; compare with common sense — difficulty: medium
- Ex. 6.9 (p. 194) — which posterior summaries survive as $\alpha_1\to\infty$ for small $n$ — difficulty: medium

## Reading notes
- This is part 2 of Chapter 6. It starts with the end of the preceding section (presumably §6.11, since §6.12 follows) and Exercise 6.5 (p. 177), then covers §§6.12–6.23, and ends at the close of §6.23 (p. 197). Printed = pdf − 30.
- Eqs. (6.84), (6.86), (6.89), (6.90), (6.93), (6.100) come from the earlier part and are only cited here. I took $p(c_1|\phi n_1)$ to be binomial from (6.112) and (6.109).
- (6.117)–(6.118) print $\theta$ where $\phi$ appears intended; in (6.122) the printed "$c/\phi$" appears to mean $c_1/\phi$; in (6.169) the printed "$a_1^{1-n}$" appears to mean $\alpha_1^{1-n}$.
- In (6.144), $\sqrt{17\times1.1}/0.1\approx43.2$ by my arithmetic; the page prints 43.3.
- Section 6.21 states the book's own claim that Bayesian analysis has no pathological cases. That is Jaynes's claim, supported by the author's reported experimentation with many cases (fn. 16), not by a proof on these pages.
