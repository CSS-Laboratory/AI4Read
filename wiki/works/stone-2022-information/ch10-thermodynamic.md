---
id: stone-2022-information/ch10-thermodynamic
work: stone-2022-information
unit: "10 Thermodynamic Entropy and Information"
pages: 203–216
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
# Thermodynamic Entropy and Information

## L0 — One line
Shannon's information entropy and physical (Boltzmann–Gibbs) entropy are syntactically similar in form, and one bit has a minimum energy cost of 0.693kT joules, which is why Maxwell's demon cannot get free power.

## L1 — The gist (≤ 120 words)
The chapter asks how entropy in physics relates to entropy in information theory. Physical entropy is the logarithm of the number of microstates (detailed arrangements) that give one macrostate (the observable state, such as temperature). With equally probable microstates it has a syntactically similar form to Shannon's $H=\log W$. Squeezing a one-molecule gas into half a jar removes exactly one bit and lowers physical entropy by $k\ln 2$. This gives the Landauer limit: acquiring or erasing a bit costs at least $0.693kT$ joules ($k$: Boltzmann's constant; $T$: temperature in kelvin). The limit explains why Maxwell's demon, who sorts molecules using information, cannot produce net energy. Information therefore has a measurable physical price.

**Prerequisites:** logarithms (base 2 and natural); Shannon entropy $H=\sum p\log(1/p)$; equally likely outcomes.

## L2 — Key ideas (5–10 bullets)
- Physical entropy is the log of the number of microstates consistent with a macrostate. Microstates in one macrostate are equally probable, so macrostates with more microstates are more probable (pp. 204–206).
- Boltzmann's $S=k\ln W$ is syntactically similar to Shannon's $H=\log W$ for equiprobable outcomes. Gibbs' formula is similar in form to Shannon's general formula (p. 207).
- A variable with unequal outcome probabilities and entropy $n$ bits behaves like a system with $2^n$ equally probable microstates, even if $2^n$ is not an integer (p. 208).
- Confining a one-molecule gas to half a jar lowers entropy by $\Delta S=k\ln 2$, which is $\Delta H=1$ bit (pp. 209–210).
- Landauer limit: acquiring a bit needs at least $0.693kT$ joules. About $3\times10^{-21}$ J at 313 K (pp. 210–211).
- The second law (isolated-system entropy rises to a maximum) is made plausible by counting: at a given temperature almost all states have high entropy. The author says it is not tautological (p. 211).
- Maxwell's demon needs information to sort molecules. The energy cost of that information balances the energy gained, so there is no net gain (pp. 213–214).

## L3 — Walkthrough

### 10.1 Introduction (p. 203)
Entropy was defined in physics by Boltzmann (1872) and Gibbs (1878), and in mathematics by Shannon (1948). Thermodynamic entropy measures the number of states a physical system can adopt. Shannon's entropy measures information. They look unrelated, but the relation matters. Thermodynamic entropy can measure the energy cost of Shannon information. If this were false, Maxwell's demon could run power stations on pure information (p. 203).

### 10.2 Physics, entropy and disorder (pp. 204–206)
- **Feynman's account** (quoted): divide the jar into small volume elements. There are many more ways to arrange black and white molecules with no restriction than with white on one side and black on the other. "Disorder" is the number of ways the insides can be arranged so the outside looks the same. Entropy is the logarithm of that number (p. 204).
- A **microstate** is one exact arrangement. A **macrostate** is the outside appearance, a global parameter such as temperature. Swapping two black molecules gives a new microstate but the same macrostate (p. 204).
- Temperature corresponds to a distribution of molecule speeds. Swapping the speeds of two molecules leaves it unchanged, so each macrostate has many microstates (p. 205).
- The author says there is no reason to suppose molecule A has speed $S_1$ and B has $S_2$ rather than the reverse. So all microstates consistent with one macrostate are equally probable (p. 205).
- Entropy of a macrostate is proportional to the log of the number of its microstates (p. 205).
- Figure 10.2: with fast and slow molecules anywhere in the jar (a), there are many more arrangements than with all fast ones in one half (b). The (b) macrostate has one hot half and one cold half. Swapping speeds between halves would change the half temperatures (pp. 205–206).
- Hence macrostates with an equal mix of fast and slow molecules in both halves (Fig. 10.3) are much more probable than the hot-half/cold-half macrostate. The probable macrostate has high entropy and the improbable one has low entropy (p. 206).
- **Key point:** macrostates with many microstates are more probable than those with few (p. 206).

*Intuition note.* "Disorder" here just means "many equivalent arrangements". A mixed jar is common because there are so many ways to be mixed.

### 10.3 Information and thermodynamic entropy (p. 207)
The author checks whether the definitions are "syntactically similar".
- Shannon: $$H=\sum_{i=1}^{m}p(x_i)\log\frac{1}{p(x_i)}\tag{10.1}$$
- With $W$ equally probable outcomes, $p(x_i)=1/W$: $$H=\sum_{i=1}^{W}\frac1W\log W\tag{10.2}$$ $$=\log W\tag{10.3}$$
- Boltzmann (natural log): $$S=k\ln W\tag{10.4}$$ Here $k=1.38\times10^{-23}$ joules/degree (Kelvin scale).
- Gibbs' generalisation: $$S=k\sum_{i=1}^{m}p(x_i)\ln\frac{1}{p(x_i)}\ \text{joules/degree}\tag{10.5}$$ where $m$ is the number of macroscopically distinguishable configurations.
- Eq. 10.3 resembles 10.4, and 10.1 resembles 10.5 (p. 207).

### 10.4 Ensembles, macrostates and microstates (p. 208)
- An **ensemble** is the set of all microstates yielding one macrostate (p. 208).
- Dice analogy: the 11 summed outcomes are macrostates, and pairs of values are microstates. Sum 7 has many microstates and sum 2 has few. So a many-microstate macrostate is more probable (p. 208).
- If each microstate corresponds to exactly one macrostate, entropy is also the log of the number of macrostates. Example: an 11-sided die has entropy $\log 11=3.46$ bits, and $2^{3.46}=11$ equiprobable macrostates (p. 208).
- Two dice have the same entropy as a single die with $2^{3.27}=9.65$ sides. Such a die is physically impossible, but it corresponds to 9.65 equally probable microstates (p. 208).
- More generally, a variable with unequal macrostate probabilities and entropy $n$ bits behaves like a system with $2^n$ equally probable microstates (p. 208).

### 10.5 Pricing information: the Landauer limit (pp. 209–211)
The Landauer limit is a lower bound on the energy needed to acquire or transmit one bit. von Neumann (1961) first proposed its value, and Landauer (1961) developed it (p. 209).
- Setup: a gas of a single molecule. It is pushed into half the jar at constant temperature. The jar is divided into $W_1$ small cubes, and the molecule's cube is its microstate. In the half jar, $W_2=W_1/2$ (p. 209).
- Entropies: $S_1=k\ln W_1$ (10.6) and $S_2=k\ln W_2$ (10.7) (p. 209).
- Decrease on confinement: $$\Delta S=k\ln W_1-k\ln W_2\tag{10.8}$$ $$=k\ln 2W_2-k\ln W_2\tag{10.9}$$ $$=k\ln 2(W_2/W_2)\tag{10.10}$$ $$=k\ln 2\ \text{joules/degree}\tag{10.11}$$ This holds however small the cubes are (pp. 209–210).
- Multiplying by temperature: $$T\Delta S=kT\ln 2\tag{10.12}$$ $$=0.693\times kT\ \text{joules}\tag{10.13}$$ (p. 210).
- In information terms, $H_1=\log_2W_1$ and $H_2=\log_2W_2$, so $$\Delta H=\log_2(W_1/W_2)\tag{10.14}$$ $$=1\ \text{bit}\tag{10.15}$$ (p. 210).
- So $\Delta S=0.693k$ J/degree corresponds to $\Delta H=1$ bit. Landauer showed the smallest energy to erase (or acquire) one bit is $$1\text{ bit}=0.693k\ \text{joules/degree}\tag{10.16}$$ $$=9.57\times10^{-24}\ \text{joules/degree}\tag{10.17}$$ (p. 210).
- The author says the limit rises with temperature because the information must overcome random fluctuations (noise), which grow with temperature. At $T=313$ K (40 °C): $$9.57\times10^{-24}\times T=3\times10^{-21}\ \text{joules/bit}\tag{10.18}$$ (p. 210).
- Interpretation: at first we have no information about which half holds the gas. Restricting it removes one bit of uncertainty. The energy to force the gas into half the jar cannot be below $T\Delta S=0.693kT$ J, which is also the cost of reducing this gas's information entropy by one bit (pp. 210–211).
- Caveat: strictly, the account applies only to logically irreversible binary operations, such as erasing (forgetting) information after an observation. Bérut et al. (2012) found evidence for the limit. Koski et al. (2014) found evidence that it can almost be achieved (p. 211).
- **Key point:** any physical device, however efficient, can acquire one bit only if it expends at least $0.693kT$ joules (p. 211).

*Intuition note.* Halving the space the molecule can occupy removes one bit of uncertainty about where it is. The author gives a minimum energy cost for forcing this, and it is proportional to temperature.

### 10.6 The second law of thermodynamics (pp. 211–212)
- The law: the entropy of an isolated system (no energy exchanged with the outside) increases until it reaches a maximum (p. 211).
- The author says the preceding analysis gives a statistical rationale. Given a few assumptions about the rules of probability, this makes us fairly certain that a system will adopt a high-entropy state, since at any given temperature almost all states have high entropy (p. 211).
- It seems almost tautological, "But it is not". It seems so only because we built up our picture of entropy from assumptions based on physically valid observations about the laws of probability (p. 211).
- A system left alone passes through macrostates of rising entropy ("running uphill" in entropy, "downhill" in order) until equilibrium, the maximum-entropy state (pp. 211–212).
- Example: push all molecules into half the jar with cardboard, then remove it. The gas fills the jar, because microstates that are evenly spread far outnumber those confined to one half (p. 212).
- Greene (quoted): we should never be surprised by, or feel the need to explain, why any physical system is in a high-entropy state (p. 212).

### 10.7 Maxwell's demon (pp. 212–214)
- **Setup.** In 1871 Maxwell proposed a demon sitting by a door in a partition between halves A and B of a gas container. The author says it cannot provide free energy "not even in principle" (p. 212).
- **Sorting.** The demon opens the door (assumed to cost no energy) for fast molecules heading from A to B and for slow ones heading from B to A. Over time, fast molecules gather in B (hot) and slow ones in A (cold) (Fig. 10.4, p. 213).
- **Use.** The temperature difference could drive work, as in a steam engine or a power station fed only with hot air (p. 213).
- **The catch.** The demon needs information about each molecule's speed and direction. Each bit costs at least $0.693kT$ J (Eq. 10.16) (p. 213).
- **Balance.** If the energy extracted per molecule exceeded the Landauer limit, there would be a net profit. The author says the usable energy gained is exactly balanced by the energy needed to get the information, so the energy generated cannot exceed the energy the demon spends (pp. 213–214).
- This is a fundamental link between Shannon entropy and thermodynamic entropy. Gabor (1951): "We cannot get anything for nothing, not even an observation" (p. 214).
- Pratchett (a novelist, "on a lighter note") speculated that knowledge needs physical storage, so that nine-tenths of the universe is knowledge about the other tenth (p. 214).

*Intuition note.* The demon's sorting looks free only if we ignore the cost of looking. Counting that cost balances the gain, so there is no net profit.

### 10.8 Quantum computation (p. 215)
- Grover's 1996 program should play "20 questions" in about $\sqrt{20}=4.47$, so five, steps. In general it should play N questions with about $\sqrt N$ quantum questions (p. 215).
- Trade-off: $N$ simple steps (conventional) against $\sqrt N$ complex steps (quantum). The quantum computer wins clearly if its $\sqrt N$ steps run faster than the conventional $N$ steps (p. 215).
- Only simple quantum computers exist so far. The 1949 *Popular Mechanics* quote about computers of the future is an analogy for slow starts (p. 215).

### 10.9 Summary (pp. 215–216)
The chapter reinforces that entropy and Shannon information have tangible physical counterparts. The author reads Wheeler's "All things physical are information-theoretic in origin" as non-metaphorical. The most remarkable fact is that information has a definite lowest cost in joules per bit. More than any other, this fact establishes the existence of a fundamental link between Shannon entropy and Boltzmann–Gibbs entropy (pp. 215–216).

## Toy example (ours, not from the text)
A one-molecule gas in a jar of $W_1=8$ equal cells. Confine it to the left half, so $W_2=4$.
- $H_1=\log_2 8=3$ bits and $H_2=\log_2 4=2$ bits, so $\Delta H=1$ bit.
- $\Delta S=k\ln 8-k\ln 4=k\ln 2=0.693k$.
- At $T=300$ K, the minimum energy is $9.57\times10^{-24}\times300=2.87\times10^{-21}$ J.

Macrostate counting with two fair coins, where the macrostate is the number of heads: 0 heads has 1 microstate (TT), 1 head has 2 (HT, TH), and 2 heads has 1 (HH). Each microstate has probability 1/4, so the macrostates have probabilities 1/4, 1/2 and 1/4. The "1 head" macrostate is the most likely because it has the most microstates.

## Concepts
- [[entropy-H]] — Shannon entropy; equals $\log W$ for $W$ equally probable outcomes (pp. 207–208)
- [[microstate-macrostate]] (new) — a microstate is one exact arrangement. A macrostate is an observable global state, which many microstates can produce (p. 204)
- [[thermodynamic-entropy]] (new) — Boltzmann's $S=k\ln W$ and Gibbs' $S=k\sum p\ln(1/p)$, in joules/degree (p. 207)
- [[ensemble]] (new) — the set of microstates that yield one macrostate (p. 208)
- [[landauer-principle]] — acquiring or erasing one bit costs at least $0.693kT$ joules (pp. 210–211)
- [[second-law-thermodynamics]] (new) — entropy of an isolated system rises to a maximum (p. 211)
- [[bit]] — here tied to a physical change, $\Delta H=1$ bit for halving the available states (p. 210)

## Canonical instances
- [[gas-jar-one-molecule]] — confining one molecule to half a jar gives $\Delta S=k\ln2$ and $\Delta H=1$ bit (pp. 209–210)
- [[maxwells-demon]] — sorting molecules by information gives no net energy, because information costs at least the Landauer limit (pp. 212–214)
- [[two-dice-macrostates]] — summed dice as macrostates, and entropy as an effective number of sides (p. 208)
- [[grover-20-questions]] — about $\sqrt N$ quantum questions for $N$ questions (p. 215)

## Bridges (candidates)
- [same-math] Boltzmann $S=k\ln W$ and Gibbs $S=k\sum p\ln(1/p)$ ↔ information theory: $H=\log W$ and $H=\sum p\log(1/p)$ — same form, up to the constant $k$ and the log base.
- [same-math] "Entropy $n$ bits ≈ $2^n$ equiprobable states" ↔ language modelling: perplexity $=2^{\text{entropy}}$ — the effective number of choices.
- [structural-analogy] Macrostate/microstate counting ↔ typical set: most outcomes fall in a huge set of roughly equiprobable states.
- [metaphor] Maxwell's demon paying for observation ↔ any agent whose information gathering has a cost (e.g. rational inattention).

## Questions this raises
- The author says the account applies "only to logically irreversible binary operations" such as erasing (p. 211), yet also states the limit for acquiring a bit (pp. 210–211). How are the two statements related?
- How close do real computers and brains come to $0.693kT$ per bit?
- Is the second law really derivable from probability alone? The author says it is not tautological (p. 211). What further assumptions are involved?
- Does Grover's $\sqrt N$ speed-up have any link to the information cost of questions?

## Reading notes
- Printed page = pdf − 16 (pdf 219 = p. 203).
- The running head on even pages reads "8 Thermodynamic Entropy and Information", although this is Chapter 10.
- Eq. 10.10 is printed as "$k\ln 2(W_2/W_2)$". This is equal to $k\ln(2W_2/W_2)=k\ln 2$, following Eq. 10.9.
- Eq. 10.16–10.17 give "joules/degree". Multiplying by $T$ gives joules.
- Section 3.5 (outside these pages) is cited only for the idea that dice sums are the same for different pairs. The entropy of two dice is not derived here: the text only states that two dice have the same entropy as a die with $2^{3.27}=9.65$ sides.
- Superscript numbers are reference numbers. The bibliography is not in these pages.
- Figures were checked against the page images. No equation was unreadable.
