---
id: stone-2022-information/appb-mathematical
work: stone-2022-information
unit: Appendix B Mathematical Symbols; Appendix C Logarithms
pages: 247–252
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Appendix B (Mathematical Symbols) and Appendix C (Logarithms)

## L0 — One line
This unit is the book's notation key plus a short log tutorial: a logarithm is the power a base must be raised to, and logs turn products into sums.

## L1 — The gist (≤ 120 words)
Appendix B lists the symbols used in the book: general maths signs, Greek letters, and information-theory notation. Examples are $H(X)$, $H(X|Y)$, $I(X,Y)$, $C$, $R$, $h(x)$, bold sequences and the transfer entropy $T$. Appendix C explains logarithms. $\log_a x$ is the power to which $a$ must be raised to give $x$. Logs turn multiplication into addition. Any base can be converted to any other by a ratio of logs. The book uses base 2 unless stated. The unit is reference material, not an argument. It helps you decode later formulas, for example by telling you which symbols are random variables and which are values.

**Prerequisites:** exponents (e.g. $10^2$); the idea of a random variable; basic mean and variance.

## L2 — Key ideas
- The capital letters $X$, $Y$ and $S$ are random variables; the lower-case $x$, $y$ and $s$ are their values. $x$ is a channel input, $y$ a channel output and $s$ a message. (pp. 249–250)
- Bold letters mark sequences: $\mathbf{x}$ of values, $\mathbf{X}$ of random variables, and hatted versions for distorted copies. (p. 250)
- Entropy is the average Shannon information (the "surprise" of a value), where $h(x)=\log(1/p(x))$ is the Shannon information of the value $x$. Conditional entropy $H(X|Y)$ is the average uncertainty about $X$ left after $Y$ is seen. (p. 248)
- $C$ (capacity, the maximum rate of communication through a channel) and $R$ (the rate at which information is communicated) are both printed with the expression $H(X)-H(X|Y)$. $C$ is printed with a "max(p(x))" label, which I read as a maximum over $p(x)$ (see Reading notes). (pp. 248, 249)
- Shannon's capacity equation is printed with $N$ as the noise variance: $C=\tfrac12\log(1+P/N)$. (p. 249)
- A logarithm answers "what power gives this number?", e.g. $\log_{10}100=2$. (p. 251)
- Logs turn products into sums: $\log_b(nm)=\log_b n+\log_b m$. Multiply by adding logs, then take the anti-logarithm (raise the base to the sum). (p. 252)
- Base change: $\log_b x=\log_a x/\log_a b$. This book uses base 2 unless told otherwise. (p. 252)

## L3 — Walkthrough

### Appendix B — Mathematical Symbols (pp. 247–250)

**General symbols (p. 247).**
- Hat $\hat{\ }$ marks an *estimated* value, e.g. $\hat v_x$ estimates the variance $v_x$.
- $|x|$ is the absolute value; $\le$, $\ge$, $\approx$ (approximately equal), $\infty$ and $\propto$ (proportional to) have their usual meanings.
- $X\sim p(X)$ means $X$ has distribution $p(X)$.
- $\in$ means "element of a set", e.g. $w\in\{1,\dots,\hat m\}$.

**Greek letters (pp. 247–248).**

| Symbol | Meaning |
|---|---|
| $\alpha$ | number of different symbols in an alphabet |
| $\Delta$ | small increment |
| $\epsilon$ | small quantity |
| $\eta$ | a single noise value in a measured quantity |
| large eta | random variable for noise |
| $\mu$ | mean |
| $\rho$ | correlation |
| $\sigma$ | standard deviation |

**Summation (p. 248).** $\sum$ means summation. For $n=3$ with $x_1=2,\ x_2=5,\ x_3=7$:
$$x_{sum}=\sum_{i=1}^{n}x_i=x_1+x_2+x_3=2+5+7=14.$$
The index $i$ counts from 1 to $n$ and each term is added to a running total. (p. 248)

**Information-theory symbols (pp. 248–249).**
- $A$ is the alphabet of values of a variable, e.g. $A_x=\{x_1,\dots,x_m\}$. (p. 248)
- $C$ is channel capacity, the maximum rate of communication through a channel, usually in bits/s. It is printed inline as $C\,\max(p(x))=H(X)-H(X|Y)$. (p. 248)
- $R$ is the rate of communicated information, $R=H(X)-H(X|Y)$. (p. 249)
- $D$ is the mean distortion between sequences $\mathbf x$ and $\hat{\mathbf x}$. $d$ is the distortion of corresponding elements. (p. 248)
- $e=2.71828182845\ldots$ is the base of natural logarithms, so $\ln e^x=x$. (p. 248)
- $\mathrm E[X]$ is the mean or expected value. $E$ (italic) is equivocation, i.e. $H(X|Y)$. (p. 248)
- $g$ is the encoding function: $\mathbf x=g(\mathbf s)$ maps a message $\mathbf s=(s_1,\dots,s_k)$ to channel inputs $\mathbf x=(x_1,\dots,x_n)$. (p. 248)
- $h(x)=\log(1/p(x))$ is Shannon information, uncertainty or surprise. $h$ is also used for the lossy compression encoding function. $\overline h(x)$ is the average Shannon information of a finite sample. (p. 248)
- $H(X)$ is the average Shannon information of $p(X)$. (p. 248)
- $H(X|Y)$ is the average uncertainty in $X$ after $Y$ is observed. $H(Y|X)$ is defined the same way with roles swapped. (p. 248)
- $H(X,Y)$ is the entropy of the joint distribution $p(X,Y)$. (p. 249)
- $I(X,Y)$ is mutual information, the average number of bits each value of $Y$ provides about $X$ and vice versa. (p. 249)
- $\ln x$ is the natural log. $\log x$ uses base 2 in this text, with a subscript if unclear. (p. 249)
- $m$ is the number of possible messages, input values, codewords or symbols. $M$ is the number of histogram bins. $n$ is the number of observations, or elements in a message, or codewords. (p. 249)
- $N$ is the noise variance in Shannon's equation $C=\tfrac12\log(1+P/N)$. (p. 249)
- $p(X)$ is the distribution of $X$. $p(x)$ is the probability (density) that $X=x$. (p. 249)
- $p(X,Y)$ is the joint distribution. For discrete variables it is the joint probability function (pf); for continuous variables, the joint probability density function (pdf). (p. 249)
- $p(x,y)$ is the joint probability of $x$ and $y$. $p(x|y)$ is the conditional probability that $X=x$ given $Y=y$. (p. 249)
- $S$ is a random variable and $s$ a value of it, used to represent a message. (p. 249)
- $T_{x_{\text{past}}\to y_t}$ is transfer entropy: the average information past values of $X$ give about the current $y_t$, over and above what $y_{\text{past}}$ gives. (p. 249)
- $v_x=\sigma_x^2=\mathrm E[(\mu-x)^2]$ is the variance of $X$ with mean $\mu$. (p. 249)
- $W$ is the total number of microstates of a system. (p. 249)

**Variables and sequences (p. 250).**
- $X$ and $Y$ are random variables. $x$ is a channel input and $y$ a channel output.
- $X^\Delta$ is $X$ quantised into intervals (e.g. histogram bins) of width $\Delta x$.
- $\hat X$ is the distorted version of $X$.
- Bold $\mathbf x$ is a vector or permutation, written $(x_1,\dots,x_n)$ with round brackets, or a combination, written $\{x_1,\dots,x_n\}$ with curly brackets.
- $\hat{\mathbf x}$ is a sequence $(\hat x_1,\dots,\hat x_n)$.
- $\mathbf X$ is a sequence $(X_1,\dots,X_n)$ of random variables, and $\hat{\mathbf X}$ is $(\hat X_1,\dots,\hat X_n)$.

*Intuition note:* Capital means "the variable as a whole", lower-case means "one value", bold means "a whole sequence", and a hat means "estimated or distorted". Keeping this straight makes formulas such as $H(X|Y)$ much easier to read.

### Appendix C — Logarithms (pp. 251–252)

**Definition.** The power to which 10 must be raised to give 100 is 2, because $100=10^2$. So $2=\log_{10}100$. (p. 251)

**Why logs are useful.** They turn multiplication into addition. The author's example for $100\times100$:
$$10^2\times10^2=10^{2+2}\tag{C.1}$$
$$=10^4\tag{C.2}$$
$$=10{,}000.\tag{C.3}$$
(p. 251)

In logs to base 10:
$$\log_{10}100+\log_{10}100=\log_{10}10^2+\log_{10}10^2\tag{C.4}$$
$$=2+2.\tag{C.5}$$
The anti-logarithm of 4 means raising the base to that power: $10^4=10{,}000$. To multiply $n$ and $m$, add their logs and take the anti-logarithm of the sum. (p. 252)

**Any base $b$.**
$$y=\log_b(n\times m)=\log_b n+\log_b m,\tag{C.6}$$
$$n\times m=b^{\log_b n+\log_b m}=b^{y}.\tag{C.7}$$
(p. 252)

**Base conversion.**
$$\log_b x=\frac{\log_a x}{\log_a b}.\tag{C.8}$$
Natural logs use base $e$ and are written $\ln x$. Logs are base 2 in this book unless otherwise specified. (p. 252)

**Summary.** $y=\log_a x$ is the power to which $a$ must be raised to get $x$. Equivalently, $x=a^y$. (p. 252)

**Figure C.1 (p. 251).** It plots $\log x$ for base 2 (dotted) and base 10 (solid) for $x$ from 0 to 10. The caption notes that $\log x$ increases monotonically with $x$.

*Intuition note:* For whole-number powers, a log counts "how many times you multiplied the base". Multiplying numbers then means adding counts. By (C.8), changing the base divides the log by the constant $\log_a b$, so it only rescales the log.

## Toy example (ours)
Compute $8\times4$ in base 2.
- $\log_2 8=3$ because $2^3=8$. $\log_2 4=2$ because $2^2=4$.
- Sum of logs: $3+2=5$. Anti-logarithm: $2^5=32$. Check: $8\times4=32$. ✓

Base change by (C.8): find $\log_4 64$ using base 2.
- $\log_2 64=6$ because $2^6=64$. $\log_2 4=2$.
- $\log_4 64=6/2=3$. Check: $4^3=64$. ✓

## Concepts
- [[self-information-surprisal]] — here $h(x)=\log(1/p(x))$, "Shannon information, uncertainty, or surprise" (p. 248)
- [[entropy]] — $H(X)$, the average Shannon information of $p(X)$ (p. 248)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ is the entropy of the joint distribution. $H(X|Y)$ is the average uncertainty in $X$ after $Y$ is observed. (pp. 248–249)
- [[mutual-information]] — $I(X,Y)$, the average bits each $Y$ value gives about $X$, and vice versa (p. 249)
- [[channel-capacity]] — the maximum rate of communication through a channel, printed with $H(X)-H(X|Y)$ (p. 248)
- [[shannon-hartley-formula]] — the appendix gives only the form $C=\tfrac12\log(1+P/N)$, with $N$ the noise variance (p. 249)
- [[transfer-entropy]] — information past $X$ gives about current $Y$ beyond what past $Y$ gives (p. 249)
- [[logarithm]] (new) — $\log_a x$ is the power of $a$ that gives $x$. Logs turn products into sums. (pp. 251–252)
- [[log-base-change]] (new) — $\log_b x=\log_a x/\log_a b$ (C.8) (p. 252)
- [[equivocation]] (new) — $E=H(X|Y)$ (p. 248)
- [[information-rate]] (new) — $R=H(X)-H(X|Y)$, usually in bits/s (p. 249)
- [[distortion]] (new) — $d$ per element, $D$ mean, between $\mathbf x$ and $\hat{\mathbf x}$ (p. 248)

## Canonical instances
None. The unit contains only notation and one numeric log example ($100\times100$), which does not belong to a named instance.

## Bridges (candidates)
- [same-math] log turns products into sums ↔ information theory: surprisal of independent events adds, because $\log$ of a product of probabilities is a sum of logs. This is a candidate only; the unit itself does not state it.
- [structural-analogy] base change (C.8) ↔ units of information: changing the log base rescales a quantity by a constant, like changing units.

## Questions this raises
- Which theorem justifies $R$ and $C$ both being written as $H(X)-H(X|Y)$, and what does the "max over $p(x)$" add for $C$?
- Why is base 2 the natural choice, and what changes when natural logs are used instead?
- How does the capacity expression with $\tfrac12\log(1+P/N)$ arise from the notation here?

## Reading notes
- Printed = pdf − 16. Printed page numbers are visible on all six pages.
- The $C$ entry on p. 248 prints "$C\max(p(x))=H(X)-H(X|Y)$" inline, with no subscript layout. This is the source's formatting. I take it to mean the maximum over $p(x)$, which is my reading.
- The "large eta" entry (p. 247) renders the capital letter like a lower-case $\eta$ in the page image and text. The text describes it as the random variable for noise.
- The text layer lost some symbols (summation sign, hat accents, overlines); I checked these against the images.
- There is no Appendix A in these pages. No exercises appear.
