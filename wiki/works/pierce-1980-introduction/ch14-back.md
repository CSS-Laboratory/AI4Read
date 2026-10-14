---
id: pierce-1980-introduction/ch14-back
work: pierce-1980-introduction
unit: "14 Back to Communication Theory"
pages: 268-277
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Back to Communication Theory

## L0 — One line
Pierce says that, to him, the indubitably valuable core of information theory lies in electrical communication, and he then surveys further mathematically grounded or active work (Kelly's gambling result, secrecy theory, sampling problems, a fidelity criterion, two-way channels, better codes and modulation), ending in a sober vein.

## L1 — The gist (≤ 120 words)
After discussing language, psychology and art, Pierce asks what information theorists have done that is mathematically sound. In his view the clearly valuable core is source entropy, channel capacity and efficient coding, applied to electrical communication. Beyond that core he names one rigorous non-coding use of information rate: Kelly's gambling result with inside information at fair odds, where capital grows by a factor $2^{NR}$. He also sketches Shannon's theory of secrecy systems, limits of the sampling theorem, a fidelity criterion, two-way channels, and engineering work on codes and modulation. His message is to appreciate the field for what it is, in a sober vein.

**Prerequisites:** bits and powers of 2; entropy and channel capacity (earlier chapters); the idea of a band-limited signal.

## L2 — Key ideas (5–10 bullets)
- Pierce says it would be wrong to believe that information theory is valuable chiefly because of its wide-ranging links to other fields; he points to the confusion that surrounded Newton's work (pp. 268–269).
- To him the "indubitably valuable" core is: entropy of an ergodic source (a statistically steady message source), capacity of noiseless and noisy channels, and encoding that approaches capacity. Its clear domain is electrical communication systems (p. 269).
- Kelly (1956) gives the only rigorous, meaningful use of information rate outside efficient encoding that Pierce says has been given so far: with inside information and fair odds (odds that match the true chances), capital grows by $2^{NR}$ over $N$ bets (pp. 270–271).
- Shannon's 1949 secrecy theory expresses the shrinking uncertainty of a cryptanalyst (a code breaker) about the message as a fall in equivocation (remaining uncertainty). Pierce thinks it doubtful that it has helped much in deciphering messages, but says it gave the first well-organized theory of cryptography and cryptanalysis (pp. 271–272).
- A band-limited signal (one of bandwidth $W$) is represented uniquely by $2W$ samples per second only when samples from all time are used. A finite set of samples does not fix one signal (pp. 272–274).
- Shannon's fidelity criterion handles the case where no uncertainty arises but damage is done, such as a consistent letter swap (p. 274).
- Two-way channels and better codes and modulation are open or active topics. Pierce ends by urging appreciation of the field as informed workers see it (pp. 275–277).

## L3 — Walkthrough

### Opening: the value of a new idea (pp. 268–269)
- To be worthy of notice, a new idea must have some solid and clearly demonstrated value, however narrow (p. 268).
- **Critic:** an information theorist criticized Pierce for exploring language, psychology and art, since the relation seems marginal or dubious (p. 268).
- **Pierce replies:** he partly owed readers a discussion of such links. He also believes information theory is useful in helping us talk sense, or at least keep from talking nonsense, about some linguistic, artistic and psychological problems. But there is a danger in overemphasizing them (p. 268).
- It would be wrong to think the theory is valuable chiefly because of wide connections. That repeats mistakes made with other discoveries (p. 269).
- Parallel: Newton's work was beclouded by controversy and philosophy and linked with a "putative universality". Newtonian mechanics later helped solve problems Newton never imagined, but it did not solve all of science's problems, as some optimistic philosophers expected (p. 269). Pierce quotes Einstein on Newton: celestial mechanics was born and confirmed many times over (p. 269).
- **Pierce's core** (his own view: "to me"): the entropy of an ergodic message source, the capacity of noiseless and noisy channels, and efficient encoding that approaches errorless transmission at a rate approaching capacity. Its clear world is electrical communication systems, especially their intelligent design (p. 269).
- The chapter asks what else is mathematically sound, "sound science" rather than speculation to argue about. It is a brief summary of work since Shannon's original paper (pp. 269–270).

### Kelly's gambling result (pp. 270–271)
- Ambitious people want to bring meaning in. Pierce says the only application of information rate beyond efficient encoding that is rigorous and meaningful, and that had been given so far, was Kelly's (J. L. Kelly, Jr., 1956) (p. 270).
- Setting: a bettor has inside information about the outcome of a chance event. The other party does not know this and gives fair odds on the basis of the chance of the outcome. Information arrives in bits (yes/no answers). One bit tells heads or tails of a coin. One bit (odd or even) narrows a die from 6 outcomes to 3 (p. 270).
- **Kelly's abstract (as quoted):** if channel input symbols are outcomes of a chance event with bets at fair odds, the gambler can make capital grow exponentially. The maximum exponential growth rate equals the rate of transmission of information over the channel. The result is generalized to arbitrary odds (pp. 270–271).
- **Kelly's abstract (continued):** the transmission rate is significant even though no coding is contemplated. Previously it was given significance only by Shannon's theorem that, with suitable encoding, binary digits could be sent at that rate with arbitrarily small probability of error (p. 271).
- After $N$ bets the capital is multiplied by $2^{NR}$, where $R$ is the average bits received per bet (p. 271).
- Pierce calls it the only mathematically established interpretation of information rate besides probable-message generation and efficient encoding (p. 271).

*Intuition note:* with fair odds, capital grows by a factor $2^{NR}$, where $R$ is the average number of bits received per bet. So each bit per bet on average corresponds to one doubling of capital. Here an information rate, normally tied to coding, measures money growth (Kelly: the maximum growth rate equals the rate of information transmission).

### Shannon's secrecy theory (pp. 271–272)
- Shannon's 1949 paper is a new use of the theory. Pierce doubts it helped much in deciphering messages. It gave, for the first time, a well-organized theory of cryptography and cryptanalysis, highly regarded by expert cryptanalysts (p. 271).
- A cryptanalyst is ignorant of two things: the message and the key, the specification of the enciphering means (p. 271).
- Example: in a simple substitution cipher, each letter is replaced by another by a fixed rule. A 3-letter message QXD could be AND, BET or any English word of three different letters. As the message lengthens, fewer English texts fit. If it is long enough, only one source message is possible (pp. 271–272).
- Shannon expressed this as a change in the equivocation $H_y(x)$ of Chapter VIII, the uncertainty about which message was enciphered. He computed, for various ciphers, how it falls as message length grows. When it approaches zero, in principle the message can be deciphered uniquely (p. 272).

*Intuition note:* as the cipher text gets longer, fewer English texts could have produced it. Equivocation measures the uncertainty that remains about which message was sent.

### Sampling theorem problems (pp. 272–274)
- A smooth band-limited signal of bandwidth $W$ is represented by its amplitudes every $1/2W$ seconds (p. 272).
- Sample times are not unique: shifted sets both work (Fig. XIV-1). They need not be equally spaced if there are on average $2W$ per second (p. 272).
- Unique representation by $2W$ samples per second needs all samples from the infinite past to the infinite future (p. 273).
- A finite run of samples does not fix one band-limited signal. Many signals pass through them and, if large outside the range, can differ greatly inside it (p. 273).
- Next idea: set all samples before and after a stretch to zero. Samples at all times then fix a unique signal. One might expect it to be small where the samples are zero (p. 273).
- **Pollak's result:** this need not be so. Almost half of the signal's energy can lie later than any specified time after the samples become zero. The signal can be zero at all the samples after $t_0$ and still be large in between them (pp. 273–274).
- Using the sampling theorem rigorously for finite-length signals is "in mathematical trouble". Work by Pollak and Slepian indicates that neither samples nor sine waves are the most appropriate way to represent band-limited functions of finite duration; they used prolate spheroidal functions instead (p. 274).

*Intuition note:* zero samples do not mean zero signal. The signal can swing between sample points. Samples fully describe a band-limited signal only when taken over all time.

### Fidelity criterion (p. 274)
- Puzzle: if a joker swaps the polarity of telegraph pulses, no uncertainty arises, so the information rate is unchanged. Yet damage seems done, worse if letters were consistently scrambled (A→W, B→K) (p. 274).
- Shannon's answer is a fidelity criterion that assigns penalties, e.g. more for a consonant replacing a vowel than for one vowel replacing another. With it he assesses damage from consistent or random errors (p. 274).
- For random errors of a noisy channel, he shows in principle how to minimize damage, and how many bits per second are needed for a given fidelity (p. 274).

### Two-way channels (pp. 275–276)
- Setting: messages in both directions between points A and B, assuming the circuit acts the same B→A as A→B. Plot capacity A→B against capacity B→A (Fig. XIV-3) (p. 275).
- No interference: the two capacities are independent, giving the solid horizontal and vertical lines (p. 275).
- Only one direction at a time: if A→B is used one-third of the time, B→A can be used two-thirds. The capacities sum to a constant, giving the dashed 45° line (p. 276).
- Some interference: roughly the dotted curve (p. 276).

### Efficient encoding, continuing (pp. 276–277)
- Discrete channels: theorists keep finding the most efficient code to correct $A$ errors in $B$ digits. They have not yet found a systematic way to find best codes (p. 276).
- In 1959 Shannon published upper and lower bounds on error rates for codes of various complexity (length) on a continuous channel with Gaussian noise (p. 276).
- Engineers seek simple, useful schemes, such as coding TV and voice into as few binary digits per second as possible (Chapter VII). Pierce expects this to matter more as digital transmission (e.g. pulse code modulation) spreads, and as encryption spreads, since secrecy is best attained digitally (p. 276).
- They also seek simple error-correcting codes for multiple errors on existing telephone circuits. Pierce says the many future possibilities of data transmission may be realized far, far more quickly if data can be sent over existing telephone circuits with a satisfactorily low error rate (pp. 276–277).
- They seek modulation better than AM and FM for long distances at low power. For satellite relay, Pierce says we will "almost surely" use broad-band modulation needing only a hundredth of the AM transmitter power. A 2-watt microwave satellite transmitter would suffice to relay a TV signal to London or Paris (p. 277).

### Closing (p. 277)
- Pierce grants these topics may seem picayune beside philosophical vistas. He asks, as a question, whether an informed appreciation of French impressionists or Dutch genre painters can ever be as meaningful as a sudden confrontation with a strange new world of art such as the Japanese (p. 277).
- The devoted connoisseur may have as much insight as the dilettante. One should appreciate a field for what it is, not for reactions it excites in the uninformed. He ends "in a sober vein" (p. 277).

## Toy example (ours, not from the text)
Take Pierce's coin case. The bettor starts with $1. Each toss, one bit (heads or tails) arrives before the bet, so $R = 1$ bit per bet. Fair odds on a fair coin: probability ½ means a winning bet pays 2 for 1.
- Bet all on the known side: capital goes 1 → 2 → 4 → 8 after $N = 3$ bets.
- Formula: $2^{NR} = 2^{3\times 1} = 8$. ✓
- Die variant (our assumption: fair odds pay 6 for 1 on each face). One bit (odd/even) leaves 3 faces. Split $1 into three bets of $\tfrac13$. The winning face pays $6\times\tfrac13 = 2$, so capital doubles. $R = 1$, factor $2^{1}=2$. ✓

## Concepts
- [[kelly-criterion-doubling-rate]] — with inside information at fair odds, capital grows by $2^{NR}$; maximum growth rate equals the information rate (pp. 270–271)
- [[entropy-rate]] — "information rate or entropy of an ergodic message source", part of the core (p. 269)
- [[channel-capacity]] — capacity of noiseless and noisy channels, part of the core (p. 269)
- [[joint and conditional entropy]] — here the equivocation $H_y(x)$: uncertainty about the message given the cipher text (p. 272)
- [[sampling-theorem]] (new) — a band-limited signal is represented by amplitudes every $1/2W$ s; unique only with samples from all time (pp. 272–273)
- [[fidelity-criterion]] (new) — Shannon's penalty scheme for assessing damage to messages (p. 274)
- [[error-correcting-code]] — codes that correct $A$ errors in $B$ digits; no systematic way to find best ones yet (p. 276)
- [[two-way-channel-capacity-region]] (new) — plot of capacity A→B against B→A (pp. 275–276)

## Canonical instances
- [[kelly-gambling-inside-information]] — coin and die bits turned into capital growth (pp. 270–271)
- [[substitution-cipher-QXD]] — a 3-letter cipher text has many readings; longer texts have one (p. 272)
- [[pollak-energy-after-zero-samples]] — almost half the energy can lie after the zero samples (pp. 273–274)
- [[reversed-polarity-telegraph]] — no uncertainty added, yet damage done; motivates fidelity criterion (p. 274)
- [[two-way-channel-capacity-plot]] — horizontal and vertical lines, 45° line, intermediate curve (pp. 275–276)

## Bridges (candidates)
- [same-math] Kelly's $2^{NR}$ growth ↔ finance/gambling: the Kelly criterion and doubling rate — the same quantity is the growth rate of wealth.
- [structural-analogy] fidelity criterion with penalties ↔ rate–distortion function — both ask how many bits suffice for a given tolerated damage (Pierce gives no formula).
- [structural-analogy] equivocation falling with cipher length ↔ conditional entropy in statistics — uncertainty shrinks as more data arrives.
- [structural-analogy] two-way channel capacity region ↔ multi-user network capacity — trade-off between directions.

## Questions this raises
- Why does the fair-odds condition matter, and what happens with arbitrary odds, which Kelly's abstract says the result generalizes to?
- Why do finite sets of samples fail while all-time samples succeed, and how do prolate spheroidal functions fix this?
- How does a fidelity criterion change the number of bits per second needed?
- What would a "systematic way" to find best error-correcting codes look like?

## Reading notes
- Page offset: printed = pdf − 16 (pdf 284–293 = printed 268–277).
- The source notes say this scan is the 1961 first edition, not the 1980 Dover edition. The pages here carry the running head "Symbols, Signals and Noise"; no title page was supplied, so I could not check this further.
- The text layer is garbled in places. On p. 271 the factor reads "2NR", which I read as $2^{NR}$. On p. 272 "1/2 PF" is read as $1/2W$, and on pp. 273–274 the symbol for the time $t_0$ is garbled. The captions Fig. XIV-1 to XIV-3 appear in the text layer but the drawings do not. The equivocation symbol reads "H^x)" there and is read here as $H_y(x)$.
- The running head on p. 277 reads "211" in the text layer. This is an OCR slip for 277.
- Figures are described from Pierce's prose only.
