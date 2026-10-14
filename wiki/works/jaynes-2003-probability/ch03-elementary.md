---
id: jaynes-2003-probability/ch03-elementary
work: jaynes-2003-probability
unit: 3 Elementary sampling theory
pages: 51-85
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Elementary sampling theory (urn problems, logic vs. causation, and the limits of "randomization")

## L0 — One line
The product rule, sum rule and indifference already give the hypergeometric and binomial distributions, and show that probability expresses logical connection between propositions (a state of knowledge), which need not be physical causation.

## L1 — The gist (≤ 120 words)
What follows from the basic rules of probability for an urn of N balls, M of them red? Drawing without replacement gives the hypergeometric distribution (the chance of r reds in n draws). Its symmetries show that, in this urn, a later draw is exactly as relevant to an earlier draw as an earlier one is. Jaynes concludes that probability tracks logical, not causal, dependence. "Randomized" sampling with replacement gives the binomial distribution (independent draws), but Jaynes calls this an approximation that discards information. A small Markov model (each draw slightly shifts the next) shows it can mislead for long runs. The chapter ends by contrasting sampling distributions (hypothesis → data) with the inverse problem (data → hypothesis) pursued next.

**Prerequisites:** product and sum rules; factorials and binomial coefficients; Boolean algebra of propositions; limits; 2×2 matrices, eigenvalues and eigenvectors.

## L2 — Key ideas (5–10 bullets)
- **Probabilities are descriptions of the robot's knowledge, not physical properties of the urn.** So "verifying" P(R₁|B) = M/N by experiments on the urn is illogical, in Jaynes's word (p. 52).
- **Hypergeometric distribution.** Drawing without replacement gives h(r|N,M,n) = C(M,r)C(N−M,n−r)/C(N,n). It has the symmetry h(r|N,M,n) = h(r|N,n,M) and a most probable r near (n+1)(M+1)/(N+2) (pp. 55–57).
- **Exchangeability.** The probability of a sequence does not depend on order, so every draw is equally relevant to every other. P(R_j|R_k B) = P(R_k|R_j B), and later draws bear on earlier ones as much as earlier ones bear on later ones (pp. 60–63).
- **Logic vs. propensity.** Logical inference runs both ways in time; physical influence runs only forward. Jaynes says that restricting probability to physical causation loses its most important applications (pp. 61–62, 83–84).
- **Vague information (R_later) behaves like an expectation.** In the N=4, n=3 example, P(R₁|R_later B) = ⟨M⟩/(N−2) = 2/5, which exceeds P(R₁|R₂B) = 1/3. In general a probability can be an expectation of a fraction, P = ⟨F⟩ (pp. 64–67).
- **Binomial limit and "randomization".** The binomial is the N→∞ limit of the hypergeometric. Sampling with replacement plus shaking gives it only approximately, by deliberately discarding relevant information. Limit theorems then hold for the model, not automatically for the real world (pp. 69–75).
- **Correlation correction.** In the Markov model with parameters ε and δ, the exact solution P(R_k|C) = [(p−δ) − (ε+δ)^{k−1}(pε−qδ)]/(1−ε−δ) shows how long runs can make the binomial approximation misleading. The special case pε = qδ restores forward–backward symmetry (pp. 75–82).
- **Looking ahead.** Sampling distributions (hypothesis → data) are rarely the real problem. Science mostly faces the inverse problem (data → hypothesis), which needs prior knowledge (pp. 84–85).

## L3 — Walkthrough

### Chapter introduction (pp. 51–52)
Available tools so far (p. 51):
- the product rule $P(AB|C)=P(A|BC)P(B|C)=P(B|AC)P(A|C)$ \tag{3.1}
- the sum rule $P(A|B)+P(\bar A|B)=1$ \tag{3.2}
- the extended sum rule $P(A+B|C)=P(A|C)+P(B|C)-P(AB|C)$ \tag{3.3}
- the principle of indifference: for mutually exclusive, exhaustive $H_1,\dots,H_N$ that $B$ does not favour, $P(H_i|B)=1/N$ \tag{3.4}
- the Bernoulli urn rule: if $A$ is true on $M$ of the $H_i$, $P(A|B)=M/N$ \tag{3.5}

Jaynes claims that essentially all of conventional probability theory, plus many results thought to lie beyond it, can be derived from this foundation (p. 51). He urges even experienced readers to study the simple applications carefully, because, he says, failure to understand their logic has been one of the major factors retarding scientific inference for many decades (pp. 51–52).

### 3.1 Sampling without replacement (pp. 52–60)
**Setup.** Background $B$: an urn holds $N$ balls, identical except for numbers $1..N$. $M$ are red and $N-M$ white. $n$ balls are drawn blindfolded, one at a time, and each is laid aside. $R_i$ = red on draw $i$, $W_i$ = white on draw $i$ (p. 52). Within $B$, $\bar R_i = W_i$ and $\bar W_i=R_i$ \tag{3.7}. For the first draw, $P(R_1|B)=M/N$ \tag{3.8} and $P(W_1|B)=1-M/N$ \tag{3.9} (p. 52).

**Meaning.** These assignments describe the robot's *state of knowledge*, not a physical property of the urn. With different knowledge (for example, known ball positions) they would differ while the urn stayed the same. Jaynes compares "verifying" them by experiments on the urn to verifying a boy's love for his dog by experiments on the dog (p. 52). The robot may only use relations between probabilities and observable facts that can be deduced from the rules of probability. Confident physical predictions may approach, but except in degenerate cases not reach, deductive certainty (p. 53).

**Sequences of reds.** By the product rule $P(R_1R_2|B)=P(R_1|B)P(R_2|R_1B)$ \tag{3.10}. One red ball has been removed, so $N-1$ balls remain, $M-1$ of them red:
$$P(R_1R_2|B)=\frac{M}{N}\frac{M-1}{N-1}\tag{3.11}$$
Continuing, for $r$ consecutive reds (p. 53):
$$P(R_1\cdots R_r|B)=\frac{M(M-1)\cdots(M-r+1)}{N(N-1)\cdots(N-r+1)}=\frac{M!\,(N-r)!}{(M-r)!\,N!},\quad r\le M\tag{3.12}$$
The restriction $r\le M$ is unnecessary if $n!=\Gamma(n+1)$ is used, since the factorial of a negative integer is infinite and (3.12) vanishes for $r>M$ (p. 53). For $w$ whites, swap $M\to N-M$:
$$P(W_1\cdots W_w|B)=\frac{(N-M)!\,(N-w)!}{(N-M-w)!\,N!}\tag{3.13}$$
White on draws $r+1,\dots,r+w$ given red on the first $r$ uses $N\to N-r$, $M\to M-r$ (p. 53):
$$P(W_{r+1}\cdots W_{r+w}|R_1\cdots R_rB)=\frac{(N-M)!\,(N-r-w)!}{(N-M-w)!\,(N-r)!}\tag{3.14}$$
Multiplying (3.12) and (3.14), with $w=n-r$ and the factor $(N-r)!$ cancelling (p. 54):
$$P(R_1\cdots R_rW_{r+1}\cdots W_n|B)=\frac{M!\,(N-M)!\,(N-n)!}{(M-r)!\,(N-M-w)!\,N!}\tag{3.15}$$

**Order does not matter.** Write $M!/(M-r)!=M(M-1)\cdots(M-r+1)$ \tag{3.16}, and similarly for the other ratios. Then (3.15) equals
$$\frac{M(M-1)\cdots(M-r+1)\,(N-M)(N-M-1)\cdots(N-M-w+1)}{N(N-1)\cdots(N-n+1)}\tag{3.17}$$
For any other order of $r$ reds and $w$ whites, the product still has $n$ factors (p. 54):
- The $k$-th draw always contributes $(N-k+1)$ to the denominator.
- The $k$-th red ball drawn contributes $(M-k+1)$ to the numerator, whenever it occurs.
- The $k$-th white ball drawn contributes $(N-M-k+1)$ to the numerator.

The same factors appear, only permuted, so every order has probability (3.15) (p. 54). Jaynes adds that the product rule could be expanded in many other ways. That all give the same answer is a nontrivial consistency property, which the derivations of Chapter 2 sought to ensure (p. 54).

**Multiplicity.** Different orders are mutually exclusive, so we multiply (3.15) by the binomial coefficient
$$\binom nr=\frac{n!}{r!(n-r)!}\tag{3.18}$$
which counts the orders of $r$ reds in $n$ draws (the "multiplicity"). Examples: three reds in three draws, $\binom33=1$ way \tag{3.19}; two reds in three draws, $\binom32=3$ ways ($R_1R_2W_3$, $R_1W_2R_3$, $W_1R_2R_3$) \tag{3.20} (p. 55). Exercise 3.1 asks why the multiplicity is not $n!$ (p. 55).

**Hypergeometric distribution.** Let $A$ be the proposition that exactly $r$ reds occur in $n$ draws, in any order, and $h(r|N,M,n)\equiv P(A|B)$ \tag{3.21}. Then (p. 55)
$$h(r|N,M,n)=\frac{\binom Mr\binom{N-M}{n-r}}{\binom Nn}\tag{3.22}$$
It vanishes automatically when $r>M$, $r>n$ or $(n-r)>(N-M)$. Notation point: capital $P(A|B)$ always has propositions as arguments. When ordinary numbers are arguments, Jaynes defines a new function such as $h$. Writing $P(r|NMn)$ hides the qualitative stipulations and has led to serious errors, such as the marginalization paradox. He still uses small-$p$ notation like most authors, where context decides the meaning (pp. 55–56).

The name comes from the Gauss hypergeometric function
$$F(a,b,c;t)=\sum_{r=0}^\infty\frac{\Gamma(a+r)\Gamma(b+r)\Gamma(c)}{\Gamma(a)\Gamma(b)\Gamma(c+r)}\frac{t^r}{r!}\tag{3.23}$$
which terminates as a polynomial if $a$ or $b$ is a negative integer. The generating function $G(t)\equiv\sum_{r=0}^n h(r|N,M,n)t^r$ \tag{3.24} equals $F(-M,-n,c;t)/F(-M,-n,c;1)$ with $c=N-M-n+1$ \tag{3.25}. $G(1)=1$ is the normalization (p. 56).

**Mode.** Setting $h(r')=h(r'-1)$ gives
$$r'=\frac{(n+1)(M+1)}{N+2}\tag{3.26}$$
If $r'$ is an integer, $r'$ and $r'-1$ are jointly most probable. Otherwise the unique mode is $\hat r=\mathrm{INT}(r')$ \tag{3.27}. So the most probable sample fraction $f=r/n$ is nearly the urn fraction $F=M/N$. Jaynes calls this his first crude example of a physical prediction: a relation between a quantity $F$ given in the information and a quantity $f$ measurable in an experiment (p. 56).

**Cumulative distribution, median, quartiles.** $H(R)\equiv\sum_{r=0}^R h(r)$ \tag{3.28}, extended to real $x$ as a staircase, $H(x)=H(\mathrm{INT}(x))$ (pp. 56–57).
- Strictly, a discrete distribution generally has no median. The unique median exists if some integer $R$ has $H(R-1)=1-H(R)$ and $H(R)>H(R-1)$.
- If instead $H(R)=1/2$, any $r$ in $R\le r<R'$ is a median, where $R'$ is the next jump point (p. 57).
- For large $n$, a relaxed usage is fine: the median is the $R$ with $H(R)$ closest to 1/2, and quartiles and deciles are defined similarly (p. 57).
- Median ± interquartile distance gives a good idea of the prediction and its accuracy.
- Probability $5/6-1/6=2/3$ (odds 2:1) that $r$ lies between the first and fifth hexile. Odds 8:2 = 4:1 that it lies between the first and ninth decile (p. 57).

**Tables.** Tables 3.1 and 3.2 (pp. 57–58) give $h(r)$ and $H(r)$ for the cases $(N,M,n)=(100,50,10)$ and $(100,10,50)$. The entries for positive $h$ are identical, e.g. $h(5)=0.259334$, $h(0)=0.000593$. This reflects the symmetry
$$h(r|N,M,n)=h(r|N,n,M)\tag{3.29}$$
which is evident from the symmetry of $F$ in $a,b$ (p. 57). Red/white relabelling gives $h(n-r|N,N-M,n)=h(r|N,M,n)$ \tag{3.30}. For $M=N/2$ this becomes the peak symmetry $h(n-r|N,M,n)=h(r|N,M,n)$ \tag{3.31}, which also holds for $n=N/2$ by (3.29) (p. 58). It does not hold in general: for $N=99$ the peak is slightly asymmetric (Table 3.3, $h(4)=0.206715$, $h(6)=0.216111$) (pp. 57–59).

> **Intuition note.** The hypergeometric distribution counts the ways to pick a sample with $r$ reds, divided by all ways to pick a sample. It peaks near the urn's red fraction. Its hidden symmetries (swap $M$ and $n$; swap colours) are consequences of the counting, not extra assumptions.

**Red on the second draw.** What is $P(R_2|B)$ when the robot does not know the first result? It does not know whether $M$ or $M-1$ reds remain, so the Bernoulli urn rule seems not to apply and the problem might look indeterminate (p. 59). Resolve $R_2=(R_1+W_1)R_2=R_1R_2+W_1R_2$ \tag{3.32}. By the sum and product rules (p. 59):
$$P(R_2|B)=P(R_2|R_1B)P(R_1|B)+P(R_2|W_1B)P(W_1|B)\tag{3.33}$$
With $P(R_2|R_1B)=\frac{M-1}{N-1}$ and $P(R_2|W_1B)=\frac M{N-1}$ \tag{3.34}:
$$P(R_2|B)=\frac{M-1}{N-1}\frac MN+\frac M{N-1}\frac{N-M}N=\frac MN\tag{3.35}$$
For the third draw, $R_3=(R_1+W_1)(R_2+W_2)R_3=R_1R_2R_3+R_1W_2R_3+W_1R_2R_3+W_1W_2R_3$ \tag{3.36}, and the four terms (3.37) again sum to $M/N$ (p. 60). So the probability of red at any draw, if the robot does not know the result of any other draw, is $M/N$. This is the "first nonobvious symmetry". It is proved in general as a special case of (3.118) (p. 60). The method is to resolve the wanted proposition into mutually exclusive, well-chosen subpropositions, then apply the sum and product rules (p. 60).

### 3.2 Logic vs. propensity (pp. 60–63)
**Question.** An earlier draw clearly bears on the $k$-th draw, since it changes the number $M_k$ of reds in the urn. Does a later draw? **Penrose's view** (as reported by Jaynes): probabilities referring to the present may depend only on what happened earlier, a necessary condition of "causality". Jaynes stresses instead that inference concerns logical connections, which may or may not match physical influence (p. 60).

**Extreme example.** $N=2$, $M=1$: $P(R_1|B)=1/2$, but if red occurs on draw 2, then
$$P(R_1|R_2B)=0\tag{3.38}$$
(p. 61). In general, from the product rule
$$P(R_jR_k|B)=P(R_j|R_kB)P(R_k|B)=P(R_k|R_jB)P(R_j|B)\tag{3.39}$$
and $P(R_j|B)=P(R_k|B)=M/N$:
$$P(R_j|R_kB)=P(R_k|R_jB),\quad\text{all }j,k\tag{3.40}$$
Later draws are exactly as relevant as earlier ones. This is the "second nonobvious symmetry" (p. 61).

**Jaynes's criticism of propensity views.** He says it appears to him that (3.40) would be quite inexplicable from a propensity viewpoint (e.g. Popper's), and that his theory of logical inference differs fundamentally, in outlook and results, from the theory of physical causation of Penrose and Popper. He does not forbid the notion of propensity: if it is formulated as a well-defined hypothesis, it can be analysed (Section 3.10) and tested against alternatives (Chapter 4). Logical inference applies whether or not a propensity exists (p. 61). Footnote 1 (p. 61) argues against Popper's propensity interpretation and says incomplete knowledge is the only working material a scientist has.

Physical influence propagates only forward, but logical inference works in both directions. Jaynes's examples are archaeology, Sherlock Holmes, sounds from a marching band, and a Toscanini recording. Using all relevant information, earlier or later, should be "a platitude, not a paradox" (p. 62). Exercise 3.6 will show a backward inference that accounts for a forward causal influence (p. 62). Jaynes also says a fully adequate theory of nonequilibrium phenomena such as sound propagation requires backward logical inferences, although they do not express physical causes (p. 62).

**Exchangeability.** If $p(x_1\cdots x_n|B)$ is invariant under any permutation of the $x_i$ (each taking values $1..k$), it depends only on the counts $(n_1\cdots n_k)$. Such a distribution is called *exchangeable*. The hypergeometric distribution is exchangeable, so every draw is equally relevant to every other, whatever their order or distance (p. 62).

**Quantitative check, $j<k$.** $R_jR_k=(R_1+W_1)\cdots(R_{j-1}+W_{j-1})R_j(R_{j+1}+W_{j+1})\cdots(R_{k-1}+W_{k-1})R_k$ \tag{3.41}. It expands into
$$2^{j-1}\times2^{k-j-1}=2^{k-2}\tag{3.42}$$
full sequences such as $W_1R_2W_3\cdots R_j\cdots R_k$ \tag{3.43}. Permuting each sequence to put $R_j$ first and $R_k$ second, then recombining, gives $R_1R_2(R_3+W_3)\cdots(R_k+W_k)=R_1R_2$ \tag{3.44}. Hence (p. 63)
$$P(R_jR_k|B)=P(R_1R_2|B)=\frac{M(M-1)}{N(N-1)}\tag{3.45}$$
$$P(W_jR_k|B)=P(W_1R_2|B)=\frac{(N-M)M}{N(N-1)}\tag{3.46}$$
$$P(R_k|R_jB)=\frac{P(R_jR_k|B)}{P(R_j|B)}=\frac{M-1}{N-1}\tag{3.47}$$
$$P(R_k|W_jB)=\frac{P(W_jR_k|B)}{P(W_j|B)}=\frac M{N-1}\tag{3.48}$$
These hold for $j<k$, and by (3.40) for all $j\ne k$ (p. 63). **Plain explanation:** learning that red appears later means one red ball must be "set aside" for it, so one fewer red is available for earlier draws (p. 63).

> **Intuition note.** If you know a red ball will turn up on some other draw, that ball is "spoken for", whatever the time order. So information about any other draw changes your odds in the same way. Only the logical bookkeeping matters, not which draw happens first.

### 3.3 Reasoning from less precise information (pp. 64–66)
New information: red occurs at least once on later draws, $R_{\rm later}\equiv R_{k+1}+\cdots+R_n$ \tag{3.49}. From the product rule (3.50),
$$P(R_k|R_{\rm later}B)=P(R_k|B)\frac{P(R_{\rm later}|R_kB)}{P(R_{\rm later}|B)}\tag{3.51}$$
The naive $P(R_{\rm later}|B)=\sum_{j>k}P(R_j|B)$ \tag{3.52} is wrong unless $M=1$, because the $R_j$ are not mutually exclusive (p. 64). Better: $\bar R_{\rm later}=W_{k+1}\cdots W_n$ \tag{3.53}. By exchangeability and (3.13) (pp. 64–65):
$$P(\bar R_{\rm later}|B)=\frac{(N-M)!\,(N-n+k)!}{N!\,(N-M-n+k)!}=\binom{N-M}{n-k}\binom N{n-k}^{-1}\tag{3.54}$$
$$P(\bar R_{\rm later}|R_kB)=\binom{N-M}{n-k}\binom{N-1}{n-k}^{-1}\tag{3.55}$$
so
$$P(R_k|R_{\rm later}B)=\frac M{N-n+k}\times\frac{\binom{N-1}{n-k}-\binom{N-M}{n-k}}{\binom N{n-k}-\binom{N-M}{n-k}}\tag{3.56}$$
Check: for $n=k+1$ it reduces to $(M-1)/(N-1)$ (p. 65).

**Example** ($n=3$ draws, $N=4$, $M=2$, $k=1$; Jaynes writes "$M=2$ of which are white", but with $N=4$ both counts are 2):
$$P(R_1|R_2+R_3,B)=\frac{6-2}{12-2}=\frac25=\frac12\cdot\frac{1-1/3}{1-1/6}\tag{3.57}$$
Compare $P(R_1|B)=1/2$ and $P(R_1|R_2B)=P(R_2|R_1B)=1/3$ \tag{3.58}. The surprise is
$$P(R_1|R_{\rm later}B)>P(R_1|R_2B)\tag{3.59}$$
(most people guess the opposite). Direct checks (p. 65):
- Extended sum rule: $P(R_{\rm later}|B)=\tfrac12+\tfrac12-\tfrac12\cdot\tfrac13=\tfrac56$ \tag{3.60}.
- Exclusive decomposition: $\tfrac12\cdot\tfrac23+\tfrac12\cdot\tfrac23+\tfrac12\cdot\tfrac13=\tfrac56$ \tag{3.61}.
- Numerator: $P(R_{\rm later}|R_1B)=\tfrac13+\tfrac13-\tfrac13\cdot0=\tfrac23$ \tag{3.62} (p. 66).

The agreement of the three calculations is what "consistency" means in practice (p. 65).

**Intuitive reading.** $R_2$ removes one red and one ball from the first draw's urn: $(M-1)/(N-1)=1/3$. $R_{\rm later}$ reduces the number of balls in the urn by two and the "effective number of reds" by more than one. Try $P(R_1|R_{\rm later}B)=(M)_{\rm eff}/(N-2)$ \tag{3.63}. Given $R_{\rm later}$, at least one red is removed, and (since $R_2R_3R_{\rm later}=R_2R_3$)
$$P(R_2R_3|R_{\rm later}B)=\frac{P(R_2R_3|B)}{P(R_{\rm later}|B)}=\frac{(1/2)(1/3)}{5/6}=\frac15\tag{3.64}$$
So the effective number removed is $1+1/5=6/5$, leaving $4/5$, and
$$P(R_1|R_{\rm later}B)=\frac{4/5}{2}=\frac25\tag{3.65}$$
(p. 66).

### 3.4 Expectations (pp. 66–67)
If $X$ takes values $x_i$ in mutually exclusive, exhaustive situations with probabilities $p_i$,
$$\langle X\rangle=E(X)=\sum_{i=1}^np_ix_i\tag{3.66}$$
is its *expectation*, a probability-weighted average. Jaynes calls the term inappropriate because it is often an impossible value, but keeps it by precedent (p. 67).

Given $R_{\rm later}$, the possibilities $R_2W_3,\ W_2R_3,\ R_2R_3$ \tag{3.67} leave $M=(1,1,0)$ reds for draw 1, with conditional probabilities $2/5,\ 2/5,\ 1/5$ \tag{3.68–3.70}. So
$$\langle M\rangle=1\cdot\tfrac25+1\cdot\tfrac25+0\cdot\tfrac15=\tfrac45\tag{3.71}$$
The "effective $M$" in (3.63) is the expectation of $M$. When $F=M/N$ is known, $P(R_1|B)=F$. When $F$ is unknown,
$$P(R_1|B)=\langle F\rangle\equiv E(F)\tag{3.72}$$
(expectation over the joint distribution of $M,N$ if both are unknown). Jaynes says that a probability equalling the expectation of a fraction will prove to be a general rule in thousands of more complicated situations. He leaves it as an exercise to derive (3.56) this way (p. 67).

> **Intuition note.** When you are unsure how many reds are in the urn, your probability for red is the average of the fractions you think possible, each weighted by how plausible it is. The effective number of reds found in 3.3 is just this average.

### 3.5 Other forms and extensions (p. 68)
The nine factorials can also be grouped as $h(r|N,M,n)=\binom nr\binom{N-n}{M-r}\big/\binom NM$ \tag{3.73}. The $M\leftrightarrow n$ symmetry shows only when all factorials are written out. A mnemonic form, with $R$ red, $W$ white, $n=r+w$:
$$h(r)=\binom Rr\binom Ww\Big/\binom{R+W}{r+w}\tag{3.74}$$
With $k$ colours ($N_i$ of colour $i$), drawing $r_i$ of colour $i$ in $n=\sum r_i$ draws gives the generalized hypergeometric distribution (Jaynes leaves the verification to the reader):
$$h(r_1\cdots r_k|N_1\cdots N_k)=\frac{\binom{N_1}{r_1}\cdots\binom{N_k}{r_k}}{\binom{\sum N_i}{\sum r_i}}\tag{3.75}$$

### 3.6 Probability as a mathematical tool (pp. 68–69)
Declare colours 1 and 2 to be one colour "a", with $N_a=N_1+N_2$, $r_a=r_1+r_2$ \tag{3.77}. Then (3.75) gives $h(r_a,r_3,\dots|N_a,N_3,\dots)$ \tag{3.76} directly. Summing over all splits $r_1+r_2=r_a$ gives it too:
$$h(r_a,r_3,\dots)=\sum_{r_1=0}^{r_a}h(r_1,r_a-r_1,r_3,\dots|N_1,\dots,N_k)\tag{3.78}$$
Comparing the two gives a purely algebraic identity (p. 69):
$$\binom{N_a}{r_a}=\sum_{r_1=0}^{r_a}\binom{N_1}{r_1}\binom{N_2}{r_a-r_1}\tag{3.79}$$
and likewise
$$\binom{N_1+N_2+N_3}{r_a}=\sum_{r_1=0}^{r_a}\sum_{r_2=0}^{r_1}\binom{N_1}{r_1}\binom{N_2}{r_2}\binom{N_3}{r_a-r_1-r_2}\tag{3.80}$$
Probabilistic reasoning can thus derive purely mathematical results (p. 69).

### 3.7 The binomial distribution (pp. 69–71)
The hypergeometric's complication comes from the changing urn contents. If $N\gg n$ the probability changes little, and as $N\to\infty$ a simpler result should appear. Rewrite (3.22) as
$$h(r|N,M,n)=\frac{\left[\frac1{N^r}\binom Mr\right]\left[\frac1{N^{n-r}}\binom{N-M}{n-r}\right]}{\left[\frac1{N^n}\binom Nn\right]}\tag{3.81}$$
The first factor is $\frac1{r!}\frac MN\left(\frac MN-\frac1N\right)\cdots\left(\frac MN-\frac{r-1}N\right)$ \tag{3.82}. In the limit $N\to\infty$, $M\to\infty$, $M/N\to f$ (p. 70):
$$\frac1{N^r}\binom Mr\to\frac{f^r}{r!}\tag{3.83}$$
$$\frac1{N^{n-r}}\binom{N-M}{n-r}\to\frac{(1-f)^{n-r}}{(n-r)!}\tag{3.84}$$
$$\frac1{N^n}\binom Nn\to\frac1{n!}\tag{3.85}$$
(The page image prints $\binom{M-1}{n-r}$ in (3.84); (3.81) requires $\binom{N-M}{n-r}$.) Each factor has its own limit, so the product's limit is the product of limits:
$$h(r|N,M,n)\to b(r|n,f)\equiv\binom nrf^r(1-f)^{n-r}\tag{3.86}$$
the *binomial distribution*. Its generating function is $G(t)=\sum_{r=0}^nb(r|n,f)t^r=(1-f+ft)^n$ \tag{3.87}, an example of Newton's binomial theorem (p. 70).

**Figure 3.1** compares hypergeometrics with $N=15,30,100$ and $M/N=0.4$, $n=10$ to the binomial ($n=10$, $f=0.4$). All peak at $r=4$ with the same mean $\langle r\rangle=4$, but the binomial is broader. For $N=15$ ($6$ red, $9$ white), $h$ is zero for $r=0$ and $r>6$. For $N>100$ the two agree so closely that for most purposes it does not matter which is used (p. 71).

**Multinomial.** If all $N_i\to\infty$ with $f_i\equiv N_i/\sum N_j$ \tag{3.88} fixed, (3.75) goes into (left as an exercise)
$$m(r_1\cdots r_k|f_1\cdots f_k)=\frac{r!}{r_1!\cdots r_k!}f_1^{r_1}\cdots f_k^{r_k},\quad r=\sum r_i\tag{3.89}$$
A generating function of $k-1$ variables proves normalization (p. 71).

> **Intuition note.** If the urn is huge compared with the sample, removing balls barely changes the contents, so draws look independent with a fixed red fraction $f$. That limit is the binomial. The binomial is broader than the hypergeometric (p. 71); our own reading (not Jaynes's) is that a finite urn runs out of reds, which narrows the spread.

Exercises 3.2–3.5 are on pp. 71–72.

### 3.8 Sampling with replacement (pp. 72–75)
Replacement suits non-destructive sampling. With background $B'$ (same as $B$ plus replacement), $P(R_1R_2|B')=P(R_1|B')P(R_2|R_1B')$ \tag{3.91}. The first factor is $M/N$, but the second is hard: a red ball dropped back in may lie on top and be more likely to be drawn again, which breaks the symmetry behind the Bernoulli urn rule (pp. 72–73).

**3.8.1 Digression: a sermon on reality vs. models (pp. 73–75).**
- The probability of a draw would depend on urn size and shape, ball size, how the ball was tossed in, friction, and so on. Jaynes doubts that the world's best scientists with all computing facilities could solve this, though he says it would not be quite right to call the problem unsolvable in principle (p. 73).
- **Jaynes's ironic account of "randomization".** Make the problem harder (shake the urn). Then assert that the shaking made all details irrelevant, so the Bernoulli rule applies. Then give this a dignified name, "randomization". He says its real meaning is: "deliberately throwing away relevant information when it becomes too complicated for us to handle" (p. 73).
- He criticizes writers who treat "randomized" as an incantation making calculations immune to criticism (p. 74).
- **In defence of the procedure:** it often gives a useful approximation, since the neglected details may have little numerical effect for simple questions such as the probability of $r$ reds when $n$ is small. There is, however, no proof of this and no reliable error estimate, so an element of vagueness necessarily enters at this point (p. 74).
- **The draft-lottery fish bowl:** to the objection that it was not shaken enough, Jaynes replies that the objector could only say it is unfair to those whose numbers are on top, whom he cannot identify; that remains true after any amount of further shaking. Shaking does not make the outcome "random" in any real-world sense. It only ensures no human can wilfully influence the result (p. 74).
- **Mind projection fallacy:** believing randomness is a real property of Nature amounts to "I don't know the detailed causes – therefore – Nature does not know them" (p. 74).
- Jaynes objects not to the procedure itself, provided one honestly admits it is an approximate compromise, but to the belief that it makes the equations exact. The worst error is in limit theorems (laws of large numbers): they are valid properties of the abstract model, but they do not establish the identity of probability and limiting frequency in real repeated experiments (pp. 74–75). He says it is probably safe to say that no limit theorem applies directly in the real world, since no model captures every relevant circumstance (p. 75).

**Result.** After shaking, declare $P(R_2|R_1B')=P(R_2|B')=M/N$, and so on. The probability of red at any trial is $M/N$, now whatever the robot knows about other trials. Hence the probability of exactly $r$ reds in $n$ trials is
$$\binom nr\left(\frac MN\right)^r\left(\frac{N-M}N\right)^{n-r}\tag{3.92}$$
the binomial (3.86). Randomized sampling with replacement from a finite urn has approximately the same effect as the $N\to\infty$ limit without replacement. It should be good for small $n$, but errors can accumulate for large $n$ (p. 75).

### 3.9 Correction for correlations (pp. 75–80)
**Model.** Suppose drawing and replacing a red ball raises the probability of red at the next draw by $\epsilon>0$, and a white one lowers it by $\delta>0$. Earlier draws are negligible. This is a small forward "propensity" (p. 76). With $p\equiv M/N$ and $C$ the background information:
$$P(R_k|R_{k-1}C)=p+\epsilon,\quad P(R_k|W_{k-1}C)=p-\delta,\quad P(W_k|R_{k-1}C)=1-p-\epsilon,\quad P(W_k|W_{k-1}C)=1-p+\delta\tag{3.93}$$
For a specified order with $r$ red and $n-r$ white, and first draw red,
$$p(p+\epsilon)^c(p-\delta)^{c'}(1-p+\delta)^w(1-p-\epsilon)^{w'}\tag{3.94}$$
(for first draw white, the first factor is $1-p$). Here $c$ = reds preceded by red, $c'$ = reds preceded by white, $w$ = whites preceded by white, $w'$ = whites preceded by red, and
$$c+c'=\begin{cases}r-1\\r\end{cases},\quad w+w'=\begin{cases}n-r\\n-r-1\end{cases}\tag{3.95}$$
(upper case: first draw red; lower: first draw white). For small counts this reduces to $p^r(1-p)^{n-r}$ \tag{3.96}. For larger counts use $(1+\epsilon/p)^c\simeq\exp\{\epsilon c/p\}$ \tag{3.97}:
$$p^r(1-p)^{n-r}\exp\left\{\frac{\epsilon c-\delta c'}{p}+\frac{\delta w-\epsilon w'}{1-p}\right\}\tag{3.98}$$
The probability now depends on order. For $N=2M$, $p=1/2$ (so $\epsilon=\delta$), the exponential factor is
$$\exp\{2\epsilon[(c-c')+(w-w')]\}\tag{3.99}$$
This shows (i) as $n\to\infty$, results with long runs become arbitrarily more probable than under the randomized approximation, and (ii) the effect becomes appreciable when numbers like $\epsilon c$ reach order unity. For $\epsilon=10^{-2}$ the randomized approximation can be trusted reasonably well while $n<100$. Real experiments are notorious for showing such "improbable" runs (pp. 76–77).

**Exact marginals.** With $q=1-p$ \tag{3.100}:
$$P(R_2|C)=(p+\epsilon)p+(p-\delta)q=p+(p\epsilon-q\delta)\tag{3.101}$$
$$P(R_3|C)=(p+\epsilon)(p+p\epsilon-q\delta)+(p-\delta)(q-p\epsilon+q\delta)=p+(1+\epsilon+\delta)(p\epsilon-q\delta)\tag{3.102}$$
$P(R_k|C)$ depends on $k$, so the distribution is no longer exchangeable (p. 77).

**Markov chain.** Let $V_k=\begin{pmatrix}P(R_k|C)\\P(W_k|C)\end{pmatrix}$ \tag{3.103} (shape 2×1). Then $V_k=\mathsf M V_{k-1}$ \tag{3.104} with the 2×2 transition matrix
$$\mathsf M=\begin{pmatrix}p+\epsilon&p-\delta\\q-\epsilon&q+\delta\end{pmatrix}\tag{3.105}$$
(Jaynes writes $M$ for both this matrix and the red count.) Then $V_k=\mathsf M^{k-1}V_1$ \tag{3.106}, with $V_1=(p,q)^T$ \tag{3.117}. The characteristic polynomial is
$$C(\lambda)=\det(M_{ij}-\lambda\delta_{ij})=\lambda^2-\lambda(1+\epsilon+\delta)+(\epsilon+\delta)\tag{3.107}$$
with eigenvalues $\lambda_1=1$, $\lambda_2=\epsilon+\delta$ \tag{3.108} (pp. 77–78). For a 2×2 matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ \tag{3.109}, a right eigenvector for eigenvalue $\lambda$ is $x=(b,\ \lambda-a)^T$ \tag{3.110}. This gives
$$x_1=\begin{pmatrix}p-\delta\\q-\epsilon\end{pmatrix},\quad x_2=\begin{pmatrix}1\\-1\end{pmatrix}\tag{3.111}$$
They are not orthogonal, since $\mathsf M$ is not symmetric. With
$$S=\begin{pmatrix}p-\delta&1\\q-\epsilon&-1\end{pmatrix}\tag{3.112}$$
$$S^{-1}=\frac1{1-\epsilon-\delta}\begin{pmatrix}1&1\\q-\epsilon&-(p-\delta)\end{pmatrix}\tag{3.113}$$
one verifies $S^{-1}\mathsf MS=\Lambda=\mathrm{diag}(\lambda_1,\lambda_2)$ \tag{3.114}, so $\mathsf M^r=S\Lambda^rS^{-1}$ \tag{3.115}, i.e.
$$\mathsf M^r=\frac1{1-\epsilon-\delta}\begin{pmatrix}p-\delta+[\epsilon+\delta]^r[q-\epsilon]&[p-\delta][1-(\epsilon+\delta)^r]\\ [q-\epsilon][1-(\epsilon+\delta)^r]&q-\epsilon+[\epsilon+\delta]^r[p-\delta]\end{pmatrix}\tag{3.116}$$
Hence
$$P(R_k|C)=\frac{(p-\delta)-(\epsilon+\delta)^{k-1}(p\epsilon-q\delta)}{1-\epsilon-\delta}\tag{3.118}$$
This agrees with (3.100)–(3.102). For $\epsilon=\delta=0$ it gives $P(R_k|C)=p$, the proof promised after (3.37) (p. 79). *Skip path:* carry forward (3.118) and the form (3.128) below.

**Exactness and extreme cases.** Positivity of $\epsilon,\delta$ was never used, so (3.118) is exact for the abstract model whatever their values. Because the entries of (3.93) are probabilities, $-p\le\epsilon\le q$ and $-q\le\delta\le p$ \tag{3.119}, hence $-1\le\epsilon+\delta\le1$ \tag{3.120} (p. 79).
- $\epsilon+\delta=1$ iff $\epsilon=q$, $\delta=p$. Then $\mathsf M$ is the unit matrix \tag{3.121}, and the first colour is certain to repeat: $P(R_k|C)=p$ for all $k$ \tag{3.122}.
- $\epsilon+\delta=-1$ gives $\mathsf M=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ \tag{3.123}, and the colours certainly alternate: $P(R_k|C)=p$ for $k$ odd, $q$ for $k$ even \tag{3.124}.
- Negative $\epsilon,\delta$ are unrealistic, since a red ball left on top should raise, not lower, the chance of red. If they cannot be negative, the lower bound in (3.120) is zero, reached only at $\epsilon=\delta=0$, where $\mathsf M$ is singular and the binomial case returns (p. 79).

**Realistic case, $0<|\epsilon+\delta|<1$.** The last term of (3.118) decays exponentially in $k$ and
$$P(R_k|C)\to\frac{p-\delta}{1-\epsilon-\delta}\tag{3.125}$$
Yet the limiting distribution is still not exchangeable. If red occurred on trial $j$, then $V_j=(1,0)^T$ \tag{3.126}, and $V_k=\mathsf M^{k-j}V_j$ for $j\le k$ \tag{3.127}, giving, for $j<k$,
$$P(R_k|R_jC)=\frac{(p-\delta)+(\epsilon+\delta)^{k-j}(q-\epsilon)}{1-\epsilon-\delta}\tag{3.128}$$
It tends to the same limit (3.125). Backward inferences differ: the product rule gives $P(R_kR_j|C)=P(R_k|R_jC)P(R_j|C)=P(R_j|R_kC)P(R_k|C)$ \tag{3.129}. Since $P(R_k|C)\ne P(R_j|C)$ (for $j\ne k$),
$$P(R_j|R_kC)\ne P(R_k|R_jC)\tag{3.130}$$
Backward inference is possible but is not the same formula as forward inference (p. 80).

This is the simplest "baby" version of an irreversible process in the "Markovian approximation", also called a first-order autoregressive model. Jaynes says that, because of confusion of inference with causality in the statistical-mechanics literature, the backward-inference part of such solutions is almost always missed, and some try to infer backward by extrapolating the forward solution, with quite bizarre, unphysical results. So the reader doing Exercise 3.6 is, in effect, conducting new research (p. 80).

> **Intuition note.** A tiny forward "stickiness" can undermine the independence assumed by the binomial once runs get long. Even then, inference runs backward in time as well as forward, using a different formula. A one-step causal influence thus produces a two-way logical dependence.

### 3.10 Simplification (pp. 81–82)
If
$$p\epsilon=q\delta\tag{3.131}$$
then $\frac{p-\delta}{1-\epsilon-\delta}=p$, $\frac{q-\epsilon}{1-\epsilon-\delta}=q$, $\epsilon+\delta=\epsilon/q$ \tag{3.132}, and (3.118) and (3.128) collapse to
$$P(R_k|C)=p\ \ \text{all }k\tag{3.133}$$
$$P(R_k|R_jC)=P(R_j|R_kC)=p+q\left(\frac\epsilon q\right)^{|k-j|}\tag{3.134}$$
The distribution is still not exchangeable, because (3.134) depends on the separation $|k-j|$. But forward–backward symmetry is restored, even though $\epsilon,\delta$ act only forward. Jaynes notes that by the derivation of (3.40) this symmetry is a necessary consequence of (3.133), exchangeable or not (p. 81). The condition does not simplify $\mathsf M$ or turn off the correlations. It makes the initial vector (3.117) equal, up to normalization, to the eigenvector $x_1$, so it is left unchanged by $\mathsf M$ (p. 81).

**Heuristic rationale** (Jaynes says the argument is too crude to count as a derivation). Suppose the $N$ balls lie in $L$ layers. After one withdrawal about $n=(N-1)/L$ remain in the top layer, about $np$ red. If the drawn ball was red and is tossed back unshaken, the chance of red next is
$$\frac{np+1}{n+1}=p+\frac{1-p}n+O\!\left(\frac1{n^2}\right)\tag{3.135}$$
and if it was white, the chance of white next is
$$\frac{n(1-p)+1}{n+1}=1-p+\frac pn+O\!\left(\frac1{n^2}\right)\tag{3.136}$$
(here $n$ is the top-layer size, not the number of draws). Comparing with (3.93): $\epsilon\simeq q/n$, $\delta\simeq p/n$ \tag{3.137}, which satisfies (3.131). So the argument at least suggests that the condition is not inherently unreasonable. Jaynes leaves its significance, and any generalization beyond the Markov case, to the reader (p. 82).

### 3.11 Comments (pp. 82–85)
**When is the urn analogy apt?** In the 250 years since Bernoulli's *Ars Conjectandi*, many physical measurements have seemed much like drawing from an urn of Nature (p. 82).
- It is literal for radioactive counts, survey sampling and industrial quality control.
- It is strained for agricultural experiments and medical trials.
- It seems "dangerously misleading" for coin flipping, repeated measurements of temperature and wind, planetary position, a baby's weight or a commodity price. There, the literature often justifies urn distributions by a "hypothetical infinite population" that is a figment of imagination. Its main functional consequence is strict independence of successive draws (p. 82).

Jaynes holds that this is unsound. He says the belief that such distributions represent not just our prior state of knowledge but the actual long-run variability of the data cannot be justified, and that supposing the assignments have real physical meaning is another form of the mind projection fallacy. The price usually paid is missed opportunities: information not expressible in urn terms goes unused (p. 83).

**Caveat.** An erroneous argument need not give a wrong conclusion: sophisticated calculations (Chapter 9) sometimes return urn distributions for purely mathematical reasons, so the hypergeometric and binomial distributions will keep reappearing (p. 83). Footnote 2 compares this to exponentials appearing throughout analysis (p. 83).

**A case where urn reasoning would be fully justified** (Jaynes says it probably never arises in the real world). Take many urns with known, identical contents, using a fresh urn for each draw. Then $P(A)=M/N$ is strictly independent of other draws, and this prior information takes precedence over any amount of data. If the contents $(M,N)$ were unknown but known to be identical, independence would be lost, because each draw would tell us about the other urns without physically influencing them (p. 83).

**Scope.** Logical dependence differs from causal dependence; Jaynes says most expositions do not recognize this at all, which has led to errors (suggested by Exercise 3.6; a more serious one appears in Chapter 4 after Eq. (4.29)). To restrict probability theory to problems of physical causation is to lose its most important applications, and most problems of this chapter fall outside expositions that treat probability as a physical phenomenon. In the 'physical probability' theory it is not even considered legitimate to speak of the probability of an outcome at a specified trial, yet that is what scientific inference needs to do (p. 84). In future applications one must check whether the experiment is really like drawing from an urn; if not, return to the product and sum rules, which may or may not give urn distributions (p. 84).

**3.11.1 A look ahead.** The distributions of this chapter are *sampling distributions* (historically "direct probabilities"): given a hypothesis $H$ (here the contents $(M,N)$), what is the probability of data $D$? Jaynes does not use "direct probability", since it connotes reasoning from physical cause to effect and not all sampling distributions can be so interpreted. Sampling distributions make predictions. If the observations disagree with them, the discrepancy hints at a better hypothesis. How wide a disagreement justifies rejecting a hypothesis is the subject of significance tests. The need for such tests in astronomy led Laplace and Gauss to study probability (p. 84). Although sampling theory dominates conventional teaching, Jaynes says that in the real world such problems are an almost negligible minority (p. 84).

In virtually all real scientific problems the data $D$ are known and the hypothesis $H$ is not: the *inverse problem*, "Given $D$, what is the probability that $H$ is true?" (Exercise 3.3 is a first example.) Jaynes will focus almost exclusively on inverse problems. Computing sampling distributions is often needed but is almost never an end in itself (p. 85). The inverse question seems to need "what did you know about $H$ before seeing $D$?", which did not appear in sampling calculations. Jaynes says this dissymmetry is more apparent than real and arises mostly from habits of notation. He turns to it in the next chapter (p. 85).

## Toy example (our own, not from the text)
An urn has $N=5$ balls, $M=2$ red, 3 white. Draw $n=2$ without replacement.

- $P(R_1)=2/5$.
- $P(R_1R_2)=\frac25\cdot\frac14=\frac1{10}$ (by 3.11).
- $P(W_1R_2)=\frac35\cdot\frac24=\frac3{10}$.
- $P(R_2)=\frac1{10}+\frac3{10}=\frac4{10}=\frac25=M/N$ (the symmetry of 3.35).
- **Backward inference:** $P(R_1|R_2)=\frac{1/10}{2/5}=\frac14$, which equals the forward $P(R_2|R_1)=\frac{M-1}{N-1}=\frac14$. Also $P(R_1|W_2)=\frac{P(R_1W_2)}{P(W_2)}=\frac{(2/5)(3/4)}{3/5}=\frac{3/10}{3/5}=\frac12=\frac M{N-1}$ (3.48, with order swapped).
- **Hypergeometric check** from (3.22): $h(0)=\binom20\binom32/\binom52=3/10$, $h(1)=\binom21\binom31/10=6/10$, $h(2)=\binom22\binom30/10=1/10$. The sum is $1$. The mode from (3.26) is $r'=\frac{3\cdot3}{7}=\frac97\approx1.29$, so $\hat r=1$, which matches $h(1)=0.6$.

A later draw therefore changes the probability of an earlier one exactly as an earlier draw changes a later one, even though a later draw cannot physically affect an earlier one.

## Concepts
- [[probability-as-extended-logic]] — probability describes the robot's state of knowledge given the stated information, not physical properties of the urn (p. 52)
- [[principle-of-indifference-maximum-entropy]] — equal probability 1/N for mutually exclusive, exhaustive hypotheses that $B$ does not distinguish, which gives the Bernoulli urn rule (p. 51)
- [[exchangeability]] — the probability of a sequence is invariant under any permutation of the trial results, so it depends only on the counts; the author's definition is for $k$-valued trials (p. 62)
- [[hypergeometric-distribution]] (new) — $h(r|N,M,n)$ of (3.22): the probability of $r$ reds in $n$ draws without replacement (p. 55)
- [[binomial-distribution]] (new) — $b(r|n,f)$ of (3.86): the $N\to\infty$ limit of the hypergeometric; also the result of "randomized" sampling with replacement (pp. 70, 75)
- [[multiplicity]] (new) — the number of orders in which an event $r$ can occur, $\binom nr$ (p. 55)
- [[expectation]] (new) — probability-weighted average of a quantity's possible values; $P(R_1|B)=\langle F\rangle$ when $F$ is unknown (pp. 66–67)
- [[logical-vs-causal-dependence]] (new) — probabilities express logical connection, which runs both ways in time; physical influence runs only forward (pp. 60–62)
- [[randomization-as-information-discarding]] (new) — Jaynes's reading of "randomization": declaring complicated relevant details irrelevant, as a practical approximation (p. 73)
- [[mind-projection-fallacy]] (new) — treating features of one's knowledge (ignorance of causes, "randomness") as properties of Nature (p. 74)
- [[markov-chain-transition-matrix]] (new) — $V_k=\mathsf MV_{k-1}$ with the 2×2 matrix (3.105), solved by eigen-decomposition (p. 77)
- [[sampling-distribution]] (new) — $P(\text{data}|\text{hypothesis})$; Jaynes uses the term whether the link is logical or causal (p. 84)
- [[Bayes-inverse-problem]] (new) — inferring the hypothesis from known data; needs prior knowledge, treated from Chapter 4 (p. 85)

## Canonical instances
- [[urn-without-replacement]] — Bernoulli urn with $N$ balls, $M$ red; derives the hypergeometric distribution and its symmetries (pp. 52–59)
- [[two-ball-urn-later-draw]] — $N=2,M=1$: $P(R_1|R_2B)=0$, showing later draws are relevant (pp. 60–61)
- [[four-ball-three-draw-example]] — $N=4,M=2,n=3$: $P(R_1|R_{\rm later}B)=2/5>P(R_1|R_2B)=1/3$, checked three ways (pp. 65–66)
- [[draft-lottery-fish-bowl]] — shaking ensures no human can influence the result; it does not make it "random" in Nature (p. 74)
- [[correlated-urn-markov-chain]] — forward correlations $\epsilon,\delta$, solved exactly; shows failure of the binomial for long runs (pp. 75–80)
- [[hypothetical-infinite-population]] — a figment used to justify urn distributions for data (p. 82)

## Bridges (candidates)
- [structural-analogy] Exchangeability: all draws equally relevant ↔ bayesian: exchangeability / de Finetti — the chapter uses permutation invariance only; the representation theorem is not in this unit.
- [same-math] $P(R_1|B)=\langle F\rangle$ (3.72) ↔ bayesian: posterior predictive for a Bernoulli trial is the posterior mean of $\theta$ — both are the law of total probability applied to a fraction.
- [structural-analogy] Logical vs. causal dependence (3.40) ↔ bayesian: association vs. intervention in the ladder of causation / do-operator — conditioning on information is not the same as physical intervention.
- [same-math] Two-state transition matrix, $V_k=\mathsf M^{k-1}V_1$ ↔ stochastic processes: two-state Markov chain with eigenvalues $1$ and $\epsilon+\delta$ — the same linear-algebra computation.
- [metaphor] Randomization as discarding relevant information ↔ bayesian: modelling assumptions and prior/posterior predictive checks — both ask what a simplification throws away.
- [structural-analogy] Sampling distribution vs. inverse problem ↔ bayesian: likelihood vs. posterior — $P(D|H)$ as a function of $D$ versus $P(H|D)$ needing a prior.

## Questions this raises
- If "randomization" only approximates the true state of knowledge, how can one bound the error of the binomial approximation for a given $n$ and $\epsilon$?
- What is the intuitive meaning of the "magic" condition $p\epsilon=q\delta$ (3.131) in the sticky-urn model? Does it generalize beyond the Markovian approximation (as Jaynes asks)?
- How does prior knowledge enter the inverse problem (data → hypothesis) that Chapter 4 begins, given that it never appeared in sampling-theory calculations?
- When real data are not like urn draws, which other kinds of background information should replace the independence assumption?

## Exercises worth doing
- Ex. 3.1 (p. 55) — why the multiplicity is $\binom nr$ and not $n!$; clarifies what "unspecified" balls means in (3.15) — difficulty: easy
- Ex. 3.2 (p. 71) — probability of at least one ball of each colour in $m$ draws; and $m$ for 90% when $k=5$, all $N_i=10$ — difficulty: medium
- Ex. 3.3 (p. 71) — a first inverse problem: infer the number of colours $k$ from a sample; needs common-sense judgments — difficulty: hard
- Ex. 3.4 (p. 72) — derive (3.90) for matches between $M$ urns and $M$ balls; limit $1-1/e$ — difficulty: medium
- Ex. 3.5 (p. 72) — probability that each of $M$ urns receives at least one of $N$ balls — difficulty: medium
- Ex. 3.6 (p. 81) — explicit backward inference $P(R_j|R_kC)$, forward vs. backward, steady values and exchangeability on sparse subsets — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 30 (pdf 81–115 are printed 51–85).
- Table captions (p. 58): the captions read Table 3.1 = (100, 10, 50) and Table 3.2 = (100, 50, 10), but the text on p. 57 describes them in the opposite order. The two tables contain identical numbers, so only the labelling differs.
- Eq. (3.84): the page image prints $\binom{M-1}{n-r}$; from (3.81) this should be $\binom{N-M}{n-r}$. I wrote the corrected form and flagged it.
- Eq. (3.57): the example text says "$M=2$ of which are white"; with $N=4$ both counts equal 2, so the numbers are unaffected. $M$ is the red count throughout.
- Eq. (3.91): the text says "an equation like (3.9)"; the product-rule equation it mirrors is (3.10).
- Eq. (3.56): I give the author's printed form. The numerical form (6−2)/(12−2) = 2/5 matches the alternative form on the same line.
- The text layers of (3.23) (Γ symbols lost) and (3.108) (ε lost) were garbled, and (3.110) is printed on one line as $x=(b\lambda-a)$. I checked against the images: (3.25) has $c=N-M-n+1$, and the eigenvector must be the column $(b,\ \lambda-a)^T$, since it reproduces (3.111).
- The symbol $M$ is used for the red count and (in italics) for the transition matrix in (3.105); I wrote $\mathsf M$ for the matrix. In 3.10, $n$ is reused for the top-layer size.
- Equations in the text layer for Section 3.9 were sometimes garbled; all were checked against page images.
