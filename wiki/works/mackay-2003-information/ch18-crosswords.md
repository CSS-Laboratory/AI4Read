---
id: mackay-2003-information/ch18-crosswords
work: mackay-2003-information
unit: "18 Crosswords and Codebreaking"
pages: 260-268
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Crosswords and Codebreaking

## L0 — One line
Information content, log evidence and weight of evidence are all logarithms of probabilities and share units; MacKay also uses crossword counts to bound the redundancy of language, and weight of evidence to score matches in Turing's Enigma codebreaking.

## L1 — The gist (≤ 120 words)
MacKay takes "a random walk" through language modelling. Counting possible crosswords gives a condition on the entropy of a simple model of English. Zipf–Mandelbrot and Dirichlet-process models of word frequencies are discussed. Information content, entropy, log evidence and log odds are all logarithms of probabilities, so they share units: bits, nats, bans and decibans. The ban comes from Bletchley Park, where Turing's team tallied Bayesian evidence against Enigma. Cyphertexts from machines in the same state, carrying English plaintext, tend to match slightly more often than random strings. In a monogram model, each match adds a fixed positive weight of evidence and each non-match subtracts a small one. Typically about 400 characters are needed to reach 20 decibans.

**Prerequisites:** logarithms; entropy and redundancy; typical sets (counting about 2^{nH} sequences); likelihood ratios and Bayes' theorem.

## L2 — Key ideas
- Crossword rules define a constrained channel (one where only some letter sequences are allowed). That many crosswords exist bounds the redundancy (how strongly a language's rules restrict which strings occur) of "word-English" (p. 260).
- Counting typical fillings against the chance of all words being valid gives a necessary condition on the dictionary entropy (the information per character of a model dictionary of $W$ words of length $L$), $H_W > \frac{f_wL-f_1}{f_w(L+1)}H_0$ (p. 261). With the book's numbers, type B is satisfied and type A is only just satisfied (p. 261).
- Zipf's law and Mandelbrot's three-parameter version are two proposed forms for the probability of the $r$th most common word. Emma fits well, the book's LaTeX source less well (pp. 262–263).
- A Dirichlet process (a rule that generates a stream of symbols using counts of the symbols seen so far) gives exchangeable streams (statistics the same everywhere in the stream) with unbounded vocabulary, but is not adequate for Zipf-like data. Declaring a character to be a "space" often gives nice Zipf plots when $\alpha$ is small (pp. 263–264).
- Information content, entropy, log evidence (log of the probability of the data under a hypothesis) and log odds (log of the ratio of two such probabilities) are all logs of probabilities, or averages of them, and share units: bit, nat, ban, deciban (pp. 264–265).
- Banburismus (Bletchley Park's Enigma inference procedure) tested two hypotheses, "same machine state" versus "different states", using the match probability (the chance that two independent letters coincide) $m=\sum_i p_i^2$ (pp. 265–267).
- The weight of evidence (the log likelihood ratio for the same-state hypothesis against the different-state one) is $M\log mA + N\log\frac{(1-m)A}{A-1}$, which builds up slowly: typically roughly 400 characters for 20 db in favour of one hypothesis or the other (pp. 267–268).

## L3 — Walkthrough

### 18.1 Crosswords (pp. 260–262)
**Setting.** Crossword rules define a constrained channel (a channel whose allowed sequences obey rules). That many valid crosswords exist shows its capacity is greater than zero (p. 260).
- Type A (American): every row and column is a succession of words of length ≥ 2 separated by spaces. Every letter lies in a horizontal and a vertical word.
- Type B (British): rows and columns mix words and single characters. Every character lies in at least one word. In a typical type B crossword only about half the letters lie in two words (p. 260).
- Type A is harder to create (no single characters allowed). Type B is generally harder to solve (fewer constraints per character) (p. 260).

**Why possible.** If a language had no redundancy, any letters on a grid would form a valid crossword. With high redundancy, crosswords are hard to make. So being able to make crosswords bounds the redundancy (p. 260). Crosswords use "word-English": strings of dictionary words separated by spaces (p. 260). Exercise 18.1 asks for its capacity (p. 260).

**Model: Wenglish.** $W$ words, all of length $L$ (section 4.1). Entropy per character, including spaces:
$$H_W \equiv \frac{\log_2 W}{L+1}. \tag{18.1}$$
For a crossword of $S$ squares, let there be $f_wS$ words and $f_1S$ letter-occupied squares. Table 18.2 gives (p. 261):

| | A | B |
|---|---|---|
| $f_w$ | $\frac{2}{L+1}$ | $\frac{1}{L+1}$ |
| $f_1$ | $\frac{L}{L+1}$ | $\frac34\frac{L}{L+1}$ |

Wenglish is assumed to be made by drawing $W$ strings from a memoryless (monogram) source with entropy $H_0$. Equal probability over $A=26$ letters gives $H_0=\log_2 A=4.7$ bits. Chapter 2's distribution gives 4.2 bits. Its redundancy has two sources: unequal letter use, and only $W$ words in the dictionary (p. 261).

**Counting.** Fill the squares at random from the same distribution and ask how likely every row and column is valid. The number of typical fillings is
$$|T| = 2^{f_1 S H_0}. \tag{18.2}$$
The probability that one word of length $L$ is valid:
$$\beta = \frac{W}{2^{LH_0}}. \tag{18.3}$$
The probability that a typical filling makes all $f_wS$ words valid is approximately
$$\beta^{f_w S}. \tag{18.4}$$
So the log of the number of valid crosswords is estimated as
$$\log \beta^{f_wS}|T| = S\left[(f_1 - f_wL)H_0 + f_w\log W\right] \tag{18.5}$$
$$= S\left[(f_1 - f_wL)H_0 + f_w(L+1)H_W\right]. \tag{18.6}$$
(Added step for (18.5): $\log\beta^{f_wS}|T| = f_wS(\log W - LH_0) + f_1SH_0$. Step to (18.6): $\log W=(L+1)H_W$ from (18.1).) This grows with $S$ only if
$$(f_1 - f_wL)H_0 + f_w(L+1)H_W > 0, \tag{18.7}$$
so arbitrarily many crosswords can be made only if
$$H_W > \frac{(f_wL-f_1)}{f_w(L+1)}H_0. \tag{18.8}$$
Margin caveat: this underestimates the count because it uses only typical fillings. If the monogram distribution is non-uniform, the true count is dominated by atypical fillings in which crossword-friendly words appear more often (p. 261).

**Result (table on p. 261).** Type A needs $H_W>\frac12\frac{L}{L+1}H_0$. Type B needs $H_W>\frac14\frac{L}{L+1}H_0$. (Added step: for A, $f_wL-f_1=\frac{L}{L+1}$ and $f_w(L+1)=2$. For B, $f_wL-f_1=\frac14\frac{L}{L+1}$ and $f_w(L+1)=1$.)

**Numbers.** Take $H_0=4.2$ bits, $W=4000$ words, $L=5$. Then type B is satisfied and type A is only just satisfied. This fits the author's experience that type A crosswords use more obscure words (p. 261). (Added check: $H_W=\log_2 4000/6\approx 2.0$, against thresholds about 1.75 for A and 0.875 for B.)

> **Intuition note.** Each word placed must be a real word. That costs bits, and the squares of the grid supply bits of freedom. Arbitrarily many crosswords are possible only if the dictionary is rich enough that the constraints cost less than the freedom gives. Type A has more words per square and a higher threshold on $H_W$, so it needs a richer dictionary.

**Further reading (p. 262).** Shannon (1948) first made these observations; the author learned them from Wolf and Siegel (1998). The topic relates to capacity of two-dimensional constrained channels (e.g. 2-D bar-codes). Exercise 18.2 is a 2-D channel in which each interior pixel has four black and four white neighbours (p. 262).

### 18.2 Simple language models (pp. 262–264)
**Zipf–Mandelbrot.** The monogram model draws each word independently from a distribution over words. Zipf's law says the $r$th most probable word has probability approximately
$$P(r) = \frac{\kappa}{r^\alpha}, \tag{18.9}$$
with $\alpha$ close to 1 and $\kappa$ a constant. A log–log plot of frequency against rank should then be a straight line of slope $-\alpha$ (p. 262). Mandelbrot adds a parameter $v$:
$$P(r) = \frac{\kappa}{(r+v)^\alpha}. \tag{18.10}$$
It fits Jane Austen's *Emma* well, with $\kappa=0.56$, $v=8.0$, $\alpha=1.26$ (fig. 18.4). The LaTeX source of the book is qualitatively linear but visibly curved (fig. 18.5). The author notes this file mixes English, maths symbols and LaTeX commands (pp. 262–263).

**Dirichlet process.** Two requirements for a generative monogram model (p. 263):
1. Vocabulary is unbounded. Some probability must go to words never used before.
2. Exchangeability. Statistical properties of the generated stream are homogeneous, so the probability of a word at a location is the same everywhere in the stream.

The Dirichlet process has one parameter $\alpha$. After a stream of $F$ symbols with counts $\{F_w\}$:
$$P(\text{new symbol}) = \frac{\alpha}{F+\alpha}, \tag{18.11}$$
$$P(\text{symbol } w) = \frac{F_w}{F+\alpha}. \tag{18.12}$$
(Added check: these sum to 1, since $\sum_w F_w=F$.) Zipf plots of million-symbol documents for $\alpha$ from 1 to 1000 (fig. 18.6) lead the author to say a Dirichlet process is not an adequate model for data roughly obeying Zipf's law (p. 263).

**The tweak.** Generate elementary symbols from a Dirichlet process with small $\alpha$, so that about 27 symbols are reasonably frequent. Declare one of them a space. Strings between spaces are "words". The word frequencies then often give very nice Zipf plots (fig. 18.7, $\alpha=2$). The choice of space character sets the slope: a less probable space character gives a richer language and a shallower slope (p. 264).

> **Intuition note.** The rule "copy an old symbol in proportion to its count, or invent a new one with weight $\alpha$" lets popular symbols get more popular while the vocabulary keeps growing. If one symbol is declared a space, the strings between spaces often give a Zipf-like spread of word frequencies.

### 18.3 Units of information content (pp. 264–265)
Definitions:
$$h(x)=\log\frac{1}{P(x)}, \tag{18.13}$$
$$H(X)=\sum_x P(x)\log\frac{1}{P(x)}. \tag{18.14}$$
For hypotheses $\mathcal H_i$ and data $D$:
$$\text{`log evidence for }\mathcal H_i\text{'}=\log P(D\,|\,\mathcal H_i), \tag{18.15}$$
$$\text{log odds}=\log\frac{P(D\,|\,\mathcal H_1)}{P(D\,|\,\mathcal H_2)}, \tag{18.16}$$
also called the "weight of evidence in favour of $\mathcal H_1$" (p. 264).

The log evidence is the negative of the information content of $D$. Data with large information content are surprising to that hypothesis. A hypothesis less surprised by the data becomes more probable. The author says information content, surprise value and log likelihood or log evidence "are the same thing" (p. 264).

Units depend on the log base (table 18.8): bit ($\log_2$), nat ($\log_e$), ban ($\log_{10}$), deciban ($10\log_{10}$). A backup name for bit is shannon. A byte is 8 bits; a megabyte is $2^{20}\simeq10^6$ bytes (p. 265).

**History of the ban.** At Bletchley Park, Turing and others faced a huge inference problem: from the day's cyphertext, infer which three wheels were in the Enigma machines, their starting positions, the steckerboard substitutions, and the messages. The methods were Bayesian; the units were decibans or half-decibans. The deciban was judged the smallest weight of evidence discernible to a human. Evidence was tallied on sheets printed in Banbury, hence "ban" and "Banburismus" (p. 265).

### 18.4 A taste of Banburismus (pp. 265–268)
The author says his description is pieced together from Sale and Good and hopes it is "not too inaccurate" (p. 265).

**Setting.** There were about $8\times10^{12}$ possible machine settings. Good: "it was therefore necessary to find about 129 decibans from somewhere" (p. 265). Banburismus aimed only at which wheels were in use. The bombes, fed with plaintext guesses (cribs), then found the wheel settings (p. 265).

The machine implemented a changing permutation cypher, moving deterministically through a state space of $26^3$ permutations. With many messages per day, two machines were likely to be in the same state at some point. They then stayed in step. The resulting correlations gave a "dribble of information-content" yielding the daily 129 decibans (pp. 265–266).

**Hypotheses.** $\mathcal H_0$: the machines are in different states and the plain messages are unrelated. $\mathcal H_1$: the machines are in the same state and the plain messages are unrelated. The data are cyphertexts $\mathbf x,\mathbf y$ of length $T$ over an alphabet of size $A$ (26). No attempt is made to infer the state (p. 266).

**Under $\mathcal H_0$:**
$$\mathbf x = c_1(u_1)c_2(u_2)\dots \tag{18.17}$$
$$\mathbf y = c_1'(v_1)c_2'(v_2)\dots \tag{18.18}$$
with $c_t, c'_t$ unrelated time-varying permutations. If each machine is an ideal random time-varying permutation, all cyphertexts are equally likely:
$$P(\mathbf x,\mathbf y\,|\,\mathcal H_0)=\left(\tfrac1A\right)^{2T}. \tag{18.19}$$

**Under $\mathcal H_1$:** a single $c_t$ underlies both:
$$\mathbf x=c_1(u_1)c_2(u_2)\dots,\qquad \mathbf y=c_1(v_1)c_2(v_2)\dots \tag{18.20, 18.21}$$
If the plaintext were completely random, $\mathcal H_0$ and $\mathcal H_1$ would be indistinguishable. But plaintext has redundancy. Some letters are commoner, so two unrelated plaintexts are slightly more likely to share letters. Common bigrams and trigrams give bursts of 2 or 3 matches (p. 266). Table 18.9: two aligned English plaintexts of length $T=74$ have twelve matches, including a run of six, against about 3 expected for random strings. The corresponding cyphertexts from machines in the same state would also have twelve matches (p. 267). Codebreakers hunted for pairs of messages with suspiciously many matching monograms, bigrams and trigrams. The method was first used by Rejewski (p. 267).

**Monogram model.** Letters are i.i.d. from $\{p_i\}$ (fig. 2.1). The probability that two letters match is the match probability
$$\sum_{u_t,v_t}P(u_t)P(v_t)\,\mathbb 1[u_t=v_t]=\sum_i p_i^2\equiv m. \tag{18.22}$$
For English and German, $m$ is about $2/26$, not $1/26$ (p. 267). With $c_t$ an ideal random permutation:
$$P(x_t,y_t|\mathcal H_1)=\begin{cases}\dfrac mA & x_t=y_t\\[2mm]\dfrac{1-m}{A(A-1)} & x_t\ne y_t.\end{cases}\tag{18.23}$$
For $M$ matches and $N$ non-matches ($M+N=T$), the log evidence for $\mathcal H_1$ is
$$\log\frac{P(\mathbf x,\mathbf y|\mathcal H_1)}{P(\mathbf x,\mathbf y|\mathcal H_0)}=M\log\frac{m/A}{1/A^2}+N\log\frac{(1-m)/(A(A-1))}{1/A^2}\tag{18.24}$$
$$=M\log mA+N\log\frac{(1-m)A}{A-1}.\tag{18.25}$$
Every match favours $\mathcal H_1$ by $\log mA$. Every non-match favours $\mathcal H_0$ by $\log\frac{A-1}{(1-m)A}$ (p. 267).

Numbers for monogram English (p. 267): $m=0.076$; $1/A=0.037$; per match $10\log_{10}mA=3.1$ db; per non-match $10\log_{10}\frac{(1-m)A}{A-1}=-0.18$ db.

**Worked cases (p. 267).**
- $M=4$, $N=47$, $T=51$: weight of evidence $+4$ db, a likelihood ratio of 2.5 to 1 for $\mathcal H_1$.
- For $T=20$, if $\mathcal H_1$ is true, matches occur at rate $m$ and the expected weight is 1.4 db per 20 characters.
- If $\mathcal H_0$ is true, spurious matches occur at rate $1/A$ and the expected weight is $-1.1$ db per 20 characters (pp. 267–268).
- Typically about 400 characters must be inspected to get more than 100 to 1 (20 db) in favour of one hypothesis or the other (p. 268).

> **Intuition note.** A match is rare under $\mathcal H_0$ (rate $1/A$) but commoner under $\mathcal H_1$ (rate $m$). So it earns a large bonus, while each non-match costs a small penalty. Evidence therefore accumulates slowly, but on average in the right direction.

**Refinements (p. 268).** English matches come in bursts because consecutive letters are dependent. Using better language models, Turing worked out and Good refined a scoring system that used runs of matches more accurately. Positive results went to automated and human codebreakers. According to Good, the longest false positive was 8 consecutive matches between machines in unrelated states (p. 268). Further reading: Hodges (1983), Good (1979), Schneier (1996) (p. 268).

### 18.5 Exercises (p. 268)
Exercise 18.3 concerns Enigma never mapping a letter to itself. It asks how much information per character this leaks, and how long a crib (a plaintext guess) must be to confirm its alignment and to identify the key (p. 268).

## Toy example (ours, not from the text)
Take $A=4$ letters with monogram probabilities $(\tfrac12,\tfrac12,0,0)$. Zero probabilities are chosen only to make the arithmetic clean.
- Match probability: $m=\tfrac14+\tfrac14=\tfrac12$.
- Under $\mathcal H_0$, each pair has probability $1/A^2=1/16$.
- Under $\mathcal H_1$ (18.23), a matching pair has probability $m/A=\tfrac18$. A non-matching pair has probability $\frac{1-m}{A(A-1)}=\frac{0.5}{12}=\frac1{24}$.
- (Check: $4\cdot\frac18=\frac12$ and $12\cdot\frac1{24}=\frac12$, so the total is 1.)
- Per-position likelihood ratios: match $\frac{1/8}{1/16}=2=mA$, giving $\log_2 2=+1$ bit. Non-match $\frac{1/24}{1/16}=\frac23=\frac{(1-m)A}{A-1}$, giving $\log_2\frac23\approx-0.585$ bits.
- Suppose $T=6$ with $M=3$, $N=3$. By (18.25) the weight is $3(1)+3(-0.585)=1.245$ bits. The likelihood ratio is $2^3\times(2/3)^3=8\times\frac{8}{27}=\frac{64}{27}\approx2.37$ to 1 for $\mathcal H_1$. (Check: $\log_2\frac{64}{27}=6-4.755=1.245$.)

## Concepts
- [[redundancy]] — here: why crosswords constrain a language. No redundancy means any grid is valid, and high redundancy makes crosswords hard (p. 260).
- [[entropy H(X)]] — average information content (18.14); for Wenglish, $H_W=\log_2W/(L+1)$ per character, spaces included (pp. 261, 264).
- [[self-information / surprisal]] — $h(x)=\log 1/P(x)$ (18.13); the author equates it with surprise value and log evidence (p. 264).
- [[typical set / AEP]] — used to count the $2^{f_1SH_0}$ typical fillings (p. 261).
- [[marginal likelihood (evidence)]] — here $\log P(D|\mathcal H_i)$, the "log evidence", the negative of the data's information content under $\mathcal H_i$ (p. 264).
- [[exchangeability]] — here: statistical properties of the generated text are homogeneous along the stream (p. 263).
- [[bit]] — one unit of information content, alongside nat, ban and deciban; backup name shannon (p. 265).
- [[constrained-channel-capacity]] (new) — crossword rules as a channel with allowed sequences; many valid crosswords imply capacity above zero (p. 260).
- [[wenglish]] (new) — $W$ words all of length $L$, built from a monogram source, used to model word-English (p. 261).
- [[zipf-mandelbrot-law]] (new) — $P(r)=\kappa/(r+v)^\alpha$; Zipf's law has $v=0$ (pp. 262–263).
- [[dirichlet-process]] (new) — new symbol with probability $\alpha/(F+\alpha)$, symbol $w$ with $F_w/(F+\alpha)$; exchangeable, unbounded vocabulary (p. 263).
- [[weight-of-evidence]] (new) — log likelihood ratio (log odds), in bans or decibans (pp. 264–265).
- [[match-probability]] (new) — $m=\sum_i p_i^2$, the chance two independent letters coincide (p. 267).

## Canonical instances
- [[crossword-counting]] — type A and B crossword conditions on $H_W$ (pp. 260–261).
- [[zipf-plot-emma]] — Zipf–Mandelbrot fit to *Emma*, $\kappa=0.56,v=8.0,\alpha=1.26$ (p. 262).
- [[banburismus]] — Enigma "same state" test; 129 decibans needed; $+3.1$ db per match (pp. 265–267).
- [[little-jack-horner-matches]] — two English plaintexts with twelve matches in 74 characters (p. 267).

## Bridges (candidates)
- [same-math] Weight of evidence $\log\frac{P(D|\mathcal H_1)}{P(D|\mathcal H_2)}$ ↔ bayesian: log Bayes factor / posterior log odds minus prior log odds — the same likelihood ratio, expressed in decibans.
- [structural-analogy] Adding $\log mA$ per match and subtracting for non-matches ↔ bayesian: sequential updating — independent observations contribute additive log-likelihood-ratio terms.
- [structural-analogy] Dirichlet process predictive rule (18.11–18.12) ↔ bayesian: exchangeable sequences with a growing vocabulary of values.
- [structural-analogy] Counting valid crosswords by $|T|\beta^{f_wS}$ ↔ information-theory: typical-set counting for constrained channels.

## Questions this raises
- The count of valid crosswords is underestimated by using only typical fillings. How much larger could the true count, and the threshold on $H_W$, be?
- What language model would reproduce Zipf plots like *Emma*'s directly, rather than via the space-character tweak?
- How would the weight of evidence per character change if bigram and trigram statistics, not only monograms, were used?
- What does the 8-match false positive imply about the error rate of this kind of scoring?

## Exercises worth doing
- Ex. 18.1 (p. 260) — estimate the capacity of word-English as a constrained channel — difficulty: medium
- Ex. 18.2 (p. 262) — capacity of a 2-D channel with four black and four white neighbours — difficulty: hard
- Ex. 18.3 (p. 268) — information leaked when Enigma never maps a letter to itself, and the crib lengths needed — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 272–280 are printed 260–268).
- Equations were read from the page images and checked against the text layer. Equation (18.18) shows primes on $c$ in the image.
- In the table on p. 267 the per-match value $3.1$ db does not exactly match $10\log_{10}(0.076\times26)\approx2.96$. The per-non-match value $-0.18$ differs slightly from the computed $-0.17$. The pages do not say why; I kept the printed values.
- Figure 18.1 crossword grids and figures 18.3–18.7 are described only from their captions and general appearance.
