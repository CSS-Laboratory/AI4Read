---
id: convolution
type: concept
fields: [bayesian, information-theory, linear-algebra]
fields_strong: [bayesian, information-theory, linear-algebra]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch07-matrix, jaynes-2003-probability/appc-convolutions, jaynes-2003-probability/ch07-central-p2]
generated_by: build_kg.py
---

# convolution

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/appc-convolutions]] (p. 677): $h(x)=\int f_1(y)f_2(x-y)\,dy$; defined for general real functions, not only densities [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch07-central-p2]] (p. 223): density of a sum of independent variables, $f_1*f_2=\int dx_1f_1(x_1)f_2(y-x_1)$ [new; work fields: bayesian, information-theory]

### linear-algebra

- [[boyd-2018-vmls/ch07-matrix]] (p. 136): $c_k=\sum_{i+j=k+1}a_ib_j$; coefficients of a polynomial product [new]

## Instances that use it

- [[polynomial-multiplication-as-convolution]] — $c=a*b$ gives the product's coefficients — from [[boyd-2018-vmls/ch07-matrix]]
- [[iresnet]] — contractive residual flow with spectrally normalized convolutions — from [[murphy-2023-pml2/ch23-normalizing]]
- [[glow-model]] — multi-scale coupling flow with $1\times1$ LU convolutions for faces — from [[prince-2023-udl/ch16-normalizing]]
- [[ai-plus-bi-convolution]] — $(x-a)^n\boxplus(x-b)^n=(x-(a+b))^n$, showing largest roots can add — from [[spielman-2025-sagt/ch43-ramanujan]]
- [[zero-matrix-convolution]] — $q=x^n$ has $\mathcal K_q(w)=1/w$, explaining the $1/w$ term — from [[spielman-2025-sagt/ch43-ramanujan]]

## Candidate bridges

- [structural-analogy] Impulse-response convolution ↔ signal filtering in time-series analysis: output is the input weighted by a kernel. — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → other:mathematics)
- [same-math] Laplace transform of a convolution is a product ($Y=HU$) ↔ probability: the transform of a density of a sum of independent variables is the product of transforms — same convolution theorem. — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (control-theory → other:probability)
- [structural-analogy] Renewal equation transform $\hat u=\hat f/(1-\hat\varphi)$ ↔ control-theory: a closed-loop transfer function $1/(1-L)$ with a convolution kernel in the loop. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [same-math] Convolution of coefficient vectors ↔ polynomial multiplication (shown on p. 137). — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → unspecified)
- [structural-analogy] Incidence matrix of a chain graph ↔ difference matrix $D$ ↔ first-order differences as convolution with $(1,-1)$. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → unspecified)
- [same-math] Fourier rules (B.10)–(B.12) ↔ signal processing: convolution theorem and derivative rule (canon link; not stated in this unit). — from [[jaynes-2003-probability/appb-mathematical]] (bayesian → other:signal-processing)
- [same-math] additivity of cumulants under convolution ↔ bayesian/probability: if the density of a sum of independent variables is the convolution of their densities, cumulants add. The text itself keeps the algebra probability-free. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → bayesian)
- [structural-analogy] $\log\mathcal F$ additive under convolution ↔ signal processing: the "cepstrum", mentioned (p. 678) but not developed here. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → other:signal-processing)
- [same-math] Gaussian convolution: variances add ↔ Bayesian: Gaussian prior × Gaussian noise gives a Gaussian marginal with summed variances — both are (7.49). — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → bayesian)
- [same-math] moving average ↔ signal processing: convolution theorem, low-pass filter — $Z=WY$ is literally the convolution theorem. — from [[jaynes-2003-probability/ch17-principles-p1]] (bayesian → other:signal-processing)
- [same-math] Check update (47.15) as a convolution computed by Fourier transform ↔ signal processing: convolution theorem; the GF(2) transform is $f^0\pm f^1$. — from [[mackay-2003-information/ch47-low]] (information-theory → other:signal-processing)
- [metaphor] FA "spray can" slid along a line (Fig. 28.6) ↔ convolution of a noise kernel along a latent direction — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [same-math] 1×1 convolution with activation (same fully connected map at every position) ↔ llm: the per-token feed-forward (MLP) block of a Transformer — both apply one shared network independently at each position. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
- [structural-analogy] self-attention as content-dependent routing ↔ convolution: both share parameters across positions, but attention weights depend on the inputs — from [[prince-2023-udl/ch12-transformers]] (llm → other:mathematics)
- [structural-analogy] GCN layer ↔ CNN convolution (ch. 10): same weights at every position, neighbours send messages, but no fixed spatial layout. — from [[prince-2023-udl/ch13-graph]] (llm → other:cnn-convolution-ch-10)
- [structural-analogy] Voiculescu's theorem (infinite dimension, equality) ↔ free probability: the finite inequality mirrors the limiting additive convolution (p. 348). — from [[spielman-2025-sagt/ch43-ramanujan]] (linear-algebra → other:probability)
- [structural-analogy] constant-diagonal K ↔ signal processing: convolution filters and Fourier transform (the author links these, p. 78). — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other:signal-processing)
- [same-math] Convolution Rule F(c ⊛ d) = (Fc).*(Fd) ↔ signal processing: convolving signals is multiplying their transforms — the text itself says this simplifies signal processing (p. 268). — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → other:signal-processing)
- [same-math] Fourier matrix diagonalizing circulants ↔ signal processing: circular convolution is diagonalized by the DFT — the same eigenvectors (1, λ, λ², λ³). — from [[strang-2023-introduction/ch08-linear]] (linear-algebra → other:signal-processing)
- [same-math] Convolution matrix with constant diagonals ↔ linear algebra: Toeplitz/band matrix — the text identifies the filter as a Toeplitz matrix (p. 383) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
