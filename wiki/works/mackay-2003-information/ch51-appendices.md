---
id: mackay-2003-information/ch51-appendices
work: mackay-2003-information
unit: Part VII Appendices (A Notation, B Some Physics, C Some Mathematics)
pages: 597-612
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Part VII Appendices: notation, phase transitions, finite fields, eigenvectors, perturbation theory, big numbers

## L0 — One line
The appendices give the book's notation and four toolkits: partition functions and phase transitions, Galois fields for linear codes, eigen-analysis of (transition) matrices with first- and second-order perturbation formulas, and a table of reference numbers.

## L1 — The gist (≤ 120 words)
These appendices collect notation and background tools; the author notes that perturbation theory is not used in the book. A fixes notation (log is base 2, ln is natural, $\mathbb{1}[S]$ is the truth function, and so on). B uses a toy spin system to show what a phase transition is: a sharp bend in $\ln Z$ that needs infinitely many states, and where "typicality" fails. C explains Galois fields (the arithmetic behind linear codes over larger alphabets), eigenvectors of symmetric, non-negative and transition-probability matrices (the invariant distribution), and a derivation of perturbation theory for non-symmetric matrices. C ends with a table of large and small numbers in powers of 2 and 10.

**Prerequisites:** matrices and eigenvalues; Taylor expansion; logarithms and exponentials; modular arithmetic; basic probability.

## L2 — Key ideas (5–10 bullets)
- Conventions: $\log$ is base 2, $\ln$ is natural, a hat marks an estimate, a prime means a derivative only where a function is meant, and $\mathbb{1}[S]$ is the truth function (pp. 598–600).
- A system at inverse temperature $\beta$ has Boltzmann probabilities $P(\mathbf{x}\mid\beta)=e^{-\beta E(\mathbf{x})}/Z(\beta)$. Derivatives of $\ln Z$ give energy fluctuations and heat capacity (pp. 601–602).
- A finite system has a smooth $Z(\beta)$, so phase transitions need infinitely many states. Joining $N$ independent copies only scales $\ln Z$ by $N$, so it creates no transition (pp. 601–602).
- In the toy coupled-spin system the asymptotes of $\ln Z$ cross at $\beta_c=\ln 2/\epsilon$. The energy variance there is about $N^2\epsilon^2/4$, against a smooth, peak-free variance for independent spins (pp. 602–603).
- Near a critical point, typicality (Chapter 4) fails: $\ln 1/P(\mathbf{x})$ is not close to the entropy, and the energy fluctuates a lot (pp. 602, 604).
- Galois fields GF($p^m$) are the finite fields. They suit linear codes because group structure under both operations avoids symmetry-breaking (pp. 605–606).
- A transition probability matrix has left-eigenvector $\mathbf{n}$ (all ones) with eigenvalue 1. Its right-eigenvector is the invariant distribution, and non-ergodic chains show extra eigenvalues of magnitude 1 (pp. 607–609).
- First-order eigenvector and second-order eigenvalue perturbation formulas are derived for non-symmetric matrices, assuming non-degenerate eigenvalues (pp. 609–611).

## L3 — Walkthrough

### A — Notation (pp. 598–600)
- $P(A\mid B,C)$ means "the probability of A given B and C" (p. 598).
- $\log x=\log_2 x$ and $\ln x=\log_e x$. A hat (as in $\hat s$) denotes a guess or estimator (p. 598).
- $\int f(u)\,du$ and $\int du\,f(u)$ are the same (p. 598).
- Product: $\prod_{n=1}^N n = N! = \exp\left[\sum_{n=1}^N \ln n\right]$ \tag{A.1}. The author names a free index as the lower-case version of its range, so $n$ runs to $N$ and $m$ to $M$ (p. 598).
- Combinations (number of unordered selections of $n$ from $N$): $\binom{N}{n}=\frac{N!}{(N-n)!\,n!}$ \tag{A.2} (p. 598).
- Gamma function: $\Gamma(x)\equiv\int_0^\infty du\,u^{x-1}e^{-u}$ for $x>0$. It extends the factorial: $\Gamma(x+1)=x\Gamma(x)$, and $\Gamma(x+1)=x!$ for integers. Digamma: $\Psi(x)\equiv\frac{d}{dx}\ln\Gamma(x)$ (p. 598).
- For large $x$ (practical range $0.1\le x\le\infty$): $\ln\Gamma(x)\simeq (x-\tfrac12)\ln x - x+\tfrac12\ln 2\pi+O(1/x)$ \tag{A.3}. For small $x$ ($0\le x\le 0.5$): $\ln\Gamma(x)\simeq\ln\frac1x-\gamma_e x+O(x^2)$ \tag{A.4}, where $\gamma_e$ is Euler's constant (pp. 598–599).
- $H_2^{-1}(h)$ is the inverse function of $h=H_2(x)$, like $\sin^{-1}$. The author avoids writing $\sin^2 x$ because it invites confusion (p. 599).
- Prime: $f'(x)\equiv\frac{d}{dx}f(x)$ \tag{A.5}; a dot is a time derivative, $\dot x\equiv\frac{d}{dt}x$ \tag{A.6}. Rule: a prime on something that could be a function means differentiation; otherwise it means "another variable" (e.g. $x'$, $n'$) (p. 599).
- Error function used: $\Phi(z)\equiv\int_{-\infty}^z \exp(-z^2/2)/\sqrt{2\pi}\,dz$ \tag{A.7}, the cumulative standard normal (p. 599).
- $\mathcal{E}[r]$ or $\langle r\rangle$ is the expected value. $|\mathcal{A}|$ is a set's size and $|x|$ an absolute value. $[\mathbf{A}|\mathbf{P}]$ puts matrices side by side. $\mathbf{x}^{\mathsf T}$ is the transpose, and vectors are normally columns (p. 599).
- $\mathrm{Trace}\,\mathbf{M}=\sum_i M_{ii}$ \tag{A.9}. $\delta_{mn}$ is the identity matrix ($1$ if $m=n$, else $0$), also written $\mathbf{I}$ or $\mathbf{1}_K$ (p. 600).
- Delta function: $\int dx\,f(x)\delta(x)=f(0)$ \tag{A.10}. The truth function is $\mathbb{1}[S]$, equal to 1 if $S$ is true and 0 otherwise. Example: the number of positive elements of $T=\{-2,1,3\}$ is $\sum_{x\in T}\mathbb{1}[x>0]$ \tag{A.11} (p. 600).
- In algorithms, $x:=y$ is an assignment. $x=y$ is a proposition (p. 600).

### B.1 About phase transitions (pp. 601–604)
**Setup.** A system with states $\mathbf{x}$ in contact with a heat bath at temperature $T=1/\beta$ has
$$P(\mathbf{x}\mid\beta)=\frac{1}{Z(\beta)}\exp(-\beta E(\mathbf{x})),\tag{B.1}$$
$$Z(\beta)=\sum_{\mathbf{x}}\exp(-\beta E(\mathbf{x})).\tag{B.2}$$
The partition function $Z$ is the normalizing sum. $\beta$ is an exchange rate between entropy and energy: $1/\beta$ is the energy that must be given to the bath to raise its entropy by one nat (p. 601). $Z$ may also depend on other parameters, such as volume $V$ (p. 601).

**Argument.**
1. For a finite number of states, $Z(\beta)$ is a sum of exponentials, so it and all its derivatives are continuous (p. 601).
2. Phase transitions occur at critical points, values of $\beta$ and $V$ where derivatives of $Z$ jump or diverge. So only systems with an infinite number of states can show phase transitions (p. 601). They may appear as $N\to\infty$; real systems have $N$ like $10^{23}$ (p. 601).
3. For $N$ independent identical systems, $Z_{(N)}(\beta)=[Z_{(1)}(\beta)]^N$ \tag{B.3}, so $\ln Z_{(N)}(\beta)=N\ln Z_{(1)}(\beta)$ \tag{B.4}. Copying only scales energy and heat capacity by $N$, so a system with no transitions gives none when scaled up. The author concludes: only systems with long-range correlations show phase transitions (pp. 601–602).
4. Long-range correlations do not need long-range couplings. A magnet has only nearest-neighbour couplings, yet they can create long-range order (p. 602).

*Intuition note.* Making many separate copies of a system never creates a transition, because $\ln Z$ just grows in proportion to $N$. A transition needs long-range correlations among the parts. (pp. 601–602)

**Why divergences matter.** Derivatives of $\ln Z$ give heat capacity (second derivative) and energy fluctuations. If the second derivative diverges at $1/\beta$, the heat capacity diverges, so the system can absorb or release energy without changing temperature (ice melting in ice water). Its energy then fluctuates a lot, unlike the usual law-of-large-numbers behaviour, where energy varies by one part in $\sqrt N$ (p. 602).

**Toy system with a transition.** $N$ coupled spins, $\mathbf{x}\in\{0,1\}^N$:
$$E(\mathbf{x})=\begin{cases}-N\epsilon & \mathbf{x}=(0,0,\dots,0)\\ 0&\text{otherwise.}\end{cases}\tag{B.5}$$
Contrast: $N$ independent spins with $E^0(\mathbf{x})=\epsilon\sum_n(2x_n-1)$ \tag{B.6}. It also has one ground state, of energy $-N\epsilon$, and roughly $2^N$ states with energy very close to 0. So the low- and high-temperature properties of the two systems are virtually identical (p. 602).
$$Z(\beta)=e^{\beta N\epsilon}+2^N-1\tag{B.7}$$
$$\ln Z(\beta)=\ln\left(e^{\beta N\epsilon}+2^N-1\right)\tag{B.8}$$
with low-temperature behaviour $\ln Z\simeq N\beta\epsilon$ as $\beta\to\infty$ \tag{B.9} and high-temperature behaviour $\ln Z\simeq N\ln 2$ as $\beta\to0$ \tag{B.10} (p. 602). The asymptotes intersect at
$$\beta=\frac{\ln 2}{\epsilon}\tag{B.11}$$
and as $N\to\infty$ the graph of $\ln Z$ bends ever more sharply there (Fig. B.1b). The second derivative of $\ln Z$ is the energy variance. At $\beta=\ln2/\epsilon$ it peaks at roughly
$$\frac{N^2\epsilon^2}{4},\tag{B.12}$$
which corresponds to the system spending half its time in the ground state and half in the other states. The heat capacity there is proportional to $N^2$, so the heat capacity per spin is proportional to $N$ and is infinite for infinite $N$. Away from transitions, capacity per atom is a finite number (p. 603). For independent spins, $\ln Z$ changes gradually between asymptotes for any $N$, and the energy variance has no peak. It is largest at high temperature and scales linearly with $N$ (Fig. B.2, p. 603).

*Intuition note.* In the coupled toy, one special state competes with $2^N-1$ ordinary ones. At $\beta_c$ they carry roughly equal weight. The tilt from one regime to the other becomes abrupt as $N$ grows, and the energy then switches between $-N\epsilon$ and 0. (pp. 602–603)

**More generally.** In a first-order transition one or more order-parameters change discontinuously. In a continuous transition all of them change continuously. An order-parameter is a scalar function of the state, or more precisely the expectation of one (pp. 603–604). Near a critical point, typicality (Chapter 4) does not hold. At its critical point the toy system has a 50% chance of energy $-N\epsilon$ and roughly a $1/2^{N+1}$ chance of each other state. So $\ln 1/P(\mathbf{x})$ is not likely to be close to the entropy, unlike $N$ i.i.d. components. Information content and energy are closely related: if typicality holds, the energy has negligible fluctuations, and vice versa (p. 604).

### C.1 Finite field theory (pp. 605–606)
**Definitions.** A field $F=\{0,F'\}$ satisfies three conditions (p. 605):
1. $F$ is an Abelian group under $+$ with identity 0. Abelian means $a+b=b+a$.
2. $F'$ is an Abelian group under $\cdot$, and multiplying anything by 0 gives 0.
3. The distributive rule holds: $(a+b)\cdot c=a\cdot c+b\cdot c$.

The reals are a field. A Galois field GF($q$) has finitely many elements $q$. A unique one exists for any $q=p^m$ ($p$ prime, $m$ a positive integer), and there are no other finite fields (p. 605).
- GF(2): arithmetic modulo 2 (Table C.1). GF($p$): arithmetic modulo $p$ (p. 605).
- GF(4) (Table C.2) is not arithmetic modulo 4. Elements $0,1,A,B$ correspond to polynomials $0,1,x,x+1$ (bit patterns 00, 01, 10, 11). Addition and multiplication are on polynomials over GF(2), modulo $x^2+x+1$. Example: $B\cdot B=x^2+(1+1)x+1=x=A$ (p. 605).
- GF(8): elements $0,1,A,\dots,F$ map to polynomials over GF(2) modulo $x^3+x+1$ (binary 000 to 111, $A=x$, $C=x^2$, $F=x^2+x+1$). The multiplication table is printed (p. 606).

**Why they suit linear codes.** Generalize a binary generator matrix $\mathbf{G}$ and vector $\mathbf{s}$ to a larger element set. For a symmetric channel it is convenient if $\mathbf{Gs}$ gives all elements equal probability for random $\mathbf{s}$. This is easiest to guarantee if the elements form a group under both operations, since then no symmetry is broken. Multiplying two random elements of a multiplicative group gives all elements with equal probability. This fails for the integers, where composite numbers arise more often. Galois fields avoid such effects by definition (p. 606).

*Intuition note.* A code over an alphabet of $q$ symbols is most convenient with arithmetic in which random inputs give uniformly random outputs. The author says this is easiest to guarantee with a group structure, as in fields, and that integer multiplication does not give it. (p. 606)

### C.2 Eigenvectors and eigenvalues (pp. 606–609)
**Definitions.** A right-eigenvector of square $\mathbf{A}$ is a non-zero $\mathbf{e}_R$ with $\mathbf{A}\mathbf{e}_R=\lambda\mathbf{e}_R$ \tag{C.1}. A left-eigenvector satisfies $\mathbf{e}_L^{\mathsf T}\mathbf{A}=\lambda\mathbf{e}_L^{\mathsf T}$ \tag{C.2}. Eigenvalues and eigenvectors may be real or complex, and an eigenvalue may be zero (p. 606). Statements for right-eigenvectors also apply to left (p. 606):
- Two or more linearly independent right-eigenvectors with the same eigenvalue make it degenerate (repeated). Any linear combination of them is again an eigenvector with that eigenvalue.
- The principal right-eigenvector is the one with the largest eigenvalue.
- If a real matrix has complex eigenvalue $\lambda=x+yi$, it also has one for $\lambda^*=x-yi$.

**Symmetric real $N\times N$ matrices** (p. 607):
1. All eigenvalues and eigenvectors are real.
2. Every left-eigenvector is a right-eigenvector with the same eigenvalue, and vice versa.
3. $N$ orthonormal eigenvectors exist, $\mathbf{e}^{(a)}\cdot\mathbf{e}^{(b)}=\delta_{ab}$ \tag{C.3}, and $\mathbf{A}=\sum_{a=1}^N\lambda_a[\mathbf{e}^{(a)}][\mathbf{e}^{(a)}]^{\mathsf T}$ \tag{C.4}.

Indices $a,b$ run over eigenvectors, and $n$ indexes components, e.g. $e^{(a)}_n$ (p. 607).

**General square matrices.** There can be up to $N$ distinct eigenvalues. Generically there are $N$, all distinct, each with one left- and one right-eigenvector. If eigenvalues coincide, each distinct non-zero eigenvalue still has at least one of each. Left and right eigenvectors with different eigenvalues are orthogonal: if $\lambda_a\ne\lambda_b$ then $\mathbf{e}_L^{(a)}\cdot\mathbf{e}_R^{(b)}=0$ \tag{C.5} (p. 607).

**Non-negative matrices** (non-zero matrix with all $C_{mn}\ge0$). A non-negative matrix has a non-negative principal eigenvector. It may have other eigenvectors with the same eigenvalue that are not non-negative. If the principal eigenvalue is not degenerate, there is only one principal eigenvector $\mathbf{e}^{(1)}$ and it is non-negative. Generically all other eigenvalues are smaller in absolute magnitude, though special cases can have several of identical magnitude (p. 607).

**Transition probability matrices.** $\mathbf{Q}\ge0$ with columns that are probability vectors:
$$\sum_i Q_{ij}=1\ \text{for all }j.\tag{C.6}$$
With the all-ones vector $\mathbf{n}$: $\mathbf{n}^{\mathsf T}\mathbf{Q}=\mathbf{n}^{\mathsf T}$ \tag{C.7}. So $\mathbf{n}$ is the principal left-eigenvector, with $\lambda_1=1$: $\mathbf{e}_L^{(1)}=\mathbf{n}$ \tag{C.8} (p. 608). $\mathbf{Q}$ has a non-negative principal right-eigenvector $\mathbf{e}_R^{(1)}$. Generically, for ergodic Markov processes, it is the only right-eigenvector with eigenvalue of magnitude 1. Normalized so $\mathbf{e}_R^{(1)}\cdot\mathbf{n}=1$, it is the invariant distribution, left unchanged by $\mathbf{Q}$. It usually cannot be identified without computation. Up to $N-1$ other right-eigenvectors are orthogonal to $\mathbf{n}$, i.e. zero-sum (p. 608).

**Printed tables.**
- Table C.4 lists small matrices with eigenvalues. For $\begin{pmatrix}0&1\\1&1\end{pmatrix}$ they are $1.62$ and $-0.62$ (p. 608).
- Table C.5 gives transition matrices for random paths through trellises (p. 608).
- Table C.6 shows two ways of being non-ergodic (p. 609). (a) The state space falls into two unconnected pieces, giving more than one principal eigenvector with eigenvalue 1. (a′) A small perturbation breaks that degeneracy. (b) The density may oscillate between two parts of the state space, giving another right-eigenvector with eigenvalue $-1$. In general, circulating densities correspond to complex eigenvalues of magnitude 1.

*Intuition note.* For a chain with columns summing to 1, "total probability is conserved" appears as a known left-eigenvector. The long-run distribution is the matching right-eigenvector. Disconnected pieces or cycles add further eigenvalues of size 1, and then the chain does not settle to one distribution. (pp. 608–609)

### C.3 Perturbation theory (pp. 609–611)
The author notes that perturbation theory is not used in the book, but is useful in its fields. The derivation is for square, not necessarily symmetric, matrices (p. 608).

**Setup.** $\mathbf{H}(\epsilon)=\mathbf{H}(0)+\epsilon\mathbf{V}+\cdots$ \tag{C.9}, $\mathbf{V}\equiv\partial\mathbf{H}/\partial\epsilon$ \tag{C.10}. Assume a complete set of $N$ right- and left-eigenvectors for all $\epsilon$ of interest, continuous in $\epsilon$. The author says this last assumption is not necessarily good. If $\mathbf{H}(0)$ has degenerate eigenvalues, eigenvectors may be discontinuous, and degenerate perturbation theory is needed. Only the non-degenerate case is treated (p. 609).
$$\mathbf{H}(\epsilon)\mathbf{e}_R^{(a)}(\epsilon)=\lambda^{(a)}(\epsilon)\mathbf{e}_R^{(a)}(\epsilon)\tag{C.11}$$
$$\lambda^{(a)}(\epsilon)=\lambda^{(a)}(0)+\epsilon\mu^{(a)}+\cdots,\quad \mu^{(a)}\equiv\frac{\partial\lambda^{(a)}}{\partial\epsilon}\tag{C.12, C.13}$$
$$\mathbf{e}_R^{(a)}(\epsilon)=\mathbf{e}_R^{(a)}(0)+\epsilon\mathbf{f}_R^{(a)}+\cdots,\quad \mathbf{f}_R^{(a)}\equiv\frac{\partial\mathbf{e}_R^{(a)}}{\partial\epsilon}\tag{C.14, C.15}$$
Left-vectors $\mathbf{e}_L,\mathbf{f}_L$ are row vectors, so no transpose is needed (p. 610).

**Normalization.** Eigenvector magnitudes are arbitrary. Constrain $\mathbf{e}_L^{(a)}(\epsilon)\mathbf{e}_R^{(a)}(\epsilon)=1$ \tag{C.16}. Expanding in $\epsilon$ (the text writes "(C.19)" for the equation, apparently a misprint for (C.16)) gives \tag{C.17}, and the $O(\epsilon)$ terms give
$$\mathbf{e}_L^{(a)}(0)\mathbf{f}_R^{(a)}+\mathbf{f}_L^{(a)}\mathbf{e}_R^{(a)}(0)=0.\tag{C.18}$$
Choose both terms to vanish: $\mathbf{e}_L^{(a)}(0)\mathbf{f}_R^{(a)}=0$, $\mathbf{f}_L^{(a)}\mathbf{e}_R^{(a)}(0)=0$ \tag{C.19}. For a symmetric matrix this fixes the eigenvectors' Euclidean length (p. 610).

**First order.** Expanding (C.11) \tag{C.20} and taking order-$\epsilon$ terms:
$$\mathbf{H}(0)\mathbf{f}_R^{(a)}+\mathbf{V}\mathbf{e}_R^{(a)}(0)=\lambda^{(a)}(0)\mathbf{f}_R^{(a)}+\mu^{(a)}\mathbf{e}_R^{(a)}(0).\tag{C.21}$$
Multiplying on the left by $\mathbf{e}_L^{(b)}(0)$, and using $\mathbf{e}_L^{(b)}\mathbf{H}(0)=\lambda^{(b)}\mathbf{e}_L^{(b)}$ and $\mathbf{e}_L^{(b)}\mathbf{e}_R^{(a)}=\delta_{ab}$:
$$\lambda^{(b)}\mathbf{e}_L^{(b)}(0)\mathbf{f}_R^{(a)}+\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)=\lambda^{(a)}(0)\mathbf{e}_L^{(b)}(0)\mathbf{f}_R^{(a)}+\mu^{(a)}\delta_{ab}.\tag{C.22}$$
- Setting $b=a$: $\mu^{(a)}=\mathbf{e}_L^{(a)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)$ \tag{C.23}.
- Setting $b\ne a$: $\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)=[\lambda^{(a)}(0)-\lambda^{(b)}(0)]\,\mathbf{e}_L^{(b)}(0)\mathbf{f}_R^{(a)}$ \tag{C.24}, so
$$\mathbf{e}_L^{(b)}(0)\mathbf{f}_R^{(a)}=\frac{1}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}\,\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0).\tag{C.25}$$
- If the $\mathbf{e}_R^{(b)}(0)$ form a complete basis, $\mathbf{f}_R^{(a)}=\sum_b w_b\mathbf{e}_R^{(b)}(0)$ \tag{C.26}, with $w_b=\mathbf{e}_L^{(b)}(0)\mathbf{f}_R^{(a)}$ \tag{C.27}. The $b=a$ term vanishes by (C.19), so
$$\mathbf{f}_R^{(a)}=\sum_{b\ne a}\frac{\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}\,\mathbf{e}_R^{(b)}(0).\tag{C.28}$$

Equations (C.23) and (C.28) solve the first-order problem (p. 611).

**Second order.** Assume $\mathbf{H}(\epsilon)=\mathbf{H}(0)+\epsilon\mathbf{V}$ exactly \tag{C.29}. Expand to $\epsilon^2$ with $\mathbf{g}_R^{(a)}$ and $\nu^{(a)}$ the second derivatives \tag{C.30}. The $\epsilon^2$ terms give
$$\mathbf{V}\mathbf{f}_R^{(a)}+\tfrac12\mathbf{H}(0)\mathbf{g}_R^{(a)}=\tfrac12\lambda^{(a)}(0)\mathbf{g}_R^{(a)}+\tfrac12\nu^{(a)}\mathbf{e}_R^{(a)}(0)+\mu^{(a)}\mathbf{f}_R^{(a)}.\tag{C.31}$$
Multiplying on the left by $\mathbf{e}_L^{(a)}(0)$ \tag{C.32}, the $\mathbf{g}_R$ terms cancel and $\mathbf{e}_L^{(a)}(0)\mathbf{f}_R^{(a)}=0$ by (C.19), leaving
$$\mathbf{e}_L^{(a)}(0)\mathbf{V}\mathbf{f}_R^{(a)}=\tfrac12\nu^{(a)}.\tag{C.33}$$
Substituting (C.28):
$$\tfrac12\nu^{(a)}=\mathbf{e}_L^{(a)}(0)\mathbf{V}\sum_{b\ne a}\frac{\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}\mathbf{e}_R^{(b)}(0)\tag{C.34}$$
$$=\sum_{b\ne a}\frac{[\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)][\mathbf{e}_L^{(a)}(0)\mathbf{V}\mathbf{e}_R^{(b)}(0)]}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}.\tag{C.35}$$

**Summary.** With $V_{ba}\equiv\mathbf{e}_L^{(b)}(0)\mathbf{V}\mathbf{e}_R^{(a)}(0)$, for $\mathbf{H}(\epsilon)=\mathbf{H}(0)+\epsilon\mathbf{V}$:
$$\mathbf{e}_R^{(a)}(\epsilon)=\mathbf{e}_R^{(a)}(0)+\epsilon\sum_{b\ne a}\frac{V_{ba}}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}\mathbf{e}_R^{(b)}(0)+\cdots\tag{C.36}$$
$$\lambda^{(a)}(\epsilon)=\lambda^{(a)}(0)+\epsilon V_{aa}+\epsilon^2\sum_{b\ne a}\frac{V_{ba}V_{ab}}{\lambda^{(a)}(0)-\lambda^{(b)}(0)}+\cdots\tag{C.37}$$
(p. 611). Left-vectors are row vectors and right-vectors are columns, so $V_{ba}$ is a scalar (p. 610).

*Intuition note.* To first order the eigenvalue shifts by the diagonal element $V_{aa}$ of the perturbation in the eigenbasis. Each eigenvector mixes in the other eigenvectors, weighted by the coupling $V_{ba}$ over the eigenvalue gap. A small gap makes the mixing large, (our reading; the author only warns that degenerate eigenvalues can make the eigenvectors discontinuous) (pp. 609, 611).

### C.4 Some numbers (p. 612)
A table lists powers of 2 beside powers of 10, with examples:
- $2^{8192}\approx10^{2466}$: distinct 1-kilobyte files.
- $2^{1024}\approx10^{308}$: states of a 2D Ising model with $32\times32$ spins.
- $2^{1000}\approx10^{301}$: binary strings of length 1000.
- $2^{469}\approx10^{141}$: such strings with 100 ones and 900 zeros.
- $2^{266}\approx10^{80}$: electrons in the universe.
- $2^{98}\approx3\times10^{29}$: age of the universe in picoseconds. $2^{58}\approx3\times10^{17}$: in seconds.
- $6\times10^9$ bits in the human genome. $2^{32}\approx6\times10^9$: population of earth.
- $2^{10}=1024$ and $e^7=1096$.
- Small probabilities: $3\times10^{-8}$ for per-nucleotide DNA transmission error per generation. $10^{-18}$ for undetected error in a hard disk drive after error correction.

## Toy example (ours, not from the source)
Check (C.36)–(C.37) on a symmetric $2\times2$ matrix, so $\mathbf{e}_L=\mathbf{e}_R^{\mathsf T}$.
- $\mathbf{H}(0)=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $\mathbf{V}=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Eigenpairs at $\epsilon=0$: $\lambda^{(1)}=1$, $\mathbf{e}^{(1)}=(1,0)$; $\lambda^{(2)}=0$, $\mathbf{e}^{(2)}=(0,1)$.
- $V_{11}=(1,0)\mathbf{V}(1,0)^{\mathsf T}=0$. $V_{21}=(0,1)\mathbf{V}(1,0)^{\mathsf T}=1$. $V_{12}=1$.
- Eigenvalue: $\lambda^{(1)}(\epsilon)\approx1+\epsilon\cdot0+\epsilon^2\cdot\frac{1\cdot1}{1-0}=1+\epsilon^2$.
- Eigenvector: $\mathbf{e}^{(1)}(\epsilon)\approx(1,0)+\epsilon\frac{V_{21}}{1-0}(0,1)=(1,\epsilon)$.
- Exact check: eigenvalues of $\begin{pmatrix}1&\epsilon\\\epsilon&0\end{pmatrix}$ are $\frac{1\pm\sqrt{1+4\epsilon^2}}{2}$. For $\epsilon=0.1$: $\sqrt{1.04}\approx1.019804$, so $\lambda\approx1.009902$, and the formula gives $1.01$. The eigenvector equation gives $v_2=(\lambda-1)v_1/\epsilon\approx\epsilon v_1$, matching $(1,\epsilon)$.

## Concepts
- [[partition-function]] (new) — $Z(\beta)=\sum_x e^{-\beta E(x)}$, the normalizer of the Boltzmann distribution; $\ln Z$'s derivatives give energy variance and heat capacity (p. 601)
- [[phase-transition]] (new) — a critical point where derivatives of $Z$ jump or diverge; needs infinitely many states and long-range correlations (pp. 601–602)
- [[typical-set]] — typicality, as used here, fails near a critical point; information content and energy fluctuations are linked (p. 604)
- [[galois-field]] (new) — finite field GF($p^m$); for GF(4) and GF(8), arithmetic via polynomials over GF(2) modulo a fixed polynomial (pp. 605–606)
- [[eigenvector-eigenvalue]] (new) — left/right eigenvectors, degeneracy, principal eigenvector, orthonormal set for symmetric matrices (pp. 606–607)
- [[invariant-distribution]] (new) — normalized principal right-eigenvector of a transition matrix $\mathbf{Q}$, left unchanged by $\mathbf{Q}$ (p. 608)
- [[perturbation-theory]] (new) — first-order eigenvector and second-order eigenvalue shifts for $\mathbf{H}+\epsilon\mathbf{V}$ in the non-degenerate case (pp. 609–611)
- [[truth-function]] (new) — $\mathbb{1}[S]=1$ if $S$ is true, else 0 (p. 600)

## Canonical instances
- [[coupled-spin-toy-system]] — one ground state vs $2^N-1$ states; critical $\beta_c=\ln2/\epsilon$, variance peak $\approx N^2\epsilon^2/4$ (pp. 602–603)
- [[independent-spin-system]] — contrast case with no transition and no variance peak (pp. 602–603)
- [[gf4-and-gf8]] — explicit tables via polynomials modulo $x^2+x+1$ and $x^3+x+1$ (pp. 605–606)
- [[non-ergodic-chains]] — Table C.6 (a), (a′), (b): disconnected state space and oscillating chains (p. 609)
- [[big-numbers-table]] — reference magnitudes from files to genomes to error probabilities (p. 612)

## Bridges (candidates)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic.
- [structural-analogy] Partition function $Z$ ↔ bayesian: marginal likelihood as normalizing constant — both are sums over all states or parameters that normalize an unnormalized weight.
- [structural-analogy] Energy fluctuations and the failure of typicality at criticality ↔ information-theory: typical set / AEP — the AEP's concentration needs fluctuations to be small.
- [same-math] Invariant distribution as principal right-eigenvector of $\mathbf{Q}$ ↔ bayesian: MCMC stationary distribution — the same linear-algebra fact about Markov chains.
- [structural-analogy] Eigenvalue gap in (C.36)–(C.37) ↔ bayesian: MCMC mixing — a small gap amplifies perturbations in the first formula, and chain mixing is also governed by eigenvalue gaps.

## Questions this raises
- Why does the toy system show a transition at exactly $\beta_c=\ln2/\epsilon$? What changes if the ground state's degeneracy or the number of other states differs?
- How does the failure of typicality near a critical point affect compression-like arguments for physical systems?
- What does degenerate perturbation theory give when eigenvalues coincide, as in Table C.6 (a)?
- Which linear-code constructions over GF($q$) improve on binary codes, and why?

## Reading notes
- Printed page = pdf page − 12 (pdf 609 = printed 597).
- Misprint: after (C.16), the text says "equation (C.19) implies" (C.17). The image shows "(C.19)", but the context requires (C.16).
- The footnote on p. 600 about $\delta(S)$ as truth function is a small-print aside; it explains why $\mathbb{1}[S]$ is used instead.
- Eigenvector entries in Tables C.4–C.6 are printed to two digits; only the eigenvalues were used above.
- In Table C.4, the 3×3 matrix and 4×4 matrix were not read entry by entry here. Only the 2×2 example is cited.
- Fig. B.1 and B.2 curves are plotted in the images; only their described shapes are reported here.
- No exercises appear in these pages.
