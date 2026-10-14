---
id: mackay-2003-information/ch06-stream
work: mackay-2003-information
unit: "6 Stream Codes"
pages: 109-131
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Stream Codes

## L0 — One line
Arithmetic coding, a stream code, can compress a long string to within about two bits of its ideal length by pairing a predictive probability model with an interval-based coder (arithmetic coding), while Lempel–Ziv coding uses no explicit model and, for many real sources, reaches the entropy only in the limit of enormous data.

## L1 — The gist (≤ 120 words)
How can we compress a stream of symbols below one bit per symbol, without chopping it into blocks? The chapter gives two answers. Arithmetic coding separates a probabilistic model, which predicts each next symbol, from a coder that maps the whole string to a sub-interval of [0,1) whose width equals the string's probability; the message length is within two bits of the ideal. Lempel–Ziv coding uses no explicit model: it replaces repeated substrings by pointers, and for many real sources compresses to the entropy only in the limit of very long data. The chapter compares them on real files and ends with exercises, including a first look at the Gaussian "thin shell".

**Prerequisites:** entropy and Shannon information content; Huffman and symbol codes (Ch. 5); conditional probability; Laplace's rule from Ch. 2–3; binary fractions such as 0.01 = 1/4.

## L2 — Key ideas
- In arithmetic coding, compression rests on prediction. In the guessing game, a good predictor turns text into mostly small numbers (1, 2), so the new string should be easy to compress. A probabilistic model plays the same role in arithmetic coding (pp. 110–111).
- An arithmetic code divides [0,1) into intervals whose lengths equal string probabilities. It sends a binary string whose own interval lies inside the source string's interval (pp. 112–113).
- Message length is always within two bits of $\log_2 1/P(\mathbf x\mid\mathcal H)$, so arithmetic coding is very nearly optimal. Model and coder are separate, so any adaptive model can be used (pp. 115, 127–128).
- A simple adaptive Bayesian model (uniform prior on $p_{\mathtt a}$, constant stop probability) gives Laplace's rule (add one to each symbol count) for the next-symbol probability. Inverting an arithmetic coder gives efficient random sampling and Dasher, a text-entry system driven by pointing gestures (pp. 116–119).
- Lempel–Ziv replaces substrings by (pointer, bit) pairs into a dictionary built on the fly. It is "universal" for ergodic sources (roughly, those that are memoryless on long timescales), but only asymptotically, and the timescale may be unfeasibly long (pp. 119–120).
- In the experiments, gzip beats the Laplace model and compress on a text file (bzip, bzip2 and ppmz do better), but is worst on a sparse 0/1 file. ppmz, an arithmetic-coding method, is best on both (pp. 121–122).
- Low-entropy sources with long-range correlations, such as row-by-row images, are not well compressed by Lempel–Ziv. MacKay says we might anticipate that the best compressors will result from artificial-intelligence methods (pp. 128–130).
- In high dimensions, a Gaussian's probability mass sits in a thin shell of radius $\sqrt N\sigma$, far from the density peak at the origin (pp. 130–131).

## L3 — Walkthrough

### Introduction (p. 110)
Two schemes are presented. **Arithmetic coding** goes with the philosophy that compressing a source requires probabilistically modelling it. **Lempel–Ziv** coding is "universal": one algorithm meant to do a reasonable job for any source. MacKay says its universal properties, for many real sources, hold only in the limit of unfeasibly large data, but it is widely used and often effective (p. 110). As of 1999 the best text compressors and several image compressors use arithmetic coding (p. 110).

### 6.1 The guessing game (pp. 110–111)
- English text has redundancy at several levels: unequal character frequencies, likely letter pairs, and words predictable from context and meaning (p. 110).
- **Game:** over the alphabet of 26 capitals plus a space, a human guesses the next character repeatedly. The only feedback is right or wrong. We record the number of guesses needed for each character. For "THERE-IS-NO-REVERSE-ON-A-MOTORCYCLE-" most characters took 1 guess; some took more, e.g. 5, 15, 17 (p. 110).
- The human acts as a time-varying map from the 27 characters onto the numbers 1–27. The number of symbols is unchanged, but 1 and 2 are used far more often, so the new string should be easy to compress (p. 111).
- **Decoding:** an identical twin of the subject plays the game with us. We stop him when he has made the given number of guesses; his last guess is the character (p. 111).
- **Without a human:** choose a window length $L$ and tabulate, for each of the $27^L$ contexts, the predictions and fallback guesses ($26\times 27^L$ questions). Two copies of the table replace the twins. Such a language model is an **$L$th-order Markov model**: the prediction depends only on the previous $L$ characters (p. 111).
- This is unrealistic in practice but illustrates the principles used next (p. 111).

### 6.2 Arithmetic codes (pp. 111–118)
**Motivation.** Arithmetic codes (invented by Elias, Rissanen and Pasco; made practical by Witten et al., 1987) fix the two problems of Huffman codes noted in section 5.6. Modelling is cleanly separated from encoding (p. 111).

**Set-up.**
- The human predictor is replaced by a model that gives a predictive distribution over the next symbol: positive numbers $\{p_i\}$ summing to one. For i.i.d. (independent, identically distributed) symbols it is the same each time, but adaptive context-dependent models work equally easily (p. 111).
- Source alphabet $\mathcal A_X=\{a_1,\dots,a_I\}$, where $a_I$ means "end of transmission". The source need not be i.i.d. Encoder and decoder run identical programs giving $P(x_n=a_i\mid x_1,\dots,x_{n-1})$ (pp. 111–112).

**Intervals.**
- A binary string is read as a binary fraction and defines an interval in $[0,1)$. Notation: $[0.01,0.10)$ includes $0.01000\ldots$ but not $0.10000\ldots$. The string `01` is $[0.01,0.10)=[0.25,0.50)$ in base ten (p. 112).
- A longer string such as `01101` gives the smaller interval $[0.01101,0.01110)$, a sub-interval of that of its prefix `01` (p. 112).
- The model also divides $[0,1)$ into $I$ intervals with lengths $P(x_1=a_i)$. Each is subdivided in proportion to $P(x_2=a_j\mid x_1=a_i)$, so that the length of $a_ia_j$ is the joint probability
$$P(x_1=a_i,x_2=a_j)=P(x_1=a_i)\,P(x_2=a_j\mid x_1=a_i).\tag{6.1}$$
- Iterating, each finite string $x_1\dots x_N$ gets an interval whose length is its probability under the model (p. 112).

**Formulae.** Lower and upper cumulative probabilities:
$$Q_n(a_i\mid x_1,\dots,x_{n-1})\equiv\sum_{i'=1}^{i-1}P(x_n=a_{i'}\mid x_1,\dots,x_{n-1}),\tag{6.2}$$
$$R_n(a_i\mid x_1,\dots,x_{n-1})\equiv\sum_{i'=1}^{i}P(x_n=a_{i'}\mid x_1,\dots,x_{n-1}).\tag{6.3}$$
For the first symbol: $a_1\leftrightarrow[0,P(x_1=a_1))$ (6.4); $a_2\leftrightarrow[P(x=a_1),P(x=a_1)+P(x=a_2))$ (6.5); $a_I\leftrightarrow[P(x_1=a_1)+\dots+P(x_1=a_{I-1}),1.0)$ (6.6) (p. 113).

**Algorithm 6.3** (p. 113): start with $u:=0.0$, $v:=1.0$, $p:=v-u$. For $n=1$ to $N$: compute $Q_n,R_n$; set $v:=u+pR_n(x_n\mid x_1,\dots,x_{n-1})$; $u:=u+pQ_n(x_n\mid x_1,\dots,x_{n-1})$; $p:=v-u$. The result is the interval $[u,v)$ for the string. To encode, send a binary string whose interval lies within $[u,v)$. This can be done on the fly (p. 113).

> **Intuition note.** Each symbol zooms into a sub-interval, shrinking it by that symbol's probability. After the whole string, the interval's width equals the string's probability. Likely strings leave wide intervals, and wide intervals need few bits to name.

**Worked example: bent coin (pp. 113–115).**
- Outcomes `a`, `b`, and an end-of-file symbol □. The model is told nothing about which of a or b is more probable. Source string: `bbba□` (p. 113).
- Predictive probabilities (p. 114):

| Context | P(a) | P(b) | P(□) |
|---|---|---|---|
| (none) | 0.425 | 0.425 | 0.15 |
| b | 0.28 | 0.57 | 0.15 |
| bb | 0.21 | 0.64 | 0.15 |
| bbb | 0.17 | 0.68 | 0.15 |
| bbba | 0.28 | 0.57 | 0.15 |

- Interval `b` is the middle 0.425 of $[0,1)$; `bb` is the middle 0.567 of `b` (p. 114).
- **Encoding.** After the first `b`, the string starts `01`, `10` or `11`, so nothing is written. After the second `b`, interval `bb` lies wholly in `1`, so write `1`. The third `b` does not yet fit inside `10`. After `a`, interval `bbba` lies inside `1001`, so append `001`. When □ arrives, interval `bbba□` wholly contains `100111101`, so append `11101` (p. 114).
- **Termination overhead** (Exercise 6.1): MacKay states that the overhead to terminate is never more than 2 bits over the ideal length $h(\mathbf x\mid\mathcal H)=\log[1/P(\mathbf x\mid\mathcal H)]$. The message length is always within two bits of the Shannon information content of the whole string, so the expected length is within two bits of the entropy of the whole message (p. 115).
- **Decoding.** The decoder runs the identical model. After bits `10` it knows the first symbol is `b`, because `10` lies wholly within `b`. It then computes the intervals for `ba`, `bb`, `b2`, and so on. The second `b` is known after `1001`, the third after `100111`. □ marks the end (p. 115).

**Multiple files.** After □, the decoder is reset, so nothing learnt on the first file transfers to the second. To share a model across files, define a second end-of-file character that tells both ends to keep the model (p. 115).

**The big picture** (p. 115).
- To send $N$ letters, encoder and decoder compute only $N|\mathcal A|$ conditional probabilities, just as in the guessing game. A Huffman code with large block size must evaluate the probabilities of all possible blocks.
- Arithmetic coding works with any source and encoded alphabet, whose sizes may change with time, and with distributions that change from context to context. If the encoded symbols (0, 1) should be used with unequal frequency, subdivide the right-hand interval in proportion.

**How the model might predict** (pp. 115–118).
- Figure 6.4 used a model with $P(\square)=0.15$ always. The other 0.85 is split between a and b by **Laplace's rule**
$$P_{\mathrm L}(\mathtt a\mid x_1,\dots,x_{n-1})=\frac{F_{\mathtt a}+1}{F_{\mathtt a}+F_{\mathtt b}+2},\tag{6.7}$$
where $F_{\mathtt a}$, $F_{\mathtt b}$ count a's and b's so far. For example, after `b`: $\tfrac13\times0.85\approx0.28$ for a and $\tfrac23\times0.85\approx0.57$ for b (p. 116).
- Figure 6.5 shows that strings with many a's or many b's get larger intervals than 50:50 strings of the same length, so they need fewer bits (p. 116).

**Details of the Bayesian model** (p. 117). Parameters $p_\square,p_{\mathtt a},p_{\mathtt b}$ are not the same as predictive probabilities in a context. The string `baaba□` means $l=5$ tosses. Assumptions:
1. The string length is exponentially distributed, i.e. there is a constant probability $p_\square$ of stopping at each character:
$$P(l)=(1-p_\square)^l\,p_\square.\tag{6.8}$$
2. Non-terminal characters are chosen independently with probabilities $\{p_{\mathtt a},p_{\mathtt b}\}$, with $p_{\mathtt a}$ fixed but unknown. Given $p_{\mathtt a}$, the next symbol is a with probability $(1-p_\square)p_{\mathtt a}$. An unterminated string of length $F$ with counts $\{F_{\mathtt a},F_{\mathtt b}\}$ has the Bernoulli probability
$$P(\mathbf s\mid p_{\mathtt a},F)=p_{\mathtt a}^{F_{\mathtt a}}(1-p_{\mathtt a})^{F_{\mathtt b}}.\tag{6.9}$$
3. Uniform prior:
$$P(p_{\mathtt a})=1,\quad p_{\mathtt a}\in[0,1],\tag{6.10}$$
with $p_{\mathtt b}\equiv 1-p_{\mathtt a}$. Other priors are easy; beta distributions are most convenient.

The predictive distribution under this model (studied in section 3.2, eq. 3.16) is precisely Laplace's rule (6.7) (p. 117).

> **Intuition note.** The code needs only a rule for "what comes next?". A simple Bayesian story (unknown bias, uniform prior) supplies one automatically and adapts as counts accumulate. The coder is indifferent to how the probabilities were produced.

**Exercise 6.2 setup** (pp. 117–118). Compare expected message length for an ASCII file under: Huffman-with-header (transmit codeword lengths, then the file); an arithmetic code with the Laplace model $P_{\mathrm L}(\mathtt a\mid\cdot)=(F_{\mathtt a}+1)/\sum_{\mathtt a'}(F_{\mathtt a'}+1)$ (6.11); and a Dirichlet model
$$P_{\mathrm D}(\mathtt a\mid\cdot)=\frac{F_{\mathtt a}+\alpha}{\sum_{\mathtt a'}(F_{\mathtt a'}+\alpha)},\tag{6.12}$$
with $\alpha$ fixed at a number such as 0.01. A small $\alpha$ is a more responsive Laplace model, expecting a more nonuniform distribution; $\alpha=1$ gives Laplace. The header must be self-delimiting. Consider short files and files with unused characters (p. 118).

### 6.3 Further applications of arithmetic coding (pp. 118–119)
**Efficient random samples.**
- Dividing $[0,1)$ into subintervals of lengths $p_i$ and sticking in a random pin lands in interval $i$ with probability $p_i$. So feeding ordinary random bits into an arithmetic *decoder* for a model generates random strings from the model. An infinite random bit sequence selects a random point of $[0,1)$ (p. 118).
- MacKay says this uses very nearly the smallest possible number of random bits, which matters because random numbers cost money (p. 118).
- Exercise 6.3 compares, for $\{p_0,p_1\}=\{0.99,0.01\}$, a standard generator using a 32-bit integer per symbol against arithmetic coding fed with random bits. For 1000 samples the standard method uses 32 000 bits. Arithmetic coding uses about $H_2(0.01)=0.081$ bits per symbol, about 83 bits for 1000 samples including a roughly two-bit termination overhead. The number of 1s fluctuates, giving a standard deviation of about 21 bits (solution, p. 128).

**Efficient data entry (Dasher).**
- Writing is an inverse of compression: compression maps text to few bits; text entry wants few gestures to produce text (p. 118).
- By inverting an arithmetic coder, one gets a text-entry device driven by continuous pointing (Ward et al., 2000), called Dasher. The user zooms in on the interval for the intended string. A language model controls interval sizes so probable strings are easy to select (p. 119).
- After an hour, a novice writes about 25 words per minute with one finger, about half normal ten-finger speed. Gaze-driven, hands-free writing at 25 wpm is also possible (p. 119).

### 6.4 Lempel–Ziv coding (pp. 119–121)
**Philosophy.** Lempel–Ziv (used in `compress` and `gzip`) has no separation between modelling and coding, and no opportunity for explicit modelling (p. 119).

**Basic algorithm.**
- Replace a substring by a pointer to an earlier occurrence. Parse the source into an ordered dictionary of substrings not seen before, starting with the empty string $\lambda$. For `1011010100010...` the parse is $\lambda$, `1`, `0`, `11`, `01`, `010`, `00`, `10`, ... (p. 119).
- Each new substring is one bit longer than some earlier dictionary entry. So send a pointer to that earlier entry (its dictionary index) plus the one extra bit. With $s(n)$ substrings enumerated at the $n$th bit, the pointer takes $\lceil\log_2 s(n)\rceil$ bits (p. 119).
- The table on p. 119 gives:

| substring | `1` | `0` | `11` | `01` | `010` | `00` | `10` |
|---|---|---|---|---|---|---|---|
| $s(n)$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| (pointer, bit) | (,1) | (0,0) | (01,1) | (10,1) | (100,0) | (010,0) | (001,0) |

- The first pointer is empty because only $\lambda$ is in the dictionary. The encoded string is `100011101100001000010`, longer than the 13-bit source, because this source has no obvious redundancy (p. 119).
- Exercise 6.4: any uniquely decodeable code from $\{0,1\}^+$ to $\{0,1\}^+$ must make some strings longer if it makes some strings shorter (p. 119).

**Inefficiencies** (p. 120).
- The code is not "complete": it transmits unnecessary bits. Once a dictionary entry has had both its children added, it will not be needed again (except possibly for termination). It can be dropped, or the second child written into the parent's place, shortening later pointers.
- Also, the second time a prefix is used, the next bit is already determined, so it need not be sent.

**Decoding.** An identical twin builds the dictionary as the data are decoded (p. 120). Exercise 6.5 asks to encode `000000000000100000000000`. The printed answer is `010100110010110001100` (solution, p. 128). Exercise 6.6's decoding is `0100001000100010101000001` (p. 128).

**Practicalities and theory** (p. 120).
- Termination is not discussed. Many variants exist with different dictionary management. They are fast, but on English text their performance, though useful, does not match the standards of the arithmetic-coding literature.
- Lempel–Ziv is defined without any probabilistic model. For any **ergodic** source (MacKay's gloss: one memoryless on sufficiently long timescales), it can be proven to compress asymptotically down to the entropy. A proof is cited to Cover and Thomas (1991).
- It achieves this by memorizing substrings. The asymptotic timescale may be unfeasibly long, since the number of typical substrings may be enormous. Its practical value reflects the many files that repeat short sequences.

> **Intuition note.** Lempel–Ziv "learns" a source only by seeing each pattern, so it needs time to learn long patterns. Universality is a statement about infinite data, not about the file in your hand.

**Common ground** (p. 121). In principle one can design adaptive probabilistic models, hence arithmetic codes, that are "universal": they compress any source in some class to within some factor (preferably 1) of its entropy. **MacKay's view:** for practical purposes, such universal models can only be built if the class of sources is severely restricted. A general-purpose compressor that discovers any source's distribution would be a general-purpose artificial intelligence, which does not yet exist (p. 121).

### 6.5 Demonstration (pp. 121–122)
- Tools mentioned: `dasher.tcl` (interactive aid); Radford Neal's arithmetic-coding package, to which the user adds a model module. There is no single general-purpose arithmetic-coding compressor; each source type needs a new model (p. 121).
- Neal's package includes a simple adaptive model like the Bayesian one above. Its counts $\{F_i\}$ are rescaled and rounded so all lie between 1 and 256. Its results are a basic benchmark (p. 121).
- DjVu uses arithmetic coding via the Z-coder (Bottou et al., 1998), an approximate binary arithmetic coder. One trick: the model adapts only occasionally, with the decision pseudo-randomly tied to whether the encoder emitted a bit. JBIG (binary images) uses a context-dependent model with a Laplace-like adaptation rule. PPM (Teahan, 1995) is a leading text method using arithmetic coding (p. 121).
- `gzip` is based on LZ77, `compress` on LZW. **MacKay's experience:** gzip is best of the Lempel–Ziv programs and `compress` is inferior on most files. `bzip` is a block-sorting compressor using the Burrows–Wheeler transform. It has no explicit probabilistic model, works well only for files larger than several thousand characters, and is effective when a character's context predicts it well (p. 121).

**Table 6.6** (p. 122): LaTeX text of this chapter, 20 942 bytes.

| Method | Compress time / s | Compressed size (% of 20 942) | Uncompress time / s |
|---|---|---|---|
| Laplace model | 0.28 | 12 974 (61%) | 0.32 |
| gzip | 0.10 | 8 177 (39%) | 0.01 |
| compress | 0.05 | 10 816 (51%) | 0.05 |
| bzip | – | 7 495 (36%) | – |
| bzip2 | – | 7 640 (36%) | – |
| ppmz | – | 6 800 (32%) | – |

**Table 6.7** (p. 122): $10^6$ characters, each 0 or 1 with probabilities 0.99, 0.01.

| Method | Compress time / s | Compressed size / bytes | Uncompress time / s |
|---|---|---|---|
| Laplace model | 0.45 | 14 143 (1.4%) | 0.57 |
| gzip | 0.22 | 20 646 (2.1%) | 0.04 |
| gzip --best+ | 1.63 | 15 553 (1.6%) | 0.05 |
| compress | 0.13 | 14 785 (1.5%) | 0.03 |
| bzip | 0.30 | 10 903 (1.09%) | 0.17 |
| bzip2 | 0.19 | 11 260 (1.12%) | 0.05 |
| ppmz | 533 | 10 447 (1.04%) | 535 |

An ideal model would give about $10^6H_2(0.01)/8\simeq10\,100$ bytes. The Laplace compressor falls short because it uses only eight-bit precision. ppmz compresses best but takes much more time (p. 122). MacKay notes that gzip "does not always do so well": the text calls it worst on this sparse file (p. 122).

### 6.6 Summary (pp. 122–123)
- **Fixed-length block codes** (Ch. 4): only a tiny fraction of strings get an encoding. They identified entropy as the measure of compressibility but are of little practical use (p. 122).
- **Symbol codes** (Ch. 5): integer codeword lengths set by symbol probabilities. Every string has a uniquely decodeable encoding. If the source matches the assumed distribution, the expected length per character $L$ lies in $[H,H+1)$. A mismatched source adds the relative entropy $D_{\mathrm{KL}}$ to the mean length. For low-entropy sources, at least one bit per symbol is emitted. Compressing below that needs blocks (p. 123).
- **Stream codes:** not constrained to emit at least one bit per source symbol. Arithmetic codes fit "good compression requires data modelling", i.e. an adaptive Bayesian model. Lempel–Ziv codes memorize earlier strings and assume nothing about the source distribution (p. 123).
- Both fail to decode correctly if any compressed bit is altered, so noisy media need error-correcting codes (Part II) (p. 123).

### 6.7–6.8 Exercises (pp. 123–126)
Brief content of the exercises (solutions to 6.8, 6.12, 6.13 and 6.14 are in 6.9 below):
- 6.7: an arithmetic code for bit strings of length $N$ and weight $K$ (here $N=5$, $K=2$). 6.8 asks how many bits are needed to choose $K$ of $N$ objects (p. 123).
- 6.9, 6.17: arithmetic-code length for $f_1=0.01$ ($N=1000$) and for $\{0.1,0.9\}$ ($N=1000$, $H_2(0.1)\simeq0.47$): estimate mean and standard deviation (pp. 124–125).
- 6.10: arithmetic coding to generate random bit strings with density $f$. 6.11–6.12: Lempel–Ziv with pruned dictionary and its incompleteness. 6.13: low-entropy sources that Lempel–Ziv handles badly (p. 124).
- 6.14: a Gaussian in $N$ dimensions (6.13), radius $r=(\sum_n x_n^2)^{1/2}$ (p. 124). 6.15–6.16: optimal symbol codes (p. 125).
- 6.18: symbols of unequal duration. With average duration $L(\mathbf p)=\sum_n p_nl_n$ (6.15) and entropy $H(\mathbf p)=\sum_np_n\log_2\frac1{p_n}$ (6.16), show that, for the rate to be maximized, $p_n$ must have the form $p_n=\frac1Z2^{-\beta l_n}$ (6.17) with $\beta=H(\mathbf p)/L(\mathbf p)$ (6.18), which implies $\log Z=0$ (6.19). For $l_n=n$ seconds (6.20), find $\mathbf p$ and the maximal rate (1 bit per second is the claimed answer), and relate it to the Kraft inequality (pp. 125–126).
- 6.19–6.21: shuffling cards, Bridge bidding, microwave keypads. 6.22: integer codes; prefix codes that satisfy the Kraft equality $\sum_n2^{-l_n}=1$ (pp. 126–127).

### 6.9 Solutions (pp. 127–131)
**Ex. 6.1 (termination).** Worst case: the source string's interval lies just inside a binary interval; two binary intervals can be chosen, each no smaller than $P(\mathbf x\mid\mathcal H)/4$. So the length is no more than $\log_21/P(\mathbf x\mid\mathcal H)+\log_24$, i.e. two bits over ideal (p. 128).

**Ex. 6.8 (choose $K$ of $N$).** It needs $\lceil\log_2\binom NK\rceil\simeq NH_2(K/N)$ bits. Arithmetic coding does it: treat the selection as a length-$N$ binary string. Initially $P(1)=K/N$. After $n$ emitted bits containing $k$ ones, $P(1)=(K-k)/(N-n)$ and $P(0)=1-(K-k)/(N-n)$ (p. 128).

**Ex. 6.12.** After five prefixes, the pointer can be `000`–`100` but not `101`, `110`, `111`, so some binary strings are not encodings (p. 128).

**Ex. 6.13: low-entropy sources that Lempel–Ziv compresses poorly** (pp. 128–130).
- (a) Long-range correlations with intervening random junk. Example: a phone book with lines like `285-3820:572-5892□`, 18 characters per line from a 13-character alphabet. The true information per line is about 14 bans (a ban is the information in a random integer 0–9). Lempel–Ziv must see all `:ddd` strings to learn that `-` follows, so near-optimal compression comes only after thousands of lines (p. 129).
- (b) Images scanned row by row, with vertically adjacent pixels a distance $w$ apart in the stream. For a fax-like image where each line differs from the line above in a fraction $f$ of bits, the true entropy is only $H_2(f)$ per pixel. MacKay says Lempel–Ziv reaches this only once all strings of length $2^w=2^{400}$ have occurred and their successors have been memorized (as printed; see Reading notes), but there are only about $2^{300}$ particles in the universe, so he is confident that Lempel–Ziv codes will never capture the redundancy of such an image (Fig. 6.11, width 400, $f=5\%$). Random horizontal and vertical pins (Fig. 6.12) have correlations in both directions. MacKay anticipates that the best compressors will come from artificial-intelligence methods (p. 129).
- (c) Computer-generated files, e.g. a LaTeX file followed by its PostScript: the pair's information is roughly that of the LaTeX file. (d) Mandelbrot set picture: information is the range, pixel size and colouring rule. (e) A ground state of a frustrated antiferromagnetic Ising model (Fig. 6.13), with correlations in two directions (p. 130).
- (f) A cellular automaton, 400 cells, 100 steps, each cell updated from five preceding cells by a randomly chosen rule. Its information is about 400 bits (boundary) plus 32 bits (rule), independent of the image height. Lempel–Ziv achieves that only after a periodic limit cycle, which could take about $2^{100}$ iterations. JBIG, modelling a pixel from local context with arithmetic coding, would do well (p. 130).

**Ex. 6.14: Gaussian shell** (pp. 130–131).
- For a one-dimensional Gaussian $E[x^2]=\sigma^2$, and components are independent, so
$$E[r^2]=N\sigma^2.\tag{6.25}$$
- $\operatorname{var}(r^2)$ is $N$ times $\operatorname{var}(x^2)$:
$$\operatorname{var}(x^2)=\int dx\,\frac1{(2\pi\sigma^2)^{1/2}}x^4\exp\!\Big(-\frac{x^2}{2\sigma^2}\Big)-\sigma^4.\tag{6.26}$$
The integral is $3\sigma^4$ (6.14), so $\operatorname{var}(x^2)=2\sigma^4$ and $\operatorname{var}(r^2)=2N\sigma^4$.
- For large $N$, the central-limit theorem says $r^2$ is approximately Gaussian with mean $N\sigma^2$ and standard deviation $\sqrt{2N}\sigma^2$. So $r$ is concentrated near $\sqrt N\sigma$.
- Thickness: for small $\delta r/r$, $\delta\log r=\delta r/r=\tfrac12\delta\log r^2=\tfrac12\delta(r^2)/r^2$. With $\delta(r^2)=\sqrt{2N}\sigma^2$ and $r=\sqrt N\sigma$: $\delta r=\tfrac12 r\,\delta(r^2)/r^2=\sigma/\sqrt2$.
- Density at a shell point, $r=\sqrt N\sigma$, and at the origin:
$$P(\mathbf x_{\text{shell}})=\frac1{(2\pi\sigma^2)^{N/2}}\exp\!\Big(-\frac{N\sigma^2}{2\sigma^2}\Big)=\frac1{(2\pi\sigma^2)^{N/2}}e^{-N/2},\tag{6.27}$$
$$P(\mathbf x=0)=\frac1{(2\pi\sigma^2)^{N/2}}.\tag{6.28}$$
- So $P(\mathbf x_{\text{shell}})/P(\mathbf x=0)=e^{-N/2}$. For $N=1000$ the density at the origin is $e^{500}$ times greater (p. 131).

> **Intuition note.** In many dimensions, each coordinate contributes a little to $r^2$ and these add up to a very predictable total. So almost all draws have nearly the same radius, though that region has lower density than the origin. "Where the density is highest" and "where the mass is" differ.

## Toy example (ours, not from the text)
Model: i.i.d. symbols with $P(\mathtt a)=0.5$, $P(\mathtt b)=0.25$, $P(\square)=0.25$. Then $[Q,R)$ is $\mathtt a:[0,0.5)$, $\mathtt b:[0.5,0.75)$, $\square:[0.75,1)$. Encode `ab□` with Algorithm 6.3, starting with $u=0$, $v=1$, $p=1$:
- $n=1$, `a` ($Q=0$, $R=0.5$): $v=0+1\cdot0.5=0.5$; $u=0+1\cdot0=0$; $p=0.5$.
- $n=2$, `b` ($Q=0.5$, $R=0.75$): $v=0+0.5\cdot0.75=0.375$; $u=0+0.5\cdot0.5=0.25$; $p=0.125$.
- $n=3$, `□` ($Q=0.75$, $R=1$): $v=0.25+0.125\cdot1=0.375$; $u=0.25+0.125\cdot0.75=0.34375$; $p=0.03125$.

The interval is $[0.34375,0.375)$, of width $0.5\times0.25\times0.25=0.03125=P(\mathtt{ab}\square)$. Ideal length $=\log_2(1/0.03125)=5$ bits. In binary, $0.34375=11/32=0.01011$ and $0.375=0.011$. The string `01011` has interval $[11/32,12/32)=[0.34375,0.375)$, which fits exactly, so 5 bits suffice here (within the two-bit bound).

Decode `01011` (value 0.34375): it lies in $[0,0.5)$, so `a`. Rescale: $0.34375/0.5=0.6875\in[0.5,0.75)$, so `b`. Rescale: $(0.6875-0.5)/0.25=0.75\in[0.75,1)$, so `□` and stop.

## Concepts
- [[huffman-arithmetic-coding]] — here, arithmetic coding: a string is identified with a sub-interval of [0,1) of width equal to its model probability (p. 112)
- [[stream-code]] (new) — a code not forced to emit at least one bit per source symbol; arithmetic and Lempel–Ziv codes (p. 123)
- [[self-information-surprisal]] — $h(\mathbf x\mid\mathcal H)=\log 1/P(\mathbf x\mid\mathcal H)$, the ideal message length, which arithmetic coding matches within 2 bits (p. 115)
- [[redundancy]] — English has redundancy in character frequencies, letter pairs and word predictability (p. 110)
- [[universal-coding]] — a single scheme that works for any source; Lempel–Ziv achieves the entropy asymptotically for ergodic sources, with a possibly unfeasible timescale (p. 120)
- [[lempel-ziv-coding]] (new) — replace a new substring by a (pointer to earlier prefix, extra bit) pair in a dictionary built on the fly (p. 119)
- [[laplace-rule]] (new) — $P(\mathtt a)=(F_{\mathtt a}+1)/(F_{\mathtt a}+F_{\mathtt b}+2)$, the predictive probability from a uniform prior over the bias (p. 116)
- [[posterior-predictive-distribution]] — the next-symbol distribution used by the coder is the Bayesian predictive distribution given the string so far (p. 117)
- [[conjugate-prior]] — the Dirichlet model (6.12) with parameter $\alpha$ generalises Laplace's rule; $\alpha=1$ recovers it (p. 118)
- [[prefix-code-kraft]] — Exercise 6.18 and 6.22 link codelengths to the Kraft inequality/equality (pp. 126–127)
- [[kl-divergence]] — mismatch between source and a symbol code's implicit distribution adds $D_{\mathrm{KL}}$ to the expected length (p. 123)
- [[typical-set-aep]] — a Gaussian's mass lies in a thin shell of radius $\sqrt N\sigma$, not at the density peak (pp. 125, 131)

## Canonical instances
- [[guessing-game]] (new) — a human predicting English text characters shows redundancy and motivates model-based compression (p. 110)
- [[bent-coin-arithmetic-code]] (new) — encoding `bbba□` as `100111101` with a Laplace-based model (pp. 113–115)
- [[dasher]] (new) — inverted arithmetic coder as a text-entry system, about 25 words per minute (p. 119)
- [[sparse-file-benchmark]] (new) — $10^6$ characters at 99%/1%, where gzip is worst and ppmz best (p. 122)
- [[gaussian-thin-shell]] (new) — in $N$ dimensions, shell radius $\sqrt N\sigma$ and thickness $\sigma/\sqrt2$ (p. 131)
- [[telephone-book-example]] (new) — long-range correlation with random junk that defeats Lempel–Ziv (p. 129)

## Bridges (candidates)
- [same-math] Arithmetic decoding as sampling ↔ simulation/statistics: inverse-CDF sampling from a cumulative-probability partition of [0,1) — random point plus cumulative intervals $[Q,R)$ yields a sample (p. 118).
- [same-math] Laplace rule in the coder ↔ bayesian: posterior predictive of a Beta–Bernoulli model with a uniform prior — MacKay derives it from the uniform prior (p. 117).
- [structural-analogy] Gaussian thin shell ↔ bayesian: typical set in high-dimensional posteriors — similar concentration of mass away from the mode, though the text treats only the Gaussian (p. 131).
- [structural-analogy] Guessing game and predictive model ↔ language modelling: next-token prediction whose cross-entropy sets the code length (p. 110).
- [structural-analogy] Universal compressor requiring severely restricted source classes ↔ bayesian: no free lunch for priors over sources (p. 121).

## Questions this raises
- How does the 2-bit termination overhead compare with per-symbol Huffman overhead as the string grows?
- How should the model learn from earlier files, e.g. with a second end-of-file symbol that keeps the model (p. 115)?
- Can a model with a richer context (e.g. PPM, JBIG) approach the entropy of images with long-range structure, where Lempel–Ziv cannot (pp. 121, 130)?
- What does the thin-shell result imply for sampling or searching in high dimensions?

## Exercises worth doing
- Ex. 6.2 (p. 117) — compare Huffman-with-header, Laplace and Dirichlet ($\alpha=0.01$) arithmetic codes on short and large files — difficulty: medium
- Ex. 6.4 (p. 119) — no uniquely decodeable code can shorten some strings without lengthening others — difficulty: easy
- Ex. 6.10 (p. 124) — design an arithmetic-coding sampler for bit strings of density $f$ — difficulty: easy
- Ex. 6.18 (p. 125) — optimal use of symbols with different durations; link to the Kraft inequality — difficulty: hard
- Ex. 6.22 (p. 127) — uniquely decodeable, prefix codes for the positive integers — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 121 = printed 109). Running text uses printed numbers.
- Table 6.6 shows blank cells for bzip, bzip2 and ppmz times (image p. 122); I left them as "–". The text layer was fine.
- Solution to Ex. 6.13(b) (p. 129) says Lempel–Ziv needs "all strings of length $2^w=2^{400}$". This is as printed. It reads like a slip for "$2^w$ strings of length $w$", but the page gives only this wording.
- The probability table on p. 114 shows 0.57 for $P(\mathtt b\mid\mathtt b)$, while the text says interval `bb` is the middle 0.567 of `b`; the table is rounded.
- The pointer table (p. 119) is printed with $s(n)$ and its binary form in separate rows. I read pointer values as dictionary indices of the prefix, which is consistent with the printed pairs.
- The sentence in the book's Section 6.5 about "ideal model... falls short because eight-bit precision" is MacKay's explanation; nothing else is given.
- Sources and tools cited (Cover and Thomas, DjVu, Neal's package) are only named here; their content is not in these pages.
