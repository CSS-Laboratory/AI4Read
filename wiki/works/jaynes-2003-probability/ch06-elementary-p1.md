---
id: jaynes-2003-probability/ch06-elementary-p1
work: jaynes-2003-probability
unit: "Chapter 6 — Elementary parameter estimation (part 1/2: intro, §§6.1–6.11, up to Eq. 6.102)"
pages: 149–176
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Elementary parameter estimation (part 1/2)

## L0 — One line
Probability theory as logic gives point and interval estimates from one posterior, and the conclusions (Laplace's rule, futile sampling under a binomial prior, Bayes vs maximum likelihood) can depend, often surprisingly, on the prior information (though different priors need not give different conclusions).

## L1 — The gist (≤ 120 words)
Question: what should a reasoning robot infer about unknown urn contents, or a continuous parameter, once data are seen? Answer: Bayes' theorem gives point and interval estimates from one posterior. A uniform prior gives Laplace's rule of succession, (r+1)/(n+2). Other priors give surprising but explicable results: a binomial "monkey" prior makes sampled balls uninformative about unsampled ones. Whether n was fixed in advance does not change inference about θ. The mean and median minimize squared and absolute error; the mode is a third estimator. In a particle-counter example, the Bayesian mean estimate (105 particles) differs sharply from maximum likelihood (150) because prior information about the source is used.

**Prerequisites:** Bayes' theorem, sum and product rules; binomial and hypergeometric distributions; binomial coefficient identities; mean, variance and median; limits of sequences and sums.

## L2 — Key ideas
- Point and interval estimation come from one calculation, and, when hypotheses are very numerous and indexed, deciding between them and estimating the index are practically the same task (p. 149).
- Urn inversion with a uniform prior on R gives an exact posterior (6.17). It reproduces deductive logic in extreme cases and gives Laplace's rule of succession, (r+1)/(n+2), independent of N (pp. 153–155).
- The data tell us nothing about N beyond N ≥ n exactly when p(D|NI) is independent of N for N ≥ n. This is a condition on p(R|NI), and many reasonable priors satisfy it (pp. 151–152).
- Different priors need not give different conclusions. A truncated uniform prior changes nothing when 0 < r < n; for the concave prior (proportional to 1/[R(N−R)], emphasizing extreme values of R), Exercise 6.2 states that for 1 ≤ r ≤ n−1 the posterior mean fractions equal r/n, but this is posed as an exercise and not derived in the text (pp. 157–160).
- The binomial "monkey" prior has logical independence between balls, so sampling teaches nothing about the unsampled balls (pp. 161–162).
- Optional stopping: if n, r or any function of the data is already in the prior information, it is redundant and cannot change conclusions. Inference depends on the observed data set, not on unobserved ones (pp. 166–167).
- Posterior mean (squared error), median (absolute error) and mode (equal to the maximum likelihood estimate, MLE, under a flat prior) are different estimators. The median and percentiles are invariant under monotonic reparametrization; the mean is not (pp. 172–175).
- In the counter example, the posterior mean ⟨n⟩ = c + s(1−φ) differs from the MLE c/φ because the source strength s is prior information. A low-efficiency counter cannot track fluctuations in particle arrival (pp. 171, 175–176).

## L3 — Walkthrough

### Introduction (p. 149)
Fisher called the split between "point" and "interval" estimation a distinction without a difference. Jaynes agrees: probability as logic gives both from one calculation (p. 149). He also treats hypothesis testing and parameter estimation as not truly different (p. 149).

With very many discrete hypotheses $H_t$, deciding among them and estimating the index $t$ are practically the same thing. Regarding the index as the quantity of interest is parameter estimation (p. 149).

### 6.1 Inversion of the urn distributions (pp. 149–150)
Chapter 3 treated the "pre-data" problem: $N$, $R$ known, predict the sample. Now the data $D\equiv(n,r)$ are known and $(N,R)$ are not (pp. 149–150). The sampling distribution is the hypergeometric (Eq. 3.22); $I$ is the general statement of the problem:

$$p(D|NRI)=h(r|NR,n)=\binom{N}{n}^{-1}\binom{R}{r}\binom{N-R}{n-r}.\tag{6.1}$$

### 6.2 Both N and R unknown (pp. 150–152)
We know deductively that $N\ge n$. **Intuition (naive):** the data can say nothing more about $N$. Jaynes says this uses a hidden assumption (p. 150).

Joint posterior, with the prior factored by the product rule:

$$p(NR|DI)=p(N|I)\,p(R|NI)\,\frac{p(D|NRI)}{p(D|I)},\tag{6.2}$$

$$p(D|I)=\sum_{N=0}^{\infty}\sum_{R=0}^{N}p(N|I)\,p(R|NI)\,p(D|NRI).\tag{6.3}$$

$p(D|NRI)=0$ when $N<n$, $R<r$ or $N-R<n-r$ (p. 150). Marginal for $N$, and the direct Bayes form (the two must agree by the sum and product rules):

$$p(N|DI)=\sum_{R=0}^{N}p(NR|DI)=p(N|I)\frac{\sum_R p(R|NI)p(D|NRI)}{p(D|I)},\tag{6.4}$$
$$p(N|DI)=p(N|I)\frac{p(D|NI)}{p(D|I)}.\tag{6.5}$$

**Naive expectation:** the data only truncate impossible values and leave the relative probabilities of the rest unchanged (p. 151):

$$p(N|DI)=\begin{cases}A\,p(N|I)&N\ge n\\0&0\le N<n.\end{cases}\tag{6.6}$$

This is exactly right if the data tell only that $Z\equiv N\ge n$ (6.7): then $p(Z|NI)=1$ for $n\le N$, else $0$ (6.8), and Bayes gives (6.6) with $A=1/p(Z|I)$ (6.9) (p. 151). Laplace considered this result (learning only $N\ge n$ leaves the relative probabilities unchanged) intuitively obvious and took it as a basic principle of his theory (p. 151).

By (6.5), however, (6.6) holds only if $p(D|NI)$ is independent of $N$ for $N\ge n$. It can fail when the prior links $N$ and $R$. Example: if one knows $R<0.06N$, then data $(n,r)=(10,6)$ imply $N>100$ (p. 151). Usually there is no such link, so estimating $N$ is uninteresting (p. 151).

The general condition is nontrivial and falls on $p(R|NI)$:

$$p(D|NI)=\sum_{R=0}^{N}p(D|NRI)\,p(R|NI)=\begin{cases}f(n,r)&N\ge n\\0&N<n,\end{cases}\tag{6.10}$$

with $f$ independent of $N$. With (6.1) this is

$$\sum_{R=0}^{N}\binom{R}{r}\binom{N-R}{n-r}p(R|NI)=f(n,r)\binom{N}{n},\qquad(N\ge n).\tag{6.11}$$

Jaynes calls (6.11) a "discrete integral equation". It is the necessary and sufficient condition for the data to be uninformative about $N$. The left side is automatically 0 for $N<n$, so the only constraint is that $f$ be independent of $N$ for $N\ge n$ (p. 152). Footnote 1: later, very general conditions of "uninformativeness" take a similar integral-equation form (p. 152).

Most "reasonable" priors satisfy (6.11), so the main concern is $p(R|NDI)$ in the factorization

$$p(NR|DI)=p(N|DI)\,p(R|NDI),\tag{6.12}$$
$$p(R|DNI)=p(R|NI)\frac{p(D|NRI)}{p(D|NI)}.\tag{6.13}$$

*Intuition note:* "The data only rule out values" is a hidden assumption about how $R$ and $N$ are linked in the prior. It holds when the prior makes the likelihood of the data the same for all $N\ge n$.

### 6.3 Uniform prior (pp. 152–155)
Prior $I_0$, seemingly as ignorant about $R$ as possible:

$$p(R|NI_0)=\frac1{N+1},\quad 0\le R\le N.\tag{6.14}$$

Terms cancel in (6.13):

$$p(R|DNI_0)=S^{-1}\binom{R}{r}\binom{N-R}{n-r},\tag{6.15}$$

$$S\equiv\sum_{R=0}^{N}\binom{R}{r}\binom{N-R}{n-r}=\binom{N+1}{n+1},\tag{6.16}$$

$$p(R|DNI_0)=\binom{N+1}{n+1}^{-1}\binom{R}{r}\binom{N-R}{n-r}.\tag{6.17}$$

This is not hypergeometric, because the variable is $R$, not $r$ (p. 153). Using (6.16),

$$\sum_{R=0}^{N}\frac1{N+1}\binom{R}{r}\binom{N-R}{n-r}=\frac1{N+1}\binom{N+1}{n+1}=\frac1{n+1}\binom{N}{n},\tag{6.18}$$

so (6.11) holds, and with this prior the data tell nothing about $N$ beyond $N\ge n$ (p. 153).

Checks (p. 153):
- (6.17) vanishes for $R<r$ or $R>N-n+r$, as deduction requires.
- For $n=N$ it reduces to $\delta(R,r)$.
- For $n=r=0$ it returns the prior $1/(N+1)$.
- For $n=r=1$: $p(R|DNI_0)=\dfrac{2R}{N(N+1)}$ (6.19). This is proportional to $R$ because the sampling probability is $R/N$ and the prior is flat.

The coefficient in (6.19) incidentally derives $\sum_{R=0}^{N}R=N(N+1)/2$ (6.20). Jaynes remarks that such results show probability as extended logic is an exact mathematical system. Footnote 2 contrasts orthodox ad hoc devices, which give nonsense in some extreme case (Chapter 17) (pp. 153–154).

**Point estimates.** Setting $p(R')=p(R'-1)$ gives the most probable value (within one unit; if $R'$ is not an integer, take the next integer below):

$$R'=(N+1)\frac rn.\tag{6.21}$$

Mean of the posterior:

$$\langle R\rangle=E(R|DNI_0)=\sum_{R=0}^{N}R\,p(R|DNI_0).\tag{6.22}$$

Use $(R+1)\binom Rr=(r+1)\binom{R+1}{r+1}$ (6.23) and (6.16) again:

$$\langle R\rangle+1=(r+1)\binom{N+1}{n+1}^{-1}\binom{N+2}{n+2}=\frac{(N+2)(r+1)}{n+2}.\tag{6.24}$$

For large $(n,r,N)$ this is close to the mode, which suggests a sharply peaked or symmetric posterior (p. 154). Expected fraction of red left in the urn:

$$\langle F\rangle=\frac{\langle R\rangle-r}{N-n}=\frac{r+1}{n+2}.\tag{6.25}$$

(Added step: $\langle R\rangle-r=\frac{(N+2)(r+1)}{n+2}-(r+1)=\frac{(r+1)(N-n)}{n+2}$.)

### 6.4 Predictive distributions (pp. 154–156)
Let $R_i\equiv$ red on the $i$th draw (6.26). Marginalizing over $R$:

$$p(R_{n+1}|DNI_0)=\sum_R p(R_{n+1}|RDNI_0)\,p(R|DNI_0)=\sum_{R=0}^{N}\frac{R-r}{N-n}\binom{N+1}{n+1}^{-1}\binom Rr\binom{N-R}{n-r},\tag{6.27–6.28}$$

and with (6.16), "after some algebra",

$$p(R_{n+1}|DNI_0)=\frac{r+1}{n+2},\tag{6.29}$$

equal to (6.25). This is **Laplace's rule of succession**. Jaynes's comment: a probability is not a frequency, but under quite general conditions the predictive probability of a single-trial event is numerically equal to the expectation of its frequency in some specified class of trials (p. 155).

History as given: Laplace first obtained the rule from a mixture of binomials (see (6.73)). The urn derivation dates from at least 1799 (Zabell 1989), was rediscovered in 1918 by C. D. Broad, and was emphasised by Wrinch and Jeffreys, W. E. Johnson and H. Jeffreys. Independence from $N$ was initially a surprise. Chapter 18 returns to the controversy (p. 155).

**Accuracy.** Extending (6.23): $(R+1)(R+2)\binom Rr=(r+1)(r+2)\binom{R+2}{r+2}$ (6.30). Summing,

$$\langle(R+1)(R+2)\rangle=(r+1)(r+2)\binom{N+1}{n+1}^{-1}\binom{N+3}{n+3}=\frac{(r+1)(r+2)(N+2)(N+3)}{(n+2)(n+3)}.\tag{6.31}$$

Using $\mathrm{var}(R)=\langle(R+1)^2\rangle-\langle R+1\rangle^2$ and $p=\langle F\rangle=(r+1)/(n+2)$ (pp. 155–156):

$$\mathrm{var}(R)=\frac{p(1-p)}{n+3}(N+2)(N-n),\tag{6.32}$$

$$(R)_{\rm est}=r+(N-n)p\pm\sqrt{\frac{p(1-p)}{n+3}(N+2)(N-n)}.\tag{6.33}$$

For $n=N$ this gives $r\pm0$, as deduction requires. For the fraction remaining:

$$(F)_{\rm est}=\frac{(R-r)_{\rm est}}{N-n}=p\pm\sqrt{\frac{p(1-p)}{n+3}\frac{N+2}{N-n}},\quad 0\le n<N,\tag{6.34}$$

which gets less accurate as a larger part of the urn is sampled. For $N\to\infty$:

$$(F)_{\rm est}=p\pm\sqrt{\frac{p(1-p)}{n+3}},\tag{6.35}$$

the binomial-type result (p. 156).

**Poll check (p. 156).** A news report: random poll of 1600 voters, 41% favour a candidate, margin ±3%. Requiring $(F)_{\rm est}=\langle F\rangle(1\pm0.03)$ in (6.35):

$$n+3=\frac{1-p}{p}\frac1{(0.03)^2}=\frac{1-0.41}{0.41}\times1111=1598.9,\tag{6.36}$$

so $n\simeq1596$. Jaynes suggests the pollsters are using this theory, or at least giving it implied lip service.

*Intuition note:* With the uniform prior, the predictive probability is not $r/n$ but $(r+1)/(n+2)$. This can be read as a weighted average of $r/n$ (weight $n$) and the prior mean $1/2$ (weight 2), so the prior seems to carry the weight of two observations; Jaynes calls this only a line of free association, not a derivation (p. 158). The same posterior gives both the estimate and its ± error.

### 6.5 Truncated uniform priors (pp. 157–158)
Prior $I_1$: it is known that $0<R<N$ (at least one red and one white ball):

$$p(R|NI_1)=\frac1{N-1},\quad 1\le R\le N-1,\ \text{else }0.\tag{6.37}$$

The sums (6.16) lose the $R=0$ and $R=N$ terms. Since $\binom Rr=\binom{R+1}{r+1}=\delta(r,0)$ at $R=0$ (6.38) and $\binom{N-R}{n-r}=\delta(r,n)$ at $R=N$ (6.39):

$$S=\sum_{R=1}^{N-1}\binom Rr\binom{N-R}{n-r}=\binom{N+1}{n+1}-\binom Nn\delta(r,n)-\binom Nn\delta(r,0),\tag{6.40}$$
$$\sum_{R=1}^{N-1}\binom{R+1}{r+1}\binom{N-R}{n-r}=\binom{N+2}{n+2}-\binom{N+1}{n+1}\delta(r,n)-\binom Nn\delta(r,0).\tag{6.41}$$

If $0<r<n$ the new terms vanish and

$$p(R|DNI_1)=p(R|DNI_0),\quad 0<r<n.\tag{6.42}$$

Jaynes explains: a pure sampling-distribution theory would see a changed sample space. But here the data already tell us by deduction that $R\neq0,N$, so whether the prior also says it cannot matter. Our state of knowledge about $R$ is the same (p. 157).

If $r=0$, $S=\binom{N+1}{n+1}-\binom Nn$ (6.43) and

$$p(R|r=0,NI_1)=\binom N{n+1}^{-1}\binom{N-R}{n},\quad 1\le R\le N-1,\tag{6.44}$$

zero elsewhere. The ratio to the $I_0$ posterior is

$$\frac{p(R|r=0,NI_1)}{p(R|r=0,NI_0)}=\frac{N+1}{N-n},\quad 1\le R\le N-1,\tag{6.45}$$

independent of $R$. Reason: $r=0$ gives no evidence against $R=0$ and some for it. Under $I_0$, $R=0$ is the most probable value; $I_1$ excludes it and compresses the posterior into a smaller range. Different priors do not necessarily lead to different conclusions; it can depend on which data we get (p. 158).

*Intuition note:* A prior restriction matters only if the data have not already enforced it. When the data are compatible with the extra restriction in a way that makes it automatic, the posterior is unchanged. Exercise 6.1 is set here (see Exercises).

### 6.6 A concave prior (pp. 158–160)
Laplace's rule can be written as a weighted average (6.46) (pp. 158–159):

$$\frac{r+1}{n+2}=\frac{n(r/n)+2(1/2)}{n+2}.$$

Jaynes says the uniform prior seems to carry the weight of two observations. He labels the following a "line of free association", not a derivation (p. 158). Could the uniform prior be a posterior after $(n,r)=(2,1)$ from a more primitive "pre-prior" $I_{00}$? Bayes backwards would need

$$p(R|DI_{00})=p(R|I_{00})\frac{p(D|RI_{00})}{p(D|I_{00})}=\text{const.},\quad0\le R\le N.\tag{6.47}$$

Here $p(D|RI_{00})=p(D|RI_0)$ is hypergeometric. For $n=2,r=1$:

$$h(r=1|N,R,n=2)=\frac{R(N-R)}{N(N-1)}.\tag{6.48}$$

This vanishes at $R=0,N$, so no pre-prior gives a constant posterior over the whole range. But the data $(2,1)$ guarantee at least one red and one white, so the truncated prior (6.37) is a valid target. Consider the prior emphasising extremes:

$$p(R|I_{00})\equiv\frac{A}{R(N-R)},\quad1\le R\le N-1.\tag{6.49}$$

For data with $1\le r\le n-1$,

$$p(R|DNI_{00})=\frac{A}{R(N-R)}\binom Rr\binom{N-R}{n-r}=\frac{A}{r(n-r)}\binom{R-1}{r-1}\binom{N-R-1}{n-r-1}.\tag{6.50}$$

From (6.16),

$$\sum_{r=1}^{N-1}\binom{R-1}{r-1}\binom{N-R-1}{n-r-1}=\binom{N-1}{n-1},\tag{6.51}$$

so

$$p(R|DNI_{00})=\binom{N-1}{n-1}^{-1}\binom{R-1}{r-1}\binom{N-R-1}{n-r-1},\quad1\le R\le N-1,\ 1\le r\le n-1.\tag{6.52}$$

Check: for $n=2,r=1$ this is $p(R|NI_1)=\frac1{N-1}$, $1\le R\le N-1$ (6.53) (p. 159).

Jaynes leaves the analogue of (6.22)–(6.35) to the reader (Exercises 6.2, 6.3). He states that the concave prior gives simpler results than the uniform one, but also near-instabilities that grow with $N$. As $N\to\infty$ it approaches an improper (non-normalizable) prior. That must give absurd answers to some questions, though still reasonable ones when the data remove the singularity (p. 160).

### 6.7 The binomial monkey prior (pp. 160–162)
Prior $I_2$: monkeys filled the urn, each ball independently red with probability $g$:

$$p(R|NI_2)=\binom NR g^R(1-g)^{N-R},\quad0\le R\le N,\tag{6.55}$$

prior estimate $(R)_{\rm est}=Ng\pm\sqrt{Ng(1-g)}$ (6.56). The sum (6.10) gives

$$p(D|NI)=\binom nr g^r(1-g)^{n-r},\quad N\ge n,\tag{6.57}$$

independent of $N$, so (6.11) holds and $p(NR|DI_2)=p(N|DI_2)p(R|NDI_2)$ (6.58). Jaynes also sets up the other factorization $p(NR|DI_2)=p(R|DI_2)p(N|RDI_2)$ (6.59). He invites the reader to guess intuitively how $p(R|DNI)$ and $p(R|DI)$ differ (p. 161).

Posterior for $R$ given $N$:

$$p(R|DNI_2)=A\binom NR g^R(1-g)^{N-R}\binom Rr\binom{N-R}{n-r}.\tag{6.60}$$

Use the rearrangement

$$\binom NR\binom Rr\binom{N-R}{n-r}=\binom Nn\binom nr\binom{N-n}{R-r}\tag{6.61}$$

to normalize:

$$1=\sum_R p=A\binom Nn\binom nr\sum_R\binom{N-n}{R-r}g^R(1-g)^{N-R}=A\binom Nn\binom nr g^r(1-g)^{n-r},\quad r\le R\le N-n+r.\tag{6.62}$$

Hence

$$p(R|DNI_2)=\binom{N-n}{R-r}g^{R-r}(1-g)^{N-R-n+r},\tag{6.63}$$

$$(R)_{\rm est}=r+(N-n)g\pm\sqrt{g(1-g)(N-n)},\tag{6.64}$$

$$\frac{(R-r)_{\rm est}}{N-n}=g\pm\sqrt{\frac{g(1-g)}{N-n}}.\tag{6.65}$$

Compared with (6.33)–(6.34), $g$ comes entirely from the prior, whereas $p$ came entirely from the data. (6.65) is exactly the prior estimate for any subset of $N-n$ balls with no data at all. So the binomial prior "nullifies" the data: if it correctly describes the prior information, sampling tells you practically nothing about the unsampled balls unless you sample practically the whole population (p. 162).

The binomial prior is more peaked, so its uncertainties in (6.64)–(6.65) are smaller than those of (6.33)–(6.34) by a factor $\sqrt{(n+3)/(N+2)}$. The striking point is dependence on data, not size of uncertainty. Even after sampling 99% of the balls we know no more about the other 1% (p. 162). Jaynes's explanation: the filling mechanism makes balls logically independent, $P(R_1R_2|I)=P(R_1|I)P(R_2|I)$, and this independence is preserved in the posterior (p. 162).

Exercise 6.4 asks for the condition that factorization is retained. Jaynes then asks whether the appearance of a binomial distribution already implies logical independence; he defers this to Part 2 (pp. 162–163).

*Intuition note:* If each ball is red independently of all others (given $g$), learning about some balls tells you nothing about others. A prior that builds in such independence therefore makes sampling useless for inferring the rest, even though one would expect a larger sample to help (Jaynes notes the result "will hardly commend itself to a survey sampler", p. 162).

### 6.8 Metamorphosis into continuous parameter estimation (p. 163)
If neighbouring hypotheses (nearby index values) are barely distinguishable by their observable consequences, no single hypothesis can be strongly favoured whatever the data. It then becomes natural to treat the index as a continuous parameter $\theta$ and give an estimate with its accuracy. Convention: Greek letters for continuous parameters, Latin for discrete indices or data (p. 163).

The process reverses: "$a<\theta<b$" is a compound hypothesis, so interval estimation is automatically compound hypothesis testing. Chapter 4 passed this way (Eqs. 4.67, 4.74). Orthodox statistics separates estimation and testing largely because it lacks a satisfactory way to treat compound hypotheses and prior information (Chapter 17) (p. 163).

### 6.9 Estimation with a binomial sampling distribution (pp. 163–166)
Bernoulli trials: each trial has two outcomes, arbitrarily "success"/"failure" (p. 164). Whether order is meaningful, known and relevant depends on the problem. Examples: ten coins tossed at once (order not meaningful); one coin tossed 100 times to judge honesty (order known but presumably irrelevant); recoveries after a new medicine (order crucial) (p. 164). Footnote 5: relevance is decided by the equations of probability theory, not intuition (p. 164).

Define $x_i=1$ for success, $0$ otherwise (6.66); $D=\{x_1,\dots,x_n\}$. Prior information $I$ gives each trial probability $\theta$, logically independent of other trials:

$$p(D|\theta I)=\prod_{i=1}^np(x_i|\theta I)=\theta^r(1-\theta)^{n-r}.\tag{6.67}$$

With any prior pdf,

$$p(\theta|DI)=\frac{p(\theta|I)p(D|\theta I)}{\int d\theta\,p(\theta|I)p(D|\theta I)}=A\,p(\theta|I)\theta^r(1-\theta)^{n-r}.\tag{6.68}$$

Uniform prior $p(\theta|I)=1$ on $0\le\theta\le1$ (6.69), with the Eulerian integral:

$$A^{-1}=\int_0^1d\theta\,\theta^r(1-\theta)^{n-r}=\frac{r!(n-r)!}{(n+1)!},\tag{6.70}$$
$$p(\theta|DI)=\frac{(n+1)!}{r!(n-r)!}\theta^r(1-\theta)^{n-r},\tag{6.71}$$

identical to Bayes' original result (Eq. 4.67). Moments:

$$\langle\theta^m\rangle=A\int_0^1d\theta\,\theta^{r+m}(1-\theta)^{n-r}=\frac{(n+1)!}{(n+m+1)!}\frac{(r+m)!}{r!}=\frac{(r+1)(r+2)\cdots(r+m)}{(n+2)(n+3)\cdots(n+m+1)}.\tag{6.72}$$

Predictive probability and (mean ± sd):

$$p\equiv\langle\theta\rangle=\int_0^1d\theta\,\theta\,p(\theta|DI)=\frac{r+1}{n+2},\tag{6.73}$$
$$(\theta)_{\rm est}=\langle\theta\rangle\pm\sqrt{\langle\theta^2\rangle-\langle\theta\rangle^2}=p\pm\sqrt{\frac{p(1-p)}{n+3}}.\tag{6.74}$$

(6.73) is Laplace's rule in its original derivation. The continuous results must follow from the discrete (6.29), (6.35) by $N\to\infty$; since those are independent of $N$, the limit has no effect (p. 165).

**Concave prior in the limit.** It becomes an improper prior,

$$\frac{A}{R(N-R)}\to\frac{d\theta}{\theta(1-\theta)}.\tag{6.75}$$

Some sums or integrals diverge, so the correct method is the limit of a ratio $\langle f(R/N)\rangle=\text{Num}/\text{Den}$ (pp. 165–166):

$$\text{Num}\equiv\sum_{R=1}^{N-1}\frac{f(R/N)}{R(N-R)}p(D|NRI),\qquad\text{Den}\equiv\sum_{R=1}^{N-1}\frac1{R(N-R)}p(D|NRI).\tag{6.76}$$

Under very general conditions this limit is well behaved. The improper prior was advocated by Haldane (1932) and Jeffreys (1939) "before the marginalization paradox". Jaynes says that "we" (the users of the method, himself included) were almost always lucky that the integrals converged, so we used them directly (ratio of limits, not limit of ratio) and still got the right answers (p. 166).

### 6.9.1 Digression on optional stopping (pp. 166–167)
Should it matter whether $n$ was fixed in advance, or we sampled until $r$ successes or until a given log-odds $u=\log[r/(n-r)]$? One could write $p(D|n\theta I)$, $p(D|r\theta I)$ or $p(D|u\theta I)$ (p. 166).

Jaynes's argument: in Boolean algebra $AA=A$, and probability as logic keeps this, because equal-truth-value propositions get equal probability (a basic desideratum). Redundant information is not counted twice. Since $p(n|n\theta I)=1$,

$$p(n\,r\ \text{order}|n\theta I)=p(r\ \text{order}|n\theta I)\,p(n|n\theta I)=p(r\ \text{order}|n\theta I),\tag{6.77}$$

so the likelihood function is the same. With

$$p(\theta n|DI)=p(\theta|nDI)p(n|DI)=p(n|\theta DI)p(\theta|DI),\tag{6.78}$$

and $p(n|\theta DI)=p(n|DI)=1$,

$$p(\theta|nDI)=p(\theta|DI).\tag{6.79}$$

The same holds for any quantity known from the data ($r$, $n-r$, $u$) (p. 167).

**Opposing view (Armitage 1960, as described by Jaynes):** statisticians who look only at sampling distributions claim the stopping rule does affect inference. Jaynes says they apparently believe parts of the sample space with false values of $r$ stay relevant after the true $r$ is known. He calls this a violation of $AA=A$. The same applies to any function $f(D)$ of the data. Inference must depend on the observed data set, not on data sets that might have been observed. Chapter 8 will show "irrational" and "spooky" consequences (p. 167).

Unobserved but real data are a major difficulty for orthodox statistics (the sampling distributions of estimators become wrong). For Jaynes they are a minor detail: they are relevant, and have a status somewhat like nuisance parameters (p. 167).

*Intuition note:* Once the data tell you $n$, the plan that produced $n$ adds no information about $\theta$, since the likelihood function is the same. What you could have seen but didn't carries no information beyond your prior information.

### 6.10 Compound estimation problems (p. 168)
Setting: two "binary games" in succession, and only the outcome of the last is observed; this resembles recovering censored data (p. 168). Scenarios:
- **(A)** Disease: frequency $p$ of contracting it, $\theta$ of dying from it; observed deaths $\{c_i\}$, infer unobserved incidence $\{n_i\}$.
- **(B)** Mosquitoes: $N$ bred per week, frequency $p$ of reaching campus, $\theta$ of being trapped; infer the numbers $n_i$ on campus and $N$.
- **(C)** Radioactive source: counts $\{c_i\}$ per second; infer the particles $n_i$ passing through the counter and the source strength.

The estimates are strongly affected by prior information (e.g. the process by which the disease is contracted). Jaynes will give a "best" estimate and an accuracy statement, using the radioactive-source language (p. 168).

### 6.11 A simple Bayesian estimate: quantitative prior information (pp. 168–171)
The counter efficiency $\phi$ is the probability that a particle makes a count, logically independent given $\phi$. If $\phi$ is unknown, successive counts are still causally independent but no longer logically independent, since other counts tell us about $\phi$ (pp. 168–169). Binomial for $n$ particles:

$$b(c|n,\phi)=\binom nc\phi^c(1-\phi)^{n-c},\quad0\le c\le n.\tag{6.80}$$

$\phi$ is, for now, "given by the teacher" (a bootstrap issue). $r$ here is the probability that a given nucleus sends a particle through the counter in one second (not the urn $r$). $N$ nuclei, $N$ constant (p. 169). Then

$$b(n|N,r)=\binom Nn r^n(1-r)^{N-n}.\tag{6.81}$$

**Poisson limit.** Let $N\to\infty$, $r\to0$, $Nr\to s$ constant, $r=s/N$ (p. 170):

$$\frac{N!}{(N-n)!}r^n=s^n\left(1-\tfrac1N\right)\left(1-\tfrac2N\right)\cdots\left(1-\tfrac{n-1}N\right)\to s^n,\tag{6.82}$$
$$(1-r)^{N-n}=\left(1-\tfrac sN\right)^{N-n}\to e^{-s},\tag{6.83}$$
$$p(n|Nr)\to p(n|s)=e^{-s}\frac{s^n}{n!}.\tag{6.84}$$

$s$ is the "source strength", the expected number of particles per second.

**Counts given only $s$.** Resolve $c$ into the alternatives $n$; $p(c|n\phi s)=p(c|\phi n)$ because, given $n$, $s$ is irrelevant (Fig. 6.1: chain $s\to n\to c$) (p. 170):

$$p(c|\phi s)=\sum_{n=0}^{\infty}p(cn|\phi s)=\sum_n p(c|n\phi s)p(n|\phi s)=\sum_np(c|\phi n)p(n|s).\tag{6.85}$$

Substituting (6.80) and (6.84), summing over $n\ge c$:

$$p(c|\phi s)=\sum_{n=c}^{\infty}\left[\frac{n!}{c!(n-c)!}\phi^c(1-\phi)^{n-c}\right]\left[\frac{e^{-s}s^n}{n!}\right]=\frac{e^{-s\phi}(s\phi)^c}{c!},\tag{6.86}$$

a Poisson distribution with

$$\langle c\rangle=\sum_{c=0}^{\infty}c\,p(c|\phi s)=s\phi.\tag{6.87}$$

**Inverse problem (Bayes).** In practice $c$ is known and $n$ unknown, e.g. when the counter is a "monitor" (p. 171):

$$p(n|\phi cs)=p(n|s)\frac{p(c|n\phi s)}{p(c|\phi s)}=\frac{p(n|s)\,p(c|n\phi)}{p(c|\phi s)}.\tag{6.88}$$

Substituting (6.80), (6.84)–(6.86):

$$p(n|\phi cs)=\frac{e^{-s(1-\phi)}[s(1-\phi)]^{n-c}}{(n-c)!}.\tag{6.89}$$

This is still Poisson, with parameter $s(1-\phi)$, shifted up by $c$ since $n\ge c$. Its mean is

$$\langle n\rangle=\sum_n n\,p(n|\phi cs)=c+s(1-\phi).\tag{6.90}$$

*Intuition note:* Of the $s$ particles expected, a fraction $1-\phi$ goes uncounted. Given $c$ counts, the unseen particles are Poisson with mean $s(1-\phi)$, regardless of $c$. The count adds only $c$ to that.

### 6.11.1 From posterior distribution function to estimate (pp. 172–176)
Choosing a "best" estimate $\alpha^*(D,I)$ is a decision-theory question (value judgments), beyond inference (Chapters 13–14); here only a preliminary discussion (p. 172). With error $e=\alpha^*-\alpha$:

- **Laplace (1774):** minimize expected $|e|$ ("most advantageous").
- **Gauss and Legendre:** minimize expected squared error; this prevailed for 150 years. Early works did not always distinguish expectation over the sampling pdf of $\alpha^*$ from expectation over the posterior pdf of $\alpha$. Jaynes says the former ignores prior information, and the latter is what we want (p. 172).

Expected squared error over the posterior:

$$\langle(\alpha-\alpha^*)^2\rangle=\langle\alpha^2\rangle-2\alpha^*\langle\alpha\rangle+\alpha^{*2}=(\alpha^*-\langle\alpha\rangle)^2+(\langle\alpha^2\rangle-\langle\alpha\rangle^2).\tag{6.91}$$

So the choice

$$\alpha^*=\langle\alpha\rangle=\int d\alpha\,\alpha\,p(\alpha|DI)\tag{6.92}$$

minimizes it, and the minimum is the variance of the posterior pdf,

$$\mathrm{var}(\alpha)\equiv\langle(\alpha-\langle\alpha\rangle)^2\rangle=\langle\alpha^2\rangle-\langle\alpha\rangle^2.\tag{6.93}$$

Jaynes notes that this is really the variance of the probability distribution the robot assigns, which the robot cannot reduce. The result holds for any posterior provided $\langle\alpha\rangle$ and $\langle\alpha^2\rangle$ exist (pp. 172–173). If the posterior is sharp and symmetric, it differs little from other reasonable estimates (p. 173).

**Objections to the mean (p. 173).**
- Squared error treats an error twice as great as four times as serious, so the mean focuses on very large but very improbable errors. It is sensitive to the tails (one rich man in a poor village).
- It is not consistent under reparametrization. For nonlinear $\lambda=\lambda(\alpha)$,

$$\lambda^*\equiv\langle\lambda\rangle=\int d\lambda\,\lambda\,p(\lambda|DI)=\int d\alpha\,\lambda(\alpha)p(\alpha|DI)\tag{6.94}$$

in general does not equal $\lambda(\alpha^*)$.

**Median.** Minimize $E\equiv\langle|\alpha^+-\alpha|\rangle$:

$$E=\int_{-\infty}^{\alpha^+}d\alpha\,(\alpha^+-\alpha)f(\alpha)+\int_{\alpha^+}^{\infty}d\alpha\,(\alpha-\alpha^+)f(\alpha),\tag{6.95}$$
$$\frac{dE}{d\alpha^+}=\int_{-\infty}^{\alpha^+}d\alpha\,f(\alpha)-\int_{\alpha^+}^{\infty}d\alpha\,f(\alpha)=0,\tag{6.96}$$

i.e. $P(\alpha>\alpha^+|DI)=1/2$: Laplace's estimator is the posterior median (p. 174). For a strictly monotonic increasing $\lambda(\alpha)$, $\lambda^+=\lambda(\alpha^+)$. Likewise every percentile is invariant: if

$$\int_{-\infty}^{\alpha_{35}}d\alpha\,f(\alpha)=0.35,\tag{6.97}$$

then

$$\lambda_{35}=\lambda(\alpha_{35}).\tag{6.98}$$

So median ± interquartile span has an invariant meaning, even when $\langle\alpha\rangle$ and $\langle\alpha^2\rangle$ diverge. An error twice as great counts only twice as serious, so the median is more "robust" against tail variations. It is unchanged by changes that move no probability across the median (p. 174).

Jaynes on robustness: it is often held desirable, and Bayesian methods are criticized as lacking it. But in the usual sense it "can always be achieved merely by throwing away cogent information" (p. 174). Footnote 8 anticipates that robustness matters only when the model is uncertain; a full Bayesian analysis over the candidate models then gives it automatically (p. 174). Before computers, percentiles were prohibitively hard to compute, so least squares prevailed; now we can have either (p. 175). Footnote 9: moments still have a theoretical significance percentiles lack (Chapter 7) (p. 175).

**Mode / MLE.** The peak of the posterior $\hat\alpha$ equals the maximum likelihood estimate $\alpha'$ if the prior is constant (or at least constant near the peak and not sufficiently greater elsewhere). Fisher coined "maximum likelihood" in the 1920s, while Laplace and Gauss used the method earlier as the "most probable value" (p. 175). Footnote 10: the MLE fails if the likelihood has a flat top; only prior information can resolve that (p. 175).

**Counter example: Bayes vs MLE (pp. 175–176).** **Orthodox statistician's view:** use maximum likelihood, with likelihood $p(c|\phi n)$ as a function of $n$. Setting the ratio to 1:

$$\frac{p(c|\phi n)}{p(c|\phi,n-1)}=\frac{n(1-\phi)}{n-c}=1,\tag{6.99}$$
$$(n)_{\rm MLE}=\frac c\phi.\tag{6.100}$$

(Added step: the ratio equals $\frac{n}{n-c}(1-\phi)$; setting it to 1 gives $n\phi=c$.)

Numbers: $\phi=0.1$, $s=100$, so $\langle c\rangle=s\phi=10$; observed $c=15$. The MLE is $150$. The robot's mean-square estimate is

$$\langle n\rangle=15+100(1-0.1)=15+90=105,\tag{6.101}$$

and in general (6.90) can be written

$$\langle n\rangle=s+(c-\langle c\rangle).\tag{6.102}$$

So $k$ extra counts are evidence for only $k$ extra particles, not $10k$ (p. 176).

Reconciliation (p. 176): with mean counts of 10, a fluctuation of about $\pm3$ ($\approx\sqrt{10}$) is unsurprising even for fixed $s$. With $s=100$, an unsurprising fluctuation is $\pm\sqrt{100}=\pm10$ particles, which corresponds to only $\pm1$ count. A low-efficiency counter cannot measure fluctuations in the arrival rate; at high efficiency practically every count corresponds to one particle. For the disease scenario: if the disease is mild and rarely fatal, or has a constant basic cause (e.g. contaminated water), changes in deaths are weak evidence of changes in incidence. If practically everyone who contracts it dies, deaths measure incidence reliably (p. 176). The difference arises because the Bayesian solution multiplies the likelihood by the prior $p(n|s)$ before maximizing, and the MLE uses only $p(c|\phi n)$ (p. 176). The page breaks mid-sentence here ("As we saw in the"); the part ends there.

*Intuition note:* The MLE asks "which $n$ makes 15 counts most likely?" and ignores that we already know about 100 particles arrive. The Bayesian estimate starts from the known 100 and moves only by the unexplained extra counts.

## Toy example (ours, not from the text)
Urn with $N=4$ balls; uniform prior on $R\in\{0,\dots,4\}$; draw $n=2$ and see $r=1$ red.

Unnormalized posterior weight $\binom R1\binom{4-R}{1}=R(4-R)$: $R=0:0$, $1:3$, $2:4$, $3:3$, $4:0$. Sum $=10=\binom{5}{3}$, matching (6.16). Posterior: $R=1,2,3$ with probabilities $0.3,0.4,0.3$.

Checks:
- Mean: $\langle R\rangle=1(0.3)+2(0.4)+3(0.3)=2$. Formula (6.24): $\langle R\rangle+1=\frac{(4+2)(1+1)}{2+2}=3$, so $\langle R\rangle=2$ ✓.
- Variance: $\langle R^2\rangle=0.3+1.6+2.7=4.6$, so $\mathrm{var}=4.6-4=0.6$. Formula (6.32), $p=\frac{2}{4}=0.5$: $\frac{0.25}{5}\cdot6\cdot2=0.6$ ✓.
- Predictive: $P(\text{next red}|R)=\frac{R-1}{2}$, so $0.3(0)+0.4(0.5)+0.3(1)=0.5=\frac{r+1}{n+2}$ ✓.

Contrast with a binomial prior with $g=\tfrac14$: weights $\binom4R g^R(1-g)^{4-R}R(4-R)\propto\binom4R R(4-R)3^{-R}$: $R=1:4$, $2:\tfrac{24}{9}$, $3:\tfrac{12}{27}$; total $\tfrac{64}{9}$. Posterior $=\tfrac{9}{16},\tfrac{6}{16},\tfrac{1}{16}$, which is $\text{Binomial}(2,\tfrac14)$ for $R-1$, as (6.63) says. Predictive probability of red next: $\tfrac{6}{16}\cdot\tfrac12+\tfrac1{16}\cdot1=\tfrac14=g$. The data (1 red in 2) do not move it from the prior value, whereas the uniform prior gave $0.5$.

## Concepts
- [[posterior-distribution]] — joint/marginal posteriors for $N$, $R$, $\theta$; from one posterior come point and interval estimates (pp. 149, 150, 165)
- [[bayes-theorem]] — used to invert urn sampling distributions and counter likelihoods (pp. 150, 171)
- [[prior-distribution]] — uniform, truncated, concave, binomial-monkey and Poisson priors; the choice drives conclusions (pp. 152–162, 170)
- [[likelihood]] — hypergeometric (6.1), binomial (6.67), $p(c|\phi n)$ as a function of $n$ (pp. 150, 164, 175)
- [[posterior-predictive-distribution]] — probability that the next draw is red (6.29, 6.73) (pp. 154–155, 165)
- [[laplace-rule-of-succession]] (new) — $(r+1)/(n+2)$ from a uniform prior; equals the posterior mean of the unsampled red fraction (p. 155)
- [[uninformative-about-N-condition]] (new) — (6.10)–(6.11): data only truncate $N<n$ iff $p(D|NI)$ is independent of $N$ for $N\ge n$ (pp. 151–152)
- [[logical-vs-causal-independence]] (new) — counts are causally independent always, but logically independent only if the parameter is known (p. 169; also pp. 162, 164)
- [[stopping-rule-irrelevance]] (new) — known-in-advance quantities are redundant ($AA=A$); inference depends on observed data only (pp. 166–167)
- [[posterior-mean-median-mode]] (new) — mean minimizes squared error; median minimizes absolute error and is reparametrization-invariant; mode equals the MLE under a flat prior (pp. 172–175)
- [[improper-prior]] (new) — $d\theta/[\theta(1-\theta)]$ as limit of the concave prior, handled as a limit of ratios (pp. 165–166)
- [[maximum-likelihood-estimate]] (new) — here, the likelihood maximizer $c/\phi$; ignores prior information (pp. 175–176)
- [[principle-of-indifference]] — the uniform prior (6.14) as the "seemingly as ignorant as possible" state (p. 152)

## Canonical instances
- [[urn-inversion]] — hypergeometric urn with unknown $(N,R)$; Laplace's rule (pp. 149–155)
- [[poll-margin-of-error]] — 1600 voters, 41%, ±3% matches $n+3\approx1599$ (p. 156)
- [[binomial-monkey-prior]] — a prior under which sampling tells nothing about unsampled balls (pp. 160–162)
- [[optional-stopping]] — stopping rules do not affect inference about $\theta$ (pp. 166–167)
- [[particle-counter-bayes-vs-mle]] — $\phi=0.1$, $s=100$, $c=15$: Bayes 105 vs MLE 150 (pp. 175–176)
- [[compound-binary-games]] — disease, mosquito, radioactive scenarios (p. 168)

## Bridges (candidates)
- [same-math] Uniform prior + binomial likelihood → posterior $\propto\theta^r(1-\theta)^{n-r}$ (6.71) ↔ bayesian: Beta–Binomial conjugate updating — same posterior form; the text does not use the Beta name.
- [structural-analogy] Rule of succession as weighted average of $r/n$ and prior mean $1/2$ with prior weight 2 (6.46) ↔ bayesian: partial pooling / shrinkage toward a prior mean.
- [structural-analogy] Chain $s\to n\to c$ with low efficiency $\phi$ (Fig. 6.1) ↔ information-theory: data processing through a noisy channel — outputs carry limited information about upstream fluctuations.
- [same-math] Posterior mean minimizes expected squared error (6.91–6.92); median minimizes expected absolute error (6.95–6.96) ↔ decision theory/statistics: squared and absolute loss — the same minimization.
- [metaphor] Optional-stopping irrelevance ↔ information-theory: only information in the data counts; unobserved sample points carry none.

## Questions this raises
- When exactly does a prior make sampling useless (binomial monkey prior), and does a binomial distribution always imply logical independence? (Jaynes defers this to Part 2, p. 163.)
- Exercise 6.4: under what condition on sampling distribution and data is logical independence of the balls retained in the posterior?
- How should the estimator be chosen when the loss function is not squared or absolute error (decision theory, Chapters 13–14)?
- How does the Bayesian counter solution change when $\phi$ and $s$ are themselves uncertain (the "bootstrap" issue, p. 169)?

## Exercises worth doing
- Ex. 6.1 (p. 158) — posterior and (mean ± sd) for $r=n$ under the truncated prior $I_1$; explain the difference from $I_0$, and predict in words the effect of "$3\le R\le N$" — difficulty: medium
- Ex. 6.2 (p. 160) — for the concave prior, show (6.11) holds, the mean fractions equal $f=r/n$ when $1\le r\le n-1$, and derive (6.54) — difficulty: hard
- Ex. 6.3 (p. 160) — concave prior with $r=0$ or $r=n$; estimate of red fraction after one non-red draw drops from 1/2 to about $1/\log N$ (vs 1/3 for uniform) — difficulty: hard
- Ex. 6.4 (p. 162) — necessary and sufficient condition for retaining the factorization $P(R_1R_2|DI)=P(R_1|DI)P(R_2|DI)$ — difficulty: hard
- Ex. 6.5 is referenced (footnote 7, p. 169, generalize to dead time) but is not among the exercises on these pages.

## Reading notes
- Printed pages 149–176 (pdf 179–206); printed = pdf − 30. The unit starts at the chapter opening (epigraph by Fisher) and ends at the bottom of p. 176, mid-sentence ("As we saw in the") in the Bayes-vs-MLE discussion after Eq. (6.102). The split is therefore not at a section end. The source notes say the split is at a section boundary, but the pages show the break inside §6.11.
- Footnotes 1–10 are all on these pages; footnotes 1, 2, 5, 8, 9 and 10 are used above in substance, footnote 7 only for the Exercise 6.5 pointer, and footnotes 3, 4 and 6 are not used.
- In (6.51) the image prints the summation index as $r=1$ to $N-1$, but the sum runs over $R$ (the constraints listed are $1\le R\le N-1$, $1\le r\le n-1$). I read it as a misprint.
- Symbols are reused: $r$ is the number of red balls drawn in §§6.1–6.7, but the nucleus-emission probability in §6.11. $p$ in (6.73) is the predictive probability, but in scenario (A) a frequency.
- Exercise 6.2(a)–(c) and Exercise 6.3 state results to be proved; I did not derive them. The comment that Ex. 6.5 appears later is from footnote 7 (p. 169).
- No OCR problems prevented reading equations; all were checked against the page images.
