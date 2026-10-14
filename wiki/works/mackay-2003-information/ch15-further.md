---
id: mackay-2003-information/ch15-further
work: mackay-2003-information
unit: "15 Further Exercises on Information Theory"
pages: 233–240
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
# Further Exercises on Information Theory

## L0 — One line
This chapter is a set of problems that moves from refresher exercises on coding and channels to multi-user settings (correlated sources, multiple access, broadcast, two-way channels), where clever coding can beat simple baselines such as time-sharing (taking turns).

## L1 — The gist (≤ 120 words)
The chapter asks the reader to practise source coding, noisy channels, capacity and error detection, and then to discover several surprising results. Two strongly dependent (correlated) sources can be encoded separately at a total rate below the sum of their own entropies. Two users of a binary adder channel (output = sum of the inputs) can, according to the author's figure, exceed a total of one bit. A broadcast channel (one sender, two receivers), or a code for an unknown noise level, can beat plain time-sharing (taking turns), though the author finds the gain small in his example. Almost no solutions are printed; only the capacity of the 8-bit one-flip channel (5 bits) is given.

**Prerequisites:** entropy and conditional entropy; binary entropy $H_2$; channel capacity as maximum mutual information; modular arithmetic; typical sets.

## L2 — Key ideas (5–10 bullets)
- The refresher exercises (15.1–15.16) cover block codes, typical sets (the likely sequences), decoding rules, capacities and error detection with check digits (pp. 233–236).
- Slepian–Wolf (Ex. 15.17): two dependent sources can be encoded separately and still be reconstructed, if each rate exceeds a conditional entropy and the sum exceeds the joint entropy (p. 237).
- In the weather example the total rate need only exceed 1.14 bits per cycle, not 2 (p. 237).
- In a noiseless binary adder multiple-access channel (two senders, one receiver, output = sum of the inputs), the author's figure 15.3c indicates an achievable region reaching a total rate above 1 bit (pp. 237–238).
- Broadcast channels can beat time-sharing (the American/Belarusian analogy); for degraded channels (receiver B gets a further-degraded copy of what A receives) the task reduces to the pair $(R_0,R_A)$ (p. 238).
- A code for unknown noise level $f_A$ or $f_B$ is mathematically the same problem as the degraded broadcast channel (p. 239).
- The two-way binary channel has achievable rates beyond the time-sharing point $(1/2,1/2)$; its general capacity is open (pp. 239–240).

## L3 — Walkthrough

### Refresher exercises on source coding and noisy channels (pp. 233–236)
Exercises are stated here only; apart from Ex. 15.12, no solutions are printed on these pages.

- **15.1 [2]** (p. 233) $\mathcal A_X=\{0,1\}$, $\mathcal P_X=\{0.995,0.005\}$. Block code on $X^{100}$: every $x$ with 3 or fewer 1s gets a distinct codeword; the others are ignored. Asks: (a) the minimum fixed codeword length; (b) the probability of an ignored $x$.
- **15.2 [2]** (p. 233) $\mathcal P_X=\{0.1,0.2,0.3,0.4\}$, symbol code $C=\{0001,001,01,1\}$, $x\in X^N$ with $N$ large. Asks for the entropy of the 4th bit, its conditional entropy given the 3rd bit, and estimates of the same two quantities for the 100th bit given the 99th.
- **15.3 [2]** (p. 233) Alice rolls two fair dice and records the sum. Bob asks yes/no questions. Devise the strategy with the minimum average number of questions.
- **15.4 [2]** (p. 233) How can a coin be used to draw straws among 3 people?
- **15.5 [2]** (p. 233) Magic trick. The volunteer writes different integers from 1 to 100 on five white cards and one blue card and keeps the blue one. The magician orders the five white cards and passes them to a soundproof assistant, who announces the blue number. How does it work?
- **15.6 [3]** (p. 234) Card trick: five chosen cards go to Esmerelda, who shows four; the magician names the hidden fifth. It works with 52 cards. Use information theory to bound the number of cards for which it can work.
- **15.7 [2]** (p. 234) Find a probability sequence $\mathbf p=(p_1,p_2,\dots)$ with $H(\mathbf p)=\infty$.
- **15.8 [2]** (p. 234) Source $\{a,b,c,d\}$, $\mathcal P_X=\{1/2,1/4,1/8,1/8\}$, $4^8=65\,536$ eight-letter words. Count the words in the typical set $T_{N\beta}$ (equation 4.29) with $N=8$, $\beta=0.1$.
- **15.9 [2]** (p. 234) Source $\mathcal A_S=\{a,b,c,d,e\}$, $\mathcal P_S=\{1/3,1/3,1/9,1/9,1/9\}$. Channel (columns are inputs: each column sums to 1; matrix as read from the page image):
$$Q=\begin{bmatrix}1&0&0&0\\0&0&2/3&0\\0&1&0&1\\0&0&1/3&0\end{bmatrix}\tag{15.1}$$
 The source emits symbols at exactly 3/4 the rate at which the channel accepts them. Design an explicit system with average error probability per source symbol below a tiny $\epsilon>0$, without invoking the noisy-channel coding theorem.
- **15.10 [2]** (p. 234) Binary symmetric channel, noise level $f$, code $\{0000,0011,1100,1111\}$ used with probabilities $\{1/2,1/8,1/8,1/4\}$. Give the error-minimizing decoding rule for each range of $f$ between 0 and 1/2; the rule depends on $f$.
- **15.11 [2]** (p. 234) Capacity and optimal input distribution for
$$Q=\begin{bmatrix}1&0&0\\0&2/3&1/3\\0&1/3&2/3\end{bmatrix}\tag{15.2}$$
- **15.12 [3]** (p. 235) Input and output are 8-bit words. Each use flips exactly one bit, chosen uniformly from the 8; the receiver does not know which. Derive the capacity. Then give an explicit encoder and decoder that communicate 5 bits per cycle with zero error probability. **Printed solution (p. 239):** $C(Q)=5$ bits; hint: a simple $(8,5)$ code works.
- **15.13 [2]** (p. 235) Inputs $\{a,b,c\}$, outputs $\{r,s,t,u\}$:
$$Q=\begin{bmatrix}1/2&0&0\\1/2&1/2&0\\0&1/2&1/2\\0&0&1/2\end{bmatrix}$$
 Find its capacity.
- **15.14 [3]** (p. 235) ISBN. Nine source digits $x_n\in\{0,\dots,9\}$ and check digit
$$x_{10}=\Big(\sum_{n=1}^{9} n x_n\Big)\bmod 11,$$
 with $x_{10}=10$ written X. Show: a valid ISBN satisfies $\big(\sum_{n=1}^{10} n x_n\big)\bmod 11=0$; the code can be used to detect (but not correct) all errors in which one digit is modified, and to detect all errors in which two adjacent digits are transposed. Which other non-adjacent transpositions are detectable? If instead $x_{10}=(\sum_{n=1}^9 n x_n)\bmod 10$, why does the code work less well (for both single-digit changes and transpositions)?
- **15.15 [3]** (p. 236) Channel (columns are inputs):
$$Q=\begin{bmatrix}1-f&f&0&0\\f&1-f&0&0\\0&0&1-g&g\\0&0&g&1-g\end{bmatrix}$$
 with input $\mathcal P_X=\{p/2,\,p/2,\,(1-p)/2,\,(1-p)/2\}$. Write $H(Y)$ and $H(Y|X)$. Show that the optimal input has
$$p=\frac{1}{1+2^{-H_2(g)+H_2(f)}},\qquad H_2(f)=f\log_2\tfrac1f+(1-f)\log_2\tfrac1{1-f}.$$
 Hint given: $\frac{d}{dp}H_2(p)=\log_2\frac{1-p}{p}$. Then give the optimal input and capacity for $f=1/2$, $g=0$, and comment.
- **15.16 [2]** (p. 236) How do the redundancies needed for error detection and for error correction differ?

### Further tales from information theory (pp. 236–240)
The author says these exercises let the reader discover surprising results (p. 236).

**15.17 [3] Correlated sources (pp. 236–237).** Sources $X^{(A)},X^{(B)}$ send to a collector C over noise-free one-way channels, using codes of rates $R_A,R_B$. Example joint distribution (rain in Allerton and Bognor):
$$P(x^{(A)},x^{(B)}):\quad \begin{matrix}&x^{(A)}=0&x^{(A)}=1\\ x^{(B)}=0&0.49&0.01\\ x^{(B)}=1&0.01&0.49\end{matrix}\tag{15.3}$$
The question: can C reconstruct all variables with a total rate below two bits per cycle? The author states the general result (Slepian and Wolf, 1973). Reliable communication of both sources is possible as long as
$$R_A>H(X^{(A)}|X^{(B)}),\qquad R_B>H(X^{(B)}|X^{(A)}),\qquad R_A+R_B>H(X^{(A)},X^{(B)}).$$
(p. 237). Figure 15.2b shows this as an achievable region; both strings can be conveyed although $R_A<H(X^{(A)})$ and $R_B<H(X^{(B)})$ (p. 237). For (15.3), each rate must exceed $H_2(0.02)=0.14$ bits and the sum must exceed 1.14 bits, e.g. $R_A=R_B=0.6$ (p. 237). The reader is to show why such codes exist, and to try an explicit solution where one source is sent as plain text, $\mathbf t^{(B)}=\mathbf x^{(B)}$, and the other is encoded (p. 237).

*Intuition note (ours, not the author's):* The author leaves the reason for the reader to work out (p. 237). The stated conditions fit this picture: if B is sent as plain text at about $H(X^{(B)})=1$ bit, then A need only exceed $H(X^{(A)}|X^{(B)})\approx0.14$ bits (added step: $1+0.14=1.14$, which matches the joint-entropy bound).

**15.18 [3] Multiple access channels (pp. 237–238).** Two binary inputs $x^{(A)},x^{(B)}$ and a noiseless output $y=x^{(A)}+x^{(B)}\in\{0,1,2\}$ (figure 15.3b). The senders cannot talk to each other or hear the output. Output 0 or 2 identifies both inputs; output 1 is ambiguous between $(0,1)$ and $(1,0)$ (p. 237). The total rate cannot be two bits; a total of one bit is easy. The question is whether $R_A+R_B>1$ is achievable. The author says the answer is indicated in figure 15.3 (p. 237). Reading the image, the shaded region in 15.3c has corner points at $(1,1/2)$ and $(1/2,1)$ and reaches beyond the line $R_A+R_B=1$ (figure 15.3c, p. 238). Practical multi-user codes: Ratzer and MacKay (2003) (p. 237).

**15.19 [3] Broadcast channels (pp. 237–238).** One transmitter, receivers A and B, memoryless channel $Q(y^{(A)},y^{(B)}|x)$. The task is to send a common message at rate $R_0$, plus individual messages at $R_A$ and $R_B$. The capacity region is the convex hull (smallest convex set containing them) of the achievable triplets $(R_0,R_A,R_B)$ (p. 237). Time-sharing benchmark: a fraction $\phi_A$ of time on A, $\phi_B=1-\phi_A$ on B, giving $(0,\phi_A C^{(A)},\phi_B C^{(B)})$ (p. 238). Better: the analogy of speaking American and Belarusian. If each listener can tell whether a word is in their own language, an extra binary file can reach both by choosing which language each next word comes from (p. 238).

Example: two binary symmetric channels with a common input, flip probabilities $f_A<f_B<1/2$ (A has the better half-channel). A closely related channel is the *degraded* broadcast channel, whose variables form a Markov chain
$$x\to y^{(A)}\to y^{(B)}\tag{15.4}$$
Then whatever reaches B can also be recovered by A, so one need not separate $R_0$ from $R_B$. The task becomes finding the capacity region for $(R_0,R_A)$ (p. 238).

**15.20 [3] Variable-rate codes for unknown noise (pp. 238–239).** The channel is a binary symmetric channel with noise level $f_A$ or $f_B$, with $f_B>f_A$ and capacities $C_A,C_B$. A code designed for $f_A$ at rate $R_A\simeq C_A$ would be expected to fail catastrophically if the noise is $f_B$ (figure 15.6, solid). A code designed for $f_B$ at rate $R_B\simeq C_B$ wastes $C_A-R_B$ if the noise is $f_A$ (dashed). The question is whether one code can send high-priority bits reliably at all noise levels between $f_A$ and $f_B$, plus low-priority bits when the noise is $f_A$ or lower (figure 15.7) (p. 239). This is mathematically equivalent to the degraded broadcast channel: the lower rate is $R_0$, the low-priority rate is $R_A$ (p. 239). Figure 15.8 gives an illustrative answer for $f_A=0.01$, $f_B=0.1$ (p. 239). The author finds the gap between simple time-sharing and the "cunning" solution "disappointingly small" (p. 239). Chapter 50 will discuss rateless codes for erasure channels, where the number of symbols sent adapts on the fly (p. 239).

**15.21 [3] Two-way binary channel (p. 239–240).** A and B both transmit and want to hear each other, but a user hears the other only while transmitting a zero. From the tables in figure 15.9b: $y^{(A)}=x^{(B)}$ if $x^{(A)}=0$, else $0$; $y^{(B)}=x^{(A)}$ if $x^{(B)}=0$, else $0$ (p. 240). Time-sharing gives rate 1/2 each way. Codes exist reaching the solid boundary of figure 15.9c, and better codes may exist. The capacity of a general two-way channel is an open problem (p. 239).

## Toy example (ours, not from the text)
Apply the Slepian–Wolf conditions of Ex. 15.17 (p. 237) to a different joint distribution: $P(0,0)=P(1,1)=0.4$, $P(0,1)=P(1,0)=0.1$.

1. Marginals: $P(x^{(A)}=0)=0.4+0.1=0.5$, so $H(X^{(A)})=1$ bit; likewise $H(X^{(B)})=1$.
2. Given $x^{(A)}=0$, $P(x^{(B)}=1)=0.1/0.5=0.2$. So $H(X^{(B)}|X^{(A)})=H_2(0.2)=0.2\log_2 5+0.8\log_2 1.25=0.2(2.3219)+0.8(0.3219)=0.4644+0.2575=0.722$. By symmetry $H(X^{(A)}|X^{(B)})=0.722$.
3. Joint entropy $=H(X^{(A)})+H(X^{(B)}|X^{(A)})=1+0.722=1.722$ bits.
4. Conditions: $R_A>0.722$, $R_B>0.722$, $R_A+R_B>1.722$. Check $R_A=R_B=0.9$: $0.9>0.722$ and $1.8>1.722$, so it is allowed, with total $1.8<2$.

## Concepts
- [[entropy]] — average surprisal; used for bit-position entropies and the joint/conditional entropies of Ex. 15.2, 15.7, 15.17 (pp. 233, 234, 237)
- [[joint-conditional-entropy]] — $H(X^{(A)},X^{(B)})$ and $H(X^{(B)}|X^{(A)})$ set the achievable rate region for dependent sources (p. 237)
- [[typical-set-aep]] — set $T_{N\beta}$ of likely sequences, to be counted in Ex. 15.8 (p. 234)
- [[noisy-channel]] — a transition matrix $Q$; columns are inputs in these exercises (pp. 234–236)
- [[channel-capacity]] — to be derived for several channels (e.g. 15.11–15.15); $C=5$ bits for 15.12 (pp. 234–236, 239)
- [[noisy-channel-coding-theorem]] — Ex. 15.9 forbids invoking it; Ex. 15.20 refers to expectations from "Shannon's theories" (pp. 234, 238)
- [[error-correcting-code]] — includes the $(8,5)$ code hint and the detect/correct contrast of Ex. 15.16 (pp. 236, 239)
- [[redundancy]] — extra digits needed for detection vs correction (p. 236)
- [[slepian-wolf-coding]] (new) — separate encoding of dependent sources with $R_A>H(A|B)$, $R_B>H(B|A)$, $R_A+R_B>H(A,B)$ (p. 237)
- [[multiple-access-channel]] (new) — several transmitters, one receiver; here a noiseless adder (p. 237)
- [[broadcast-channel]] (new) — one transmitter, several receivers; capacity region is a convex hull of $(R_0,R_A,R_B)$ (p. 237)
- [[degraded-broadcast-channel]] (new) — Markov chain $x\to y^{(A)}\to y^{(B)}$ (p. 238)
- [[time-sharing]] (new) — baseline: devote fractions of time to each channel (p. 238)
- [[check-digit-code]] (new) — ISBN last digit defined by a weighted sum mod 11 (p. 235)
- [[rateless-code]] (new) — number of transmitted symbols is set on the fly (p. 239)
- [[two-way-channel]] (new) — both users transmit and receive; general capacity open (p. 239)

## Canonical instances
- [[isbn-check-digit]] — error-detecting code with weights $n$ and modulus 11 (p. 235)
- [[allerton-bognor-weather]] — correlated binary rain reports, joint table (15.3) (p. 236)
- [[binary-adder-mac]] — $y=x^{(A)}+x^{(B)}$ multiple-access channel (p. 237)
- [[american-belarusian-broadcast]] — extra bits sent by choosing which language the next word comes from (p. 238)
- [[two-bsc-broadcast]] — two binary symmetric channels with a shared input, $f_A=0.01$, $f_B=0.1$ (pp. 238–239)
- [[binary-two-way-channel]] — a user hears only while sending zero (p. 239)

## Bridges (candidates)
- [structural-analogy] Minimum-error decoding with unequal codeword probabilities (Ex. 15.10) ↔ Bayesian inference: prior over codewords combined with the channel likelihood — the best decoder depends on both.
- [structural-analogy] Slepian–Wolf rate conditions ↔ information theory: chain rule $H(A,B)=H(A)+H(B|A)$ — the corner point with B sent as plain text has sum rate $H(B)+H(A|B)=H(A,B)$ (the chain rule is not on these pages).
- [structural-analogy] Variable-rate code for unknown noise ↔ Bayesian decision under model uncertainty — hedging between two possible noise models.

## Questions this raises
- Why can separate encoders achieve the joint entropy $H(X^{(A)},X^{(B)})$ without communicating?
- Is there an explicit code, not just an existence proof, for the corner point with $\mathbf t^{(B)}=\mathbf x^{(B)}$?
- How large can the gain over time-sharing be for broadcast channels, given that the author calls it small in his example?
- What do achievable rates look like beyond the boundary shown for the two-way binary channel?

## Exercises worth doing
- Ex. 15.6 (p. 234) — an information-theoretic upper bound on the number of cards for the trick — difficulty: hard
- Ex. 15.12 (p. 235) — capacity of a one-flip channel plus an explicit zero-error code — difficulty: hard
- Ex. 15.14 (p. 235) — check digits: detection of single errors and transpositions, mod 11 vs mod 10 — difficulty: medium
- Ex. 15.15 (p. 236) — optimal input for a channel made of two noisy blocks — difficulty: hard
- Ex. 15.17 (p. 236) — Slepian–Wolf with one source sent as plain text — difficulty: hard
- Ex. 15.18 (p. 237) — can the adder channel exceed total rate 1? — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 245–252 are printed 233–240).
- The text layer garbles several formulas. I checked the images for: the matrices in (15.1), (15.2), Ex. 15.13 and 15.15; the optimal-$p$ formula in 15.15 (image shows $2^{-H_2(g)+H_2(f)}$); and the tables of figure 15.9b.
- Figure 15.8 has no axis labels, only tick values; figure 15.9c has axes labelled R(A) and R(B) with tick values. My description of figure 15.3c (corner points) is read from the image, not stated in the text.
- Only one solution is printed in this unit (Ex. 15.12, p. 239). The chapter mentions equation 4.29 and Chapter 50, which are outside these pages.
