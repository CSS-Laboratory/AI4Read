---
id: mackay-2003-information/ch11-error
work: mackay-2003-information
unit: "11 Error-Correcting Codes and Real Channels"
pages: 176-190
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Error-Correcting Codes and Real Channels

## L0 — One line
A Gaussian channel with an average-power limit has capacity $C=\tfrac12\log(1+v/\sigma^2)$, but explicit practical codes as good as Shannon promised are still unknown: random codes need exponential resources, and decoding is hard even for simply defined linear codes.

## L1 — The gist (≤ 120 words)
Shannon's coding theorem was proved for discrete channels. Two questions follow. What can be said about channels with real-valued inputs and outputs, such as the Gaussian channel? And how close do practical codes come to the proved limits? MacKay shows that mutual information survives the move to continuous variables, gives the Gaussian-channel capacity, and links it to a sphere-packing picture and a bandwidth formula. He also shows that, for a Gaussian input, the posterior's precision (inverse variance) is the sum of the prior's and the likelihood's. For practical codes he defines very good, good, bad and practical codes, surveys families of practical codes, and notes that decoding is the hard part.

**Prerequisites:** Gaussian distribution and its precision; Bayes' rule; mutual information and the discrete noisy-channel coding theorem (Chs 9–10); binary matrices mod 2; Lagrange multipliers.

## L2 — Key ideas
- A continuous-time channel with bandwidth $W$, noise density $N_0$ and power $P$ is equivalent to $2W$ uses per second of a discrete-time Gaussian channel with $\sigma^2=N_0/2$ (p. 178).
- Defining the entropy of real variables by replacing sums with integrals is not well defined (it depends on the grain size). Mutual information has a well-behaved continuous limit, so capacity is still defined through it (p. 180).
- With a power cost $v(x)=x^2$, the capacity-achieving input is Gaussian and $C=\tfrac12\log(1+v/\sigma^2)$ (pp. 180–181, 189).
- For a Gaussian prior and Gaussian noise, the posterior mean is a precision-weighted average of the observation and the prior mean, and the precisions add (p. 181).
- A sphere-packing argument gives an upper bound on capacity (equality needs a more detailed argument). Combined with the 2W-uses equivalence, the capacity gives $C=W\log(1+P/N_0W)$, which favours wide bandwidth at low signal-to-noise ratio when power is fixed (p. 182).
- Random codes are good but need exponential resources. Linear codes are easy to encode, but general decoding is NP-complete (a class of problems widely believed to need exponential time in general) (pp. 183–184).
- Concatenation (an outer code around an inner code) is one trick for building codes with practical decoders; interleaving (reordering bits) lets the inner code's errors be treated as independent. Turbo and low-density parity-check codes use semi-random constructions and probabilistic message-passing decoding (pp. 184–187).
- Treating burst errors as independent (interleaving) loses capacity. In the worked example, 0.79 versus 0.53 bits per use (pp. 189–190).

## L3 — Walkthrough

### Preview (p. 177)
Chapter questions: (1) what Shannon's theory says about real-valued channels and how to map digital signals to analogue waveforms; (2) how practical codes are made and how they compare with Shannon's limits (p. 177). Background: the one- and multi-dimensional Gaussians, eqs. (11.1)–(11.4). The precision is $\tau\equiv1/\sigma^2$ (p. 176).

### 11.1 The Gaussian channel (pp. 177–178)
**Definition.** Real input $x$, real output $y$, with
$$P(y\mid x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\big[-(y-x)^2/2\sigma^2\big]\tag{11.5}$$
It is continuous in input and output but discrete in time. It is also called the additive white Gaussian noise (AWGN) channel (p. 177).

**Continuous-time motivation.** Output is $y(t)=x(t)+n(t)$. The power constraint is
$$\int_0^T dt\,[x(t)]^2/T\le P\tag{11.6}$$
The noise is white Gaussian with spectral density $N_0$ (p. 177).

Send $N$ real numbers using orthonormal basis functions $\phi_n$, with $\int_0^T\phi_n\phi_m\,dt=\delta_{nm}$:
$$x(t)=\sum_{n=1}^N x_n\phi_n(t)\tag{11.7}$$
The receiver computes
$$y_n\equiv\int_0^T dt\,\phi_n(t)y(t)=x_n+\int_0^T dt\,\phi_n(t)n(t)\equiv x_n+n_n\tag{11.8–11.9}$$
with $n_n\sim\mathrm{Normal}(0,N_0/2)$ (11.10). So this use of a continuous channel is the Gaussian channel (11.5). The power constraint becomes
$$\sum_n x_n^2\le PT\ \Rightarrow\ \overline{x_n^2}\le PT/N\tag{11.11}$$
(p. 178).

**Bandwidth.** $W=N^{\max}/2T$ (11.12), where $N^{\max}$ is the maximum number of orthonormal functions in time $T$. For a band-limited signal built from sines and cosines of maximum frequency $W$, $N^{\max}=2WT$. This matches Nyquist sampling: a signal with highest frequency $W$ is determined by samples spaced $\Delta t=1/2W$ apart (p. 178).

**Conclusion.** A real channel with bandwidth $W$, density $N_0$ and power $P$ equals $N/T=2W$ uses per second of a Gaussian channel with $\sigma^2=N_0/2$ and $\overline{x_n^2}\le P/2W$ (p. 178).

**Eb/N0.** To compare encoders with different rates $R$ (bits per channel use) and powers, use the power per source bit $E_b=\overline{x_n^2}/R$ relative to $N_0$:
$$E_b/N_0=\frac{\overline{x_n^2}}{2\sigma^2R}\tag{11.13}$$
It is dimensionless and usually quoted in decibels, $10\log_{10}E_b/N_0$ (p. 178). (Added step: since $\sigma^2=N_0/2$, i.e. $N_0=2\sigma^2$, this equals $\overline{x_n^2}/(RN_0)$.)

*Intuition note.* In this construction, a stretch of analogue wave is described by a list of real numbers, each hit by Gaussian noise of variance $N_0/2$. So the discrete-time Gaussian channel is the model to study.

### 11.2 Inferring the input to a real channel (p. 179)
Shannon's 1944 memorandum: tell apart two pulses of known shape, vectors $\mathbf x_0,\mathbf x_1$, sent through noise. The noise density is
$$P(\mathbf n)=\Big[\det\!\big(\tfrac{\mathbf A}{2\pi}\big)\Big]^{1/2}\exp\!\big(-\tfrac12\mathbf n^{\mathsf T}\mathbf A\mathbf n\big)\tag{11.14}$$
$\mathbf A$ is the inverse covariance, symmetric and positive definite. If $\mathbf A=\mathbf I/\sigma^2$ the noise is "white", otherwise "coloured". Then
$$P(\mathbf y\mid s)=\Big[\det\!\big(\tfrac{\mathbf A}{2\pi}\big)\Big]^{1/2}\exp\!\big(-\tfrac12(\mathbf y-\mathbf x_s)^{\mathsf T}\mathbf A(\mathbf y-\mathbf x_s)\big)\tag{11.15}$$
The optimal detector uses the posterior ratio:
$$\frac{P(s{=}1\mid\mathbf y)}{P(s{=}0\mid\mathbf y)}=\frac{P(\mathbf y\mid s{=}1)P(s{=}1)}{P(\mathbf y\mid s{=}0)P(s{=}0)}\tag{11.16}$$
$$=\exp\!\Big(-\tfrac12(\mathbf y-\mathbf x_1)^{\mathsf T}\mathbf A(\mathbf y-\mathbf x_1)+\tfrac12(\mathbf y-\mathbf x_0)^{\mathsf T}\mathbf A(\mathbf y-\mathbf x_0)+\ln\tfrac{P(s=1)}{P(s=0)}\Big)$$
$$=\exp\big(\mathbf y^{\mathsf T}\mathbf A(\mathbf x_1-\mathbf x_0)+\theta\big)\tag{11.17}$$
$$\theta=-\tfrac12\mathbf x_1^{\mathsf T}\mathbf A\mathbf x_1+\tfrac12\mathbf x_0^{\mathsf T}\mathbf A\mathbf x_0+\ln\tfrac{P(s=1)}{P(s=0)}\tag{11.18}$$
(Added step: the $\mathbf y^{\mathsf T}\mathbf A\mathbf y$ terms cancel, and with $\mathbf A$ symmetric the cross terms give $\mathbf y^{\mathsf T}\mathbf A(\mathbf x_1-\mathbf x_0)$.) The decision that minimizes the error probability is the most probable hypothesis. With the discriminant
$$a(\mathbf y)\equiv\mathbf y^{\mathsf T}\mathbf A(\mathbf x_1-\mathbf x_0)+\theta\tag{11.19}$$
guess $s=1$ if $a>0$, $s=0$ if $a<0$, and either if $a=0$ (11.20). It is linear in $\mathbf y$: $a=\mathbf w^{\mathsf T}\mathbf y+\theta$ with $\mathbf w\equiv\mathbf A(\mathbf x_1-\mathbf x_0)$ (11.21) (p. 179). In the example figures the pulses are 31-dimensional vectors (Fig. 11.2).

*Intuition note.* Gaussian noise makes the log posterior ratio a straight-line (linear) function of the received vector. The weights $\mathbf w$ are the pulse difference, reweighted by the noise's inverse covariance.

### 11.3 Capacity of the Gaussian channel (pp. 179–182)
Two issues arise for continuous variables: the infinite length of the real line and the infinite precision of real numbers (p. 179).

**Infinite inputs.** If any real $x$ were allowed, one use could carry arbitrarily many digits, reliably. So one introduces a cost function $v(x)$ and constrains the average cost $\bar v$. A generalized coding theorem with input cost exists (McEliece 1977), giving a capacity $C(\bar v)$. For the Gaussian channel, $v(x)=x^2$ (11.22), so $\overline{x^2}$ is constrained and one use cannot carry infinite information (p. 180).

**Infinite precision.** Replacing sums by integrals in the entropy is not well defined. The entropy of a discretized distribution diverges like the logarithm of the granularity: one more bit for every halving of the grain size $g$. Also one cannot take the log of a dimensional density (Fig. 11.4). Mutual information is the exception. Its log argument is a ratio of densities over the same space, so
$$I(X;Y)=\int dx\,dy\,P(x,y)\log\frac{P(x,y)}{P(x)P(y)}\tag{11.24}$$
$$=\int dx\,dy\,P(x)P(y\mid x)\log\frac{P(y\mid x)}{P(y)}\tag{11.25}$$
(discrete form 11.23) (p. 180).

Questions posed: (a) which $P(x)$ maximizes $I$ subject to $\overline{x^2}=v$; (b) does the maximum still measure the maximum error-free rate (p. 180).

**Result (Exercises 11.1–11.2, solutions p. 189).** The maximizing $P(x)$ is Gaussian with mean 0 and variance $v$. Then
$$C=\tfrac12\log\Big(1+\frac{v}{\sigma^2}\Big)\tag{11.26}$$
(p. 181). This depends on the signal-to-noise ratio $v/\sigma^2$.

*Proof of 11.1 (p. 189).* Use Lagrange multipliers $\lambda$ (power) and $\mu$ (normalization):
$$F=I(X;Y)-\lambda\!\int\! dx\,P(x)x^2-\mu\!\int\! dx\,P(x)\tag{11.36}$$
$$=\int dx\,P(x)\Big[\int dy\,P(y\mid x)\ln\frac{P(y\mid x)}{P(y)}-\lambda x^2-\mu\Big]\tag{11.37}$$
The functional derivative at $x^*$ is
$$\frac{\delta F}{\delta P(x^*)}=\int dy\,P(y\mid x^*)\ln\frac{P(y\mid x^*)}{P(y)}-\lambda x^{*2}-\mu-\int dx\,P(x)\int dy\,P(y\mid x)\frac{1}{P(y)}\frac{\delta P(y)}{\delta P(x^*)}\tag{11.38}$$
Since $P(y)=\int dx\,P(x)P(y\mid x)$, $\delta P(y)/\delta P(x^*)=P(y\mid x^*)$. The last term then equals 1 and is absorbed into $\mu$ (giving $\mu'$). Setting the derivative to zero and inserting the Gaussian $P(y\mid x)$:
$$\int dy\,P(y\mid x)\ln\frac{P(y\mid x)}{P(y)}-\lambda x^2-\mu'=0\tag{11.39}$$
$$\Rightarrow\int dy\,\frac{e^{-(y-x)^2/2\sigma^2}}{\sqrt{2\pi\sigma^2}}\ln[P(y)\sigma]=-\lambda x^2-\mu'-\tfrac12\tag{11.40}$$
This must hold for all $x$. Expand $\ln[P(y)\sigma]=a+by+cy^2+\cdots$. A term $y^p$ with $p>2$ would produce $x^p$ terms absent on the right, so only $a+cy^2$ works. Hence $P(y)$ is Gaussian. A Gaussian $P(x)$ produces it (p. 189).

*Proof of 11.2 (p. 189).* With Gaussian input of variance $v$, $P(y)=\mathrm{Normal}(0,v+\sigma^2)$, because variances add for independent variables.
$$I(X;Y)=\int dx\,dy\,P(x)P(y\mid x)\log P(y\mid x)-\int dy\,P(y)\log P(y)\tag{11.41}$$
$$=\tfrac12\log\tfrac1{\sigma^2}-\tfrac12\log\tfrac1{v+\sigma^2}=\tfrac12\log\Big(1+\frac v{\sigma^2}\Big)\tag{11.42–11.43}$$

*Intuition note.* Noise power fixes how finely you can tell inputs apart. Signal power fixes how far apart inputs can be. The Gaussian-channel capacity (per use) is a function of their ratio $v/\sigma^2$.

**Inference given a Gaussian input (p. 181).** If $P(x)=\mathrm{Normal}(x;0,v)$ and $P(y\mid x)=\mathrm{Normal}(y;x,\sigma^2)$, then $P(y)=\mathrm{Normal}(y;0,v+\sigma^2)$ and
$$P(x\mid y)\propto P(y\mid x)P(x)\tag{11.27}$$
$$\propto\exp(-(y-x)^2/2\sigma^2)\exp(-x^2/2v)\tag{11.28}$$
$$=\mathrm{Normal}\!\Big(x;\frac{v}{v+\sigma^2}y,\Big(\frac1v+\frac1{\sigma^2}\Big)^{-1}\Big)\tag{11.29}$$
by completing the square. The posterior mean is a weighted combination of the best fit to the output ($x=y$) and the best fit to the prior ($x=0$):
$$\frac{v}{v+\sigma^2}y=\frac{1/\sigma^2}{1/v+1/\sigma^2}y+\frac{1/v}{1/v+1/\sigma^2}0\tag{11.30}$$
The weights are the precisions of likelihood and prior. The posterior precision is their sum. The author states this generally: when two independent sources give Gaussian information about an unknown, the precisions add. This is "the dual" of variances adding when independent variables are added (p. 181).

*Intuition note.* The less noisy source gets more weight. In this Gaussian case the combined precision is the sum of the two, so it is at least as large as either alone.

**Coding theorem for the Gaussian channel (pp. 181–182).** Two routes. One: define a sequence of discrete channels derived from the Gaussian channel, with more and more inputs and outputs. Show their capacities tend to $C$, and apply the discrete theorem to each. The other is an intuitive argument, given next.

**Sphere packing (p. 182).** Treat $\mathbf x=(x_1,\dots,x_N)$ and $\mathbf y$ as points in $N$ dimensions. For large $N$, the noise power is very likely close (fractionally) to $N\sigma^2$. So $\mathbf y$ is very likely near the surface of a sphere of radius $\sqrt{N\sigma^2}$ centred on $\mathbf x$. If $\mathbf x$ is random with $\overline{x^2}=v$, it lies near a sphere of radius $\sqrt{Nv}$. The total average power of $\mathbf y$ is $v+\sigma^2$, so $\mathbf y$ lies near a sphere of radius $\sqrt{N(v+\sigma^2)}$. The volume of a radius-$r$ sphere is
$$V(r,N)=\frac{\pi^{N/2}}{\Gamma(N/2+1)}r^N\tag{11.31}$$
The maximum number of non-confusable inputs (spheres not overlapping significantly) is bounded by the ratio of volumes:
$$S\le\Big(\frac{\sqrt{N(v+\sigma^2)}}{\sqrt{N\sigma^2}}\Big)^N\tag{11.32}$$
$$C=\frac1N\log M\le\tfrac12\log\Big(1+\frac v{\sigma^2}\Big)\tag{11.33}$$
The author says a more detailed argument, like the one in the previous chapter, can establish equality (p. 182).

**Continuous channel (p. 182).** Substituting into the equivalence (2W uses per second):
$$C=W\log\Big(1+\frac P{N_0W}\Big)\ \text{bits per second}\tag{11.34}$$
With $W_0\equiv P/N_0$ (the bandwidth at which the signal-to-noise ratio is 1), $C/W_0=(W/W_0)\log(1+W_0/W)$ (Fig. 11.5). Capacity rises to an asymptote $W_0\log e$. For fixed power it is dramatically better to use low signal-to-noise over a large bandwidth than high signal-to-noise over a narrow one. This motivates wideband methods such as direct-sequence spread spectrum in 3G phones. Neighbours may object, so engineers often use higher-power narrow-bandwidth transmitters (p. 182).

### 11.4 Capabilities of practical error-correcting codes (pp. 183–186)
Nearly all codes are good, but nearly all need exponential look-up tables in the blocklength $N$, and the theorem needs large $N$. A practical code can be encoded and decoded in time polynomial in $N$, preferably linear (p. 183). Writing an explicit practical encoder and decoder as good as Shannon promises is still unsolved (p. 183).

**Definitions (p. 183).**
- *Very good* codes: a family achieving arbitrarily small error probability at any rate up to capacity.
- *Good* codes: arbitrarily small error probability at non-zero rates up to some maximum rate, which may be less than capacity.
- *Bad* codes: cannot achieve arbitrarily small error, or only by letting the rate go to zero. Repetition codes are an example. Bad codes are not necessarily useless in practice.
- *Practical* codes: encodable and decodable in time and space polynomial in blocklength.
- An $(N,K)$ block code is a list of $S=2^K$ codewords of length $N$.
- A *linear* $(N,K)$ block code has codewords forming a $K$-dimensional subspace. Encoding is $\mathbf t=\mathbf G^{\mathsf T}\mathbf s \bmod 2$, with $\mathbf G^{\mathsf T}$ an $N\times K$ binary matrix and $\mathbf s$ a $K$-bit vector. Codewords are also the vectors with $\mathbf H\mathbf t=\mathbf 0 \bmod 2$ ($\mathbf H$ the parity-check matrix).
- Example, the (7,4) Hamming code: four signal bits followed by three parity bits, $\mathbf G^{\mathsf T}$ shown on p. 183 (rows: $1000$, $0100$, $0010$, $0001$, $1110$, $0111$, $1011$).

Coding theory began with Hamming's codes, each able to correct one error per block (of which $R_3$ and the (7,4) code are the simplest). Most established codes since are generalizations: Bose–Chaudhury–Hocquenhem (as printed), Reed–Müller, Reed–Solomon, Goppa (pp. 183–184).

**Convolutional codes (p. 184).** No blocks. Bits are read and sent continuously, as linear functions of past source bits, using a linear-feedback shift register. The output is the source convolved with a linear filter. Discussed in Chapter 48.

**Are linear codes good? (p. 184)** *Rhetorical question:* is the Shannon limit missed because linear codes are inherently worse than random codes? The answer given is no. The coding theorem can still be proved for linear codes, at least for some channels (Ch. 14), but non-constructively. Linear codes are easy to encode. Decoding is not necessarily easy: the general maximum-likelihood decoding problem (find $\mathbf s$ in $\mathbf G^{\mathsf T}\mathbf s+\mathbf n=\mathbf r$) is NP-complete (Berlekamp et al. 1978). NP-complete problems are all equally hard and widely believed to need exponential time in general. So attention goes to codes with fast decoders.

**Concatenation (p. 184).** An encoder–channel–decoder chain $\mathcal C\to Q\to\mathcal D$ defines a super-channel $Q'$ with smaller error probability and complex error correlations. Build an outer encoder/decoder $\mathcal C',\mathcal D'$ for $Q'$. Outer code $\mathcal C'$ followed by inner code $\mathcal C$ is a concatenated code. *Interleaving*: read data in blocks larger than both blocklengths. After outer encoding, reorder bits so that nearby bits are separated when fed to the inner code. A simple interleaver is the *product code*: data in a $K_2\times K_1$ block, encoded horizontally by an $(N_1,K_1)$ code, then vertically by an $(N_2,K_2)$ code. (Exercise 11.3: show that either code can serve as inner or outer.)

**Figure 11.6 example (pp. 184–185).** Encode horizontally with $R_3=H(3,1)$ and vertically with $H(7,4)$. The figure shows 7 rows of 3 bits. Four source bits per codeword. Decoding each subcode in turn is convenient but not optimal. It makes most sense to decode first the code with the lowest rate, hence the most error-correcting ability.
- Order $H(3,1)$ then $H(7,4)$, with 5 flipped bits: the first decoder corrects three errors but wrongly alters the third bit of the second row (two errors in that row). The (7,4) decoder then corrects all remaining errors; the result matches the original.
- Other order: columns one and two hold two errors each, so the (7,4) decoder adds two errors. It fixes the one error in column 3. The (3,1) decoder cleans up four errors but wrongly infers the second bit. Three errors remain.

**Why interleave (p. 185).** Spreading out bits that are nearby in one code lets us ignore the complex correlations among the inner code's errors. A ruined inner codeword is spread one bit per outer codeword, so the errors can be treated as independent.

**Other channel models (pp. 185–186).**
- *Burst-error channels.* Reed–Solomon codes use Galois-field alphabets with many elements (e.g. $2^{16}$). Even if 17 successive bits are corrupted, only 2 successive symbols are. Concatenated Reed–Solomon codes on compact discs correct bursts of 4000 bits (p. 185).
- Exercise 11.4: interleaving is "theoretically a poor way" to protect against bursts, in terms of redundancy required (p. 186).
- *Fading channels.* Like Gaussian channels but with received power varying in time (e.g. a moving mobile phone). Power can vary by 10 dB (a factor of ten) over about a wavelength, a few centimetres (p. 186).

*Intuition note.* Maximum-likelihood decoding of a general linear code is NP-complete. Concatenation is one trick for getting practical decoders: each subcode is decoded with its own decoder in turn, conveniently though not optimally.

### 11.5 State of the art (pp. 186–187)
All practical codes for Gaussian channels are linear, based on convolutional or block codes (p. 186).
- *Textbook convolutional*: constraint length 7, the "de facto standard" for satellites.
- *Concatenated convolutional*: that code as inner code with an eight-bit-symbol Reed–Solomon outer code, used in deep space (Voyager).
- *Galileo*: same format, constraint length 15 and a larger Reed–Solomon code (JPL; details unpublished outside JPL; decoding needs special-purpose hardware). In 1992 it was the best known code of rate 1/4.
- *Turbo codes* (Berrou, Glavieux, Thitimajshima, 1993): two convolutional encoders; source bits fed to both, one in randomly permuted order (fixed at design time), and the parity bits of both are sent (Fig. 11.7). Decoding iterates between the two constituent decoders, each using the other's output; this is an instance of the sum–product message-passing algorithm (pp. 186–187).
- *Gallager's low-density parity-check codes*: the best known block codes for Gaussian channels. Invented 1962, promptly forgotten by most of the community, rediscovered 1995. Decoded by message passing (Ch. 47). Fig. 11.8 example: $N=16$, $M=12$ constraints, each bit in $j=3$ constraints, each constraint over $k=4$ bits, a rate-1/4, (16,4) code. Outstanding performance arises for $N\simeq10\,000$ (p. 187).

### 11.6 Summary (p. 187)
Random codes are good but need exponential resources. Non-random codes tend for the most part not to be as good; encoding may be easy, but decoding stays hard even for simply defined linear codes. The best practical codes (a) use very large block sizes, (b) use semi-random constructions, and (c) use probability-based decoding.

### 11.7 Nonlinear codes (p. 187)
Most practical codes are linear, not all. Cinema film sound errors come from dirt (many 1s) and scratches (many 0s), so no codeword should look like all-1s or all-0s. One cinema code is a nonlinear (8,6) code of 64 of the $\binom84$ weight-4 patterns.

### 11.8 Errors other than noise (p. 187)
If the receiver's time $u(t)$ is an imperfectly known function of the transmitter's time, capacity is reduced. The theory is incomplete. Not even the capacity of channels with synchronization errors is known. Codes for them are an active research area.

### 11.9–11.10 Exercises and solutions (pp. 188–190)
Solutions printed here that carry results:
- **Ex. 11.4 (burst channel, p. 189–190).** Chunks of $N=100$, burst probability $b=0.2$, binary symmetric channel with $f=0.5$ during bursts, error-free otherwise. Capacity is one minus the noise's information per bit. Per chunk, the noise information is roughly $H_2(b)+Nb$, accurate for large $N$. So
$$C=1-\Big(\tfrac1N H_2(b)+b\Big)=1-0.207=0.793\tag{11.44}$$
Interleaving treats it as a binary symmetric channel with $f=0.2\times0.5=0.1$, capacity about 0.53. Interleaving discards the information that errors are correlated. In theory, a code that treats bursts as bursts could communicate about $0.79/0.53$ times faster, which the source prints as $\simeq1.6$ (the ratio is actually about 1.5; see Reading notes).
- **Ex. 11.5 (p. 190).** (a) $C=\tfrac12\log(1+v/\sigma^2)$ (11.45). (b) For binary input $\pm\sqrt v$ the capacity is achieved with equal probabilities. It is a "somewhat messy integral" (11.46), smaller than (a), but close to it at small signal-to-noise. (c) Thresholding the output gives a binary symmetric channel, $C''=1-H_2(f)$ with $f=\Phi(\sqrt v/\sigma)$ (11.47), where $\Phi$ is the error function of p. 156.
- **Ex. 11.9–11.10 (RAID, p. 190).** One easily understood RAID stores data at rate 4/7 using the (7,4) Hamming code, one codeword bit per disk (7 disks). Two, perhaps three, dead disks can be survived; the channel model is the erasure channel, since dead disks are detectable. The code has weight-3 codewords. If the three lost disks match a weight-3 codeword, the other four disks give only 3 bits about the four source bits. Any other three lost disks are fine because the corresponding $4\times4$ submatrix of the generator matrix is invertible. A better code would be a digital fountain (Ch. 50).

## Toy example (ours)
Gaussian channel with noise variance $\sigma^2=1$ and input power $v=3$.
- Capacity: $C=\tfrac12\log_2(1+3/1)=\tfrac12\log_2 4=1$ bit per use.
- Sphere packing: radius ratio $\sqrt{N(v+\sigma^2)}/\sqrt{N\sigma^2}=\sqrt4=2$, so $S\le2^N$ non-confusable inputs. Then $\tfrac1N\log_2S\le1$ bit, the same value.
- Inference with Gaussian input: suppose $y=2$ is received. The posterior mean is $\frac{v}{v+\sigma^2}y=\frac34\cdot2=1.5$. Check via weights: precisions are $1/\sigma^2=1$ and $1/v=1/3$, sum $4/3$. The weight on $y$ is $1/(4/3)=0.75$, the weight on 0 is $(1/3)/(4/3)=0.25$, so the mean is $0.75\cdot2+0.25\cdot0=1.5$. The posterior variance is $(4/3)^{-1}=0.75$, smaller than both $\sigma^2=1$ and $v=3$.
- Rate-compensated SNR: using $x_n^2=3$ and rate $R=1/2$, $E_b/N_0=3/(2\cdot1\cdot0.5)=3$.

## Concepts
- [[gaussian-channel]] (new) — real input and output, $y=x+$ Normal$(0,\sigma^2)$ noise, discrete in time; also called AWGN (p. 177)
- [[channel-capacity]] — maximum mutual information under the input cost constraint; for the Gaussian channel $\tfrac12\log(1+v/\sigma^2)$ (pp. 180–181)
- [[shannon-hartley-formula]] — $C=W\log(1+P/N_0W)$ bits per second for the continuous band-limited channel (p. 182)
- [[mutual-information]] — the one information measure with a well-behaved continuous limit, eq. (11.24) (p. 180)
- [[differential-entropy]] — the problem MacKay points out: replacing sums by integrals is not well defined; entropy depends on grain size (p. 180)
- [[noisy-channel-coding-theorem]] — here extended to the Gaussian channel via derived discrete channels or sphere-packing intuition (p. 181)
- [[sphere-packing-argument]] (new) — count non-overlapping noise spheres inside the output sphere to bound capacity (p. 182)
- [[eb-n0]] (new) — rate-compensated signal-to-noise ratio $x_n^2/(2\sigma^2R)$ (p. 178)
- [[posterior-distribution]] — for Gaussian prior and likelihood, a Gaussian with the sum of the precisions (p. 181)
- [[likelihood]] — $P(\mathbf y\mid s)$, used in Shannon's pulse detector (p. 179)
- [[precision-addition]] (new) — independent Gaussian sources of information add their precisions (p. 181)
- [[error-correcting-code]] — redundancy added to detect and correct errors; classified here as very good, good, bad, practical (p. 183)
- [[linear-block-code]] (new) — codewords form a subspace; $\mathbf t=\mathbf G^{\mathsf T}\mathbf s$, $\mathbf H\mathbf t=0$ mod 2 (p. 183)
- [[concatenated-code-interleaving]] (new) — outer code on the super-channel made by an inner code; interleaving makes errors look independent (pp. 184–185)
- [[burst-error-channel]] (new) — errors arrive in correlated bursts; interleaving ignores this and loses capacity (pp. 185–186, 189–190)
- [[turbo-and-ldpc-codes]] (new) — semi-random constructions with iterative message-passing decoding (pp. 186–187)

## Canonical instances
- [[shannon-1944-pulse-detection]] — Bayesian detector for two known pulses in coloured Gaussian noise, linear discriminant (p. 179)
- [[hamming-7-4-code]] — a linear (7,4) code with $\mathbf G^{\mathsf T}$ given (p. 183)
- [[product-code-figure-11-6]] — decoding order matters in $H(3,1)\times H(7,4)$ (p. 185)
- [[burst-channel-capacity-0.79-vs-0.53]] — interleaving's loss on a burst channel (pp. 189–190)
- [[galileo-voyager-codes]] — concatenated convolutional + Reed–Solomon deep-space codes (p. 186)
- [[raid-hamming-erasure]] — RAID as a (7,4) Hamming code over an erasure channel (p. 190)
- [[cinema-sound-nonlinear-8-6-code]] — 64 weight-4 patterns avoid all-0 and all-1 words (p. 187)

## Bridges (candidates)
- [same-math] Gaussian posterior with added precisions ↔ bayesian: conjugate Normal–Normal updating — posterior mean is a precision-weighted average of prior mean and data.
- [structural-analogy] Shannon's linear discriminant for two pulses ↔ bayesian: posterior odds with Gaussian class-conditional densities — both give a log-odds linear in $\mathbf y$.
- [structural-analogy] Capacity $\tfrac12\log(1+\mathrm{SNR})$ ↔ information-theory: Shannon–Hartley formula, with one use of the channel as one sample.
- [structural-analogy] Interleaving to make errors look independent ↔ bayesian: assuming exchangeability or independence of errors that are not truly independent.
- [metaphor] Concatenation as a super-channel ↔ information-theory: source–channel separation — build blocks separately and chain them.

## Questions this raises
- If linear codes can achieve capacity non-constructively (the chapter says at least for some channels), which structure makes some codes (turbo, LDPC) both decodable and near-capacity?
- What is the capacity of channels with synchronization errors, which the chapter says is unknown?
- When the true channel has correlated errors, how much does a decoder gain by modelling them rather than interleaving?
- How closely does the sphere-packing heuristic (noise power near $N\sigma^2$) match a rigorous proof of the Gaussian coding theorem?

## Exercises worth doing
- Ex. 11.2 (p. 181) — derive the Gaussian-channel capacity from the optimal input — difficulty: easy
- Ex. 11.1 (p. 181) — prove the optimal input is Gaussian (Lagrange multipliers, functional derivative) — difficulty: medium
- Ex. 11.4 (p. 186) — compute the burst-channel capacity versus the independent-error approximation — difficulty: easy
- Ex. 11.5 (p. 188) — compare capacities for real, binary-input, and thresholded-output Gaussian channels — difficulty: easy
- Ex. 11.3 (p. 184) — show that either code of a product code can be viewed as inner or outer — difficulty: medium
- Ex. 11.6 (p. 188) — fraction of binary codes that are linear — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 188 = printed 176).
- p. 185 text says the product code's blocklength "is 27". Figure 11.6 shows 7 rows of 3 bits, i.e. 21. Probably a misprint in the source.
- Eq. (11.46) is labelled $C''$ in the solution to Ex. 11.5(b). The exercise (and Fig. 11.9 caption) call the binary-input capacity $C'$, and (11.47) is $C''$. Also, $N(y;x)$ is printed as $(1/\sqrt{2\pi})\exp[(y-x)^2/2]$ without the minus sign in the exponent; the image shows no minus.
- Eq. (11.33) uses $M$ for the number of codewords, while (11.32) uses $S$. They denote the same count.
- Eq. (11.42) is printed as shown; the page goes directly from (11.41) to (11.42) without showing the intermediate integrals.
- p. 190 prints $(0.79/0.53)\simeq1.6$, but $0.79/0.53\approx1.49$, so the printed factor looks like an arithmetic slip in the source.
- The text layer garbles $\binom84$ on p. 187 into "84". The image shows a binomial coefficient.
- The printed text (p. 184) spells the names "Bose–Chaudhury–Hocquenhem"; L3 follows the printed spelling.
- Solution to Ex. 11.4 uses "$N$" for the entropy of the flipped bits in a burst; the page does not explain this; it is consistent with $f=0.5$, where each bit in a burst carries one bit of entropy.
- Ex. 11.7, 11.8 have no printed solutions in these pages; Ex. 11.6 has none either.
