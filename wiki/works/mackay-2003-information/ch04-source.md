---
id: mackay-2003-information/ch04-source
work: mackay-2003-information
unit: "4 The Source Coding Theorem"
pages: 66–89
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Source Coding Theorem (MacKay, ch. 4)

## L0 — One line
For N independent, identically distributed symbols from a source with entropy H, the number of bits needed to describe them with any fixed error probability δ (0 < δ < 1) is close to NH, because almost all probability lies in a "typical set" of about 2^{NH} strings.

## L1 — The gist (≤ 120 words)
The chapter asks how to measure the information in a random outcome, and how few bits per symbol a source needs. It first argues, through a weighing puzzle, a yes/no guessing game, the game of submarine and an invented language, that h = log₂(1/p) and entropy H are sensible measures. It then defines the essential bit content H_δ: the log-size of the smallest set of outcomes with probability at least 1−δ. Theorem 4.1 says (1/N)H_δ(X^N) is within ε of H for large N, for any δ strictly between 0 and 1. The proof uses the typical set and the law of large numbers. So entropy is the compressed size per symbol, which links information measures to coding.

**Prerequisites:** logarithms base 2; probability, independence, expectation and variance; the binomial distribution; sums over sets.

## L2 — Key ideas
- Shannon information content h(x)=log₂(1/p) is additive for independent outcomes, and entropy H(X) is its average (pp. 67–68).
- Informative experiments have outcomes as close to equiprobable as possible. In the 12-ball weighing problem, 3² < 24 ≤ 3³ shows that two weighings cannot be enough, while three might suffice (pp. 68–70).
- In sixty-three and in submarine, the total information gained is log₂ of the number of hypotheses, however the outcomes unfold (pp. 70–72).
- Raw bit content H₀=log₂|A| ignores probabilities. Allowing failure probability δ gives the essential bit content H_δ=log₂|S_δ|, where S_δ is the smallest set of probability ≥ 1−δ (pp. 74–75).
- Source coding theorem (Thm 4.1): for N i.i.d. (independent, identically distributed) symbols and any 0<δ<1, (1/N)H_δ(X^N) is within ε of H for N large. The same rate H applies whether the allowed error is tiny or close to 1 (pp. 78, 83).
- Typical set T_{Nβ}: strings whose (1/N)log₂(1/P) is within β of H. It holds almost all probability and has about 2^{NH} members (pp. 80, 82, 84).
- The proof uses the typical set and the weak law of large numbers (the average of many independent variables is close to their common mean with high probability), which the text derives from Chebyshev's inequality (a bound on how likely a variable is to be far from its mean, in terms of its variance). The law is proved only for finite discrete variables, for which mean and variance exist; the Cauchy distribution (a continuous distribution with no mean or variance) shows that the mean of N samples need not narrow without such conditions (pp. 81–83, 85, 88).
- "Equipartition" (the idea that typical strings have roughly equal probability) is weak: the probabilities of typical strings can differ by an exponentially large factor (pp. 83–84).

## L3 — Walkthrough

### About Chapter 4 and Exercise 4.1 (p. 66)
The chapter is about measuring the information content of a random experiment's outcome. The author says it has "tough bits"; if the maths is hard, skim it, since Chapters 5 and 6 can be enjoyed without this chapter's tools (p. 66).

Notation (p. 66): x∈A (member), S⊂A (subset), S⊆A (subset or equal), B∪A (union), B∩A (intersection), |A| (number of elements).

**Exercise 4.1 (weighing problem).** There are 12 balls, all equal in weight except one that is heavier or lighter. A two-pan balance gives three outcomes: equal, left heavier, left lighter. The task is to find the odd ball and whether it is heavy or light in as few weighings as possible. The author's guiding questions ask how to measure information, how much is gained, and how much is gained at the first step with 6 v 6 versus 4 v 4 (p. 66).

### 4.1 How to measure the information content of a random variable (pp. 67–73)

**Ensemble** (p. 67). An ensemble X is a triple (x, A_X, P_X). The outcome x takes a value in A_X={a₁,…,a_I} with probabilities P_X={p₁,…,p_I}, p_i ≥ 0, Σp_i=1.

The chapter examines two assertions (p. 67):

$$h(x=a_i)\equiv\log_2\frac{1}{p_i}\tag{4.1}$$

(Shannon information content), and

$$H(X)=\sum_i p_i\log_2\frac{1}{p_i}\tag{4.2}$$

(entropy, the average information content of the ensemble).

The binary entropy function is

$$H_2(p)=H(p,1-p)=p\log_2\frac1p+(1-p)\log_2\frac{1}{1-p}\tag{4.3}$$

Figure 4.1 gives these values (p. 67):

| p | h(p) | H₂(p) |
|---|---|---|
| 0.001 | 10.0 | 0.011 |
| 0.01 | 6.6 | 0.081 |
| 0.1 | 3.3 | 0.47 |
| 0.2 | 2.3 | 0.72 |
| 0.5 | 1.0 | 1.0 |

The less probable an outcome, the greater its h (p. 67).

**Independent variables** (p. 68). Independence means

$$P(x,y)=P(x)P(y)\tag{4.4}$$

The author says we might want information to be additive for independent variables. Then

$$h(x,y)=\log\frac{1}{P(x,y)}=\log\frac1{P(x)P(y)}=\log\frac1{P(x)}+\log\frac1{P(y)}\tag{4.5}$$

so

$$h(x,y)=h(x)+h(y)\ \text{ if $x$, $y$ independent.}\tag{4.6}$$

Exercise 4.2 asks for the entropy version, H(X,Y)=H(X)+H(Y) (4.7). The author's solution is on p. 86 (see 4.8 below). The author says the question "why log 1/p and not some other function" will be explored later, and that sections 4.4 and Chapters 5–6 relate h and H to the number of bits needed to describe an outcome (p. 68).

> *Intuition note.* Surprises from unrelated events should just add up, and a logarithm turns the product of probabilities into a sum. The author points this out as a nice property of this particular h; why log 1/p rather than some other function is left to be explored later (p. 68).

**The weighing problem** (pp. 68–70).
- Three weighings have 3³=27 conceivable outcomes. There are 24 states of the world (12 balls × heavy/light). So three weighings might suffice, but two cannot, since 3²<24 (p. 68).
- At each step of an optimal procedure, the three outcomes are as close as possible to equiprobable (p. 68). Figure 4.2 shows an optimal solution. The first weighing is balls 1234 v 5678, and the next weighings depend on the outcome (p. 69).
- A suboptimal first weighing, 1–6 v 7–12, can never balance. A binary outcome rules out only half the hypotheses, so such a strategy must sometimes take longer (pp. 68–70).
- The first weighing must split the 24 hypotheses into three groups of eight. The second must give a 3:3:2 split (p. 70).
- The author's conclusion: the outcome of a random experiment is guaranteed to be most informative if its distribution is uniform. This agrees with the entropy property of exercise 2.25 (entropy is largest when p_i=1/|A_X|) (p. 70).

> *Intuition note.* A question whose answers are equally likely cuts the remaining possibilities as much as any three-way question can. A question with lopsided outcomes rules out fewer hypotheses, so a strategy built on it must sometimes take longer.

**Guessing games: sixty-three** (p. 70). Example 4.3: what is the smallest number of yes/no questions needed to identify an integer x in 0–63? Six questions suffice: "x≥32?", "x mod 32≥16?", "x mod 16≥8?", "x mod 8≥4?", "x mod 4≥2?", "x mod 2=1?". The answers (yes→1, no→0) give the binary expansion of x, e.g. 35 ⇒ 100011.

If all x are equally likely, the answers are independent. Each has information log₂(1/0.5)=1 bit, so the total is always six bits. The questioning strategy encodes x as a binary file. The author asks whether h also makes sense for unequal probabilities (p. 70).

**Submarine** (pp. 71–72). One submarine hides in one square of an 8×8 grid. Each shot is an ensemble with outcomes {y (hit), n (miss)}. Initially P(y)=1/64. After one miss, P(y)=1/63, and so on (p. 71).
- Hit on the first shot: h=log₂64=6 bits (4.8). The author notes that one lucky binary outcome conveys six bits because it fixes one of 64 squares (p. 71).
- First miss: h=log₂(64/63)=0.0227 bits (4.9). Second miss: log₂(63/62)=0.0230 bits (4.10).
- After 32 misses the total is

$$\log_2\tfrac{64}{63}+\log_2\tfrac{63}{62}+\dots+\log_2\tfrac{33}{32}=0.0227+0.0230+\dots=1.0\text{ bits}\tag{4.11}$$

This equals one bit because learning "not in these 32 squares" is the same as the first answer "no" in sixty-three (p. 72). After 48 misses the gain is 2 bits (the location is narrowed to a quarter of the space).
- Hit on the 49th shot, with 16 squares left: h=log₂16=4.0 bits (4.12). The total over all outcomes is

$$\log_2\tfrac{64}{63}+\dots+\log_2\tfrac{17}{16}+\log_2\tfrac{16}{1}=0.0227+0.0230+\dots+0.0874+4.0=6.0\text{ bits}\tag{4.13}$$

- The total is 6 bits whenever the hit occurs, with n squares left:

$$\log_2\!\left[\tfrac{64}{63}\times\tfrac{63}{62}\times\dots\times\tfrac{n+1}{n}\times\tfrac n1\right]=\log_2\tfrac{64}{1}=6\text{ bits}\tag{4.14}$$

The author concludes that submarine makes a convincing case that h is a sensible measure. Sixty-three connects h to the size of a file that encodes outcomes, which hints at data compression (p. 72).

> *Intuition note.* Each miss tells you very little, but the small amounts add up (the fractions cancel in the product) to exactly the information in "where is it?". The total does not depend on how lucky you were.

**Wenglish** (pp. 72–73). A Wenglish dictionary has 2¹⁵=32,768 words, each of 5 letters. Each word was built by drawing five letters from the letter distribution of figure 2.1. This is far fewer than 26⁵≃12,000,000 possible words. Because P(z)≈1/1000, only 32 words start with z. Because P(a)≈0.0625, 2048 start with a; of these, two start az and 128 start aa (p. 72).
- Read word by word, each word has h=log 32,768=15 bits (all words equally likely), so 3 bits per character (p. 73).
- Read letter by letter, the first letter has h≃log(1/0.0625)≃4 bits if it is a, and ≃log(1/0.001)≃10 bits if it is z. So the first-character information is highly variable. The five characters together carry exactly 15 bits, so letters after an initial z carry less on average than letters after an initial a (p. 73).

### 4.2 Data compression (pp. 73–74)
The author says the examples justify h as a natural measure: improbable outcomes convey more information. He now asks how many bits are needed to describe a source's outcome. If data from a source can be compressed to a file of L bits per symbol and recovered reliably, the source's average information content is *at most* L bits per symbol (p. 73).

**Text files** (p. 73). A byte has 8 bits. ASCII uses only 7 of them. Exercise 4.4 asks how much an ASCII file can shrink. Intuitively an ASCII file holds 7/8 as much information as an arbitrary file of the same size. This is a simple case of redundancy; English text has more (unequal character frequencies, likely letter pairs, predictable words) (p. 73).

**Raw bit content** (p. 74).

$$H_0(X)=\log_2|A_X|\tag{4.15}$$

H₀ is a lower bound for the number of binary questions always guaranteed to identify an outcome. It is additive:

$$H_0(X,Y)=H_0(X)+H_0(Y)\tag{4.16}$$

since the pair has |A_X||A_Y| outcomes. It contains no probabilities, and the code it corresponds to maps each outcome to a constant-length string, so it does not compress (p. 74).

Exercise 4.5 asks whether a compressor could give every outcome a code shorter than H₀ bits. The author says a simple counting argument shows no reversible program can shrink all files, and ridicules claims that a program can compress files repeatedly (p. 74).

There are only two ways a compressor can actually compress (p. 74):
1. **Lossy**: some files share an encoding. Let δ be the probability that the source string is one of these confusable files; this is the probability of failure.
2. **Lossless**: all files get different encodings. If some are shortened, others must be lengthened. Design aims for a small probability of lengthening and a large probability of shortening.

This chapter treats a simple lossy compressor; later chapters treat lossless ones (p. 74).

### 4.3 Information content defined in terms of lossy compression (pp. 74–78)
To distinguish a text file where all 128 ASCII characters are equally likely from one with English frequencies, we must take probabilities into account. The latter should hold less information per character because it is more predictable (pp. 74–75). The idea is to drop improbable symbols from the alphabet and take the raw bit content of the smaller alphabet. The parameter δ is the probability that an outcome has no name (p. 75).

**Example 4.6** (p. 75). A_X={a,…,h} and P_X={1/4,1/4,1/4,3/16,1/64,1/64,1/64,1/64}. H₀=3 bits (8 names). But P(x∈{a,b,c,d})=15/16. With risk δ=1/16, four names suffice, which is 2 bits. Table 4.5 gives the names: for δ=0, 3-bit codes 000–111; for δ=1/16, a–d get 00, 01, 10, 11 and e–h get none.

**Smallest δ-sufficient subset** S_δ: the smallest subset of A_X satisfying

$$P(x\in S_\delta)\ge 1-\delta\tag{4.18}$$

Construction: rank elements by decreasing probability and add them until the total probability is ≥ 1−δ. (If several elements tie in probability, only the size of S_δ matters.) (p. 75)

**Essential bit content**

$$H_\delta(X)=\log_2|S_\delta|\tag{4.19}$$

H₀ is the special case δ=0 (if P(x)>0 for all x). H_δ should not be confused with H₂(p) (p. 75). Figure 4.6 shows H_δ(X) for example 4.6 as a staircase falling from 3 bits at δ=0 (passing H_{1/16}=2 bits) down to the single set {a}; the labels on the steps are the sets {a,…,h}, {a,…,g}, …, {a} (p. 76).

**Extended ensembles** (p. 76). Let x=(x₁,…,x_N) be N i.i.d. draws from X; call this ensemble X^N. By additivity (exercise 4.2), H(X^N)=NH(X).

**Example 4.7** (bent coin). Flip a coin N times, with p₀=0.9 and p₁=0.1. If r(x) is the number of 1s,

$$P(\mathbf x)=p_0^{\,N-r(\mathbf x)}\,p_1^{\,r(\mathbf x)}\tag{4.20}$$

The smallest sufficient set S_δ contains all x with r=0,1,…,r_max(δ)−1 and some with r=r_max(δ). Figures 4.7 (N=4) and 4.8 (N=10) plot H_δ(X^N) against δ. The steps are the δ values where |S_δ| changes by one; the cusps are where r_max changes (p. 76). Exercise 4.8 asks for the shape between cusps; the author's answer is that H_δ varies logarithmically with (−δ) (p. 86).

H_δ(X^N) depends strongly on δ for these small N, which makes it look like a poor definition. But the author announces that as N grows, H_δ(X^N) becomes almost independent of δ and close to NH(X) for all δ (p. 76). Figure 4.9 shows (1/N)H_δ(X^N) for N=10, 210, …, 1010 flattening, except for tails near δ=0 and δ=1 (pp. 77–78).

**Theorem 4.1 (Shannon's source coding theorem).** Let X be an ensemble with entropy H(X)=H bits. Given ε>0 and 0<δ<1, there exists a positive integer N₀ such that for N>N₀,

$$\left|\frac1N H_\delta(X^N)-H\right|<\epsilon\tag{4.21}$$

(p. 78). In words: with a tiny allowed error probability, compression down to NH bits is possible; even with a large allowed error probability, we can compress only down to NH bits (p. 78).

> *Intuition note.* For a single symbol or a short block, how many bits you need depends heavily on how much failure you accept. For long blocks the answer settles at H bits per symbol, almost whatever failure probability you accept (as long as it is strictly between 0 and 1).

### 4.4 Typicality (pp. 78–84)
**Why large N helps** (pp. 78–80). For a string with r 1s and N−r 0s:

$$P(\mathbf x)=p_1^{\,r}(1-p_1)^{N-r}\tag{4.22}$$

$$n(r)=\binom Nr\tag{4.23}$$

$$P(r)=\binom Nr p_1^{\,r}(1-p_1)^{N-r}\tag{4.24}$$

r is binomial with mean Np₁ and standard deviation √(Np₁(1−p₁)). For p₁=0.1:

$$N=100:\ r\sim Np_1\pm\sqrt{Np_1(1-p_1)}\simeq 10\pm3\tag{4.25}$$

$$N=1000:\ r\sim 100\pm 10\tag{4.26}$$

The possible range of r grows as N but its standard deviation grows only as √N. So r, and hence the outcome x, lies mostly in a small subset, the typical set (p. 80). Figure 4.10 shows 15 random strings from X^100 with p₁=0.1. Their log₂P ranges from −37.3 to −65.9 bits, compared with H(X¹⁰⁰)=46.9 bits. The all-zeros string has log₂P=−15.2 and the all-ones string has −332.1 (p. 78). Figure 4.11 plots n(r), P(x) and n(r)P(x) for N=100 and 1000 (p. 79).

**Definition** (p. 80). A long string usually contains about p_iN occurrences of the i-th symbol, so

$$P(\mathbf x)_{\rm typ}\simeq p_1^{(p_1N)}p_2^{(p_2N)}\cdots p_I^{(p_IN)}\tag{4.27}$$

$$\log_2\frac1{P(\mathbf x)}\simeq N\sum_i p_i\log_2\frac1{p_i}=NH\tag{4.28}$$

So log₂(1/P(x)) is very likely close to NH. Typical elements are those with probability close to 2^{−NH}. With a closeness parameter β:

$$T_{N\beta}\equiv\left\{\mathbf x\in A_X^N:\left|\frac1N\log_2\frac1{P(\mathbf x)}-H\right|<\beta\right\}\tag{4.29}$$

The author notes that the typical set, unlike S_δ, does *not* contain the most probable strings, but these contribute negligible probability (p. 80).

**'Asymptotic equipartition' principle** (p. 80). For N i.i.d. variables X^N with N sufficiently large, the outcome is almost certain to lie in a subset of A_X^N with only 2^{NH(X)} members, each of probability "close to" 2^{−NH(X)}. If H(X)<H₀(X), then 2^{NH(X)} is a tiny fraction of |A_X|^N=2^{NH₀(X)}. "Equipartition" here means roughly equal probability, not the thermal-physics sense (each degree of freedom has energy ½kT) (p. 80).

**Verbal form of the source coding theorem** (p. 81). N i.i.d. variables, each with entropy H(X), can be compressed into more than NH(X) bits with negligible risk of information loss as N→∞. Conversely, if compressed into fewer than NH(X) bits, it is virtually certain that information will be lost. The author says this is equivalent to the AEP, because one can give each typical x a distinct name of NH(X) bits (p. 81).

### 4.5 Proofs (pp. 81–83)
The author says this section may be skipped.

**Law of large numbers** (p. 81).
- Mean ū=E[u]=Σ_u P(u)u. Variance σ_u²=E[(u−ū)²]=Σ_u P(u)(u−ū)².
- Technical note: u is assumed to be a function u(x) of a sample from a *finite discrete* ensemble. This guarantees that mean and variance exist, which need not hold for general P(u).

**Chebyshev's inequality 1** (p. 81). For a non-negative random variable t and α>0,

$$P(t\ge\alpha)\le\frac{\bar t}{\alpha}\tag{4.30}$$

Proof: P(t≥α)=Σ_{t≥α}P(t). Multiply each term by t/α≥1 to get P(t≥α)≤Σ_{t≥α}P(t)t/α. Add the non-negative missing terms to get ≤Σ_t P(t)t/α=t̄/α.

**Chebyshev's inequality 2** (p. 82). For a random variable x and α>0,

$$P\big((x-\bar x)^2\ge\alpha\big)\le\sigma_x^2/\alpha\tag{4.31}$$

Proof: take t=(x−x̄)² in inequality 1.

**Weak law of large numbers** (p. 82). Let x be the average of N independent variables h₁,…,h_N with common mean h̄ and variance σ_h². Then

$$P\big((x-\bar h)^2\ge\alpha\big)\le\sigma_h^2/(\alpha N)\tag{4.32}$$

The proof is by showing x̄=h̄ and σ_x²=σ_h²/N (then apply 4.31) (added step: combining the two). However small α, or the desired failure probability, or however large σ_h², N can be chosen large enough (p. 82).

**Proof of Theorem 4.1** (pp. 82–83). Apply the law of large numbers to (1/N)log₂(1/P(x)). This is the average of N terms h_n=log₂(1/P(x_n)), each with mean H and variance σ²≡var[log₂(1/P(x_n))]. Define the typical set with a squared condition:

$$T_{N\beta}=\left\{\mathbf x\in A_X^N:\left[\frac1N\log_2\frac1{P(\mathbf x)}-H\right]^2<\beta^2\right\}\tag{4.33}$$

For all x∈T_{Nβ},

$$2^{-N(H+\beta)}<P(\mathbf x)<2^{-N(H-\beta)}\tag{4.34}$$

and by the law of large numbers

$$P(\mathbf x\in T_{N\beta})\ge1-\frac{\sigma^2}{\beta^2N}\tag{4.35}$$

This proves the AEP: as N increases, P(x∈T_{Nβ}) approaches 1 for any β (p. 82).

*Part 1: (1/N)H_δ(X^N) < H+ε.* T_{Nβ} need not be the best subset, so its size bounds H_δ from above. The smallest probability of a member is 2^{−N(H+β)} and the total probability is at most 1, so

$$|T_{N\beta}|\,2^{-N(H+\beta)}<1\tag{4.36}$$

$$|T_{N\beta}|<2^{N(H+\beta)}\tag{4.37}$$

Set β=ε and choose N₀ with σ²/(ε²N₀)≤δ. Then P(T_{Nβ})≥1−δ, so T_{Nβ} witnesses H_δ(X^N)≤log₂|T_{Nβ}|<N(H+ε) (p. 82).

*Part 2: (1/N)H_δ(X^N) > H−ε.* Suppose a rival subset S′ has |S′|≤2^{N(H−2β)} and P(x∈S′)≥1−δ, with β=ε/2. We show it cannot exist for large N (p. 83). Split

$$P(\mathbf x\in S')=P(\mathbf x\in S'\cap T_{N\beta})+P(\mathbf x\in S'\cap\overline{T_{N\beta}})\tag{4.38}$$

The first term is at most 2^{N(H−2β)} elements, each at most 2^{−N(H−β)}. The second is at most P(x∉T_{Nβ}). So

$$P(\mathbf x\in S')\le 2^{N(H-2\beta)}2^{-N(H-\beta)}+\frac{\sigma^2}{\beta^2N}=2^{-N\beta}+\frac{\sigma^2}{\beta^2N}\tag{4.39}$$

Choose N₀ so that this is <1−δ. Then S′ cannot be δ-sufficient, so any subset of size ≤2^{N(H−ε)} has probability <1−δ, and H_δ(X^N)>N(H−ε). Hence for large N, (1/N)H_δ(X^N) is essentially constant in δ for 0<δ<1 (figures 4.9, 4.13) (p. 83).

> *Intuition note.* Part 1 says "the typical set is small enough to name cheaply and still catches almost everything". Part 2 says "any set smaller than the typical set misses too much probability". Together they pin the cost at NH bits.

### 4.6 Comments (pp. 83–84)
- Part 1 says that even with extremely small δ, the bits per symbol need not exceed H+ε, a big drop from H₀(X). Part 2 says that even if δ is close to 1 (errors most of the time), at least H−ε bits per symbol are still needed. So the number of bits per symbol is H, "no more and no less" (p. 83).
- **Caveat on "equipartition".** Elements of T_{Nβ} have log₂(1/P) within 2Nβ of each other, which is not the same as nearly equal probability. To keep the bound 1−σ²/(β²N) fixed as β shrinks, N must grow as 1/β². Writing β=α/√N, the most probable typical string is "of order" 2^{α√N} times more probable than the least probable one. This ratio grows exponentially, so equipartition holds only in a weak sense (pp. 83–84).
- **Why introduce the typical set?** The best block-compression subset is S_δ, not T. But the typical set can be *counted*: all elements have about probability 2^{−NH} and the set has probability near 1, so it has roughly 2^{NH} elements. Counting S_δ directly would be hard (p. 84).

### 4.7 Exercises (pp. 84–86)
The exercises are listed under "Exercises worth doing" below. Other content in this section:
- Exercises 4.9–4.14 are weighing problems: the information in a 6 v 6 weighing (4.9); 39 balls (4.10); 16 balls with a balance that has only two outcomes (4.11); weights for flour bags of 1–40 pounds (4.12); fixed weighings and the count (3^W−3)/2 (4.13); two odd balls, with an estimate of the number of weighings and a variant with known weights of 99 g, 100 g and 110 g (4.14) (pp. 84–85). Exercise 4.16 asks for sketches of (1/N)H_δ(Y^N) for P_Y={0.5,0.5}, N=1,2,3,100 (p. 85).
- A short passage states that the law of large numbers was proved here only for finite discrete variables. Many continuous distributions also satisfy it, but some do not have a mean or variance (p. 85).
- Exercise 4.18 introduces the Cauchy distribution P(x)=(1/Z)·1/(x²+1) (4.40).
- Exercise 4.19 (Chernoff bound) takes t=exp(sx) in Chebyshev inequality 1, to show

$$P(x\ge a)\le e^{-sa}g(s),\ s>0\tag{4.41}$$

$$P(x\le a)\le e^{-sa}g(s),\ s<0\tag{4.42}$$

with moment-generating function

$$g(s)=\sum_xP(x)e^{sx}\tag{4.43}$$

- Exercise 4.20 asks for a sketch of f(x)=x^{x^{x^{⋰}}} (4.44) (p. 86).

### 4.8 Solutions (pp. 86–89)
- **Ex. 4.2** (p. 86): with P(x,y)=P(x)P(y),

$$H(X,Y)=\sum_{xy}P(x)P(y)\log\frac1{P(x)P(y)}\tag{4.45}$$

$$=\sum_{xy}P(x)P(y)\log\frac1{P(x)}+\sum_{xy}P(x)P(y)\log\frac1{P(y)}\tag{4.46}$$

$$=\sum_xP(x)\log\frac1{P(x)}+\sum_yP(y)\log\frac1{P(y)}\tag{4.47}$$

$$=H(X)+H(Y)\tag{4.48}$$

- **Ex. 4.4**: a file can be reduced by a factor 7/8, by a block code mapping 8-byte blocks to 7-byte blocks, copying the 56 information-carrying bits and ignoring the last bit of each character (p. 86).
- **Ex. 4.5**: pigeon-hole principle. There are only 2^l names of length l, and l<log₂|A_X| implies 2^l<|A_X|, so two inputs share an output (p. 86).
- **Ex. 4.8**: between cusps H_δ varies logarithmically with (−δ) (p. 86).
- **Ex. 4.13** (found by Dyson and Lyness in 1946, presented by Conway in 1999): the 12-ball problem can be solved by three fixed weighings, and in W weighings an odd ball can be identified among

$$N=(3^W-3)/2\tag{4.49}$$

balls (pp. 86–87).
- **Ex. 4.15**: figure 4.14 shows staircase curves for N=1 and N=2 and a nearly flat curve for N=1000; H₂(0.2)=0.72 bits (p. 87).
- **Ex. 4.17**: Gibbs entropy k_B Σp_i ln(1/p_i) equals the Shannon entropy apart from k_B. Boltzmann entropy S_B=k_B ln Ω equals H₀ of a microcanonical ensemble (uniform over accessible states) apart from k_B. The author argues that fixing total energy to precision ε is equivalent to fixing ln(1/P(x)) to within εk_BT, so the microcanonical ensemble is equivalent to a uniform distribution over the typical set of the canonical ensemble P(x)=(1/Z)exp(−E(x)/k_BT) (4.50). The AEP proof then shows that, for a system with separable energy, the Boltzmann entropy of the microcanonical ensemble is close, for large N, to the Gibbs entropy of the canonical ensemble if the energy is fixed at the mean (pp. 87–88).
- **Ex. 4.18** (Cauchy): Z=π (4.51). Mean and variance are undefined. The sum z=x₁+x₂ is Cauchy with width parameter 2 (4.52–4.53). The mean of N samples has the same distribution as a single sample, so it does not narrow as 1/√N. The central-limit theorem does not apply because the variance is not finite. The author also gives an alternative route: the Fourier transform of the Cauchy distribution is a biexponential e^{−|ω|}, convolution becomes multiplication, so the transform of z is e^{−|2ω|} (p. 88).
- **Ex. 4.20**: f has inverse g(y)=y^{1/y} (4.54), log g(y)=(1/y)log y (4.55). The graph suggests f is single-valued on (0,1), two-valued on (1,e^{1/e}) and infinite for x>e^{1/e}≈1.44. The author adds a caveat about the iteration's limit (pp. 88–89).

## Toy example (ours, not from the text)
**Setup.** Bent coin with p₀=0.9, p₁=0.1, as in example 4.7, and N=2 flips.

**Entropy.** H = 0.9·log₂(1/0.9) + 0.1·log₂(1/0.1) = 0.9×0.152 + 0.1×3.322 = 0.137 + 0.332 = 0.469 bits per flip.

**String probabilities.** 00: 0.9×0.9=0.81. 01 and 10: 0.9×0.1=0.09 each. 11: 0.1×0.1=0.01. Sum = 1.

**H_δ(X²).** We need the smallest set with probability ≥ 1−δ.
- δ<0.01: three strings give only 0.81+0.09+0.09=0.99, so we need all 4. H_δ=log₂4=2, so 1 bit per flip.
- 0.01≤δ<0.10: three strings (0.99) suffice, but two strings give only 0.90. H_δ=log₂3=1.585, so 0.79 per flip.
- 0.10≤δ<0.19: two strings (0.81+0.09=0.90≥1−δ). H_δ=1, so 0.5 per flip.
- δ≥0.19: one string (0.81). H_δ=0.

So at N=2, (1/N)H_δ jumps between 1, 0.79, 0.5 and 0, which is far from the flat value H=0.469. The theorem promises flatness only for large N (as in figure 4.9).

**Typicality at N=100.** A string with r=10 ones has log₂P = 90·log₂0.9 + 10·log₂0.1 = 90×(−0.1520) + 10×(−3.3219) = −13.68 − 33.22 = −46.9. This equals −N·H₂(0.1) = −100×0.469 = −46.9, so log₂(1/P)/N=0.469=H: this string is typical. The all-zeros string has log₂P=100×(−0.152)=−15.2 (probability about 2.7×10⁻⁵). It is far more probable than a typical string, but it is one string, and r≈10±3 holds almost all the probability.

## Concepts
- [[ensemble]] — triple (x, A_X, P_X): outcome, alphabet, probabilities (new) (p. 67)
- [[self-information / surprisal]] — Shannon information content h(x)=log₂(1/p); additive for independent outcomes (p. 67)
- [[entropy H(X)]] — Σ p_i log₂(1/p_i), the average Shannon information content; maximal for the uniform distribution (p. 67, p. 70)
- [[bit]] — here also "a binary symbol with two values", distinguished from the unit of information content (p. 73)
- [[redundancy]] — structure making a file compressible, e.g. unused ASCII bit, unequal letter frequencies (p. 73)
- [[raw-bit-content]] — H₀(X)=log₂|A_X|; ignores probabilities (new) (p. 74)
- [[smallest-delta-sufficient-subset]] — smallest S_δ with P(x∈S_δ)≥1−δ (new) (p. 75)
- [[essential-bit-content]] — H_δ(X)=log₂|S_δ|; bits needed with failure probability δ (new) (p. 75)
- [[lossy-vs-lossless-compression]] — lossy: confusable files, failure probability δ; lossless: all encodings distinct, some files lengthen (new) (p. 74)
- [[typical set / AEP]] — T_{Nβ}: strings with (1/N)log₂(1/P) within β of H; holds almost all probability; about 2^{NH} members (p. 80)
- [[source coding theorem]] — (1/N)H_δ(X^N) is within ε of H for N large and 0<δ<1 (Thm 4.1) (p. 78)
- [[chebyshev-inequality]] — P(t≥α)≤t̄/α for non-negative t; the variance form follows (new) (p. 81)
- [[weak-law-of-large-numbers]] — P((x−h̄)²≥α)≤σ_h²/(αN) for the average of N independent variables (new) (p. 82)

## Canonical instances
- [[weighing-problem]] — 12 balls, three-outcome balance; at each step of an optimal strategy the outcomes are as close as possible to equiprobable (pp. 66, 68–70)
- [[sixty-three-game]] — six yes/no questions give a 6-bit binary encoding of x (p. 70)
- [[submarine-game]] — total information is 6 bits regardless of when the hit occurs (pp. 71–72)
- [[wenglish]] — 2¹⁵ equiprobable 5-letter words; 15 bits per word, 3 bits per character (pp. 72–73)
- [[bent-coin-extended-ensemble]] — N flips with p₁=0.1; H_δ(X^N) staircases and typicality (pp. 76–79)
- [[cauchy-distribution]] — no mean or variance; the mean of N samples does not narrow (pp. 85, 88)

## Bridges (candidates)
- [same-math] Shannon entropy H ↔ statistical mechanics: Gibbs entropy k_B Σp_i ln(1/p_i), equal to H up to the factor k_B (p. 87).
- [same-math] Raw bit content H₀ ↔ statistical mechanics: Boltzmann entropy k_B ln Ω for a microcanonical ensemble (p. 87).
- [structural-analogy] Typical set of X^N (high-probability strings are not the single most probable ones) ↔ Bayesian: typical set in high-dimensional posteriors, where mass lies away from the mode.
- [structural-analogy] Submarine: product of conditional probabilities telescopes to log 1/P(location) (4.14) ↔ Bayesian: sequential updating, where the order of evidence does not change the final posterior.

## Questions this raises
- Why log₂(1/p) and not some other function of p? The author promises to explore this but the question is not answered in these pages (p. 68).
- Since NH bits is only the limit for lossy compression with failure probability δ, how can a *lossless* code approach H (the author defers this to later chapters) (p. 74)?
- How large must N be for a given ε and δ? The proof gives only N₀ from σ²/(ε²N₀)≤δ-type bounds. How fast does the flattening in figure 4.9 actually occur?
- What replaces the law of large numbers, and hence the theorem, for sources whose log-probabilities have infinite variance, as for the Cauchy distribution?

## Exercises worth doing
- Ex. 4.1 (p. 66) — design the 12-ball weighing strategy and track information at each node — difficulty: medium
- Ex. 4.9 (p. 84) — information about "which ball" versus "which ball and heavy/light" for a 6 v 6 first weighing — difficulty: easy
- Ex. 4.13 (p. 84) — fixed (non-adaptive) weighing scheme, and the count (3^W−3)/2 — difficulty: hard
- Ex. 4.15 (p. 85) — sketch (1/N)H_δ(X^N) for P_X={0.2,0.8}, N=1, 2, 1000 — difficulty: medium
- Ex. 4.17 (p. 85) — relate the AEP proof to Boltzmann versus Gibbs entropy — difficulty: medium
- Ex. 4.18 (p. 85) — Cauchy distribution: no mean or variance, and sample means do not concentrate — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 12 (pdf 78 = printed 66).
- Eq. (4.11) (p. 71) prints the last term as 0.0430. The figure 4.3 table shows 0.0443 for move 32, and log₂(33/32)≈0.0444, so 0.0430 looks like a misprint.
- Figure 4.14 caption (p. 87) says "p₁=0.4" and "N=1, 2, 100", while exercise 4.15 and its tables use P_X={0.2,0.8} (the table values fit 0.2) and N=1, 2, 1000.
- In the caveat (pp. 83–84) the spread of log₂(1/P) is stated as within 2Nβ, and with β=α/√N the ratio is printed as of order 2^{α√N}. A spread of 2Nβ=2α√N would suggest 2^{2α√N}; only the exponential growth is the stated point.
- The text layer is garbled in figures 4.2, 4.3 and 4.7–4.11; the images were used for these. The weighing tree (fig. 4.2) was not transcribed in full. Exercises 4.9–4.12, 4.14, 4.16 and 4.19 have no printed solution here. Exercise 4.14's questions (pp. 84–85) were only summarized.
