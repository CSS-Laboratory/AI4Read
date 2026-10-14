---
id: polyanskiy-2025-information/ch26-rate
work: polyanskiy-2025-information
unit: Part V opening — Rate-distortion theory and metric entropy
pages: 473-476
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Part V opening: Rate-distortion theory and metric entropy

## L0 — One line
Part V extends compression from exact reconstruction of discrete sources to lossy compression of continuous ones, where the cost is measured by bits versus allowed distortion.

## L1 — The gist (≤ 120 words)
Lossless compression (Part II) has entropy as its limit, but this paradigm is confined to discrete random variables. Part V asks how few bits are needed to encode a continuous random variable so that the decoded version stays within a prescribed distortion of the original. The study of optimal quantization is called rate-distortion theory. It matters because many natural signals are continuous, and because allowing some errors can save a lot of bits. The Part then moves from a converse bound to random-coding achievability, to explicit Gaussian and Hamming cases, and to the separation principle for end-to-end communication. It ends with metric entropy, a non-probabilistic theory that can be viewed as rate-distortion for a worst-case distribution.

**Prerequisites:** lossless source coding and entropy; channel coding (error-correcting codes); the idea of a metric (distance) on a space.

## L2 — Key ideas (5–10 bullets)
- Lossless compression has entropy as its fundamental limit, but this paradigm is confined to discrete random variables (p. 475).
- Lossy compression asks for a decoded $\hat X$ whose distortion from $X$ is bounded, on average or with high probability (p. 475).
- There are two motivations: natural signals are continuous, and allowing errors gives large savings, as in JPEG, MPEG and MP3 (p. 475).
- Quantization maps analog signals to digital ones; in information theory, the study of optimal quantization is rate-distortion theory (p. 475).
- Chapters 24–26 give the formulation and a tight converse, then random-coding achievability with covering lemmas, then Gaussian and Hamming examples (pp. 475–476).
- Optimal lossy compression plus an optimal error-correcting code gives an optimal end-to-end scheme; the text says this explains why bits are the "natural currency" of the digital age (p. 476).
- Metric entropy is a non-probabilistic quantization theory that compresses any element of a metric space, and it can be viewed as rate-distortion for a worst-case distribution (p. 476).

## L3 — Walkthrough

**Motivation and setup (p. 475).**
- Part II treated lossless compression: compress a source $X$ into a minimal number of bits, on average (resp. exactly) so that $X$ can be reconstructed exactly (resp. with high probability). The limit is the entropy of $X$. The authors say this paradigm is confined to discrete random variables (p. 475).
- Part V treats continuous random variables, called *lossy data compression*. $X$ is encoded into as few bits as possible. The decoded $\hat X$ must be a faithful reconstruction, meaning a *distortion metric* (a numerical measure of mismatch) between $X$ and $\hat X$ is bounded by a prescribed fidelity. The bound holds either on average or with high probability (p. 475).
- Motivation 1: audio, images and video are continuous. There is a need to represent them using finitely many bits for digital processing. Figure 23.7 shows sampling (continuous to discrete time) and quantization (analog to digital range) (p. 475).
- Motivation 2: much can be gained if reconstruction errors are allowed. This matters when some errors, such as high-frequency components in natural audio and visual signals, are imperceptible to humans. This underlies JPEG (images), MPEG (video) and MP3 (audio) (p. 475).
- *Quantization* is the mapping of continuous or analog signals into discrete or digital ones. The study of optimal quantization in information theory is *rate-distortion theory*, introduced by Shannon in 1959 (p. 475).

*Intuition note.* The text says lossless coding, whose limit is entropy, is confined to discrete variables (p. 475). For continuous variables the requirement is changed: the decoded value only has to stay within a bounded distortion of the original. The question then becomes how few bits are enough for a given distortion bound.

**Roadmap of the Part (pp. 475–476).**
- Section 24.1 looks at quantization. Section 24.2 gives the information-theoretic formulation. Section 24.3 gives a simple and tight converse bound. The matching achievability bound is deferred to the next chapter (p. 475).
- Chapter 25 presents the hard direction of the rate-distortion theorem: the random-coding construction of a quantizer. The method extends to a covering lemma and a soft-covering lemma. These give Cuff's sharp result that the fundamental limit of channel simulation is Wyner's common information. They also give a strengthened form of Han–Verdú's results on approximating output distributions in KL (p. 475).
- Chapter 26 evaluates the rate-distortion function for Gaussian and Hamming sources. It also discusses the foundational implication: an optimal lossy compressor paired with an optimal error-correcting code forms an optimal end-to-end communication scheme. This is the joint source-channel coding separation principle (pp. 475–476).
- Chapter 27 studies Kolmogorov's metric entropy, a non-probabilistic theory of quantization for sets in metric spaces. Rate-distortion compresses samples from a fixed distribution. Metric entropy compresses any element of the space. The link is that metric entropy can be viewed as rate-distortion theory applied to the "worst-case" distribution on the space, an idea expanded in Section 27.6 (p. 476).
- Metric entropy has consequences in probability (empirical processes, small-ball probability) and in statistical learning (entropic upper and lower bounds for estimation), explored in Part VI. Exercises cover Brownian motion (Exercise V.30) and random matrices (Exercise V.29) (p. 476).

*Intuition note.* Traditional rate-distortion compresses samples from a fixed distribution; metric entropy compresses any element of the metric space. The text says metric entropy can be viewed as rate-distortion theory applied to the "worst-case" distribution on the space (p. 476).

## Toy example (ours, not from the text)
Let $X$ be uniform on $[0,1)$ and use squared error $(X-\hat X)^2$ as distortion.
- 0 bits: always output $\hat X=0.5$. Average distortion $=\int_0^1 (x-0.5)^2dx = 2\cdot\frac{0.5^3}{3}=\frac1{12}\approx 0.0833$.
- 1 bit: say whether $X<0.5$. Output $0.25$ or $0.75$. On $[0,0.5)$: $\int_0^{0.5}(x-0.25)^2dx = 2\cdot\frac{0.25^3}{3}=\frac1{96}$. The other half gives the same. The total is $\frac1{96}+\frac1{96}=\frac1{48}\approx0.0208$.
- Going from 0 to 1 bit lowered the distortion from $\frac1{12}$ to $\frac1{48}$ here. Distortion is paid for with bits; for this continuous $X$, no finite number of bits gives exact recovery.

## Concepts
- [[lossy-compression]] (new) — encoding a continuous random variable into few bits so that reconstruction is only within a distortion bound (p. 475)
- [[distortion-metric]] (new) — measure of mismatch between $X$ and $\hat X$, bounded on average or with high probability (p. 475)
- [[quantization]] (new) — mapping continuous/analog signals into discrete/digital ones (p. 475)
- [[rate-distortion-function]] — named here as the quantity evaluated for Gaussian and Hamming sources in Chapter 26; the text calls the study of optimal quantization rate-distortion theory, and the function itself is not defined in this unit (p. 475)
- [[source-coding-theorem]] — lossless limit given by entropy; here only recalled from Part II (p. 475)
- [[source-channel-separation]] — optimal lossy compressor plus optimal error-correcting code gives an optimal end-to-end scheme (p. 476)
- [[metric-entropy]] (new) — Kolmogorov's non-probabilistic quantization theory for sets in metric spaces (p. 476)

## Canonical instances
- [[jpeg-mpeg-mp3]] — deployed lossy standards that exploit imperceptible errors (p. 475)
- [[sampling-and-quantization]] — analog-to-digital pipeline of Figure 23.7 (p. 475)

## Bridges (candidates)
- [structural-analogy] metric entropy ↔ statistical learning: entropic upper and lower bounds for estimation — the text says metric entropy has far-reaching consequences for statistical learning, e.g. entropic bounds for estimation (p. 476)
- [structural-analogy] rate-distortion for the worst-case distribution ↔ minimax thinking: metric entropy as the hardest-distribution case (p. 476)
- [metaphor] "bits as currency" ↔ economics: the text says the separation principle explains why bits are the natural currency of the digital age (p. 476).

## Questions this raises
- What exactly is the rate-distortion function, and why is the converse bound tight?
- Why does random coding achieve the rate-distortion limit?
- How do Gaussian and Hamming sources differ in their rate-distortion functions?
- In what precise sense is metric entropy rate-distortion for a worst-case distribution?

## Reading notes
- The unit is a Part opener: printed pages 473–476, with no equations. Printed = pdf − 25.
- Pages 473 and 474 are only the Part title and a blank page. Running header: "itbook-export CUP/HE2-design August 16, 2024".
- Section numbers (24.1–24.3, 27.6) and Figure 23.7 refer to chapters outside this unit. The unit id contains "ch26", but the content is the Part V introduction.
- The text says Shannon introduced rate-distortion theory "in 1959 [380]"; I report it as printed.
