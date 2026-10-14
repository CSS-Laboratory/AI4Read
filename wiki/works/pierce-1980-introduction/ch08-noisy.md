---
id: pierce-1980-introduction/ch08-noisy
work: pierce-1980-introduction
unit: "8 The Noisy Channel"
pages: 145-165
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
# The Noisy Channel (Pierce, ch. 8)

## L0 — One line
Shannon showed that a noisy channel has a capacity $C$ (the largest information rate it can carry), and that a source with entropy below $C$ can be sent with arbitrarily few errors by adding the right kind of redundancy.

## L1 — The gist (≤ 120 words)
How can we guard against errors that noise causes in transmitted digits? Simple repetition detects or corrects rare errors, but it cuts the rate to 1/2 or 1/3. The equivocation (Shannon's measure) is the receiver's leftover uncertainty about what was sent. The information rate is the source entropy minus the equivocation, and the channel capacity is the largest such rate. Shannon's theorem says that below capacity, coding can make errors as rare as we like. Above capacity, the equivocation cannot be pushed below $H-C$. For the symmetric binary channel, $C = 1 + p\log p + (1-p)\log(1-p)$. Efficient codes use long blocks, but even the best ones seem too complicated to use.

**Prerequisites:** entropy $-\sum p\log p$ in bits; probability and conditional probability; binary digits; Chapter V/VII ideas (redundancy, block coding).

## L2 — Key ideas (5–10 bullets)
- Pierce says mathematicians and engineers found, and still find, Shannon's noisy-channel results very surprising, though one layman saw nothing remarkable; he says the questions, however natural they now seem, belong to the post-Shannon era (pp. 146–147).
- Naive repetition detects (×2) or corrects (×3) rare errors, but costs rate 1/2 or 1/3 and fails if errors are frequent. Pierce says this simple repetition approach will never lead to a sound understanding of error correction (pp. 149–150).
- A noisy channel is modelled by probabilities $p_x(y)$ of receiving $y$ when $x$ is sent. This gives entropies $H(x), H(y), H(x,y), H_x(y), H_y(x)$ and the relations 8.6–8.7 (pp. 151–154).
- The equivocation $H_y(x)$ is the information lost. The rate is $R = H(x) - H_y(x)$, and the capacity $C$ is the maximum of $R$ over message sources (pp. 154–156).
- Fundamental theorem: if $H<C$ there is a code with arbitrarily small error. If $H>C$, the equivocation can be made less than $H-C+\epsilon$ but never less than $H-C$ (p. 156).
- The proof averages over random codes with long blocks. Since the average error goes to zero, some code must do at least as well (p. 157).
- For the symmetric binary channel, $C = 1+p\log p+(1-p)\log(1-p)$. $C=0$ at $p=\tfrac12$, and $C$ is the same for $p$ and $1-p$ (pp. 157–159).
- Practical codes use check digits, with block size trading overhead against how many errors can be corrected. Correcting $n$ errors needs code words at distance $\ge 2n+1$ (pp. 159–162).
- Error-free communication means removing the source's natural redundancy and then adding redundancy of the right sort. Pierce says the efficient codes found so far seem too complicated to use (pp. 162, 165).

## L3 — Walkthrough

### Opening: a question that had not been asked (pp. 145–147)
- Pierce says that, at least in science, ideas partly come into being as responses to new or better-phrased questions (p. 145).
- He imagines a communication engineer questioned in 1945 (imagined dialogue; the engineer's replies are Pierce's invention). The engineer might answer: more transmitter power, a less noisy receiver, or frequency modulation, which uses a large bandwidth (p. 146).
- The engineer might say he knows a five-pulse code in which every decimal digit has exactly two "on" and three "off" pulses; with it he can often tell that an error occurred, since a received sequence may have other than two ons (p. 146).
- Asked about error-free delivery, the engineer might say that repeating enough times would work but is very wasteful, so "fix the circuit" (p. 146).
- Told that coding can give an error fraction below any assignable value, up to a calculable number of characters per second, he might well say it seems extremely improbable (pp. 146–147).
- Pierce reports that mathematicians and engineers still find Shannon's results very surprising. He also reports one intelligent layman who saw nothing remarkable. He leaves the reader to be surprised or not (p. 147).
- Reminder: a signal of bandwidth $W$ is represented by $2W$ samples per second, and about 7 binary digits per sample suffice (pulse code modulation). All this works perfectly if the received digits equal the sent ones (p. 147).

### Errors and naive protection (pp. 147–150)
- Errors arise from faulty relays, tubes or transistors, or from interfering noise (p. 147).
- Fig. VIII-1: signal samples $s=\pm1$ for digits 1011 10010. Added noise samples $n$ give $s+n$. Read positive as 1 and negative as 0. Errors occur in positions 2, 3 and 7 (pp. 148–149).
- Errors are most dangerous in text and numbers: $1,000 might become $9,000, and a computer program can become meaningless. If a signal is coded very efficiently (redundancy largely removed), an error can cause a gross change in its meaning (p. 149).
- **Repeat each digit twice:** the rate is halved. A received pair of unlike digits (01 or 10) shows an error, but we cannot tell whether 00 or 11 was sent. This is detection without correction (pp. 149–150).
- **Repeat each digit three times:** the rate is one-third. If a group is not all alike (e.g. 101), assume a single error, so 111 was sent. This works if the chance of two errors in a group of three is negligible (p. 150).
- Cost: we pay the full rate loss even when nearly all digits are right, and the schemes fail when errors are frequent enough that more than one can fall within two or three digits (p. 150).

> **Intuition note:** Repetition buys error-spotting by wasting channel use on every digit, good or bad. Shannon's question is whether a smarter use of the same extra digits can do much better.

### The abstract model of a noisy channel (pp. 150–153)
- Discrete channel: digits 0–9 as "buttons" at the transmitter and "lights" at the receiver (Fig. VIII-2). Pressing button 4 may light any light, with probability $p_4(6)$ for light 6. Looking backward, if light 6 lights, button 4 was pressed with probability $p_6(4)$. In a noiseless system $p_6(6)=1$ and the others are 0 (pp. 151–152).
- Assumption: each outcome is a matter of chance, independent of what has gone before (pp. 151–152).
- $x$ = characters sent, $y$ = characters received, $m$ of each. Source entropy (from Chapter V):
$$H(x)=\sum_{x=1}^{m}-p(x)\log p(x)\tag{8.1}$$
$$H(y)=\sum_{y=1}^{m}-p(y)\log p(y)\tag{8.2}$$
- $H(x)$ depends only on the input. $H(y)$ depends on the input and on the errors (p. 152).
- Joint, and the two conditional entropies:
$$H(x,y)=\sum_{x=1}^{m}\sum_{y=1}^{m}-p(x,y)\log p(x,y)\tag{8.3}$$
$$H_x(y)=\sum_{x=1}^{m}\sum_{y=1}^{m}-p(x)\,p_x(y)\log p_x(y)\tag{8.4}$$
$$H_y(x)=\sum_{y=1}^{m}\sum_{x=1}^{m}-p(y)\,p_y(x)\log p_y(x)\tag{8.5}$$
- Each conditional entropy is the uncertainty for a given condition, weighted by the probability of that condition and summed over conditions. Pierce says this form is reminiscent of the entropy of a finite-state machine (p. 153).
- Meanings (p. 154):
  - $H(x)$: uncertainty of which character is sent.
  - $H(y)$: uncertainty of which is received.
  - $H(x,y)$: uncertainty of the pair.
  - $H_x(y)$: the sender's average uncertainty about what will be received.
  - $H_y(x)$: the recipient's average uncertainty about what was sent.
- Relations:
$$H(x,y)=H(x)+H_x(y)\tag{8.6}$$
$$H(x,y)=H(y)+H_y(x)\tag{8.7}$$
- If $H_x(y)$ is zero, then $H_y(x)$ is zero and $H(y)=H(x)$. This is the noiseless channel (p. 154). The text layer prints "$H(y)$" here, but the context requires $H_x(y)$.

### Equivocation, rate and capacity (pp. 154–156)
- $H_y(x)$ is a natural measure of the information lost in transmission. It is called the **equivocation** (p. 154).
- With entropies in bits per second, the rate of transmission is (pp. 154–155):
$$R=H(x)-H_y(x)\tag{8.8}$$
$$R=H(y)-H_x(y)\tag{8.9}$$
$$R=H(x)+H(y)-H(x,y)\tag{8.10}$$
- For 8.10, the text layer is garbled. I read it from the author's sentence that the rate is "the entropy of $x$ plus the entropy of $y$ less" $H(x,y)$ (p. 155).
- Noiseless case: $p(x,y)=0$ unless $x=y$, so $H(x,y)=H(x)=H(y)$ and $R=H(x)$ (p. 155).
- Plausibility (Fig. VIII-3): an observer compares sent and received signals and sends correction data. Shannon shows that the entropy of the correction signal must equal the equivocation (p. 155).
- $R$ depends on both channel and source. The maximum of $R$ over message sources is the **channel capacity** $C$ (pp. 155–156).

> **Intuition note:** The rate is what the received signal tells you about what was sent: the source's uncertainty minus the uncertainty left after receiving. The capacity is that quantity for the best possible source.

### Shannon's fundamental theorem (pp. 156–157)
- Statement (p. 156, as printed, minus signs restored from context): for a discrete channel of capacity $C$ and a discrete source of entropy $H$ per second:
  - If $H<C$, there is a coding system with arbitrarily small frequency of errors (or arbitrarily small equivocation).
  - If $H>C$, one can encode so that the equivocation is less than $H-C+\epsilon$, with $\epsilon$ arbitrarily small.
  - No encoding gives an equivocation less than $H-C$.
- As errors become more frequent, $C$ decreases gradually. To get as few errors as wished, the rate must be at most $C$ (p. 156).
- Method: as in efficient source coding, long blocks of characters must be coded together, and only certain sent/received blocks have more than vanishing probability (pp. 156–157).
- Proof idea: Shannon finds the error frequency averaged over all codes chosen at random (all associations of input blocks with output blocks). When $C$ exceeds the source entropy, this average goes to zero as block length grows. So some single code must do at least this well. Pierce quotes one theorist calling this proof "weird" (p. 157).

> **Intuition note:** You do not need to find the good code to know it exists. If the average over all codes is good, at least one code is that good. Long blocks are needed so that the average error becomes small.

### The symmetric binary channel (pp. 157–159)
- Setup: a 1 is received as 1, and a 0 as 0, each with probability $p$. Errors have probability $1-p$. Probabilities are independent of the past and constant in time (Fig. VIII-4) (p. 157).
- By symmetry, the capacity is reached when sending 1 and 0 are equally likely. Then
$$H(x)=H(y)=-\left(\tfrac12\log\tfrac12+\tfrac12\log\tfrac12\right)=1\ \text{bit per symbol}.$$
- Equivocation: each of the two received symbols has probability $\tfrac12$. For each, the sent symbol is the correct one with probability $p$ and the other with probability $1-p$. Each received symbol contributes $\tfrac12\big(-p\log p-(1-p)\log(1-p)\big)$. Summing the two contributions (p. 158):
$$H_y(x)=-p\log p-(1-p)\log(1-p)$$
- From 8.8 (p. 158):
$$C=1+p\log p+(1-p)\log(1-p)$$
- $C$ is 1 minus the function plotted against $p$ in Fig. V-1 (p. 159). Consequences (p. 159):
  - At $p=\tfrac12$, $C=0$: the received digit does nothing to resolve uncertainty about the sent one.
  - $C$ is the same for $p=0$ and $p=1$: a channel that always inverts is as informative as a perfect one.
  - One error in 10 digits: $C$ falls to .53 of its errorless value. One error in 100: to .92.
- Pierce testifies that the simplicity of this result is in a sense misleading (to him at least). For an unsymmetrical binary channel (1 received as 1 with probability $p$, 0 as 0 with a different probability $q$), the capacity expression "is a mess" (p. 159).

> **Intuition note:** Noise costs capacity gradually, not all at once. A channel that is wrong 1% of the time still carries 92% of a bit per digit.

### Codes in practice (pp. 159–163)
- Hamming's examples were mentioned in Shannon's original paper. Golay published on error-correcting codes in 1949, Hamming in 1950. Pierce notes these codes came after Shannon showed error-free transmission possible (p. 159).
- **Check digits in a 4×4 grid** (Fig. VIII-5) (p. 160):
  - Message digits go in blocks of 16. Each row and column gets a check digit (0 or 1) making its total number of 1s even.
  - In the author's example the column counts are 2, 2, 2, 4 and the row counts are 4, 2, 2, 2, all even.
  - A single error in a message digit makes one row and one column odd. The digit where they cross is changed.
  - A single error in a check digit gives an odd number of 1s in a row or in a column. We know the error is not in the message.
  - Cost: $16+8=24$ digits sent, ratio $24/16=1.5$.
  - With 400 message digits, 40 check digits give $440/400=1.1$, but only one error per block of 440 digits can be corrected, rather than one error per block of 24 (pp. 160–161).
- **General code:** a code is a set of $2^M$ blocks representing all $M$-digit message blocks. The code blocks are longer than $M$ (p. 161).
- **Distance:** the number of digits that must change to turn one sequence into another. Example: 1111 and 0010 are at distance 3 (p. 161).
- **Addition mod 2:** $0+0=0$, $0+1=1$, $1+1=0$ (like binary addition without carries). The distance equals the number of 1s in the sum mod 2. Examples: $1111+0010=1101$ (3 ones); $10110101+10011101=00101000$ (2 ones) (pp. 161–162).
- The check digits in Fig. VIII-5 are sums mod 2 of rows and columns (p. 162).
- **Rule:** deducing the sent block despite $n$ digit errors is possible if code blocks are at distance at least $2n+1$ (p. 161). For the received block always to be nearer to the sent block than to any other code block, all code blocks must be separated by at least $2n+1$ (p. 162). $n$ errors move a received block distance $n$ from the sent block, and possibly $n$ nearer to another code block (pp. 161–162).
- Slepian and others have found the best codes for quite a number of $M$ and $n$. Pierce says "I won't attempt to tell how" (p. 162).
- Pierce says there are "more error-correcting codes than we know what to do with": equipment for the longer, efficient codes is too complicated. Single-error codes don't help much, because telephone-line noise comes in long pulses that corrupt several successive digits (p. 162).
- Hagelbarger (Bell Laboratories) devised a code using twice the number of digits of the text. It corrects up to six adjacent errors with quite simple equipment. Pierce calls it "inefficient but useful" (pp. 162–163).

### Summary of the chapter (pp. 163–165)
- Chapter VII removed redundancy. This chapter adds redundancy to a nonredundant message to get virtually error-free transmission (p. 163).
- Over a noisy channel, the recipient's uncertainty about what was sent is not fully resolved by receiving. The remainder depends on how often a received symbol differs from the sent one (p. 163).
- Rate is source entropy minus equivocation. Capacity is the greatest possible rate (p. 164). Capacity is a quantity computable from the error probabilities (p. 164).
- Block coding is used here "to add redundancy to nonredundant messages". The whole problem of efficient, error-free communication is to remove the messages' inefficient natural redundancy and then add redundancy of the right sort (p. 164).
- On a binary symmetric channel with 1 digit in 100 wrong, only 92 correct message digits can be sent per 100 digits fed in. Eight extra check digits per 92 message digits are included "in some way" (pp. 164–165).
- Finding efficient codes is formidable even here, and the best codes seem too complicated to use. But we now know what the problem is and, in principle, how well we can do (p. 165).

## Toy example (ours, not from the text)
Symmetric binary channel with $p=0.75$ (a correct digit 75% of the time), inputs 0 and 1 equally likely.

Joint probabilities: $p(1,1)=p(0,0)=0.5\times0.75=0.375$ and $p(1,0)=p(0,1)=0.5\times0.25=0.125$.
- $H(x)=H(y)=1$ bit, since the outputs are also equally likely.
- $H(x,y)=-2(0.375\log_2 0.375)-2(0.125\log_2 0.125)$. Here $\log_2 0.375=-1.41504$, so $0.375\times1.41504=0.53064$, and doubling gives $1.06128$. Also $0.125\times3=0.375$, and doubling gives $0.75$. So $H(x,y)=1.81128$.
- By 8.7, $H_y(x)=1.81128-1=0.81128$.
- By 8.8, $R=1-0.81128=0.18872$.
- Check with 8.10: $1+1-1.81128=0.18872$. ✓.
- Check with the formula: $C=1+0.75\log_2 0.75+0.25\log_2 0.25=1+0.75(-0.41504)+0.25(-2)=1-0.31128-0.5=0.18872$. ✓.

Equal inputs are optimal by symmetry (p. 157), so $C\approx0.189$ bit per digit. By the theorem, reliable coding needs a message rate of at most 0.189 message digits per channel digit.

## Concepts
- [[noisy-channel]] — channel where the received character is chance-dependent on the sent one, with probabilities $p_x(y)$ (p. 151)
- [[joint and conditional entropy]] — $H(x,y)$, $H_x(y)$, $H_y(x)$: pair uncertainty and uncertainty given the other symbol (pp. 153–154)
- [[chain-rule]] — relations 8.6 and 8.7 (p. 154)
- [[equivocation]] (new) — $H_y(x)$, the recipient's remaining uncertainty about what was sent; the information lost (p. 154)
- [[mutual information I(X;Y)]] — Pierce does not use this name. His rate $R$ in 8.8–8.10 is the same quantity (p. 155; canon link, not stated in this unit)
- [[channel-capacity]] — maximum rate $R$ over message sources, in bits per symbol or per second (pp. 155–156, 164)
- [[noisy-channel-coding-theorem]] — Shannon's fundamental theorem for the noisy channel (p. 156)
- [[redundancy]] — here: added deliberately, in the right form, to permit correction (p. 164)
- [[error-correcting-code]] — code with check digits or large distances between code blocks (pp. 159–162)
- [[binary-symmetric-channel]] (new) — binary channel where each digit is received correctly with probability $p$ (p. 157)
- [[hamming-distance]] (new) — number of digit changes between two binary sequences; separation $\ge 2n+1$ corrects $n$ errors (pp. 161–162)
- [[parity-check-digit]] (new) — extra digit chosen to make a count of 1s even (p. 160)
- [[random-coding-argument]] (new) — error averaged over random codes goes to zero as block length grows (when $C$ exceeds the source entropy), so some good code exists (p. 157)

## Canonical instances
- [[binary-symmetric-channel]] — capacity $1+p\log p+(1-p)\log(1-p)$; .53 at 1/10 errors and .92 at 1/100 (pp. 158–159)
- [[repetition-code]] — sending each digit twice (detect) or three times (correct) costs rate 1/2 or 1/3 (pp. 149–150)
- [[parity-grid-code]] — 4×4 message digits with 8 even-parity check digits (pp. 160–161)
- [[hagelbarger-code]] — doubles the digits and corrects up to six adjacent errors (pp. 162–163)

## Bridges (candidates)
- [same-math] equivocation and rate (8.6–8.10) ↔ information-theory: conditional entropy and mutual information identities — same quantities under other names.
- [structural-analogy] random-coding existence proof ↔ probabilistic method in combinatorics: an average over objects shows one object has the property.
- [structural-analogy] distance $\ge 2n+1$ for correcting $n$ errors ↔ geometry of nearest-neighbour classification: spheres of radius $n$ around code words must not overlap.

## Questions this raises
- Why does a larger block length make the random-code average error shrink, and what does it cost in complexity?
- What is the capacity of the unsymmetrical binary channel that Pierce calls "a mess"?
- Why are the best codes too complicated for practical equipment, and how do simple codes such as Hagelbarger's handle bursts of errors?
- Is the 92-in-100 figure at 1% error achievable by a code that is practical, not only possible in principle?

## Reading notes
- Page offset: printed = pdf − 16 (pdf 161 = printed 145). Printed numbers are given in this file.
- Edition: per the metadata, this PDF is the 1961 Harper & Brothers first edition, titled *Symbols, Signals and Noise*, not the 1980 Dover edition named in the work citation. The page headers show "Symbols, Signals and Noise". Cited page numbers follow this scan and may not match Dover.
- The text layer is heavily garbled. I checked the images only for pdf 169 (p. 153) and pdf 174 (p. 158). Equations 8.6–8.10, the theorem text and the example sequences come from the text layer plus the author's own prose, and I did not check them against images.
- Misprint on p. 153 (image): Eq. 8.3 shows both sums running over $x=1$; the second should be $y=1$. I wrote the sums with $x$ and $y$.
- The text layer for 8.9 shows "$H_f(y)$"; I read it as $H_x(y)$, from the author's prose ("sender's uncertainty as to what will be received").
- The sent line of the double-sending example (p. 149) is garbled in the text layer; the received line reads 110011000111110011 there, and the prose gives the message 101001101. I could not read the 4×4 grid contents (p. 160) and did not reproduce them. The column and row counts are taken from the text layer.
- The theorem on p. 156 lost its minus signs in the text layer, and the printed first case reads $H<C$. I restored $H-C+\epsilon$ and $H-C$ from context and kept the first case as $H<C$. Pierce's closing summary (p. 164) says the entropy is less than $C$.
- Exercises: the chapter contains none.
