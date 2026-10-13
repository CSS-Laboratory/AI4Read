---
id: cover-2006-elements/ch01-introduction
work: cover-2006-elements
unit: "1 Introduction and Preview"
pages: 1-11
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Introduction and Preview

## L0 — One line
Information theory answers two questions, "how far can data be compressed?" (entropy $H$) and "how fast can data be sent reliably?" (capacity $C$), and its quantities $H, I, C, D, K, W$ recur across physics, computer science, statistics, probability and economics.

## L1 — The gist (≤ 120 words)
The chapter is a map of the book. It states Shannon's two limits: entropy bounds compression, and channel capacity bounds reliable transmission. It defines entropy, mutual information, capacity and relative entropy, and illustrates them with a 32-outcome variable, an eight-horse race and three simple channels. It then lists the fields the authors say the theory touches: communication, Kolmogorov complexity, thermodynamics, probability and statistics, Occam's razor, and investment. The authors argue the theory is more than a branch of communication theory. The same few quantities keep appearing as answers in very different problems. Chapter 2 starts the formal treatment.

**Prerequisites:** discrete probability (mass function, expectation); logarithms base 2; the idea of a random variable. Nothing else is assumed.

## L2 — Key ideas
- Two ultimate limits: compression is bounded by the entropy $H$, and transmission by the channel capacity $C$ (p. 1). The book places all modulation and compression schemes between a compression minimum $\min I(X;\hat X)$ (a mutual-information quantity, defined below) and the transmission maximum $\max I(X;Y)$, the capacity. Every compression scheme needs a description rate at least equal to the minimum (p. 2).
- Shannon's surprise: error need not grow with transmission rate as long as the rate stays below capacity (p. 1).
- Entropy $H(X)=-\sum p(x)\log_2 p(x)$ is the average number of bits needed to describe $X$. The horse-race example reaches $H=2$ bits with a variable-length code, against 3 bits for fixed-length labels (pp. 5–6).
- Capacity is $C=\max_{p(x)} I(X;Y)$, where $I(X;Y)$ is the reduction in uncertainty about $X$ gained by observing $Y$. Over a sequence of transmissions, the book says all channels look like the noiseless-subset example, so approximately disjoint sets of output sequences can be assigned to codewords (pp. 7–8).
- Relative entropy $D(p\|q)$ is a distance-like quantity, non-negative and zero iff $p=q$. Mutual information is a special case of it, and it is the exponent in the error probability of a hypothesis test between $p$ and $q$ (pp. 8–9).
- Kolmogorov complexity $K$ (shortest program length) is approximately $H$ for random sequences. The authors regard $K$ as more fundamental than $H$ (p. 3).
- The doubling rate $W$ (the maximum asymptotic exponent of wealth growth in investment) is described as a dual of the market's entropy rate (a term this chapter does not define), and the authors call the parallels between investment theory and information theory striking (pp. 4, 9, 11).
- Network information theory (many senders and receivers) is unfinished, and a unifying theory "remains to be found" (p. 3).

## L3 — Walkthrough

### Opening claims (p. 1)
- The chapter is a "first and last lecture". Full definitions begin in Chapter 2 (p. 1).
- Information theory answers two questions in communication theory. The ultimate data compression is the entropy $H$. The ultimate transmission rate is the channel capacity $C$ (p. 1).
- Some people treat the theory as a subset of communication theory. The authors argue it is much more. They name contributions to statistical physics, computer science (Kolmogorov or algorithmic complexity), statistical inference (Occam's razor) and probability and statistics (error rates in optimal hypothesis testing and estimation) (p. 1).
- Figure 1.1 shows information theory overlapping physics, mathematics, electrical engineering, computer science, probability, statistics and economics (p. 2). In the figure, the overlaps are labelled: limits of communication theory; AEP/thermodynamics; Kolmogorov complexity; inequalities; portfolio theory/Kelly gambling; Fisher information/hypothesis testing; limit theorems/large deviations (p. 2).

### Electrical engineering (communication theory) (pp. 1–3)
- **Historical claim.** In the early 1940s it was thought that raising the transmission rate raised the probability of error. Shannon showed this is false as long as the rate is below capacity. Capacity can be computed simply from the channel's noise characteristics (p. 1).
- **Entropy named.** Shannon argued that music and speech have an irreducible complexity below which the signal cannot be compressed. He named it entropy, after its use in thermodynamics. He argued that if the source entropy is less than the channel capacity, asymptotically error-free communication can be achieved (pp. 1–2).
- **Extreme points.** Figure 1.2 shows the data-compression limit $\min I(X;\hat X)$ and the data-transmission limit $\max I(X;Y)$ as the two extremes of all communication schemes. All compression schemes need description rates at least equal to the minimum. All modulation and compression schemes lie between the limits (pp. 2–3).
- **Practicality.** Optimal schemes "may turn out to be computationally impractical". Simple modulation is used instead of Shannon's random coding with nearest-neighbour decoding. Better integrated circuits and code design have captured some of the gains, for example error-correcting codes on compact discs (p. 3).
- **Network information theory** studies simultaneous rates from many senders to many receivers. Some rate trade-offs are unexpected, all have a certain mathematical simplicity, and a unifying theory remains to be found (p. 3).

*Intuition note.* Compression and transmission have separate limits, and the theoretically optimal schemes may be computationally impractical. Shannon's result is surprising because, below capacity, higher rates do not force a higher probability of error.

### Computer science (Kolmogorov complexity) (p. 3)
- Kolmogorov, Chaitin and Solomonoff put forth the idea that the complexity of a data string is the length of the shortest binary program that computes it, i.e. the minimal description length (p. 3).
- This definition is universal (computer-independent) (p. 3).
- $K\approx H$ if the sequence is drawn at random from a distribution of entropy $H$. **Authors' view:** Kolmogorov complexity is more fundamental than Shannon entropy, because it is the ultimate data compression and leads to a logically consistent procedure for inference (p. 3).
- Algorithmic complexity (program length) and computational complexity (running time) are two axes. Each theory minimises along one axis, and little work has been done on minimising both (p. 3).

### Physics (thermodynamics) (pp. 3–4)
- Statistical mechanics is the birthplace of entropy and the second law. The authors state "Entropy always increases", and the second law lets one dismiss perpetual-motion claims. It is discussed in Chapter 2 (pp. 3–4).

### Mathematics (probability and statistics) (p. 4)
- Entropy, relative entropy and mutual information are functionals of probability distributions. They characterise the behaviour of long random sequences, allow estimation of rare-event probabilities (large deviation theory), and give the best error exponent in hypothesis tests (p. 4).

### Philosophy of science (Occam's razor) (p. 4)
- Occam: "Causes shall not be multiplied beyond necessity", paraphrased as "the simplest explanation is best" (p. 4).
- **Solomonoff, later Chaitin, argue:** a weighted combination of all programs that explain the data, plus observing what they print next, gives a universally good prediction procedure. **Authors add:** it works in problems statistics does not handle. It will eventually predict later digits of $\pi$ and will infer a coin with heads probability 0.7. It "should essentially find" all the laws of the stock market, and in principle would have found Newton's laws (p. 4).
- **Caveat:** the procedure is highly impractical, because weeding out all programs that fail to generate the data takes impossibly long. The authors say we would predict tomorrow "a hundred years from now" (p. 4).

### Economics (investment) (p. 4)
- Repeated investment in a stationary market gives exponential wealth growth. The growth rate (the doubling rate) is a dual of the market's entropy rate. The parallels are called striking, and the book develops the theory to explore this duality (p. 4).

### Computation vs. communication (p. 4)
- Larger computers built from smaller components face both a computation limit and a communication limit. Computation is communication-limited and communication is computation-limited. **Authors infer:** communication-theory results should affect the theory of computation (p. 4).

### 1.1 Preview of the book

**Entropy (p. 5).** For a random variable $X$ with probability mass function $p(x)$:
$$H(X) = -\sum p(x)\log_2 p(x) \tag{1.1}$$
With base-2 logs, entropy is in bits. It measures average uncertainty and is the average number of bits needed to describe $X$ (p. 5).

**Example 1.1.1 (uniform on 32 outcomes).** Labels need 5-bit strings. Then
$$H(X) = -\sum_{i=1}^{32} p(i)\log p(i) = -\sum_{i=1}^{32}\frac1{32}\log\frac1{32} = \log 32 = 5 \text{ bits} \tag{1.2}$$
This matches the bits needed, and all outcomes have equal-length representations (p. 5).

**Example 1.1.2 (horse race, 8 horses).** Win probabilities are $(\tfrac12,\tfrac14,\tfrac18,\tfrac1{16},\tfrac1{64},\tfrac1{64},\tfrac1{64},\tfrac1{64})$ (p. 5).
$$H(X) = -\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac1{16}\log\tfrac1{16}-4\tfrac1{64}\log\tfrac1{64} = 2 \text{ bits} \tag{1.3}$$
- Sending the horse's index costs 3 bits for every horse. Using shorter strings for likelier horses lowers the average. The code is $0, 10, 110, 1110, 111100, 111101, 111110, 111111$, with average length 2 bits, equal to the entropy (pp. 5–6).
- **Forward pointer:** Chapter 5 shows that entropy is a lower bound on the average number of bits, and on the average number of questions in "twenty questions". It also shows how to build representations within one bit of entropy (p. 6).

*Intuition note.* Likely outcomes deserve short names and unlikely ones long names. In this example the average name length of such a code equals the entropy, exactly 2 bits.

**AEP (p. 6).** For $n$ i.i.d. variables, the probability of a "typical" sequence is about $2^{-nH(X)}$ and there are about $2^{nH(X)}$ typical sequences. This asymptotic equipartition property is the basis of many proofs (p. 6). Entropy also answers other problems, for example the number of fair coin flips needed to generate a random variable (p. 6).

**Kolmogorov complexity (p. 6).** The Kolmogorov complexity of a binary string is the length of the shortest program that prints it. If the string is indeed random, it is close to the entropy. It gives a framework for inference and modelling and a clearer view of Occam's razor. Basic properties are in Chapter 7 (p. 6).

**Conditional entropy and mutual information (p. 6).** Conditional entropy is the entropy of one variable given another. The reduction in uncertainty is the mutual information:
$$I(X;Y) = H(X) - H(X|Y) = \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)} \tag{1.4}$$
$I(X;Y)$ measures the dependence between $X$ and $Y$. It is symmetric in $X$ and $Y$ and always non-negative (p. 6).

**Channel and capacity (pp. 6–7).** A channel is a system whose output depends probabilistically on its input. It is characterised by a probability transition matrix giving the conditional distribution of output given input.
$$C = \max_{p(x)} I(X;Y) \tag{1.5}$$
**Forward claim:** capacity is the maximum rate at which information can be sent and recovered with vanishingly low error probability (p. 7).

**Example 1.1.3 (noiseless binary channel).** The input is reproduced exactly, so 1 bit per transmission is sent reliably. $C=\max I(X;Y)=1$ bit (p. 7).

**Example 1.1.4 (noisy four-symbol channel).** Each input letter is received as itself with probability 1/2 or as the next letter with probability 1/2 (Fig. 1.4) (p. 7).
- Using all four inputs, the output does not reveal the input with certainty. Using only inputs 1 and 3, the output identifies the input at once. The channel then acts like the noiseless one, giving 1 bit per use without error. The capacity calculation agrees: $C=1$ bit (p. 7).
- In general, channels lack this simple structure, so one cannot always find an error-free subset of inputs. Over a sequence of transmissions, however, every channel looks like this example. One can pick a subset of input sequences (codewords) whose sets of possible output sequences are approximately disjoint. The output then identifies the input with vanishingly low error probability (pp. 7–8).

**Example 1.1.5 (binary symmetric channel).** The output equals the input with probability $1-p$, and the bit is flipped with probability $p$ (Fig. 1.5). Capacity is $C = 1 + p\log p + (1-p)\log(1-p)$ bits per transmission. How to achieve it is not obvious. Over many uses the channel looks like the four-symbol example, and rate $C$ is achievable with arbitrarily low error probability (p. 8).

**Channel coding theorem (p. 8).** Capacity is the ultimate rate limit, achievable with codes of long block length. Practical systems limit code complexity, so capacity may not be reached (p. 8).

*Intuition note.* One noisy use is ambiguous, but long blocks can be chosen so that their noisy outputs do not overlap. Capacity is the maximum rate at which this can be done with vanishingly low error probability.

**Relative entropy (pp. 8–9).** Mutual information is a special case of relative entropy, a "distance" between mass functions $p$ and $q$:
$$D(p\|q) = \sum_x p(x)\log\frac{p(x)}{q(x)} \tag{1.6}$$
- It is not a true metric but has some metric properties. It is always non-negative and zero iff $p=q$ (p. 8).
- It is the exponent in the error probability of a hypothesis test between $p$ and $q$. It also defines a geometry on distributions that helps interpret large deviation results (pp. 8–9).

**Investment (p. 9).** A stock market is a random vector $X$ with non-negative entries: end-of-day price over start-of-day price for each stock. For distribution $F(x)$, the doubling rate is
$$W = \max_{b:\ b_i\ge 0,\ \sum_i b_i = 1}\int \log b^{t}x\, dF(x) \tag{1.7}$$
(constraint reconstructed from garbled text; see Reading notes). $W$ is the maximum asymptotic exponent in wealth growth. Its properties parallel those of entropy, and Chapter 15 explores them (p. 9).

**Where $H, I, C, D, K, W$ arise (pp. 9–11).**
- *Data compression:* $H$ lower-bounds the average description length, achievable within one bit. Relaxing perfect recovery to distortion $D$ gives rate distortion theory. Shortest descriptions of non-random objects give $K$, which is universal (p. 9).
- *Data transmission:* choose codewords whose noisy versions are distinguishable, which is equivalent to sphere packing in high-dimensional space. Computing the exact error probability is usually tedious. Shannon used a randomly generated code to show rates below $C$ are achievable with arbitrarily low error. This idea is "very unusual", gives a simple analysis of a hard problem, and rests on typical sequences (pp. 9–10).
- *Network information theory:* Slepian–Wolf (compress many sources, joint reconstruction), the multiple access channel (Liao and Ahlswede), the broadcast channel, and the general capacity-region problem. **Authors' hope:** a unified theory may be beyond current techniques, but all answers may involve only elaborate forms of mutual information and relative entropy (p. 10).
- *Ergodic theory:* most $n$-sequences of an ergodic process have probability about $2^{-nH}$, and there are about $2^{nH}$ of them (p. 10).
- *Hypothesis testing:* $D$ is the error exponent and a natural distance (p. 10).
- *Statistical mechanics:* $H$ measures uncertainty or disorganisation. The second law says the entropy of a closed system cannot decrease (p. 10).
- *Inference:* use $K$ to find the shortest description of the data as a model for prediction. A model maximising entropy gives the maximum entropy approach (p. 10).
- *Gambling and investment:* for a horse race with uniform odds, $W + H$ is constant. The mutual information between the race and side information upper-bounds the increase in $W$ (pp. 10–11).
- *Probability theory:* most sequences have sample entropy close to $H$, so attention can be restricted to the roughly $2^{nH}$ typical ones. In large deviation theory, a set's probability is about $2^{-nD}$, with $D$ the relative entropy distance from the true distribution to the closest element of the set (p. 11).
- *Complexity theory:* $K$ measures descriptive complexity, related to but different from computational complexity (time or space) (p. 11).

**Closing (p. 11).** Entropy and relative entropy "arise again and again" as answers to basic questions in communication and statistics. The next chapter studies their definitions and basic properties (p. 11).

## Toy example (ours, not from the text)
*Source.* Four symbols A, B, C, D with probabilities $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$.
- Entropy: $H = \tfrac12(1)+\tfrac14(2)+\tfrac18(3)+\tfrac18(3) = 0.5+0.5+0.375+0.375 = 1.75$ bits.
- Fixed-length labels need 2 bits. A variable-length code A=0, B=10, C=110, D=111 has lengths 1, 2, 3, 3 and average $0.5+0.5+0.375+0.375 = 1.75$ bits. This equals $H$, as in the horse race.

*Channel.* A binary symmetric channel with $p=\tfrac14$ has
$C = 1 + \tfrac14\log_2\tfrac14 + \tfrac34\log_2\tfrac34 = 1 - 0.5 + 0.75(-0.41504) = 1 - 0.5 - 0.31128 \approx 0.189$ bits per use. By the book's claim (1.1.5), rates up to about 0.189 bits per use can be sent with arbitrarily low error using long codes. At $p=0$ the formula gives $C=1$, the noiseless case.

## Concepts
- [[bit]] — unit of entropy when logs are base 2 (p. 5)
- [[entropy H(X)]] — $-\sum p(x)\log_2 p(x)$; average bits needed to describe $X$ (p. 5)
- [[joint and conditional entropy]] — here only conditional entropy $H(X|Y)$ is named, as uncertainty of $X$ given $Y$ (p. 6)
- [[mutual information I(X;Y)]] — reduction in uncertainty, $H(X)-H(X|Y)$; symmetric, non-negative (p. 6)
- [[noisy channel]] — output depends probabilistically on input, given by a transition matrix (p. 6)
- [[channel capacity]] — $\max_{p(x)} I(X;Y)$ (p. 7)
- [[noisy-channel coding theorem]] — stated informally: capacity is achievable with long block length codes (pp. 7–8)
- [[typical set / AEP]] — about $2^{nH}$ sequences, each of probability about $2^{-nH}$ (p. 6)
- [[source coding theorem]] — only previewed: $H$ lower-bounds average length, achievable within one bit (pp. 6, 9)
- [[relative entropy / KL divergence]] — $D(p\|q)$, non-negative, zero iff $p=q$, not a metric (p. 8)
- [[rate–distortion function]] — rates needed to describe the source up to distortion $D$ (p. 9)
- [[Kolmogorov complexity K(x)]] — length of shortest program printing the string (p. 3)
- [[algorithmic probability (Solomonoff)]] — weighted combination of all programs explaining the data, used for prediction (p. 4)
- [[Kelly criterion / doubling rate]] — $W$ in (1.7), the maximal asymptotic growth exponent of wealth (p. 9)
- [[maximum entropy principle]] — mentioned: a model maximising entropy gives the maximum entropy approach to inference (p. 10)
- [[network information theory]] (new) — rates among many senders and receivers: Slepian–Wolf, multiple access, broadcast (p. 10)

## Canonical instances
- [[uniform-32-outcomes]] — $H=\log 32=5$ bits, equal-length labels (p. 5)
- [[horse-race-8]] — $H=2$ bits, and a code reaching it (pp. 5–6)
- [[noiseless-binary-channel]] — $C=1$ bit (p. 7)
- [[noisy-four-symbol-channel]] — two inputs give an error-free subchannel, $C=1$ (p. 7)
- [[binary-symmetric-channel]] — $C=1+p\log p+(1-p)\log(1-p)$ (p. 8)
- [[compact-disc-error-correction]] — real application of error-correcting codes (p. 3)

## Bridges (candidates)
- [same-math] relative entropy $D(p\|q)$ ↔ statistics: error exponent in hypothesis testing between $p$ and $q$ (pp. 8–9)
- [same-math] typical sequences, $2^{nH}$ ↔ probability: the AEP for i.i.d. sources (p. 6)
- [structural-analogy] doubling rate $W$ ↔ entropy rate: the authors call $W$ a "dual" of the entropy rate (p. 4)
- [structural-analogy] shortest program length $K$ ↔ Occam's razor / MDL: the simplest explanation as the shortest description (pp. 3–4)
- [structural-analogy] channel codewords ↔ sphere packing in high dimension (p. 9)
- [metaphor] channel capacity as a limit on message flow ↔ a limit on how much information an agent can absorb (our suggestion, not in the source)

## Questions this raises
- Why is $K\approx H$ only for sequences drawn at random from a distribution, and what does "approximately" mean precisely?
- Why does "entropy always increases" (p. 4) differ from "entropy of a closed system cannot decrease" (p. 10)? Are they the same statement?
- How can a randomly generated code, which looks unusable, prove that capacity is achievable?
- In what exact sense is the doubling rate "dual" to the entropy rate?

## Reading notes
- **Edition:** the title page reads "Copyright © 1991 John Wiley & Sons", print ISBN 0-471-06259-6, which the unit metadata identifies as the 1991 first edition (the pages themselves do not say "first edition"). The metadata lists the work as the 2nd edition (2006), so chapter numbers and contents may differ from the 2006 edition. Chapter references (Ch. 2, 5, 7, 15) are the 1991 numbering as printed here.
- **Offset:** printed = pdf − 22.
- **OCR:** the text layer garbles the page 9 equation, and no image was supplied for p. 9. I reconstructed equation (1.7) as $W=\max_{b:\,b_i\ge0,\ \sum b_i=1}\int\log b^tx\,dF(x)$ from the garbled string "b:bi~~i=l". The constraint under the max is not confirmed against an image.
- The OCR labels the binary symmetric channel "Example 1.1.6", but the p. 8 image shows "Example 1.1.5". I used 1.1.5.
- On p. 4 the OCR renders π as "r"; I read it as π, from the context of predicting digits (no image supplied for that page).
- The OCR text for p. 6 and p. 11 (e.g. "ZnH") has garbled exponents. I read them as $2^{nH}$.
- This unit is a preview. Results are stated without proof, and the book defers proofs to later chapters.
