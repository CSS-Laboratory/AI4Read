---
id: cover-2006-elements/ch07-kolmogorov
work: cover-2006-elements
unit: 7 Kolmogorov Complexity
pages: 144–182
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Kolmogorov Complexity (Cover & Thomas, Ch. 7)

## L0 — One line
The complexity of a single string is the length of its shortest program on a universal computer. It is machine-independent up to a constant, it matches entropy on average, and it is within an additive constant of −log of the universal probability, but it cannot be computed.

## L1 — The gist (≤ 120 words)
How can we measure the information in one object, with no probability distribution? Kolmogorov complexity K(x) is the length of the shortest program that prints x on a universal computer (a computer that can mimic others). It changes only by an additive constant from machine to machine. Most strings cannot be compressed much. For i.i.d. sources, expected K per symbol tends to the entropy. K(x) is also essentially −log of the "universal probability" of x. K is not computable, because of the halting problem. The chapter uses these ideas for Chaitin's number Ω, gambling, Occam's razor and a "sufficient statistic" of a string. The authors present K as a way of thinking, not a practical algorithm.

**Prerequisites:** entropy and typical sets; prefix codes and the Kraft inequality; binomial coefficients and $\binom nk\le 2^{nH(k/n)}$; Jensen's inequality; the idea of a Turing machine and of halting.

## L2 — Key ideas (5–10 bullets)
- **K(x) = shortest program length on a universal computer (7.1).** It drops the probability distribution used by Shannon codes (p. 144, p. 147).
- **Invariance up to a constant:** $K_U(x)\le K_A(x)+c_A$, where $c_A$ is a simulation program independent of x. The theory is therefore useful mainly for long strings (p. 148–149, p. 153).
- **Counting shows incompressibility is typical.** Fewer than $2^k$ strings have $K<k$, so $P(K(X^n|n)<n-k)<2^{-k}$ for fair-coin strings. Incompressible strings obey the law of large numbers, and the authors argue in outline that they pass every computable randomness test (p. 150, p. 157–159).
- **Link to entropy.** For i.i.d. finite-alphabet sources, $H\le \frac1n E K(X^n|n)\le H+|\mathcal X|\frac{\log n}{n}+\frac cn$. The proof uses Kraft for program lengths and a two-stage "type, then index" description (p. 154–155).
- **Universal probability** $P_U(x)=\sum_{p:U(p)=x}2^{-l(p)}$ dominates, for every computer $A$, the distribution $P_A$ that $A$ induces, up to a constant factor; the book says this covers computable distributions (Thm 7.6.1, p. 161). It is within a constant factor of $2^{-K(x)}$, so $K(x)$ and $\log 1/P_U(x)$ are equivalent measures (p. 160–161, p. 169–175).
- **K is not computable** (halting problem, Berry paradox). Halting programs form a prefix-free set (none is a prefix of another; p. 154), and $\Omega=\Pr(U(p)\text{ halts})$ is algorithmically random (incompressible: $K(\omega_1\dots\omega_n)\ge n-c$), yet its first $n$ bits settle every provable or finitely refutable theorem of under $n$ bits (finitely refutable: a finite counterexample search can disprove it) (p. 162–166).
- **Applications:** universal gambling achieves $\log S(x)+K(x)\ge l(x)$ (p. 166–168). Universal probability gives a Laplace-like rule of succession as an Occam's-razor argument (p. 168–169).
- **Kolmogorov sufficient statistic.** The structure function $K_k(x^n|n)$ separates the "structure" of a string (a short description of a small set containing x) from its residual randomness (p. 175–178).

## L3 — Walkthrough

### Introduction (p. 144–145)
- Earlier chapters: X is a random variable, and the descriptive complexity of the event $X=x$ is $\log\frac1{p(x)}$ (Shannon code), so it depends on the distribution (p. 144).
- Kolmogorov (1965): the algorithmic complexity of an object is the length of the shortest binary program that makes a computer output it. No distribution is needed, and the definition is "essentially computer independent" (p. 144).
- The expected length of the shortest description of a random variable is approximately its entropy. The shortest description therefore acts as a universal code (p. 144).
- The authors say the chapter is demanding and can be omitted in a first course. The shortest program may take infinitely long to find, so practice uses short, non-minimal programs. The authors present the idea as a way to think (p. 144–145).
- **Three strings** (p. 145):
  1. Thirty-two copies of 01: simple.
  2. Looks random but is the binary expansion of $\sqrt2-1$ (the text layer is garbled here): simple, constant-length program.
  3. A string with fraction of 1s not near 1/2, assumed otherwise random. Describe the number k of 1s, then the index among strings with k ones: about $\log n+nH(k/n)$ bits. This is less than n but proportional to n.
  4. A truly random string from coin flips probably has no program better than "Print the following: …", because there are not enough short programs (p. 145).
- Computer independence is true "up to an additive constant" (the length of a pre-program that lets one machine mimic another). That constant is negligible for long complex strings (p. 145).

### 7.1 Models of computation (p. 146–147)
- Turing (1936) modelled a human computing as a finite-state machine on a finite symbol set, with a program tape, a work tape and a transition table (p. 146).
- Every new computational system was found reducible to a Turing machine and conversely. **Church's thesis:** all sufficiently complex computational models compute the same family of functions, matching "effectively computable" (a finite program, finitely many mechanical steps) (p. 146).
- Machine of Fig. 7.1: the program is read one way only and never re-read, so halting programs form a **prefix-free set** (none is a prefix of another). This makes the theory formally analogous to information theory (p. 146).
- The machine maps finite binary strings to finite or infinite ones. It may not halt, and then the value is undefined. The functions computable this way are the partial recursive functions (p. 147).

### 7.2 Definitions and examples (p. 147–153)
**Definition.** For a universal computer $U$, with $l(x)$ the length of x and $U(p)$ the output on program p:
$$K_U(x)=\min_{p:\,U(p)=x}l(p)\tag{7.1}$$
Here $K_U(x)$ is the shortest description length over all descriptions interpreted by $U$ (p. 147).
- **Upper-bound technique:** any unambiguous finite description is an upper bound on K. Example: "Print out the first 1,239,875,981,825,931 bits of the square root of e" is a 73-character program. At 8 bits/character, $K\le 8\cdot73=584$ bits. Most numbers of that length have complexity about as large as their length (p. 147–148).
- **Conditional complexity** given the length: $K(x|l(x))=\min_{p:\,U(p,l(x))=x}l(p)$ (7.2; see the summary, p. 178). The authors note that $K(x|y)$ is usually defined as $K(x|y,y^*)$ to keep chain rules symmetric, but they do not use that definition (p. 148).

**Theorem 7.2.1 (Universality).** If $U$ is universal, then for any computer $A$
$$K_U(x)\le K_A(x)+c_A\quad\text{for all }x,\tag{7.3}$$
with $c_A$ independent of x (p. 148).
*Proof.* Let $p_A$ be a program for A printing x. Prefix it with a simulation program $s_A$ that tells $U$ how to simulate A. Then $p=s_Ap_A$ and
$$l(p)=l(s_A)+l(p_A)=c_A+l(p_A)\tag{7.4}$$
so $K_U(x)\le K_A(x)+c_A$ (7.5) (p. 148).
- $c_A$ may be huge (it contains the implementation of all of A's functions) but does not depend on x. For long x it can be neglected (p. 148–149).
- If both are universal, $|K_U(x)-K_A(x)|\le c$ for all x (7.6). The subscript is dropped from now on (p. 149).

**Theorem 7.2.2.** $K(x|l(x))\le l(x)+c$ (7.7). *Proof:* the program "Print the following $l$-bit sequence: $x_1\dots x_{l(x)}$" is self-delimiting because $l(x)$ is given (p. 149).

**Theorem 7.2.3.** $K(x)\le K(x|l(x))+2\log l(x)+c$ (7.8) (p. 149–150).
*Proof.* Without $l(x)=n$ the computer needs an end marker. Repeat each bit of the binary expansion of n twice and end with 01 as a "comma". Example: 5 = 101 becomes 11001101. This costs $2\lceil\log n\rceil+2$ bits (p. 149–150).
- A recursive scheme (specify the bit-length of n, then specify that, and so on) gives $\log n+\log\log n+\log\log\log n+\cdots$ (sum to the last positive term) $=\log^*n$. Hence
$$K(x)\le K(x|l(x))+\log^*l(x)+c\tag{7.9}$$
(p. 150).

**Theorem 7.2.4 (Lower bound).** $|\{x\in\{0,1\}^*:K(x)<k\}|<2^k$ (7.10).
*Proof.* List all programs of length $<k$: $\Lambda,0,1,00,01,10,11,\dots$ (7.11). Their number is
$$1+2+4+\cdots+2^{k-1}=2^k-1<2^k\tag{7.12}$$
Each program gives only one output (p. 150).

**Notation.** $H_0(p)=-p\log p-(1-p)\log(1-p)$ (7.13), the binary entropy function. $H_0(\frac1n\sum X_i)$ means $H_0$ evaluated at the sample mean $\bar X_n$, not the entropy of the random variable $\bar X_n$ (p. 150).

We assume (7.14), provable by Stirling's formula (or see Example 12.1.3):
$$\frac1{n+1}2^{nH(k/n)}\le\binom nk\le2^{nH(k/n)}$$
(p. 151).

**Examples** (computer that accepts English commands, p. 151–152):
- 7.2.1, n zeros: "Print the specified number of zeroes", with n known. $K(0\dots0|n)=c$ for all n (7.15).
- 7.2.2, first n bits of π (series expression), n known: $K(\pi_1\dots\pi_n|n)=c$ (7.16).
- 7.2.3, Gotham weather for n days (rain = 1): fit a Markov model with empirical transitions (described in $O(\log n)$ bits), then use the Shannon code of length $\log\frac1{p(x)}$. If the entropy is 1/5 bit/day: $K(\text{weather}|n)\approx\frac n5+O(\log n)+c$ (7.17).
- 7.2.4, $0101\dots01$: $K=c$ (7.18).
- 7.2.5, the Mandelbrot fractal on the cover: iterate $z_{i+1}=z_i^2+c$ from $z_0=0$ and count steps for $|z|$ to cross a threshold. Looks complex, but "its Kolmogorov complexity is nearly zero" (p. 152).
- 7.2.6, Mona Lisa: "probably" compressible by a factor of about 3 with an existing algorithm, so $K\le\frac n3+c$ for n pixels (7.19) (p. 152).
- 7.2.7, an integer n: if its bit-length is known, the program has length $c+\log n$. Otherwise $K(n)\le\log^*n+c$ (7.20) (p. 152).
- 7.2.8, n bits with k ones: the program "generate in lexicographic order all sequences with k ones; print the ith". Its variables are k (range $0..n$) and i (range $\binom nk$):
$$l(p)=c+2\log k+\log\binom nk\tag{7.21}$$
$$\le c+2\log k+nH_0\!\left(\tfrac kn\right)\tag{7.22}$$
using $2\log k+2$ bits for k (the inefficient method) and (7.14). So $K(x_1\dots x_n|n)\le nH(\tfrac kn)+2\log k+c$ (7.23) (p. 152–153).

**Theorem 7.2.5.** $K(x_1\dots x_n|n)\le nH_0\!\left(\frac1n\sum x_i\right)+2\log n+c$ (7.24). *Proof:* use the program of Example 7.2.8 (p. 153).

**Remark.** Treat p as the compressed data. Compression succeeds only if $l(p)<l(x)$, i.e.
$$K(x)<l(x)\tag{7.25}$$
For short x the constants dominate, so the theory is useful mainly when $l(x)$ is very large (p. 153).

*Intuition note.* K(x) is "how short can a recipe for x be". Any clear instruction is an upper bound, and counting limits how many strings can have short recipes. A change of machine costs only a fixed-size translator.

### 7.3 Kolmogorov complexity and entropy (p. 153–155)
**Lemma 7.3.1 (Kraft for programs).** For any computer $U$,
$$\sum_{p:\,U(p)\text{ halts}}2^{-l(p)}\le1\tag{7.26}$$
*Proof.* A halting computer reads no further input, so halting programs form a prefix-free set. Apply the Kraft inequality (Theorem 5.2.1) (p. 154).

**Theorem 7.3.1.** Let $X_i$ be i.i.d. with pmf $f(x)$ on a finite alphabet $\mathcal X$, and $f(x^n)=\prod f(x_i)$. Then there is a constant c such that for all n
$$H(X)\le\frac1n\sum_{x^n}f(x^n)K(x^n|n)\le H(X)+\frac{|\mathcal X|\log n}n+\frac cn\tag{7.27}$$
so $E\frac1nK(X^n|n)\to H(X)$ (7.28) (p. 154).
*Proof, lower bound.* Give each $x^n$ the length of its shortest program with $U(p,n)=x^n$. These lengths satisfy Kraft. Expected codeword length is at least the entropy (source coding), so
$$\sum_{x^n}f(x^n)K(x^n|n)\ge H(X_1,\dots,X_n)=nH(X)\tag{7.29}$$
*Upper bound, binary case* (Bernoulli(θ)). By Theorem 7.2.5,
$$K(x_1\dots x_n|n)\le nH_0\!\left(\tfrac1n\sum x_i\right)+2\log n+c\tag{7.30}$$
Taking expectations,
$$EK(X_1\dots X_n|n)\le nEH_0\!\left(\tfrac1n\sum X_i\right)+2\log n+c\tag{7.31}$$
$$\overset{(a)}\le nH_0\!\left(\tfrac1n\sum EX_i\right)+2\log n+c\tag{7.32}$$
$$=nH_0(\theta)+2\log n+c\tag{7.33}$$
where (a) is Jensen's inequality with concavity of entropy (p. 154–155).
*Non-binary alphabet.* First describe the type of the sequence (empirical symbol frequencies, Section 12.1) in $|\mathcal X|\log n$ bits. Then give the index within the type class, which has fewer than $2^{nH(P_{x^n})}$ elements:
$$K(x^n|n)\le nH(P_{x^n})+|\mathcal X|\log n+c\tag{7.34}$$
Expectation plus Jensen gives $EK(X^n|n)\le nH(X)+|\mathcal X|\log n+c$ (7.35). Divide by n (p. 155).

*Intuition note.* Averaged over a random source, the shortest program is about as long as an optimal code, i.e. the entropy. The extra $O(\log n)$ bits pay for naming the type.

### 7.4 Kolmogorov complexity of integers (p. 155–156)
- Definition: $K(n)=\min_{p:\,U(p)=n}l(p)$ (7.36), i.e. the complexity of the corresponding binary string (p. 155).
- Theorem 7.4.1: $K_U(n)\le K_A(n)+c_A$ (7.37). Theorem 7.4.2: $K(n)\le\log^*n+c$ (7.38) (p. 155–156).
- **Theorem 7.4.3.** Infinitely many integers n have $K(n)>\log n$.
*Proof.* By Lemma 7.3.1, $\sum_n2^{-K(n)}\le1$ (7.39), while $\sum_n2^{-\log n}=\sum\frac1n=\infty$ (7.40). If $K(n)<\log n$ for all $n>n_0$, then $\sum_{n\ge n_0}2^{-K(n)}>\sum_{n\ge n_0}2^{-\log n}=\infty$ (7.41), a contradiction (p. 156).

### 7.5 Algorithmically random and incompressible sequences (p. 156–160)
- Some long strings and integers are simple (e.g. the first million bits of π, $2^{2^{2^{\cdot^{\cdot}}}}$, $(100!)!$). Most are not (p. 156).

**Theorem 7.5.1.** For $X_1,\dots,X_n$ from a Bernoulli(1/2) process,
$$P(K(X_1\dots X_n|n)<n-k)<2^{-k}\tag{7.42}$$
*Proof.* The probability is $\sum_{x:\,K<n-k}p(x)=\sum 2^{-n}=|\{x:K(x|n)<n-k\}|\,2^{-n}$ (7.43–7.44). By Theorem 7.2.4 this is $<2^{n-k}2^{-n}$ (7.45) $=2^{-k}$ (7.46) (p. 157).
- Example: the fraction of length-n strings with complexity below $n-5$ is less than 1/32 (p. 157).

**Definitions.**
- A sequence $x_1\dots x_n$ is **algorithmically random** if $K(x_1\dots x_n|n)\ge n$ (7.47). By counting, for each n at least one such $x^n$ exists (7.48) (p. 157).
- An infinite string is **incompressible** if $\lim_{n\to\infty}\frac{K(x_1\dots x_n|n)}n=1$ (7.49) (p. 157).

**Theorem 7.5.2 (SLLN for incompressible sequences).** If $x_1x_2\dots$ is incompressible, then $\frac1n\sum_{i=1}^nx_i\to\frac12$ (7.50). The proportions of 0s and 1s are almost equal (p. 157).
*Proof.* Let $\theta_n=\frac1n\sum x_i$. By the method of Example 7.2 one can write a program of length $nH_0(\theta_n)+2\log(n\theta_n)+c$ printing $x^n$. Incompressibility gives the lower bound
$$n-c_n\le K(x^n|n)\le nH_0(\theta_n)+2\log n+c'\tag{7.51}$$
with $c_n/n\to0$ and $c'$ independent of n. Hence
$$H_0(\theta_n)>1-\frac{2\log n+c_n+c'}n\tag{7.52}$$
By the graph of $H_0$ (Fig. 7.2),
$$\theta_n\in\left(\tfrac12-\delta_n,\tfrac12+\delta_n\right)\tag{7.53}$$
where $\delta_n$ is chosen so that $H_0(\tfrac12-\delta_n)=1-\frac{2\log n+c_n+c'}n$. (Eq. 7.54 is unreadable in the text layer, p. 159; this form is read off Fig. 7.2.) This implies $\delta_n\to0$ as $n\to\infty$, so $\frac1n\sum x_i\to\frac12$ (p. 158–159).
- The authors state that an incompressible sequence satisfies *all computable statistical tests for randomness*. If it failed one, identifying that test would shorten its description. In this sense the algorithmic test is the ultimate test (p. 159).

**Theorem 7.5.3.** For $X_i$ i.i.d. Bernoulli(θ),
$$\frac1nK(X_1,\dots,X_n|n)\to H_0(\theta)\ \text{in probability}\tag{7.55}$$
(p. 159–160).
*Proof.* Let $\bar X_n=\frac1n\sum X_i$. By (7.23), $K(X_1..X_n|n)\le nH_0(\bar X_n)+2\log n+c$ (7.56). By the weak law, $\bar X_n\to\theta$ in probability, so $\frac1nK-H_0(\theta)\le\epsilon\to0$ (7.57; garbled in text).
Conversely, split sequences by the AEP into typical set $A_\epsilon^{(n)}$ and the rest. The typical set has at least $(1-\epsilon)2^{n(H_0(\theta)-\epsilon)}$ sequences. At most $2^{n(H_0(\theta)-c)}$ typical sequences can have complexity below $n(H_0(\theta)-c)$. Then
$$P\big(K<n(H_0-c)\big)\le\epsilon+\sum_{x^n\in A_\epsilon^{(n)},\,K<n(H_0-c)}p(x^n)\tag{7.58}$$
$$\le\epsilon+\sum 2^{-n(H_0(\theta)-\epsilon)}\tag{7.59}$$
$$\le\epsilon+2^{n(H_0(\theta)-c)}2^{-n(H_0(\theta)-\epsilon)}\tag{7.60}$$
$$=\epsilon+2^{-n(c-\epsilon)}\tag{7.61}$$
This is small for suitable $\epsilon,n,c$ (added step: this needs $c>\epsilon$). Hence (7.62): $\frac1nK(X^n|n)\to H_0(\theta)$ in probability (p. 159–160).

*Intuition note.* A string with no short description looks statistically random, and a random coin-flip string has, with high probability, no short description. For a biased coin the shortest description is about n times the binary entropy.

### 7.6 Universal probability (p. 160–162)
- Feed fair coin flips (a monkey at a keyboard) into a universal Turing machine. Most programs give nothing sensible. Since program p has probability $2^{-l(p)}$, short programs dominate, so outputs are far from uniform: simple strings are more likely than complicated strings of the same length (p. 160).

**Definition.** The universal probability of a string x is
$$P_U(x)=\sum_{p:\,U(p)=x}2^{-l(p)}=\Pr(U(p)=x)\tag{7.63}$$
the probability that a random coin-flip program prints x (p. 160).
- The authors say that, in this framework, Occam's razor ("if many explanations fit the data, choose the simplest") corresponds to choosing the shortest program that produces the string (p. 161).

**Theorem 7.6.1.** For every computer $A$ there is a constant $c'_A$, depending only on $U$ and $A$, such that
$$P_U(x)\ge c'_AP_A(x)\quad\text{for all }x\in\{0,1\}^*\tag{7.64}$$
*Proof.* For every program $p'$ for A printing x there is a program p for $U$ of length at most $l(p')+c_A$ (prefix simulation program). Hence
$$P_U(x)=\sum_{p:\,U(p)=x}2^{-l(p)}\ge\sum_{p':\,A(p')=x}2^{-l(p')-c_A}=c'_AP_A(x)\tag{7.65}$$
(p. 161).
- A computable pmf on binary strings can be seen as produced by some computer acting on random input, so $P_U$ includes a mixture of all computable distributions (p. 161).
- **Bounded likelihood ratio.** If $U$ and $A$ are both universal, $P_U(x)/P_A(x)$ is bounded away from 0 and ∞ for all x. In contrast, for Bernoulli($\theta_1$) vs Bernoulli($\theta_2$) the ratio goes to 0 or ∞. The authors say that apparently $P_U$ can never be completely rejected as the true distribution of data drawn from a computable distribution; the authors add that we cannot reject the possibility that the universe is the output of monkeys at a computer (p. 161–162).
- Section 7.11 will show that $P_U(x)$ is essentially $2^{-K(x)}$ (Eq. 7.66 is garbled in the text layer), so $K(x)$ and $\log\frac1{P_U(x)}$ have equal status (p. 162).
- **Shakespeare example.** Assume the text is 1 million bits. A monkey on a typewriter types it with probability $2^{-1{,}000{,}000}$. At a computer the probability is $2^{-K(\text{Shakespeare})}=2^{-250{,}000}$, "extremely small" but exponentially larger (p. 162).

### 7.7 The halting problem and non-computability of K (p. 162–163)
- Liar paradox ("This statement is false"); Gödel (1931) used self-reference to show that any interesting mathematical system is incomplete. The **halting problem**: for any computational model, there is no general algorithm to decide whether a program halts. It is not a claim about any specific program (p. 162–163).
- **Consequence:** K is not computable. One would have to try all short programs, but at any time some have not halted, and there is no effective way to tell if they will or what they print (p. 163).
- Berry paradox ("the shortest number not nameable in under ten words"): if "describable" means "described by a program for a computer", the number exists but is not computable. Beckenbach's "smallest dull number must be interesting" is a similar problem (p. 163).
- Estimates of K from above converge to the true K as more programs are found halting, but one may never know that no shorter program exists. K still gives a framework for randomness and inference (p. 163).

### 7.8 Chaitin's Ω (p. 164–166)
**Definition.**
$$\Omega=\sum_{p:\,U(p)\text{ halts}}2^{-l(p)}=\Pr(U(p)\text{ halts})\tag{7.67}$$
the probability that the computer halts on a Bernoulli(1/2) random input. By Kraft, $0\le\Omega\le1$ (the text says "between 0 and 1"). $\Omega_n=.\omega_1\dots\omega_n$ is the first n bits (p. 164).

**Properties.**
1. **Ω is not computable.** There is no effective way to check whether arbitrary programs halt, so there is no effective way to compute Ω (p. 164).
2. **Ω is a "Philosopher's Stone".** Knowing n bits of Ω gives an effective procedure (possibly very slow) to decide the truth of any provable or finitely refutable theorem that can be written in under n bits (p. 164).
   - *Procedure.* Run all programs until the sum of masses $2^{-l(p)}$ of halting programs reaches or exceeds $\Omega_n$. Since
$$\Omega-\Omega_n\le2^{-n}\tag{7.68}$$
all further halting contributions total less than $2^{-n}$. So no program of length $\le n$ that has not halted yet will ever halt. This decides halting for all programs of length $\le n$ (p. 164).
   - *Running all programs "in parallel" (dovetailing).* List programs $\Lambda,0,1,00,01,10,11,000,\dots$ (7.69). In cycle 1 run $\Lambda$ one step. In cycle 2 run $\Lambda$ and 0 two steps each. In cycle 3 run the first three programs three steps each, and so on. Any halting program is eventually found to halt (p. 164–165).
   - Many problems are searches for a counterexample: Fermat's last theorem ($x^n+y^n=z^n$ has no integer solution for $n\ge3$, 7.70) and Goldbach's conjecture (a program halts only on an even number that is not a sum of two primes). A program that searches all proofs halts only if it finds a proof (p. 165–166).
   - Another number carries the same information: the real whose ith bit says whether program i halts. It is "very dilute", needing about $2^n$ bits to decide halting for n-bit programs. Ω is the most compact representation because it is incompressible (p. 165).
3. **Ω is algorithmically random.**

**Theorem 7.8.1.** There is a constant c such that
$$K(\omega_1\omega_2\dots\omega_n)\ge n-c\quad\text{for all }n\tag{7.71}$$
*Proof.* Given n bits of Ω we can decide halting for all programs of length $\le n$. With $K(\omega_1\dots\omega_n)$ bits we can compute n bits of Ω, list all halting programs of length $\le n$ with their outputs, and find the first string $x_0$ not on that list. Then $K(x_0)>n$. The program for $x_0$ costs $K(\omega_n)+c$ bits, so
$$K(\omega_n)+c\ge K(x_0)>n\tag{7.72}$$
for all n. So Ω cannot be compressed by more than a constant (p. 166).

*Intuition note.* Ω packs the answers to all halting questions into one real number so densely that no pattern in its bits can be used to shorten it. Knowing $n$ bits of Ω settles the halting of all programs of length $\le n$ (p. 164).

### 7.9 Universal gambling (p. 166–168)
- Gambler bets sequentially on $x\in\{0,1\}^*$ at fair odds, 2-for-1 per bit (the text layer reads "a-for-l", and $2^{l(x)}$ below fits 2-for-1). He knows nothing of the origin of the sequence. If he knew x in advance he could multiply wealth by $2^{l(x)}$. With bet $b(x)$, $\sum b(x)=1$, wealth is
$$S(x)=2^{l(x)}b(x)\tag{7.73}$$
(p. 166–167).
- **Universal gambling:** $b(x)=2^{-K(x)}$. The bets sum to
$$\sum_xb(x)=\sum_x2^{-K(x)}\le\sum_{p\ \text{halts}}2^{-l(p)}=\Omega\le1\tag{7.74}$$
so not all money is used; the rest is thrown away. Wealth on $x=0110$ is $2^4b(0110)$ plus winnings from bets on sequences extending 0110 (p. 167).

**Theorem 7.9.1.**
$$\log S(x)+K(x)\ge l(x)\tag{7.75}$$
the counterpart of the gambling conservation theorem $W^*+H=\log m$ from Chapter 6.
*Proof.* With $x'\sqsupseteq x$ meaning x is a prefix of $x'$,
$$S(x)=\sum_{x'\sqsupseteq x}2^{l(x')}b(x')\ge2^{l(x)}2^{-K(x)}\tag{7.76}$$
Take logarithms (p. 167).
- For sequences of finite complexity, $S(x)\ge2^{l(x)-K(x)}=2^{l(x)-c}$ (7.77). Since $2^{l(x)}$ is the most winnable in $l(x)$ fair gambles, this does asymptotically as well as knowing the sequence. For the digits of π, $S_n=S(\pi_1\dots\pi_n)\ge2^{n-c}$ (p. 167–168).
- For a Bernoulli(p) process:
$$S(X_1\dots X_n)\ge2^{n-nH_0(\bar X_n)-2\log n-c}\approx2^{n\left(1-H_0(p)-2\frac{\log n}n-\frac cn\right)}\tag{7.78}$$
the same to first order as the rate when the distribution is known (Chapter 6) (p. 168).

### 7.10 Occam's razor (p. 168–169)
- **Laplace's approach** (Laplace's view). Model sunrise as Bernoulli(θ) with θ uniform on [0,1]. The posterior probability of sunrise on day n+1 after n sunrises is
$$P(X_{n+1}=1|X_n=\dots=X_1=1)=\frac{\int_0^1\theta^{n+1}d\theta}{\int_0^1\theta^nd\theta}=\frac{n+1}{n+2}\tag{7.79–7.80}$$
(p. 168).
- **Universal-probability approach** (the authors'). The conditional probability that the next bit is 1 after $1^n$ is the ratio of the probability of sequences starting $1^n1$ to those starting $1^n$. The simplest programs carry most probability, so approximate by the program "Print 1s forever":
$$\sum_yp(1^n1y)\approx p(1^\infty)=c>0\tag{7.81}$$
Any program printing $1^n0\dots$ describes n, so its length should be at least $K(n)$, which for most n is about $\log n+O(\log\log n)$. Ignoring second-order terms,
$$\sum_yp(1^n0y)\approx p(1^n0)\approx2^{-\log n}=\frac1n\tag{7.82}$$
so
$$p(0|1^n)=\frac{p(1^n0)}{p(1^n0)+p(1^\infty)}\approx\frac1{cn+1}\tag{7.83}$$
which the book calls similar to "the result $p(0|1^n)=1/(n+1)$ derived by Laplace" (p. 169). Note (ours): (7.80) itself gives sunrise probability $(n+1)/(n+2)$, so the complementary event has probability $1/(n+2)$ (p. 168).
- This is a special case of Occam's razor: weight explanations by complexity. The authors' example: general relativity is easier to accept than a Newtonian law with an added $c/r^3$ correction to explain Mercury's perihelion, since it explains more with fewer assumptions (p. 169).

### 7.11 Kolmogorov complexity and universal probability (p. 169–175)
Recall $K(x)=\min_{p:U(p)=x}l(p)$ (7.84) and $P_U(x)=\sum_{p:U(p)=x}2^{-l(p)}$ (7.85) (p. 169).

**Theorem 7.11.1.** There is a constant c, independent of x, with
$$2^{-K(x)}\le P_U(x)\le c\,2^{-K(x)}\tag{7.86}$$
for all x. Equivalently,
$$K(x)-c'\le\log\frac1{P_U(x)}\le K(x)\tag{7.87}$$
(p. 170). So $K_U(x)$ and $\log\frac1{P_U(x)}$ are essentially equivalent complexity measures, in parallel with $H(X)$ and $\log\frac1{p(x)}$ in Shannon theory (Shannon code length $\lceil\log\frac1{p(x)}\rceil$) (p. 170).
- The upper bound in (7.87) is obvious. The lower bound is "surprising": there are infinitely many programs for x (padding with irrelevant instructions), yet $P_U(x)$ is determined within a constant by the largest term $2^{-K(x)}$ (p. 170).
- Why it is less surprising: for any *computable* pmf, a Shannon–Fano code gives a description of length $\log\frac1{p(x)}+c$. $P_U$ is not computable, so a tree construction is needed (p. 170–171).

*Proof, first inequality.* If $p^*$ is the shortest program for x, then $P_U(x)\ge2^{-l(p^*)}=2^{-K(x)}$ (7.88; garbled, reconstructed) (p. 171).

*Proof, second inequality* (shown as $K(x)\le\log\frac1{P_U(x)}+c$, 7.89). Goal: a short program for strings of high $P_U$. Huffman or Shannon–Fano coding on $P_U$ cannot be run, so build a code tree directly (not optimal, but within a constant) (p. 171).
1. **Run all programs** by dovetailing (list in 7.90, as in 7.8). Produce, in order of halting, triplets $(p_k,x_k,n_k)$ with
$$n_k=\left\lceil\log\frac1{\hat P_U(x_k)}\right\rceil\tag{7.91}$$
$$\hat P_U(x_k)=\sum_{(p_i,x_i):\,x_i=x_k,\,i\le k}2^{-l(p_i)}\tag{7.92}$$
$\hat P_U(x_k)\uparrow P_U(x)$ on times when $x_k=x$ (p. 172).
2. **Winnow.** Remove triplets that repeat an earlier (x, n) pair, so the $n_i$ for a given x are distinct (at most one node per level per x). Assign each surviving triplet to the first available node at level $n'_i+1$. Once assigned, its descendants become unavailable (prefix-free) (p. 172).
3. **Example (7.93–7.94, Fig. 7.3).**
   - $(10111,1110,5)$: $n_1=5$, as $\hat P(x_1)\ge2^{-5}$.
   - $(11,10,2)$: $n_2=2$ ($\ge2^{-2}$).
   - $(0,1110,1)$: $n_3=1$, as $\hat P\ge2^{-1}+2^{-5}\ge2^{-1}$.
   - $(1010,1111,4)$: $n_4=4$ ($\ge2^{-4}$).
   - $(101101,1110,1)$: $n_5=1$, as $\hat P\ge2^{-1}+2^{-5}+2^{-6}\ge2^{-1}$.
   - $(100,1,3)$: $n_6=3$ ($\ge2^{-3}$).
   - String 1110 appears three times (positions 1, 3, 5) but $n_3=n_5$: $\hat P(1110)$ has not jumped enough, so the fifth triplet is cut. The winnowed list displayed in (7.94) has five triplets, followed by dots (p. 172–173).
4. **Enough nodes (Kraft).** Assignment is possible iff the Kraft inequality holds. Split the sum by output string:
$$\sum_{k=1}^\infty2^{-(n_k+1)}=\sum_{x}\sum_{k:\,x_k=x}2^{-(n_k+1)}\tag{7.95}$$
The inner sum is
$$\sum_{k:x_k=x}2^{-(n_k+1)}=2^{-1}\sum_{k:x_k=x}2^{-n_k}\tag{7.96}$$
$$\le2^{-1}\left(2^{\lfloor\log P_U(x)\rfloor}+2^{\lfloor\log P_U(x)\rfloor-1}+2^{\lfloor\log P_U(x)\rfloor-2}+\cdots\right)\tag{7.97}$$
$$=2^{-1}2^{\lfloor\log P_U(x)\rfloor}\left(1+\tfrac12+\tfrac14+\cdots\right)\tag{7.98}$$
$$=2^{-1}2^{\lfloor\log P_U(x)\rfloor}\cdot2\tag{7.99}$$
$$\le P_U(x)\tag{7.100}$$
(7.97) holds because the $n_k$ for a given x are distinct integers. Hence
$$\sum_k2^{-(n_k+1)}\le\sum_x\sum_{k:x_k=x}2^{-(n_k+1)}\le\sum_xP_U(x)\le1\tag{7.101}$$
and the tree exists (p. 174).
5. **Describing x.** Let $\tilde p$ be the lowest-depth node printing x; by construction $l(\tilde p)\le\log\frac1{P_U(x)}+2$. To print x, give $\tilde p$ (the path) and tell the computer to run the same simulation and build the same tree. When node $\tilde p$ is assigned, it halts and prints x. In the example, 1110 is described by the path 01 (node $(p_3,x_3,n_3)$) and 1111 by 00001 (p. 174).
6. **Caveat.** This is an effective procedure to *reconstruct* x, but there is no effective procedure to *find* the lowest-depth node. All that is proved is that a tree with a node for x at level $\lceil\log\frac1{P_U(x)}\rceil+1$ exists (p. 174).
7. **Conclusion.** The program has length $l(\tilde p)+c$ with
$$l(\tilde p)\le\left\lceil\log\frac1{P_U(x)}\right\rceil+1\tag{7.102}$$
so
$$K(x)\le\left\lceil\log\frac1{P_U(x)}\right\rceil+c\tag{7.103}$$
(p. 174–175).

**Skip path:** carry forward Theorem 7.11.1, $K(x)\approx\log\frac1{P_U(x)}$ up to an additive constant.

*Intuition note.* Adding up the probability of all programs that print x gives almost the same number as the shortest program alone. Having many longer programs adds only a constant factor.

### 7.12 The Kolmogorov sufficient statistic (p. 175–178)
- Take x from a Bernoulli(θ) process. $K(x^n|n)\approx nH_0(\theta)+\log n+c$, much less than n when $\theta\ne\frac12$, so $x^n$ has structure. But the shortest program $p^*$ shows no structure, because its own shortest description is about as long as $p^*$ (otherwise $p^*$ could be compressed) (p. 175).
- Hint: $p^*$ is a two-stage description ("k ones; the ith such sequence"). The first stage (k, about $\log(n+1)$ bits) defines a set $S=\{x\in\{0,1\}^n:\sum x_i=k\}$ and holds all the structure. The second stage costs $\log|S|=\log\binom nk\approx nH_0(\bar x_n)\approx nH_0(\theta)$ bits and shows nothing unusual. $x^n$ is maximally complex given the first stage (p. 175).

**Definition (structure function).** For $x\in\{0,1\}^n$,
$$K_k(x^n|n)=\min_{\substack{p:\,l(p)\le k\\ U(p,n)=S\\ x^n\in S\subseteq\{0,1\}^n}}\log|S|\tag{7.104}$$
Here $U(p,n)=S$ means the program prints the indicator function of S. It is the log-size of the smallest set containing $x^n$ describable in at most k bits (p. 175–176).

**Definition (minimal sufficient statistic).** For a small constant c, let $k^*$ be the least k with
$$K_k(x^n|n)+k\le K(x^n|n)+c\tag{7.105}$$
Let $S^{**}$ be the corresponding set and $p^{**}$ the program printing its indicator function. Then $p^{**}$ is a **Kolmogorov minimal sufficient statistic** for $x^n$ (p. 176).
- Programs $p^*$ for sets $S^*$ with $K_k(x^n|n)+k=K(x^n|n)$ (7.106) are all "sufficient" (x is maximally complex given $S^*$). The minimal one is the shortest of them. Equality is up to a large constant depending on the computer (p. 176).
- $S^{**}$ captures all the structure. The rest is the index within $S^{**}$, i.e. the randomness (p. 176).
- **Parallel to statistical sufficiency:** T is sufficient for θ if $\theta\to T(X)\to X$ is a Markov chain (7.107). Here $p^{**}$ is sufficient for the "structure" and the remainder is essentially independent of it (p. 176).
- **Shape of the structure function (Fig. 7.4).** At $k=0$ only $\{0,1\}^n$ is describable, so the log set size is n. As k grows the size drops rapidly until $k+K_k(x^n|n)\approx K(x^n|n)$ (7.108). Then each extra bit of k halves the set, along a line of slope −1 until $k=K(x^n|n)$. For $k\ge K(x^n|n)$ the smallest set is $\{x^n\}$, so $K_k=0$ (p. 176–177).
- **Examples** (p. 177–178):
  1. Bernoulli(θ): give the number of 1s, then the index. $k^{**}\approx\log n$ (Fig. 7.5). For special θ such as 1/3 or $e/\pi^2$, $p^{**}$ describes θ and $k^{**}=c$.
  2. First-order binary Markov chain: $p^{**}$ describes the Markov type (counts of 00, 01, 10, 11). $k^*\approx2\log n$, since two elements of the conditional joint type determine the others.
  3. "Mona Lisa": a gray circle on white, gray level Bernoulli(θ) (Fig. 7.6). $p^{**}$ gives the circle's position, size and average gray level, about $\log n$ bits each, so $k^*\approx3\log n$.

### Chapter summary and problems (p. 178–181)
The chapter summary restates the definitions and theorems above (7.109–7.121). The problems are listed under "Exercises worth doing". Historical notes (p. 182) are not part of the argument and are summarised in Reading notes.

## Toy example (ours, not from the text)
Take n = 16 and a string x with exactly k = 2 ones (constants such as the fixed program overhead c are ignored).
- Two-stage description (as in Example 7.2.8, with n known): the index among strings with 2 ones needs $\log_2\binom{16}2=\log_2120$ bits. Since $2^6=64<120\le128=2^7$, that is 7 bits.
- k can take 17 values (0..16), so it needs 5 bits ($2^4=16<17\le32$). Total $5+7=12$ bits $<16$. So x is compressible: $K(x|n)\lesssim12+c$.
- Counting (Theorem 7.2.4): fewer than $2^{12}=4096$ strings have a description shorter than 12 bits. There are $2^{16}=65536$ strings, and $4096/65536=1/16=2^{-4}$. This matches Theorem 7.5.1 with $k=4$: $P(K<16-4)<2^{-4}$.
- So at most 1 in 16 strings is that compressible. Strings with exactly two ones number just 120 of the 65536, about 0.18%, and they are among the compressible ones.

## Concepts
- [[kolmogorov-complexity]] — K(x): length of the shortest program printing x (and halting) on a universal computer; the shortest-program definition (7.1) (p. 147)
- [[conditional-kolmogorov-complexity]] (new) — $K(x|l(x))$: shortest program given the length of x as side information (p. 148)
- [[universal-computer]] (new) — a computer, e.g. a universal Turing machine, that can mimic any other; makes K machine-independent up to a constant (p. 146, 148)
- [[invariance-theorem]] (new) — $K_U(x)\le K_A(x)+c_A$ (7.3) (p. 148)
- [[prefix-code-kraft]] — halting programs form a prefix-free set, so $\sum2^{-l(p)}\le1$ (Lemma 7.3.1) (p. 154)
- [[incompressibility-algorithmic-randomness]] — algorithmically random if $K(x^n|n)\ge n$; incompressible if $K/n\to1$ (p. 157)
- [[entropy]] — $H(X)$; here $\frac1n EK(X^n|n)$ tends to it for i.i.d. sources (p. 154)
- [[typical-set-aep]] — used in the lower bound of Theorem 7.5.3 (p. 159–160)
- [[algorithmic-probability-solomonoff]] — universal probability $P_U(x)$ of (7.63); the authors do not use the name "Solomonoff" in the text pages, only in the Historical Notes (p. 160, 182)
- [[halting-problem]] (new) — no algorithm decides, for all programs, whether they halt; makes K uncomputable (p. 162–163)
- [[chaitin-omega]] (new) — $\Omega=\Pr(U(p)\text{ halts})$; non-computable, algorithmically random, a "Philosopher's Stone" (p. 164–166)
- [[dovetailing]] (new) — running all programs in rounds, giving each more steps, so every halting one is eventually detected (p. 164–165)
- [[occams-razor]] (new) — prefer the simplest explanation; here, shortest program / highest universal probability (p. 161, 169)
- [[kelly-criterion-doubling-rate]] — universal gambling bets $2^{-K(x)}$ on string x; $\log S(x)+K(x)\ge l(x)$ (p. 166–167)
- [[kolmogorov-structure-function]] (new) — $K_k(x^n|n)$: log-size of the smallest set containing $x^n$ describable in $\le k$ bits (7.104) (p. 175)
- [[kolmogorov-sufficient-statistic]] (new) — the shortest program describing a set that captures all of x's structure, with x maximally complex within it (p. 176)
- [[minimum-description-length]] — mentioned in Historical Notes as "close in spirit" to the Kolmogorov sufficient statistic (p. 182)
- [[universal-coding]] — the authors say the shortest program acts as a universal code, uniformly good for all distributions (p. 144)

## Canonical instances
- [[three-strings-example]] — periodic string, √2−1 expansion, biased random string, fair-coin string (p. 145)
- [[gotham-weather]] — Markov model gives $K\approx n/5+O(\log n)$ (p. 151)
- [[mandelbrot-set]] — complex-looking object of near-zero K (p. 152)
- [[mona-lisa-compression]] — K bounded by about n/3 (p. 152); circle image has $k^*\approx3\log n$ (p. 178)
- [[laplace-sunrise]] — rule of succession $(n+1)/(n+2)$ vs the universal-probability argument (p. 168–169)
- [[monkey-shakespeare]] — typewriter $2^{-10^6}$ vs computer $2^{-K}=2^{-250{,}000}$ (p. 162)
- [[berry-paradox]] — "shortest number not nameable in under ten words" (p. 163)
- [[fermat-goldbach-halting-programs]] — conjectures encoded as halting questions, decided by Ω bits (p. 165–166)

## Bridges (candidates)
- [same-math] Lemma 7.3.1 (halting programs satisfy Kraft) ↔ information-theory: prefix codes and the Kraft inequality — the proof applies Theorem 5.2.1 directly.
- [structural-analogy] $K(x)\approx\log\frac1{P_U(x)}$ ↔ Shannon code length $\log\frac1{p(x)}$ — the text itself draws this parallel (p. 170).
- [structural-analogy] Universal gambling, $\log S+K\ge l$ ↔ Kelly gambling, $W^*+H=\log m$ — the text calls it the counterpart.
- [same-math] Laplace's $(n+1)/(n+2)$ ↔ Bayesian prediction with a uniform prior on θ (the Beta-integral calculation (7.79–7.80)).
- [structural-analogy] Kolmogorov sufficient statistic ↔ statistics: sufficient statistics, $\theta\to T(X)\to X$ — the text draws the parallel via a Markov chain.
- [structural-analogy] Kolmogorov structure function / minimal sufficient statistic ↔ MDL: model plus data cost — the Historical Notes call MDL close in spirit.
- [metaphor] Universal probability as "monkeys at a computer" ↔ priors that favor simple structure in inductive inference.

## Questions this raises
- Since K is not computable, what practical compressors give useful upper bounds, and how can we tell how far they are from K?
- Theorem 7.3.1 shows $\frac1nEK\to H$ for i.i.d. sources. What happens for sources with memory (entropy rate)?
- The constants hide machine dependence. For realistic string lengths, how large can the constant $c_A$ become before the theory says nothing?
- Is $P_U(x)\approx2^{-K(x)}$ a usable prior in practical inference, given $P_U$ is not computable?

## Exercises worth doing
- Ex. 1 (p. 180) — subadditivity of K for a pair of strings (the printed statement reads $K(n)$ where $K(x)$ is probably meant); practice with concatenating programs — difficulty: easy
- Ex. 2 (p. 180) — K of integers: $K(n)\le\log n+2\log\log n+c$, subadditivity under addition, and a case where the sum is simpler than the parts — difficulty: medium
- Ex. 3 (p. 180) — complexity of images (line, square, two lines) to first order — difficulty: easy
- Ex. 4 (p. 181) — "monkeys on a computer": probability estimates that a random program prints given prefixes — difficulty: medium
- Ex. 6 (p. 181) — computers do not reduce entropy: the output X = U(P) has $H(X)=\infty$ — difficulty: hard
- Ex. 7 (p. 181) — law of large numbers for ternary algorithmically random sequences — difficulty: hard

## Reading notes
- The PDF is the **1991 first edition** (running line on p. 144: Copyright 1991, John Wiley & Sons; Print ISBN 0-471-06259-6), not the 2nd edition named in the citation. The unit metadata warns that chapter content and numbering differ from the 2006 edition; I cannot check this from these pages.
- **Page offset:** printed = pdf − 22 (the page printed as 144 is PDF page 166). References use printed pages.
- The text layer is heavily garbled in equations. I checked against the images for pp. 147, 150–151, 153–154, 156–160, 167–169, 172–181. Not every page has an image. Pages 144–146, 148–149, 152, 155, 161–166, 170–171, 182 are text-layer only, so details there rely on the text and on context.
- Eq. 7.2, 7.7, 7.57, 7.54, 7.66, 7.88 were garbled or unreadable in the text layer; I reconstructed them from the surrounding statements and the chapter summary (p. 178–180) and flagged them. In string 2 (p. 145) the text layer reads "fi − 1" where I read $\sqrt2-1$.
- The text layer's page running header on the problems page reads 183, while the image shows 181 (printed). Problem 1 as printed reads $K(x,y)\le K(n)+K(y)+c$; "K(n)" is probably a misprint for "K(x)". The Mona Lisa bound (7.19) is garbled as "i + c" in the text layer; I read it as $n/3+c$ from the "factor of 3" statement.
- Eq. 7.83 and its text: the book says Laplace's result is $p(0|1^n)=1/(n+1)$ (p. 169), while its own calculation (7.80) gives $1/(n+2)$ for the complementary event. I report both as printed.
- Eq. 7.97 as printed has $2^{\lfloor\log P_U(x)\rfloor}$ terms. I verified this is consistent with $n_k\ge\lceil\log\frac1{P_U(x)}\rceil$.
- Historical Notes (p. 182) credit Kolmogorov, Solomonoff and Chaitin for the original ideas. They also mention Martin-Löf (random sequences), Gács and Levin (universal probability), Chaitin (proofs), Schnorr, V'yugin (sequences that reveal structure slowly), Zurek (Maxwell's demon) and Rissanen (MDL). The structure function was defined by Kolmogorov in 1973 and not published. I did not expand on these.
