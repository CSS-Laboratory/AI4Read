# Notebook for "How much is a surprise worth?"

| File | What it is |
|---|---|
| `01_surprise_entropy.ipynb` | Eight practice exercises, ordered from easier to harder: surprisal and entropy, the village script, the submarine, whose model, your own text, estimation bias, the weighing (an optional extension, a fold-out in the post), and building the best script with the bound H <= EQ < H + 1. |
| `results.md` | Every number printed by the reference run, the cell that printed it, what was run, and the frame of each number (what a gap is measured against). |

## What you need

* `numpy` and `matplotlib`. Nothing else: no model, no download, no network.
* Jupyter (`jupyter lab` or `jupyter notebook`) to open the notebook.
* Python 3. The reference run used Python 3.12.12. Python 3.9 or later should work, but we did not test it.

```bash
python3 -m venv ~/venvs/ai4read-surprise
source ~/venvs/ai4read-surprise/bin/activate
pip install numpy matplotlib jupyter
jupyter lab
```

The reference run used Python 3.12.12, numpy 2.5.5 and matplotlib 3.11.2 (`results.md` lists the numbers it printed). Every random draw is seeded (`SEED = 20261207`, plus 6 and 8 in exercises 6 and 8), but numpy does not promise identical random streams across versions, so on other versions the simulated numbers (exercises 2 and 6) may differ in the last digits. The exact sums (exercises 1, 3, 4, 7 and 8) do not depend on the random generator, except the random share vectors in exercise 8(c). If you change the seed or the sample sizes, your numbers will differ.

## How to practise

1. Run the first cells (setup and the village).
2. For each exercise: read the task, **predict** the answer, open the hint if you need it, and write your own code in the empty cell.
3. Open the solution cell to compare. Solution cells are saved folded (source and output hidden). In JupyterLab, click the bar at the left of the folded cell, or use *View > Collapse All Code / Expand All Code*. In classic Jupyter, the cell is simply shown.
4. The solution cells also define the functions later exercises use (`surprisal`, `entropy`, `encode`, `decode`, `huffman_lengths`), so run them in order even if you wrote your own versions.
5. Change one line and watch a number move. Suggestions: the shares in `SHARES` and the script in `SCRIPT` (exercise 2); `MY_TEXT` (exercise 5); the sample sizes (exercise 6); the beliefs of Ana and Ben (exercise 4).

## What to look for

* Exercise 2: the village script averages about 1.75 questions a day, two-question labels cost 2, and the same script on a uniform village costs about 2.25.
* Exercise 3: 32 misses add to 1, 48 to 2, and a hit on any shot gives a total of 6.
* Exercise 6: the plug-in entropy of a small sample is biased low (about 0.25 bits for ten days).
* Exercise 7 (optional): the best first weighing is 4 against 4 (1.585 bits); 6 against 6 gives 1.000 bit and leaves 12 of the 24 hypotheses after either outcome.
* Exercise 8: joining the two rarest outcomes, again and again, builds the best script; the bound H <= EQ < H + 1 holds for every random share vector you try.

All of this is "ours": toy numbers and simulations, not results from the sources. The post says which source states which fact.
