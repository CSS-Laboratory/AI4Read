---
id: stone-2022-information/appa-glossary
work: stone-2022-information
unit: Appendix A Glossary
pages: 241-246
fields: [information-theory]
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
# Appendix A: Glossary

## L0 — One line
A short reference list fixing how Stone uses the vocabulary of information theory and the probability and statistics it needs.

## L1 — The gist (≤ 120 words)
The glossary gives short definitions of the terms used in the book. It covers coding terms (alphabet, codeword, prefix code, capacity, rate). It covers information measures (information, entropy, conditional entropy, equivocation, mutual information, relative entropy, transfer entropy). It also covers basic probability and statistics (Bayes' rule, random variable, variance, iid). It matters because, "in this text", Stone gives some words particular meanings: "outcome" versus "outcome value", and "uncertainty" as surprisal (the information $\log(1/p(x))$ of one value) or entropy (its average). "Rate" has two uses, one of them $H(X)-H(X|Y)$. Several entries are loose and point to other chapters.

**Prerequisites:** sums and logarithms; basic probability (distribution, conditional probability); binary numbers.

## L2 — Key ideas (5–10 bullets)
- Information is $h(x)=\log(1/p(x))$ and entropy is its average, $H(X)=\sum p(x_i)\log(1/p(x_i))$ (p. 243).
- Conditional entropy $H(Y|X)$ is average uncertainty about $Y$ once $X$ is known. Equivocation is $H(X|Y)$, the channel-input uncertainty once the output is known (pp. 242–243).
- Channel rate is $R=H(X)-H(X|Y)$ and cannot exceed capacity $C$ (p. 245).
- Coding efficiency is $H(S)/L(X)$, the information carried per binary digit (p. 242).
- A bit is not the same as a binary digit; a bit is the information needed to pick one of two equally probable alternatives (p. 242).
- A prefix code lets each codeword be decoded as soon as it arrives (p. 244).
- Random variable, outcome and outcome value are separate ideas: a physical outcome gets a numerical value (pp. 244–245).
- The glossary says there are many definitions of probability and names the two main ones (Bayesian, frequentist); variance is given by two formulas (pp. 244–246).

## L3 — Walkthrough
The entries are alphabetical. They are grouped here by topic, and each group keeps the author's wording and numbers.

### Symbols, messages, codes (pp. 241–242, 244)
- **Alphabet:** a set of symbols used to build a message. Example: $A_s=\{1,\dots,6\}$. A message is one symbol ($s=4$) or an ordered list ($\mathbf s=(1,1,6,3,2,3,1,1,4)$) (p. 241).
- **Binary digit:** a 0 or a 1. **Binary number:** a number made of binary digits, e.g. 1001. **Byte:** an ordered set of 8 binary digits (pp. 241–242).
- **Bit:** a fundamental unit of information, often confused with a binary digit. A bit gives enough information to specify one of two equally probable alternatives (p. 242).
- **Code:** a set of symbols or messages, an encoder (symbols → channel inputs) and a decoder (channel outputs → inputs). The **codebook** is the set of codewords the encoder produces. A **codeword** $x$ is what each message symbol $s$ is encoded as before transmission (p. 242).
- **Encoding:** ideally, each element of the encoded message conveys as much information as possible (p. 242).
- **Coding efficiency:** a source with entropy $H(S)$ is encoded with mean codeword length $L(X)$. Efficiency is $H(S)/L(X)$ bits per binary digit, the information each binary digit carries (p. 242).
- **Prefix code:** no codeword is the prefix of another, so each can be decoded on arrival. Also called instantaneous or self-punctuating (p. 244).
- **Parity:** a measure of the number of 1s or 0s in a binary number, shown by a parity binary digit. Stone says it is often wrongly called a "parity bit" (p. 244).
- **Message:** a sequence of symbols or values, written bold $\mathbf s$ or plain $s$ by context (p. 244). **Symbol:** one element of an alphabet, a value a random variable can take (p. 246).

### Channels (pp. 241–245)
- **Channel:** a conduit for communicating data from input to output. **Binary symmetric channel:** the probability $P$ that input $X=1$ is flipped to output $Y=0$ equals the probability that a 0 is flipped to a 1 (pp. 241–242).
- **Capacity:** the maximum rate at which a channel can communicate information from input to output, in bits/s or bits/symbol (p. 242).
- **Rate:** in information theory, the rate at which information passes from input $X$ to output $Y$ is
$$R=H(X)-H(X|Y)\ \text{bits/s},$$
and it cannot exceed capacity $C$ (p. 245). **Transmission rate:** see rate (p. 246).
- **Noise:** the random "jitter" that is part of a measured quantity (p. 244).
- **Rate distortion theory:** gives a theoretical bound on the information needed to represent a signal at a given distortion (p. 245). In it, $\hat X$ is a distorted version of $X$, and the rate $R$ is the entropy $H(\hat X)$, the bits allocated to represent an element of $\mathbf X=(X_1,\dots,X_n)$ (p. 245).
  - **Rate distortion function:** smallest rate $R$ that represents $X$ as $\hat X$ at a given distortion $D$.
  - **Rate equivocation function:** smallest rate $R$ for a given equivocation $E=H(X|\hat X)$ (p. 245).

*Intuition note:* Rate is the input entropy minus what is still unknown about the input once the output is seen. That leftover is the equivocation. Capacity is the ceiling on this rate (pp. 243, 245).

### Information measures (pp. 242–246)
- **Information:** for $X=x$, $h(x)=\log(1/p(x))$. Average information per value is entropy, $H(X)=\sum p(x_i)\log(1/p(x_i))$ (p. 243).
- **Entropy:** the glossary only says it is a measure of a variable's overall variability (p. 243). **Uncertainty:** in this text, surprisal or average surprisal (entropy) (p. 246).
- **Conditional entropy:** $H(Y|X)=\mathrm E[\log(1/p(y|x))]$ bits, the average uncertainty about $Y$ when $X$ is known (p. 242).
- **Equivocation:** average uncertainty of the input $x$ when the output $y$ is known, $H(X|Y)$ (p. 243).
- **Mutual information:** reduction in uncertainty $I(X,Y)$ about $Y$ from knowing $X$. It is symmetric: $I(X,Y)=I(Y,X)$ (p. 244).
- **Differential entropy:** defined as the expected value of "a continuous random variable, $\mathrm E[\log(1/p(x))]$" (p. 242). Read it as the expectation of $\log(1/p(x))$; the printed wording is loose.
- **Kullback–Leibler divergence** (= **relative entropy**): a measure of the difference between two distributions $p(X)$ and $q(X)$ (pp. 243, 246).
- **Kolmogorov complexity:** the smallest number of binary digits needed to represent a given entity. The glossary calls it asymptotically equivalent to Shannon information (p. 243).
- **Transfer entropy** $T_{x_{\text{past}}\to y_t}$: the average information that past values $x_{\text{past}}$ give about current $y_t$, over and above what $y_{\text{past}}$ gives (p. 246).
- **Redundancy:** in an ordered set of values (image, sound), a value is redundant if it can be obtained from knowledge of other values (p. 245).
- **Ensemble:** in physics, the set of all possible microstates of a system. In information theory, source entropy is defined using the ensemble of an infinite set of sequences (p. 243).
- **Stationary source:** the probability of each symbol, and of every sub-sequence, stays stable over time (p. 246).

### Probability (pp. 241–246)
- **Bayes' rule:** for observed $x$,
$$p(y|x)=\frac{p(x|y)\,p(y)}{p(x)},$$
where $p(y|x)$ is the posterior, $p(x|y)$ the likelihood, $p(y)$ the prior and $p(x)$ the marginal probability (p. 241).
- **Probability:** two main definitions, using coin bias. *Bayesian:* an observer's estimate based on all their information, including past proportions of heads. *Frequentist:* the proportion of heads over many flips (pp. 244–245).
- **Conditional probability** $p(y|x)$ (p. 242); **joint probability:** two dice giving $x_3=3$ and $y_4=4$ has $p(x_3,y_4)=1/36$ (p. 243).
- **Independence:** the value of $X$ gives no information about $Y$, and vice versa. **iid:** values chosen independently from a single distribution (p. 243).
- **Marginal distribution:** from marginalising a joint distribution; the glossary writes $p(X)=\int_y p(x,y)\,dy$ (p. 244).
- **Outer product:** for $p(X)$ with $n$ values and $p(Y)$ with $m$ values, an $n\times m$ matrix whose entries are $p(x_i)\times p(y_j)$. It represents $p(X,Y)=p(X)p(Y)$ (p. 244).
- **Probability distribution:** a pdf for a continuous variable, a probability function (pf, also "pmf") for a discrete one (p. 245).
- **Random variable:** a physical outcome (a pair of dice $(x_a,x_b)$) is assigned a value $x=x_a+x_b$, and probabilities come from $p(X)$ (p. 245).
- **Outcome** is a single physical result. **Outcome value** is the number assigned to it, $x=X(x_1,x_2)$ (p. 244).
- **Sample space:** all possible experiment outcomes. Three coin flips give 8 sequences (p. 246).
- **Law of large numbers:** the mean of $n$ samples converges to $\mu$ as $n\to\infty$ (p. 243).
- **Relative frequency:** frequency as a proportion; E is $1304/10000=0.134$ of English letters (p. 246).
- **Histogram:** counts of each value; divided by the total gives a normalised histogram (p. 243).
- **Cdf:** cumulative area under the pdf (p. 242).
- **Average:** $\bar x=\frac1n\sum_{j=1}^n x_j$ (A.1) (p. 241).
- **Variance:** the sample estimate is
$$\hat v_x=\frac1n\sum_{j=1}^n (x_j-\bar x)^2\tag{A.3}$$
and with $m$ possible values,
$$v_x=\sum_{i=1}^m p(x_i)\,(x_i-\mathrm E[x])^2\tag{A.4}$$
(p. 246). **Standard deviation** $\sigma=\sqrt{\text{variance}}$; **precision** $=1/\text{variance}$ (pp. 244, 246).

### Maths and other terms (pp. 241–246)
- **Binomial coefficient:** the number of ways to place $k$ 1s among $n$ binary positions is $C_{n,k}=n!/(k!(n-k)!)$ (A.2), with $n!=n\times(n-1)\times\dots\times1$ (p. 241).
- **Logarithm:** $y=\log_a x$ is the power to which $a$ is raised to get $x$ (p. 243).
- **Monotonic:** a change in $x$ always raises $y$ or always lowers $y$ (p. 244).
- **Disjoint:** no shared items; $\{pqr\}$ and $\{stu\}$ are disjoint, $\{pqr\}$ and $\{rst\}$ are not (p. 242).
- **Integration:** "a platonic form of summation" (p. 243). **Continuous / discrete:** any value vs clearly separated values (p. 242). **Theorem:** a proven mathematical statement. **Variable:** a "container", usually for one number (p. 246). **Quantum computer:** uses quantum mechanics to speed up computation (p. 245).

## Toy example (ours)
A source has four symbols with $p=(1/2,\,1/4,\,1/8,\,1/8)$.
- Surprisals $\log_2(1/p)$: $1,\,2,\,3,\,3$ bits.
- $H=\tfrac12(1)+\tfrac14(2)+\tfrac18(3)+\tfrac18(3)=0.5+0.5+0.375+0.375=1.75$ bits.
- Prefix code A: codewords 0, 10, 110, 111. Mean length $L=\tfrac12(1)+\tfrac14(2)+\tfrac18(3)+\tfrac18(3)=1.75$. Efficiency $=1.75/1.75=1$ bit per binary digit.
- Fixed code B: 00, 01, 10, 11. $L=2$, efficiency $=1.75/2=0.875$ bits per binary digit.

Code B uses 2 binary digits for every symbol, more than the source entropy needs, so each binary digit carries less than 1 bit.

## Concepts
- [[bit]] — information to pick one of two equally probable alternatives; not the same as a binary digit (p. 242)
- [[self-information-surprisal]] — $h(x)=\log(1/p(x))$ (p. 243)
- [[entropy]] — average of $h(x)$; the glossary defines it only as overall variability, and uses "uncertainty" for surprisal or entropy (pp. 243, 246)
- [[joint-and-conditional-entropy]] — $H(Y|X)=\mathrm E[\log(1/p(y|x))]$ (p. 242)
- [[mutual-information]] — symmetric reduction in uncertainty (p. 244)
- [[equivocation]] (new) — $H(X|Y)$, uncertainty about the channel input given the output (p. 243)
- [[redundancy]] — a value obtainable from other values (p. 245)
- [[channel-capacity]] — maximum rate of information from input to output (p. 242)
- [[transmission-rate]] (new) — $R=H(X)-H(X|Y)\le C$ (p. 245)
- [[coding-efficiency]] (new) — $H(S)/L(X)$ (p. 242)
- [[prefix-code-kraft]] — no codeword is a prefix of another (p. 244)
- [[rate-distortion-function]] — smallest rate for a given distortion $D$ (p. 245)
- [[relative-entropy-kl]] — measure of difference between two distributions (pp. 243, 246)
- [[differential-entropy]] — expected value $\mathrm E[\log(1/p(x))]$ for a continuous variable (p. 242)
- [[kolmogorov-complexity]] — fewest binary digits to represent an entity (p. 243)
- [[transfer-entropy]] — extra information from past of $X$ about $y_t$ beyond $y_{\text{past}}$ (p. 246)
- [[noisy-channel]] — no entry of this name; the glossary defines noise (p. 244) and the binary symmetric channel (p. 241)

## Canonical instances
- [[dice-pair]] — joint probability $1/36$; outcome vs outcome value (pp. 243–245)
- [[coin-flip-sample-space]] — three flips give 8 sequences (p. 246)
- [[english-letter-frequency]] — E has relative frequency 0.134 (p. 246)
- [[binary-symmetric-channel]] — symmetric flip probability $P$ (p. 241)

## Bridges (candidates)
- [same-math] Variance $\sum p(x_i)(x_i-\mathrm E[x])^2$ ↔ statistics: variance of a discrete distribution — same formula (p. 246).
- [structural-analogy] Entropy of a source via an ensemble ↔ statistical physics: ensemble of microstates — both average over a set of possible configurations (p. 243).
- [structural-analogy] Bayesian vs frequentist probability ↔ statistics: two readings of "probability" (pp. 244–245).

## Questions this raises
- Why is $H(S)/L(X)$ at most 1 for a prefix code?
- How does $R=H(X)-H(X|Y)$ relate to mutual information, and when is it maximised to give $C$?
- How does the entropy of a continuous variable differ from the discrete sum?
- In what sense is Kolmogorov complexity "asymptotically equivalent" to Shannon information?

## Reading notes
- Printed page = pdf − 16.
- Typos and loose wording in the source: "it is or encoded" (encoding entry); differential entropy is called "the expected value of a continuous random variable", which presumably means the expected value of $\log(1/p(x))$ (as the formula that follows shows); the marginal-distribution entry prints "$p(X)=\int_y p(x,y)\,dy$", with capital $X$ on the left and lower-case $x$ inside.
- The outer-product entry says "the $i$th column and $j$th row" holds $p(x_i)\times p(y_j)$, as printed.
- The glossary only summarises; fuller treatments are in other chapters and appendices (cited: Sections 1.3, 1.5, 2.2; Appendices C–G).
