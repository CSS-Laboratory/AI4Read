---
id: pierce-1980-introduction/ch05-entropy
work: pierce-1980-introduction
unit: "5 Entropy"
pages: 78-106
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Entropy (Pierce, ch. 5)

## L0 — One line
The entropy $H=-\sum p_i\log_2 p_i$ of a message source, measured in bits, equals the average number of binary digits per symbol needed to encode its messages, and long-block (Huffman) coding gets as close to it as we like.

## L1 — The gist (≤ 120 words)
How many binary digits per symbol are really needed to encode what a source produces? Pierce defines entropy as a measure of the source's freedom of choice, which is also the receiver's uncertainty. He argues that entropy gives the average number of binary digits per symbol needed. For independent symbols, long messages almost always fall into about $2^{MH}$ probable ones. Huffman coding (short codes for likely symbols) of long blocks comes within a negligible excess of $H$. Shannon's noiseless-channel theorem says a source can be sent over a channel of capacity $C$ if its entropy is at most $C$, and cannot if it is larger. English text is hard to measure: Shannon's guessing experiment gives 0.6–1.3 bits per letter.

**Prerequisites:** logarithms to base 2; probability of independent events; sums ($\Sigma$); Chapters III–IV ideas (ergodic source, block coding, binary digits).

## L2 — Key ideas
- Information is measured by the logarithm of the number of possible messages, not the number itself. Four telegraph lines carry 4 times the digits, so the measure should scale that way (p. 80).
- Entropy for independent symbols is $H=-\sum p_i\log p_i$ bits per symbol (5.1). For two symbols it is largest (1 bit) when both are equally likely and zero when the outcome is certain; more choice and more freedom of choice raise it (pp. 81–85).
- Shannon's theorem: of all long $M$-symbol messages, only about $2^{MH}$ are probable. Labelling just those needs about $MH$ binary digits (pp. 88–90).
- For sources with memory, entropy is approached by taking very long blocks (5.3), or by conditioning on the preceding block (5.4), or by a finite-state machine (a machine with states that emit symbols) (5.5). Ignoring dependence always overestimates $H$ (pp. 90–94).
- A Huffman code (a code giving short code words to likely symbols) uses less than one binary digit per symbol more than $H$. Using long blocks makes the excess negligible (pp. 94–97).
- Noiseless-channel theorem: a channel of capacity $C$ (the largest entropy it can carry, in bits/s) can carry a source of entropy $H$ at rate $(C/H)-\epsilon$ symbols/s, and not above $C/H$ (p. 98).
- Pierce uses "bit" for amount of information and "binary digit" for 0/1. The entropy in bits is usually different from the number of binary digits sent (pp. 98–100).
- For English, the ergodic-source model (a source with unchanging statistics) is useful but imperfect. Frequencies of 100-letter blocks cannot be measured from text. Shannon's estimate is 0.6–1.3 bits per letter (pp. 101–104).

## L3 — Walkthrough

### Motivation: is there a minimum? (pp. 78–80)
- Chapter IV showed that the digits needed depend on the encoding. Blocks of letters need fewer digits per character than single letters, and word-by-word coding needs far fewer still (p. 78).
- Pierce asks whether some statistical measure of the source tells the minimum average number of binary digits per symbol, without trying every code (p. 79).
- The source is an ergodic source (unvarying statistics: symbol frequencies and following-probabilities). A source always exercises choice, or its output would be fully predictable. The recipient's matching uncertainty is resolved by reading the message (p. 79).
- A source with no choice (all 1s or all 0s) needs no message to be examined: the recipient could predict it in advance. So the measure must grow with choice and with the recipient's uncertainty (p. 80).
- Counting messages ($2,4,16,256,\dots$ for 1, 2, 4, 8 digits) is rejected. Four telegraph lines at equal speed send 4 times the digits, so it "seems reasonable" that information should be 4 times as large. Hence information is the logarithm of the number of messages (p. 80).
- This measure is called **entropy**. Pierce says to clear one's mind of the entropy of physics first, since mixing the two caused lasting confusion (p. 80).
- Entropy is measured in bits, per letter, word, message or second (pp. 80–81). It rises with the number of choices and with freedom of choice. A restriction that makes some messages very frequent or very rare lowers it (p. 81).

### Entropy for independent symbols (pp. 81–86)
- **Two symbols.** The source picks X with probability $p_0$ and Y with $p_1$, each choice independent of earlier ones. The probabilities must not change in time if the source is to be ergodic (p. 81).
$$H=-(p_0\log p_0+p_1\log p_1)\ \text{bits per symbol}$$
- Pierce says the real justification will become apparent only later and defers it (p. 81). Logarithms are to base 2: $\log_2 x$ is the power to which 2 is raised to give $x$ (p. 82).
- Fair coin: $p_0=p_1=\tfrac12$, $H=-[(\tfrac12)(-1)+(\tfrac12)(-1)]=1$ bit per toss. One binary digit per toss encodes it, so digits equal entropy here (pp. 82–83).
- Biased coin with $p_1=\tfrac34$, $p_0=\tfrac14$: $H=-[(\tfrac14)(-2)+(\tfrac34)(-.415)]=.811$ bit per toss. We "feel" fewer than one digit per toss should suffice, but it is not yet clear how many (p. 83).
- Figure V-1 plots $H$ against $p_1$ (with $p_0=1-p_1$). The maximum is 1 at $p_1=0.5$ and $H=0$ at $p_1=0$ or 1. The curve is symmetric about $p_1=0.5$ because relabelling heads and tails changes nothing (pp. 83–84).
- **$n$ symbols.** With independent choices and probabilities $p_i$:
$$H=-\sum_{i=1}^{n}p_i\log p_i\ \text{bits per symbol}\tag{5.1}$$
  For $n=2$ this is the earlier case (pp. 84–85).
- Two honest coins: four outcomes of probability $\tfrac14$, $H=-(4\cdot\tfrac14\cdot(-2))=2$ bits per pair. One digit per coin gives 2 digits, again equal to $H$ (p. 85).
- $n$ equally probable symbols: $H=-\log(1/n)$. A fair die gives $\log 6=2.58$ bits per throw (p. 85).
- All $N$-digit binary numbers equally likely: there are $2^N$ of them, $H=-\log(1/2^N)=N$ bits, and $N$ digits represent each. Pierce says this shows why the logarithm must be the right function (p. 86).

> **Intuition note.** Entropy is the average of "$\log$ of how many equally likely alternatives this outcome is worth". It is 0 when nothing is open and grows as the choices get more even and more numerous. For equally likely messages it is just the number of yes/no digits needed to name one of them.

### Word entropy of English and Zipf's law (pp. 86–88)
- Take a source that picks English words independently with their English probabilities (first-order word approximation of Ch. III). Ranked by frequency (the = 1, of = 2, …), empirically the rank-$r$ word has probability very nearly (if $r$ is not too large)
$$p_r=.1/r\tag{5.2}$$
  This is called Zipf's law; it is used here, and Pierce defers its discussion to Chapter XII (Fig. V-2; p. 86).
- It cannot hold for all words. A coin with extra "edge" probability $\tfrac1{10}$ would give 110 outcomes in 100 tosses, which is absurd. Probabilities must sum to 1. Summing (5.2) reaches 1 by $r=8{,}727$, which would leave no room for other words (pp. 86–87). (The text writes "equation 5.1" here; context shows it means 5.2; see Reading notes.)
- Shannon kept only the 8,727 most frequent words so the sum is 1, and found $H=11.8$ bits per word (p. 88).
- Chapter IV encodings: 5 digits/character (27.5 per word) letter by letter; about 14 per word with codes for 16,357 words and 27 characters. Pierce suspects the true requirement is the entropy, 11.8 here (p. 88).

### Shannon's theorem on probable messages (pp. 88–90)
- Consider all messages of $M$ symbols from an independent-symbol source. In probable messages symbol $i$ occurs about $Mp_i$ times. Other kinds of message are possible but seldom produced (p. 88).
- **Theorem (stated informally):** if $H$ is the entropy per symbol, there are just about $2^{MH}$ probable messages; the rest have vanishingly small probability. Rank messages by probability and give binary labels of $MH$ digits to the top $2^{MH}$. Then we are almost certain to have a label for the message actually produced (pp. 88–89).
- Fair binary digits, $M=1000$: $MH=1000$, so $2^{1000}$ probable messages and 1000-digit labels (p. 89).
- Biased coin (heads $\tfrac34$), $M=1000$: $MH=811$, so only $2^{811}$ probable messages. Labelling them takes 811 digits. The scheme is not foolproof: the source may occasionally produce an unlabelled message, which then cannot be sent with 811 digits (p. 89).
- This saving uses **block encoding**: lumping 1000 (or another large number of) digits and coding each probable block (p. 90).

> **Intuition note.** A long run of a biased coin looks "typical": about the expected share of heads. There are far fewer typical sequences than all sequences. Naming only those costs fewer digits: about $H$ per symbol, e.g. .811 instead of 1 for the biased coin.

### Sources with memory: blocks, conditional entropy, finite-state machines (pp. 90–94)
- English has constraints of word order, so symbols are not independent. In any ergodic process of which we are to make mathematical sense, the effect of the past must fade with remoteness (p. 90).
- Cut the message into very long blocks. Only symbols near a block's start depend on the previous block, and they become a negligible fraction. So (5.1) can be applied to blocks, with $P(B_i)$ the probability of the $i$th block (pp. 90–91). A mathematician would object to calling this the entropy: it approaches the entropy as blocks lengthen. Dividing by block length $N$:
$$H=-(1/N)\sum_i P(B_i)\log P(B_i)\ \text{bits per symbol}\tag{5.3}$$
- An entropy estimate is always high if it fails to take into account some relations between symbols. As $N$ grows, (5.3) decreases toward the true entropy (p. 91).
- **Additivity.** Entropies of simultaneous independent sources add. An intermittent source's entropy is multiplied by the fraction of time it operates (p. 91).
- **Conditional view.** After a particular preceding block (e.g. TH, or NQ) we have a different "source". After NQ, U has probability 1. The overall entropy is the average of these sources' entropies, each weighted by how often it operates. For a digram source (only the last letter matters), the source after E operates in .13 of instances, after W in .02 (pp. 91–92).
- Formally, if block $B_i$ of $N$ symbols has just occurred, the next symbol is $S_j$ with probability $p_{B_i}(S_j)$. Its source has entropy $-\sum_j p_{B_i}(S_j)\log p_{B_i}(S_j)$ (reconstructed from a garbled line), and it operates with fraction $p(B_i)$. Summing over all blocks gives
$$H_N=-\sum_{i,j}p(B_i)\,p_{B_i}(S_j)\log p_{B_i}(S_j)\tag{5.4}$$
  As $N$ grows, $H_N$ approaches the entropy of the source. If no statistical influence reaches beyond $N$ symbols (digram source: $N=1$; trigram: $N=2$), then $H_N$ is the entropy (pp. 92–93).
- Shannon writes it with $p(B_i,S_j)=p(B_i)\,p_{B_i}(S_j)$: $H_N=-\sum_{i,j}p(B_i,S_j)\log p_{B_i}(S_j)$ (p. 93).
- **Finite-state machine** (Ch. III). Treat each state $i$ as a source. In state $i$, symbol $j$ has probability $p_i(j)$ (example: $p_{10}(3)=.03$). State entropy is $H_i=-\sum_j p_i(j)\log p_i(j)$. With $P_i$ the probability of being in state $i$:
$$H=\sum_i P_iH_i=-\sum_{i,j}P_i\,p_i(j)\log p_i(j)\ \text{bits per symbol}\tag{5.5}$$
  (p. 93)
- The three methods (5.3 / 5.4 / 5.5) are equivalent and rigorous for true ergodic sources. English is only approximately ergodic (p. 94).

> **Intuition note.** Entropy with memory is "the average surprise of the next symbol, given what came before". Ignoring the past makes the source look more random than it is. That is why single-letter estimates are too high and longer contexts give lower numbers.

### Huffman coding (pp. 94–97)
- The problem is now to code efficiently a sequence drawn from a very large group of symbols with given probabilities. Shannon and Fano showed methods. Huffman found a better one (p. 94).
- Example: eight words the, man, to, runs, house, likes, horse, sells with probabilities .50, .15, .12, .10, .04, .04, .03, .02 (Fig. V-3, p. 95). Their entropy is 2.21 bits per word (as printed); fixed 3-digit labels need 3 digits per word (p. 94).
- **Construction** (Fig. V-3): repeatedly join the two lowest probabilities. .02+.03→.05; .04+.04→.08; .05+.08→.13; and so on until 1.00. Label each upper path 1 and each lower path 0. A word's code is the digits met going left from 1.00 to that word (pp. 95–96).
- The average digits per word is the sum of probability × code length: 2.26, a little above the entropy but below 3 (p. 96).
- It can be proved that the Huffman code is the most efficient code for symbols with given probabilities. It always needs less than one binary digit per symbol more than the entropy (p. 96).
- With blocks of 1, 2, 3, … independent symbols (block probability = product), the extra is still less than one digit per block, so it becomes a negligible fraction. Digits per block equal entropy per block as closely as we like (pp. 96–97).

> **Intuition note.** Frequent symbols get short codes and rare ones long codes. The Huffman code costs less than one extra digit per code word above the entropy. For a long block, that extra digit is a negligible fraction per symbol.

### Channel capacity and the noiseless-channel theorem (pp. 97–98)
- A channel transmitting $C$ on/off pulses per second has capacity $C$ bits per second. If a source's entropy $H$ (bits/s) is less than $C$, Huffman coding lets it be sent (p. 97).
- Other channels (three pulse heights; Morse-like pulses of different lengths) can be fed different sources. The highest entropy that can be sent is the **channel capacity** $C$, in bits per second. Huffman coding converts it to very close to $C$ binary digits per second, and this can be run in reverse (p. 97).
- **Shannon's fundamental theorem of the noiseless channel** (quoted by Pierce): let a source have entropy $H$ (bits per symbol) and a channel have capacity $C$ (bits per second). Then the source output can be encoded to transmit at average rate $(C/H)-\epsilon$ symbols per second, with $\epsilon$ arbitrarily small. Transmitting at an average rate above $C/H$ is not possible (p. 98).
- Plain restatement: if $H\le C$ the source can be sent; if $H>C$ it cannot. Pierce says the first part was indicated above. The converse (no code uses fewer than $H$ digits per symbol) "can be proved", but is not shown here (p. 98).

### Bit versus binary digit (pp. 98–100)
- "Bit" is a contraction of "binary digit". Pierce uses "bit" only as a measure of information and "binary digit" for 0/1 (p. 98).
- Example: a source emits 1 with probability ¼ or ¾ (the two probabilities in the earlier biased coin; the scan is garbled) and 10 symbols/s. It makes 10 digits/s but has entropy .811 bit per digit, so 8.11 bits/s. On average 8.11 digits/s would suffice (p. 99).
- A channel carrying 10,000 arbitrary on/off pulses/s has capacity 10,000 bits/s. If it sends a completely repetitive pattern, the information actually sent is far lower than its 10,000 digits/s (the figure is missing in the scan; the context implies essentially none) (p. 99).
- A bit as a measure: an elementary choice between two equally probable possibilities. For grammatical English there is about one bit of choice per letter at the source, and about one bit of uncertainty per letter at the destination (p. 99).
- If we know the source entropy is below the digits used per second, fewer digits could be used in principle. Calling digit rate "bit rate" is convenient but risky for the inexperienced (pp. 99–100).

### Prefix property and decoding (pp. 100–101)
- In the Huffman code (Table XII), no code is the first part of another. This is the **prefix property** (p. 100).
- Example message: "the man sells the house to the man the horse runs to the man", encoded as one digit string (p. 100).
- Decoding from a point in the middle (after the first vertical dashed line): take the shortest digit sequence that is a code word, here 00010 = likes. After a few errors the decoded words line up with the true ones, and then all are correct. So we need not know where the message starts in order to decode it (as correctly as possible) (p. 101).

### How long must blocks be? English text (pp. 101–104)
- Two reasons for long blocks: (1) make the Huffman excess negligible; (2) capture the influence of earlier symbols (via 5.3). For English, condition (2) governs (p. 101).
- Shannon estimated entropy per letter by testing a person's ability to guess the next letter after seeing 1, 2, 3, … preceding letters. The alphabet was 26 letters plus space (p. 101).
- Fig. V-4 shows upper and lower bounds on entropy against the number of letters seen. The curve falls slowly from 10 to 15 letters but substantially between 15 and 100. So blocks as long as about 100 letters might be needed (pp. 101–103).
- From Fig. V-4 the entropy of English appears to lie between 0.6 and 1.3 bits per letter. Taking 1 bit per letter, a 100-letter block needs about 100 digits, so there are $2^{100}$ probable sequences. Pierce writes $2^{100}$ as 1 followed by 30 zeros, i.e. roughly $10^{30}$ (p. 103).
- Counting the frequency of each of $10^{30}$ blocks is physically impossible. It is also impossible in principle, because most such sequences have never been written down, so their frequencies do not exist in the text (p. 103).
- Pierce separates two questions: how accurate is the ergodic-source description of English, and what is the best statistical description? One may hold that suitable probabilities exist in the human being even if they cannot be taken from text. Equations 5.4 and 5.5 also give entropy for ergodic sources. A finite-state state-and-symbol picture of a person is "appealing" (p. 103).
- **Linguists' objection:** some linguists hold that English grammar is inconsistent with the output of a finite-state machine (p. 103). Pierce says a good description must involve grammar, the next chapter's topic (p. 104).
- It is "safe if not subtle" to apply an exact theory mechanically to its ideal abstraction. Using it on real problems needs wisdom (p. 104).
- Coding numbers for English (per character, including space): ignoring letter frequencies, 4.76 digits; letter by letter with frequencies, 4.03; word by word, 2.14. Shannon's entropy estimate is .6 to 1.3 bits per letter, so one may hope for better coding (p. 104). (Added step: 11.8 bits per word ÷ 5.5 characters per word ≈ 2.15, consistent with the 2.14.)
- Pushing any one procedure to the limit can produce nonsense. Part of this may be due to man differing from an ideal ergodic source, part to an inappropriate approach. The ergodic-source model of man is judged "good and useful if not perfect" (p. 104).

### Summary of the chapter (pp. 104–106)
- Entropy in bits per symbol or per second gives the average number of binary digits needed (p. 105). For the source it measures choice. For the recipient it measures uncertainty, resolved on receipt (p. 105).
- For $n$ equally probable messages, $H=\log n$ (p. 105). In general use (5.1); with long blocks, (5.3); other forms are (5.4) and (5.5) (p. 105).
- With a Huffman code, it is possible to prove that the entropy of an ergodic source in bits equals the average number of binary digits needed. An approximation that disregards the effect of some past symbols is always too large (pp. 105–106).
- The largest entropy transmittable over an error-free channel is its capacity. If the source entropy is below it, the messages can be encoded to be sent (p. 106).
- Shannon's guessing experiment shows the entropy of English lies between .6 and 1.3 bits per character (p. 106).

## Toy example (ours, not from the text)
Source: binary symbols, 1 with probability $.9$, 0 with $.1$, independent.

- Entropy: $H=-(.9\log_2 .9+.1\log_2 .1)=.9(.152)+.1(3.322)=.137+.332=.469$ bit per symbol.
- Symbol by symbol, Huffman uses 1 digit per symbol (excess $\approx .53$).
- Blocks of 2: probabilities $11:.9\cdot.9=.81$; $10:.09$; $01:.09$; $00:.01$ (sum $=1.00$). Join the two lowest: $.01+.09=.10$; then $.09+.10=.19$; then $.81+.19=1$. Code lengths: $11\to1$, $10\to2$, $01\to3$, $00\to3$.
- Average length per pair: $.81(1)+.09(2)+.09(3)+.01(3)=.81+.18+.27+.03=1.29$ digits per pair, so $.645$ per symbol.
- Check the bound: entropy per pair is $2(.469)=.938$ and $.938\le1.29<1.938$, the "less than one extra digit" bound. Per symbol the excess has fallen from $.53$ to $.18$. Longer blocks would shrink it further.

## Concepts
- [[bit]] — here a measure of information: one binary choice between equally probable options; not the same as a binary digit (pp. 98–100)
- [[entropy]] — $H=-\sum p_i\log_2 p_i$; the source's choice, the recipient's uncertainty, and the average digits per symbol needed (pp. 79–85, 105)
- [[entropy-rate]] — entropy per symbol of a source with memory, as limit of (5.3), $H_N$ of (5.4), or (5.5) (pp. 91–94)
- [[joint-and-conditional-entropy]] — (5.4) averages the entropy of the next symbol given the preceding block, weighted by block probability (pp. 91–93)
- [[typical-set-aep]] — about $2^{MH}$ probable $M$-symbol messages carry almost all probability (p. 88)
- [[source-coding-theorem]] — encoding takes about $H$ digits per symbol; converse only asserted provable here (pp. 98, 105)
- [[huffman-arithmetic-coding]] — Huffman code: always less than one digit per symbol above $H$ (pp. 94–97)
- [[prefix-code-kraft]] — prefix property: no code word begins another; allows decoding without a known start (pp. 100–101). Kraft's inequality is not stated here.
- [[channel-capacity]] — highest entropy (bits/s) that can be sent over a given error-free channel (p. 97)
- [[noiseless-channel-theorem]] (new) — transmission rate $(C/H)-\epsilon$ symbols/s is possible, above $C/H$ is not (p. 98)
- [[ergodic-source]] (new) — a source with unchanging statistics, whose past matters less the further back it lies (pp. 79, 90)
- [[zipf-law]] (new) — word probability $\approx .1/r$ for rank $r$ (5.2); fails when summed over all words (pp. 86–87)
- [[block-coding]] (new) — coding long blocks as single symbols to approach entropy (pp. 90, 96–97)

## Canonical instances
- [[fair-coin-one-bit]] — $H=1$ bit per toss; also two coins = 2 bits and $N$-digit binary numbers $=N$ bits (pp. 82–86)
- [[biased-coin-entropy]] — heads $\tfrac34$ gives .811 bit; Fig. V-1 curve (pp. 83–84)
- [[english-word-entropy-shannon]] — 11.8 bits per word from the 8,727-word Zipf model (p. 88)
- [[huffman-eight-word-example]] — eight words, 2.26 digits against 3 (pp. 94–96)
- [[shannon-guessing-experiment]] — English entropy between .6 and 1.3 bits per letter (pp. 101–103)

## Bridges (candidates)
- [same-math] Probable $M$-symbol messages ($2^{MH}$) ↔ information-theory canon "typical set / AEP": same counting claim, informally stated.
- [same-math] $H_N$ in (5.4) ↔ conditional entropy / entropy rate: next-symbol entropy given the preceding block, averaged over blocks.
- [structural-analogy] Guessing the next letter (Shannon's experiment) ↔ next-token prediction by language models: both measure how predictable text is, in bits per symbol.

## Questions this raises
- Pierce defers the "real and true reason" for the entropy formula. What is it, and is the logarithm the only function that works (p. 81)?
- Why must the converse of the noiseless theorem hold, i.e. why can no code beat $H$ digits per symbol (p. 98)?
- If block statistics of English cannot be measured, what better description of English could be used (pp. 103–104)?
- How does grammar constrain the next word, and does it fit a finite-state model (pp. 103–104)?

## Reading notes
- **Edition:** the metadata names the 1980 Dover edition, but the scan appears to be the 1961 Harper & Brothers edition titled *Symbols, Signals and Noise* (running headers). The metadata warning is truncated.
- **Page offset:** printed = pdf − 16 (pdf 94 = p. 78).
- **Missing content:** Tables X, XI and XII are not in the text layer. The Huffman probabilities come from Fig. V-3, and code strings are not reproduced. The curves of Figs. V-1, V-2 and V-4 are not in the text layer; they are described only as the surrounding text describes them (V-4 from p. 103). On p. 92 the formulas for the next-symbol probability and the per-block source entropy are garbled in the text layer; they are reconstructed from context and from the legible equation on p. 93.
- **Misprints and checks:** p. 87 says "Equation 5.1 must be a little in error"; context shows 5.2 is meant. On p. 99 the information rate of a repetitive pattern is blank in the scan. Recomputing the entropy from the Fig. V-3 probabilities as read gives about 2.25 bits per word, not the printed 2.21. The printed "0.05 extra digits" (2.26 − 2.21) would then be about 0.01. The probabilities sum to 1.00, and the Huffman average of 2.26 checks out for tree depths 1, 3, 3, 3, 5, 5, 5, 5.
- **Voice:** all views are the author's, except Shannon's quoted theorem, the objection a mathematician would raise (p. 91), and the linguists' view (p. 103).
