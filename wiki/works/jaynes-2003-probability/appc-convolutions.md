---
id: jaynes-2003-probability/appc-convolutions
work: jaynes-2003-probability
unit: Appendix C — Convolutions and cumulants
pages: 677-682
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Appendix C — Convolutions and cumulants

## L0 — One line
Cumulants are combinations of moments that add when functions are convolved; the (scaled) Taylor coefficients of the logarithm of the Fourier transform are additive and so are cumulants, and Jaynes argues they give all the independent ones.

## L1 — The gist (≤ 120 words)
Which combinations of moments add up under convolution? Jaynes finds by direct calculation that the first moment, the variance and a third combination are additive. He calls such quantities cumulants and notes that the notion has nothing, fundamentally, to do with probability. The Fourier transform turns convolution into multiplication, so its logarithm is additive. The Taylor coefficients of that logarithm are therefore cumulants. The first three equal the mean, the second central moment and the third central moment, but the fourth cumulant differs from the fourth central moment. A Gaussian has only two nontrivial cumulants, mean and variance. For probability densities, the first few cumulants give efficient approximations.

**Prerequisites:** double integrals and change of variables; Taylor series; complex exponential $e^{i\alpha x}$. Convolution: $(f_1*f_2)(x)=\int f_1(y)f_2(x-y)\,dy$. Moment: $\int x^nf(x)\,dx$. Central moment: moment about the mean. Fourier transform: $\int f(x)e^{i\alpha x}dx$.

## L2 — Key ideas
- Under convolution the zeroth moments multiply and, once each $Z_i=1$, the first moments add (p. 677).
- After subtracting lower-moment terms, $S-F^2$ and $T-3SF+2F^3$ also add. This generalizes to $n$ functions (p. 678).
- The Fourier transform of a convolution is the product of the transforms, so $\log\mathcal F(\alpha)$ is additive (p. 678).
- The coefficients $C_n=i^{-n}\,d^n\log\mathcal F/d\alpha^n$ at $\alpha=0$ are additive, hence cumulants. The term "cumulant" is often defined by this relation (p. 679).
- Jaynes argues that if all moments exist, the $C_i$ determine $f$, so they include all algebraically independent cumulants. If $f$ lacks moments of some order, he says the answer is not obvious and needs further investigation (p. 679).
- $C_1,C_2,C_3$ equal the mean and the second and third central moments. The fourth central moment is $C_4+3C_2^2$, so it is not a cumulant (p. 680).
- For a Gaussian, $\log\mathcal F$ is quadratic in $\alpha$, so all cumulants above $C_2$ vanish (p. 681).

## L3 — Walkthrough

**Setup (p. 677).** Take real functions $f_i$, not necessarily non-negative, with moments $Z_i=\int f_i$, $F_i=\int x f_i$, $S_i=\int x^2 f_i$, $T_i=\int x^3 f_i$ all finite (C.1). Convolution:
$$h(x)=\int_{-\infty}^{\infty}dy\,f_1(y)f_2(x-y)\tag{C.2}$$
It is associative, so $f_1*\dots*f_n$ is unambiguous.

**Moments under convolution.**
- Zeroth: $Z_h=\int dy\,f_1(y)Z_2=Z_1Z_2$ (C.3).
- If $Z_i\neq0$, rescale so that $Z_i=1$; this is preserved under convolution. Assume it from here on.
- First: substitute $q=x-y$.
$$F_h=\int dy\,f_1(y)\int dq\,(y+q)f_2(q)=F_1Z_2+Z_1F_2\tag{C.4}$$
so $F_h=F_1+F_2$ (C.5).
- Second:
$$S_h=\int dy\,f_1(y)\int dq\,(y^2+2yq+q^2)f_2(q)=S_1Z_2+2F_1F_2+Z_1S_2\tag{C.6}$$
so $S_h=S_1+2F_1F_2+S_2$ (C.7).
- Subtracting the square of (C.5), the cross term cancels:
$$S_h-F_h^2=(S_1-F_1^2)+(S_2-F_2^2)\tag{C.8}$$
(added step: $S_1+2F_1F_2+S_2-(F_1+F_2)^2=S_1-F_1^2+S_2-F_2^2$) (p. 678).
- Third: $T_h=T_1Z_2+3S_1F_2+3F_1S_2+Z_1T_2$ (C.9). After "some algebra", $T_h-3S_hF_h+2F_h^3$ is additive (C.10) (p. 678).
- For $h=f_1*\dots*f_n$ (C.11):
$$F_h=\sum_i F_i,\quad S_h-F_h^2=\sum_i (S_i-F_i^2),\quad T_h-3S_hF_h+2F_h^3=\sum_i(T_i-3S_iF_i+2F_i^3)$$

These additive quantities are the *cumulants*. Jaynes stresses that the notion is not fundamentally about probability. He asks: (1) do correction terms making higher moments additive always exist, and (2) how can they be constructed? (p. 678)

**Fourier route (p. 678).** Define
$$\mathcal F_i(\alpha)=\int dx\,f_i(x)e^{i\alpha x},\qquad f_i(x)=\frac1{2\pi}\int d\alpha\,\mathcal F_i(\alpha)e^{-i\alpha x}\tag{C.12}$$
Substituting $x=y+q$ in the transform of $h$:
$$\mathcal H(\alpha)=\int dy\,f_1(y)\int dq\,e^{i\alpha(y+q)}f_2(q)=\mathcal F_1(\alpha)\mathcal F_2(\alpha)\tag{C.13}$$
So $\log\mathcal F$ is additive under convolution.

*Intuition note:* Convolution is a messy integral, but its transform is a plain product. A logarithm turns a product into a sum, so every Taylor coefficient of $\log\mathcal F$ adds.

**Series (p. 679).**
$$\mathcal F(\alpha)=M_0+M_1(i\alpha)+M_2\frac{(i\alpha)^2}{2!}+M_3\frac{(i\alpha)^3}{3!}+\cdots\tag{C.14}$$
$$M_n=\frac1{i^n}\frac{d^n\mathcal F}{d\alpha^n}\Big|_{\alpha=0}=\int dx\,x^nf(x)\tag{C.15}$$
If $f$ has moments up to order $N$, $\mathcal F$ is differentiable $N$ times at the origin. Similarly:
$$\log\mathcal F(\alpha)=C_0+C_1(i\alpha)+C_2\frac{(i\alpha)^2}{2!}+\cdots,\qquad C_n=\frac1{i^n}\frac{d^n}{d\alpha^n}\log\mathcal F\Big|_{\alpha=0}\tag{C.16, C.17}$$
All $C_n$ are additive, hence cumulants. The term "cumulant" is often defined by (C.17).

First few:
- $C_0=\log\mathcal F(0)=\log Z$ (C.18).
- $C_1=F/Z$ (C.19).
- $C_2=\frac{d^2}{d(i\alpha)^2}\log\mathcal F=\dfrac{\int f\int x^2f-(\int xf)^2}{(\int f)^2}$ (C.20), i.e. $C_2=\dfrac SZ-\Big(\dfrac FZ\Big)^2$ (C.21).

$C_3$ and $C_4$ are said to follow "after some tedious calculation" (p. 679).

**Completeness question (p. 679).** Jaynes "would argue" that if all $C_i$ exist (all moments finite, $\mathcal F$ entire), the $C_i$ determine $\mathcal F$ and so $f$. Hence they include all algebraically independent cumulants, and any others must be linear functions of the $C_i$. If $f$ does not have moments of all orders, "the answer is not obvious" and further investigation is needed.

**C.1 Relation of cumulants and moments (pp. 679–680).** With $Z=1$, write $M_n=\int x^nf=\frac{d^n}{d(i\alpha)^n}\int f e^{i\alpha x}\big|_0=i^{-n}\mathcal F^{(n)}(0)$ (C.22), and $M_n=\overline{x^n}$ (C.23). Jaynes stresses that these are not in general probability averages, since $f$ need not be non-negative. Jaynes reserves $\langle x\rangle$ or $E(x)$ for probability averages (p. 680). If all moments exist, (C.24) as printed gives $\mathcal F(\alpha)=\sum_n M_n(i\alpha)^n$ (see Reading notes).

Relations:
- $C_1=M_1=\bar x$ (C.25).
- $C_2=M_2-M_1^2=\overline{(x-\bar x)^2}=\overline{x^2}-\bar x^2$ (C.26), the second central moment.
- The third central moment $\int(x-\bar x)^3f=\int[x^3-3\bar xx^2+3\bar x^2x-\bar x^3]f$ (C.27) equals $C_3=M_3-3M_1M_2+2M_1^3$ (C.28).
- One might conjecture that all cumulants are central moments, but this fails. The fourth central moment is
$$\overline{(x-\bar x)^4}=M_4-4M_3M_1+6M_2M_1^2-3M_1^4\tag{C.29}$$
while
$$C_4=M_4-4M_3M_1-3M_2^2+12M_2M_1^2-6M_1^4\tag{C.30}$$
so
$$\overline{(x-\bar x)^4}=C_4+3C_2^2\tag{C.31}$$
The fourth central moment is therefore not a linear function of cumulants. For $n=1,\dots,4$, moments up to order $n$ and cumulants up to order $n$ determine each other. Whether this holds for all $n$ is left to the reader (p. 680). Jaynes adds that if the functions are probability densities, many useful approximations are written most efficiently in terms of the first few terms of a cumulant expansion (p. 680).

*Intuition note:* Cumulants are moments with terms from lower moments subtracted so that the result adds under convolution. $C_1$ is the mean, and $C_2$ and $C_3$ coincide with the second and third central moments. At order 4, the second cumulant still contributes a $3C_2^2$ term to the central moment.

**C.2 Examples (pp. 680–681).** Gaussian $f(x)=(2\pi\sigma^2)^{-1/2}\exp\{-[x-\mu]^2/2\sigma^2\}$ (C.32). Then $\mathcal F(\alpha)=\exp\{i\alpha\mu-\alpha^2\sigma^2/2\}$ (C.33), so $\log\mathcal F=i\alpha\mu-\alpha^2\sigma^2/2$ (C.34). Hence $C_0=0$, $C_1=\mu$, $C_2=\sigma^2$, and all higher $C_n=0$ (C.35). A Gaussian is characterized by having only two nontrivial cumulants, the mean and the variance (p. 681).

## Toy example (ours)
Take $f_1=f_2=e^{-x}$ for $x>0$ (zero otherwise). Then $Z=1$, $F=1$, $S=2$, $T=6$.
- Each function: $S-F^2=1$ and $T-3SF+2F^3=6-6+2=2$.
- Convolution $h=f_1*f_2$. By (C.5), $F_h=1+1=2$. By (C.7), $S_h=2+2\cdot1\cdot1+2=6$. By (C.9), $T_h=6+3\cdot2\cdot1+3\cdot1\cdot2+6=24$.
- Check: $S_h-F_h^2=6-4=2=1+1$ ✓. $T_h-3S_hF_h+2F_h^3=24-36+16=4=2+2$ ✓.

## Concepts
- [[convolution]] (new) — $h(x)=\int f_1(y)f_2(x-y)\,dy$; defined for general real functions, not only densities (p. 677)
- [[moment]] (new) — $M_n=\int x^nf(x)\,dx$; "average" here need not be a probability average (pp. 677, 680)
- [[cumulant]] (new) — moment corrected by lower moments so it is additive under convolution; equivalently $C_n=i^{-n}\,d^n\log\mathcal F/d\alpha^n$ at 0 (pp. 678–679)
- [[fourier-transform-characteristic-function]] (new) — $\mathcal F(\alpha)=\int f e^{i\alpha x}dx$; turns convolution into a product (p. 678)
- [[central-moment]] (new) — moment about the mean; the second and third central moments equal $C_2$ and $C_3$, but the fourth does not equal $C_4$ (p. 680)

## Canonical instances
- [[gaussian-cumulants]] — only $C_1=\mu$ and $C_2=\sigma^2$ are nontrivial; all higher $C_n$ vanish (p. 681)
- [[fourth-central-moment-vs-cumulant]] — $\overline{(x-\bar x)^4}=C_4+3C_2^2$ (p. 680)

## Bridges (candidates)
- [same-math] additivity of cumulants under convolution ↔ bayesian/probability: if the density of a sum of independent variables is the convolution of their densities, cumulants add. The text itself keeps the algebra probability-free.
- [structural-analogy] $\log\mathcal F$ additive under convolution ↔ signal processing: the "cepstrum", mentioned (p. 678) but not developed here.
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints.

## Questions this raises
- Do moments up to order $n$ and cumulants up to order $n$ determine each other for every $n$? (Left to the reader, p. 680.)
- What happens to the completeness argument when $f$ lacks moments of some order? (p. 679)
- How do the first few cumulants truncate a cumulant expansion of a density as an approximation? (Mentioned, p. 680.)

## Reading notes
- Printed page = pdf − 30. The last pdf page (712/682) is blank.
- (C.24) prints $\mathcal F(\alpha)=\sum M_n(i\alpha)^n$ without the $1/n!$ that appears in (C.14). This looks like a misprint, and I did not correct it in the formula. (C.22) writes the limit as "$\alpha=o$".
- p. 679 says $C_3$ and $C_4$ equal "the third and fourth cumulants (C.10)", but (C.10) gives only the third.
- p. 680 refers to the third cumulant as "(C.11)"; the third-cumulant expression is in (C.10) and (C.11).
- Jaynes states the third-moment additivity (C.10) and the $C_3$, $C_4$ identifications without full algebra. They are not re-derived here.
