---
id: jaynes-2003-probability/ch15-paradoxes
work: jaynes-2003-probability
unit: "15 Paradoxes of probability theory"
pages: 451-489
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 22
pipeline_version: 0.1
---
# Paradoxes of probability theory

## L0 — One line
Jaynes argues that the famous paradoxes of probability (nonconglomerability, Borel–Kolmogorov, marginalization) come mainly from using infinite sets, zero-measure conditions or improper priors as if the limit were already reached, and, in the tetrahedra and marginalization cases, from leaving prior information out of the notation.

## L1 — The gist (≤ 120 words)
Why do apparent contradictions arise in probability theory, and how are they removed? Jaynes's answer: strictly follow the sum and product rules of Chapter 2, do the arithmetic on finite sets first, and pass to the limit last. Then nonconglomerability vanishes (rectangular array, tumbling tetrahedra). Conditioning on a measure-zero event depends on the limiting process. In Jaynes's analysis, the marginalization paradox is two Bayesians solving two different problems, because they have different prior information. Only the Jeffreys prior dη/η lets the two agree for a scale parameter. The chapter shows how to use infinite sets safely, and argues that an improper prior has meaning only as a limit of proper priors.

**Prerequisites:** sum and product rules; Bayes' theorem; binomial distribution; matrix powers and Markov chains; change of variables with a Jacobian; improper priors; the gamma integral; the idea of a Hilbert space (only for §15.9.1).

## L2 — Key ideas
- **Limit last (Gauss).** Do ordinary arithmetic only on finite expressions, then see how the result behaves as n grows. The parlor-game series "proof" breaks this rule (p. 452), and Jaynes says most later paradoxes come from the same kind of error (pp. 453, 485).
- **Nonconglomerability is an artifact.** Nonconglomerability means that $P(A|I)$ lies outside the range of the conditional probabilities over a partition. On finite sets a weighted average cannot leave the range of its terms. The rectangular-array claim comes from counting directly on an infinite set. It throws away the ratio R = M/N that fixes P(A|I) (pp. 453–455).
- **Tumbling tetrahedra.** The problem is a reflected random walk with n and y(n) as sufficient statistics (the only parts of the record that matter). The exact finite-n answer is (15.26); for large n it is well approximated by p(A|yn) = (n−y)/(2(n−1)), in which the sampling probabilities 1/4, 3/4 cancel out (pp. 459–464).
- **"Finite additivity" is a red herring.** It is a euphemism for passing to the infinite limit first, which brings non-normalizable distributions (pp. 464–467).
- **Borel–Kolmogorov.** A density conditioned on a measure-zero event (y = 0) depends on which limiting sequence of positive-measure events is used (pp. 467–470).
- **Marginalization paradox.** In the Dawid–Stone–Zidek (DSZ) scenario, a Bayesian B₁ uses the full model and a lazy Bayesian B₂ uses a reduced model; in Jaynes's analysis they solve different problems because I₁ ≠ I₂ (their prior information differs). DSZ's proof that proper priors remove the disagreement uses contradictory assumptions. The separation property p(ζ|yz) = p(ζ|z) can hold, in the change-point example, only for improper priors (priors that cannot be normalized) η^{−k}, and agreement with B₂ then needs k = 1 (pp. 471–477).
- **Example #5 and ζ-overdetermination.** Even the existence of a nuisance parameter can be relevant prior information. Agreement of B₁ and B₂ means that one prior must solve a Fredholm integral equation (an integral equation for the unknown prior) for every data set (pp. 480–483).
- **Recipe for paradoxes.** Start from a well-defined finite situation, pass to a limit without specifying how, then ask a question whose answer depends on how. Jaynes concludes that, in probability theory, an infinite set should be treated only as the limit of a specified sequence of finite sets (pp. 485–487).

## L3 — Walkthrough

### Introduction (p. 451)
Jaynes defines "paradox" as something absurd or contradictory that looks like the result of sound reasoning (not Székely's "true but surprising"). Most paradoxes come from careless use of infinite and infinitesimal quantities. A paradox is, in Jaynes's usage, simply an error that has got out of control: it has trapped many minds and is taught as truth (p. 451).

### 15.1 How do paradoxes survive and grow? (pp. 451–452)
- A false proposition lets you deduce anything. Bad shortcut reasoning survives because it gives some correct results, and warnings (Poincaré, Weyl, and Jaynes's own past) are ignored (pp. 451–452).
- Removing a paradox requires, at the very least, three things: (1) show the result is absurd; (2) show the reasoning violates the Chapter 2 rules; (3) show the paradox disappears when the rules are obeyed (p. 452).

### 15.2 Summing a series the easy way (pp. 452–453)
Parlor game: "prove" that $S=\sum a_i$ equals any chosen $x$. With $s_n = a_1+\dots+a_n$ and $s_0\equiv 0$:
$$a_n=(s_n-x)-(s_{n-1}-x),\quad 1\le n<\infty \tag{15.1}$$
$$S=(s_1-x)+(s_2-x)+\cdots-(s_0-x)-(s_1-x)-\cdots \tag{15.2}$$
$$S=-(s_0-x)=x \tag{15.3}$$
The fallacy is cancelling infinitely many terms at once. Jaynes's rule, repeated from Chapter 2: apply arithmetic and analysis only to expressions with finite $n$, and then watch how the finite results behave as $n$ grows. Put briefly, passage to a limit should always be the last operation, not the first; in case of doubt this is, he says, the only safe way to proceed (p. 452). At a finite stage the $x$'s cancel and the last $s$ remains, giving the correct sum (p. 453). The partial sum is $(s_n-x)-(s_0-x)=s_n$ (added step).

*Intuition note:* An infinite cancellation hides a leftover term that never goes away at any finite stage. Doing the finite calculation first keeps that term visible.

### 15.3 Nonconglomerability (pp. 453–455)
**Finite theorem.** For mutually exclusive, exhaustive $C_1,\dots,C_n$:
$$P(A|I)=\sum_{i=1}^n P(AC_i|I)=\sum_{i=1}^n P(A|C_iI)P(C_i|I) \tag{15.4}$$
This is a weighted average. If $L\le P(A|C_iI)\le U$ for all $i$ (15.5), then $L\le P(A|I)\le U$ (15.6). De Finetti called this "conglomerability" (p. 453). So nonconglomerability cannot arise from a correct application of the rules on finite sets, nor on an infinite set reached as a well-defined limit of finite sets (p. 453). Jaynes says it has nevertheless become an institutionalized literature, and he draws his examples from Kadane, Schervish and Seidenfeld (KSS) (p. 453).

**Example 1: rectangular array.** Take $p(i,j)=1/MN$ on $1\le i\le M$, $1\le j\le N$, and event $A: i<j$. By counting (p. 454):
$$P(A|I)=\begin{cases}(2N-M-1)/2N & M\le N\\ (N-1)/2M & N\le M\end{cases}\tag{15.8}$$
With $C_i$ = the statement that we are on column $i$, $P(C_i|I)=1/M$ and
$$P(A|C_iI)=\begin{cases}(N-i)/N & 1\le i\le M\le N\\ (N-i)/N & 1\le i\le N\le M\\ 0 & N\le i\le M\end{cases}\tag{15.9}$$
(the third line is as printed). The bounds are
$$U=(N-1)/N\ \text{(all }M,N),\qquad L=\begin{cases}1-R & M\le N\\ 0 & N\le M\end{cases},\quad R=M/N \tag{15.10}$$
Conglomerability (15.6) therefore always holds (p. 454).

**The fallacious argument (the opponents' reasoning, as Jaynes reports it).** Let $M,N\to\infty$ and count directly on the infinite set (p. 454).
- For fixed $i$, infinitely many points make $A$ true and finitely many make it false. The argument then concludes that $P(A|C_iI)=1$ for all $i$, yet $P(A|I)<1$.
- For rows $D_j$, the same argument gives $P(A|D_jI)=0$ for all $j$, yet $P(A|I)>0$. These are two nonconglomerabilities in opposite directions from one model.
- A single partition also gives both. Taking $i=1,2,\dots$ in increasing order, the probabilities look like 1. Taking $i=N,N-1,\dots$ in decreasing order, they look like 0. Relabeling $i$ by subtracting $N+1$ would leave this infinite-set reasoning equally "valid", whereas in finite-first arithmetic an arbitrary relabeling has no effect on the counting (p. 455).

**Jaynes's diagnosis.** The argument assumes the limit is already accomplished before the arithmetic, which reverses Gauss's policy. With strict finite-first calculation, however the limit is approached, the conditional probabilities take values in a wide interval whose lower bound is 0 or $1-R$ and whose upper bound tends to 1, and (15.5) is always satisfied (p. 455). There is a second fallacy: $P(A|I)$ was never computed on the infinite set. From (15.8) the limit depends only on $R$:
$$P(A|I)\to\begin{cases}1-R/2 & R\le1\\ 1/(2R) & R\ge1\end{cases}\tag{15.11}$$
Without a limiting ratio, $P(A|I)$ is indeterminate, and any value in $[0,1]$ is possible. The ratio $R$ holds all the relevant information, and it was thrown away too early (p. 455).

*Intuition note:* The "paradox" compares conditional probabilities obtained by counting directly on the infinite set with an unconditional probability that was only bounded by a verbal argument, never calculated. The unconditional value depends on how the array grows, and that dependence was discarded.

### 15.4 The tumbling tetrahedra (pp. 456–459)
**Setup (Stone 1979; KSS notation).** A tetrahedron with faces e⁺, e⁻, µ⁺, µ⁻ is tossed repeatedly. Whenever e⁺ is followed by e⁻ (or e⁻ by e⁺, µ⁺ by µ⁻, µ⁻ by µ⁺), the pair is erased from the record. The player calls for one more toss, sees only the final record $x\in X$, and must bet on $A$ = annihilation occurred at the final toss. What is $P(A|x)$? (p. 456)

**Missing information.** The answer depends on a nuisance parameter, the number $n$ of tosses (noted by Hill 1980). KSS do not mention $n$ except by implication, in a passing remark that the die is rolled a very large number of times. Jaynes infers they mean $n\to\infty$ (p. 456). They ask whether $P(A)=\sum_{x\in X}P(A|x)P(x)$ is conglomerable in the partition $x$ (15.12). With $\theta\in S$ the record before the final toss, KSS conclude by verbal argument (p. 456):
- (a) $0\le p(A|\theta)\le 1/4$ for all $\theta$;
- (b) $3/4\le p(A|x)\le 1$ for all $x$.

If $P(A)$ were conglomerable in both partitions it would have to lie in both $[3/4,1]$ and $[0,1/4]$, which is impossible (p. 456).

**Jaynes's reply.**
- He accepts (a). Tosses are independent, so $p(A|\theta)=1/4$, except for a blank record, where it is 0 (p. 457).
- (b) fails as argued: the final toss affects $x$, so knowing $x$ gives information about it (p. 457).
- The two statements use different prior information, which the notation hides. With $I$ written out, $P(A|I)=\sum_x P(A|xI)P(x|I)$ (15.13). $I_a$ gives uniform probability on the $4^n$ toss sequences. $I_b$ gives uniform probability on the set of records, which is very non-uniform on toss sequences. They are two different problems (p. 457).
- Exercise 15.1 asks the reader to show that a record of length 20 after 40 tosses (10 annihilations) corresponds to about $10^{14}$ of the $4^{40}=1.21\times10^{24}$ sequences, while a record of length 40 corresponds to one (p. 457). This is also Jaynes's argument for writing $I$ explicitly (pp. 457–458).

**Finite-$n$ structure.** With $I$ as in $I_a$, for known $n$ the quantities $p(A|nI)$, $p(x|nI)$, $p(A|nxI)$ are determinate combinatorial problems. For unknown $n$:
$$p(A|I)=\sum_n p(A|nI)p(n|I),\qquad p(x|I)=\sum_n p(x|nI)p(n|I)\tag{15.14}$$
$$p(A|xI)=\sum_n p(A|nxI)p(n|xI)=\frac{\sum_n p(A|nxI)p(x|nI)p(n|I)}{\sum_n p(x|nI)p(n|I)}\tag{15.15}$$
The problem is indeterminate until $p(n|I)$ is assigned. Passing to infinite $n$ means choosing priors on $n$ that sit on ever larger $n$. This can be done in many ways, and the results depend on the way unless the three conditional probabilities have $n$-independent limits (p. 458).

For any finite $n$, $X$ and $S$ are finite (about $3^n$ records asymptotically), and
$$p(A|nI)=\sum_{x\in X}p(A|xnI)p(x|nI)=\sum_{\theta\in S}p(A|\theta nI)p(\theta|nI)\tag{15.16}$$
so the weighted-average theorem excludes nonconglomerability in both partitions (p. 458). Two bounds for finite $n$:
- Some records have known no-annihilation, so the lower bound is $p(A|nxI)=0$, not 3/4.
- For even $n$, some records of length zero must have ended in annihilation, so the upper bound 1 is reached (p. 458).
- For even $n$, $\theta$ cannot be blank, so $p(A|nI)=p(A|\theta nI)=1/4$ for all $\theta$, and no averaging theorem is needed (p. 459).

### 15.5 Solution for a finite number of tosses (pp. 459–464)
**Reduction to a random walk (p. 459).** Let $y(n)$ be the record length. Annihilation at toss $n$ gives $y(n)=y(n-1)-1$. No annihilation gives $y(n)=y(n-1)+1$. If $y(n-1)=0$, annihilation is impossible. Only $\alpha\equiv y(n-1)$ matters for $A$. Permuting symbols of $x$ at fixed $y$ changes nothing, so $n$ and $y\equiv y(n)$ are sufficient statistics. The problem is a one-dimensional random walk with a reflecting boundary at $y=0$: up with probability 3/4, down with probability 1/4, and up with probability 1 at $y=0$. After $m$ annihilations $y(n)=n-2m$ (p. 459).

**Exact solution (pp. 459–461).** Let $p^{(n)}_i\equiv p(i|nI)$ for $0\le i\le n$ (15.17). The initial vector is $p^{(0)}=(1,0,0,\dots)^T$ (15.18), and
$$p^{(n)}_i=\sum_{j=0}^{n-1}M_{ij}p^{(n-1)}_j,\quad 0\le i\le n,\ 1\le n<\infty \tag{15.19}$$
$$M=\begin{pmatrix}0&1/4&0&0&\cdots\\1&0&1/4&0&\cdots\\0&3/4&0&1/4&\cdots\\0&0&3/4&0&\cdots\\ \vdots&&&&\ddots\end{pmatrix}\tag{15.20}$$
(rows and columns numbered from 0; $M_{10}=1$ is the reflection, which would be 3/4 without it). Shapes: at step $n$ only the first $n+1$ rows and columns of $M$ are used, and $p^{(n)}$ is a vector of length $n+1$. The prior is the first column of $M^n$:
$$p^{(n)}_i=M^n_{i,0}\tag{15.21}$$
meaning $(M^n)_{i,0}$. With $D\equiv y(n)=i$ and $H\equiv y(n-1)=\alpha$ (15.22):
$$p(D|I)=M^n_{i,0},\quad p(H|I)=M^{n-1}_{\alpha,0}\tag{15.23}$$
$$p(D|HI)=\begin{cases}\tfrac34\delta(i,\alpha+1)+\tfrac14\delta(i,\alpha-1)&\alpha>0\\ \delta(i,1)&\alpha=0\end{cases}\tag{15.24}$$
Bayes' theorem gives
$$p(H|DI)=p(H|I)\frac{p(D|HI)}{p(D|I)}=\frac{M^{n-1}_{\alpha,0}}{M^n_{i,0}}\{\text{the braces of (15.24)}\}\tag{15.25}$$
Since $A$ occurs iff $\alpha=i+1$,
$$p(A|DnI)=\frac{M^{n-1}_{i+1,0}}{4M^n_{i,0}}\tag{15.26}$$
and, because
$$4M^n_{i,0}=4\sum_j M_{ij}M^{n-1}_{j,0}=3M^{n-1}_{i-1,0}+M^{n-1}_{i+1,0}\tag{15.27}$$
the posterior odds are
$$o(A|DnI)=\frac{p(A|xnI)}{p(\bar A|xnI)}=\frac13\frac{M^{n-1}_{i+1,0}}{M^{n-1}_{i-1,0}}\tag{15.28}$$
Jaynes says the exact solution of the problem KSS had in mind appears to be the limit $n\to\infty$ of (15.26) or (15.28) (p. 461).

**Approximation by an unreflected walk (pp. 461–462).** Without the reflection, the walk with up-probability $p$ and down-probability $q=1-p$ obeys
$$f(i|n+1)=pf(i-1|n)+qf(i+1|n)\tag{15.29}$$
whose solution is binomial, $b(r|n,p)$ with $r=(n+i)/2$. Since $y(1)=1$ is forced, $f(i|n)=b(r|n-1,p)$. This ignores the reflecting boundary. For $p=3/4$ the probability that drifts below zero is almost negligible. For large $n$ nearly all the probability lies in $\hat y\pm\sqrt n$, with $\hat y=(p-q)n=n/2$, far from the boundary, so the approximation becomes exact in the limit (p. 462).

**Closed form (asymptotic approximation).** The first toss cannot annihilate, so after $n-1$ tosses there are $n-2$ chances, each with probability 1/4. The prior for $m$ annihilations is
$$f(m)=\binom{n-2}{m}\left(\tfrac14\right)^m\left(\tfrac34\right)^{n-2-m},\ 0\le m\le n-2\tag{15.30}$$
$$p(\alpha|n)=f\!\left(\frac{n-1-\alpha}{2}\right),\quad E(\alpha|I)=n/2\tag{15.31}$$
The prior for $y(n)=i$ is (15.31) with $n-1\to n$ and $\alpha\to i$. Given $y$, $\alpha=y\pm1$. Writing $m\equiv(n-y)/2$:
$$o=\frac{p(A|yn)}{p(\bar A|yn)}=\frac{p(\alpha=y+1|yn)}{p(\alpha=y-1|yn)}=\frac{(1/4)\binom{n-2}{m-1}(1/4)^{m-1}(3/4)^{n-1-m}}{(3/4)\binom{n-2}{m}(1/4)^m(3/4)^{n-2-m}}\tag{15.32}$$
The factors 1/4 and 3/4 cancel:
$$o=\frac{m!(n-2-m)!}{(m-1)!(n-1-m)!}=\frac{n-y}{n-2+y}\tag{15.33}$$
$$p(A|yn)=\frac{o}{1+o}=\frac{n-y}{2(n-1)}\tag{15.34}$$
The sampling probabilities 3/4 and 1/4 do not appear. Jaynes presents (15.34) as the asymptotic approximation, compared with the exact (15.26) in Figure 15.1 (pp. 462–463).

**Direct reading.** Given $n$ and $y(n)$, annihilation occurred in exactly $(n-y)/2$ of the $n-1$ possible tosses, and we do not know which. So the probability for the final toss is $(n-y)/(2(n-1))$ (15.35); Jaynes notes that with a little intuitive understanding one could have reasoned this out without any calculation (pp. 462–463). Figure 15.1 (n = 100) compares exact and asymptotic results. The difference is negligible for $n>20$ (p. 463).

**Why 1/4 looked right.** The prior mean is $E(y|I)=(n+1)/2$, so
$$p(A|nI)=\frac{n-E(y|I)}{2(n-1)}=\frac14\tag{15.36}$$
The posterior is 1/4 if the observed $y$ equals its expected value. If $y$ differs, it reveals the actual number of annihilations, and this overrides the 1/4, 3/4 assignments (p. 463). The limit for the original problem is
$$p(A|xI)=\tfrac12(1-z),\quad z\equiv\lim y(n)/n\tag{15.37}$$
(p. 464).

**Common feature.** In the array, the ratio $M/N$ was lost. Here, $n$ and $y(n)$ (hence the sufficient statistic $y/n$) were lost. In both cases supposing the limit already taken throws away the information needed for the solution (p. 464).

*Intuition note:* After $n$ tosses and a record of length $y$, you know how many annihilations occurred. You do not know when, so each toss after the first is equally likely to have been one. The answer equals 1/4 only when $y$ is its expected value; otherwise the observed $y$ overrides the 1/4, 3/4 assignments.

### 15.6 Finite vs. countable additivity (pp. 464–467)
- **Whose view is whose.** Jaynes says nonconglomerability is only a red herring hiding the real issue. A follower of de Finetti would say the issue is "finite additivity"; Jaynes replies that this is also a red herring, because it is used for almost the opposite of what it sounds like (p. 464).
- Chapter 2 gives the finite sum rule $p(A|C)=\sum_{i=1}^n p(A_i|C)$ (15.38). Passing to countably many terms (a convergent series) seems rather innocuous to Jaynes. If the series failed to converge, Jaynes would refuse to pass to the limit (p. 464).
- **Feller's definitions (quoted).** A function $F$ on intervals is finitely additive if $F\{I\}=F\{I_1\}+\dots+F\{I_n\}$ for finite partitions. His weird example on $R^1$: $F\{I\}=0$ for $I=(a,b)$ with $b<\infty$ and $F\{(a,\infty)\}=1$. It is finitely but not countably additive (p. 465).
- **Jaynes's reading.** The weirdness is not lost continuity. It assigns probability 0 to every finite range and 1 to the infinite range. Think instead of
$$p(x|r)=\begin{cases}1/r&0\le x<r\\0&r\le x<\infty\end{cases}\tag{15.39}$$
$$F(a,b)=\int_a^b dx\,p(x|r)=\begin{cases}(b-a)/r&0\le a\le b\le r<\infty\\(r-a)/r&0\le a\le r\le b<\infty\\0&0\le r\le a\le b<\infty\end{cases}\tag{15.40}$$
For finite $r$ this is countably (and finitely) additive. Taking the limit first would require a probability density that is everywhere zero yet integrates to one, and Jaynes says there is no such thing (p. 465).
- **Limit last.** Take a continuous monotonic cumulative function with $G(x)\to1$ as $x\to+\infty$ and $G(x)\to 0$ as $x\to-\infty$ (15.41), and set $F\{(a,b)\}=G(b)-G(a)$. This is manifestly countably additive. If $G$ is differentiable, $f=G'$ is a normalized density (p. 466).
- **Conclusion.** "Finite additivity" is a euphemism for reversing the order of limits and getting into trouble with non-normalizable distributions. Feller saw this and warned against it (p. 466). The real question is whether uniform distributions on infinite sets are legitimate objects, i.e. whether infinitely many zeros can add to one. Advocating finite additivity (de Finetti) is a devious "yes". Advocating countable additivity (Kolmogorov, Feller) is, he says, an equally devious "no" in the spirit of Gauss. De Finetti, in Jaynes's report, regards finite additivity as the weaker assumption (p. 466). The terms are compared to "randomization" in Chapter 3 (p. 467).

### 15.7 The Borel–Kolmogorov paradox (pp. 467–470)
**Setup.** Prior information $I$ assigns a bivariate normal density with correlation $\rho$:
$$p(dx\,dy|I)=\frac{\sqrt{1-\rho^2}}{2\pi}\exp\!\left\{-\tfrac12(x^2+y^2-2\rho xy)\right\}dx\,dy\tag{15.42}$$
(the minus sign is my addition; see Reading notes). The marginals are
$$p(dx|I)=\sqrt{\tfrac{1-\rho^2}{2\pi}}\exp\{-\tfrac12(1-\rho^2)x^2\}dx\tag{15.43}$$
and the same for $y$ (15.44). The quick conditional is obtained by setting $y=y_0$ in (15.42) and renormalizing:
$$p(dx|y=y_0I)=A\exp\{-\tfrac12(x^2+y_0^2-2\rho xy_0)\}dx\tag{15.45}$$
This is an ad hoc device, not derived from the rules (15.46), (15.47): $p(AB|X)=p(A|BX)p(B|X)$ and $p(A|BX)=p(AB|X)/p(B|X)$. With the discrete propositions
$$A\equiv x\text{ in }dx,\quad B\equiv y\text{ in }(y_0<y<y_0+dy)\tag{15.48}$$
the rules give
$$p(A|BI)=p(dx|dy\,I)=\frac{p(dx\,dy|I)}{p(dy|I)}=\frac1{\sqrt{2\pi}}\exp\{-\tfrac12(x-\rho y_0)^2\}dx\tag{15.49}$$
(since $dy$ cancels, taking $dy\to0$ does nothing). This is identical to (15.45), so here the shortcut happened to work (p. 468).

**Generating the paradox.** Use $(x,u)$ with $u\equiv y/f(x)$, $0<f(x)<\infty$ (15.50). The Jacobian is
$$\frac{\partial(x,u)}{\partial(x,y)}=\left(\frac{\partial u}{\partial y}\right)_x=\frac1{f(x)}\tag{15.51}$$
$$p(dx\,du|I)=\frac{\sqrt{1-\rho^2}}{2\pi}\exp\{-\tfrac12(x^2+u^2f^2(x)-2\rho uf(x))\}f(x)\,dx\,du\tag{15.52}$$
The marginals are as before. But setting $u=0$ and renormalizing gives
$$p(dx|u=0\,I)=A\exp\{-\tfrac12x^2\}f(x)\,dx\tag{15.53}$$
which differs from (15.45) at $y_0=0$ by the arbitrary factor $f(x)$, although "$u=0$" and "$y=0$" are the same condition (p. 468).

**Resolution.** The hypothesis space contains propositions like $a\le y\le b$ of positive measure. "$y=0$" can only mean a limit of such propositions, e.g. $A_\epsilon\equiv|y|<\epsilon$ (15.54), with $p(H|A_\epsilon I)=p(HA_\epsilon|I)/p(A_\epsilon|I)$ (15.55) for $H\equiv$ "$x$ in $dx$". But "$y=0$" can equally be the limit of wedges $B_\epsilon\equiv|y|<\epsilon|x|$ (15.56). The limits differ:
$$\lim_{\epsilon\to0}p(H|A_\epsilon)\propto g(x),\qquad\lim_{\epsilon\to0}p(H|B_\epsilon)\propto|x|g(x)\tag{15.57}$$
and $|x|$ could be any non-negative $f(x)$. Footnote 3: the rules say to take the limit of the ratio, not the ratio of the limits (p. 469). The only safe procedure for a measure-zero subspace is to specify the limit explicitly, and the answer "will and must" depend on it (p. 469).

**Great-circle puzzle (p. 470).** Take a uniform density on a sphere, with latitude $\theta$ and longitude $\phi$. Conditioning on the equator ($|\theta|<\epsilon$) gives uniform $p(\phi)=(2\pi)^{-1}$. Conditioning on the Greenwich meridian ($|\phi|<\epsilon$) gives $p(\theta)=\tfrac12\cos\theta$, which is largest at the equator and zero at the poles. "Great circle" is ambiguous until the limiting operation is specified. The symmetry argument assumes the equatorial limit, while someone slicing an orange might assume the other (p. 470).

*Intuition note:* "y = 0" does not say how thin the strip around y = 0 is, or how its thickness varies with x. Different thinning rules weight x differently, so they give different conditional densities.

### 15.8 The marginalization paradox (pp. 470–473)
Background (p. 470): the paradox came from Dawid, Stone and Zidek (1973), "DSZ". Jaynes says it seems to have fooled every expert except D. A. S. Fraser, and that the establishment endorsed it immediately and enthusiastically. Marginalization may nonetheless be useful for constructing uninformative priors (Jaynes 1980), which Jaynes calls ongoing research.

**B₁ (conscientious Bayesian).** Data $x$, parameters $\theta=(\eta,\zeta)$ with $\eta$ a nuisance parameter. With prior $\pi(\eta,\zeta)$:
$$p(\zeta|x)=\int d\eta\,p(\eta\zeta|x)=\frac{\int d\eta\,p(x|\eta\zeta)\pi(\eta,\zeta)}{\int d\zeta\int d\eta\,p(x|\eta\zeta)\pi(\eta,\zeta)}\tag{15.58}$$
Jaynes's policy: any proper prior, or any limit of proper priors for which the ratio converges to a proper posterior, is admissible. He believes that following this strictly cannot produce ambiguities (p. 471).

**DSZ's special circumstance.** The data split as $x=(y,z)$ with
$$p(z|\eta\zeta)=\int dy\,p(yz|\eta\zeta)=p(z|\zeta)\tag{15.59}$$
(examples: translation-invariant $z$ for a location $\eta$; scale-invariant $z$ for a scale $\eta$). DSZ found cases, with an improper prior for $\eta$, where B₁'s posterior depends on $z$ only:
$$p(\zeta|yz)=p(\zeta|z)\tag{15.60}$$
**B₂ (lazy Bayesian).** From (15.59) and (15.60), B₂ guesses that $y$ and $\eta$ can be dropped and uses the reduced model:
$$p(\zeta|z)=\frac{p(z|\zeta)\pi(\zeta)}{\int d\zeta\,p(z|\zeta)\pi(\zeta)}\tag{15.61}$$
He cannot reproduce B₁'s result for any $\pi(\zeta)$. **DSZ's view:** on grounds of this intuitive "reduction principle" they thought it obvious that B₁ and B₂ must agree, so one of them must be guilty. They blamed B₁'s improper prior for $\eta$ and spoke of the "paradoxical unBayesianity" of B₁'s posterior (p. 472).

**Jaynes's reply (p. 472).** (15.61) is an intuitive guess and does not follow from (15.58)–(15.60). Three confusions are hidden by the notation:
1. (15.60) is a different function of $z$ for different $\eta$-priors, so prior information about $\eta$ still matters. B₁ uses relevant information that B₂ ignores.
2. Orthodox notation is ambiguous. The symbol $p(z|\zeta)$ would normally mean a different model with no $\eta$. The intended meaning (model with $\eta$ present, but $z$'s distribution independent of its value) seems expressible in orthodox notation only as $\frac{\partial}{\partial\eta}p(z|\eta\zeta)=0$ (15.62).
3. $p(\zeta|z)$ likewise refers to a model without $y$, and posteriors depend on a prior that the notation never shows (p. 473).

**Charitable reading.** B₂ may just be uninformed, given only $p(z|\zeta)$ and unaware of $(\eta,y)$. Then (15.61) is valid for his state of knowledge, whether or not (15.60) holds. With Jeffreys's notation, $p(\zeta|yzI_1)$ and $p(\zeta|zI_2)$, there is no paradox. Different prior information gives different conclusions, as different data would (p. 473). Footnote 5: Jaynes (1980) had not yet seen that (15.60) is not essential, and followed DSZ in concentrating on its validity. With hindsight there is in general no reason to expect it to hold (p. 473).

**Exercise 15.2 (p. 473).** B₃ has B₁'s prior but is not given $y$. The exercise asks the reader to show that, if (15.59) holds (in the sense of (15.62)), B₂ and B₃ always agree, without using (15.60).

#### 15.8.1 On to greater disasters (pp. 474–477)
**DSZ's "proof" (p. 474).** They claim the discrepancy could not have arisen if B₁ used a proper prior. With proper $\pi(\eta,\zeta)$ the integrals converge, and by the product rule and (15.59)
$$p(x|\eta\zeta)=p(y|z\eta\zeta)p(z|\eta\zeta)=p(y|z\eta\zeta)p(z|\zeta)\tag{15.63}$$
$$p(\zeta|yz)\int d\zeta\int d\eta\,p(y|z\eta\zeta)p(z|\zeta)\pi(\eta,\zeta)=\int d\eta\,p(y|z\eta\zeta)p(z|\zeta)\pi(\eta,\zeta)\tag{15.64}$$
Assuming (15.60) and integrating out $y$ (using $\int d\eta\,\pi(\eta,\zeta)=\pi(\zeta)$) gives
$$p(\zeta|z)\int d\zeta\,p(z|\zeta)\pi(\zeta)=p(z|\zeta)\pi(\zeta)\tag{15.65}$$
which equals (15.61). **Jaynes (following Fraser):** the proof uses contradictory assumptions. If B₁'s prior is proper, (15.60) cannot be true, which is why DSZ found it only with improper priors (p. 474).

**Change-point problem (pp. 474–476).** There are $n$ independent exponential observations. The first $\zeta$ have mean $1/\eta$ and the rest $1/(c\eta)$, with $c\ne1$ known and $\eta,\zeta$ unknown. The sampling density is
$$p(x|\eta\zeta I_1)=c^{n-\zeta}\eta^n\exp\left\{-\eta\left(\sum_{i=1}^{\zeta}x_i+c\sum_{i=\zeta+1}^{n}x_i\right)\right\},\ 1\le\zeta\le n\tag{15.66}$$
Let $y\equiv x_1$, $z_i\equiv x_i/x_1$ (so $z_1\equiv1$), and $dx_1\cdots dx_n=y^{n-1}dy\,dz_2\cdots dz_n$. Then
$$p(z_2\cdots z_n|\eta\zeta I_1)=\int_0^\infty dy\,c^{n-\zeta}\eta^ny^{n-1}\exp\{-\eta yQ(\zeta,z)\}=\frac{c^{n-\zeta}(n-1)!}{Q(\zeta,z)^n}=p(z|\zeta I_1)\tag{15.67}$$
$$Q(\zeta,z)\equiv\sum_1^\zeta z_i+c\sum_{\zeta+1}^nz_i\tag{15.68}$$
(the sign in the exponent of (15.67) is as needed for convergence; see Reading notes). With independent priors $\pi(\zeta)$ (proper) and $\pi(\eta)$, B₁ and B₂ obtain
$$p(\zeta|yzI_1)\propto\pi(\zeta)c^{n-\zeta}\int_0^\infty d\eta\,\exp\{-\eta yQ\}\pi(\eta)\eta^n\tag{15.69}$$
$$p(\zeta|zI_2)\propto\pi(\zeta)p(z|\zeta)=\frac{\pi(\zeta)c^{-\zeta}}{[Q(\zeta,z)]^n}\tag{15.70}$$
B₁'s answer depends on $y$, $z$ and on $\pi(\eta)$. Common sense expects this: if $\eta$ is known, the absolute sizes of the $x_i$ help locate the change point. With partial knowledge of $\eta$ they help less but are still relevant, so (15.60) cannot hold (p. 475).

For the improper prior
$$\pi(\eta)=\eta^{-k},\ 0<\eta<\infty\tag{15.71}$$
(any $k$ for which (15.69) converges), the separation (15.60) does hold:
$$p(\zeta|zI_1)\propto\frac{\pi(\zeta)c^{-\zeta}}{[Q(\zeta,z)]^{n-k+1}}\tag{15.72}$$
(This follows from $\int\eta^{n-k}e^{-\eta yQ}d\eta=(n-k)!/(yQ)^{n-k+1}$; added step.) B₂ agrees with B₁ for some $\pi(\zeta)$ only when $k=1$ (p. 476).

**Exercise 15.3 (p. 476).** If $p(yz|\eta\zeta)=\eta^{-1}h(z,\zeta;y/\eta)$ (15.73), then (15.59) follows, and B₁ and B₂ agree iff $\pi(\eta)\propto\eta^{-1}$. The $k=1$ prior is the Jeffreys prior, "completely uninformative" about a scale parameter by several criteria. With it B₁ has no extra information, so agreement is expected (p. 476). Footnote 6: DSZ wrote priors in terms of the "wrong" original parameters, which hid this. Jaynes (1980) showed that, after transforming to the relevant parameters $\eta,\zeta$, in every DSZ example except #5 $\eta$ is a scale parameter for $y$ and the paradox disappears for and only for the Jeffreys prior (p. 476).

**When does separation hold?** In the change-point problem, for any prior $\pi(\eta)$, (15.69) depends on $y,z$ through $yQ(\zeta,z)$. Separation (15.60) needs $y$ and $\zeta$ in separate factors:
$$\int_0^\infty d\eta\,\exp\{-\eta yQ\}\pi(\eta)\eta^n=f(yQ)=g(y,z)h(\zeta,z)\tag{15.74}$$
A function of $\log y+\log Q$ that equals $\log g(y)+\log h(\zeta)$ must be linear, so $f(yQ)=(yQ)^a$ with $a(z,n)$. Since the Laplace transform is uniquely invertible and
$$\int_0^\infty d\eta\,\exp\{-\eta yQ\}\eta^{a-1}=\frac{(a-1)!}{(yQ)^a}\tag{15.75}$$
(15.60) cannot hold in the change-point problem unless the prior is of the improper form $\pi(\eta)=\eta^{-k}$ (p. 477). Exercise 15.4: this holds in any problem like Exercise 15.3, so DSZ's later examples repeat the same point (p. 477).

**Proper prior counter-example.** Take $\pi(\eta)\propto\eta^a\exp\{-b\eta\}$ with $b>0$:
$$p(\zeta|yzI_1)\propto\frac{\pi(\zeta)c^{-\zeta}}{(b+yQ)^{n+a+1}}\tag{15.76}$$
$y$ cannot be disentangled, so (15.60) fails. The "paradox" disappears not because B₁ and B₂ agree but because B₂ cannot invoke his reduction principle. Jaynes says that in any DSZ example, inserting any proper prior for which the integrals can be done gives an equally good counter-example to (15.65) (p. 477).

*Intuition note:* A proper prior on η says something about how big η is, so the actual sizes of the data carry information about ζ. For a scale parameter, only a prior that says nothing about η (the scale-invariant η^{-1}) lets B₁ and B₂ agree.

### 15.9 Discussion (pp. 478–480)
- The mathematics supports the idea of "complete ignorance", contrary to DSZ's apparent goal and some discussants. The Jeffreys prior does what an uninformative prior should whenever $\eta$ is a scale parameter. Exercise 15.3 turns "uninformative" from an intuition into a theorem (p. 478).
- Fraser's remark (quoted by Jaynes): restricting to proper priors means that in the interesting cases one cannot eliminate a variable. Jaynes: with a proper prior, in general (15.60) fails and B₂'s reduction cannot be applied. Agreement in the change-point problem requires an improper prior, which is the opposite of the DSZ conclusion (p. 478).
- Jaynes argues that, generally, if $y$ and $\eta$ are both known, they are relevant to $\zeta$ unless $p(yz|\eta\zeta)=p(y|\eta)p(z|\zeta)$. Any proper prior on an infinite domain is informative about $\eta$, because it fixes finite bounds within which $\eta$ almost surely lies (pp. 478–479).
- **History, as Jaynes reports it.** Anti-Bayesians seized on DSZ; Lindley, Jaynes says, confessed to sins he had not committed; the Royal Statistical Society thanked DSZ. A flood of articles since 1973 rejects improper priors, and nobody noted that proper priors do not remove the discrepancy (p. 479).
- Jeffreys (1939, §3.8) and Geisser and Cornfield (1963) had already seen and correctly interpreted this. Geisser and Cornfield called B₂'s result a "pseudoposterior distribution". Jaynes says DSZ cite them but trust the reduction principle over the rules (p. 479).
- In all examples but #5, within each infinite class $C$ of improper priors, one prior makes B₁ and B₂ agree. Such a prior must be "completely uninformative" about $\eta$. Jaynes calls this a purely objective definition of complete ignorance from the sum and product rules alone, without entropy or group invariance (pp. 479–480).

#### 15.9.1 The DSZ Example #5 (pp. 480–483)
**Setup.** The data are $n$ observations from $N(\mu,\sigma)$. With proper prior $f(\mu,\sigma)$ (15.77), the posterior is $g(\mu,\sigma)=f L/\int\!\!\int fL$ (15.78–15.79), with likelihood
$$L(\mu,\sigma)=\sigma^{-n}\exp\left\{-\frac{n}{2\sigma^2}[s^2+(\mu-\bar x)^2]\right\}\tag{15.80}$$
where $\bar x$ and $s^2$ are the usual sample mean and variance, which are sufficient statistics. For $s^2>0$ the likelihood is bounded, so a proper prior gives a proper posterior, and moment conditions (15.81) give higher posterior moments (p. 480).

**Interest in $\zeta\equiv\mu/\sigma$ (15.82).** With $d\mu\,d\sigma=\sigma\,d\zeta\,d\sigma$,
$$h_1(\zeta)=\int_0^\infty\sigma\,d\sigma\,g(\sigma\zeta,\sigma)\tag{15.83}$$
which converges for $n>1$ (p. 481). Take the conjugate prior
$$f(\mu,\sigma)\,d\mu\,d\sigma\propto\sigma^{-\gamma-1}\exp\{-\beta/\sigma-\alpha\mu^2\}d\mu\,d\sigma\tag{15.84}$$
proper for $(\alpha,\beta,\gamma)>0$ and tending to the Jeffreys prior $d\mu\,d\sigma/\sigma$ as $(\alpha,\beta,\gamma)\to0$. The posterior is
$$g(\mu,\sigma)\propto\sigma^{-n-\gamma-1}\exp\left\{-\frac\beta\sigma-\alpha\mu^2-\frac n{2\sigma^2}[s^2+(\mu-\bar x)^2]\right\}\tag{15.85}$$
Use the sufficient statistics
$$R^2\equiv n(\bar x^2+s^2)=\sum x_i^2,\qquad r\equiv\frac{n\bar x}R=\frac{\sum x_i}{\sqrt{\sum x_i^2}}\tag{15.86}$$
Then
$$h_1(\zeta|r,R)\propto e^{-n\zeta^2/2}\int_0^\infty d\omega\,\omega^{n+\gamma-1}\exp\left\{-\tfrac12\omega^2+r\zeta\omega-\beta R^{-1}\omega-\alpha\zeta^2R^2\omega^{-2}\right\}\tag{15.87}$$
As $\alpha,\beta\to0$, $R$ drops out:
$$h_1(\zeta|r,R)\to h_1(\zeta|r)\propto e^{-n\zeta^2/2}\int_0^\infty d\omega\,\omega^{n+\gamma-1}\exp\{-\tfrac12\omega^2+r\zeta\omega\}\tag{15.88}$$
The sampling distribution for $r$ depends only on $\zeta$:
$$p(r|\mu\sigma)\propto(n-r^2)^{(n-3)/2}\int_0^\infty d\omega\,\omega^{n-1}\exp\{-\tfrac12\omega^2+r\zeta\omega\}\tag{15.89}$$
(sign as discussed in Reading notes). **But** $h_1(\zeta|r)/p(r|\zeta)$ still depends on $r$. The Jeffreys case $\gamma=0$ equalizes the integrals but leaves a factor involving $(n-r^2)$, so no prior $p(\zeta|I_2)$ makes B₂ reproduce (15.88) (p. 482).

**Meaning.** Here the disagreement persists for proper priors too (another counter-example to (15.65)). What B₁ uses and B₂ ignores is not a prior on the nuisance parameter. It is the qualitative fact that a nuisance parameter exists, which already constitutes relevant prior information. In general, any prior information relevant to $\zeta$, whether or not it concerns $\eta$, that B₁ uses and B₂ does not will give different conclusions. Jaynes (1980) calls this "ζ-overdetermination" (p. 482).

**Necessary and sufficient condition for agreement (Jaynes 1980).** The quantity
$$\int d\eta\,p(y|z\eta\zeta I_1)\pi(\eta)=p(y|z\zeta I_1)\tag{15.90}$$
must be independent of $\zeta$ for all samples $y,z$. Equivalently,
$$\int_{S_\eta}d\eta\,p(yz|\eta\zeta)\pi(\eta)=p(y|zI_1)p(z|\zeta),\quad\zeta\in S_\zeta,\ \text{all }y,z\tag{15.91}$$
$$\int_{S_\eta}d\eta\,K(\zeta,\eta)\pi(\eta)=\lambda f(\zeta)\tag{15.92}$$
This is a Fredholm integral equation. The kernel is B₁'s likelihood $K=p(yz|\zeta\eta)$, the driving term is B₂'s likelihood $f=p(z|\zeta)$, and $\lambda(y,z)=p(y|zI_1)$ is unknown. Each data set gives a different equation, so an "uninformative" prior must satisfy (in general) uncountably many at once (p. 482).

**Why a solution can still exist (p. 483).** The $L^2$ functions on $S_\zeta$ form a Hilbert space $H_\zeta$. For fixed data, $K(\zeta,\eta)$ as $\eta$ varies spans a subspace $H'_\zeta(y,z)$. The kernel is *complete* if $H'_\zeta=H_\zeta$. If it is incomplete and $f(\zeta)$ lies outside $H'_\zeta$ for some data, there is no solution. In that case the bare existence of $(y,\eta)$ restricts B₁'s possible likelihood functions, and no prior on $S_\eta$ restores agreement. Jaynes says Example #5 is of this kind. Each single-data-set equation constrains $\pi(\eta)$ only on a tiny subspace, and these subspaces are scattered, in Jaynes's image, like stars in the sky inside $H_\zeta$. So the whole system can have nontrivial solutions (p. 483).

#### 15.9.2 Summary (pp. 483–484)
(15.88) is the correct marginal posterior in problem P₁ with parameters $(\zeta,\sigma)$. It still depends on the prior for $\sigma$, as it should. (15.89) can be interpreted as a valid sampling distribution for a problem P₂ in which $\zeta$ is the only parameter. P₂ gives
$$h_2(\zeta)\propto f_2(\zeta)\int d\omega\,\omega^{n-1}\exp\{-\tfrac12\omega^2+r\zeta\omega\}\tag{15.93}$$
a different functional form. There is no paradox (p. 483). Jeffreys avoided the errors because (1) he held that the sum and product rules take precedence over ad hoc devices, and (2) he always indicated prior information $I$ in the symbols. Jaynes says orthodox training had no term or symbol for prior information (p. 484). Footnote 7 is Jaynes's remarks on orthodoxy, Fisher and prior information in 1930–1960.

### 15.10 A useful result after all? (pp. 484–485)
Marginalization suggests a further principle for uninformative priors (besides entropy and transformation groups). Suppose the sufficient statistics are $(t_1,t_2)$ and some $r(t_1,t_2)$ has sampling distribution $p(r|\zeta\eta I)=p(r|\zeta I)$. This defines a pseudoproblem with information $I_2$ in which $\eta$ is absent. A prior $p(\eta|I)$ may make the marginal posterior equal the pseudoposterior. If so, it seems that introducing $\eta$ with that prior conveyed no information about $\zeta$, so the prior must express "complete ignorance" of $\eta$ in a rather fundamental sense. In all cases found so far, such a prior on an infinite domain is improper. Jaynes says extending this to a general construction is still ongoing research (p. 485).

### 15.11 How to mass-produce paradoxes (pp. 485–486)
The procedural error was always failure to obey the product and sum rules, usually through careless infinite sets and limits, sometimes with ad hoc devices such as the reduction principle. Paradoxes of this type can be produced by a three-step recipe (p. 485):
1. Start from a well-defined situation (finite set, normalized distribution, convergent integral) with an unquestioned correct solution.
2. Pass to a limit (infinite magnitude, infinite set, zero measure, improper pdf) without specifying how it is approached.
3. Ask a question whose answer depends on how the limit was approached.

This is "guaranteed" to give a question with several seemingly right answers. Using infinite sets to define propositions is not forbidden. $G\equiv1\le x\le2$ (15.94) is a single discrete proposition. Replacing 2 by $z$ typically gives a well-behaved function $f(z)=P(G|zI)$ whose analytic properties can be used, without losing the protection of Cox's theorems (p. 486).

### 15.12 Comments (pp. 486–489)
- Chapter 5's Hempel paradox is "conceptually generated". Nonconglomerability is "mathematically generated". Marginalization is a compound of both (p. 486).
- Cox's derivation of the rules is for finite sets, and extension to infinite sets by a well-behaved limit is accepted. Jaynes tried for many years to extend Cox's proofs directly to infinite sets, but paradoxes (since Bertrand 1889) argue against it (p. 486).
- **Conclusion (pp. 486–487).** In probability theory an infinite set should be thought of only as the limit of a specified sequence of finite sets, and an improper pdf has meaning only as the limit of a well-defined sequence of proper pdfs. Almost any departure from this policy has the potential to produce a paradox. The Borel–Kolmogorov and marginalization paradoxes turn up so seldom as to encourage overconfidence in the inexperienced. Jaynes's reply to the saying that one cannot argue with success is that one can, and should, argue with success obtained by fraudulent means (p. 487).
- **Mea culpa.** Jaynes admits he too was careless with improper priors until marginalization showed he had been lucky in his choice of problems. If one wants to use an improper prior, the only correct way is to approach it as a limit of proper priors. If the correct limit gives an improper posterior, the data and prior information are too meager for inference about that parameter, and the remedy is more data or information. Past successes were simple problems where data dominated, and the two results typically agreed to six or more significant figures. In future, with complex computer-solved problems in which prior information is essential, improper priors would usually crash programs or give quantitatively wrong answers. Since likelihoods are bounded, proper priors always give finite results (pp. 487–488).
- **Note added.** Jaynes restates the DSZ error: their proof assumes contradictory things. He says every DSZ example is a counter-example when B₁ uses a proper prior. B₁ and B₂ do agree with a proper prior in the trivial case of two independent problems, where $p(yz|\eta\zeta)=p(y|\eta)p(z|\zeta)$ and the prior also factors (p. 489). He says the tetrahedra solution and the marginalization argument are issues of mathematically demonstrable fact that every reader can judge (pp. 488–489).

## Toy example (ours; checks §15.3)
Rectangular array, $p(i,j)=1/MN$, $A: i<j$. Small case $M=N=3$:
- Direct count: $(1,2),(1,3),(2,3)$ are 3 of 9 points, so $P(A)=1/3$. Formula (15.8): $(2\cdot3-3-1)/(2\cdot3)=2/6=1/3$. ✓
- Columns (15.9): $P(A|C_1)=2/3$, $P(A|C_2)=1/3$, $P(A|C_3)=0$. Average: $(2/3+1/3+0)/3=1/3$. ✓ This is inside $[L,U]=[0,2/3]$.

Now let $N=100$ and vary $M$, always with $i=1$:

| $M$ | $R$ | $P(A\mid C_1)=(N-1)/N$ | $P(A\mid I)$ from (15.8) | limit from (15.11) |
|---|---|---|---|---|
| 50 | 0.5 | 99/100 | $(200-50-1)/200=0.745$ | $1-0.25=0.75$ |
| 100 | 1 | 99/100 | $(200-100-1)/200=0.495$ | $0.5$ |
| 200 | 2 | 99/100 | $99/(2\cdot200)=0.2475$ | $1/4=0.25$ |

For every row $P(A|C_1)\to1$, so "P(A|C_i) = 1 for all i" is read off from column 1 of an infinite array. But $P(A|I)$ is 0.745, 0.495 or 0.2475, set by $R$. Conglomerability holds in each row. For $M=50$, $N=100$ we have $L=1-R=0.5$ and $U=0.99$, and $0.5\le0.745\le0.99$. At the other end, for $M\ge N$ (e.g. $M=200$) the column $i=N-1=99$ gives $P(A|C_{99})=(100-99)/100=0.01$, so "$P(A|C_i)=0$ for all $i$" is equally "visible" if one counts from the other side. The claim depends on how the infinite array is approached.

## Concepts
- [[nonconglomerability]] (new) — $P(A|I)$ lies outside the range of the $P(A|C_iI)$ over a partition; Jaynes says it cannot occur on finite sets or well-defined limits of them (p. 453)
- [[conglomerability]] (new) — de Finetti's name for the weighted-average property $L\le P(A|C_iI)\le U\Rightarrow L\le P(A|I)\le U$ (p. 453)
- [[limit-last-policy]] (new) — do arithmetic on finite sets first; take the infinite limit last (Gauss's advice) (p. 452)
- [[finite-vs-countable-additivity]] (new) — Jaynes: a disguised dispute about admitting non-normalizable distributions, i.e. about order of limits (p. 466)
- [[borel-kolmogorov-paradox]] (new) — a conditional density on a measure-zero set depends on the limiting sequence of positive-measure events (p. 469)
- [[marginalization-paradox]] (new) — disagreement of B₁ (full model) and B₂ (reduced model), attributed to different prior information (p. 472)
- [[improper-prior]] (new) — meaningful only as a limit of proper priors; the Jeffreys prior $\eta^{-1}$ is the case relevant to a scale parameter (pp. 476, 487)
- [[complete-ignorance]] (new) — a prior leaving B₁ and B₂ in agreement; Jaynes calls this an objective definition from the sum and product rules (pp. 479–480)
- [[nuisance-parameter]] (new) — parameter integrated out of the posterior; a prior on it still affects the marginal posterior (p. 471)
- [[zeta-overdetermination]] (new) — relevant prior information used by B₁ but ignored by B₂, so no prior reconciles them (p. 482)
- [[sufficient-statistic]] (new) — here $n$ and $y(n)$ in the tetrahedra problem (p. 459)
- [[prior-information-notation]] (new) — Jeffreys's symbol $I$ in $P(A|BI)$; missing $I$ hides that two probabilities are conditional on different information (pp. 457, 473)
- Prior distribution — a proper $\pi(\eta)$ on an infinite domain is informative, since it bounds $\eta$ (p. 479)
- Bayes' theorem — used for $p(H|DI)$ in the tetrahedra problem (p. 461)
- Conjugate prior — the prior (15.84) used in Example #5 (p. 481)
- Probability as extended logic — rules derived by Cox's functional equations, for finite sets (p. 486)
- Cox's theorem — the finite-set derivation of the rules; Jaynes accepts well-defined limits (p. 486)
- Maximum entropy / transformation groups — routes to uninformative priors discussed in earlier chapters; marginalization suggests another (p. 484)

## Canonical instances
- [[rectangular-array-example]] — nonconglomerability from a uniform $M\times N$ array, resolved by the ratio $R$ (pp. 453–455)
- [[tumbling-tetrahedra]] — a reflected random walk with exact solution (15.26) and closed form (15.34) (pp. 456–464)
- [[feller-weird-interval-function]] — finitely additive, not countably additive, and the limit of (15.39) (p. 465)
- [[great-circle-puzzle]] — equator vs. Greenwich meridian conditioning on a sphere (p. 470)
- [[change-point-problem]] — exponential data with a change at $\zeta$ and scale $\eta$ (pp. 474–477)
- [[dsz-example-5]] — normal data with $\zeta=\mu/\sigma$, where B₁ and B₂ never agree (pp. 480–483)
- [[series-sum-fallacy]] — "proof" that any series sums to any $x$ (p. 452)

## Bridges (candidates)
- [structural-analogy] Passage to the limit last ↔ Bayesian: improper prior as the limit of proper priors — the same ordering discipline in a different setting.
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit.
- [metaphor] Conditioning on a measure-zero event ↔ Bayesian: ambiguity of conditioning in a causal model — the answer depends on which limiting experiment is meant.
- [structural-analogy] "Jeffreys prior is uninformative for a scale parameter" ↔ information-theory: the group-invariance / maximum-entropy prior constructions Jaynes mentions (pp. 484–485).
- [structural-analogy] Missing $I$ in $P(A|B)$ ↔ Bayesian: Bayesian workflow's insistence on stating the model — the same demand that the problem be fully specified.

## Questions this raises
- Jaynes says marginalization may give a general principle for uninformative priors beyond location and scale parameters. What would that principle look like for parameters that are not location or scale? (p. 485)
- For a limit of proper priors to give an improper posterior, how large must the data be before the posterior is proper? What does this say about when "too meager" is the right diagnosis? (p. 487)
- How do alternative formalisms that start from measure theory treat the sphere and wedge examples, and would Jaynes accept an explicit specification of the limit as sufficient? (p. 469)
- Are there useful problems where the limit does not exist for any specified sequence, and what would Jaynes's policy say there? (p. 464)

## Exercises worth doing
- Ex. 15.1 (p. 457) — Count how many toss sequences give one record; shows why uniform-on-tosses differs from uniform-on-records — difficulty: medium
- Ex. 15.2 (p. 473) — Show that B₂ and B₃ agree without using (15.60); withholding $y$ makes prior knowledge of $\eta$ irrelevant — difficulty: medium
- Ex. 15.3 (p. 476) — Show the $k=1$ prior is uninformative whenever $\eta$ is a scale parameter for $y$ — difficulty: medium
- Ex. 15.4 (p. 477) — Show that the scale-parameter factorization works for $\pi(\eta)=\eta^{-k}$ in general — difficulty: medium
- Unnumbered (p. 465) — Explain why Feller's weird example "manifestly" violates countable additivity — difficulty: easy

## Reading notes
- Printed pages 451–489; printed = pdf − 30.
- Text layer vs image: some exponent minus signs are missing or unclear in (15.42), the exponent of (15.67), and (15.89). I wrote them with the sign needed for convergence and for consistency with neighboring equations (15.43)–(15.45) and (15.93). Please check against the page images.
- On p. 467 the text says "variance unity", but the marginals (15.43)–(15.44) have variance $1/(1-\rho^2)$.
- (15.9) is copied as printed; its second and third lines overlap at $i=N$, where both give 0.
- p. 454: the text writes $P(A|C_iB)$ where $I$ is meant.
- p. 488 (Note added) refers to "an asymptotic approximation (15.18)". This is probably a misprint for (15.34).
- (15.28) uses an overline (complement) on $A$ in the denominator, which the text layer does not show.
- Footnotes 3, 5, 6 and 7 are summarized in L3; footnotes 1, 2 and 4 are not. Figure 15.1 is a plot (exact points vs. approximating line); I did not read off numeric values.
