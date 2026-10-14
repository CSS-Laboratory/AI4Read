---
id: polyanskiy-2025-information/ch04-mutual
work: polyanskiy-2025-information
unit: "Chapter 3 (printed numbering; listed as ch04 in the metadata) — Mutual information"
pages: 41-65
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Mutual information

## L0 — One line
Mutual information is the KL divergence between a joint law and the product of its marginals, and its basic properties (non-negativity, chain rule, data processing) lead to Fano's inequality, which the author calls a main workhorse for showing that some tasks cannot be done.

## L1 — The gist (≤ 120 words)
The chapter defines I(X;Y) as D(P_{X,Y}‖P_X P_Y). It shows that for discrete variables this equals a drop in entropy. It proves non-negativity, symmetry, the chain rule and the data-processing inequality (DPI). Equality in the DPI is linked to Fisher's sufficient statistics. Fano's inequality says that when I(X;Y) is small, one should not be able to predict X from Y with a small probability of error. Two starred sections prove the I-MMSE identity for Gaussian noise and use it to derive the entropy power inequality. Fano's inequality in particular is presented as a main workhorse for studying fundamental limits in information theory and statistics.

**Prerequisites:** KL divergence and its chain rule and DPI (Ch. 2); entropy and differential entropy (Ch. 1–2); conditional probability and Markov chains; basic measure theory (absolute continuity); gradients and Hessians for §3.7.

## L2 — Key ideas (5–10 bullets)
- I(X;Y) = D(P_{X,Y}‖P_X P_Y) = D(P_{Y|X}‖P_Y|P_X) (the P_X-average of D(P_{Y|X=x}‖P_Y)). It is symmetric, non-negative, and zero iff X and Y are independent (X ⊥⊥ Y) (pp. 42–43).
- For discrete X, I(X;Y) = H(X) − H(X|Y) when H(X|Y) < ∞. Conditioning reduces entropy on average, not for each realization (pp. 44–46).
- Closed forms: bivariate Gaussian ½ log 1/(1−ρ²) (ρ = correlation); AWGN channel (additive white Gaussian noise, Y = X + N) with Gaussian input ½ log(1+SNR), where SNR is the signal-to-noise power ratio; BSC (binary symmetric channel, flip probability δ) log 2 − h(δ), with h the binary entropy function; Gaussian vectors via determinants (pp. 47–50).
- Conditional mutual information obeys the chain rule I(X,Y;Z) = I(X;Z) + I(Y;Z|X), and I(X;Z|Y) = 0 iff X→Y→Z (a Markov chain: Z depends on X only through Y). This gives the DPI I(X;Z) ≤ I(X;Y) (pp. 50–52).
- Equality in the DPI (for every parameter distribution P_θ) is equivalent to sufficiency of a statistic. Fisher's factorization theorem gives a practical test (pp. 53–55).
- Fano: H(X|Y) ≤ P_e log(M−1) + h(P_e), proved by applying the divergence DPI to an auxiliary distribution Q (P_e = probability of error, M = size of X's alphabet). This yields lower bounds on error probability (pp. 56–58).
- I-MMSE: for Y = √γ X + Z with Gaussian noise Z, dI(X;Y)/dγ = (log e/2)·mmse, where mmse is the minimum mean squared error of estimating X from Y (p. 59). From it the entropy power inequality N(A₁+A₂) ≥ N(A₁)+N(A₂) follows (p. 64).

## L3 — Walkthrough

**Intro (p. 41).** The author says Shannon defined mutual information and Robert Fano coined the name. It has two equivalent forms: a KL divergence and a difference of entropies (p. 41). Section 3.6 gives the first operational statement (Fano); §3.7–3.8 treat I-MMSE and the entropy power inequality (p. 41).

### 3.1 Mutual information (pp. 41–44)
**Definition 3.1.** $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$. It measures dependence by comparing the joint law with the product of marginals (p. 42). It can also be seen as a functional of the pair $(P_X,P_{Y|X})$ (p. 42).

**Example 3.1.** If X = Y ~ N(0,1), then $P_{X,Y}\not\ll P_XP_Y$ and I = ∞. If at least one of X, Y is discrete, then always $P_{X,Y}\ll P_XP_Y$ (p. 42). Proof idea: if $P_{X,Y}(E)>0$, some atom $x_0$ has $P_Y(E^{x_0})>0$, so $P_XP_Y(E)\ge P_X(\{x_0\})P_Y(E^{x_0})>0$ (p. 42).

**Theorem 3.2 (properties).**
- (a) If Y is standard Borel, $I(X;Y)=D(P_{Y|X}\|P_Y|P_X)$ (3.1). This is Theorem 2.16(a) with $Q_{Y|X}=P_Y$.
- (b) Symmetry. The DPI applied to the swap kernel $(x,y)\mapsto(y,x)$ gives $D(P_{X,Y}\|P_XP_Y)\ge D(P_{Y,X}\|P_YP_X)$. Applying it again gives equality.
- (c) $I\ge0$, with equality iff $X\perp\!\!\!\perp Y$ (from $D\ge0$).
- (d) For any f, $I(f(X);Y)\le I(X;Y)$ (DPI for the kernel $(x,y)\mapsto(f(x),y)$). If f is one-to-one with measurable inverse, equality holds (apply the inequality to f and $f^{-1}$).
- (e) $I(X_1,X_2;Z)\ge I(X_1;Z)$ (take $f(X_1,X_2)=X_1$ in (d)) (pp. 42–43).

(3.1) implies $D(P_{X,Y}\|P_XP_Y)<\infty$ iff $x\mapsto D(P_{Y|X=x}\|P_Y)$ is $P_X$-integrable (p. 43).

**Lemma 3.3.** For Y standard Borel, $P_{X,Y}\ll P_XP_Y \iff P_{Y|X=x}\ll P_Y$ for $P_X$-a.e. x (p. 43).
- (⇒) Let $g=dP_{X,Y}/d(P_XP_Y)$ and $\rho(x)=\int g(x,y)P_Y(dy)$. Computing $P_X[E]$ two ways gives ρ = 1 $P_X$-a.e. Define $\tilde P_{Y|X}(dy|x)=g(x,y)P_Y(dy)$ if ρ(x)=1, and $P_Y(dy)$ otherwise. This is a valid version of the conditional law and is ≪ $P_Y$ for every x (p. 43).
- (⇐) Modify the kernel to $P_Y$ off the good set. Theorem 2.12 gives a density f(y|x), and then $P_{X,Y}[E]=\int_E f\,dP_YdP_X$, so $P_{X,Y}\ll P_XP_Y$ (pp. 43–44).

*Intuition note.* Mutual information is "how far the joint law is from independence". The condition-by-condition form (3.1) is the one used most: average over x the divergence of Y's conditional law from its marginal.

### 3.2 Mutual information as a difference of entropies (pp. 44–46)
**Theorem 3.4.**
- (a) $I(X;X)=H(X)$ if X is discrete, and $+\infty$ otherwise.
- (b) If X is discrete, $I(X;Y)+H(X|Y)=H(X)$ (3.2). Hence either $H(X|Y)=H(X)=\infty$, or $H(X|Y)<\infty$ and $I(X;Y)=H(X)-H(X|Y)$ (3.3). The first case can occur with Y constant and X from Example 1.3 (footnote, p. 44).
- (c) If X, Y are both discrete, $I(X;Y)+H(X,Y)=H(X)+H(Y)$. If $H(X,Y)<\infty$, then $I=H(X)+H(Y)-H(X,Y)$.
- (d) For real vectors with a joint PDF, $I=h(X)+h(Y)-h(X,Y)$ provided $h(X,Y)<\infty$. Also $I=h(X)-h(X|Y)$ provided $h(X|Y)<\infty$.
- (e) If X or Y is discrete, $I(X;Y)\le\min(H(X),H(Y))$. Equality holds iff $H(X|Y)=0$ or $H(Y|X)=0$, equivalently iff one is a deterministic function of the other (pp. 44–45).

*Proof of (a)* (p. 45). By Theorem 3.2(a), $I(X;X)=\mathbb E_{x\sim X}D(\delta_x\|P_X)$. For discrete $P_X$, $D(\delta_x\|P_X)=\log\frac1{P_X(x)}$, which gives $H(X)$. If $P_X$ is not discrete, let $\mathcal A$ be its set of atoms and $\Delta=\{(x,x):x\notin\mathcal A\}$. Then $P_{X,X}(\Delta)=P_X(\mathcal A^c)>0$ but $(P_X\times P_X)(\Delta)=0$. So $P_{X,X}\not\ll P_XP_X$ and $I=+\infty$.

*Proof of (b)* (p. 45). Take a countable support S, counting measure λ, and $\mu=\lambda\times P_Y$. Then $f_P=dP_{X,Y}/d\mu=p_{X|Y}(x|y)$ and $f_Q=dP_XP_Y/d\mu=p_X(x)$. By the definition of Radon–Nikodym derivatives, $\mathbb E[p_{X|Y}(x_0|Y)]=p_X(x_0)$ (3.4). Then
$$I(X;Y)=\mathbb E_{y\sim P_Y}\sum_{x\in S}p_{X|Y}(x|y)\log\frac{p_{X|Y}(x|y)}{p_X(x)},\qquad H(X|Y)=\mathbb E_{y\sim P_Y}\sum_{x\in S}p_{X|Y}(x|y)\log\frac1{p_{X|Y}(x|y)}.$$
Adding them, $I+H(X|Y)=\mathbb E_y\sum_x p_{X|Y}(x|y)\log\frac1{p_X(x)}$ (linearity). Interchanging E and Σ (Fubini) and using (3.4) gives $\mathbb E\log\frac1{P_X(X)}=H(X)$.

(c) adds H(Y) to (3.2) and uses the chain rule for H. (d) is the same with Lebesgue measure and is left as an exercise. (e) follows from (b) (pp. 45–46).

**Corollary 3.5.** For discrete X, $H(X|Y)\le H(X)$, with equality iff $X\perp\!\!\!\perp Y$. If $H(X)=\infty$ there is nothing to prove; otherwise use (3.2) (p. 46).

This holds on average, not per realization. Example: $U,Y\overset{\text{iid}}\sim\mathrm{Ber}(\frac12)$, $X=U\ \text{OR}\ Y$. Then $X\sim\mathrm{Ber}(\frac34)$ and $H(X)=h(\frac14)<1$ bit $=H(X|Y=0)$. But $H(X|Y)=\frac12\cdot1+\frac12\cdot0=\frac12$ bit $<H(X)$ (p. 46).

*Intuition note.* I(X;Y) is the average amount by which seeing Y shrinks the uncertainty about X. A single observation can raise uncertainty (Y = 0 above), but the average cannot.

**Remark 3.1 (Venn diagrams, p. 46–47).** For discrete variables the Venn diagram has H(X,Y) as the union and I(X;Y) as the overlap. For three variables, inclusion–exclusion gives the triple intersection
$$I(X_1;X_2;X_3)=H(X_1)+H(X_2)+H(X_3)-H(X_1,X_2)-H(X_2,X_3)-H(X_1,X_3)+H(X_1,X_2,X_3)\tag{3.5}$$
It can be positive or negative (the author asks "why?"). In general a unique signed measure μ on the finite algebra generated by sets $E_i$ turns every information quantity into a set operation, via $I/H\to\mu$, ";"→∩, ","→∪, "|"→∖. Examples: $H(X_1|X_2,X_3)=\mu(E_1\setminus(E_2\cup E_3))$ (3.6) and $I(X_1,X_2;X_3|X_4)=\mu(((E_1\cup E_2)\cap E_3)\setminus E_4)$ (3.7). The quantity (3.5) corresponds to $\mu(E_1\cap E_2\cap E_3)$, which is why μ need not be positive (p. 47).

### 3.3 Examples of computing mutual information (pp. 47–50)
**Example 3.2 (bivariate Gaussian).** With correlation $\rho_{X,Y}$,
$$I(X;Y)=\tfrac12\log\frac1{1-\rho_{X,Y}^2}\tag{3.8}$$
(plotted in Fig. 3.1). It diverges as $\rho\to\pm1$ (p. 47). Proof: WLOG $\mathbb EX=\mathbb EY=0$, $\mathbb EX^2=\mathbb EY^2=1$, so $Y=\rho X+Z$ with $Z\sim\mathcal N(0,1-\rho^2)\perp\!\!\!\perp X$. By the Gaussian divergence formula (2.7),
$$I=D(P_{Y|X}\|P_Y|P_X)=\mathbb E\,D(\mathcal N(\rho X,1-\rho^2)\|\mathcal N(0,1))=\mathbb E\Big[\tfrac12\log\tfrac1{1-\rho^2}+\tfrac{\log e}{2}\big((\rho X)^2+1-\rho^2-1\big)\Big]=\tfrac12\log\tfrac1{1-\rho^2}.$$
Alternatively, $I=h(Y)-h(Y|X)=h(Y)-h(Z)=\frac12\log(2\pi e)-\frac12\log(2\pi e(1-\rho^2))$, using shift invariance of h and independence of X and Z (pp. 47–48). The correlation coefficient also measures dependence, in a certain sense, for real (or inner-product-space) variables. Mutual information is invariant to bijections and defined for arbitrary random variables (p. 48).

**Example 3.3 (AWGN channel).** $Y=X+N$, $X\perp\!\!\!\perp N\sim\mathcal N(0,\sigma_N^2)$. If $X\sim\mathcal N(0,\sigma_X^2)$ then $Y\sim\mathcal N(0,\sigma_X^2+\sigma_N^2)$ and
$$I(X;Y)=h(Y)-h(Y|X)=h(X+N)-h(N)=\tfrac12\log\Big(1+\frac{\sigma_X^2}{\sigma_N^2}\Big).$$
The ratio $\sigma_X^2/\sigma_N^2$ is the signal-to-noise ratio (SNR); in dB it is $10\log_{10}\mathrm{SNR}$ (p. 48).

**Example 3.4 (BI-AWGN).** Input restricted to $\{\pm1\}$, $X\sim\mathrm{Ber}(1/2)$. Use $I=H(X)-H(X|Y)=\log2-H(X|Y)$. The posterior is $\mathbb P[X=+1|Y=y]=\dfrac{e^{y/\sigma_N^2}}{e^{-y/\sigma_N^2}+e^{y/\sigma_N^2}}$. After "some algebra",
$$I(X;Y)=\log2-\int_{-\infty}^{\infty}\tfrac1{\sqrt{2\pi}}e^{-z^2/2}\log\!\big(1+e^{-\frac2{\sigma^2}+\frac2\sigma z}\big)dz$$
(with σ meaning $\sigma_N$ as printed; p. 49). Here SNR $=\mathbb E[X^2]/\mathbb E[N^2]=1/\sigma_N^2$. Figure 3.2 shows that at low SNR binary input loses virtually no information relative to AWGN (p. 49). The figure's caption says these mutual informations will later be shown to coincide with the channel capacities (p. 49).

**Example 3.5 (Gaussian vectors).** For jointly Gaussian $\mathbf X\in\mathbb R^m$, $\mathbf Y\in\mathbb R^n$ (shapes: $\Sigma_{\mathbf X}$ is m×m, $\Sigma_{\mathbf Y}$ is n×n, $\Sigma_{[\mathbf X,\mathbf Y]}$ is (m+n)×(m+n)):
$$I(\mathbf X;\mathbf Y)=\tfrac12\log\frac{\det\Sigma_{\mathbf X}\det\Sigma_{\mathbf Y}}{\det\Sigma_{[\mathbf X,\mathbf Y]}}.$$
For $\mathbf Y=\mathbf X+\mathbf N$ with $\mathbf N\perp\!\!\!\perp\mathbf X$: $I(\mathbf X;\mathbf X+\mathbf N)=\frac12\log\frac{\det(\Sigma_{\mathbf X}+\Sigma_{\mathbf N})}{\det\Sigma_{\mathbf N}}$, since $\det\begin{pmatrix}\Sigma_{\mathbf X}&\Sigma_{\mathbf X}\\\Sigma_{\mathbf X}&\Sigma_{\mathbf X}+\Sigma_{\mathbf N}\end{pmatrix}=\det\Sigma_{\mathbf X}\det\Sigma_{\mathbf N}$ (the author marks this "why?"; p. 49).

**Example 3.6 (BSC).** $X\sim\mathrm{Ber}(\frac12)$, $N\sim\mathrm{Ber}(\delta)$ independent, $Y=X\oplus N$. Since $H(X|Y)=H(N)=h(\delta)$ (Example 1.4(1)), $I(X;Y)=\log2-h(\delta)$. The kernel $P_{Y|X}$ is $\mathrm{BSC}_\delta$ (p. 50).

**Example 3.7 (finite groups).** If X is uniform on a finite abelian group G and independent of Z, then $I(X;X+Z)=\log|G|-H(Z)$, because X+Z is uniform on G whatever the law of Z. The same holds for non-abelian groups with + replaced by the group operation, $x\mapsto x\circ Z$ (p. 50).

### 3.4 Conditional mutual information and conditional independence (pp. 50–54)
**Definition 3.6.** For standard Borel spaces,
$$I(X;Y|Z)\triangleq D(P_{X,Y|Z}\|P_{X|Z}P_{Y|Z}|P_Z)\tag{3.9}$$
$$=\mathbb E_{z\sim P_Z}[I(X;Y|Z=z)]\tag{3.10}$$
Under $P_{X|Z}P_{Y|Z}$, X and Y are independent given Z. $I(X;Y|Z)$ is linear in $P_Z$; measurability of $z\mapsto I(P_{X,Y|Z=z})$ follows from Lemma 2.13 (p. 50).

*Graphical language (pp. 50–51).* A DAG has random variables as nodes. Incoming edges of U list the variables needed to generate U. A Markov chain X→Y→Z means $P_{X,Y,Z}=P_XP_{Y|X}P_{Z|Y}$. This is equivalent to each of the following: $P_{X,Z|Y}=P_{X|Y}P_{Z|Y}$; $P_{Z|X,Y}=P_{Z|Y}$; $X\perp\!\!\!\perp Z|Y$; $X\leftarrow Y\to Z$ with $P_Y P_{X|Y}P_{Z|Y}$; and $Z\to Y\to X$. For general graphs, d-separation applies. A variable V is a *collider* on a path if the path has $\cdots\to V\leftarrow\cdots$. A and B are *d-connected by C* if some undirected path from A to B has (a) no non-colliders in C, and (b) every collider in C or with a descendant in C. Then $A\perp\!\!\!\perp B|C$ holds in every distribution satisfying the graphical model iff A and B are not d-connected by C. The book only needs the linear-chain equivalences (p. 51).

**Theorem 3.7** (all variables in standard Borel spaces).
- (a) $I(X;Z|Y)\ge0$, with equality iff X→Y→Z.
- (b) Chain rule (Kolmogorov identities): $I(X,Y;Z)=I(X;Z)+I(Y;Z|X)=I(Y;Z)+I(X;Z|Y)$.
- (c) DPI: if X→Y→Z then $I(X;Z)\le I(X;Y)$ (3.12), with equality iff X→Z→Y.
- (d) If X→Y→Z→W then $I(X;W)\le I(Y;Z)$.
- (e) Full chain rule: $I(X^n;Y)=\sum_{k=1}^nI(X_k;Y|X^{k-1})$.
- (f) If f, g are one-to-one with measurable inverses, $I(f(X);g(Y))=I(X;Y)$ (pp. 51–52).

*Proofs (p. 52).* (a) is the definition plus Theorem 3.2(c). (b): from (3.1), $I(Y;Z|X=x)=D(P_{Y|Z,X=x}\|P_{Y|X=x}|P_{Z|X=x})$. Averaging over X gives $I(Y;Z|X)=D(P_{Y|X,Z}\|P_{Y|X}|P_{X,Z})$. The divergence chain rule (2.24) gives
$$D(P_{X,Y,Z}\|P_{X,Y}P_Z)=D(P_{X,Z}\|P_XP_Z)+D(P_{Y|X,Z}\|P_{Y|X}|P_{X,Z}),$$
because conditioning on (X,Z) under $P_{X,Y}P_Z$ leaves $P_{Y|X}$. These two give the identity. (c): apply the Kolmogorov identity to $I(Y,Z;X)=I(X;Y)+I(X;Z|Y)=I(X;Z)+I(X;Y|Z)$; the term $I(X;Z|Y)=0$ for a Markov chain. (d): $I(X;W)\le I(X;Z)\le I(Y;Z)$. (e): recursion. (f): DPI for f and $f^{-1}$.

*Intuition note.* Processing a signal can never create information about its source. Equality means the processing lost nothing; the source states this as the Markov condition X→Z→Y, i.e. given the processed version Z, the original Y carries no further information about X.

**Remark 3.2.** $I(X;Y|Z)$ and $I(X;Y)$ are in general incomparable. Take $X,Z\overset{\text{iid}}\sim\mathrm{Ber}(\frac12)$ and $Y=X\oplus Z$: then $I(X;Y)=0$ but $I(X;Y|Z)=H(X)=1$ bit. In the other direction, take finite alphabets with Z = Y: then $I(X;Y|Y)=0$; the source writes this as $I(X;Y|Z)<I(X;Y)$ (strict only when $I(X;Y)>0$) (p. 53).

**Remark 3.3.** Setting $Y=X^n$ in (e) gives $H(X^n)=\sum_kH(X_k|X^{k-1})$, since $H(X_k|X^n,X^{k-1})=0$ (p. 53).

**Remark 3.4.** The DPI for I follows from the divergence DPI: $I(X;Z)=D(P_{Z|X}\|P_Z|P_X)\le D(P_{Y|X}\|P_Y|P_X)=I(X;Y)$, because for each x, $P_{Y|X=x}\to P_{Z|X=x}$ and $P_Y\to P_Z$ through the same kernel $P_{Z|Y}$. Any divergence satisfying the DPI (e.g. an f-divergence, Ch. 7) defines such a quantity $I_{\mathcal D}$ (p. 53).

**Remark 3.5 (strong DPI).** For many channels $P_{Y|X}$ there is $\eta_{KL}<1$, depending only on the channel, with $D(P_Y\|Q_Y)\le\eta_{KL}D(P_X\|Q_X)$ for all $P_X,Q_X$. Then U→X→Y implies $I(U;Y)\le\eta_{KL}I(U;X)$. For $\mathrm{BSC}_\delta$, $\eta_{KL}=(1-2\delta)^2$. If U→X→Y and $I(U;X)=I(U;Y)$, Y is called a sufficient statistic of X for U (p. 53).

### 3.5 Sufficient statistic and data processing (pp. 53–55)
Setting: a family $P_X^\theta$, θ∈Θ; a kernel $P_{T|X}$; induced $P_T^\theta=P_{T|X}\circ P_X^\theta$ (p. 54).

**Definition 3.8.** T is a *sufficient statistic* of X for θ if there is a kernel $P_{X|T}$ with $P_X^\theta P_{T|X}=P_T^\theta P_{X|T}$ for all θ, i.e. $P_{X|T}$ does not depend on θ. Interpretation: X can be simulated from T without knowing θ, so X adds nothing for identifying θ. Any one-to-one transform of X is sufficient, but the interesting cases have T much lower-dimensional. θ need not be random (frequentist view) (p. 54).

**Theorem 3.9.** The following are equivalent: (a) T is sufficient; (b) θ→T→X for all $P_\theta$; (c) $I(\theta;X|T)=0$ for all $P_\theta$; (d) $I(\theta;X)=I(\theta;T)$ for all $P_\theta$ (DPI with equality). The "∀$P_\theta$" is as printed; the source does not say how θ is randomised in (b)–(d) (see Reading notes). The proof restates conditions as conditional independence or uses the equality cases of Theorem 3.7 (p. 54).

**Theorem 3.10 (Fisher's factorization).** Let $P_X^\theta$ have densities $p_\theta$ w.r.t. a common dominating measure μ, and T = T(X) deterministic. Then T is sufficient iff $p_\theta(x)=g_\theta(T(x))h(x)$ for some measurable $g_\theta,h$ and all θ (p. 54).
Discrete proof. (⇒) $p_\theta(x)=P_\theta(X=x|T=T(x))\,P_\theta(T=T(x))$; the first factor is h(x) because sufficiency removes θ, and the second is $g_\theta(T(x))$. (⇐) $P_\theta(X=x|T=t)=\dfrac{g_\theta(t)h(x)}{\sum_x\mathbb 1\{T(x)=t\}g_\theta(t)h(x)}=\dfrac{h(x)}{\sum_x\mathbb 1\{T(x)=t\}h(x)}$, free of θ (pp. 54–55).

**Example 3.8.** For n i.i.d. samples: normal mean model $\mathcal N(\theta,1)$ has sufficient statistic the sample mean $\bar X$; coin flips $\mathrm{Ber}(\theta)$ have $\sum B_i$; $\mathrm{Unif}(0,\theta)$ has $\max_iU_i$ (p. 55).

**Example 3.9 (hypothesis testing).** Θ = {0,1}, X ~ $P_X$ or $Q_X$. Y (output of $P_{Y|X}$) is sufficient iff $D(P_{X|Y}\|Q_{X|Y}|P_Y)=0$, i.e. $P_{X|Y}=Q_{X|Y}$ $P_Y$-a.s. If $D(P_Y\|Q_Y)<\infty$, then $D(P_X\|Q_X)=D(P_Y\|Q_Y)\iff$ Y is sufficient for testing $P_X$ vs $Q_X$. Proof: with $P_{X,Y}=P_XP_{Y|X}$ and $Q_{X,Y}=Q_XP_{Y|X}$,
$$D(P_{X,Y}\|Q_{X,Y})=\underbrace{D(P_{Y|X}\|Q_{Y|X}|P_X)}_{=0}+D(P_X\|Q_X)=D(P_{X|Y}\|Q_{X|Y}|P_Y)+D(P_Y\|Q_Y)\ge D(P_Y\|Q_Y),$$
with equality iff the conditional term vanishes (p. 55). This explains the equality condition in Theorem 2.17.

*Intuition note.* A sufficient statistic is a summary that keeps all the information the data carry about the parameter. In information terms, summarising loses zero bits about θ.

### 3.6 Probability of error and Fano's inequality (pp. 55–58)
Three guessing problems for W with prediction Ŵ: random guessing (W ⊥⊥ Ŵ); guessing with data W→X→Ŵ with X = f(W); guessing with noisy data W→X→Y→Ŵ. The aim is converses: high uncertainty or scarce information makes guessing hard (pp. 55–56).

**Theorem 3.11.** Let |𝒳| = M < ∞. For any X̂ ⊥⊥ X,
$$H(X)\le F_M(\mathbb P[X=\hat X]),\quad F_M(x)\triangleq(1-x)\log(M-1)+h(x)\tag{3.13–3.14}$$
With $P_{\max}=\max_xP_X(x)$,
$$H(X)\le F_M(P_{\max})=(1-P_{\max})\log(M-1)+h(P_{\max}),\tag{3.15}$$
with equality iff $P_X=(P_{\max},\frac{1-P_{\max}}{M-1},\dots,\frac{1-P_{\max}}{M-1})$. $F_M$ is concave with maximum log M at 1/M but not monotone, so (3.15) does not imply (3.13), though $\mathbb P[X=\hat X]\le P_{\max}$ (p. 56).

*Proof.* Let $Q_{X,\hat X}=U_XP_{\hat X}$ with $U_X$ uniform, so $Q[X=\hat X]=1/M$. Apply the divergence DPI to the processor $(X,\hat X)\mapsto\mathbb 1\{X=\hat X\}$. With $P_S=\mathbb P[X=\hat X]$ this gives $d(P_S\|1/M)\le D(P_{X\hat X}\|Q_{X\hat X})=\log M-H(X)$ (p. 56). *(added step)* Here $d(p\|1/M)=\log M-h(p)-(1-p)\log(M-1)$, which turns this into (3.13). For (3.15): without side information the best guess is the mode, so $\max_{\hat X\perp\!\!\!\perp X}\mathbb P[X=\hat X]=P_{\max}$ (3.16); apply (3.13) with X̂ the mode. For equality, with $P=(P_{\max},P_2,\dots,P_M)$ and Q as in the equality condition, RHS − LHS of (3.15) equals $D(P\|Q)\ge0$, with equality iff P = Q (p. 57).

**Remark 3.6.** The proof builds an auxiliary distribution Q for which the error probability is easy, then uses the DPI to transfer the statement to P. The author calls this the *meta-converse* method (developed in Section 22.3). More direct proofs of (3.15) are in Ex. I.25. $H_\infty(P)=\log\frac1{P_{\max}}$ (3.17) is the Rényi entropy of order ∞, so Theorem 3.11 compares H and $H_\infty$ (p. 57). The estimator minimizing $\mathbb P[X\ne\hat X]$ is the MAP rule $\hat X(y)=\arg\max_xP_{X|Y}(x|y)$ (p. 57).

**Theorem 3.12 (Fano).** Let |𝒳| = M < ∞, X→Y→X̂, $P_e=\mathbb P[X\ne\hat X]$. Then
$$H(X|Y)\le F_M(1-P_e)=P_e\log(M-1)+h(P_e).\tag{3.18}$$
If $P_{\max}>0$, then regardless of |𝒳|,
$$I(X;Y)\ge(1-P_e)\log\frac1{P_{\max}}-h(P_e).\tag{3.19}$$
*Proof* (pp. 57–58). For (3.18), apply the divergence DPI to $P_{X,Y,\hat X}=P_XP_{Y|X}P_{\hat X|Y}$ versus $Q_{X,Y,\hat X}=U_XP_YP_{\hat X|Y}$ with processor $\mathbb 1\{X\ne\hat X\}$ ($P_{\hat X|Y}$ is the same in both). For (3.19), use $Q=P_XP_YP_{\hat X|Y}$:
$$I(X;Y)=D(P\|Q)\ge d(\mathbb P[X=\hat X]\|\mathbb Q[X=\hat X])\ge-h(P_e)+(1-P_e)\log\frac1{\mathbb Q[X=\hat X]}\ge-h(P_e)-(1-P_e)\log P_{\max},$$
since $\mathbb Q[X=\hat X]\le P_{\max}$ when X ⊥⊥ X̂ under Q (p. 58).

**Corollary 3.13.** If W→X→Y→Ŵ and W is uniform on [M] = {1,…,M}, then
$$P_e=\mathbb P[W\ne\hat W]\ge1-\frac{I(X;Y)+h(P_e)}{\log M}\ge1-\frac{I(X;Y)+\log2}{\log M}.\tag{3.20–3.21}$$
Proof: Theorem 3.12 plus $I(W;\hat W)\le I(X;Y)$ (p. 58).

*Intuition note.* If the observation carries less than about log M bits about a uniform W, then W cannot be recovered reliably. This is the pattern for converse proofs in coding and statistics.

### 3.7* Estimation error in Gaussian noise (I-MMSE) (pp. 58–63)
For X ∈ ℝ^d with $\mathbb E\|X\|^2<\infty$, $\mathrm{mmse}(X|Y)\triangleq\mathbb E\|X-\mathbb E[X|Y]\|^2$; the best estimator is $\mathbb E[X|Y]$ (p. 58). By Tao's inequality (Cor. 7.11), for X ∈ [−1,1], $0\le\mathrm{Var}(X)-\mathrm{mmse}(X|Y)\le\frac2{\log e}I(X;Y)$ (p. 58). The section proves an equality for Gaussian noise.

**Theorem 3.14 (I-MMSE).** Let X ∈ ℝ^d be independent of $Z\sim\mathcal N(0,I_d)$ with $\mathbb E\|X\|^2<\infty$. For all γ > 0,
$$\frac d{d\gamma}I(X;\sqrt\gamma X+Z)=\frac{\log e}2\,\mathrm{mmse}(X|\sqrt\gamma X+Z)\tag{3.22}$$
$$\frac{d^2}{d\gamma^2}I(X;\sqrt\gamma X+Z)=-\frac{\log e}2\,\mathbb E\big[\|\Sigma_\gamma(\sqrt\gamma X+Z)\|_F^2\big]\tag{3.23}$$
where $\Sigma_\gamma(y)=\mathrm{Cov}(X|\sqrt\gamma X+Z=y)$ and $\|\cdot\|_F$ is the Frobenius norm (p. 59). For Gaussian X, (3.22) can be checked by combining Example 3.3 with Example 28.1 (p. 59).

*Preliminaries.*
- (3.24) Differentiation under the integral: if K, L satisfy (a) $\int K(x,\theta)\mu(dx)$ exists; (b) $\int\mu(dx)\int_I d\theta|L|<\infty$; (c) $t\mapsto\int\mu(dx)L(x,t)$ is continuous; (d) $\partial_\theta K=L$; then $\frac\partial{\partial\theta}\int K\,dx=\int L\,dx$. On a finite interval, (b) and (c) follow from (e): $|L(x,t)|\le\ell(x)$ with ℓ μ-integrable (p. 59).
- Let $\varphi_a$ be the density of $\mathcal N(0,aI_d)$ and $p*f(x)=\mathbb E_{X'\sim p}f(x-X')$. For any derivative operator D, $D(p*\varphi_a)=p*(D\varphi_a)$ (3.25), via (3.24) with D = ∂/∂x₁ and induction (p. 59).
- The heat equation (3.26): $\frac\partial{\partial a}p*\varphi_a=p*\frac\partial{\partial a}\varphi_a=\frac12\Delta(p*\varphi_a)$, using $\frac\partial{\partial a}\varphi_a(x)=\frac1{2a^2}(\|x\|^2-ad)\varphi_a(x)=\frac12\Delta\varphi_a(x)$ (p. 60). The first equality uses (3.24) with $K=\varphi_a(y-x)$, since $\partial_a\varphi_a$ is bounded.

**Lemma 3.15.** Let $Y=X+\sqrt aZ$, X ~ p, X ⊥⊥ Z.
1. If $\mathbb E\|X\|<\infty$: $\nabla\ln(p*\varphi_a)(y)=\frac1a(\mathbb E[X|Y=y]-y)$ (3.27), and $\|\nabla\ln p*\varphi_a(x)\|\le\frac3a\|x\|+\frac4a\mathbb E\|X\|$ (3.28; cited from [344, Prop. 2]).
2. If $\mathbb E\|X\|^2<\infty$: $\mathrm{Hess}\ln(p*\varphi_a)(y)=\frac1{a^2}\mathrm{Cov}[X|Y=y]-\frac1aI_d$ (3.29) (p. 60).
Proof of (3.27): write $\mathbb E[X|Y=y]=\frac1{p*\varphi_a(y)}\int(y-x)p(y-x)\varphi_a(x)dx$ and use $\nabla\varphi_a(x)=-\frac xa\varphi_a(x)$ and (3.25) to get $y+\frac a{p*\varphi_a(y)}\nabla(p*\varphi_a)$ (p. 60).

*Proof of Theorem 3.14, (3.22).* Use natural logs. Let $a=1/\gamma$. Then $I(X;\sqrt\gamma X+Z)=I(X;X+\sqrt aZ)=h(X+\sqrt aZ)-\frac d2\ln(2\pi ea)$ (pp. 60–61). It suffices to show
$$\frac d{da}h(X+\sqrt aZ)=\frac d{2a}-\frac1{2a^2}\mathrm{mmse}(X|Y_a),\quad Y_a=X+\sqrt aZ\tag{3.30}$$
*(added step)* Then $\frac d{da}I=-\frac{1}{2a^2}\mathrm{mmse}$, and multiplying by $da/d\gamma=-1/\gamma^2$ with $a=1/\gamma$ gives $\frac12\mathrm{mmse}$, i.e. (3.22) in nats. The core computation (p. 61):
$$-\tfrac d{da}h=\tfrac d{da}\!\int(p*\varphi_a)\ln(p*\varphi_a)\overset{(a)}=\int\tfrac\partial{\partial a}[\cdots]\overset{(b)}=\tfrac12\!\int(1+\ln p*\varphi_a)\Delta(p*\varphi_a)\overset{(c)}=\tfrac12\!\int(p*\varphi_a)\Delta\ln(p*\varphi_a)\overset{(d)}=\tfrac12\!\int(p*\varphi_a)(y)\Big(\tfrac1{a^2}\mathrm{mmse}(X|Y_a=y)-\tfrac da\Big)dy.$$
Here (b) is (3.26) and (d) is the trace of (3.29). Steps (a) and (c) need justification (pp. 61–63):
- (a): apply (3.24) with μ = Lebesgue, $K=(p*\varphi_a)\ln(p*\varphi_a)$, $L=\partial_aK=\frac12(1+\ln(p*\varphi_a))(p*\Delta\varphi_a)$. Integrating (3.28) gives $|\ln p*\varphi_a(x)|\le c(1+\|x\|+\|x\|^2)$ (3.31). Also $|D(p*\varphi_a)|\le c'p*\varphi_{a_2}$ for $a<a_2$ (3.32). Hence $|L|\le\frac{cc'}2|2+\|x\|+\|x\|^2|\,(p*\varphi_{a_2})$, which is integrable, so condition (e) holds.
- (c): needs $\int V\Delta U=\int U\Delta V$ (3.34). The 1-D version is $\int u''v=\int v''u$ (3.33), under $\int|u''v|$, $\int|v''u|$ finite and $\int|u'v'|<\infty$, by integration by parts along a sequence where boundary terms vanish. The d-dimensional version follows by fixing the other coordinates and integrating. It is applied with $U=1+\ln(p*\varphi_a)$, $V=p*\varphi_a$. The integrability conditions follow from (3.29), (3.28), (3.31), (3.32).

The proof of (3.23) is by differentiating $\gamma\mapsto\mathrm{mmse}(X|\sqrt\gamma X+Z)$ with similar methods; the author refers to [206] (p. 63).

*Intuition note.* Adding a little more signal power γ raises the information about X at a rate proportional to the remaining estimation error. When X is already well estimated, extra power buys little extra information.

**Remark 3.7 (tensorization).** The 1-D version of (3.22) implies the d-dimensional one. Take a vector $\gamma=(\gamma_1,\dots,\gamma_d)$ and $Y_j=\sqrt{\gamma_j}X_j+Z_j$. By the chain rule, $\frac\partial{\partial\gamma_j}I(X;Y)=\frac\partial{\partial\gamma_j}I(X_j;Y_j|Y_{\sim j})$ (3.35). Since $\mathbb E[\mathrm{mmse}(X_j|Y_j,Y_{\sim j}=y_{\sim j})]=\mathrm{mmse}(X_j|Y)$, the 1-D result gives $\frac\partial{\partial\gamma_j}I(X;Y)=\frac{\log e}2\mathrm{mmse}(X_j|Y)$. Summing over j with $\mathrm{mmse}(X|Y)=\sum_j\mathrm{mmse}(X_j|Y)$ gives the d-dimensional identity along the diagonal. The author names the area theorem and Guerra interpolation as users of this idea (p. 63).

### 3.8* Entropy-power inequality (pp. 63–65)
The *entropy power* of an $\mathbb R^d$-valued X is $N(X)\triangleq\frac1{2\pi e}\exp\{\frac2dh(X)\}$. By Theorem 2.8 it is maximized, under a second-moment constraint, by an iid Gaussian vector. The EPI is read as "convolution increases Gaussianity". It was conjectured by Shannon and proved by Stam (p. 64). (Footnote 4: Barron's entropic CLT says $D(\frac{X_1+\dots+X_n}{\sqrt n}\|\mathcal N(0,1))\to0$ for iid zero-mean, unit-variance $X_i$ whenever finite, and the convergence is monotone.)

**Theorem 3.16 (EPI).** For independent $A_1,A_2$ in $\mathbb R^d$ with finite second moments, $N(A_1+A_2)\ge N(A_1)+N(A_2)$ (p. 64).

**Remark 3.8 (Costa).** For $A_2=\sqrt aZ$, the EPI is equivalent to $\frac d{da}N(A_1+\sqrt aZ)\ge1$. Costa proved the stronger fact that $a\mapsto N(A_1+\sqrt aZ)$ is concave (p. 64).

*Proof (following [437]).* Step 1 (Lieb): the EPI is equivalent to
$$h(U_1\cos\alpha+U_2\sin\alpha)\ge h(U_1)\cos^2\alpha+h(U_2)\sin^2\alpha\tag{3.36}$$
for all $U_1\perp\!\!\!\perp U_2$ and $\alpha\in[0,2\pi)$. To get the EPI from (3.36): take $\cos^2\alpha=\frac{N(A_1)}{N(A_1)+N(A_2)}$, $U_1=A_1/\cos\alpha$, $U_2=A_2/\sin\alpha$ (p. 64). Step 2: it suffices to prove (3.36) for smoothed versions $U_i+\sqrt\epsilon Z_i$, because $h(U_i+\sqrt\epsilon Z)=h(U_i)+O(\sqrt\epsilon)$ as ε→0 when $\mathbb E\|U_i\|^2<\infty$ ([344, Prop. 1]). Let $X=U_1\cos\alpha+U_2\sin\alpha$ and $Z=Z_1\cos\alpha+Z_2\sin\alpha$. By scale invariance, show for all γ ≥ 0:
$$h(\sqrt\gamma X+Z)\ge h(\sqrt\gamma U_1+Z_1)\cos^2\alpha+h(\sqrt\gamma U_2+Z_2)\sin^2\alpha.$$
Step 3: replace differential entropies by mutual informations. *(added step)* Since $h(\sqrt\gamma X+Z)=I(X;\sqrt\gamma X+Z)+h(Z)$ and Z has the same law as $Z_1$ and $Z_2$, the $h(Z)$ terms cancel because $\cos^2\alpha+\sin^2\alpha=1$. The inequality holds trivially at γ = 0, so it suffices to compare γ-derivatives; by (3.22) this reads
$$\mathrm{mmse}(X|\sqrt\gamma X+Z)\ge\mathrm{mmse}(U_1|\sqrt\gamma U_1+Z_1)\cos^2\alpha+\mathrm{mmse}(U_2|\sqrt\gamma U_2+Z_2)\sin^2\alpha.$$
Step 4: $\mathrm{mmse}(X|\sqrt\gamma X+Z)\ge\mathrm{mmse}(X|\sqrt\gamma U_1+Z_1,\sqrt\gamma U_2+Z_2)$ (more data). Given both observations, X is a sum of two conditionally independent terms, so the right side equals the claimed combination (p. 65).

**Corollary 3.17 (Minkowski).** For real positive definite n×n $\Sigma_1,\Sigma_2$: $\det(\Sigma_1+\Sigma_2)^{1/n}\ge\det(\Sigma_1)^{1/n}+\det(\Sigma_2)^{1/n}$. Proof: take $A_i\sim\mathcal N(0,\Sigma_i)$, use (2.18) and the EPI (p. 65). The author mentions uses of the EPI in the capacity region of the Gaussian broadcast channel and, through Ex. I.65, the log-Sobolev inequality (p. 65).

## Toy example (ours)
Take $X\sim\mathrm{Ber}(\frac12)$ and $Y=X\oplus N$, $N\sim\mathrm{Ber}(\frac14)$ independent (a $\mathrm{BSC}_{1/4}$).

*Joint law.* $P(0,0)=P(1,1)=\frac12\cdot\frac34=\frac38$ and $P(0,1)=P(1,0)=\frac12\cdot\frac14=\frac18$. Both marginals are $(\frac12,\frac12)$, so every product cell is $\frac14$.

*As a KL divergence (Def. 3.1).*
$$I=2\cdot\tfrac38\log_2\frac{3/8}{1/4}+2\cdot\tfrac18\log_2\frac{1/8}{1/4}=\tfrac34(\log_23-1)+\tfrac14(-1)$$
Numerically: $\log_2\frac{3/8}{1/4}=\log_2\frac32=\log_23-1\approx0.58496$, so the first part is $\frac34(0.58496)=0.43872$. The second part is $\frac14\cdot(-1)=-0.25$. So $I\approx0.43872-0.25=0.18872$ bit.

*As an entropy difference (3.3).* $H(X)=1$ bit. $H(X|Y)=h(\frac14)=\frac14\log_24+\frac34\log_2\frac43=0.5+0.75(0.41504)=0.81128$. So $I=1-0.81128=0.18872$ bit. ✓.

*Fano check (3.18).* The guess $\hat X=Y$ has $P_e=\frac14$, M = 2, so $F_2$ gives $P_e\log1+h(\frac14)=0.81128$. This equals $H(X|Y)$, so Fano is tight here.

## Concepts
- [[mutual information I(X;Y)]] — here defined as D(P_{X,Y}‖P_X P_Y), the general definition; equals H(X)−H(X|Y) for discrete X when H(X|Y)<∞ (p. 42, 44)
- [[relative entropy / KL divergence]] — the base object; its DPI and chain rule are used to prove Thms 3.2 and 3.7 (pp. 42, 52)
- [[joint and conditional entropy]] — $I+H(X|Y)=H(X)$ (3.2) (p. 44)
- [[chain rule]] — Kolmogorov identities for I; full form for $I(X^n;Y)$ (p. 51–52)
- [[data processing inequality]] — $I(X;Z)\le I(X;Y)$ for X→Y→Z; equality iff X→Z→Y (p. 52)
- [[Fano's inequality]] — $H(X|Y)\le P_e\log(M-1)+h(P_e)$ and the version (3.19) (p. 57)
- [[differential entropy]] — used for Gaussian examples and the EPI (pp. 44, 47, 64)
- [[noisy channel]] — Markov kernels AWGN, BI-AWGN, BSC (pp. 48–50)
- [[channel capacity]] — only mentioned: the Fig. 3.2 caption says these mutual informations will be shown to be the channels' capacities (p. 49)
- [[conditional-mutual-information]] (new) — $I(X;Y|Z)=\mathbb E_z I(X;Y|Z=z)$ (p. 50)
- [[sufficient-statistic]] (new) — T such that $P_{X|T}$ does not depend on θ; equivalent to equality in the DPI (p. 54)
- [[markov-chain-d-separation]] (new) — DAG language and d-connectedness for conditional independence (p. 51)
- [[strong-data-processing-inequality]] (new) — $I(U;Y)\le\eta_{KL}I(U;X)$ with $\eta_{KL}<1$ for many channels (p. 53)
- [[meta-converse]] (new) — prove a bound under an auxiliary Q, then transport it to P by the DPI (p. 57)
- [[i-mmse-relation]] (new) — $\frac d{d\gamma}I=\frac{\log e}2\mathrm{mmse}$ for Gaussian noise (p. 59)
- [[entropy-power-inequality]] (new) — $N(A_1+A_2)\ge N(A_1)+N(A_2)$ (p. 64)

## Canonical instances
- [[bivariate-gaussian-mi]] — $I=\frac12\log\frac1{1-\rho^2}$ (p. 47)
- [[awgn-channel]] — $I=\frac12\log(1+\mathrm{SNR})$ for Gaussian input (p. 48)
- [[bi-awgn-channel]] — binary input loses almost nothing at low SNR (p. 49)
- [[binary-symmetric-channel]] — $I=\log2-h(\delta)$ (p. 50)
- [[or-gate-conditioning]] — conditioning raises entropy for Y=0 but lowers it on average (p. 46)
- [[xor-conditioning-example]] — $I(X;Y|Z)>I(X;Y)$ with Y = X⊕Z (p. 52)
- [[normal-mean-sufficient-statistic]] — the sample mean is sufficient for the mean of $\mathcal N(\theta,1)$ (p. 55)

## Bridges (candidates)
- [same-math] Venn diagram / signed measure μ on sets ↔ combinatorics: inclusion–exclusion — information quantities become set operations (p. 46–47).
- [structural-analogy] I(X;Y) = −½ log(1−ρ²) for Gaussians ↔ statistics: correlation coefficient — both measure dependence, but I is bijection-invariant (p. 48).
- [structural-analogy] Sufficient statistic ↔ statistics: Fisher's sufficiency — equality in the DPI is the information-theoretic form (p. 54).
- [metaphor] Guerra interpolation in statistical physics ↔ vector-to-scalar derivative trick in the I-MMSE proof — the author notes this idea underlies both (p. 63).

## Questions this raises
- Why can the triple quantity $I(X_1;X_2;X_3)$ be negative, and what does that say about "information" as a measure?
- How tight is Fano's inequality, and what replaces it when X is continuous (Tao's inequality)?
- For which channels is $\eta_{KL}$ computable, and how much does it improve converse bounds?
- Is the I-MMSE identity special to Gaussian noise, or do other noise models give similar formulas?

## Exercises worth doing
The unit prints no numbered exercises. It refers to exercises elsewhere and poses in-text "why?" questions:
- (p. 46) Why can $I(X_1;X_2;X_3)$ be both positive and negative? — difficulty: medium
- (p. 49) Why does $\det\Sigma_{[\mathbf X,\mathbf X+\mathbf N]}=\det\Sigma_{\mathbf X}\det\Sigma_{\mathbf N}$? — difficulty: medium
- (p. 51) Ex. I.26–I.30 (referred to, not printed here): practising d-separation and Markov-chain equivalences — difficulty: medium
- (p. 57) Ex. I.25 (referred to): direct proofs of (3.15) and (3.19) — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 25. The chapter is numbered 3 on the pages (running section numbers 3.1–3.8), though the unit id says ch04. Running header on every page: "itbook-export CUP/HE2-design August 16, 2024".
- Misprint (p. 48): the Example 3.2 alternative proof writes $h(Y|X)=h(Y-X|X)=h(Z|X)$. For $Z=Y-\rho X$ this should read $Y-\rho X$.
- In Theorem 3.4(e), the equality condition is printed as "H(X|Y)=0 or H(Y|X)=0"; copied as printed.
- Theorem 3.9's "∀P_θ" is as printed; my gloss that θ is treated as random is an interpretation.
- The BI-AWGN integral on p. 49 uses σ where the text elsewhere has $\sigma_N$.
- Step (3.30) to (3.22) (the chain rule in a = 1/γ) and the algebra of $d(p\|1/M)$ are marked (added step) and are not printed. The (3.23) proof, (3.28), and the full Tao inequality are cited from elsewhere, not proved here.
- Step 3 of the EPI proof (cancellation of the Gaussian-noise entropy terms) is marked (added step) and is not printed.
