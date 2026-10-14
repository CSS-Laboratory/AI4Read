---
id: stone-2022-information/ch02-entropy
work: stone-2022-information
unit: "Chapter 2 — Entropy of Discrete Variables"
pages: 21-44
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Entropy of Discrete Variables

## L0 — One line
The entropy of a discrete variable is the average surprise, $-\log_2 p(x)$ averaged over its outcomes, and it equals $\log_2 m$ bits when $m$ outcomes are equally probable.

## L1 — The gist (≤ 120 words)
The chapter asks how to measure the uncertainty of a random outcome, such as a coin flip or a die throw. It first fixes the vocabulary: random variables, probability distributions, messages, codes and channels. It then defines the surprise of one outcome as $h(x)=\log_2(1/p(x))$ bits, and entropy as the average surprise over the distribution. A fair coin has 1 bit, a coin with $p(\text{head})=0.9$ has 0.469 bits, and an $m$-sided fair die has $\log_2 m$ bits. Entropy depends only on the probabilities, not on the labels of the outcomes. It is a core concept of information theory.

**Prerequisites:** relative-frequency probability; logarithms and powers of 2; the summation sign; the idea of an average (expected value).

## L2 — Key ideas
- A random variable is really a function from experiment outcomes to numbers (outcome values). This separates "what happened" from "what number we record" (p. 23, p. 25, p. 26).
- A message is encoded into codewords, sent through a possibly noisy channel, and decoded. Channel capacity is the maximum rate (information actually communicated per second); a code's rate can be below it but never above (p. 26, p. 29).
- Shannon's four desiderata (continuity, symmetry, maximal value, additivity) are the minimal properties a measure of information should have. The author says Shannon proved that the logarithmic definition is the only one with all four (p. 31).
- Surprise (Shannon information) of an outcome is $h(x)=\log_2(1/p(x))=-\log_2 p(x)$ bits. Rarer outcomes carry more bits (p. 32, p. 36).
- Entropy is average surprise: $H(X)=\sum_i p(x_i)\log(1/p(x_i))=E[\log(1/p(x))]$. It can be computed from the distribution, or estimated from a large sample (p. 38–41).
- $m=2^{H(X)}$ gives the number of equally probable values a variable is "worth". Doubling the number of equally probable outcomes adds one bit (p. 36, p. 42).
- For a discrete variable, entropy depends only on the probabilities, not on the outcome values. The formula assumes iid values (independent, identically distributed); related values give less entropy than the summed individual entropies (p. 43).
- Bits (also called shannons), nats (log base $e$) and bans (log base 10) are units set by the logarithm base (p. 44).

## L3 — Walkthrough

### 2.1–2.2 Ground rules and terminology
**Probability.** The author uses an informal, relative-frequency notion. In a bag of 40 white and 60 black balls, p(black) = 60/100 = 0.6. A probability lies between 0 (definitely will not occur) and 1 (definitely will occur). Probabilities of mutually exclusive events must add up to one (p. 21).

**Discrete variables.** Discrete elements are clearly separated, like integers. The distribution of probabilities over a discrete variable is a *probability function*, drawn as a bar graph. Continuous variables, with points packed densely like a line, have *probability density functions* (Chapter 5). The text calls both "probability distributions" (p. 22).

**Random variables.** A random variable $X$ is strictly a function mapping each experiment outcome to a number, the *outcome value* (p. 23). The author says it is not like the algebraic $x$ in $3x+2=5$ (p. 23). For a coin the alphabet is
$$A_x=\{x_h,x_t\}\tag{2.1}$$
with $X(x_h)=1$ (2.2) and $X(x_t)=0$ (2.3). The *sample space* is the set of all possible experiment outcomes. Three coin flips give 8 possible sequences (p. 23). Equations 2.4–2.7 give the shorthand $X=x_h$, $X=x_t$, $X=1$, $X=0$ (p. 24).

If the experiment is repeated infinitely often, the frequencies of values define the distribution $p(X)=\{p(x_h),p(x_t)\}$ (2.8–2.9) (p. 24). A fair coin has $\{0.5,0.5\}$ (2.10–2.12). A coin bent to land heads 90% of the time has $\{0.9,0.1\}$ (2.13–2.15) (p. 25). The probabilities vary continuously between 0 and 1, even though the values of $X$ are discrete (p. 25).

Outcome and outcome value only need to be distinguished when their numbers differ. Example: a die with $X=0$ for outcomes 1, 3, 5 and $X=1$ for 2, 4, 6 has six outcomes but two outcome values (p. 25). Usually lower-case $x$ stands for both. The terms "outcome" and "outcome value" are unique to this book (p. 26).

**Communication terminology** (Figure 2.3, p. 26).
- A *source* generates *messages*. A message is an ordered sequence of $k$ symbols, $\mathbf s=(s_1,\dots,s_k)$ (2.16) (p. 26).
- Each symbol is a value of a random variable $S$ over an alphabet of $\alpha$ symbols, $A_s=\{s_1,\dots,s_\alpha\}$ (2.17), with distribution $p(S)=\{p(s_1),\dots,p(s_\alpha)\}$ (2.18). By definition
$$\sum_{i=1}^{\alpha}p(s_i)=1\tag{2.19}$$
(p. 27).
- An *encoder* (a generic function $g$) turns each message into the *channel input* $\mathbf x=g(\mathbf s)=(x_1,\dots,x_n)$ (2.20). Each *codeword* is a value of $X$ from the *codebook* $A_x=\{x_1,\dots,x_m\}$ (2.21), with $p(X)=\{p(x_1),\dots,p(x_m)\}$ (2.22) (p. 27).
- Several symbols may be combined into one codeword, or the message may be compressed by removing redundancy, so $n$ and $k$ may differ (p. 28). Compression is *lossless* if perfect decompression is possible, and *lossy* if information is discarded (p. 28).
- A *code* is a look-up table of symbols and codewords. In Table 2.1, eight symbols (3, 6, …, 24) map to the 3-bit codewords 000, …, 111 (p. 28).
- Redundancy may be added to codewords so they withstand noise (p. 28).
- Transmission yields outputs $\mathbf y=(y_1,\dots,y_n)$ (2.23), values of $Y$ from $A_y=\{y_1,\dots,y_m\}$ (2.24), with $p(Y)$ (2.25). If the channel is noisy, $y_j$ may differ from the transmitted $x_j$ (p. 28–29). Figure 2.3 writes this as $y=x+\eta$ with noise $\eta$ (p. 26).
- The decoder converts each output to a possibly incorrect message. The *error rate* of a code is the number of incorrect inputs associated with that codebook divided by the number of possible inputs (p. 29).

**Channel capacity.** This is the maximum amount of information that can be communicated from input to output. It can be expressed per symbol, or per second (e.g. bits/s) (p. 29). Bucket analogy: capacity is the bucket's size and rate is the water poured in. We can pour in less than capacity, but not more (p. 29). A noiseless channel sending $n$ symbols/s from an alphabet of $\alpha$ symbols has capacity $n\log\alpha$ bits/s, which is $n$ bits/s for binary data (p. 29). The rate depends on the code. The rate of a code may be below capacity but not above it. Capacity is the maximum rate over all possible codes (p. 29). A binary code in which 0s and 1s are equally frequent gives one bit per binary digit; any other code gives less than one bit per digit (p. 30). So a noiseless binary channel's capacity equals its binary-digit rate, and a noisy one's is lower (Figure 2.4) (p. 30).

*Intuition note.* The setup separates the message (what we want to say), the code (how we write it) and the channel (what can go wrong). Capacity limits the channel, and rate describes what a particular code achieves.

### 2.3 Shannon's desiderata
Shannon required a useful measure of information to have four properties (p. 31):
1. *Continuity*: information changes smoothly as the outcome's probability changes.
2. *Symmetry*: information in a sequence of outcomes does not depend on their order.
3. *Maximal value*: information in a set of outcomes cannot be increased if the outcomes are already equally probable.
4. *Additive*: information in a set of outcomes is obtained by adding the information of the individual outcomes.

The author states that Shannon proved the definition below is the only one with all four properties (p. 31).

### 2.4 Information, surprise and entropy
For a coin with p(head) = 0.9, a head is unsurprising and a tail is more surprising. The more improbable an outcome, the more surprise (p. 31). Defining surprise as $1/p(x)$ would increase with improbability, but to satisfy additivity Shannon showed it is better to use the logarithm of $1/p(x)$. This is the *Shannon information*, also called *surprisal* (p. 31). In bits:
$$h(x)=\log_2\frac1{p(x)}\ \text{bits}\tag{2.26}$$
$$\log_2\frac1{p(x)}=-\log_2p(x)\tag{2.27}$$
$$h(x)=-\log_2p(x)\ \text{bits}\tag{2.28}$$
The subscript 2 is usually omitted (p. 32).

**Needing p(X).** Surprise can only be evaluated if the probability of each outcome is known. The probabilities may be estimated from outcomes observed over a long time (p. 33).

**Entropy is average Shannon information.** The average surprise of $X$ with distribution $p(X)$ is its entropy $H(X)$. Strictly, entropy refers to the distribution $p(X)$, though we speak of the entropy of the variable (p. 33). For a sequence of $n$ flips,
$$H(X)\approx\frac1n\sum_{i=1}^n\log\frac1{p(x_i)}\tag{2.29}$$
(p. 33).

**Fair coin.** $h(x_h)=\log(1/0.5)=1$ bit (2.30–2.32), and a tail is also 1 bit (p. 34). Take 100 independent flips with exactly 50 heads and 50 tails (an assumption "for the sake of argument") (p. 35):
$$H(X)=\frac{\big[\sum_{j=1}^{50}\log\frac1{p(x_h)}\big]+\big[\sum_{j=1}^{50}\log\frac1{p(x_t)}\big]}{100}\tag{2.33}$$
$$=\frac{[50\log(1/p(x_h))]+[50\log(1/p(x_t))]}{100}\tag{2.34}$$
$$=[0.5\log(1/0.5)]+[0.5\log(1/0.5)]\tag{2.35}$$
$$=1\ \text{bit per coin flip.}\tag{2.36}$$
The two $50/100$ weights become the probabilities (p. 35).

**Interpreting entropy.** The author says entropy is the logarithm of the number $m$ of equally probable outcome values:
$$H(X)=\log m\ \text{bits}\tag{2.37}$$
For the fair coin, $m=2$, so $H=\log2=1$ bit (2.38–2.39) (p. 35). Raising 2 to both sides:
$$m=2^{H(X)}\tag{2.40}$$
$$=2\ \text{equally probable values}\tag{2.41}$$
Key point: a variable with entropy $H(X)$ bits provides enough information to choose between $2^{H(X)}$ equally probable alternatives (p. 36).

**Biased coin, p(head) = 0.9.** Its average uncertainty is lower than a fair coin's (Figure 2.6) (p. 36).
- $h(x_h)=\log(1/0.9)=0.15$ bits (2.42–2.43).
- $h(x_t)=\log(1/0.1)=3.32$ bits (2.44–2.45).
- The more surprising outcome carries more information (p. 36).

Over 100 flips we expect 90 heads and 10 tails:
$$H(X)=\frac1{100}\Big[\sum_{j=1}^{90}\log\frac1{p(x_h)}+\sum_{j=1}^{10}\log\frac1{p(x_t)}\Big]\tag{2.46}$$
$$=\frac1{100}[90\log(1/p(x_h))+10\log(1/p(x_t))]\tag{2.47}$$
$$=[0.9\log(1/0.9)]+[0.1\log(1/0.1)]\tag{2.48}$$
$$=0.469\ \text{bits per coin flip.}\tag{2.49}$$
Equations 2.50–2.51 write the same as $p(x_h)\log(1/p(x_h))+p(x_t)\log(1/p(x_t))$. With $x_1=x_t$, $x_2=x_h$,
$$H(X)=\sum_{i=1}^2p(x_i)\log\frac1{p(x_i)}=0.469\ \text{bits per coin flip}\tag{2.52–2.53}$$
(p. 37). The average uncertainty is lower even though a tail is more surprising here (3.32 bits) than for a fair coin (1 bit). The text states that no biased coin can have more average uncertainty than an unbiased coin (Figure 2.6) (p. 37). The author says 1,000 flips could be represented using as little as 469 binary digits, a point the text says it will return to ("as we will see later") (p. 37).

Equivalent number of values:
$$m=2^{H(X)}=2^{0.469}=1.38\ \text{equally probable values}\tag{2.54–2.56}$$
So the coin's entropy equals that of an imaginary die with 1.38 sides. The author calls this odd at first sight, but an intuitive guide (p. 38).

**Summary.** For $p(X)=\{p(x_1),\dots,p(x_m)\}$ (2.57):
$$H(X)=\sum_{i=1}^mp(x_i)\log\frac1{p(x_i)}\tag{2.58}$$
$$H(X)=E[\log(1/p(x))]\ \text{bits}\tag{2.59}$$
where $E$ is the expected (average) value (p. 38).

*Intuition note.* Surprise belongs to one outcome; entropy is the average over all outcomes, weighted by how often each occurs. A lopsided coin is mostly predictable, so its rare surprises do not raise its average much.

### 2.5 Evaluating entropy
As the sample size $n\to\infty$, the estimate from a sample converges to the $H(X)$ calculated from the distribution (p. 39).

**From a distribution.** A fair 8-sided die has $A_x=\{1,\dots,8\}$ (2.60) and uniform $p(X)=\{1/8,\dots,1/8\}$ (2.61) (Figure 2.7). Then
$$H(X)=\sum_{i=1}^{8}\tfrac18\log\frac1{1/8}=\log8=3\ \text{bits}\tag{2.62–2.64}$$
and $m=2^3=8$ equally probable values (2.65–2.67) (p. 39). For an $m$-sided die, $p(x_i)=1/m$ and
$$H(X)=\sum_{i=1}^m\tfrac1m\log\frac1{1/m}=\log m\ \text{bits}\tag{2.68–2.69}$$
Substituting $p(x_i)=1/m$ into 2.65 gives $2^{H(X)}=1/p(x_i)$ (2.70), so
$$p(x_i)=2^{-H(X)}\tag{2.71}$$
(p. 40).

**From a sample.** For $n=1{,}000$ throws $\mathbf x=(x_1,\dots,x_n)$, with $h(x_j)=\log1/p(x_j)$ (2.72), the sample average is
$$\bar h(\mathbf x)=\frac1n\sum_{j=1}^nh(x_j)=\frac1n\sum_{j=1}^n\log\frac1{p(x_j)}\ \text{bits}\tag{2.73–2.74}$$
(p. 40). For large $n$, $\bar h(\mathbf x)\approx H(X)$ (2.75) (p. 41). Eq. 2.74 sums over $n$ instances, which can repeat; Eq. 2.58 sums over the $m$ unique outcomes, and usually $n\gg m$ (p. 41). Both give the average Shannon information of a single value (p. 41).

### 2.6 Properties of entropy
Entropy measures uncertainty. Gaining information reduces uncertainty, so information and entropy are "two sides of the same coin" (p. 41). Average information has the same definition as entropy. Whether we call a quantity information or entropy usually depends on whether it is being given to us or taken away (p. 42). If we are told the value of $X$, we receive on average information exactly equal to its entropy (p. 42).

**Doubling the sides.** Going from 8 to 16 sides gives $H=\log16=4$ bits, which adds exactly one bit ($\log2$) (p. 42). Key point: doubling the number of possible values adds one bit.

**Doubling the numbers on each side.** Relabelling the 8-sided die with $\{2,4,\dots,16\}$ leaves each probability at $1/8$, so $H=3$ bits (p. 43). The text contrasts this with continuous variables, where doubling the values does change entropy (Section 5.5, not covered here) (p. 43). Key point: the entropy of a discrete variable depends only on its probability distribution. Changing the values leaves it unchanged if the number of values stays the same (p. 43).

*Intuition note.* Entropy counts how uncertain we are, not what the outcomes are called. Renaming outcomes changes nothing, but doubling the number of equally likely outcomes adds one bit.

### 2.7 Independent and identically distributed values
Values drawn independently from the same distribution are *iid* (independent and identically distributed) (p. 43). Eq. 2.58 gives the entropy of a sequence only if its values are iid. If consecutive values are related (e.g. English text), they are not iid and the sequence has less entropy than the summed individual entropies from Eq. 2.58 (p. 43). A source whose underlying distribution stays constant over time is *stationary*. All sources in the text are assumed stationary unless stated otherwise (p. 43).

### 2.8 Bits, Shannons and bans
The maximum information of a discrete variable is $\log m$ for $m$ equally probable values. A binary variable conveys up to 1 bit (p. 43). The number depends on the logarithm base, as an amount of water can be two pints or about 1.14 litres (p. 44).
- Base $e$ gives *nats*.
- Base 10 gives *bans*, named by British code-breakers at Bletchley Park after Banbury, where the printed cards ("banburies") came from. The method was called Banbarismus (p. 44).
- Because "bit" is often misused for a binary digit, the less ambiguous name is the *Shannon* (Sh) (p. 44).

### 2.9 Summary
Entropy is the average surprise of a variable such as a coin flip or die throw, and it requires a sound grasp of probability, random variables and distributions (p. 44).

## Toy example (ours, not from the text)
A source emits symbols $a,b,c$ with $p=\{1/2,1/4,1/4\}$.
- Surprisals: $h(a)=\log_2 2=1$ bit; $h(b)=h(c)=\log_2 4=2$ bits.
- Entropy by Eq. 2.58: $H=\tfrac12(1)+\tfrac14(2)+\tfrac14(2)=0.5+0.5+0.5=1.5$ bits.
- Equivalent number of values: $2^{1.5}\approx2.83$. This is below 3, matching the maximal-value property: $\log_2 3\approx1.585>1.5$.
- Sample check (Eq. 2.74): a sample of 8 outcomes with 4 $a$, 2 $b$, 2 $c$ has average surprisal $(4\cdot1+2\cdot2+2\cdot2)/8=12/8=1.5$ bits, equal to $H$. The sample frequencies here happen to equal the probabilities exactly.

## Concepts
- [[bit]] — unit of information from base-2 logarithms; a binary variable conveys up to one bit (p. 43). The author prefers "Shannon" (Sh) because "bit" is often misused for binary digit (p. 44).
- [[self-information-surprisal]] — $h(x)=-\log_2p(x)$ bits; surprise of one outcome (p. 32).
- [[entropy]] — average Shannon information $H(X)=\sum p(x_i)\log(1/p(x_i))=E[\log(1/p(x))]$; strictly a property of the distribution (p. 33, p. 38).
- [[channel-capacity]] — maximum information communicable from channel input to output; maximum rate over all codes (p. 29).
- [[noisy-channel]] — channel that may corrupt codewords by noise, so $y_j\ne x_j$ (p. 28).
- [[redundancy]] — natural redundancy can be removed by compression; redundancy may be added against noise (p. 28).
- [[random-variable]] (new) — function mapping experiment outcomes to numeric outcome values (p. 23).
- [[probability-distribution]] (new) — probabilities of all values of a variable; sums to 1 (p. 22, p. 27).
- [[encoder-codeword-code]] (new) — encoder $g$ maps messages to codewords; a code is a symbol–codeword look-up table (p. 27–28).
- [[lossless-vs-lossy-compression]] (new) — lossless allows perfect recovery; lossy discards information (p. 28).
- [[shannon-desiderata]] (new) — continuity, symmetry, maximal value, additivity (p. 31).
- [[iid-and-stationary-source]] (new) — independent draws from one distribution; stationary means the distribution is constant over time (p. 43).
- [[nats-bans-shannons]] (new) — information units for log base $e$, base 10, and base 2 (p. 44).

## Canonical instances
- [[fair-coin]] — 1 bit per flip; both outcomes 1 bit (p. 34–35).
- [[biased-coin-0.9]] — 0.15 bits per head, 3.32 per tail, entropy 0.469 bits, equal to a 1.38-sided die (p. 36–38).
- [[eight-sided-die]] — uniform over 8 outcomes, 3 bits; 16 sides gives 4 bits (p. 39, p. 42).
- [[code-table-2-1]] — eight numbers encoded as 3-bit codewords (p. 28).
- [[bucket-analogy-capacity]] — capacity as bucket size, rate as water poured in (p. 29).

## Bridges (candidates)
- [structural-analogy] Entropy as average surprisal ↔ statistics: sample mean converging to the expected value $E[\cdot]$ — Eq. 2.74 is a sample mean of $-\log p$, and Eq. 2.58 is its expectation.
- [structural-analogy] $2^{H}$ as equivalent number of equally probable values ↔ ecology/social science: "effective number" of categories (e.g. effective number of parties) — both turn a diversity index into a count of equal-weight categories. (Not stated in this unit.)
- [metaphor] Channel capacity as a bucket's size ↔ everyday volume: the rate is the amount actually poured (the author's own analogy).

## Questions this raises
- Why is the logarithm the only function meeting all four desiderata? The unit cites Shannon's proof but gives none.
- If values are not iid (as in English), how is the entropy of a sequence computed? Eq. 2.58 over-estimates it (p. 43).
- What is the entropy-based limit on compressing 1,000 flips of the 0.9 coin to 469 binary digits, and how is it reached? (promised "later", p. 37)
- Why does doubling the values of a continuous variable change its entropy when it does not for a discrete one (Section 5.5)?

## Reading notes
- Printed page = pdf page − 16. Citations use printed numbers.
- The chapter has no exercises.
- Section 2.7 defines iid as values "chosen independently from the same uniform distribution" (p. 43). The word "uniform" looks like an inaccuracy, since the next paragraph says "the same distribution" and the coin example 0.9 distribution is non-uniform.
- Eq. 2.37 is introduced "in general" as $\log m$ for equally probable values. The 0.469-bit coin example (1.38-sided die) applies it as an equivalence, not as an actual die.
- The text layer for equations was mostly readable. The page images match the transcribed equation numbers (2.1–2.75).
- The unit mentions later sections (3.4, 3.5, 4.7, Chapter 5, Appendices B–F). These are not in this unit and are not summarised.
