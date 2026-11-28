---
name: series-information-theory
description: Weekly series 1, information theory, in seven posts. Proposals for the S0 planner; the concept spine is in canon/information-theory.md.
updated: 2026-11-28
status: proposed (awaiting Kunhao's check)
---

# Series 1: Information theory (7 weeks)

The arc of the seven posts:
- surprise, the unit of information;
- compression;
- what one variable tells about another;
- noise and its limit;
- the cost of a wrong model;
- the least-biased guess;
- the shortest description.

Each post stands alone. The core canon is digested and audited where it counts:
- Shannon 1948, 1951;
- MacKay 2003;
- Cover & Thomas 2006;
- Polyanskiy & Wu 2025;
- Jaynes 1957, 2003;
- Kelly 1956;
- Gibson et al. 2019;
- Rosvall & Bergstrom 2008;
- Tishby et al. 2000.

## Week 1. How much is a surprise worth?
- **Core idea:** bit, surprisal, entropy (spine: bit, self-information, entropy).
- **L1 motivation:** before Shannon, engineers measured messages by length or by the number of signal levels (Hartley, Nyquist). That measure ignores how likely each message is. Phenomenon: some news "carries more" than other news.
- **L2 café scene:** twenty questions, or finding one marked cup among 32 with yes/no questions. A good question halves the remaining options.
- **L3 smallest example:** a four-word weather report with unequal probabilities. Compute the surprisal of each word, the average, and the best question tree. Uniform vs skewed.
- **L4 cross-field links:**
  - same-math: thermodynamic entropy (with care);
  - structural analogy: surprisal and reading effort (Gibson 2019 is an empirical claim, not a theorem).
- **L4 failure boundaries:**
  - entropy ignores meaning (Weaver's semantic level);
  - it needs a known distribution;
  - one-off events have no frequency.
- **L5 CSS imagination:** one reader's information overload (a trouble) vs a society's attention economy (an issue); the extremes, where every message is certain or every message is equally likely.
- **Canon:** shannon-1948-mathematical (Part I), mackay-2003-information (ch. 1–2, 4), pierce-1980-introduction.

## Week 2. Why can a message be squeezed?
- **Core idea:** redundancy, source coding theorem, prefix codes, Huffman coding.
- **L1:** Morse code gave E a single dot by intuition; telegraph costs were paid per symbol. Why does English compress to roughly a quarter of its letters?
- **L2:** packing a suitcase with the things you use most within reach. Short codes go to frequent things.
- **L3:** Huffman code for the four-word report. Average length vs entropy; a prefix code read without separators; Kraft's inequality with three code words.
- **L4 cross-field links:**
  - same-math: word length vs predictability (Gibson 2019, efficient communication);
  - structural analogy: Zipf's law.
- **L4 failure boundaries:**
  - the source must be stable;
  - codes built for one population fail on another;
  - lossless limits do not cover lossy, meaning-preserving summaries.
- **L5:** jargon and abbreviations as community compression. Who is locked out (trouble ↔ issue)? Compare scientific writing across fields.
- **Canon:** shannon-1948-mathematical, cover-2006-elements (ch. 5), mackay-2003-information (ch. 5), gibson-2019-efficiency.

## Week 3. How much does one thing tell you about another?
- **Core idea:** joint and conditional entropy, chain rule, mutual information, data processing inequality.
- **L1:** correlation misses non-linear dependence. Survey designers ask which question tells you most about a person's vote.
- **L2:** a doctor choosing which single test to order: the one that leaves the least doubt.
- **L3:** a 2×2 table (umbrella × rain): H(X), H(X|Y), and I(X;Y) computed by hand. A table with zero correlation but positive mutual information.
- **L4 cross-field links:**
  - same-math: the Theil segregation index is a mutual information between group and place;
  - structural analogy: feature selection.
- **L4 failure boundaries:**
  - estimation bias with small samples;
  - mutual information says nothing about causal direction;
  - it is not about meaning.
- **L5:** segregation measured as information. One family's choice of school vs a city's sorting; a comparison across cities and decades.
- **Canon:** cover-2006-elements (ch. 2), mackay-2003-information (ch. 8–9), polyanskiy-2025-information; Theil index source to fetch.

## Week 4. How fast can you talk through noise?
- **Core idea:** noisy channel, channel capacity, noisy-channel coding theorem, error-correcting codes.
- **L1:** telephone and telegraph engineers fought noise with power and repetition, and paid for it in speed. Shannon showed that errors can vanish at a positive rate.
- **L2:** a noisy café. Repeating every word three times vs speaking in a code where each sentence checks the others.
- **L3:** the binary symmetric channel with flip probability 0.1:
  - repetition-3 error rate vs the Hamming (7,4) code's rate and error rate;
  - the capacity number.
- **L4 cross-field links:**
  - structural analogy: rational inattention (Sims 2003), people with limited capacity to absorb news;
  - metaphor: the Shannon–Weaver diagram in communication studies (and what it leaves out).
- **L4 failure boundaries:**
  - capacity is a limit over long blocks, so it does not apply to single messages;
  - adversarial noise and changing channels break the theorem's assumptions;
  - misinformation is not channel noise.
- **L5:** the rumour chain (a trouble) vs the information quality of a platform (an issue); invert the scale: one channel for a whole nation.
- **Canon:** shannon-1948-mathematical (Part II), mackay-2003-information (ch. 1, 9–10), cover-2006-elements (ch. 7); sims-2003-implications to check.

## Week 5. What does it cost to use the wrong model?
- **Core idea:** cross-entropy, KL divergence, perplexity, log scoring.
- **L1:** weather forecasters and pollsters need a score that rewards honest probabilities. Language models are trained by minimizing a number few people can read.
- **L2:** packing for a trip using last year's weather. The extra luggage you carry is the price of a wrong forecast.
- **L3:** the true vs believed weather distribution. Cross-entropy equals entropy plus KL, computed by hand. Perplexity as "effective number of choices". Asymmetry shown with two numbers.
- **L4 cross-field links:**
  - same-math: LLM training loss;
  - same-math: Kelly betting, where side information raises the growth rate by its mutual information (Kelly 1956);
  - same-math: the gap in variational inference.
- **L4 failure boundaries:**
  - KL is not a distance (it is asymmetric);
  - it is infinite when the model gives probability zero to an outcome that occurs;
  - low loss does not mean true understanding.
- **L5:** one forecaster's calibration vs public trust in polls; compare scoring rules across professions.
- **Canon:** cover-2006-elements (ch. 2, 6), kelly-1956-information, mackay-2003-information, shannon-1951-prediction.

## Week 6. What is the least-biased guess?
- **Core idea:** maximum entropy principle, exponential family / Gibbs form.
- **L1:** with only an average to go on (mean income, mean degree), analysts invent distributions. Physics derived the Boltzmann law from one constraint.
- **L2:** a fair referee who knows only one fact and refuses to assume anything else.
- **L3:** a die whose mean is 4.5 instead of 3.5. Find the maximum-entropy probabilities (solve for one multiplier numerically). Uniform as the no-constraint case.
- **L4 cross-field links:**
  - same-math: exponential random graph models (ERGMs) in network science;
  - structural analogy: logit choice models.
- **L4 failure boundaries:**
  - the answer depends on which constraints you choose;
  - in the continuous case it depends on coordinates;
  - hidden structure (real causal constraints) makes the max-entropy answer wrong.
- **L5:** what "neutral" assumptions in policy models hide. Compare networks of very different sizes.
- **Canon:** jaynes-1957-information, jaynes-2003-probability (ch. 11), cover-2006-elements (ch. 12).

## Week 7. What is the shortest description of a society's network?
- **Core idea:** Kolmogorov complexity (intuition only), Minimum Description Length, the map equation.
- **L1:** community detection methods disagree. Which division of a network is "real"? Overfitting in models of social data.
- **L2:** giving directions in a city by naming districts and reusing street names inside each district.
- **L3:** a 9-node toy network with two communities. Description length of a random walk with one codebook vs two-level codebooks, computed by hand.
- **L4 cross-field links:**
  - same-math: Bayesian marginal likelihood as code length (MDL);
  - structural analogy: Occam's razor.
- **L4 failure boundaries:**
  - the map equation finds flow communities, not every kind of group;
  - resolution limits;
  - the shortest code is not necessarily the true mechanism.
- **L5:** whether online communities "exist" or are an artefact of the method. Compare a platform's network across years.
- **Canon:** rosvall-2008-maps, mackay-2003-information (ch. 28), li-2019-kolmogorov (if available), grunwald MDL (check access).

## Open points for Kunhao
- Week 7 could be replaced by **information bottleneck** (Tishby 2000) if you prefer an LLM-facing ending.
- Sources to fetch at S1 (free, legal): the Theil index (week 3); Sims 2003 (week 4); a Grünwald MDL tutorial (week 7).
