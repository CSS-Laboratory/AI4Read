---
id: mackay-2003-information/ch19-have
work: mackay-2003-information
unit: "19 Why have Sex? Information Acquisition and Evolution"
pages: 269–280
fields: [information-theory, bayesian]
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
# Why have Sex? Information Acquisition and Evolution

## L0 — One line
In a simple additive-fitness model, a sexual population acquires information from natural selection of order √G times faster than an asexual one, and tolerates a mutation rate of order √G times higher (G = genome size in bits).

## L1 — The gist (≤ 120 words)
Natural selection gives at most one bit of feedback per offspring (whether it survived to have children), and that feedback is highly redundant. How fast can a species learn from it? MacKay builds a model in which fitness is the number of "good" bits in a G-bit genome. With variation by mutation alone, the rate is about 1 bit per generation, as John Maynard Smith suggested. With recombination (sex), it can be of order √G bits per generation. Sex also tolerates much higher mutation rates, so the model predicts that species with very large genomes use recombination at least occasionally. These results quantify the known argument for sex in terms of information acquisition.

**Prerequisites:** mean/variance of a Gaussian; binomial distribution; basic differential equations; logarithms in base 2; the idea of a bit as information.

## L2 — Key ideas (5–10 bullets)
- Natural selection is a teaching signal of at most one bit per offspring, and it is highly redundant. So the naive count of bits received overstates the information gained, because of the redundancy (pp. 269–270).
- Model: fitness is the sum of G bits (19.1); selection is truncation selection (keep the fittest $N$ children); variation comes from bit-flip mutation or from recombination with no linkage (each child bit is copied from a randomly chosen parent) (pp. 270–271).
- Mutation alone lowers the children's mean fitness (when $f>\tfrac12$). Writing $\delta f=f-\tfrac12$ for the excess normalized fitness, the best fitness gain is at most $1/(8\,\delta f)$ per generation (for $G(\delta f)^2\gg1$), so it is of order 1 or less once $\delta f$ is not small (pp. 271–272).
- Recombination keeps the mean fitness and adds a spread (standard deviation) of order √G. Fitness rises at a rate $\propto\sqrt{G}$ and perfection is reached in finite time of order √G generations (p. 273).
- The maximal tolerable mutation rate is about $1/G$ without sex and of order $1/\sqrt{G}$ with sex. Asexual litters would have to grow exponentially in $mG$ to compensate (p. 276).
- Information acquired is $I=\sum_g\log_2(f_g/\tfrac12)$, roughly twice the fitness gain above $G/2$ (p. 276).
- The "cost of males" argues that asexual mothers (parthenogens) should outbreed sexual ones. In the simulations parthenogens take over at low mutation rate ($mG=1$, where $mG$ is the mean number of bits flipped per genome) but never at $mG=4$; and MacKay argues that in a sufficiently unstable environment they always lag behind (pp. 277–278).
- The conclusions rest on an additive fitness function. The Baldwin effect (learning-like noise guiding evolution) and a conjectured noisy genetic code are offered as possible ways to smooth non-linear fitness (pp. 278–279).

## L3 — Walkthrough

### Introduction (pp. 269–270)
- Evolution has run for about $10^9$ years. The "teacher" is natural selection: fitter individuals have more progeny (p. 269).
- Fitness is a function of the DNA sequence and the environment (p. 269).
- The signal for an individual is only its number of grandchildren. Its content is at most one bit per offspring (which offspring survived to have children). It does not describe the organism's defects. It is highly redundant, since similar unfit individuals fail for similar reasons (p. 269).
- Naive count: 4 000 000 years since apes, 10-year generations gives about 400 000 generations. With $10^9$ individuals each receiving "a couple of bits", the total is about $8\times10^{14}$ bits (p. 270).
- Doubling the population would not double the speed, because selection would correct the same defects twice as often (p. 270).
- **Maynard Smith's suggestion:** the rate is independent of population size and of order 1 bit per generation. That gives about 400 000 bits of ape–human difference, far below the genome size of $6\times10^9$ bits (about $3\times10^9$ nucleotides) (p. 270).
- MacKay's model finds: (1) 1 bit per generation is correct for asexual reproduction; (2) with sex the rate can be as large as $\sqrt G$ bits per generation (p. 270).

### 19.1 The model (pp. 270–271)
- Genotype $\mathbf x$ is a vector of $G$ bits, with good state $x_g=1$ and bad state $x_g=0$. Fitness is
$$F(\mathbf x)=\sum_{g=1}^{G}x_g .\tag{19.1}$$
- The essential assumption: fitness is locally roughly linear in the genome. Many small changes exist, and their effects combine about linearly (pp. 270–271). Normalized fitness: $f(\mathbf x)\equiv F(\mathbf x)/G$ (p. 271).
- **Mutation model.** Discrete generations. Each individual has two children, whose bits flip independently with probability $m$, the same for every bit. **Truncation selection** keeps the fittest $N$ of the children (p. 271).
- **Recombination model.** The parents are haploid (one copy of each gene). The $N$ individuals form $M=N/2$ random couples, each with $C=4$ children, so the population doubles and halves each generation. Each child's bit comes from either parent with no linkage:
$$z_g=\begin{cases}x_g &\text{with probability }1/2\\ y_g&\text{with probability }1/2.\end{cases}\tag{19.2}$$
Then the parents die and the fittest $N$ of the $MC$ progeny are selected (p. 271).

### 19.2 Rate of increase of fitness (pp. 271–274)
**Theory of mutations.** Work with excess normalized fitness $\delta f\equiv f-\tfrac12$ and assume $f>\tfrac12$. For small $m$, a child of a parent with excess $\delta f$ has mean and variance
$$\overline{\delta f}_{\text{child}}=(1-2m)\,\delta f\tag{19.3}$$
$$\frac{m(1-m)}{G}\simeq\frac mG.\tag{19.4}$$
- Let the parents have mean $\delta f(t)$ and variance $\sigma^2(t)\equiv\beta m/G$. Before selection the children have mean $(1-2m)\delta f(t)$ and variance $(1+\beta)m/G$. Selection keeps the upper half (p. 272):
$$\delta f(t{+}1)=(1-2m)\,\delta f(t)+\alpha\sqrt{(1+\beta)}\sqrt{\frac mG}\tag{19.5}$$
$$\sigma^2(t{+}1)=\gamma(1+\beta)\frac mG\tag{19.6}$$
Here $\alpha$ is the mean deviation of the selected half, in standard deviations. $\gamma$ is the factor by which selection reduces the variance. Both are of order 1; for a Gaussian, $\alpha=\sqrt{2/\pi}\simeq0.8$ and $\gamma=1-2/\pi\simeq0.36$ (p. 272).
- Dynamic equilibrium of the variance, $\sigma^2(t{+}1)\simeq\sigma^2(t)$, gives
$$\gamma(1+\beta)=\beta,\quad\text{so}\quad 1+\beta=\frac1{1-\gamma}.\tag{19.7}$$
For the Gaussian values, $\alpha\sqrt{1+\beta}=1$ (added step: $\alpha^2(1+\beta)=\frac2\pi\cdot\frac\pi2=1$). This is poorest for small $m$, where discreteness matters (p. 272).
- Hence
$$\frac{df}{dt}\simeq-2m\,\delta f+\sqrt{\frac mG}.\tag{19.8}$$
If $G(\delta f)^2\gg1$ this is maximized at
$$m_{\rm opt}=\frac1{16G(\delta f)^2}\tag{19.9}$$
$$\left(\frac{df}{dt}\right)_{\rm opt}=\frac1{8G(\delta f)}\tag{19.10}$$
(added step: setting $\partial_m$ of (19.8) to zero gives $\sqrt{mG}=1/(4\delta f)$; then the two terms are $-\tfrac1{8G\delta f}$ and $+\tfrac1{4G\delta f}$.) So
$$\frac{dF}{dt}=\frac1{8(\delta f)}\ \text{per generation (at most).}\tag{19.11}$$
- For $\delta f<0.125$ the rate may exceed 1 unit per generation. If $\delta f\lesssim1/\sqrt G$ and $m=\tfrac12$, the rate is of order $\sqrt G$, but this spurt lasts only of order $\sqrt G$ generations. For $\delta f>0.125$ the rate is below one per generation (p. 272).
- As fitness approaches $G$, $m_{\rm opt}\to1/(4G)$: on average $1/4$ bit is flipped per genotype, fitness rises at $1/4$ per generation, and information is gained at about 0.5 bits per generation. About $2G$ generations are needed for all genotypes to reach perfection (p. 272).
- For fixed $m$:
$$\delta f(t)=\frac1{2\sqrt{mG}}\left(1-c\,e^{-2mt}\right),\tag{19.12}$$
subject to $\delta f\le\tfrac12$. The constant $c=1$ if $f(0)=\tfrac12$. If $mG>1$, $F$ approaches $F_{\rm eqm}=\left(\tfrac12+\tfrac1{2\sqrt{mG}}\right)G$ (pp. 272–273).
- The theory is inaccurate, since the true fitness distribution is non-Gaussian, asymmetric and quantized. Its predictions are "not grossly at variance" with simulations (p. 273).

*Intuition note.* Mutation is blind. When $f>\tfrac12$ it damages the typical child, so selection must first undo the damage before it can gain. The gain per generation is therefore of order one bit at most once the population is reasonably fit.

**Theory of sex** (p. 273). Two approximations: the gene pool mixes fast enough that correlations between genes are neglected; and *homogeneity*: the fraction $f_g$ of good bits is the same, $f(t)$, for every $g$.
- If two parents of fitness $F=fG$ mate, the children's fitness has mean $F$. Sex does not reduce average fitness. Its standard deviation scales as $\sqrt{Gf(1-f)}$. Since the selection gain is proportional to this standard deviation, the gain per generation scales as $\sqrt G$ (p. 273).
- **Box 19.2** (p. 274). Take two parents with exactly $fG$ good bits, as independent random subsets. About $f^2G$ bits are good in both and about $2f(1-f)G$ in one only. The child's fitness is $f^2G$ plus the sum of $2f(1-f)G$ fair coin flips (binomial, mean $f(1-f)G$, variance $\tfrac12f(1-f)G$). So
$$F_{\rm child}\sim\text{Normal}\!\left(fG,\ \tfrac12 f(1-f)G\right).$$
- With parental variance $\sigma^2(t)=\beta\,\tfrac12f(1-f)G$, the child variance is $(1+\beta/2)\tfrac12f(1-f)G$. Selection of the upper side then gives
$$\bar F(t{+}1)-\bar F(t)=\left[\alpha(1+\beta/2)^{1/2}/\sqrt2\right]\sqrt{f(1-f)G},$$
$$\sigma^2(t{+}1)=\gamma(1+\beta/2)\,\tfrac12f(1-f)G,$$
with $\alpha=\sqrt{2/\pi}$, $\gamma=1-2/\pi$. At dynamic equilibrium the bracket equals $\sqrt{2/(\pi+2)}\simeq0.62$ (p. 274).
- Defining $\eta\equiv\sqrt{2/(\pi+2)}$:
$$\frac{d\bar F}{dt}\simeq\eta\sqrt{f(t)(1-f(t))G}\tag{19.13}$$
$$f(t)=\frac12\left[1+\sin\!\left(\frac{\eta}{\sqrt G}(t+c)\right)\right],\quad t+c\in\left(-\tfrac\pi2\sqrt G/\eta,\ \tfrac\pi2\sqrt G/\eta\right),\tag{19.14}$$
with $c=\sin^{-1}(2f(0)-1)$. This idealized system reaches perfection ($f=1$) in finite time $(\pi/\eta)\sqrt G$ generations (p. 273).

*Intuition note.* Shuffling genes between parents spreads out the children's fitness without lowering the average. Selection can then pick the lucky upper tail. The spread grows like $\sqrt G$, so the gain does too.

**Simulations** (p. 273, Figs 19.1, 19.3). With $N=G=1000$ and $f(0)=0.5$, the sexual population follows the theoretical curve (19.14) "remarkably well". Panels (b) and (c) use mutation at $m=0.25/G$ and $m=6/G$, with and without sex. The time axes differ greatly from panel (a). In (b) the no-sex curve takes about 1500 generations (read from the plot). In (c), at $mG=6$, the no-sex population levels off near 700 and the sex population near 930 (read from the plot) (p. 275).

**Exercises 19.1, 19.2** (p. 275) ask how the results depend on population size and on the crossover mechanism.

### 19.3 The maximal tolerable mutation rate (pp. 275–276)
- Combining mutation and sex:
$$\frac{df}{dt}\simeq-2m\,\delta f+\eta\sqrt2\sqrt{\frac{m+f(1-f)/2}{G}}\tag{19.15}$$
This is positive if
$$m<\eta\sqrt{\frac{f(1-f)}G}.\tag{19.16}$$
- Without sex, from (19.8):
$$m<\frac1G\,\frac1{(2\,\delta f)^2}.\tag{19.17}$$
So the tolerable rate with sex is of order $\sqrt G$ times greater (p. 276).
- **Could bigger litters rescue asexuals?** If $mG$ bits flip on average, the chance of no flips is roughly $e^{-mG}$. A mother needs roughly $e^{mG}$ offspring to have one child as fit as herself. Litter size has to be exponential in $mG$ (if $mG>1$), if the species is to persist (p. 276).
- Thus the tolerable rate is pinned near $1/G$ without sex and is of order $1/\sqrt G$ with recombination (p. 276, Fig. 19.4).
- Reversed: for fixed $m$, the largest genome is of order $1/m$ (parthenogenetic) or $1/m^2$ (sexual). With $m=10^{-8}$ per nucleotide per generation (Eyre-Walker and Keightley, 1999) and a maximum brood of 20 000 ($mG\simeq10$), the prediction is that all species with more than $G=10^9$ coding nucleotides use recombination at least occasionally. For a brood of 12 the figure is $G=2.5\times10^8$ (p. 276).

### 19.4 Fitness increase and information acquisition (p. 276)
- Random bits give $F\approx G/2$. If all individuals reach $F=G$, the species has acquired $G$ bits: for each bit it has "figured out" the better state (p. 276).
- At intermediate fitness, information is defined as the selection (in bits) needed to pick the perfect state from the gene pool. Using the urn picture ($\log_2(1/f)$ bits to find a black ball when black:white is $f:1-f$), with $f_g$ the fraction of the population having $x_g=1$:
$$I=\sum_g\log_2\frac{f_g}{1/2}\ \text{bits.}\tag{19.18}$$
If all $f_g=F/G$,
$$I=G\log_2\frac{2F}{G},\tag{19.19}$$
well approximated by
$$\tilde I\equiv2(F-G/2).\tag{19.20}$$
The information rate is therefore about twice the rate of fitness increase (p. 276).

### 19.5 Discussion (pp. 277–279)
- The results quantify the known argument that recombination spreads useful mutations faster and clears deleterious ones faster. Sex acquires information of order $\sqrt G$ times faster and tolerates a mutation rate of order $\sqrt G$ times greater. Kondrashov (1988) noted this advantage; MacKay says it does not seem to have spread widely (p. 277).
- **"Cost of males."** The argument: of every two sexual offspring, one (on average) is a male who cannot bear children. A parthenogenetic mother passes on 100% of her genome rather than 50%, so single mothers should outbreed sexual cousins (p. 277).
- **Modified model.** One genome bit selects parthenogenesis ($x=1$) or sex ($x=0$). $K_p$ and $K_s$ are the numbers of children of a single mother and of a couple. MacKay concentrates on $K_p=K_s=4$, which favours parthenogens most. Their maximum tolerable mutation rate is then twice (19.17); at high fitness, $mG\simeq2$ (p. 277).
- **Results** (Fig. 19.5, $G=N=1000$, half the population initially parthenogenetic). While fitness rises quickly, pockets of parthenogens vanish within a couple of generations. At top fitness, parthenogens take over if the mutation rate is low ($mG=1$). They never take over at $mG=4$ (pp. 277–278).
- At $mG=4$, the sexual fitness spread is of order $\sqrt G$. A mutant parthenogenetic colony with slightly above-average fitness lasts about $\sqrt G/(mG)=1/(m\sqrt G)$ generations. If the population is large enough for some sexual individuals to survive that long, sex does not die out. In a sufficiently unstable environment, where the fitness function keeps changing, parthenogens will always lag (MacKay's argument). This is consistent with Haldane and Hamilton's (2002) parasite arms-race argument (p. 278).
- **Additive fitness.** Maynard Smith (1968) argues additivity is reasonable. With interactions, crossover might reduce average fitness. But sex helps most when fitness is additive, so MacKay predicts that evolution favoured genome representations with weak interactions. Even with interactions, fitness may still be a sum of interacting terms (p. 278). Exercise 19.3 asks the reader to simulate XOR-pair interactions (p. 279).
- **Baldwin effect (MacKay's conjecture).** If fitness is a highly nonlinear function of sequence (a small island of good sequences in a flat ocean), a faulty transcription or translation system would occasionally produce a working protein, more often near a good sequence. This smooths the fitness landscape. MacKay conjectures that, at least early on, the genetic code was implemented noisily (p. 279).
- MacKay believes the qualitative $\sqrt G$ scaling would survive more complex fitness and crossover models. Only in small, in-bred populations does he expect the benefits of sex to be diminished. Summary: "Why have sex? Because sex is good for your bits!" (p. 279).

### 19.6–19.7 Further exercises and solutions (pp. 279–280)
- Exercises 19.4–19.6 are listed below.
- **Solution to Ex. 19.1** (final result only). For small $N$, unlucky bits freeze into the bad state ("hitchhikers") and homogeneity fails. Experimentally, the theory fits poorly only if $N\lesssim\sqrt G$. If $N$ is much smaller than $\sqrt G$, a rate of $\sqrt G$ is impossible, since selection carries at most $2N$ bits per generation. Baum et al. (1995), analysing a similar model, say $N\approx\sqrt G(\log G)^2$ makes hitchhikers unlikely (p. 280).

## Toy example (ours, not from the text)
Take $G=4$. Parent $x=(1,1,1,0)$, so $F=3$, $f=0.75$, $\delta f=0.25$.

**Sex.** Take a mate $y=(1,1,0,1)$, also $F=3$. Bits 1, 2 are good in both, so they are always good. Bits 3 and 4 are good in exactly one parent, so each is a fair coin. The child's fitness is $2+\text{Bin}(2,\tfrac12)$: 2, 3, 4 with probabilities $\tfrac14,\tfrac12,\tfrac14$. The mean is $2\cdot\tfrac14+3\cdot\tfrac12+4\cdot\tfrac14=3$, the same as the parents. Keeping the upper half (4 with $\tfrac14$, plus 3 with $\tfrac14$) gives mean $(4\cdot\tfrac14+3\cdot\tfrac14)/\tfrac12=3.5$, a gain of $+0.5$.

**Mutation, $m=\tfrac14$.** Each of the three good bits stays good with probability $\tfrac34$. The bad bit becomes good with probability $\tfrac14$. Mean: $3\cdot\tfrac34+\tfrac14=2.5$. This matches (19.3): $(1-2m)\delta f=0.5\times0.25=0.125$, so $f=0.625$, $F=2.5$. The full distribution of $F$ (in 256ths) is 0:3, 1:28, 2:90, 3:108, 4:27 (sum 256). Keep the top half (128): all 27 fours and 101 of the 108 threes. The mean is $(4\cdot27+3\cdot101)/128=411/128\approx3.21$, a gain of $+0.21$.

Mutation first loses 0.5 and then selection recovers part of it. Sex loses nothing before selection. This is one family only, not a population simulation, but it shows the mechanism of Fig. 19.1.

## Concepts
- [[truncation-selection]] (new) — keep exactly the fittest $N$ children each generation; the "teacher" in the model (p. 271)
- [[additive-fitness-model]] (new) — fitness $F=\sum_g x_g$ over $G$ good/bad bits; locally linear fitness (p. 270)
- [[recombination-no-linkage]] (new) — each child bit is copied from either parent with probability ½ (p. 271)
- [[maximal-tolerable-mutation-rate]] (new) — largest $m$ at which mean fitness still rises: about $1/G$ without sex, of order $1/\sqrt G$ with sex (p. 276)
- [[information-acquired-by-selection]] (new) — $I=\sum_g\log_2(f_g/\tfrac12)$, bits needed to pick the good states from the gene pool (p. 276)
- [[redundancy]] — the selection signal's bits are redundant because similar unfit individuals fail for similar reasons (p. 269)
- [[bit]] — here the unit for the information gained by a species, and a genome bit's good/bad state (pp. 269, 276)
- [[baldwin-effect]] (new) — noisy transcription or translation lets learning-like noise smooth a nonlinear fitness landscape (p. 279)

## Canonical instances
- [[maynard-smith-1-bit-per-generation]] — the claimed rate of information acquisition, which the model confirms for asexuals (pp. 270, 272)
- [[urn-of-black-and-white-balls]] — $\log_2(1/f)$ bits to find a black ball, used to define acquired information (p. 276)
- [[parthenogenesis-vs-sex-simulation]] — the sex/parthenogen simulation of Fig. 19.5: parthenogens take over at $mG=1$ but never at $mG=4$ (p. 278)
- [[genome-size-limit-from-mutation-rate]] — the $10^9$ and $2.5\times10^8$ nucleotide predictions (p. 276)

## Bridges (candidates)
- [structural-analogy] Maximal tolerable mutation rate (error threshold) ↔ information-theory: noisy-channel capacity limit — mutation corrupts the genome "message", and sex raises the tolerable noise.
- [structural-analogy] Selection as a 1-bit-per-individual teacher ↔ Bayesian: updating from weak, redundant feedback.
- [metaphor] Baldwin effect via a noisy genetic code ↔ stochastic or noisy search that smooths a rugged objective.
- [structural-analogy] $I=\sum_g\log_2(f_g/\tfrac12)$ ↔ information-theory: bits gained relative to a uniform ½ prior per site.

## Questions this raises
- How do the $\sqrt G$ results change when fitness has strong interactions between bits (Ex. 19.3), or with linkage between nearby bits?
- Is $I=\sum_g\log_2(f_g/\tfrac12)$ the right measure of information when the bits of the genome are represented redundantly?
- What population size is needed for the homogeneity assumption to hold, given hitchhikers (the Ex. 19.1 solution)?
- If the genetic code was noisy, how would that change the information a species can acquire per generation?

## Exercises worth doing
- Ex. 19.2 (p. 275) — effect of lower crossover probability, or crossovers only at hot-spots every $d$ bits, on the theory of sex — difficulty: medium
- Ex. 19.3 (p. 279) — simulate sexual and asexual species with an XOR-of-pairs fitness function and compare with the additive case — difficulty: medium (computer)
- Ex. 19.5 (p. 280) — how DNA replication and protein synthesis reach error rates far below $\exp(-\Delta E/kT)$ — difficulty: hard
- Ex. 19.6 (p. 280) — estimate the information rate of long-term memory, to compare with the genome's few bits per generation — difficulty: easy

## Reading notes
- Printed pages 269–280 correspond to pdf 281–292 (printed = pdf − 12).
- Box 19.2 (p. 274) says the factor "in (19.2)" equals $\sqrt{2/(\pi+2)}\simeq0.62$. Equation (19.2) is the crossover rule, so this is probably a mis-reference to (19.13) or the mean-increase formula. I checked the algebra and the value 0.62 is consistent.
- Figure 19.3 values for fitness plateaus and times are read from the plots, not stated in the text.
- Section 19.5 mentions G ≃ $10^8$ coding nucleotides for "substantial" √G.
- The text layer for equations was garbled in places; I checked every equation against the page images.
