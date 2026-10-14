---
id: stone-2022-information/appd-probability
work: stone-2022-information
unit: Appendices D–E (Probability Density Functions; Averages From Distributions)
pages: 253–258
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Probability Density Functions; Averages From Distributions

## L0 — One line
A pdf is the limit of a normalised histogram as bins shrink, and an average over a distribution is a probability-weighted sum (or integral), which turns Shannon information into entropy.

## L1 — The gist (≤ 120 words)
Appendix D asks how probability can be assigned to a continuous variable such as height. Its answer: build a histogram, scale it so the total area is 1, and shrink the bins. The bin height becomes a probability density, and the area under the curve is 1. Appendix E shows how to compute a mean, E[X], from a distribution by weighting each value by its probability. It extends this to any function h(x). With h(x) = log(1/p(x)), the expected value is the entropy H(X). For continuous X it is the differential entropy.

**Prerequisites:** sums (Σ) and integrals as area under a curve; the idea of a limit; logarithms; the mean as a weighted average.

## L2 — Key ideas
- Counting how many people have one exact height makes no sense, since no two individuals have exactly the same height. The author therefore divides height into intervals (bins) and counts per interval (p. 253).
- In a normalised histogram, bin area equals the probability of that bin, and the bin areas sum to 1 (p. 255).
- Probability density is probability divided by bin width. This is the same form as mass divided by volume (p. 256).
- Shrinking the bin width to zero turns the sum of $p(x_i)\,\delta x$ into $\int p(x)\,dx = 1$ (p. 256).
- E[X] is the sum of each value times its probability. This matches the sample mean when sample frequencies follow the probabilities (p. 257).
- For a function h (the author starts from $h(x_i)=x_i^2$), $E[h(X)] = \sum_i p(x_i)h(x_i)$ (p. 258).
- If h is the Shannon information $\log(1/p(x))$, the expectation is the entropy H(X). For continuous X the integral version gives differential entropy (p. 258).

## L3 — Walkthrough

### Appendix D: Probability Density Functions

**Functions (p. 253).** A function maps a domain to a range, for example $y=\pi x^2$ or generically $y=f(x)$. It can relate continuous variables or abstract quantities like probability. The author says that a probability density function "defines the probability of every value of a variable" (p. 253); on p. 256 he calls the height $p(x_i)=P_i/\Delta x$ the probability density.

**From histogram to bins (pp. 253–254).**
- Example: 5,000 heights. Counting people at an exact height makes no sense, so height is divided into bins of width $\delta x = 1.6$ inches between 60 and 84 inches. This gives $M=15$ bins (p. 253–254). *(added step: 24/1.6 = 15.)*
- The counts give a bell-shaped histogram, and the author expects a large proportion of measurements in bins around 72 inches (p. 254).

**Dots picture (p. 254).** Drop dots at random onto the histogram image. A dot's probability of landing in bin $i$ is the bin area as a share of the total area: $P_i = a_i/A$. The author writes $a_i = n_i \times \Delta x$, where $n_i$ is the number of dots in the bin, taken as its height (p. 254).

$$A=\sum_{i=1}^{M} a_i \tag{D.1}$$

$$\sum_{i=1}^{M} P_i = 1 \tag{D.2}$$

The bin width is

$$\Delta x = x_i^{max}-x_i^{min} \tag{D.3}$$

In a *normalised* histogram, bin area is numerically equal to probability (p. 255):

$$P_i = p(X \text{ is between } x_i^{min} \text{ and } x_i^{max}) \tag{D.4}$$

**Density (p. 256).** Bin height is area divided by width: $p(x_i)=P_i/\Delta x$, the probability density near $x_i$. Shrinking the bin width towards zero makes $\Delta x$ an infinitesimal $dx$. The density values then define a continuous curve $p(X)$. A pdf can be written as an equation, for example a Gaussian (Appendix G) (p. 256).

**Rod analogy (p. 256).** Take a rod whose gold content, and so density, rises from left to right. Bin area plays the role of segment mass, and bin width plays the role of volume.

$$\text{rod segment density}=\frac{\text{segment mass}}{\text{segment volume}} \tag{D.5}$$

$$\text{probability density}=\frac{\text{probability (=bin area)}}{\text{bin width}} \tag{D.6}$$

**Normalisation (p. 256).** Using $P_i=p(x_i)\Delta x$, Equation D.2 becomes

$$\sum_{i=1}^{M} p(x_i)\,\delta x = 1 \tag{D.7}$$

As $\delta x \to 0$ this becomes

$$\int_x p(x)\,dx = 1 \tag{D.8}$$

The area under the pdf is, by definition, 1 (p. 256).

*Intuition note:* A density is not a probability. It is probability per unit width (probability / bin width, D.6). Multiply it by a width to get a probability. Because the total area must be 1, the heights can exceed 1 if the curve is narrow. (This last remark is ours, not the author's.)

### Appendix E: Averages From Distributions

**Mean as weighted sum (p. 257).**

$$E[X]=\sum_{i=1}^{m} p(x_i)\,x_i \tag{E.1}$$

Worked example: values $[4\ 5\ 6]$ with relative frequencies $[0.1\ 0.2\ 0.7]$. A typical sample of 100 has 10 fours, 20 fives and 70 sixes. Its mean is

$$\frac{(10\times4)+(20\times5)+(70\times6)}{100}=(0.1\times4)+(0.2\times5)+(0.7\times6) \tag{E.2}$$

With $x_1=4,\ x_2=5,\ x_3=6$ and $p(x_1)=0.1,\ p(x_2)=0.2,\ p(x_3)=0.7$:

$$E[X]=(0.1\times4)+(0.2\times5)+(0.7\times6) \tag{E.3}$$
$$=p(x_1)x_1+p(x_2)x_2+p(x_3)x_3 \tag{E.4}$$
$$E[X]=\sum_{i=1}^{3}p(x_i)\,x_i \tag{E.5}$$

*(added step: the value is $0.4+1.0+4.2=5.6$.)* (pp. 257–258)

**Function of a variable (p. 258).** For $h(x_i)=x_i^2$ and $m$ values:

$$E[X^2]=p(x_1)x_1^2+p(x_2)x_2^2,\ldots,+p(x_m)x_m^2 \tag{E.6}$$
$$=\sum_{i=1}^{m}p(x_i)\,x_i^2 \tag{E.7}$$
$$=\sum_{i=1}^{m}p(x_i)\,h(x_i) \tag{E.8}$$
$$=E[h(x)] \tag{E.9}$$

**Entropy as an average (p. 258).** With Shannon information $h(x)=\log(1/p(x))$:

$$E[h(X)]=\sum_{i=1}^{m}p(x_i)\log\frac{1}{p(x_i)} \tag{E.10}$$
$$=H(X) \tag{E.11}$$

So average Shannon information is the entropy (p. 258).

**Continuous case (p. 258).** The sum becomes an integral:

$$E[h(X)]=\int_x p(x)\,h(x)\,dx \tag{E.12}$$

With $h(x)=\log(1/p(x))$:

$$E[h(X)]=\int_x p(x)\log\frac{1}{p(x)}\,dx \tag{E.13}$$
$$=H(X) \tag{E.14}$$

The author says this "yields the differential entropy of X" (p. 258).

*Intuition note:* An average over a distribution just means "weight each value by how often it occurs". Entropy uses the same recipe, with surprise, $\log(1/p(x))$, as the value being averaged.

## Toy example (ours, not from the text)
100 dots fall into 4 bins of width $\Delta x=0.5$ covering 0 to 2, with counts 10, 30, 40, 20.
- Probabilities: $P_i = 0.1,\ 0.3,\ 0.4,\ 0.2$. Sum $=1.0$.
- Densities $p(x_i)=P_i/\Delta x = 0.2,\ 0.6,\ 0.8,\ 0.4$.
- Check D.7: $(0.2+0.6+0.8+0.4)\times0.5 = 2.0\times0.5 = 1$.
- $P(0.5<X<1.5)=0.3+0.4=0.7$.
- Mean using bin midpoints 0.25, 0.75, 1.25, 1.75 (an approximation): $0.1(0.25)+0.3(0.75)+0.4(1.25)+0.2(1.75)=0.025+0.225+0.5+0.35=1.1$.

## Concepts
- [[probability-density-function]] (new) — curve whose height is the probability density; in a normalised histogram each bin's area equals its probability (p. 255), and the total area under the pdf is 1 (p. 256)
- [[histogram-normalisation]] (new) — scaling bin areas so they equal probabilities and sum to 1 (p. 255)
- [[expected-value]] (new) — mean obtained as $\sum_i p(x_i)x_i$, or the integral version (p. 257–258)
- [[self-information / surprisal]] — $h(x)=\log(1/p(x))$, called Shannon information here (p. 258)
- [[entropy H(X)]] — expected Shannon information, $\sum p\log(1/p)$ (p. 258)
- [[differential entropy]] — the same expectation for continuous X, as an integral (p. 258)

## Canonical instances
- [[height-histogram]] — 5,000 heights, 15 bins of 1.6 inches (p. 253–254)
- [[gold-aluminium-rod]] — mass/volume analogy for probability/width (p. 256)
- [[three-value-mean-example]] — values 4, 5, 6 with probabilities 0.1, 0.2, 0.7 (p. 257)

## Bridges (candidates)
- [structural-analogy] probability density = probability / bin width ↔ physics: mass density = mass / volume — the author draws this analogy himself (p. 256).
- [same-math] $E[h(X)]=\sum p(x)h(x)$ ↔ statistics: expectation of a function of a random variable — entropy is the special case $h=\log(1/p)$.
- [structural-analogy] sum over bins → integral as bin width → 0 ↔ calculus: Riemann sum → integral.

## Questions this raises
- Why can differential entropy differ in behaviour from discrete entropy, given that a density is not a probability?
- Does the choice of bin width change the entropy of a binned variable?
- Does the log base in E.10 matter for the meaning of H(X)? The text does not state a base here.

## Reading notes
- Printed pages 253–258 equal pdf 269–274 (printed = pdf − 16).
- The unit metadata title says "+ following appendices", but these pages contain only Appendices D and E.
- The text uses $\Delta x$ and $\delta x$ interchangeably (see D.7). It also refers to Figure 5.1, which is not in these pages.
- E.6 is printed with commas between terms ("$\ldots,\ +p(x_m)x_m^2$"). This looks like a typo for plus signs. Equation E.9 writes $E[h(x)]$ with lowercase x.
- The author writes both "probability density function defines the probability of every value" (p. 253) and later "density". Page 256 then calls the bin height the "probability density", so the p. 253 sentence is best read loosely.
