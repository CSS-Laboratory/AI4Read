---
id: polyanskiy-2025-information/ch01-introduction
work: polyanskiy-2025-information
unit: "Introduction (front matter, unnumbered)"
pages: xvii–xxiii
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Introduction

## L0 — One line
The authors treat information as a measure of difference between two beliefs, with Shannon's KL-based version as the case that gets premium treatment, and present information theory as a field whose true scope is much broader than compression and transmission, with recent developments in statistics, learning and computer science.

## L1 — The gist (≤ 120 words)
The Introduction asks what "information" and "information theory" mean for this book. Its answer: information is the dissimilarity between a prior and a posterior belief. KL divergence is often the right choice (Shannon's argument) and gives Shannon entropy as the average information of an observation. The authors are convinced other measures (total variation, Hellinger, χ²) are also needed. They say the field has no precise definition. They name four recent drivers: high-dimensional systems, non-memoryless channels, machine learning, and theoretical computer science. They also state the book's scope and omissions, explain the link to statistics, and suggest course routes. This matters because it shows the lens through which later chapters are written.

**Prerequisites:** probability mass functions; logarithms; the idea of a prior and a posterior belief. Terms used here but defined elsewhere in the book: KL divergence $D(Q\|P)$ (a dissimilarity between distributions, Definition 2.1), Shannon entropy (Definition 1.1), f-divergences (a family of dissimilarity measures that includes Hellinger and χ²), memoryless channel (a classical channel model, not defined in this unit).

## L2 — Key ideas
- Information is defined here as a measure of difference between two beliefs P (before) and Q (after an observation); Brillouin's quote is read as general except for its last sentence, which gives the Shannon case (p. xvii).
- With KL divergence as the dissimilarity, observing outcome $i$ gives $\log\frac1{p_i}$, and its average is the Shannon entropy (p. xviii).
- Measures other than KL (total variation, Hellinger, χ²) are claimed to be needed outside the classical realm, so Part I is not only about Shannon-type measures (p. xviii).
- Information theory has no precise definition. Narrowly it is the study of optimal storage and transmission, and in practice it reaches mathematics, physics, NLP and more (pp. xviii–xix).
- Four developments motivated the book: high-dimensional systems, "one-shot" analysis of non-memoryless channels, machine learning, and exchange with theoretical computer science (pp. xix–xx).
- A data-transmission channel and a statistical model are both a conditional distribution $P_{Y|X}$. The difference is who controls the allowed values of $X$ (p. xxii).
- Information theory also gives upper bounds in statistics, not only negative results (p. xxii).
- The book almost entirely skips multi-terminal theory, only briefly mentions functional inequalities, does not teach practical code design, and gives course routes for three audiences (pp. xxi, xxiii).

## L3 — Walkthrough

### What is information? (pp. xvii–xviii)
- The text notes that dictionaries list 17–18 meanings of "information". The book concerns only a precise mathematical notion that is independent of the application domain (p. xvii).
- Early quantification attempts named: Fisher on the uncertainty of statistical estimates, and Hartley, who defined information as the logarithm of the number of possibilities. Fisher and others also linked information to thermodynamic entropy (p. xvii).
- Shannon's work formalised "Shannon information" and adopted Tukey's word *bit* as its unit. It answers rigorous questions about optimal data compression and transmission rate, which singled it out as the right measure. Classical texts [106, 111, 177] focus exclusively on this view (p. xvii).
- **Brillouin's view (quoted):** with no special information there are several possible answers. Information reduces their number. It is a function of the ratio of the numbers before and after, and a logarithm is chosen so that information from independent situations adds (p. xvii).
- **Authors' reading:** only the last sentence (the logarithm) specialises to Shannon's version. The authors drop that sentence. For them, information is a measure of difference between two beliefs about the system state (p. xvii).
- Setup: the prior distribution $P$ describes our understanding (e.g., chance of rain). After an observation it becomes $Q$. The information in the observation is the dissimilarity between $P$ and $Q$, and how to quantify that depends on context (p. xvii).
- Shannon's case, by the authors' account: the choice is often the KL divergence $D(Q\|P)$ (Definition 2.1, not given in this unit). With prior $P=(p_1,\dots,p_k)$, observing outcome 1 gives posterior $Q=(1,0,\dots,0)$ and
$$D(Q\|P)=\log\frac1{p_1},$$
and similarly for other outcomes. Outcome $i$ has probability $p_i$, so the average dissimilarity is
$$\sum_{i=1}^k p_i\log\frac1{p_i},$$
which is the Shannon entropy (Definition 1.1) (p. xviii).
- The authors are convinced that non-KL measures are needed beyond the classical realms. Total variation, Hellinger distance and χ²-divergence (the latter two in the f-divergence family) are said to have found deep applications in statistical estimation, probability, communication complexity, estimation under communication constraints and property testing (Part VI). Shannon-type measures still get "premium treatment" in Part I (p. xviii).

*Intuition note:* An observation is informative when it moves your beliefs a lot. KL divergence is one way to measure the move, and averaging it over outcomes gives entropy. Other dissimilarities between beliefs are useful in other tasks.

### What is information theory? (pp. xviii–xx)
- It has no precise definition. Narrowly, it studies optimal methods of transmitting and storing data. "Coding theorems" (e.g., Shannon's noisy channel coding theorem, Theorem 19.9) show that algorithms exist, quantify their performance, and show it is best possible. This branch is sometimes called "IEEE-style" and influenced or revolutionized digital communication, wireless networks, cryptography, data compression (Lempel–Ziv) and more (p. xviii).
- Reach beyond that: Arnold and Kolmogorov resolved Hilbert's 13th problem (smooth functions) using Kolmogorov's metric entropy, following Shannon's rate-distortion theory. Kolmogorov–Sinai entropy solved the isomorphism problem for Bernoulli shifts. Landauer's principle and Maxwell-demon work were influenced by information theory. Modelling text as a high-order Markov model has seen spectacular successes recently, in the form of GPT and related models. Biology, neuroscience, control and AI also appear (pp. xviii–xix).
- The authors write that it seems objectively circumscribing the field is futile, and instead name four developments (p. xix):
  1. **New systems.** Robots have million-dimensional inputs (e.g., images), delayed, quantised and sent over noisy links. Inference targets are high-dimensional structured objects (sparse matrices, networks with communities), and sources are separated and rate-limited. Classical results on maximum likelihood and Fisher-information variance bounds are being re-examined (Chapter 29). These developments rely on f-divergences (Ch. 7), the mutual-information method (Ch. 30) and strong data-processing inequalities (Ch. 33) (p. xix).
  2. **Non-memoryless channels.** Modern channels (flash storage, multi-path or multi-antenna wireless) are far from memoryless, so "asymptotic i.i.d." theory is insufficient. The "one-shot" approach proves main results with abstract inputs and outputs, and gives them long-sequence structure only at the last step. It is also necessary in quantum information theory (p. xix).
  3. **Machine learning.** Metric entropy (Ch. 27) is a cornerstone of Vapnik's empirical risk minimisation, non-linear regression and density estimation (Ch. 32). Density estimation is probabilistic generative modelling. The authors say the best algorithms came from information-theoretic ideas: the Gibbs variational principle for KL (VAE, Example 4.2) and a variational characterisation of Jensen–Shannon divergence (GAN, Example 7.5) (p. xix). Optimal online-learning prediction performance is given by the maximum of the mutual information, via a link between prediction and universal compression (Ch. 13) that led to the multiplicative weight update algorithm (p. xx). Strong data processing (Ch. 33) helped resolve problems in distributed estimation, community detection and spiked Wigner PCA. PAC-Bayes methods, rooted in Donsker–Varadhan, gave generalisation-error bounds (Section 4.8*) (p. xx).
  4. **Theoretical computer science.** Links include entropy and combinatorics (Ch. 8), randomness extraction (Ch. 9), noisy gates (Section 33.1), models on trees and graphs (Section 33.5), and communication complexity with Hellinger distance (Exercise I.41). Recent examples: the chain rule gave Tao's strengthening of Szemerédi's regularity lemma (I.63) and Gilmer's union-closed sets result (I.61). The I-MMSE identity (Section 3.7*) gave a short proof of stochastic localisation (I.66). Spectral independence resolved sampling and counting conjectures (VI.26) (p. xx).

*Intuition note:* The authors say the classical "asymptotic i.i.d." theory of memoryless channels is insufficient for modern channels, and that inference targets are no longer low-dimensional parameters. Their response is a set of tools they name as needed: f-divergences, one-shot methods, strong data processing.

### Why another book on information theory? (pp. xx–xxi)
- Two motives: a graduate-level text at general level (not only discrete variables) with full rigour, and an introduction to the new connections above (p. xx).
- Cover–Thomas [106] introduces entropy, information and divergence, proves the main results, and samples topics such as universal compression and gambling. Csiszár–Körner [111] uses the "method of types" and gives error exponents and multi-terminal rate regions. Both focus almost exclusively on asymptotics, Shannon-type measures and finite alphabets (pp. xx–xxi).
- Specialised monographs exist [177, 211, 287, 198, 451, 264, 424] (p. xxi). Topics claimed to be treated only here include Chapters 7, 18, 22, 27, 30, 32 and 33 (p. xxi).
- **Omissions:** multi-terminal theory (except Sections 11.7*, 16.5*, 25.3*), functional inequalities (only briefly mentioned, in Sections 3.7*, 3.8* and associated exercises), and practical error-correcting codes and wireless design (references [360], [423] suggested) (p. xxi).

### A note to statisticians (pp. xxi–xxii)
- Information theory has long been used for minimax rates of estimation. Part VI applies Parts I–V to chosen examples and is not a full treatment of decision theory (p. xxii).
- Shared structure: both data transmission and inference are defined by a conditional distribution $P_{Y|X}$, called a *channel* in the first and a *statistical model/experiment* in the second. Both aim to estimate $X$ from noisy $Y$ (p. xxii).
- Difference: in transmission, $X$ is typically discrete and restricted to a carefully chosen codebook, whose design is considered the main difficulty. In statistics the allowed $X$ (the parameter) is constrained by the problem (e.g., sparsity or low rank), not by the statistician (p. xxii).
- Chapter 29: the data processing inequality gives Hammersley–Chapman–Robbins, Cramér–Rao and van Trees bounds. Chapter 30: the mutual-information method compares the information in the data with that needed for a given accuracy, using capacity and rate-distortion theory to lower-bound risk. It unifies the Le Cam, Assouad and Fano methods (Ch. 31) (p. xxii).
- Against the "common misconception" that information theory only gives negative results, Chapter 32 gives three upper bounds based on metric entropy (Yang–Barron, Le Cam–Birgé, Yatracos). Chapter 33 applies strong data processing to community detection, distributed estimation and random tree colourings (p. xxii).

### How to use this textbook (p. xxiii)
- **Introductory course:** Part I (Ch. 1–3 and selected sections, discrete case only), Part II (Ch. 10, 11.1–11.5), Part III (Ch. 14 and selected sections), Part IV (Ch. 17–18 and selected sections), Part V (selected sections), then Chapters 30 and 33 (p. xxiii).
- **Graduate, communication and compression:** go faster through Part I, then Parts II–V in depth (strong converse, finite blocklength, feedback), omit Chapter 27, and work the Part IV exercises (p. xxiii).
- **Graduate, statistical learning:** Part I (especially Ch. 7), Part II (especially Ch. 13), Part III, Chapters 17–19 and 27, then more than half the semester on Part VI, with at least 5–6 lectures on Chapters 32–33 (p. xxiii).
- Asterisked sections are difficult and can be skipped at first reading. The index links topics (p. xxiii).

## Toy example
*(Ours, not from the text.)* Prior over three outcomes: $P=(\tfrac12,\tfrac14,\tfrac14)$. Use $\log_2$.
- Observing outcome 1 gives $Q=(1,0,0)$, so $D(Q\|P)=\log_2\frac1{1/2}=1$ bit.
- Observing outcome 2 or 3 gives $\log_2\frac1{1/4}=2$ bits.
- Average over outcomes: $\tfrac12\cdot1+\tfrac14\cdot2+\tfrac14\cdot2=0.5+0.5+0.5=1.5$ bits.
- Entropy: $H(P)=\sum p_i\log_2\frac1{p_i}$ is the same sum, so it also equals 1.5 bits. The rarer outcomes move beliefs more.

## Concepts
- [[entropy-H-X]] — average, over outcomes, of the KL dissimilarity between prior and the posterior that puts all mass on the observed outcome (p. xviii)
- [[relative-entropy-kl-divergence]] — $D(Q\|P)$, the dissimilarity between posterior $Q$ and prior $P$ in Shannon's case (p. xviii)
- [[f-divergence]] — family that includes Hellinger and χ² (named alongside total variation); used where KL is not the right measure (p. xviii)
- [[bit]] — unit of Shannon information, from Tukey's word (p. xvii)
- [[noisy-channel]] — a conditional distribution $P_{Y|X}$, also the statistical model in inference (p. xxii)
- [[noisy-channel-coding-theorem]] — named as a classical coding theorem (Theorem 19.9) (p. xviii)
- [[data-processing-inequality]] — used for estimation lower bounds (Ch. 29); strong version in Ch. 33 (pp. xix, xxii)
- [[fisher-information]] — gives classical variance bounds for estimation, re-examined (p. xix)
- [[rate-distortion-function]] — theory used to lower-bound statistical risk (p. xxii)
- [[universal-coding]] — linked to optimal online prediction (Ch. 13) (p. xx)
- [[one-shot-coding]] (new) — proving results with abstract inputs and outputs, adding sequence structure last (p. xix)
- [[metric-entropy]] (new) — Kolmogorov's notion, used in learning and in statistical upper bounds (pp. xviii, xix, xxii)
- [[mutual-information-method]] (new) — lower-bounding statistical risk by comparing data information with the information required for a given accuracy (p. xxii)

## Canonical instances
- [[brillouin-information-definition]] — information as a function of the ratio of possible answers before and after (p. xvii)
- [[rain-clouds-belief-update]] — prior $P$ on rain, posterior $Q$ after seeing clouds (p. xvii)
- [[hilbert-13th-problem]] — resolved using metric entropy (p. xviii)
- [[vae-gibbs-variational]] — VAE via the Gibbs variational principle, Example 4.2 (p. xix)
- [[gan-jensen-shannon]] — GAN via Jensen–Shannon variational characterisation, Example 7.5 (p. xix)
- [[gpt-markov-text-model]] — text modelled as a high-order Markov model (p. xix)

## Bridges (candidates)
- [structural-analogy] channel $P_{Y|X}$ ↔ statistics: statistical model/experiment — both are conditional distributions, and the codebook is the main point of difference (p. xxii)
- [structural-analogy] information as prior-to-posterior dissimilarity ↔ Bayesian updating: belief change after an observation (p. xvii)
- [structural-analogy] Brillouin's logarithm chosen for additivity over independent situations ↔ Shannon's log-based information: the same motive for a logarithm (p. xvii)
- [structural-analogy] prediction ↔ universal compression: optimal online prediction linked to maximal mutual information (p. xx)

## Questions this raises
- For which tasks is KL the right dissimilarity, and when do total variation, Hellinger or χ² fit better?
- Why does the "asymptotic i.i.d." theory fail for non-memoryless channels, and what does one-shot analysis change?
- How exactly does the mutual-information method turn capacity and rate-distortion theory into minimax lower bounds?
- What does the Gibbs variational principle contribute to VAEs?

## Reading notes
- Printed pages are roman numerals xvii–xxiii, matching the page labels (pdf 19–25, offset 2 plus roman numbering). No misprints noticed.
- Page headers show an export stamp ("itbook-export … August 16, 2024"). The text layer garbles the equations (e.g. "D(QkP)", "log p11"), so they were transcribed from the page images.
- This unit has no equations beyond $D(Q\|P)=\log\frac1{p_1}$ and the entropy sum, and no exercises. Cross-references to chapters, examples and exercises point to material outside these pages, so only the authors' claims about them are reported.
