---
id: stone-2022-information/ch04-noisy
work: stone-2022-information
unit: "4 The Noisy Channel Coding Theorem"
pages: 79-112
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
# The Noisy Channel Coding Theorem

## L0 — One line
Mutual information $I(X,Y)=H(X)+H(Y)-H(X,Y)$ measures how much a noisy channel's output tells us about its input, and Shannon's theorem says reliable communication is possible at rates up to the capacity $C=\max_{p(X)} I(X,Y)$ but not above it.

## L1 — The gist (≤ 120 words)
How much of a noisy channel's output carries information about its input? Stone builds joint and conditional entropy, and shows that mutual information equals input entropy minus the uncertainty left after seeing the output. Worked examples include a 4×4 joint table, a noisy binary image, a parity-check block code and the noisy typewriter. Channel capacity is the largest mutual information over input distributions. Shannon's theorem says that at rates up to capacity the error can be made arbitrarily small, and that, when source entropy exceeds capacity, the uncertainty left about the input is at least the excess. The chapter ends with a sketch of Shannon's random-codebook proof. This is the theory behind reliable transmission over unreliable channels.

**Prerequisites:** entropy as average surprisal in bits; logarithms base 2; expected value; the product rule $p(x,y)=p(y|x)p(x)$; reading 2-D probability tables; conditional entropy $H(Y|X)$ as the uncertainty left in $Y$ after seeing $X$.

## L2 — Key ideas (5–10 bullets)
- Joint entropy $H(X,Y)$ is the average surprisal of an (input, output) pair. Summing a joint table over rows or columns gives the marginal distributions, i.e. the distributions of $X$ alone and $Y$ alone (pp. 84–86).
- If $X$ and $Y$ are independent, $H(X,Y)=H(X)+H(Y)$. Mutual information is the shortfall from this additivity, $I=H(X)+H(Y)-H(X,Y)$ (pp. 87–90).
- Equivalent forms are $I=H(Y)-H(Y|X)=H(X)-H(X|Y)$. For $Y=X+\eta$, $H(Y|X)$ equals the noise entropy $H(\eta)$ (pp. 92–93).
- Noise produces cross-talk: each input can give about $2^{H(Y|X)}$ outputs, and each output can come from about $2^{H(X|Y)}$ inputs (p. 96).
- In the noisy-image example, $I(X,Y)=0.436$ bits per pixel and the transmission efficiency is $I/H(Y)=0.481$ (pp. 98–101).
- Error-correcting codes add redundancy (for example parity digits: extra check digits that keep the number of 1s in each row and column even) to detect and fix errors. The price is more digits sent per message digit (pp. 102–104).
- Channel capacity is $C=\max_{p(X)}I(X,Y)$. Shannon's theorem gives arbitrarily small error up to $C$, and, when the source entropy $H(X)$ exceeds $C$, an equivocation (the remaining uncertainty $H(X|Y)$ about the input) of at least $H(X)-C$ (pp. 104–107).
- The noisy typewriter reaches error-free communication at the capacity rate by using only a subset of inputs whose possible outputs never overlap (pp. 108–110).
- Shannon's proof averages the error over random codebooks (random assignments of outputs to inputs). If the average is small, at least one codebook is at least that good (p. 111).

## L3 — Walkthrough

### 4.1 Introduction (pp. 79–80)
Mutual information $I(X,Y)$ is the average information gained about one variable by observing the other. It is symmetric. Equivalently, it is the average reduction in uncertainty about one variable from knowing the other (p. 79). Residual uncertainty about $Y$ after seeing $X$ is the conditional entropy $H(Y|X)$. When noise $\eta$ is added to the input, this is called the noise entropy, $H(\eta)=H(Y|X)$ (p. 80). The remainder of the chapter concerns discrete variables (p. 80), although the proof sketch in 4.11 speaks of a 'discrete or continuous channel' (p. 111).

**Intuition note.** Entropy says how unsure we are. Mutual information says how much of that unsureness disappears when we look at the other end of the channel.

### 4.2 Joint distributions (pp. 80–88)
**Setup.** A source emits one of four messages $s_1..s_4$ (integers 0–3). The encoding is trivial, so $p(X)=p(S)$. Inputs are 2-bit codewords $A_x=\{00,01,10,11\}$ and outputs have the same form, $A_y$ (pp. 80–82). A sample of 128 (input, output) pairs is counted in a 4×4 grid (Table 4.1). The author treats the sample as exactly representing the channel's statistics (p. 81). Dividing each count by 128 gives the joint probabilities $p(x_i,y_j)$ (Table 4.2). All 16 sum to one (pp. 82–83). The joint distribution $p(X,Y)$ is a matrix with entry $p(x_i,y_j)$ in column $i$, row $j$ (p. 83).

**Joint entropy.**
$$H(X,Y)=\sum_{i=1}^{m_x}\sum_{j=1}^{m_y}p(x_i,y_j)\log\frac{1}{p(x_i,y_j)}\tag{4.10}$$
$$=\mathrm{E}\!\left[\log\frac{1}{p(x,y)}\right]\ \text{bits per pair}\tag{4.11}$$
It is the average Shannon information per pair. Within a fixed range, a uniform joint distribution has maximum entropy (p. 84).

**Marginalisation.** Summing over the other variable gives $p(x_i)=\sum_{j=1}^{m_y}p(x_i,y_j)$ (4.12). The marginals are
- $p(X)=\{0.125,0.375,0.375,0.125\}$ (4.13);
- $p(Y)=\{0.227,0.273,0.273,0.227\}$ (4.14);
- $p(y_j)=\sum_{i=1}^{m_x}p(x_i,y_j)$ (4.15) (pp. 85–86).

**Independence.** If $X$ and $Y$ are statistically independent, then $p(x_i,y_j)=p(x_i)p(y_j)$ (4.16). Over all values, $p(X,Y)=p(X)p(Y)$, read as an outer product (4.17) (p. 86). Then
$$H(X,Y)=\mathrm{E}\!\left[\log\tfrac{1}{p(x,y)}\right]=\mathrm{E}\!\left[\log\tfrac{1}{p(x)p(y)}\right]=\mathrm{E}\!\left[\log\tfrac{1}{p(x)}\right]+\mathrm{E}\!\left[\log\tfrac{1}{p(y)}\right]\tag{4.18–4.20}$$
$$=\sum_i p(x_i)\log\tfrac{1}{p(x_i)}+\sum_j p(y_j)\log\tfrac{1}{p(y_j)}=H(X)+H(Y)\tag{4.21–4.22}$$
So for independent variables $H(X)+H(Y)-H(X,Y)=0$ (4.23) (p. 87).

**Two dice (p. 87–88).** The two dice are independent. All 36 pairs are equally likely, so $H(X,Y)=\log 36=5.17$ bits per pair (4.24). Each die has $H=\log 6=2.59$ bits (4.26–4.27). Hence $H(X,Y)=H(X)+H(Y)=5.17$ (4.28).

**Intuition note.** If knowing one variable tells you nothing about the other, their uncertainties just add. Any shortfall below the sum is evidence of a link between them.

### 4.3 Mutual information (pp. 88–91)
For a channel, the information rate depends on $H(X)$, $H(Y)$ and the relationship between $X$ and $Y$ (p. 88). To communicate as much as possible, input entropy should be high, output entropy should be high, and noise entropy should be low (p. 89). If input and output are mutually independent, then even with high input and high output entropy, all of the output entropy is just output noise (p. 89). High output entropy with low input entropy is pointless, because the output variability has little to do with the input (p. 88). High input entropy with low output entropy means some of the input variability is effectively "input noise" (p. 89).

**Definition.**
$$I(X,Y)=\sum_{i=1}^{m_x}\sum_{j=1}^{m_y}p(x_i,y_j)\log\frac{p(x_i,y_j)}{p(x_i)p(y_j)}\tag{4.29}$$
$$=\mathrm{E}\!\left[\log\frac{p(x,y)}{p(x)p(y)}\right]\ \text{bits}\tag{4.30}$$
**Derivation.**
$$I=\mathrm{E}[\log p(x,y)-\log(p(x)p(y))]\tag{4.31}$$
$$=\mathrm{E}[\log p(x,y)]-\mathrm{E}[\log(p(x)p(y))]\tag{4.32}$$
with $\mathrm{E}[\log(p(x)p(y))]=\mathrm{E}[\log p(x)]+\mathrm{E}[\log p(y)]$ (4.33), so
$$I=\mathrm{E}[\log p(x,y)]-\mathrm{E}[\log p(x)]-\mathrm{E}[\log p(y)]\tag{4.34}$$
$$=\mathrm{E}[\log\tfrac{1}{p(x)}]+\mathrm{E}[\log\tfrac{1}{p(y)}]-\mathrm{E}[\log\tfrac{1}{p(x,y)}]\tag{4.35}$$
$$=H(X)+H(Y)-H(X,Y)\ \text{bits}\tag{4.36}$$
Rearranged: $H(X,Y)=H(X)+H(Y)-I(X,Y)$ (4.37). The joint entropy acts as a "container" for the other quantities (p. 90).

**Worked example (Table 4.2, pp. 90–91).**
- $H(X)=1.81$ bits (4.38–4.40).
- $H(Y)=1.99$ bits (4.41–4.43).
- $H(X,Y)=3.30$ bits (4.44). Zero-probability cells are handled by defining $p\log(1/p)=0$ when $p=0$ (p. 91).
- $H(X)+H(Y)=3.80>H(X,Y)$, so $X$ and $Y$ are not independent (4.45–4.46).
- $I(X,Y)=1.81+1.99-3.30=0.509$ bits (4.47–4.49).
- Only $I/H(Y)=0.509/1.99=0.256$ of the output entropy is information about the input. The rest is channel noise (p. 91).

**Intuition note.** Add the two separate uncertainties and subtract the uncertainty of the pair. What is left is the part that is counted twice, because the variables share it.

### 4.4 Conditional entropy (pp. 91–94)
$H(Y|X)$ is the average uncertainty in $Y$ after $X$ is observed. It is the part of the uncertainty in $Y$ not attributable to $X$ (pp. 91–92). Then
$$I(X,Y)=H(Y)-H(Y|X)\tag{4.50}$$
**Proof (p. 92).** Start from (4.51), which repeats (4.29). With the product rule $p(x,y)=p(y|x)p(x)$:
$$I=\sum_i\sum_j p(x_i,y_j)\log\frac{p(y_j|x_i)}{p(y_j)}\tag{4.52}$$
$$=\sum_i\sum_j p(x_i,y_j)\log\frac{1}{p(y_j)}-\sum_i\sum_j p(x_i,y_j)\log\frac{1}{p(y_j|x_i)}$$
The first term is $H(Y)$ and the second is $H(Y|X)$. (Added step: the first term equals $H(Y)$ because summing $p(x_i,y_j)$ over $i$ gives $p(y_j)$, by (4.15).) By symmetry,
$$I(X,Y)=H(X)-H(X|Y)\tag{4.53}$$

**Conditional entropy and noise (p. 93).** Put $Y=X+\eta$ (4.54) into (4.50): $I=H(Y)-H([X+\eta]|X)$ (4.55).
- Given $X$, $X$ adds no uncertainty, so $I=H(Y)-H(\eta|X)$ (4.56).
- Noise is independent of $X$, so $H(\eta|X)=H(\eta)$ and $I=H(Y)-H(\eta)$ (4.57).
- Comparing with (4.50): $H(Y|X)=H(\eta)$ (4.58).
- For Table 4.2: $H(\eta)=H(Y)-I=1.99-0.509=1.481$ bits (4.59–4.60).

**Intuition note.** What remains uncertain about the output once you know the input is exactly the randomness the channel adds.

**Schematic representations (pp. 94–95).** Venn diagrams (Fig. 4.4) show $H(X,Y)=I+H(X|Y)+H(Y|X)$. In (a) the overlap is smaller, so the channel is noisier. The author notes that MacKay showed areas in Venn diagrams can become negative in some circumstances. The stacked-box form (Fig. 4.5) avoids this. Fig. 4.6 gives a geometric form (p. 95).

### 4.5 Noise and cross-talk (pp. 95–97)
Chapter 2 read entropy as a count of equally probable values, and Shannon used this reading for the conditional entropies. In his proofs he showed that the inputs (encoded messages) are all equally probable, provided they are sufficiently long (p. 95). Cross-talk means one input may give many outputs and one output may come from many inputs (fan diagram, Fig. 4.7). The number of possible outputs per input and of inputs per output are
$$m_{y|x}=2^{H(\eta)}=2^{H(Y|X)}\tag{4.61}$$
$$m_{x|y}=2^{H(X|Y)}\tag{4.62}$$
(p. 96). In Fig. 4.8 the mutual information is the same disc in both panels. It is a larger proportion of the input entropy than of the output entropy, so, by this reasoning, noise is a larger share of the output than of the input (p. 97). The printed sentence states the opposite (see Reading notes).

**Intuition note.** An entropy of $h$ bits behaves like $2^h$ equally likely options. So $H(Y|X)$ counts how many outputs a single input might fan out to.

### 4.6 Noisy pictures and coding efficiency (pp. 98–101)
**Setup.** The input is a binary image. The output is the same image after a binary symmetric channel, in which each pixel flips with probability 10% (p. 98). Pixels are treated as independent, so these entropies are upper bounds for images with these pixel proportions (pp. 98–99). Table 4.3 gives the joint pixel probabilities: 0.651, 0.073, 0.028 and 0.249 (p. 99).
- $H(X)=0.724\log\frac{1}{0.724}+0.276\log\frac{1}{0.276}=0.851$ bits/pixel (4.63–4.65).
- $H(Y)=0.679\log\frac{1}{0.679}+0.322\log\frac{1}{0.322}=0.906$ bits/pixel (4.66–4.68).
- $H(X,Y)=0.651\log\frac{1}{0.651}+0.073\log\frac{1}{0.073}+0.028\log\frac{1}{0.028}+0.249\log\frac{1}{0.249}=1.32$ bits (4.69–4.72).
- $I=0.851+0.906-1.321=0.436$ bits (4.73–4.75).
- $H(X|Y)=H(X)-I=0.851-0.436=0.415$ bits (4.76–4.78).
- $H(Y|X)=H(Y)-I=0.906-0.436=0.470$ bits (4.79–4.81) (p. 100).

**Check against the known noise.** With flip probability $p=0.1$,
$$H(\eta)=p\log\tfrac1p+(1-p)\log\tfrac{1}{1-p}=0.332+0.137=0.469\ \text{bits}\tag{4.82–4.85}$$
The 0.470 versus 0.469 gap arises because 0.470 is estimated from sampled data and 0.469 comes from the known flip probability (p. 101).

**Transmission efficiency** is defined here as $I(X,Y)/H(Y)=0.436/0.906=0.481$ (4.86). Almost half of the output entropy depends on the input, and the rest is channel noise (p. 101).

### 4.7 Error-correcting codes (pp. 101–104)
Removing redundancy suits noiseless channels (source coding). For noisy channels, redundancy is added so errors can be detected and/or corrected (pp. 101–102).

**Block code (Pierce's example).** The message $\mathbf s=[1\,1\,0\,1\,0\,0\,1\,1\,0\,1\,0\,1\,1\,0\,0\,0]$ (4.88) is arranged in a 4×4 grid. A parity digit is added to each row and each column, so every row and column has an even number of 1s. A parity digit is 0 if the count of 1s is even and 1 otherwise. The result is a 5×5 array with an unused corner, and sending its rows in turn gives 24 digits:
$$\mathbf x=[1\,1\,0\,1\,1\,0\,0\,1\,1\,0\,0\,1\,0\,1\,0\,1\,0\,0\,0\,1\,0\,0\,1\,1]\tag{4.89}$$
(p. 102).

**Correction.** If the first digit flips from 1 to 0, only the first row's and the first column's parity checks fail. The parity digits show both that there is an error and where it is, so it can be corrected (p. 103). Each parity digit is fully determined by the grid, so it carries zero bits in the encoded message. In the corrupted output it gives information about the true digits (p. 103).

**Cost.** The 4×4 code sends 24 digits per 16, a factor $24/16=1.5$. For an $n\times n$ block, the factor is $(n^2+2n)/n^2=1+2/n$. But it corrects only one error per $n^2+2n$ digits. For $n=20$, 400 digits become 440 (factor 1.1), with one correctable error per 440 digits. There is a trade-off between robustness and extra digits (pp. 103–104).

**Redundancy is good and bad (p. 104).** Redundancy can be removed to compress, but then the data are more prone to noise. Images and language are highly redundant. This makes each value robust to noise but means large amounts of data must be processed to recover little information (p. 104).

**Intuition note.** Extra digits that look useless in a clean channel become clues for spotting and fixing damage in a noisy one.

### 4.8 Shannon's noisy channel coding theorem (pp. 104–105)
**Channel capacity.**
$$C=\max_{p(X)}I(X,Y)\ \text{bits}\tag{4.90}$$
$$=\max_{p(X)}\,[H(X)-H(X|Y)]\ \text{bits}\tag{4.91}$$
If there is no noise, $H(X|Y)=0$ and this reduces to the noiseless definition (Eq. 3.2) (p. 104).

Error-correcting codes cut errors but also cut the information rate. In Shannon's day it was widely believed that zero error required zero rate. Shannon proved that information can be sent with vanishingly small error at a rate limited only by the channel capacity (p. 105). Shannon used "equivocation" for $H(X|Y)$, the remaining uncertainty about the input after the output is observed (p. 105).

**Theorem (Shannon, quoted by Stone, p. 105).** For a discrete channel of capacity $C$ and a source of entropy per second $H(X)$:
- If $H(X)\le C$, a coding system exists that transmits the source with an arbitrarily small frequency of errors (or arbitrarily small equivocation).
- If $H(X)\ge C$, one can encode so that $H(X|Y)<H(X)-C+\epsilon$ for arbitrarily small $\epsilon$.
- No encoding gives $H(X|Y)<H(X)-C$.

Stone's gloss: one can communicate with low error rate $\epsilon$ at a rate $R$ arbitrarily close to $C$, but not at a rate above $C$ (p. 105).

**Intuition note.** Capacity is a speed limit. Below it, clever coding can make errors as rare as you like. Above it, the excess becomes unavoidable uncertainty.

### 4.9 Rate distortion theory (pp. 106–107)
If $H(X)>C$, transmission is still possible but not without errors. Rate distortion theory describes the minimum distortion implied by the "channel overload" $H(X)-C$ (p. 106). Shannon (1949) said that attempting rate $C+E$ forces equivocation at least $E$, and "Nature takes payment by requiring just that much uncertainty" (p. 107). A fuller theory appeared in 1959 and is covered in Chapter 8 (p. 107). The text then says that, given a noiseless channel with fixed capacity $C$, we can expect almost perfect fidelity until the input entropy approaches $C$, with equivocation approaching zero up to that point. Beyond it equivocation increases, and this increase exactly matches the amount by which the input entropy exceeds $C$, so $R$ stays approximately equal to $C$ (p. 107).

**Figure 4.10 (p. 106).**
- If $H(X|Y)\ge H(X)$, then $I=0$ and $R=0$ (the "undesirable" region above the line $H(X|Y)=H(X)$).
- The "unattainable" region is below the line $H(X|Y)=H(X)-C$.

**Figure 4.11 (p. 107).** For $H(X)<C$, $R\approx H(X)$. For $H(X)>C$, $R\approx C$, and the excess entropy shows up as equivocation $H(X|Y)\ge H(X)-C$.

### 4.10 The noisy typewriter (pp. 108–110)
**Channel.** Typing a letter yields that letter or one of its two alphabetic neighbours, each with probability 1/3. The space is the 26th symbol and Z the 27th. Any output could come from three different inputs (Fig. 4.12, p. 108).

**Code.** Use only every third letter starting at B: B, E, H, K, N, Q, T, W, SP. Their output triplets are disjoint, so a look-up table decodes with no error ($\epsilon=0$). The last triplet is rearranged to [Y SP Z]. Output XFZAEYXDU decodes to WE BE WET (pp. 108–109).

**Numbers (1 letter per second, nine equally used inputs, p. 109).**
- $H(X)=\log 9=3.17$ bits/s (4.92–4.93).
- $H(Y)=\log 27=4.76$ bits/s (4.94–4.95).
- $H(Y|X)=\log 3=1.59$ bits/s, the noise entropy (4.96–4.97).
- $I=H(Y)-H(Y|X)=4.76-1.59=3.17$ bits/s (4.98–4.100).

**Check (p. 110).** Errors are zero, so $H(X|Y)=0$ and $I=3.17-0.00=3.17$ (4.101–4.103). The author argues that $I$ cannot exceed the input entropy, so $C=3.17$ bits/s. He states that, provided the noise entropy is fixed (e.g. a binary symmetric channel), a uniform input distribution is guaranteed to maximise $I$ for a discrete noisy channel.

**Use.** A 27-letter message needs $\log 27=4.75$ binary digits per letter. At 3.17 bits per typed letter, two typed letters carry each message letter, so the noisy typewriter becomes error-free (p. 110). The theorem's remarkable claim is that error can be made arbitrarily small for any data set, not only in cases like this one where it is zero (p. 110).

**Intuition note.** Using fewer, well-spaced symbols throws away some rate but removes confusion. The rate left over is the capacity.

### 4.11 Why the theorem is true (p. 111)
The author gives only a sketch of Shannon's proof.
- Take $N$ messages encoded as inputs $x_1..x_N$ whose entropy $H$ is below $C$. Build a random codebook in which each randomly chosen input is interpreted as a fixed, randomly chosen output. Chance overlaps cause cross-talk and decoding errors, so every codebook has an error rate.
- Shannon proved that, if $H\le C$, the error averaged over all possible codebooks approaches zero as the input length grows.
- So for long inputs, at least one codebook has an error rate as small as the small average $\epsilon$. The author's reasoning: if all codebooks had error $\epsilon$, the average would be $\epsilon$. If one has error greater than $\epsilon$, then at least one has error smaller than $\epsilon$.
- Stone cites Pierce: some regard the proof's logic as weird.

**Intuition note.** A random code is good on average, and an average cannot beat the best member. So a good code must exist.

### 4.12 Summary (p. 112)
Mutual information is the average uncertainty about one variable eliminated by knowing the other. The chapter applied it to a binary image, error-correcting codes, the noisy typewriter and Shannon's theorem. It notes that error-correcting codes always require more binary digits, which lowers the information per digit sent (p. 112).

## Toy example (ours, not from the text)
A binary channel is sampled 16 times. Counts of (input $x$, output $y$) pairs: (0,0): 6; (0,1): 2; (1,0): 2; (1,1): 6.
- Joint probabilities (divide by 16): 0.375, 0.125, 0.125, 0.375.
- Marginals: $p(x=0)=0.375+0.125=0.5$ and $p(x=1)=0.5$. Likewise $p(y)=\{0.5,0.5\}$. So $H(X)=H(Y)=1$ bit.
- $\log_2(1/0.375)=\log_2(8/3)=3-1.585=1.415$ and $\log_2(1/0.125)=3$.
- $H(X,Y)=2(0.375)(1.415)+2(0.125)(3)=1.061+0.75=1.811$ bits.
- $I=1+1-1.811=0.189$ bits.
- $H(Y|X)=H(Y)-I=1-0.189=0.811$ bits.
- Check against the noise: the flip probability is $0.125/0.5=0.25$. Then $H(\eta)=0.25\log 4+0.75\log\frac43=0.5+0.75(0.415)=0.811$ bits ✓, so $H(Y|X)=H(\eta)$ (Eq. 4.58).
- Fan-out: $2^{0.811}\approx1.75$ effectively equally likely outputs per input (Eq. 4.61).
- Transmission efficiency $I/H(Y)=0.189$.

## Concepts
- [[mutual-information]] — average reduction in uncertainty about one variable from knowing the other; $H(X)+H(Y)-H(X,Y)$ (p. 79, p. 90)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ is average surprisal per pair; $H(Y|X)$ is residual uncertainty about $Y$ after $X$ (pp. 84, 91)
- [[bit]] — unit of information; the author uses "bits per pair" and "bits per outcome" for emphasis (p. 84, p. 88)
- [[noisy-channel]] — channel whose output is the input plus noise, $Y=X+\eta$ (p. 93)
- [[channel-capacity]] — $C=\max_{p(X)}I(X,Y)$ (p. 104)
- [[noisy-channel-coding-theorem]] — near-zero error up to capacity; equivocation at least $H(X)-C$ above it (p. 105)
- [[error-correcting-code]] — redundancy (e.g. parity digits) that allows errors to be detected or corrected (p. 102)
- [[redundancy]] — here it is compressible, but also protects against noise (p. 104)
- [[rate-distortion-function]] — theory of the minimum error forced when $H(X)>C$; only introduced here (p. 106)
- [[marginalisation]] (new) — summing a joint distribution over one variable to get the marginal (p. 85)
- [[statistical-independence]] (new) — if $X$ and $Y$ are independent then $p(X,Y)=p(X)p(Y)$ and $H(X,Y)=H(X)+H(Y)$ (pp. 86–87)
- [[equivocation]] (new) — Shannon's name for $H(X|Y)$ (p. 105)
- [[transmission-efficiency]] (new) — Stone's definition: $I(X,Y)/H(Y)$ (p. 101)
- [[cross-talk-fan-diagram]] (new) — one input giving $2^{H(Y|X)}$ outputs and one output from $2^{H(X|Y)}$ inputs (p. 96)
- [[binary-symmetric-channel]] (new) — each bit flipped with fixed probability (p. 98)

## Canonical instances
- [[two-dice-joint-entropy]] — independence gives $5.17=2.59+2.59$ bits (p. 87)
- [[joint-table-4x4]] — $H(X)=1.81$, $H(Y)=1.99$, $H(X,Y)=3.30$, $I=0.509$ (pp. 82, 90–91)
- [[noisy-binary-image]] — 10% pixel flips; $I=0.436$; efficiency 0.481 (pp. 98–101)
- [[parity-block-code]] — Pierce's 4×4 + parity code; overhead $1+2/n$ (pp. 102–104)
- [[noisy-typewriter]] — non-confusable subset gives error-free 3.17 bits/s (pp. 108–110)

## Bridges (candidates)
- [structural-analogy] Disjoint output triplets in the noisy typewriter ↔ coding theory: non-overlapping decoding regions for codewords — one input per region lets lookup decoding work.
- [same-math] $I(X,Y)=H(X)+H(Y)-H(X,Y)$ ↔ KL divergence: $I$ equals the KL divergence of $p(X,Y)$ from $p(X)p(Y)$ — this follows from (4.29–4.30) read as an expected log ratio, but the chapter does not name it.
- [metaphor] Averaging over random codebooks to prove one good codebook exists ↔ probabilistic existence arguments in mathematics: a random object is good on average, so a good one exists.

## Questions this raises
- How does $\max_{p(X)}I(X,Y)$ get computed when the noise is not symmetric, so a uniform input may not be best?
- Why do random long codes reach capacity, and can practical codes be constructed that do?
- How does the capacity change for continuous channels, such as those with Gaussian noise?
- What exactly is the minimum distortion for a given rate, in the full rate-distortion theory the text defers to Chapter 8?

## Reading notes
- Printed page = pdf − 16 (pdf 95–128 are printed 79–112).
- Text-layer losses in the theorem quote (p. 105): the symbol $\epsilon$ is blank in the extraction and I wrote it from context.
- Misprints and loose points:
  - p. 83: text says "$Y=y_i$" for what should be $y_j$; "$n\times n$ array" is used for a 4×4 table.
  - p. 91: $H(X)$ is written as 1.811 in (4.45) but 1.81 in (4.40); the printed difference $1.81+1.99-3.30=0.50$ versus the stated 0.509 presumably reflects unrounded values (the page does not say).
  - Table 4.3 caption says cells are $p(\text{input},\text{output})$, but the cell for Output=0, Input=1 is labelled $p(0,1)$, which is output-first.
  - The output proportions 0.679 and 0.322 sum to 1.001, so they are rounded (p. 99).
  - Eq. (4.86) has a stray (4.87) label.
  - p. 107 says "Given a noiseless channel with a fixed capacity $C$" while discussing equivocation. I reported the passage as written.
- p. 97: the last sentence of the Fig. 4.8 discussion says the proportion of noise in the input is large compared with that in the output. This looks reversed relative to the preceding sentences (MI is a large share of the input entropy and a small share of the output entropy). The digest gives the reading consistent with those sentences and flags the printed wording.
- The claim on p. 110 that a uniform input maximises $I$ is stated in general form without proof here.
- No exercises appear in this unit. Section 4.11 is explicitly only a sketch.
