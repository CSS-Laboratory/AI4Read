---
id: mackay-2003-information/ch14-very
work: mackay-2003-information
unit: "14 Very Good Linear Codes Exist"
pages: 228–232
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
# Very Good Linear Codes Exist

## L0 — One line
Averaging over random parity-check matrices, one union-bound calculation over the typical set of noise vectors shows that, for the binary symmetric channel, linear codes exist at every rate below $1-H(X)$ (with $H(X)$ the noise entropy per bit), and that, for binary sources, linear compression works at every rate above $H(X)$.

## L1 — The gist (≤ 120 words)
The question: can linear codes reach the noisy-channel limit on the binary symmetric channel, and can linear maps compress a binary source down to its entropy? MacKay answers both with one calculation. The receiver computes the syndrome of the received word and looks for a unique typical noise vector with that syndrome. Averaged over all random binary matrices $\mathbf H$, the chance that a given non-zero vector is mapped to zero is $2^{-M}$. The average clash error is therefore at most about $2^{NH(X)}2^{-M}$. This vanishes when $H(X)<M/N$. Read as channel coding, this gives rates $R<1-H(X)$. Read as compression, it gives rates $M/N>H(X)$. Almost all linear codes are shown to be "very good".

**Prerequisites:** a binary parity-check matrix $\mathbf H$ (codewords $\mathbf t$ satisfy $\mathbf{Ht}=\mathbf 0 \bmod 2$) and the syndrome $\mathbf z=\mathbf{Hr} \bmod 2$ of a received word $\mathbf r$; mod-2 arithmetic and matrix–vector products; typical sets (Ch. 4); binary entropy $H_2$; the random-linear-code fact $P(\mathbf{Hv}=\mathbf 0)=2^{-M}$ (Ch. 13); union bound.

## L2 — Key ideas
- One calculation proves both the noisy-channel coding theorem (binary symmetric channel) and the source coding theorem (binary sources) (p. 229).
- Decoding is reduced to finding the noise $\mathbf x$ from the syndrome $\mathbf z=\mathbf{Hx}$, which does not depend on the codeword (p. 229).
- A sub-optimal typical-set decoder is analysed because it is easier. Its error splits into "true noise not typical" and "a clashing typical vector" (p. 230).
- The clash probability is bounded by a union bound, then averaged over all $\mathbf H$ using $P(\mathbf{Hv}=\mathbf 0)=2^{-M}$ for non-zero $\mathbf v$ (pp. 230–231).
- The average clash (type-II) error is at most about $2^{NH(X)-M}$, since the typical set has roughly $2^{NH(X)}$ members (p. 231). It vanishes if $H(X)<M/N$, so good linear codes exist for $R<1-H(X)$ (p. 231).
- The same inequality gives linear hash compression $\mathbf x\mapsto\mathbf{Hx}$ at any rate above $H(X)$ (p. 231).
- The source result needs only a definable typical set, so it covers sources with memory or varying in time, provided they are ergodic (p. 231). The channel proof can be reworked for more general channels with symmetric binary inputs (p. 229).
- The method extends to other linear codes, e.g. LDPC codes, given an approximate expected weight enumerator (p. 232).

## L3 — Walkthrough

### Chapter intro (p. 228)
The proof draws on typical sets (Chs. 4, 10) and on the random-linear-code weight enumerator calculation (§13.5). It is more constructive than Chapter 10, which showed that almost any *random* code is very good. Here almost any *linear* code is shown to be very good. On the compression side, random linear hash functions compress compressible binary sources (link to Ch. 12) (p. 228).

### 14.1 Simultaneous proof (pp. 229–231)
**Setup.** The code has binary parity-check matrix $\mathbf H$ with $M$ rows and $N$ columns. Later $N$ and $M$ grow with $M\propto N$. The rate satisfies
$$R\ge 1-\frac MN \tag{14.1}$$
with equality if the rows of $\mathbf H$ are independent. The author assumes equality. He says the gap (M − rank) is negligible, and leaves this to the reader (p. 229).

A codeword $\mathbf t$ satisfies
$$\mathbf{Ht}=\mathbf 0 \bmod 2 \tag{14.2}$$
The binary symmetric channel adds noise $\mathbf x$ (here $\mathbf x$ is the noise, not the channel input):
$$\mathbf r=\mathbf t+\mathbf x \bmod 2 \tag{14.3}$$
The receiver computes the syndrome (a mod-2 check pattern that depends only on the noise):
$$\mathbf z=\mathbf{Hr} \bmod 2=\mathbf{Ht}+\mathbf{Hx} \bmod 2=\mathbf{Hx} \bmod 2 \tag{14.4}$$
Decoding means finding the most probable $\mathbf x$ with
$$\mathbf{Hx}=\mathbf z \bmod 2 \tag{14.5}$$
Subtracting the estimate $\hat{\mathbf x}$ from $\mathbf r$ gives the best guess for $\mathbf t$ (pp. 229–230).

**Claim.** If $R<1-H(X)=1-H_2(f)$, with $f$ the flip probability, then the optimal syndrome decoder has vanishing error probability as $N$ increases, for random $\mathbf H$ (p. 230).

**Typical-set decoder.** The proof studies a sub-optimal decoder that is easier to analyse. Let $T$ be the typical set of noise vectors $\mathbf x'$, those with $\log 1/P(\mathbf x')\simeq NH(X)$. The $\epsilon$s and $\beta$s that make this rigorous are omitted (margin note). The decoder checks whether any typical $\mathbf x'$ satisfies
$$\mathbf{Hx}'=\mathbf z \tag{14.6}$$
If exactly one does, it reports that vector. If none or several do, it reports an error (p. 230).

**Error split.**
$$P_{\mathrm{TS}|\mathbf H}=P^{(I)}+P^{(II)}_{\mathrm{TS}|\mathbf H} \tag{14.7}$$
$P^{(I)}$ is the probability that the true $\mathbf x$ is not typical. It vanishes as $N$ increases (Ch. 4). $P^{(II)}$ is the probability that the true $\mathbf x$ is typical and at least one other typical vector clashes with it, i.e. $\mathbf H(\mathbf x'-\mathbf x)=\mathbf 0$ (p. 230).

**Union bound.** With the truth function $\mathbb 1[\mathbf H(\mathbf x'-\mathbf x)=0]$ (1 if true, 0 if false; 14.8), the number of type-II errors given $\mathbf x$ and $\mathbf H$ is bounded by
$$\sum_{\mathbf x'\in T,\ \mathbf x'\ne\mathbf x}\mathbb 1[\mathbf H(\mathbf x'-\mathbf x)=0] \tag{14.9}$$
The true number is 0 or 1, but the sum may exceed 1 when several typical vectors share a syndrome. Averaging over $\mathbf x$:
$$P^{(II)}_{\mathrm{TS}|\mathbf H}\le\sum_{\mathbf x\in T}P(\mathbf x)\sum_{\mathbf x'\in T,\ \mathbf x'\ne\mathbf x}\mathbb 1[\mathbf H(\mathbf x'-\mathbf x)=0] \tag{14.10}$$
(p. 230).

**Averaging over $\mathbf H$.** Write $\langle\cdots\rangle_{\mathbf H}$ for the average over all binary matrices. The average type-II error is
$$\bar P^{(II)}_{\mathrm{TS}}=\sum_{\mathbf H}P(\mathbf H)P^{(II)}_{\mathrm{TS}|\mathbf H}=\big\langle P^{(II)}_{\mathrm{TS}|\mathbf H}\big\rangle_{\mathbf H} \tag{14.11}$$
Applying (14.10), then moving the average inside the sums:
$$\bar P^{(II)}_{\mathrm{TS}}\le\Big\langle\sum_{\mathbf x\in T}P(\mathbf x)\sum_{\mathbf x'}\mathbb 1[\mathbf H(\mathbf x'-\mathbf x)=0]\Big\rangle_{\mathbf H} \tag{14.12}$$
$$=\sum_{\mathbf x\in T}P(\mathbf x)\sum_{\mathbf x'}\big\langle\mathbb 1[\mathbf H(\mathbf x'-\mathbf x)=0]\big\rangle_{\mathbf H} \tag{14.13}$$
(The page writes (14.12) with "=". Strictly an inequality is needed because of (14.10); this is an added step.) Showing that the *average* vanishes shows that linear codes with vanishing error exist, and the author says almost all linear codes are very good (p. 230).

**Key fact (from §13.5).** For any non-zero binary $\mathbf v$, averaged over $\mathbf H$, $P(\mathbf{Hv}=\mathbf 0)=2^{-M}$. Since $\mathbf x'\ne\mathbf x$, the vector $\mathbf x'-\mathbf x$ is non-zero. Hence
$$\bar P^{(II)}_{\mathrm{TS}}\le\Big(\sum_{\mathbf x\in T}P(\mathbf x)\Big)(|T|-1)\,2^{-M} \tag{14.14}$$
$$\le|T|\,2^{-M} \tag{14.15}$$
(the second step uses $\sum_{\mathbf x\in T}P(\mathbf x)\le1$ and $|T|-1<|T|$; added step. The page prints (14.14) with "="; it is written here with $\le$ because (14.12) is an inequality). The typical set has roughly $2^{NH(X)}$ members (Ch. 4), so
$$\bar P^{(II)}_{\mathrm{TS}}\le2^{NH(X)}2^{-M} \tag{14.16}$$
(p. 231).

**Conclusion.** With $M\propto N$, this bound either vanishes or grows exponentially in $N$. It vanishes if
$$H(X)<M/N \tag{14.17}$$
Substituting $R=1-M/N$: very good linear codes exist for any rate
$$R<1-H(X) \tag{14.18}$$
where $H(X)$ is the entropy of the channel noise per bit (p. 231). The author notes the proof can be reworked for non-binary outputs, time-varying channels and channels with memory, if the inputs are binary with a symmetry property (§10.6) (p. 229).

*Intuition note.* There are about $2^{NH(X)}$ plausible noise patterns but only $2^M$ possible syndromes. A random $\mathbf H$ sends each wrong pattern to the true syndrome with probability $2^{-M}$. So wrong clashes are rare when there are fewer plausible patterns than syndromes.

**Exercise 14.1** asks for the proof redone for a more general channel (p. 231).

### 14.2 Data compression by linear hash codes (p. 231)
The decoding game is also an *uncompression* game. The world produces a binary vector $\mathbf x$ from source $P(\mathbf x)$. It has redundancy if $f\neq0.5$. A linear compressor maps the $N$-bit $\mathbf x$ to the $M$-bit syndrome $\mathbf z$, and the task is to recover $\mathbf x$ from $\mathbf z$. Its rate is
$$R_{\text{compressor}}\equiv M/N \tag{14.19}$$
The author ignores possible linear redundancies in this definition. Because decoding succeeds for almost any $\mathbf H$ when $H(X)<M/N$, the **source coding theorem** follows. For a binary source of entropy $H(X)$ and a required rate $R>H(X)$, there exists a linear compressor $\mathbf x\to\mathbf z=\mathbf{Hx}\bmod 2$ with rate $M/N$ equal to $R$, and an uncompressor, that is virtually lossless. The theorem holds not only for i.i.d. sources but for any source with a definable typical set, such as sources with memory or time-varying sources. All that is required is that the source be ergodic (p. 231).

*Intuition note.* The same inequality serves two jobs. Needing $2^M$ labels for $2^{NH(X)}$ typical patterns is a compression statement. Having enough syndromes to tell the likely noise patterns apart is an error-correction statement.

### Notes (p. 232)
The method applies to other linear codes, such as low-density parity-check codes. For each code one needs an approximation of its expected weight enumerator function (p. 232).

## Toy example (ours)
**Mechanism.** Take $M=1$, $N=2$, so $\mathbf H=(h_1\ h_2)$ and there are 4 matrices: 00, 01, 10, 11. For $\mathbf v=(1,1)$, $\mathbf{Hv}=h_1+h_2\bmod 2=0$ for 00 and 11, so the fraction is $2/4=1/2=2^{-1}$. For $\mathbf v=(1,0)$, $\mathbf{Hv}=h_1=0$ for 00 and 01, again $1/2$.

**Clash count.** Take $N=3$, $M=2$, typical set $T=\{100,010,001\}$, true noise $\mathbf x=100$.
- Clash with $\mathbf x'=010$ needs $\mathbf H(110)=0$, i.e. column 1 = column 2. Columns are 2-bit vectors, so the probability is $1/4$.
- Clash with $001$ needs $\mathbf H(101)=0$, i.e. column 1 = column 3. The probability is $1/4$.
- Expected number of clashes $=(|T|-1)2^{-M}=2/4=0.5$. This is the bound of (14.14).
- Exact $P(\text{at least one clash})=\tfrac14+\tfrac14-P(\text{all columns equal})=\tfrac14+\tfrac14-\tfrac1{16}=\tfrac7{16}=0.4375\le0.5$. The union bound is slightly loose.

**Rate numbers.** For $f=0.1$: $H_2(0.1)=0.1\log_2 10+0.9\log_2(1/0.9)\approx0.332+0.137=0.469$. The theorem then gives good linear codes for $R<1-0.469=0.531$.

## Concepts
- [[noisy-channel-coding-theorem]] — here proved for the binary symmetric channel: good linear codes exist for $R<1-H(X)$ (p. 231)
- [[source-coding-theorem]] — here: a linear compressor exists at any rate $R>H(X)$, virtually lossless (p. 231)
- [[typical-set-aep]] — noise vectors with $\log 1/P\simeq NH(X)$; about $2^{NH(X)}$ of them (p. 230)
- [[entropy-hx]] — here $H(X)=H_2(f)$ is the noise entropy per bit (p. 230)
- [[error-correcting-code]] — linear code defined by parity-check matrix $\mathbf H$, $\mathbf{Ht}=0$ (p. 229)
- [[syndrome-decoding]] (new) — compute $\mathbf z=\mathbf{Hr}$, which depends only on the noise, and solve $\mathbf{Hx}=\mathbf z$ (p. 229)
- [[typical-set-decoder]] (new) — sub-optimal decoder: report the unique typical $\mathbf x'$ matching the syndrome, else error (p. 230)
- [[union-bound]] (new) — error count ≤ sum of clash indicators (14.9) (p. 230)
- [[weight-enumerator-function]] (new) — used via $P(\mathbf{Hv}=0)=2^{-M}$ for random $\mathbf H$ (p. 231)
- [[linear-hash-code]] (new) — compressor $\mathbf x\mapsto\mathbf{Hx}\bmod 2$ with rate $M/N$ (p. 231)

## Canonical instances
- [[binary-symmetric-channel]] (new) — flips each bit with probability $f$; the channel analysed (p. 230)
- [[random-linear-code-ensemble]] (new) — average over all binary $\mathbf H$ shows good codes exist (p. 230)

## Bridges (candidates)
- [structural-analogy] Averaging error over random $\mathbf H$ to prove existence ↔ combinatorics: the probabilistic method — if the average is small, some member is good.
- [structural-analogy] Syndrome-based compression $\mathbf x\to\mathbf{Hx}$ ↔ Chapter 12 hashing (the unit links the two, p. 228): both map long strings to short labels (Chapter 12 itself is not on these pages).
- [structural-analogy] Typical-set decoding ↔ Chapter 10's random-code proof: the unit says both use typical sets (p. 228) and contrasts this linear-code proof with Chapter 10's random-code proof.

## Questions this raises
- The decoder analysed is not practical. How could decoding be made efficient for such codes?
- What exactly do the omitted $\epsilon$ and $\beta$ terms change in the bound (14.16)?
- What replaces $P(\mathbf{Hv}=0)=2^{-M}$ for structured ensembles such as LDPC codes, where only an approximate weight enumerator is available (p. 232)?
- How does the proof change for the more general channels mentioned (Exercise 14.1)?

## Exercises worth doing
- Ex. 14.1 (p. 231) — redo the proof for a more general channel; tests which steps used the binary-symmetric structure — difficulty: medium (book marks it [3])

## Reading notes
- Printed page = pdf − 12 (pdf 240–244 ↔ printed 228–232).
- Page 228 is the "About Chapter 14" preface. The chapter proper starts on p. 229.
- The text layer garbles the indicator-function brackets and the angle brackets in (14.8)–(14.14). I checked them against the page images.
- Eq. (14.12) is printed with "=", but it is an inequality, since it averages (14.10). This is not marked in the source. Eq. (14.14) is also printed with "="; the digest writes it with $\le$.
- The ε/β details of the typical set are deliberately left out by the author (margin note, p. 230).
- The author states the aim of showing that the optimal decoder has vanishing error, and says he proves this by studying the sub-optimal typical-set decoder. The calculation itself bounds only the typical-set decoder, and these pages do not spell out the step between the two (p. 230).
