---
id: shannon-1951-prediction/main
work: shannon-1951-prediction
unit: paper
pages: 50–64
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 6
---
# Prediction and Entropy of Printed English

## L0 — One line
Shannon estimates the entropy of English by having people guess the next letter, and he proves bounds that turn an ideal predictor's guess-number frequencies into bounds on the N-gram entropy.

## L1 — The gist (≤ 120 words)
How many bits per letter does English need once long-range structure counts? Tables of N-letter frequencies were not available beyond N = 3. Shannon has people guess the next letter and records how many guesses each letter takes. These guess numbers form a "reduced text" from which the original can, at least in principle, be recovered by an identical predictor. Their frequencies give an upper and a lower bound on the N-gram entropy; the lower bound is proved for an ideal predictor only. For 27-letter English with 100 letters known, his data give bounds of 1.3 and 0.6 bits per letter. He says it appears that entropy is of the order of one bit per letter, with redundancy roughly 75%.

**Prerequisites:** base-2 logarithms; entropy as average uncertainty; conditional probability; sums over a table of rows and columns; convex ("concave upward") functions: second derivative > 0 means the curve bends upward.

## L2 — Key ideas
- Speakers know a great deal of English statistics implicitly. Guessing the next letter therefore tests that knowledge. It extends the estimate beyond what N-gram tables (frequency tables of N-letter blocks; digram = 2 letters, trigram = 3) allow (pp. 50, 52, 54).
- Table-based values for 26 letters: $F_0 = 4.7$, $F_1 = 4.14$, $F_2 = 3.56$, $F_3 \approx 3.3$ bits/letter. Word frequencies (Zipf-type law) give an estimate of 2.62 bits/letter. Shannon says this corresponds more nearly to, say, $F_5$ or $F_6$ than to $F_{4.5}$, because the $F_N$ curve at 4.5 lies above it (pp. 51–54).
- Replacing each letter by its guess number gives the "reduced text". It carries the same information, in the sense that the original can in principle be recovered with an identical predictor. The redundancy shows up as very unequal frequencies of the numbers (pp. 55–56).
- In Experiments 1–2, a good subject guessed about 69–77% of letters on the first try. Prediction improves with more known letters, apart from statistical fluctuation. Reverse prediction was only slightly poorer (pp. 55–58).
- An ideal N-gram predictor guesses in order of decreasing conditional probability. Its first-$S$-guess success frequencies cannot fall when N rises (11) (pp. 58–59).
- Any transducer (a device translating an input sequence into an output sequence) whose output depends only on the present letter and the N−1 preceding letters, and which is instantaneously reversible, satisfies (15). So the ideal predictor's output frequencies majorize (are more concentrated than, in the sense of (15)) those of such a transducer (pp. 60–61).
- Bounds (17): the upper bound is valid for any predictor. The lower bound is proved for ideal prediction, by a "rectangular decomposition". Both bounds decrease with N (pp. 61–64).
- Experimental bounds at 100 known letters are 1.3 and 0.6 bits/letter. They are subject to sampling error and rest on human, not ideal, prediction (p. 64).

## L3 — Walkthrough

### 1. Introduction (pp. 50–51)
- A previous paper defined **entropy** (average information per letter; the average number of binary digits per letter in the most efficient binary translation) and **redundancy** (the constraint imposed by statistical structure, e.g. frequent E, H after T) (p. 50).
- That paper estimated that, with effects extending over not more than eight letters, entropy is roughly 2.3 bits/letter and redundancy about 50% (p. 50).
- The new method is more sensitive and takes account of long-range statistics. It is based on how well the next letter can be predicted when the preceding N letters are known (p. 50).
- Combining experiment and theory gives upper and lower bounds. From this analysis it appears that in ordinary literary English long-range effects (up to 100 letters) reduce entropy to something of the order of one bit per letter, redundancy roughly 75% (p. 50).
- The redundancy may be higher if structure over paragraphs and chapters is included. As lengths grow, the parameters become more erratic and depend more critically on the type of text (pp. 50–51).

### 2. Entropy from the statistics of English (pp. 51–54)
$F_N$ is the **N-gram entropy**. It measures information due to statistics over N adjacent letters. Here $b_i$ is a block of $N-1$ letters, $j$ a following letter, and $p_{b_i}(j)=p(b_i,j)/p(b_i)$ (p. 51).

$$F_N=-\sum_{i,j}p(b_i,j)\log_2 p_{b_i}(j)=-\sum_{i,j}p(b_i,j)\log_2 p(b_i,j)+\sum_i p(b_i)\log p(b_i)\tag{1}$$

$$H=\lim_{N\to\infty}F_N\tag{2}$$

- (1) is the average conditional uncertainty of the next letter given the preceding $N-1$ letters (p. 51).
- With spaces and punctuation ignored (26 letters), $F_0=\log_2 26=4.7$ by definition (p. 51). Then:

$$F_1=-\sum_{i=1}^{26}p(i)\log_2p(i)=4.14\tag{3}$$

$$F_2=-\sum_{i,j}p(i,j)\log_2p_i(j)=-\sum_{i,j}p(i,j)\log_2p(i,j)+\sum_ip(i)\log_2p(i)=7.70-4.14=3.56\tag{4}$$

$$F_3=-\sum_{i,j,k}p(i,j,k)\log_2p_{ij}(k)=-\sum p(i,j,k)\log_2p(i,j,k)+\sum p(i,j)\log_2p(i,j)\doteq 11.0-7.7=3.3\tag{5}$$

- The trigram table omitted trigrams bridging two words (WOW, OWO in TWO WORDS). A rough correction was used, with $p'$ the table's probability, $r(i)$ the probability of $i$ as a word's last letter and $s(k)$ of $k$ as a word's first letter (p. 52):

$$p(i,j,k)=\tfrac{2.5}{4.5}p'(i,j,k)+\tfrac1{4.5}r(i)p(j,k)+\tfrac1{4.5}p(i,j)s(k)$$

- Within-word trigrams (about 2.5 per word) are counted from the table. The bridging ones (one of each type per word) assume independence of the last letter of one word and the first digram of the next, or vice versa. $F_3$ is less reliable than the earlier numbers (p. 52).
- **Word statistics.** N-gram tables for $N>3$ were not available, so word frequencies were used. On log-log axes, probability against frequency rank is roughly a line of slope −1 (Fig. 1; "the" .071, "of" .034). So roughly (p. 52):

$$p_n=\frac{.1}{n}\tag{6}$$

- Zipf has pointed out that $p_n=k/n$ approximates word probabilities in many languages (p. 52).
- (6) cannot hold forever, because $\sum_1^\infty .1/n$ is infinite. Assume it holds up to the $n$ where total probability reaches 1, and $p_n=0$ beyond. That $n$ is rank 8,727 (p. 53). Then:

$$-\sum_{1}^{8727}p_n\log_2p_n=11.82\text{ bits per word}\tag{7}$$

- With 4.5 letters per word this is 11.82/4.5 = 2.62 bits/letter (p. 53).
- This should not be identified with $F_{4.5}$. The $F_N$ curve at $N=4.5$ will be above this value, because $F_4$ or $F_5$ involves letter groups regardless of word boundaries. Letters within words are more restricted than those bridging words. So 2.62 corresponds more nearly to, say, $F_5$ or $F_6$ (pp. 53–54).
- Summary table, bits per letter (p. 54):

| | $F_0$ | $F_1$ | $F_2$ | $F_3$ | $F_{word}$ |
|---|---|---|---|---|---|
| 26 letters | 4.70 | 4.14 | 3.56 | 3.3 | 2.62 |
| 27 letters (with space) | 4.76 | 4.03 | 3.32 | 3.1 | 2.14 |

- The earlier estimate of 2.3 for $F_8$ was found by several methods, one being extrapolation of the 26-letter series. Since the space is almost completely redundant over sequences of words, 27-letter $F_N$ is about .818 of the 26-letter $F_N$ for reasonably large $N$ (p. 54).

*Intuition note.* $F_N$ is the average uncertainty about the next letter when $N-1$ letters are known. The entropy $H$ is defined as its limit as $N$ grows. Tables of $N$-gram frequencies were not available beyond $N=3$, so the word-frequency estimate (2.62) is a further approximation. Shannon says it corresponds more nearly to, say, $F_5$ or $F_6$, and that $F_{4.5}$ would lie above it (pp. 51–54).

### 3. Prediction of English (pp. 54–58)
- **Experiment 1.** The subject guesses the first letter of an unfamiliar passage and is told if right; otherwise he is told the correct letter. He continues letter by letter, with the correct text so far in front of him (27-letter alphabet). In example (8) the reduced text has a dash for each correct guess and the true letter for each wrong one (p. 54).
- Of 129 letters, 89 (69%) were guessed correctly. Errors are most frequent at the beginnings of words and syllables, where the line of thought can branch (p. 55).
- **Recoverability.** The reduced text contains the same information as the original, in the sense that the original can, at least in principle, be recovered. This needs an identical twin of the subject, "mathematically, not just biologically" identical (p. 55). The twin guesses the same way. A dash means his guess is right, and wrong letters are supplied (p. 55).
- The twin can be dropped. In general, good prediction does not require more than $N$ preceding letters, with $N$ fairly small. There are finitely many $N$-grams, so the subject could guess the next letter for each one. This list serves both for reducing and for reconstructing the text (p. 55).
- The reduced text is then an encoded form of the original, from a reversible transducer. A communication system could transmit only the reduced text, with two identical predictors (Fig. 2) (p. 55).
- **Experiment 2.** The subject guesses until right, and the number of the successful guess is recorded (example (9)). Of 102 symbols he was right at the first guess 79 times, second 8, third 3, fourth and fifth 2 each; only eight needed more than five guesses (79+8+3+2+2+8 = 102). This is typical of a good subject with ordinary literary English. Newspaper writing, scientific work and poetry generally give somewhat poorer scores (p. 56).
- Recovery works as before: the twin guesses as many times as the number given. Without a human, the subject lists for each $N$-gram the most probable next letter, the second most probable, and so on (p. 56).
- The reduced text is a translation from the 27-letter alphabet into the alphabet $1,\dots,27$. Symbol 1 has a very high frequency, 2, 3, 4 successively smaller, and 20–27 are rare. Redundancy that lay in complicated constraints among letters is made explicit to a large extent in the unequal probabilities of the new symbols. This is what enables the entropy to be estimated (p. 56).

*Intuition note.* The guess numbers record where the subject's predictions failed and how many tries were needed. If the predictor is good, most numbers are 1, so their distribution is very uneven. That unevenness is how the redundancy is made explicit, to a large extent, and it is what lets the entropy be estimated from these experiments (p. 56).

- **Experiment 3 (dependence on N).** 100 samples of 15 letters were chosen at random from "Jefferson the Virginian" by Dumas Malone. The subject had 0, 1, …, 14 preceding letters, and used letter, digram and trigram tables, a table of initial-letter frequencies, a list of common word frequencies and a dictionary. A similar test gave 100 known letters (pp. 56–57).
- Table I: column $N$ = number of known letters + 1. Entry (row $S$) = number of times (per 100) the letter was right at guess $S$. The first two columns were calculated from letter and digram frequencies for best prediction, not obtained experimentally. E.g. with no letters known, space (.182) is guessed first, then E (.107). These two columns have less sampling error (pp. 57–58).
- First-guess row, columns 1–15 and 100: 18.2, 29.2, 36, 47, 51, 58, 48, 66, 66, 67, 62, 58, 66, 72, 60, 80 (p. 57). Prediction gradually improves, apart from statistical fluctuation, with more knowledge of the past (p. 58).
- **Reverse prediction.** Two 101-letter samples were used (p. 58):

| Guess no. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | >8 |
|---|---|---|---|---|---|---|---|---|---|
| Forward | 70 | 10 | 7 | 2 | 2 | 3 | 3 | 0 | 4 |
| Reverse | 66 | 7 | 4 | 4 | 6 | 2 | 1 | 2 | 9 |

- Reverse prediction is subjectively much more difficult, yet the scores were only slightly poorer. $F_N$ for a reversed language equals that for the forward one, since both terms in the second form of (1) have the same value (p. 58).

### 4. Ideal N-gram prediction (pp. 58–61)
- For a language there is a set of conditional probabilities $p_{i_1,\dots,i_{N-1}}(j)$. The best guess is the letter with highest conditional probability, the second guess the second highest, and so on. Reducing a text with this **ideal predictor** maps the letters to $1,\dots,27$, with the most probable next letter mapped to 1 (p. 58).
- The frequency of 1's in the reduced text, summed over all $(N-1)$-grams with $j$ the maximizing letter, is (p. 58):

$$q_1^N=\sum p(i_1,\dots,i_{N-1},j)\tag{10}$$

- $q_2^N$ is given by the same formula with $j$ the second most probable letter, and so on (p. 58).
- A predictor using $N$ letters gives frequencies $q_i^{N+1}$ (p. 59). Since it knows more of the past, one expects low numbers to be more probable, and one can prove:

$$\sum_{i=1}^{S}q_i^{N+1}\ge\sum_{i=1}^{S}q_i^{N},\qquad S=1,2,\dots\tag{11}$$

- **Proof.** Arrange $p(i_1,\dots,i_N,j)$ in a table with 27 columns ($j$) and $27^N$ rows (the $N$-grams). The left side of (11) is the sum of the $S$ largest entries in each row, summed over rows. The right side is also a sum of $S$ entries from each row, but not necessarily the $S$ largest. This holds because the right side would be computed from a table with $(N-1)$-grams as rows, and each such row is the sum of 27 rows of the $N$-gram table (p. 59):

$$p(i_2,\dots,i_N,j)=\sum_{i_1=1}^{27}p(i_1,i_2,\dots,i_N,j)\tag{12}$$

- The sum of the $S$ largest entries in a row of the $(N-1)$-table will equal the sum of the $27S$ selected entries from the corresponding 27 rows only if the latter fall into $S$ columns (p. 59).
- Equality in (11) for a particular $S$ requires this for every row of the $(N-1)$-table. Then the first letter of the $N$-gram does not affect the set of the $S$ most probable next letters, although it may affect the order within the set (p. 59).
- If equality holds for all $S$, the ordering is also unaffected. The reduced text from an ideal $(N-1)$-gram predictor is then identical with that from an ideal $N$-gram predictor (p. 59).
- Partial sums $Q_S^N=\sum_{i=1}^Sq_i^N$ (13) increase with $N$ and are below 1, so they approach limits. Hence the $q_i^N$ approach limits $q_i^\infty$. These may be interpreted as the relative frequencies of correct first, second, … guesses with knowledge of the entire infinite past (p. 59).
- **Transducer properties.** The ideal predictor is a transducer with two properties (p. 60):
  1. Its output symbol is a function of the present input letter and the preceding $N-1$ letters.
  2. It is instantaneously reversible: the input can be recovered without loss of time, using only the $N-1$ preceding symbols of the reduced text and the present output.
- For an $(N-1)$-gram predictor the same inequalities hold in the form $\sum_1^S q_i^N\ge\sum_1^S q_i^{N-1}$, $S=1,\dots,27$ (14). The proof of (11) carries over to any transducer with these two properties (p. 60). Take the array with $(N-1)$-grams as rows and the present letter as columns, and enter the output symbol at each cell. Reversibility requires that no two entries in a row be the same, otherwise the reversal would be ambiguous (p. 60).
- The probability of the $S$ most probable output symbols is the sum of $S$ entries per row, summed over rows. So it is at most the sum of the $S$ largest entries per row. With $r_i$ the output frequencies of such a transducer, this gives (p. 60):

$$\sum_{1}^{S}q_i^N\ge\sum_{1}^{S}r_i,\qquad S=1,2,\dots,27\tag{15}$$

- "Roughly speaking", ideal prediction collapses the probabilities onto a small group of symbols more than any other instantaneously reversible translation involving the same number of letters (p. 60).
- **Majorization.** Sets satisfying (15) were studied by Muirhead (Hardy, Littlewood, Pólya). If (15) holds with $q_i^N$ and $r_i$ in decreasing order, and $\sum q_i^N=\sum r_i$ (true here, both total 1), the first set $q$ **majorizes** the second set $r$. This is equivalent to either of the following (p. 61):
  1. $r$ can be obtained from $q$ by a finite series of "flows", each a transfer of probability from a larger to a smaller value, like heat from hotter to cooler bodies.
  2. $r$ is a generalized average of $q$: there are $a_{ij}\ge0$ with $\sum_ia_{ij}=\sum_ja_{ij}=1$ and
$$r_i=\sum_ja_{ij}\,q_j^N\tag{16}$$

*Intuition note.* Of all translations that need only the present letter and the $N-1$ preceding letters and can be undone at once, the ideal predictor piles probability onto the small numbers most strongly, in the sense of (15). Knowing one more letter can only keep this success frequency the same or raise it (11) (pp. 59–61).

### 5. Entropy bounds from prediction frequencies (pp. 61–64)
Given the ideal-predictor frequencies $q_i^N$ (p. 61):

$$\sum_{i=1}^{27}i\,(q_i^N-q_{i+1}^N)\log i\;\le\;F_N\;\le\;-\sum_{i=1}^{27}q_i^N\log q_i^N\tag{17}$$

- **Upper bound.** The maximum entropy for symbol frequencies $q_i^N$ is $-\sum q_i^N\log q_i^N$, so the reduced text's entropy per symbol is not greater. The $N$-gram entropy of the reduced text equals that of the original, by inspection of (1): the same terms appear, perhaps in a different order. The bound is valid whether or not the prediction is ideal (p. 61).
- **Lower bound.** One must show, for any $N$-gram probabilities (p. 61):

$$\sum_{i=1}^{27}i\,(q_i^N-q_{i+1}^N)\log i\;\le\;-\sum_{i_1,\dots,i_N}p(i_1\cdots i_N)\log p_{i_1\cdots i_{N-1}}(i_N)\tag{18}$$

- **Rectangular decomposition.** Arrange the $q_i$ as lines of decreasing height (Fig. 3). They are the sum of rectangular (flat) distributions. The $i$-th has total probability $i(q_i-q_{i+1})$ and entropy $\log i$. The total entropy is the left side of (18). So the claim is that any $N$-gram system with best-prediction frequencies $q_i$ has $F_N\ge$ the entropy of this rectangular system (pp. 61–62).
- Fig. 3's example: $q_1=.60$, $q_2=.20$, $q_3=q_4=.05$, $q_5=\dots=q_8=.025$. The rectangles have heights .40 ($q_1-q_2$, width 1), .15 ($q_2-q_3$, width 2), .025 ($q_4-q_5$, width 4) and .025 ($q_8$, width 8) (p. 62). (Added check: the total probabilities .40 + .30 + .10 + .20 sum to 1.)
- **Proof.** Each row of the table, arranged in decreasing order, is a monotonic decreasing distribution, and the $q_i$ are the sum of these. Replace each by its rectangular decomposition. The $q_i$ are then the sum of $27\times27^N$ rectangular distributions of 1–27 elements, all starting at the left column (p. 62).
- The entropy of this set is ≤ that of the original set, since termwise addition of distributions always increases entropy. This applies the theorem $H_y(x)\le H(x)$, with equality only if the added distributions are proportional (pp. 62–63).
- Components of the same width are proportional, so they can be added without changing entropy. Thus the rectangular decomposition of the $q_i$ is reached from the original $N$-gram probabilities by steps that decrease or leave entropy unchanged. So $F_N\ge$ the entropy of the rectangular decomposition (p. 63).
- The lower bound is definitely below $F_N$ unless each row has a rectangular distribution. That requires, for each $(N-1)$-gram, a set of next letters with equal probability, and all other next letters with probability zero (p. 63).

*Intuition note.* The lower bound is the entropy of the "flat blocks" into which the guess-frequency curve can be cut. The bound is definitely below $F_N$ unless every row of the table has a flat (rectangular) distribution. Both bounds need only the rank frequencies $q_i$, which is why the guessing experiment can supply them (pp. 61–63).

- **Monotonicity.** Both bounds in (17) decrease with $N$ (p. 63).
  - Upper bound: $q^{N+1}$ majorizes $q^N$, and any equalizing flow increases entropy (p. 63).
  - Lower bound: show $U=\sum_ii(q_i-q_{i+1})\log i$ (20) is increased by an equalizing flow. For a flow from $q_i$ to $q_{i+1}$ (first decreased by $\Delta q$, second increased by the same), three terms change (p. 63):

$$\Delta U=\bigl[-(i-1)\log(i-1)+2i\log i-(i+1)\log(i+1)\bigr]\Delta q\tag{21}$$

  - The bracket is $-f(x-1)+2f(x)-f(x+1)$ with $f(x)=x\log x$. Here $f$ is concave upward, since $f''(x)=1/x>0$. The bracket is twice the difference between the curve's ordinate at $x=i$ and the midpoint of the chord from $i-1$ to $i+1$, hence negative. As $\Delta q$ is negative, $\Delta U>0$ (pp. 63–64).
  - A simpler calculation covers flows from $q_1$ to $q_2$ and from $q_{26}$ to $q_{27}$ (only two terms change). Hence the lower bound from $N$-gram frequencies is ≥ that from $(N+1)$-gram frequencies (p. 64).
- *Skip path:* carry forward (17) and the fact that both bounds fall with $N$.

### 6. Experimental bounds for English (p. 64)
- Table I was smoothed to reduce sampling fluctuation. Low entries are least reliable and were averaged in groups. In column 4, 47, 18 and 14 were kept and the remaining 21 were spread uniformly over rows 4–20 (p. 64).
- Bounds from (17), bits/letter, for columns 1–15 and 100 (p. 64):

| Column | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Upper | 4.03 | 3.42 | 3.0 | 2.6 | 2.7 | 2.2 | 2.8 | 1.8 | 1.9 | 2.1 | 2.2 | 2.3 | 2.1 | 1.7 | 2.1 | 1.3 |
| Lower | 3.19 | 2.50 | 2.1 | 1.7 | 1.7 | 1.3 | 1.8 | 1.0 | 1.0 | 1.0 | 1.3 | 1.3 | 1.2 | .9 | 1.2 | .6 |

- Considerable sampling error remains, from identifying sample frequencies with prediction probabilities. The lower bound was proved only for the ideal predictor, while the data come from human prediction (p. 64).
- Rough calculations indicate that the gap between actual $F_N$ and the ideal-prediction lower bound (because conditional distributions are not rectangular) more than compensates for the humans' non-ideal prediction. So Shannon feels reasonably confident of both bounds, apart from sampling errors. The values are plotted in Fig. 4 (p. 64).

## Toy example (ours, not from the text)
Take a source with no memory ($N=1$) and three letters a, b, c with probabilities .5, .3, .2.
- Ideal predictor: guess a, then b, then c. So $q=(.5,.3,.2)$, and $q_4=0$. Text "c a b a" reduces to ranks "3 1 2 1".
- Upper bound: $-\sum q\log_2q=.5(1)+.3(1.737)+.2(2.322)=.5+.521+.464=1.485$ bits.
- Lower bound, $\sum i(q_i-q_{i+1})\log_2 i$:
  - $i=1$: $1(.5-.3)\log_21=0$.
  - $i=2$: $2(.3-.2)\log_22=.2$.
  - $i=3$: $3(.2-0)\log_23=.6\times1.585=.951$.
  - Sum: $1.151$ bits.
- So $1.15\le F\le1.49$. The true $F_1=1.485$ equals the upper bound here. The lower bound is strictly below it, because (.5,.3,.2) is not a flat distribution.
- Equality case: for probabilities (.5, .5), $q=(.5,.5)$, and the lower bound is $2(.5)\log_22=1$. This equals the entropy, since the row is flat.

## Concepts
- [[entropy-rate]] — here $H=\lim_{N\to\infty}F_N$, entropy per letter of English with ever longer context (p. 51)
- [[joint-and-conditional-entropy]] — $F_N$ is the average uncertainty of the next letter given the preceding $N-1$ letters (p. 51)
- [[redundancy]] — constraint imposed on text by statistical structure; estimated at about 50% (≤ 8 letters) and roughly 75% (long range) (p. 50)
- [[entropy]] — Shannon's $H$: average binary digits per letter in the most efficient binary translation (p. 50)
- [[n-gram-entropy-F_N]] (new) — $F_N$, entropy due to statistics over $N$ adjacent letters, a sequence of approximations to $H$ (p. 51)
- [[reduced-text]] (new) — a text rewritten as guess numbers (or dashes), recoverable in principle with an identical predictor (pp. 55–56)
- [[ideal-n-gram-predictor]] (new) — guesses next letters by decreasing conditional probability given $N-1$ letters (p. 58)
- [[majorization]] (new) — $q$ majorizes $r$ if (15) holds in sorted order and totals are equal; equivalent to flows or averaging (p. 61)
- [[rectangular-decomposition]] (new) — splitting a decreasing distribution into flat blocks, used for the lower bound (p. 61)
- [[zipf-law]] (new) — word probability roughly $.1/n$ for rank $n$ (p. 52)

## Canonical instances
- [[shannon-guessing-game]] (new) — human next-letter prediction, 69% first-guess success on 129 letters (p. 55)
- [[zipf-word-entropy]] (new) — 11.82 bits/word = 2.62 bits/letter from word ranks up to 8,727 (p. 53)
- [[identical-twin-decoder]] (new) — conceptual twin that recovers the text from the reduced text (p. 55)

## Bridges (candidates)
- [structural-analogy] next-letter prediction with $N-1$ letters of context ↔ language-model next-token prediction: uncertainty left after a context is measured the same way.
- [structural-analogy] reduced text of guess ranks, mostly 1's ↔ source coding: a good model turns data into a skewed symbol stream that can be compressed.
- [structural-analogy] equalizing "flows" raise entropy ↔ majorization / Schur-concavity of entropy in other fields: more even distributions have higher entropy.
- [metaphor] identical twin as decoder ↔ shared model at sender and receiver in compression schemes.

## Questions this raises
- How large is the gap between human guessers and the ideal predictor, and can it be measured rather than estimated roughly (p. 64)?
- How strongly does the entropy estimate depend on the type of text (literary, newspaper, scientific, poetry) (pp. 51, 56)?
- Can the lower-bound proof be extended to non-ideal predictors with bounded error?
- What happens to the estimates when structure over paragraphs and chapters is included (p. 50)?

## Reading notes
- Printed page = pdf page + 49 (pdf 1 = p. 50). The page header reads *Bell System Technical Journal, January 1951*; the manuscript was received Sept. 15, 1950. The acknowledgment thanks Mrs. Mary E. Shannon and Dr. B. M. Oliver (p. 64).
- The text layer is heavily garbled (OCR). Equations (10), (14) and (15) are missing or garbled in it; they are printed legibly on pp. 58 and 60 and were checked against the page images. (13) was checked on the image of p. 59.
- Equation numbers jump from (18) to (20); no (19) appears on these pages.
- In (18) the right-hand sum is printed without a leading minus sign. That would make it negative, so I wrote it with the minus, matching $F_N$ in (1). In (17) the minus before the upper-bound sum is visible in the image.
- Page 57 (the sentence runs onto p. 58) says the digram table gives the entries "in column 1". The digram-based figures (29.2, 14.8, …) are in the second column of Table I. This is probably a misprint for column 2.
- The text layer reads the earlier estimate on p. 54 as "$F_a$" and the word-based comparison as "$F_5$ or $F_a$". I read these as $F_8$ (consistent with "eight letters", p. 50) and $F_6$. The ratio ".818" on p. 54 is partly garbled, but the value is legible.
- The upper/lower bound table on p. 64 was read from the text layer only. Values of the 100-letter column (1.3, 0.6) and the monotone trend were cross-checked with Fig. 4 (p. 63) only roughly.
- The source contains no exercises.
