---
id: spielman-2025-sagt/ch21-cheeger
work: spielman-2025-sagt
unit: Chapter 21 — Cheeger's Inequality
pages: 176–180
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Cheeger's Inequality

## L0 — One line
If a vector $z$, centered with respect to the degree vector $d$, has a small generalized Rayleigh quotient $\rho$, then a random threshold cut of $z$ has expected boundary at most $\sqrt{2\rho}$ times the expected smaller side, so some threshold set has conductance at most $\sqrt{2\rho}$.

## L1 — The gist (≤ 120 words)
The previous chapter showed $\phi(S)\ge \nu_2/2$ for every vertex set $S$. This chapter asks for a converse: is there a set whose conductance (cut weight relative to the smaller side's degree) is small when $\nu_2$ is small? The answer is yes: some set has $\phi(S)\le\sqrt{2\nu_2}$. The proof follows Trevisan. Take a vector $z$ with small Rayleigh quotient $\rho$ and cut it at a random threshold $\tau$ with density $2|t|$. Then compute the expected cut weight and the expected smaller-side degree. Their ratio is at most $\sqrt{2\rho}$, so some threshold must do at least as well. This shows that a small $\nu_2$ forces a sparse cut.

**Prerequisites:** conductance $\phi(S)=w(\partial S)/\min(d(S),d(V-S))$; weighted degrees $d$, $D=\mathrm{diag}(d)$; Laplacian quadratic form; generalized Rayleigh quotient; expectation; Cauchy–Schwarz.

## L2 — Key ideas
- Cheeger's inequality is a partial converse to $\phi(S)\ge\nu_2/2$: some $S$ has $\phi(S)\le\sqrt{2\nu_2}$ (p. 176).
- The theorem works for any $y\perp d$ with small Rayleigh quotient. An eigenvector gives $y=D^{1/2}\psi_2$, but any such $y$ will do (p. 176).
- Centering shifts $y$ so that the weighted median vertex $j$ has value $0$. This does not increase the Rayleigh quotient (pp. 176–177).
- Trevisan's idea: pick the threshold $\tau\in[z(1),z(n)]$ with density $2|t|$. Then interval probabilities are differences of $\mathrm{sgn}(x)x^2$ (p. 178).
- The expected smaller-side degree equals exactly $z^TDz$ (Lemma 21.1.5, p. 179).
- The expected cut weight is at most $\sum w_{a,b}|z(a)-z(b)|(|z(a)|+|z(b)|)$ (Lemma 21.1.4, p. 178).
- Cauchy–Schwarz splits that sum into two square-root factors, which together are at most $\sqrt{\rho z^TDz}\sqrt{2z^TDz}$. So the expectation of the cut is at most $\sqrt{2\rho}$ times the expectation of the denominator (p. 180).
- Expectation bounds imply the existence of one good $\tau$ (footnote, p. 178).

## L3 — Walkthrough

**Intro (p. 176).** The last chapter gave $\phi(S)\ge\nu_2/2$ for all $S\subseteq V$. This chapter shows that there exists $S$ with $\phi(S)\le\sqrt{2\nu_2}$, "and provides an algorithm" using the $\nu_2$ eigenvector. Cheeger proved the original for manifolds; discrete versions came in the late 1980s. This proof follows Trevisan (p. 176).

**21.1 Setup (pp. 176–177).** Sets are $S_\tau=\{a: y(a)\le\tau\}$. If $\psi_2$ is an eigenvector for $\nu_2$, then $y=D^{1/2}\psi_2$ is orthogonal to $d$, and its generalized Rayleigh quotient equals $\nu_2$ (p. 176). Any $y\perp d$ with small quotient also works; the author prefers vectors *centered* with respect to $d$.

*Definition 21.1.1.* $y$ is centered if $\sum_{a:y(a)>0}d(a)\le d(V)/2$ and $\sum_{a:y(a)<0}d(a)\le d(V)/2$ (p. 176).

To center, renumber so $y(1)\le\dots\le y(n)$. Let $j$ be the least index with $\sum_{a=1}^j d(a)\ge d(V)/2$, and set $z=y-y(j)\mathbf 1$, so $z(j)=0$ (p. 177). The author says $\frac{z^TLz}{z^TDz}\le\frac{y^TLy}{y^TDy}$ (p. 177).

*Lemma 21.1.2.* For $v_s=y+s\mathbf 1$, $v_s^TDv_s$ is minimized at the $s$ with $v_s^Td=0$. Proof: the derivative is $2d^Tv_s$, which is zero at the minimum (p. 177).

(added step) The ratio claim follows because $L\mathbf 1=0$ leaves the numerator unchanged. Since $y^Td=0$, $s=0$ is the minimizer, so $z^TDz\ge y^TDy$. The text does not spell this out.

*Theorem 21.1.3.* Let $z$ be centered with respect to $d$. Then some $\tau$ gives $S_\tau$ with
$$\phi(S_\tau)\le\sqrt{2\,\tfrac{z^TLz}{z^TDz}}.$$
Scale $z$ so that $z(1)^2+z(n)^2=1$. Define $\rho=z^TLz/z^TDz$. It suffices to find $\tau$ with $\phi(S_\tau)\le\sqrt{2\rho}$ (p. 177).

**Strategy (pp. 177–178).** Define a distribution on $\tau$ such that
$$\mathbb E[w(\partial S_\tau)]\le\sqrt{2\rho}\;\mathbb E[\min(d(S_\tau),d(V-S_\tau))].$$
Then some $\tau$ has $w(\partial S_\tau)\le\sqrt{2\rho}\min(d(S_\tau),d(V-S_\tau))$. Reason (footnote 1): the expectation of $\sqrt{2\rho}\min(\cdot)-w(\partial S)$ is $\ge0$, so some $S$ makes it non-negative (pp. 177–178). From here the sets are $S_\tau=\{a:z(a)\le\tau\}$ (p. 178).

**The distribution (p. 178).** Choose $\tau\in[z(1),z(n)]$ with density $2|t|$. Total probability: $\int_{z(1)}^{0}2|t|\,dt+\int_0^{z(n)}2|t|\,dt=z(1)^2+z(n)^2=1$, using $z(1)\le0\le z(n)$. For $a<b$, $\Pr[\tau\in[a,b]]=\mathrm{sgn}(b)b^2-\mathrm{sgn}(a)a^2$, with $\mathrm{sgn}$ the sign function ($1,0,-1$).

*Intuition note.* The density $2|t|$ gives more weight to thresholds far from zero. With it, interval probabilities become differences of squares, and these match the quadratic sums in $z^TDz$.

**Lemma 21.1.4 (numerator, p. 178–179).**
$$\mathbb E_\tau[w(\partial S_\tau)]=\sum_{(a,b)\in E}w_{a,b}\Pr_\tau[(a,b)\in\partial S_\tau]\le\sum_{(a,b)\in E}w_{a,b}|z(a)-z(b)|(|z(a)|+|z(b)|).\tag{21.1}$$
Proof. An edge with $z(a)\le z(b)$ is on the boundary if $z(a)\le\tau<z(b)$. The author gives the probability of this as $\mathrm{sgn}(z(b))z(b)^2-\mathrm{sgn}(z(a))z(a)^2$.
- *Different signs ($\mathrm{sgn}(a)\ne\mathrm{sgn}(b)$):* the probability is $z(a)^2+z(b)^2\le(z(b)-z(a))^2=|z(a)-z(b)|(|z(a)|+|z(b)|)$ (p. 178).
- *Same sign:* the probability is $|z(a)^2-z(b)^2|=|z(a)-z(b)|(|z(a)|+|z(b)|)$ (p. 179).

**Lemma 21.1.5 (denominator, p. 179).** $\mathbb E_\tau[\min(d(S_\tau),d(V-S_\tau))]=z^TDz$.
Proof. By centering, $\tau<0$ implies $d(S)$ is the minimum, and $\tau\ge0$ implies $d(V-S)$ is. So vertices $a<j$ count when $z(a)<\tau<0$, and vertices $a\ge j$ count when $z(a)>\tau\ge0$. Hence
$$\sum_{a<j}\Pr[z(a)<\tau<0]d(a)+\sum_{a\ge j}\Pr[z(a)>\tau\ge0]d(a)=\sum_a z(a)^2d(a)=z^TDz.$$
The probabilities equal $z(a)^2$ by the density formula.

**Finishing (p. 180).** Cauchy–Schwarz bounds the sum in (21.1) by
$$\sqrt{\textstyle\sum_{(a,b)\in E}w_{a,b}(z(a)-z(b))^2}\;\sqrt{\textstyle\sum_{(a,b)\in E}w_{a,b}(|z(a)|+|z(b)|)^2}.\tag{21.2}$$
- The first factor squared is $z^TLz\le\rho z^TDz$.
- Second factor: $\sum w_{a,b}(|z(a)|+|z(b)|)^2\le2\sum w_{a,b}(z(a)^2+z(b)^2)=2\sum_a z(a)^2d(a)=2z^TDz$. (added step: $(x+y)^2\le2(x^2+y^2)$ because $2xy\le x^2+y^2$.)

Together:
$$\mathbb E[w(\partial S)]\le\sqrt{\rho z^TDz}\sqrt{2z^TDz}=\sqrt{2\rho}\,z^TDz=\sqrt{2\rho}\,\mathbb E[\min(d(S),d(V-S))].$$

*Intuition note.* The expected denominator is computed exactly and the expected cut is bounded in closed form, so the ratio of expectations can be bounded without searching. If the average threshold meets the bound, at least one threshold does.

## Toy example (ours)
Path $1\!-\!2\!-\!3\!-\!4$, unit weights. $d=(1,2,2,1)$, $d(V)=6$. Take $y=(-3,-1,1,3)$. The least $j$ with $\sum_{a\le j}d(a)\ge3$ is $j=2$ (since $1+2=3$). So $z=y-y(2)\mathbf 1=(-2,0,2,4)$.
- $z^TLz=2^2+2^2+2^2=12$; $z^TDz=4+0+8+16=28$; $\rho=3/7$; $\sqrt{2\rho}\approx0.926$.
- Normalizer: $z(1)^2+z(4)^2=20$, so $\Pr[\tau\in[a,b]]=(\mathrm{sgn}(b)b^2-\mathrm{sgn}(a)a^2)/20$.
- $\tau\in[-2,0)$: $S=\{1\}$, probability $4/20$, min $=1$. $\tau\in[0,2)$: $S=\{1,2\}$, probability $4/20$, min $=3$. $\tau\in[2,4)$: $S=\{1,2,3\}$, probability $12/20$, min $=1$.
- $\mathbb E[\min]=(4\cdot1+4\cdot3+12\cdot1)/20=1.4=28/20=z^TDz$ after scaling $z$ by $1/\sqrt{20}$, as Lemma 21.1.5 says.
- Every set has boundary weight 1, so $\mathbb E[w(\partial S)]=1$. The Lemma 21.1.4 sum is $(4+4+12)/20=1$ (equality here). Bound: $0.926\times1.4\approx1.296\ge1$.
- Conductances: $1,\ 1/3,\ 1$. The best set has $\phi=1/3\le0.926$.

## Concepts
- [[cheeger-inequality]] (new) — some $S$ has $\phi(S)\le\sqrt{2\nu_2}$; partial converse to $\phi\ge\nu_2/2$ (p. 176)
- [[conductance]] (new) — $\phi(S)=w(\partial S)/\min(d(S),d(V-S))$ (p. 177)
- [[rayleigh-quotient]] — here the generalized one with respect to $L$ and $D$; equals $\nu_2$ for $y=D^{1/2}\psi_2$ (p. 176)
- [[centered-vector]] (new) — neither the positive nor the negative part carries more than half the degree (p. 176)
- [[graph-laplacian]] — $z^TLz$ as the numerator of the Rayleigh quotient (p. 177)
- [[random-threshold-cut]] (new) — Trevisan's $\tau$ with density $2|t|$, used to bound expectations (p. 178)

## Canonical instances
- Random threshold rounding of an eigenvector-like vector $z$ into a cut $S_\tau$ (p. 178).

## Bridges (candidates)
- [structural-analogy] Random threshold with density $2|t|$ ↔ probabilistic method: an expectation bound implies the existence of one good outcome.
- [structural-analogy] Centering $z=y-y(j)\mathbf 1$ ↔ choosing a weighted median; the shift changes only the denominator.

## Questions this raises
- How is the set $S_\tau$ found by an actual algorithm from the eigenvector? The unit promises one (p. 176) but only proves existence.
- Is the square root in $\sqrt{2\nu_2}$ necessary, or can the gap to $\nu_2/2$ be closed?
- Why is density $2|t|$ the right choice for this proof?

## Reading notes
- Printed = pdf − 24.
- Theorem 21.1.3 defines $S_\tau$ with $z(a)<\tau$; the proof uses $z(a)\le\tau$ (p. 178). The author says the definition changed.
- In the proof of Lemma 21.1.4 (p. 178) the text writes $\mathrm{sgn}(a)$, $\mathrm{sgn}(b)$; the quantities presumably meant are $\mathrm{sgn}(z(a))$, $\mathrm{sgn}(z(b))$.
- The same-sign line on p. 179 shows $z(a)^2-z(b)^2$ inside an absolute value, which is why the sign works out.
- Footnote 1 and the final chain drop the subscript $\tau$ on $\mathbb E$.
- Page images match the text layer; the equations were readable.
