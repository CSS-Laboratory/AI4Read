# Notebook 01 (surprise and entropy): results for citation

Produced by running the saved notebook `01_surprise_entropy.ipynb` from top to bottom with nbclient, on 28 November 2026. Every number below is printed by the cell named in its row (the execution count [n] shown in Jupyter). Re-running gives the same numbers on the same versions: every random draw uses the fixed seed 20261207 (offsets +6 and +8 in exercises 6 and 8).

## What was run

| Item | Value |
|---|---|
| Python / numpy / matplotlib | Python 3.12.12 / numpy 2.5.5 / matplotlib 3.11.2 |
| Platform | macOS (Darwin), CPU only; no GPU, no network |
| Seed | 20261207 |
| Libraries | standard library (`math`, `heapq`, `itertools`, `collections`), numpy, matplotlib |
| Not run | no language model, no real text corpus; the sample text in exercise 5 is a paragraph we wrote |

The stub cells ("your attempt") produce no output. The solution cells are saved with their source and outputs collapsed (`jupyter.source_hidden`, `outputs_hidden`).

## Outputs, cell by cell

### Setup and versions  [cell 1]

What was run: The first cell prints the Python, numpy and matplotlib versions and the seed.

```text
Python 3.12.12 | numpy 2.5.5 | matplotlib 3.11.2
seed 20261207
```

### The village table (setting)  [cell 2]

What was run: Prints each word, its share, the number of questions and the string.

```text
rain  share 0.500  questions 1  string 0
sun   share 0.250  questions 2  string 10
wind  share 0.125  questions 3  string 110
snow  share 0.125  questions 3  string 111
```

### Exercise 1. Surprisal and entropy (solution cell)  [cell 4]

What was run: `surprisal`, `entropy`; village, uniform, one-word and stall entropies.

```text
village surprisals : [1.0, 2.0, 3.0, 3.0]
village entropy    : 1.7500
uniform village    : 2.0000
one-word village   : 0.0000
market stall of 5  : 1.8750
```

Frame: No relative numbers. The entropies are exact sums.

### Exercise 2. 100,000 simulated days (solution cell)  [cell 6]

What was run: `numpy.random.default_rng(SEED)`; 100,000 days drawn from the village shares, encoded with the script, joined, decoded again; the same script on 100,000 uniform days (a second draw from the same generator).

```text
round trip ok      : True
village, script    : 1.7499 questions per day  (entropy 1.7500)
village, 2-question labels: 2.0000
uniform, same script: 2.2470 questions per day  (entropy 2.0000)
```

Frame: The average length is a sample mean. Its true value is 1.75 (village, equal to H) and 2.25 (uniform, the script's expected cost); the sample means differ from them by sampling error only. No relative number.

### Exercise 3. The submarine (solution cell)  [cell 8]

What was run: Miss worths `log2((65-k)/(64-k))` for shots 1 to 48; sums; the total for a hit on every shot t = 1 to 64; a plot.

```text
shot  worth(miss)  total
   1  0.0227       0.0227
   2  0.0231       0.0458
   3  0.0235       0.0693
  32  0.0444       1.0000
  33  0.0458       1.0458
  48  0.0875       2.0000
32 misses: 1.0000   48 misses: 2.0000   hit on shot 49 (16 squares): 4.0000   total 6.0000
hit on shot t, total for t = 1..64: min 6.000000  max 6.000000
a hit on shot 1 is worth 6.0 ; a hit on shot 64 is worth 0.0 (the last square is a certainty)
```

Frame: Exact sums, rounded to 4 decimals. MacKay (2003, p. 71) prints 0.0230 for shot 2 because he cuts digits off; we round, so 0.0231.

### Exercise 4. The weighing (solution cell)  [cell 10]

What was run: All 24 hypotheses (ball, heavy or light) enumerated; outcome chances and entropy for k against k, k = 1 to 6; information about the ball (outcome entropy minus the average conditional outcome entropy over balls) and about ball and direction (outcome entropy, since the outcome is then certain).

```text
k  chances (left down, right down, balance)   outcome entropy
1  0.083 0.083 0.833                         0.817
2  0.167 0.167 0.667                         1.252
3  0.250 0.250 0.500                         1.500
4  0.333 0.333 0.333                         1.585
5  0.417 0.417 0.167                         1.483
6  0.500 0.500 0.000                         1.000
all 24 hypotheses: log2(24) = 4.585 bits
4 against 4: about which ball 0.918 bits; about which ball and heavy-or-light 1.585 bits
6 against 6: about which ball 0.000 bits; about which ball and heavy-or-light 1.000 bits
```

Frame: Exact. Our computation: MacKay prints no solution to his Exercise 4.9.

### Exercise 5. A sample text (solution cell)  [cell 12]

What was run: A 480-symbol paragraph written for this notebook (not a published text); 27-symbol alphabet (a to z and the space) after lower-casing and collapsing spaces, which left 26 distinct symbols because the text has no j; plug-in entropy; a unigram word model estimated from the same text.

```text
480 symbols, 26 distinct; letter entropy 4.012 bits per symbol (log2 27 = 4.755)
most surprising symbols: [(8.91, 'z'), (8.91, 'x'), (8.91, 'g'), (7.91, 'q'), (7.91, 'k')]
least surprising symbols: [(2.37, '<space>'), (3.18, 'e'), (3.58, 'a')]
94 word tokens, 59 word types
word types with most total bits (count x surprisal): [('the', 8, 28.4), ('a', 5, 21.2), ('we', 4, 18.2)]
a model, not a mind: each word's share comes from this same text, so a word seen once costs 6.55 bits
```

Frame: Plug-in estimate from one short text, so it is biased low and noisy (see exercise 6). It is not comparable with MacKay's 4.11 (p. 32) or Shannon's 4.03 (1951, p. 54), which come from other texts.

### Exercise 6. Estimation bias (solution cell)  [cell 14]

What was run: `numpy.random.default_rng(SEED + 6)`; for n = 10, 30, 100, 1,000: 2,000 repeats, `multinomial` counts, plug-in entropy, mean, gap from the true 1.75, standard error of the mean.

```text
true entropy 1.7500; 2000 repeats per n
    n   mean plug-in H   gap from true   std. error of the mean
   10   1.5036           -0.2464          0.0071
   30   1.6753           -0.0747          0.0037
  100   1.7253           -0.0247          0.0019
 1000   1.7469           -0.0031          0.0006
```

Frame: Gaps are absolute, in bits, against the true entropy 1.75. They are not relative numbers.

### Exercise 7. Whose model? (solution cell)  [cell 16]

What was run: Surprisal of the same event under two beliefs; p = 0 handled as infinity.

```text
Ana 3.000  Ben 1.000  gap 2.000
a forecaster who said 0 and sees snow: inf
```

### Exercise 8. The bound (solution cell)  [cell 18]

What was run: Huffman lengths with `heapq`; the 0.7 village; the weather village; `numpy.random.default_rng(SEED + 8)`, 150 Dirichlet(1,...,1) share vectors for each of 4 to 10 outcomes (1,050 in all); the stall of the transfer challenge.

```text
0.7 village: H = 1.357, lengths [1, 2, 3, 3], EQ = 1.500, H + 1 = 2.357
weather village: H = 1.750, EQ = 1.750
1050 random share vectors on 4 to 10 outcomes: H <= EQ < H + 1 holds for all: True
gap EQ - H: smallest 0.0019, largest 0.6301
stall: lengths [1, 2, 3, 4, 4] EQ 1.875 H 1.875
stall after the change: old script (1,2,3,4,4) costs 2.5 ; best lengths [2, 2, 2, 3, 3] cost 2.25 ; H 2.25
```

Frame: Gaps EQ - H are absolute, in bits.

## Numbers the post quotes from this run

| Number in the post | Value | Cell |
|---|---|---|
| Village script average on 100,000 days | 1.7499 (entropy 1.7500) | 6 |
| Two-question labels | 2.0000 (exact, not simulated) | 6 |
| Village script on a uniform village, 100,000 days | 2.2470 (expected value 2.25) | 6 |
| First miss, second miss (rounded) | 0.0227, 0.0231 | 8 |
| 32 misses; 48 misses; hit on shot 49; total | 1.0000; 2.0000; 4.0000; 6.0000 | 8 |
| Weighing, k against k, k = 1 to 6 | 0.817, 1.252, 1.500, 1.585, 1.483, 1.000 | 10 |
| 6 against 6: about which ball; about ball and direction | 0.000 bits; 1.000 bit | 10 |
| Plug-in entropy of the sample text | 4.012 bits per symbol | 12 |
| Estimation: mean estimate for n = 10, 30, 100, 1,000 | 1.5036, 1.6753, 1.7253, 1.7469 | 14 |
| Estimation: gap from 1.75 | -0.2464, -0.0747, -0.0247, -0.0031 | 14 |
| Ana and Ben on the same snow | 3.000, 1.000, gap 2.000 | 16 |
| 0.7 village: H, EQ | 1.357, 1.500 | 18 |
| Bound H <= EQ < H + 1 on 1,050 random share vectors | holds for all; gap EQ - H from 0.0019 to 0.6301 | 18 |
| Market stall: EQ, H; after the change: old script, best script, H | 1.875, 1.875; 2.5, 2.25, 2.25 | 18 |
