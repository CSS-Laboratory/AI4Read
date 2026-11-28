# Notebook 01 (surprise and entropy): results for citation

Produced by running the saved notebook `01_surprise_entropy.ipynb` from top to bottom with nbclient, on 28 November 2026 (third run, after the round-2 revision: the exercises reordered again (whose model is now exercise 2, the best script exercise 7, the weighing last as an optional extension), the best-script exercise credited to Huffman and given a printed answer to its prediction, the share vectors of that exercise redrawn with seed offset +7). Every number below is printed by the cell named in its row (the execution count [n] shown in Jupyter). This is the output of one run on the versions below. Other Python or numpy versions may differ in the last digits, because numpy does not promise identical random streams across versions. Every random draw uses the fixed seed 20261207 (offsets +6 and +7 in exercises 6 and 7).

## What was run

| Item | Value |
|---|---|
| Python / numpy / matplotlib | Python 3.12.12 / numpy 2.5.5 / matplotlib 3.11.2 |
| Platform | macOS (Darwin), CPU only; no GPU, no network |
| Seed | 20261207 |
| Libraries | standard library (`math`, `heapq`, `itertools`, `collections`), numpy, matplotlib |
| Not run | no language model, no real text corpus; the sample text in exercise 5 is a paragraph we wrote; other Python versions (the notebook says 3.9 or later should work, untested) |

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

### Exercise 2. Whose model? (solution cell)  [cell 6]

What was run: Surprisal of the same event under two beliefs; p = 0 handled as infinity.

```text
Ana 3.000  Ben 1.000  gap 2.000
a forecaster who said 0 and sees snow: inf
```

### Exercise 3. 100,000 simulated days (solution cell)  [cell 8]

What was run: `numpy.random.default_rng(SEED)`; 100,000 days drawn from the village shares, encoded with the script, joined, decoded again; the same script on 100,000 uniform days (a second draw from the same generator).

```text
round trip ok      : True
village, script    : 1.7499 questions per day  (entropy 1.7500)
village, 2-question labels: 2.0000
uniform, same script: 2.2470 questions per day  (entropy 2.0000)
```

Frame: The average length is a sample mean. Its true value is 1.75 (village, equal to H) and 2.25 (uniform, the script's expected cost); the sample means differ from them by sampling error only. No relative number.

### Exercise 4. The submarine (solution cell)  [cell 10]

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

Frame: Exact sums, rounded to 4 decimals. MacKay (2003, p. 71) prints 0.0230 for shot 2, which matches cutting digits off (our reading); we round, so 0.0231.

### Exercise 5. A sample text (solution cell)  [cell 12]

What was run: A 480-symbol paragraph written for this notebook (not a published text); 27-symbol alphabet (a to z and the space) after lower-casing and collapsing spaces, which left 26 distinct symbols because the text has no j; plug-in entropy; a unigram word model (each word's share in the text) estimated from the same text.

```text
480 symbols, 26 distinct; letter entropy 4.012 bits per symbol (log2 27 = 4.755)
most surprising symbols: [(8.91, 'z'), (8.91, 'x'), (8.91, 'g'), (7.91, 'q'), (7.91, 'k')]
least surprising symbols: [(2.37, '<space>'), (3.18, 'e'), (3.58, 'a')]
94 word tokens, 59 word types
word types with most total bits (count x surprisal): [('the', 8, 28.4), ('a', 5, 21.2), ('we', 4, 18.2)]
a model, not a mind: each word's share comes from this same text, so a word seen once costs 6.55 bits
```

Frame: Plug-in estimate from one short text, so it is biased low and noisy (see exercise 6). It is a number for this text only.

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

### Exercise 7. The best script and the bound (solution cell)  [cell 16]

What was run: Huffman's rule (Cover & Thomas 1991, pp. 92-94, 101; MacKay 2003, p. 99) with `heapq` (a trace for three outcomes and for the 0.7 village); the weather village; `numpy.random.default_rng(SEED + 7)`, 150 Dirichlet(1,...,1) share vectors for each of 4 to 10 outcomes (1,050 in all); the stall of the transfer challenge; the gap EQ - H for the examples whose shares are powers of 1/2 and for the 0.7 village.

```text
three outcomes (1/2, 1/4, 1/4):
  join 0.25 and 0.25 into 0.50; outcomes [1, 2] get one more question
  join 0.50 and 0.50 into 1.00; outcomes [0, 1, 2] get one more question
  lengths [1, 2, 2], EQ = 1.500, H = 1.500
0.7 village:
  join 0.10 and 0.10 into 0.20; outcomes [1, 2] get one more question
  join 0.10 and 0.20 into 0.30; outcomes [1, 2, 3] get one more question
  join 0.30 and 0.70 into 1.00; outcomes [0, 1, 2, 3] get one more question
0.7 village: H = 1.357, lengths [1, 2, 3, 3], EQ = 1.500, H + 1 = 2.357
weather village: H = 1.750, EQ = 1.750
1050 random share vectors on 4 to 10 outcomes: H <= EQ < H + 1 holds for all: True
gap EQ - H: smallest 0.0033, largest 0.8361
stall: lengths [1, 2, 3, 4, 4] EQ 1.875 H 1.875
stall after the change: old script (1,2,3,4,4) costs 2.5 ; best lengths [2, 2, 2, 3, 3] cost 2.25 ; H 2.25
gap EQ - H: three outcomes 0.0000, weather village 0.0000, stall 0.0000 (all shares are powers of 1/2); 0.7 village 0.1432
EQ = H exactly when every share is a power of 1/2 (Cover & Thomas 1991, p. 86)
```

Frame: Gaps EQ - H are absolute, in bits.

### Exercise 8 (optional extension). The weighing (solution cell)  [cell 18]

What was run: All 24 hypotheses (ball, heavy or light) enumerated; outcome chances and entropy for k against k, k = 1 to 6; the number of hypotheses left after each outcome for 4 against 4 and 6 against 6.

```text
k  chances (left down, right down, balance)   outcome entropy
1  0.083 0.083 0.833                         0.817
2  0.167 0.167 0.667                         1.252
3  0.250 0.250 0.500                         1.500
4  0.333 0.333 0.333                         1.585
5  0.417 0.417 0.167                         1.483
6  0.500 0.500 0.000                         1.000
all 24 hypotheses: log2(24) = 4.585 bits
4 against 4: hypotheses left after left down / right down / balance: 8, 8, 8 of 24
6 against 6: hypotheses left after left down / right down / balance: 12, 12, 0 of 24
```

Frame: Exact counts and entropies. The 12 : 12 : 0 split for 6 against 6 is our count; MacKay (2003, p. 68) says only that those pans can never balance.

## Numbers the post quotes from this run

| Number in the post | Value | Cell |
|---|---|---|
| Village script average on 100,000 days | 1.7499 (entropy 1.7500) | 8 |
| Two-question labels | 2.0000 (exact, not simulated) | 8 |
| Village script on a uniform village, 100,000 days | 2.2470 (expected value 2.25) | 8 |
| First miss, second miss (rounded) | 0.0227, 0.0231 | 10 |
| 32 misses; 48 misses; hit on shot 49; total | 1.0000; 2.0000; 4.0000; 6.0000 | 10 |
| Ana and Ben on the same snow | 3.000, 1.000, gap 2.000 | 6 |
| Plug-in entropy of the sample text | 4.012 bits per symbol | 12 |
| Estimation: mean estimate for n = 10, 30, 100, 1,000 | 1.5036, 1.6753, 1.7253, 1.7469 | 14 |
| Estimation: gap from 1.75 | -0.2464, -0.0747, -0.0247, -0.0031 | 14 |
| Weighing, k against k, k = 1 to 6 | 0.817, 1.252, 1.500, 1.585, 1.483, 1.000 | 18 |
| Weighing: hypotheses left, 4 v 4 and 6 v 6 | 8, 8, 8; 12, 12, 0 | 18 |
| 0.7 village: H, EQ | 1.357, 1.500 | 16 |
| Bound H <= EQ < H + 1 on 1,050 random share vectors | holds for all; gap EQ - H from 0.0033 to 0.8361 | 16 |
| Market stall: EQ, H; after the change: old script, best script, H | 1.875, 1.875; 2.5, 2.25, 2.25 | 16 |
| EQ - H on shares that are powers of 1/2 (three outcomes, weather village, stall); on the 0.7 village | 0.0000, 0.0000, 0.0000; 0.1432 | 16 |
