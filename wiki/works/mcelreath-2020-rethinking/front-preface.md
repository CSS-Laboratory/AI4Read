---
id: mcelreath-2020-rethinking/front-preface
work: mcelreath-2020-rethinking
unit: Preface
pages: xi–xviii
fields: [bayesian]
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
# Preface

## L0 — One line
The book is a "scaffold": a sequential, code-heavy course whose slow, step-by-step calculations are meant to build understanding that you keep after you drop the scaffold.

## L1 — The gist (≤ 120 words)
The preface says who the book is for and how to use it. The audience is researchers who have taken a basic regression course and are uneasy about statistical modeling; they sense something is wrong with p-value-dominated practice. The method is learning by running code: more code than formal mathematics, read in order, with analyses saved as scripts. Optional boxes ("Rethinking", "Overthinking") add context and detail. The slow, manual calculations are deliberate. They help you make sound modeling choices later, when you use more automation. The preface also gives setup instructions (R, the `rethinking` package, `rstan`) and acknowledgments.

**Prerequisites:** a basic regression course; basic R (assignment, functions, loops, vectorization).

## L2 — Key ideas (5–10 bullets)
- The book is a scaffold. Its step-by-step calculations are usually automated, but doing them by hand gives the understanding needed for sound choices and interpretations (p. xi).
- It is for researchers who know basic regression and are ready to try inference without p-values. It does not really argue against p-values (pp. xi–xii).
- Avoiding significance testing is not uniquely Bayesian. The author attributes it to epistemological concerns (p. xii).
- It teaches with code more than formal mathematics, because code removes ambiguity and implementation details can matter (p. xii).
- It is a course, not a reference. Read it in order, and run the code (pp. xii–xiii).
- Optional "Rethinking" and "Overthinking" boxes give context and detail. One shows why statistical calculations nearly always use the logarithm of a probability (p. xiv).
- Command-line scripts are preferred over point-and-click. They document the analysis, make it repeatable and meet an ethical obligation (pp. xiv–xv).
- R's interrogative style (fit a model, then ask questions) differs from procedures that print masses of default output (p. xvi).

## L3 — Walkthrough

**Epigraph and purpose.** The poem is Heaney's "Scaffolding": masons test the scaffolding, and it comes down when the wall stands. The book is meant to raise your knowledge of and confidence in statistical modeling (p. xi). It teaches in "often inconvenient fashion", forcing step-by-step calculations that are usually automated. The reason is that you should understand enough detail to make reasonable choices and interpretations in your own work. You will later use more automation, but at first you should go slowly (p. xi).

*Intuition note:* You build a skill by doing the slow version first. Once you know why each step is there, you can let software do it with more confidence.

**Audience.** The main audience is natural- and social-science researchers, from new PhD students to seasoned professionals. They have had a basic regression course but remain uneasy about modeling. They feel something is vaguely wrong with typical early-21st-century practice, dominated by p-values and a "menagerie" of tests. They are not sure where to go to learn these alternatives (p. xi).
- The author's opinion is that the problem is less p-values than the odd rituals that grew around them, and the exclusion of other useful tools. So the book assumes you are ready to infer without p-values (pp. xi–xii).
- It would be better to also teach how to spot mistakes about p-values. The author sneaks in a little such material but has little space (p. xii).
- Disregard for p-values is "not a uniquely Bayesian attitude". Significance testing can be, and has been, formulated as a Bayesian procedure. The choice to avoid it is stimulated by epistemological concerns, some of which are briefly discussed in the first chapter (p. xii).

**Teaching strategy.**
- The book uses much more code than formal mathematics. Even excellent mathematicians can struggle with an approach until they see a working algorithm, because code removes ambiguity (p. xii).
- Much of statistics is computational. The same mathematical model can sometimes be implemented in different ways, and the differences matter (p. xii).
- Each section is "the tip of an iceberg". The author does not aim to be exhaustive but to explain something well. Topics such as centering predictors are woven into data-analysis narratives, not given their own units (p. xii).
- The author says this style has worked for many students. He suspects it fails dramatically for people forced to learn the material, and that it suits the internally motivated (p. xii).

**How to use this book.**
- It is a course, not a reference. It expects sequential reading, which has pedagogical advantages but violates how most scientists read books (p. xii).
- The code is integrated into the text and is "not optional". The author erred toward too much code. His experience is that novices learn faster by modifying working code than by writing algorithms from scratch (p. xii).

*What the book assumes (p. xiii).* It does not teach basic programming. You should have made a basic effort to install and use R. You should know that `y<-7` stores 7 in `y`, that symbols ending in parentheses are functions, what a loop is, that commands can be nested, and that R vectorizes much code. You need not be confident in R. The book explains important or unusual code tricks at length. The purpose is to let you tell whether an error is minor or major, as with rusty algebra in mathematical evolutionary theory (p. xiii).

*Using the code (p. xiii).* Code sits in shaded boxes, with output beneath in fixed-width type. Each snippet has a number that matches the code file on the book's website. Readers should run the code and compare output because, just as one cannot learn martial arts by watching Bruce Lee movies, you cannot learn to program statistical models by only reading a book. You can also run each line separately and print intermediate values. Example 0.2 is "a confusing way" to multiply 10 and 20:
`x <- 1:2; x <- x*10; x <- log(x); x <- sum(x); x <- exp(x)`, which gives `200` (p. xiii). If you do not understand a step, you can print `x` right after it; this is how you come to understand the examples and find the source of problems in your own code (p. xiv).

*Optional sections (p. xiv).* "Rethinking" boxes give context: connections to other approaches, history, common misunderstandings. "Overthinking" boxes give detail on code or mathematics and are useful on a second reading. Example 0.3: mathematically $p_1=\log(0.01^{200})$ and $p_2 = 200\times\log(0.01)$ are equal. In R, `log(0.01^200)` gives `-Inf` and `200*log(0.01)` gives `-921.034`. The second is right. The cause is rounding error: the computer rounds very small decimals to zero, losing precision and possibly causing substantial inference errors. Hence statistical calculations nearly always use the logarithm of a probability (p. xiv).

*Intuition note:* A tiny probability can become exactly zero inside the computer. Taking logs first keeps the number visible.

*The command line is the best tool (pp. xiv–xv).* Reasons given:
- It is more powerful.
- It saves time, because each script documents itself and can be replicated and shared years later. Point-and-click leaves no trail, so you pay later.
- It meets an ethical obligation. Science requires fully documented, repeatable analyses, and peer review and cumulative research depend on it.
- It is harder at first, but the author says the benefits are worth it.

*How you should work (pp. xv–xvi).* Work back and forth between a plain-text editor and R. Examples of editors: Notepad, TextEdit, Emacs, RStudio, Atom. Word files are not plain text. Keep a running log of commands there, and paste lines or read whole scripts into R. Typing directly into R is acceptable for exploring, debugging or playing, but serious work belongs in the script. Comments begin with `#`. Example 0.4 is a short script: load `cars`, fit `lm(dist ~ speed, data=cars)`, print `coef(m)`, and plot residuals against speed (p. xv). Stata/SAS users also need to adjust. Those tools issue procedures (e.g. `PROC GLM`) that produce a mass of default output. In R you fit a model and then issue commands to ask questions about it, a more "interrogative paradigm" in which you decide what to ask (p. xvi).

**Installing the rethinking package (p. xvi).** The package holds the data examples and many of the modeling tools. It relies on `rstan` for the more advanced models in the second half. Install `rstan` first from mc-stan.org, which also needs a C++ compiler. Then run `install.packages(c("coda","mvtnorm","devtools"))`, `library(devtools)`, and `devtools::install_github("rmcelreath/rethinking")` (example 0.5). The package is not on CRAN, at least not yet. Bug reports and source code are at github.com/rmcelreath/rethinking (p. xvi).

**Acknowledgments (pp. xvi–xvii).** The author thanks his graduate students, colleagues and many named commenters. None of the people he thanks agrees with all of his choices, and all mistakes and deficiencies remain his responsibility. The book is dedicated to Dr. Parry M. R. Clarke (1977–2012), who asked him to write it (p. xvii).

## Toy example
(Ours, not from the text.) The book's idea is to inspect each step. Multiply 3 and 4 the "confusing" way:
1. `x <- c(3,4)` gives (3, 4).
2. `x <- log(x)` gives (ln 3, ln 4) ≈ (1.0986, 1.3863).
3. `x <- sum(x)` gives 1.0986 + 1.3863 = 2.4849.
4. `x <- exp(x)` gives e^2.4849 ≈ 12.0, which is 3 × 4.

Printing `x` after each step shows the logs adding while the product is recovered at the end. For the log scale: 0.01³ = 0.000001, and 3 × ln(0.01) = 3 × (−4.605) ≈ −13.82, so the log is a modest number. By the same arithmetic, 200 × ln(0.01) ≈ −921.03, matching the book (p. xiv).

## Concepts
- [[scaffold-learning]] (new) — do slow, manual calculations to build understanding you keep after automating (p. xi)
- [[log-probability]] (new) — computing with the logarithm of a probability to avoid rounding very small values to zero (p. xiv)
- [[reproducible-scripting]] (new) — keep analyses as command scripts so they document themselves and can be replicated (pp. xiv–xv)
- [[frequentist-vs-bayesian]] — here only a note: avoiding significance testing is not uniquely Bayesian (p. xii)

## Canonical instances
- [[log-underflow-example]] (new) — `log(0.01^200)` gives `-Inf`, while `200*log(0.01)` gives `-921.034` (p. xiv)
- [[cars-regression-script]] (new) — a short commented script fitting `dist ~ speed` and plotting residuals (p. xv)

## Bridges (candidates)
- [same-math] log of a product = sum of logs, used to avoid rounding to zero ↔ bayesian: working with log-likelihoods and log-posteriors — the same identity.
- [structural-analogy] scaffold that is removed after learning ↔ cognitive science: worked examples gradually faded — both build understanding through temporary support.

## Questions this raises
- Which epistemological concerns about significance testing does Chapter 1 discuss?
- How exactly do different implementations of the same mathematical model "matter" (p. xii)?
- What does an analysis lose when it uses default output instead of asking questions of a fitted model?
- Where does the code-first, narrative style fail, beyond the author's guess about unmotivated learners?

## Reading notes
- Printed pages xi–xvii are visible in the text layer (pdf 7–13). Printed numbers are roman numerals: pdf 7 = xi. pdf 14 (xviii) is blank.
- In the text layer, the Overthinking expression $p_1=\log(0.01^{200})$ appears garbled as "0.01200". The superscript 200 is consistent with the code `0.01^200` and the result `-Inf`.
- The `cars` script comment says distances are in feet and speeds in km/h. I report it as printed.
- No exercises in this unit.
