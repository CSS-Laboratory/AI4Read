---
id: polyanskiy-2025-information/ch13-fixed
work: polyanskiy-2025-information
unit: "Chapter 11 (printed numbering; unit id ch13-fixed): Fixed-length compression and Slepian-Wolf theorem"
pages: 212-229
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Fixed-length compression and Slepian-Wolf theorem

## L0 — One line
If a small error probability is tolerated, fixed-length compression reaches the entropy $H(S)$ per symbol, and random hashing lets a decompressor holding side information $Y$ get away with only $H(X|Y)$ bits, even though the compressor never sees $Y$.

## L1 — The gist (≤ 120 words)
Question: how many bits $k$ are needed if the compressor's output must have fixed length and a small error probability is allowed? Answer: for iid sources, $k/n \to H(S)$. The chapter gives exact and finite-blocklength formulas, then random coding, the asymptotic equipartition property (AEP) and linear (matrix) hashing as ways to achieve this. With side information $Y$ at the decompressor only, the rate $H(X|Y)$ is still achievable (Slepian-Wolf). For two sources compressed separately, the rate region is characterised. Finally, a rate-limited helper describing $Y$ is treated (Ahlswede-Körner-Wyner). This matters because random coding is the proof technique reused for channel coding and lossy compression.

**Prerequisites:** entropy and conditional entropy; mutual information; weak law of large numbers; union bound; basic linear algebra over a field; Fano's inequality.

## L2 — Key ideas
- Allowing error $\epsilon$ makes fixed-length coding possible: the best code keeps the $2^k-1$ most likely symbols and sends everything else to an error symbol. For $\mathcal X=\mathbb N$ with $P_X(1)\ge P_X(2)\ge\cdots$ this gives $\epsilon^*(X,k)=\sum_{x\ge 2^k}P_X(x)$ (p. 213).
- For iid sources, $\epsilon^*(S^n,nR)\to 0$ if $R>H(S)$ and $\to1$ if $R<H(S)$. If the varentropy $V(S)$ (from the previous chapter) is finite, then at non-vanishing error $\epsilon$, asymptotically $k=nH(S)+\sqrt{nV(S)}\,Q^{-1}(\epsilon)$ bits are enough, where $Q$ is the Gaussian tail function (p. 214).
- Random coding: hash each $x$ to a random $k$-bit string. At most $2^{k-\tau}$ high-probability inputs exist, so collisions are rare, and some codebook is at least as good as average (pp. 215–217).
- AEP: iid sequences concentrate on a typical set of size at most $e^{(H+\delta)n}$, on which $P_{S^n}$ is nearly uniform (p. 218).
- Linear hashing $w=Hx$ over a finite field achieves a bound of the same form; the proof needs only the collision probability $q^{-k}$ between two different inputs (Remark 11.3 notes that random coding needs only pairwise independence). In general the argument does not carry over to rings with zero divisors, which ruin the low collision probability (pp. 217–221).
- Slepian-Wolf: side information at the decompressor only costs nothing in rate, $H(X|Y)$. This depends on undetectable errors being allowed (pp. 223–224).
- Two separately compressed correlated sources have rate region $a\ge H(S|T)$, $b\ge H(T|S)$, $a+b\ge H(S,T)$ (p. 225).
- With a rate-limited helper, the achievable rate pairs $(R_1,R_2)$ are those with $R_1\ge H(X|U)$, $R_2\ge I(Y;U)$ for some $U$ with $X\to Y\to U$ (p. 227).

## L3 — Walkthrough

### 11.1 Source coding theorems
Setting: $f:\mathcal X\to\{0,1\}^k$, $g:\{0,1\}^k\to\mathcal X\cup\{e\}$ ($e$ = "error" symbol). Demanding $g(f(X))=X$ with probability one forces $k\ge\log_2|\mathrm{supp}(P_X)|$, so no useful compression (p. 212). Instead, require lossless decoding only on a subset $\mathcal S$; the error probability is $P[X\notin\mathcal S]$ (p. 213).

**Definition 11.1.** A $(k,\epsilon)$-code has $g(f(x))\in\{x,e\}$ for all $x$ and $P[g(f(X))=e]\le\epsilon$. Fundamental limit: $\epsilon^*(X,k)\triangleq\inf\{\epsilon:\exists (k,\epsilon)\text{-code}\}$ (p. 213).

**Theorem 11.2.** Let $\mathcal X=\mathbb N$ with $P_X(1)\ge P_X(2)\ge\cdots$, and $f^*$ the optimal variable-length compressor of Theorem 10.2. Then
$$\epsilon^*(X,k)=P[l(f^*(X))\ge k]=\sum_{x\ge 2^k}P_X(x).$$
Proof: one $k$-bit string must be reserved for $e$. Since $1+2+\dots+2^{k-1}=2^k-1$, take $\mathcal S$ = the $2^k-1$ most likely elements; then $\epsilon^*=P[X\notin\mathcal S]=P[l(f^*(X))\ge k]$ by (10.1) (p. 213). Optimal fixed-length code: $\mathcal S$ goes to $00\ldots0,\dots,11\ldots10$; all else to $11\ldots1$, which $g$ decodes as $e$ (p. 213).

**Remark 11.1 (undetectable errors).** If errors need not be detectable, define $\tilde\epsilon^*(X,k)=\inf P[g(f(X))\ne X]$. Then $\tilde\epsilon^*(X,k)=\sum_{x>2^k}P_X(x)$, because $\mathcal S=\{x:g(f(x))=x\}$ has $|\mathcal S|\le 2^k$. It differs from $\epsilon^*$ by $P_X(2^k)\le 2^{-k}$, and $\epsilon^*(X,k+1)\le\tilde\epsilon^*(X,k)\le\epsilon^*(X,k)$: at most one bit is saved (p. 214).

**Corollary 11.3 (Shannon).** For iid $S^n$ and $R>0$: $\lim_n\epsilon^*(S^n,nR)=0$ if $R>H(S)$, $=1$ if $R<H(S)$. If the varentropy $V(S)<\infty$, then $\lim_n\epsilon^*(S^n,nH(S)+\sqrt{nV(S)}\gamma)=Q(\gamma)$, with $Q(x)=\int_x^\infty\frac1{\sqrt{2\pi}}e^{-t^2/2}dt$. Proof: Theorem 11.2 with Corollary 10.5 (p. 214). Hence the minimal $k$ with vanishing error has $k/n\to H(S)$; with error $\epsilon$ non-vanishing, $k=nH(S)+\sqrt{nV(S)}Q^{-1}(\epsilon)$ suffices (the "normal approximation") (p. 214).

> *Intuition note.* The best fixed-length code is a lookup table of the most likely messages, and everything else is given up. For long iid blocks the probability left outside the table is tiny once $k$ exceeds $nH(S)$, and near one below it.

**Theorem 11.4 (finite blocklength).** For all $\tau>0$, $k\in\mathbb Z_+$:
$$P\Big[\log_2\tfrac1{P_X(X)}>k+\tau\Big]-2^{-\tau}\le\tilde\epsilon^*(X,k)\le\epsilon^*(X,k)\le P\Big[\log_2\tfrac1{P_X(X)}\ge k\Big].$$
Converse: for the optimal code, $\mathcal S=\{x:g(f(x))=x\}$,
$1-\tilde\epsilon^*=P[X\in\mathcal S]\le P[\log_2\frac1{P_X(X)}\le k+\tau]+P[X\in\mathcal S,\log_2\frac1{P_X(X)}>k+\tau]$. The second term is $\sum_{x\in\mathcal S}P_X(x)1\{P_X(x)<2^{-k-\tau}\}\le|\mathcal S|2^{-k-\tau}\le2^{-\tau}$. Upper bound: sort the masses, use Theorem 11.2 and $P_X(m)\le 1/m$ for the $m$-th largest mass: $\epsilon^*=\sum_{m\ge2^k}P_X(m)\le\sum1\{\frac1{P_X(m)}\ge2^k\}P_X(m)=P[\log_2\frac1{P_X(X)}\ge k]$ (p. 215).

**Theorem 11.5 (random coding achievability).** For any $k\in\mathbb Z_+$ and all $\tau>0$,
$$\tilde\epsilon^*(X,k)\le P\Big[\log_2\tfrac1{P_X(X)}>k-\tau\Big]+2^{-\tau}.\tag{11.1}$$
The author calls this weaker than Theorem 11.4 with a longer proof, but it introduces random coding (probabilistic method), which later drives Slepian-Wolf, data transmission (Part IV) and lossy compression (Part V) (p. 215).

Proof. For a given $f$ the optimal decoder is MAP: $g^*(w)=\arg\max_{x:f(x)=w}P_X(x)$. It is hard to analyse, so use instead $g(w)=x$ if there is a unique $x$ with $f(x)=w$ and $\log_2\frac1{P_X(x)}\le k-\tau$ (equivalently $P_X(x)\ge2^{-(k-\tau)}$, called "high-probability"), else $e$ (p. 216). Write $f(x)=c_x$; the vector $\mathcal C=[c_x]$ is a codebook (a hash table). Let
$J(x,\mathcal C)=\{x'\ne x:c_{x'}=c_x,\ \log_2\frac1{P_X(x')}\le k-\tau\}$ (high-probability inputs colliding with $x$). Then
$$P[g(f(X))=e]\le P\Big[\log_2\tfrac1{P_X(X)}>k-\tau\Big]+P[J(X,\mathcal C)\ne\emptyset].$$
The first term is independent of $\mathcal C$. Draw each $c_x$ iid $\mathrm{Unif}\{0,1\}^k$, independent of $X$ (an $|\mathcal X|\times k$ matrix of fair coins). Then
$$E_{\mathcal C}P[J\ne\emptyset]\le E_{\mathcal C,X}\sum_{x'\ne X}1\{P_X(x')\ge2^{-k+\tau}\}1\{c_{x'}=c_X\}\ \text{(union bound)}=2^{-k}E_X\sum_{x'\ne X}1\{P_X(x')\ge2^{-k+\tau}\}\le2^{-k}\sum_{x'\in\mathcal X}1\{\cdot\}\le2^{-k}2^{k-\tau}=2^{-\tau},$$
using that at most $2^{k-\tau}$ values $x'$ have $P_X(x')>2^{-k+\tau}$ (p. 216). Since the average over codebooks meets the bound, some codebook does (p. 216).

> *Intuition note.* Only few inputs are likely (at most $2^{k-\tau}$), and they are scattered among $2^k$ labels. A random label assignment therefore rarely makes two likely inputs collide.

**Remark 11.2.** The argument is non-constructive: a random table needs much randomness and storage (p. 217). **Remark 11.3.** Only pairwise independence $c_x\perp c_{x'}$ ($x\ne x'$) was used (the author says "exercise!"). From independent bits $B_1,B_2$, the three bits $B_1,B_2,B_1\oplus B_2$ are pairwise independent. This motivates linear compression (p. 217).

### 11.2 Asymptotic equipartition property (AEP)
**Proposition 11.6.** For iid $S^n$ and $\delta>0$, define the entropy $\delta$-typical set $T_\delta^n=\{s^n:|\frac1n\log\frac1{P_{S^n}(s^n)}-H(S)|\le\delta\}$. Then (1) $P[S^n\in T^n_\delta]\to1$; (2) $|T^n_\delta|\le\exp\{(H(S)+\delta)n\}$ (pp. 217–218).
Example: for $S_i\sim\mathrm{Ber}(p)$, $P_{S^n}(s^n)=p^{w_H(s^n)}\bar p^{\,n-w_H(s^n)}$, so typical means Hamming weight fraction near $p$ (p. 218).
Proof: the WLLN gives $\frac1n\log\frac1{P_{S^n}(S^n)}\xrightarrow{P}H(S)$ (11.2), hence (1). Every $s^n\in T^n_\delta$ has $P_{S^n}(s^n)>\exp\{-(H(S)+\delta)n\}$, so there are at most $\exp\{(H+\delta)n\}$ of them (p. 218). On $T^n_\delta$, $P_{S^n}(s^n)=\exp\{-nH(S)\pm n\delta\}$ (nearly uniform).

Third proof of Shannon's theorem: let $f$ enumerate $T^n_\delta$ with strings of $\{0,1\}^{nR}$. If $R>H(S)+\delta$, error is $P[S^n\notin T^n_\delta]\to0$. If $R<H(S)$, $2^{nR}$ strings cover no significant part of the almost uniform $T^n_\delta$, so the error tends to 1 (exponentially fast). This explains why the optimal compressor's output looks like iid Ber(1/2) (p. 218).

> *Intuition note.* Almost all probability sits on exponentially few sequences, all about equally likely. Compressing then means numbering these sequences.

### 11.3 Linear compression (hashing)
The previous proofs need sorting, a huge table, or enumerating $T^n_\delta$ (p. 218). Now the source is $X=S^n$ with $S_i\in\mathbb F_q$, a finite field ($q=p^k$ for a prime $p$) (p. 219). **Definition 11.7:** a Galois field has $+$ and $\cdot$ associative and commutative, elements $0,1$ with $0+a=1\cdot a=a$, additive inverses, multiplicative inverses for $a\ne0$, and distributivity. Examples: $\mathbb F_p=\mathbb Z/p\mathbb Z$; $\mathbb F_4=\{0,1,x,x+1\}$ with polynomial arithmetic in $\mathbb F_2[x]$ modulo $x^2+x+1$ (p. 219).

A linear compressor is $w=Hx$ with $H\in\mathbb F_q^{k\times n}$ ($x$: $n\times1$, $w$: $k\times1$). Compression needs $k<n$ (a "fat" matrix) (p. 219).

**Theorem 11.8.** For $X\in\mathbb F_q^n$ and all $\tau>0$ there exist a linear compressor $H$ and decompressor $g$ with undetectable error
$$P[g(HX)\ne X]\le P\Big[\log_q\tfrac1{P_X(X)}>k-\tau\Big]+q^{-\tau}.$$
(The theorem prints $H\in\mathbb F_q^{n\times k}$; the matrix is $k\times n$.) **Remark 11.4:** for $q=2$ a fully random codebook costs $k2^n$ random bits; a random $H$ costs $kn$ bits, and the codebook is a $k$-dimensional linear subspace (p. 219).

Proof. Same suboptimal decoder as Theorem 11.5: output the unique $x$ with $Hx=w$ that is high-probability ($\log_q\frac1{P_X(x)}\le k-\tau$), else $e$ (p. 220). Union bound twice:
$$P[g(HX)\ne X|H]\le P\Big[\log_q\tfrac1{P_X(X)}>k-\tau\Big]+\sum_xP_X(x)\sum_{x'\text{ h.p.},x'\ne x}1\{Hx'=Hx\}.$$
Take $H$ with iid uniform entries. For $x_0\ne x_1$, with $x_2=x_1-x_0\ne0$:
$P[Hx_1=Hx_0]=P[Hx_2=0]=P[H_1\cdot x_2=0]^k$ ($H_1$ = first row; rows iid). The vectors orthogonal to a nonzero $x_2$ number $q^{n-1}$, so a row lies there with probability $q^{n-1}/q^n=1/q$; the collision probability is $q^{-k}$. Hence
$E_H\sum_{x'\text{ h.p.},x'\ne x}1\{Hx'=Hx\}=|\{x'\text{ h.p.},x'\ne x\}|q^{-k}\le q^{k-\tau}q^{-k}=q^{-\tau}$ (p. 220).

Errors: the non-linear construction of Theorem 11.5 can be modified to make all errors detectable (e.g. increase $k$ by 1 and set the first bit to 1 for low-probability $x$). For linear compressors, errors cannot be made detectable (p. 220). **Rings:** over $\mathbb Z/6\mathbb Z$ the argument fails because of zero divisors: $P[H(1,0,\dots,0)^\top=0]=6^{-k}$ but $P[H(2,0,\dots,0)^\top=0]=3^{-k}$, since $0\cdot2=3\cdot2=0$ (pp. 220–221).

> *Intuition note.* A random matrix collides two different inputs with probability exactly $q^{-k}$, the same as a random table. So the cheap random linear map works just as well in the proof.

### 11.4 Side information at both compressor and decompressor
**Definition 11.9.** $f:\mathcal X\times\mathcal Y\to\{0,1\}^k$, $g:\{0,1\}^k\times\mathcal Y\to\mathcal X\cup\{e\}$, error $P[g(f(X,Y),Y)\ne X]<\epsilon$; limit $\epsilon^*(X|Y,k)$. $Y$ need not be discrete. Given $Y=y$ both sides use the best code for $P_{X|Y=y}$, so $\epsilon^*(X|Y,k)=E_{y\sim P_Y}[\epsilon^*(P_{X|Y=y},k)]$ (p. 221).

**Theorem 11.10.** $P[\log\frac1{P_{X|Y}(X|Y)}>k+\tau]-2^{-\tau}\le\epsilon^*(X|Y,k)\le P[\log_2\frac1{P_{X|Y}(X|Y)}>k-\tau]+2^{-\tau}$ for all $\tau>0$ (p. 222).
**Corollary 11.11.** For iid pairs $(S_i,T_i)$: $\lim_n\epsilon^*(S^n|T^n,nR)=0$ if $R>H(S|T)$, $1$ if $R<H(S|T)$. Proof: WLLN gives $\frac1n\sum_i\log\frac1{P_{S|T}(S_i|T_i)}\xrightarrow{P}H(S|T)$ (p. 222).

### 11.5 Slepian-Wolf: side information at decompressor only
**Definition 11.12.** $f:\mathcal X\to\{0,1\}^k$ (no access to $Y$), $g:\{0,1\}^k\times\mathcal Y\to\mathcal X\cup\{e\}$, error $\le\epsilon$; limit $\epsilon^*_{SW}(X|Y,k)$ (p. 222).

**Theorem 11.13 (Slepian-Wolf).**
$$\epsilon^*(X|Y,k)\le\epsilon^*_{SW}(X|Y,k)\le P\Big[\log\tfrac1{P_{X|Y}(X|Y)}\ge k-\tau\Big]+2^{-\tau}.$$
**Corollary 11.14:** $\lim_n\epsilon^*_{SW}(S^n|T^n,nR)=0$ for $R>H(S|T)$, $1$ for $R<H(S|T)$. $T$ need not be discrete (Exercise II.9, referenced) (p. 223).

Proof. Left inequality: side information at both ends is at least as good. Right: random codebook $c_x$ iid uniform, independent of $(X,Y)$; $f(x)=c_x$; $g(w,y)=x$ if there is a unique $x$ with $c_x=w$ and $x$ "h.p.$|y$" ($\log_2\frac1{P_{X|Y}(x|y)}<k-\tau$), else a default output (printed as $0$). With $J(x,\mathcal C|y)=\{x'\ne x:x'\text{ h.p.}|y,\ c_x=c_{x'}\}$,
$$P[X\ne g(f(X))|\mathcal C]\le P\Big[\log\tfrac1{P_{X|Y}(X|Y)}\ge k-\tau\Big]+\sum_{x,y}P_{X,Y}(x,y)1\{J(x,\mathcal C|y)\ne\emptyset\}.$$
Averaging over $\mathcal C$: (a) union bound, (b) at most $2^{k-\tau}$ values $x'$ are h.p.$|y$, (c) $P[c_{x'}=c_x]=2^{-k}$:
$P[J(x,\mathcal C|y)\ne\emptyset]\le E_{\mathcal C}\sum_{x'\ne x}1\{x'\text{ h.p.}|y\}1\{c_{x'}=c_x\}\le2^{k-\tau}2^{-k}=2^{-\tau}$ (pp. 223–224).

> *Intuition note.* The encoder hashes $x$ blindly, but given $y$ at most $2^{k-\tau}$ candidates for $x$ are plausible (high probability given $y$). Each shares the true $x$'s hash value with probability $2^{-k}$, so the decoder can usually pick out the right one.

**Remark 11.5.** This depends on undetectable errors. Suppose $g(f(x),y)\in\{x,e\}$ is required for all $(x,y)$ with $P_{X,Y}>0$. If $f(x_1)=f(x_2)=c$, the author says $g(c,y)=e$ for all $y$; if $c$ has a unique preimage, $y$ can be ignored. In either case, side information is not useful and one can only reach $H(X)$, not $H(X|Y)$. The author adds that one can show Slepian-Wolf also fails for variable-length lossless compression: the minimal average length is at least $H(X)$ (p. 224).

### 11.6 Slepian-Wolf: compressing multiple sources
**Definition 11.15.** Separate compressors $f_1:\mathcal X\to\{0,1\}^{k_1}$, $f_2:\mathcal Y\to\{0,1\}^{k_2}$; joint decompressor $g$ must output $(X,Y)$; error $\le\epsilon$; limit $\epsilon^*_{SW}(X,Y,k_1,k_2)$ (p. 225).

**Theorem 11.16.** For iid $(S_i,T_i)$: $\lim_n\epsilon^*_{SW}(S^n,T^n,nR_1,nR_2)=0$ if $(R_1,R_2)\in\mathrm{int}(\mathcal R_{SW})$, $=1$ if $(R_1,R_2)\notin\mathcal R_{SW}$, where
$$\mathcal R_{SW}=\{(a,b):a\ge H(S|T),\ b\ge H(T|S),\ a+b\ge H(S,T)\}.$$
The region's boundary has slope $-1$ since $H(T)-H(T|S)=H(S)-H(S|T)=I(S;T)$ (p. 225).

Converse: if $(R_1,R_2)\notin\mathcal R_{SW}$, one case holds. (1) $R_1<H(S|T)$: even with $T^n$ at encoder and decoder, error does not vanish (Cor. 11.11). (2) $R_2<H(T|S)$: same. (3) $R_1+R_2<H(S,T)$: this would compress the pair below $H(S,T)$, contradicting Cor. 11.3 (p. 225).

Achievability (p. 226). Corner point $(H(S),H(T|S))$: let $k_1=n(H(S)+\delta)$, $k_2=n(H(T|S)+\delta)$. By Cor. 11.3 there are $f_1,g_1$ with $P[g_1(f_1(S^n))\ne S^n]\le\epsilon_n\to0$; by Theorem 11.13 there are $f_2,g_2$ with $P[g_2(f_2(T^n),S^n)\ne T^n]\le\epsilon_n\to0$. Define $g(w_1,w_2)=(g_1(w_1),g_2(w_2,g_1(w_1)))$. Union bound:
$P[g(f_1(S^n),f_2(T^n))\ne(S^n,T^n)]\le P[g_1(f_1(S^n))\ne S^n]+P[g_2(f_2(T^n),S^n)\ne T^n]\le2\epsilon_n\to0.$
The other corner is obtained "similarly". **Time sharing:** if $(R_1,R_2)$ and $(R_1',R_2')$ are achievable, use the first code on the first $\lambda n$ symbols and the second on the remaining $\bar\lambda n$. This gives $(\lambda R_1+\bar\lambda R_1',\lambda R_2+\bar\lambda R_2')$; so the region is convex.

> *Intuition note.* Each source can be compressed without seeing the other, yet the total rate need only be the joint entropy. The corner points are "compress one source fully, the other given it"; time sharing fills the line between them.

### 11.7* Source coding with a helper (Ahlswede-Körner-Wyner)
Now $Y$ is sent over a rate-limited link and the decompressor needs only $\hat X$. What must be sent is the part of $Y$ most useful for $X$. This was resolved independently in two works (p. 227).

**Theorem 11.17.** Iid $(X^n,Y^n)\sim P_{X,Y}$, $X$ discrete; $W_1=f_1(X^n)$, $W_2=f_2(Y^n)$ with at most $nR_i$ bits; $\hat X^n=g(W_1,W_2)$. If $(R_1,R_2)$ is achievable with $P[\hat X^n\ne X^n]\to0$, then there is an auxiliary $U$ with alphabet size $|\mathcal Y|+1$, $X\to Y\to U$ ($P_{X,Y,U}=P_{X,Y}P_{U|Y}$), and
$$R_1\ge H(X|U),\quad R_2\ge I(Y;U).\tag{11.3}$$
Conversely, for every such $U$, $(H(X|U),I(Y;U))$ is achievable. The region is $\cup_{P_{U|Y}}\{[H(X|U),\infty)\times[I(Y;U),\infty)\}$ (p. 227).

Converse. The set of pairs satisfying (11.3), over all $U$ without cardinality limit, is convex. Fano's inequality (3.19) with error $o(1)$ gives $H(X^n|W_1,W_2)=o(n)$. Then
$$nR_1\ge I(X^n;W_1|W_2)\ge H(X^n|W_2)-o(n)\tag{11.4}$$
$$=\sum_{k=1}^nH(X_k|W_2,X^{k-1})-o(n)\tag{11.5}$$
$$\ge\sum_{k=1}^nH(X_k|\underbrace{W_2,X^{k-1},Y^{k-1}}_{\triangleq U_k})-o(n)\tag{11.6}$$
and, from (6.2),
$$nR_2\ge I(W_2;Y^n)=\sum_kI(W_2;Y_k|Y^{k-1})\tag{11.7}$$
$$=\sum_kI(W_2,X^{k-1};Y_k|Y^{k-1})\tag{11.8}$$
$$=\sum_kI(W_2,X^{k-1},Y^{k-1};Y_k).\tag{11.9}$$
(11.8) uses $I(W_2,X^{k-1};Y_k|Y^{k-1})=I(W_2;Y_k|Y^{k-1})+I(X^{k-1};Y_k|W_2,Y^{k-1})$ and $(W_2,Y_k)\perp X^{k-1}|Y^{k-1}$; (11.9) uses $Y^{k-1}\perp Y_k$. With $U_k=(W_2,X^{k-1},Y^{k-1})$: $X_k\to Y_k\to U_k$ and $(R_1,R_2)\ge\frac1n\sum_k(H(X_k|U_k),I(U_k;Y_k))$, so by convexity the pair lies in the region. The alphabet bound $|\mathcal Y|+1$ follows from Carathéodory's theorem (Lemma 7.14); details omitted (p. 228).

Achievability. If the decoder had an iid sequence $U^n$ correlated with $X^n$, Slepian-Wolf would need only $R_1=H(X|U)$. Sending $U^n$ exactly costs $nH(U)$ bits, but $nI(U;X)$ bits suffice to send a "fake" jointly typical $\hat U^n$ with $P_{X^n|\hat U^n}\approx P_{X^n|U^n}$; this is the covering lemma (Corollary 25.6, studied later) (p. 228). By Cor. 25.6 and Prop. 25.7, for each $\delta>0$ there are $m$ and $\hat U^m=f_2(Y^m)\in\{0,1\}^{mR_2}$ with $X^m\to Y^m\to\hat U^m$ and $I(X^m;\hat U^m)\ge m(I(X;U)-\delta)$, i.e. $H(X^m|\hat U^m)\le mH(X|U)+m\delta$. Apply Slepian-Wolf to block symbols $\tilde X=X^m$, $\tilde U=\hat U^m$: for large $\ell$ there is $f_1$ with rate $\tilde R_1\le H(\tilde X|\tilde U)+m\delta\le mH(X|U)+2m\delta$. With $n=\ell m$, $R_1=\tilde R_1/m\le H(X|U)+2\delta$. Since $\delta$ is arbitrary, done (p. 229).

> *Intuition note.* The helper need not describe $Y$; it describes a compressed version $U$ of $Y$. Its cost is rate $I(Y;U)$, and the gain for the decoder is that $X$ then needs only rate $H(X|U)$.

## Toy example (ours, not from the text)
Binary pair $(S,T)$ with $P(0,0)=P(1,1)=0.4$, $P(0,1)=P(1,0)=0.1$. Then $P(S=0)=P(T=0)=0.5$, so $H(S)=H(T)=1$ bit.
- $H(S,T)=-2(0.4\log_20.4)-2(0.1\log_20.1)=0.8(1.3219)+0.2(3.3219)=1.0575+0.6644=1.7219$.
- $H(S|T)=H(T|S)=H(S,T)-1=0.7219$; $I(S;T)=1-0.7219=0.2781$.
- By Theorem 11.16 the region is $a\ge0.7219$, $b\ge0.7219$, $a+b\ge1.7219$. Corners: $(0.7219,1)$ and $(1,0.7219)$.
- $(0.9,0.9)$: sum $1.8\ge1.7219$, both coordinates $\ge0.7219$, so interior and achievable. Each source is compressed separately below 1 bit/symbol.
- $(0.8,0.8)$: sum $1.6<1.7219$, so not achievable.
- If $T^n$ is known only at the decoder, Cor. 11.14 says $S^n$ can still be sent at any rate above $0.7219$ bits/symbol. For $n=100$, about 73 bits instead of 100.

## Concepts
- [[source-coding-theorem]] — fixed-length version: $\epsilon^*(S^n,nR)\to0$ if $R>H(S)$, $\to1$ if $R<H(S)$ (p. 214)
- [[fixed-length-almost-lossless-code]] (new) — $(k,\epsilon)$-code: $k$-bit outputs, decoding is $x$ or $e$, error $\le\epsilon$ (p. 213)
- [[typical-set-aep]] — $T^n_\delta$: sequences with $|\frac1n\log\frac1{P}-H|\le\delta$; probability $\to1$, size $\le e^{(H+\delta)n}$ (p. 217)
- [[random-coding]] (new) — pick the codebook at random and show the average error is small, so a good code exists; non-constructive (pp. 215, 217)
- [[linear-compression-hashing]] (new) — compress by $w=Hx$ over a finite field; needs only pairwise independence (pp. 217, 219)
- [[varentropy-normal-approximation]] (new) — with varentropy $V$, $k=nH+\sqrt{nV}Q^{-1}(\epsilon)$ at error $\epsilon$ (p. 214)
- [[joint-conditional-entropy]] — $H(S|T)$ is the optimal rate with side information at both ends (p. 222)
- [[slepian-wolf-theorem]] (new) — decompressor-only side information still allows rate $H(X|Y)$ (p. 223)
- [[slepian-wolf-rate-region]] (new) — $\mathcal R_{SW}$: $a\ge H(S|T)$, $b\ge H(T|S)$, $a+b\ge H(S,T)$ (p. 225)
- [[time-sharing]] (new) — split the block to get convex combinations of achievable rate pairs (p. 226)
- [[compression-with-helper]] (new) — region $\cup_U[H(X|U),\infty)\times[I(Y;U),\infty)$, $X\to Y\to U$ (p. 227)
- [[mutual-information]] — $H(T)-H(T|S)=H(S)-H(S|T)=I(S;T)$ is why the sloped boundary of the Slepian-Wolf region has slope $-1$; $I(Y;U)$ is the helper's rate (pp. 225, 227)
- [[fanos-inequality]] — used in the converse of Theorem 11.17 (p. 227)

## Canonical instances
- [[ber-p-typical-set]] — typical sequences have Hamming weight fraction near $p$ (p. 218)
- [[pairwise-independent-bits]] — $B_1,B_2,B_1\oplus B_2$ are pairwise independent (p. 217)
- [[z6z-zero-divisor-failure]] — over $\mathbb Z/6\mathbb Z$, collision probabilities are $6^{-k}$ vs $3^{-k}$ (p. 221)
- [[galois-field-examples]] — $\mathbb F_p$ and $\mathbb F_4$ (p. 219)

## Bridges (candidates)
- [structural-analogy] random hash tables with pairwise-independent codewords ↔ computer science: universal hashing — collision probability $q^{-k}$ is what the proof uses.
- [structural-analogy] linear compression $w=Hx$ with a decoder choosing the likeliest $x$ ↔ coding theory: syndrome decoding of linear error-correcting codes — the text says efficient decoders of such codes can make the decompressor practical (p. 218).
- [structural-analogy] $U$ in Ahlswede-Körner-Wyner ↔ machine learning: information bottleneck — compress $Y$ to $U$, paying $I(Y;U)$, to keep information about $X$.
- [structural-analogy] random coding with a union bound here ↔ channel coding (Part IV): the text says data transmission is based on the same method (p. 215).
- [structural-analogy] normal approximation $nH+\sqrt{nV}Q^{-1}(\epsilon)$ ↔ statistics: central limit theorem for the sum of surprisals.

## Questions this raises
- Slepian-Wolf allows undetectable errors; how much extra redundancy would making errors detectable cost in the decompressor-only setting? (Remark 11.5 says it kills the gain.)
- How can the decompressor be made efficient, e.g. by reusing decoders of linear error-correcting codes? (p. 218)
- Can the helper problem be solved explicitly for specific $P_{X,Y}$? The text points to the $F_I$-curve (Definition 16.5).
- How do these results extend from iid sources to ergodic processes? (The text promises Chapter 12.)

## Reading notes
- The unit id says "ch13", but the chapter is printed as **Chapter 11**. Printed page = pdf − 25 (pdf 237 = p. 212). Running headers are "itbook-export CUP/HE2-design August 16, 2024" (a build stamp).
- Misprints seen in the images: Theorem 11.8 writes $H\in\mathbb F_q^{n\times k}$ though $H$ is $k\times n$ (p. 219). In §11.6, $g_2$ is typed with domain $\{0,1\}^{k_1}\times\mathcal S^n$ instead of $\{0,1\}^{k_2}$, and "Similarly, the point $(H(S),H(T|S))$ can be approached" repeats the first corner; the other corner is $(H(S|T),H(T))$ (p. 226). The first line of the union-bound chain there is typed "=", where "≤" is meant. The Slepian-Wolf decoder in the proof of Theorem 11.13 outputs "0 otherwise" where $e$ is meant (p. 223). Remark 11.5's claim "$g(c,y)=e$ for all $y$" is reported as printed; the argument is only sketched. In the same remark the requirement is printed as "g(f(x),y) = x e" (a symbol seems missing); it is read here as $g(f(x),y)\in\{x,e\}$.
- Theorem 11.2 sums over $x\ge2^k$; Remark 11.1 sums over $x>2^k$; both are as printed.
- The text mentions an exercise ("exercise!", Remark 11.3; Exercise II.9) but contains no exercise list, so no Exercises section is given. §11.7 omits the Carathéodory details and refers to Chapter 25 results not in these pages.
