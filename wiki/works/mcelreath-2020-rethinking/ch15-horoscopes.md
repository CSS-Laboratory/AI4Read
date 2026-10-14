---
id: mcelreath-2020-rethinking/ch15-horoscopes
work: mcelreath-2020-rethinking
unit: Chapter 15. Horoscopes
pages: 441-444
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
# Chapter 15. Horoscopes

## L0 — One line
Statistical analysis is only one part of a scientific process that can produce mostly false findings at any one time, so every stage of research needs attention, and one thing you do personally control is openness.

## L1 — The gist (≤ 120 words)
McElreath asks how we know that much published science may be untrue, how science can still work despite that, and what an individual researcher can do about it. Generic statistical advice, like a horoscope, is vague and tends to oversell. Statistics matters, but only as much as every other part of research. Science works through variation and selective retention across many hypotheses. So most findings at a given time may be false while the long-run process still works. He lists eight parts of this process that matter, from theory quality to replication. His practical advice is to pre-plan the analysis, register the plan, document any changes, and share data and code online.

**Prerequisites:** none beyond the earlier chapters' idea of overfitting and significance testing; the chapter has no math.

## L2 — Key ideas (5–10 bullets)
- Statistics books tend to resemble horoscopes. They must stay vague because the targets of the advice are diverse, and they are too often over-optimistic because incentives reward promises. Better advice needs more detail, which typically only the scientist can supply (p. 441).
- Statistics is not more important than other parts of research. Science is not additive: a flaw in one part cannot be cancelled by strength in another (p. 441).
- Much of the literature may be untrue. Two lines of evidence are the difficulty of repeating findings and the history of error in the sciences (pp. 441–442).
- Science acts on populations of hypotheses by variation and selective retention. Most findings at a given time can be false while the long-run process still works (p. 442).
- Eight pieces of the discovery dynamic are listed: theory, funding, measurement, analysis, peer review, publication, post-publication review, and replication/meta-analysis. The list is the author's own and not special (pp. 442–443).
- Many of these pieces are beyond individual control, so social solutions are needed (p. 443).
- Openness is personally controllable. Pre-plan, register, analyze as planned, justify changes, and put data and scripts online (p. 443).
- The data and analysis are the scientific product; the paper is an advertisement (p. 443).

## L3 — Walkthrough
The chapter has no numbered sections. The order below is the author's.

**Two senses of "horoscope" (p. 441).**
1. Statistics courses and books (the author's own included) tend to resemble horoscopes. To remain plausibly correct they must stay vague, because the targets of the advice are diverse. A horoscope uses only basic facts of birth. A textbook guide uses only basic facts of measurement and design to dictate a model. With more detail one can do better, and typically only the scientist can supply it, not the statistician (p. 441).
2. Astrologers and statisticians both have incentives to exaggerate. Scientists want results and will favour procedures that promise them. The outcome is often "horoscopic": vague and optimistic, yet claiming critical importance (p. 441).

**Statistics is important, but not uniquely so (p. 441).** Scientific discovery is not additive, so sin in one part cannot be atoned for by virtue in another; everything interacts. Statistics can be neither uniquely credited for science's success nor uniquely blamed for its failures (p. 441).

*Intuition note (our gloss):* Because the parts interact and do not add up, strong statistics cannot be assumed to make up for weak measurement or selective publication; every part needs attention.

**Evidence that much literature is untrue (pp. 441–442).**
- **Horton's claim (Lancet editor-in-chief, 2015):** much of the literature, "perhaps half," may simply be untrue. He blames small samples, tiny effects, invalid exploratory analyses, conflicts of interest, and fashion-chasing (p. 441).
- **Method 1, repeatability.** Many published findings are hard to repeat, even in the best journals. Some failures come from methodological subtleties rather than falsity. But many famous findings cannot be repeated by anyone. The author says there is a sense in which this should be unsurprising given the nature of statistical testing, and points to an earlier box (p. 442).
- Costs: wasted drug development, even costlier policy built on false findings, and damage to science's reputation (p. 442).
- **Method 2, history.** More false elements were announced than there are elements in the periodic table. Fermi, a great physicist, reported ausonium (93) and hesperium (94). These numbers now belong to neptunium and plutonium, because he had mistaken a mix of lighter, already-known elements (p. 442).
- **Pessimistic induction:** philosophers' term for the observation that because most past science was wrong, most science is wrong (p. 442).

**Reconciling error with success (p. 442).** Science is a population-level process of variation and selective retention. It acts on populations of hypotheses, not single ones. The same dynamics that may eventually reveal nature's clockwork also generate error. So most findings at one time can be false while science works in the long run. The author compares this to natural selection: most individual variation in a generation is maladaptive, yet the population can adapt (p. 442).

*Intuition note (our gloss):* Many false findings at one moment are compatible with science still working in the long term, as in the author's natural-selection comparison, where most variation in one generation is maladaptive.

**Eight pieces of the dynamic (pp. 442–443).** The author says the list is in no particular order and that readers may make their own.
1. **Theory and predictions.** If most theories are wrong, most findings will be false positives. Popper held that falsifiability is all a theory needs to be scientific, but effective science requires more. A good theory gives precise predictions, and usually more than one model is needed (p. 442).
2. **Research funding.** Without long-term funding, necessary long-term research is not done. If current grant-holders judge new funding, research may become overly conservative and possibly corrupt (p. 442).
3. **Measurement quality.** Low signal-to-noise designs are a persistent problem. Poor signal does not mean no findings, but unreliable ones (p. 442).
4. **Data analysis.** Many common practices exacerbate false discovery. If the analysis is not designed before seeing the data, it may overfit in ways that regularization cannot reliably fix (p. 443).
5. **Peer review.** Good review is invaluable, but much is not good. Mistakes get through and brilliant papers are missed. Review selects for hyperbole, because admitting limitations hurts a paper's chances (p. 443).
6. **Publication.** We worry about bias in measurement and analysis, then allow it back in at publication. Incentives for positive, newsworthy results distort design and summary (p. 443).
7. **Post-publication review.** It is common for invalid analyses to appear in top journals and then be torn apart on blogs. No system links papers to later criticism, formal incentives are few, and retracted papers are still cited (p. 443).
8. **Replication and meta-analysis.** Repetition and synthesis are the most important aspects of science. No single study is definitive. Incentives to replicate and summarize are weaker than those for novelty (p. 443).

Attention goes to statistics, perhaps because it alone has formulas and theorems. Every piece deserves improvement, and many are outside individual control, so social solutions are needed (p. 443).

**What you control: openness (p. 443).**
- Pre-plan the research together with the analysis. This improves both design and statistics.
- Write a mock analysis you would not be ashamed to show a colleague, and register it publicly (for example on GitHub or a personal webpage).
- Collect data, then analyze as planned. Changes are acceptable if documented and justified.
- Put all data and scripts online, not "on request." Privacy can block full release, but the bulk of science is not of that sort (p. 443).
- "The data and its analysis are the scientific product. The paper is just an advertisement." (p. 443)

**Rethinking box (p. 443).** Speed's essay says "statistics is no closer to mathematics than cooking is to chemistry." Each field rests on another but is abstracted enough that practice depends mostly on other factors. In statistics, context is king, and mathematical foundations solve few, if any, of the contingent problems of a study (p. 443).

## Toy example
*(Our own, not from the text. It illustrates "if most theories are wrong, most findings will be false positives," p. 442.)*
Suppose 1000 hypotheses are tested, and only 5% are true. Assume each true effect is detected with probability 0.5 and each false one is wrongly "detected" with probability 0.05.
- True hypotheses: 1000 × 0.05 = 50. Detected: 50 × 0.5 = 25.
- False hypotheses: 1000 − 50 = 950. False positives: 950 × 0.05 = 47.5.
- Positive findings: 25 + 47.5 = 72.5. Share that are false: 47.5 / 72.5 ≈ 0.655.

About 65% of the "discoveries" are false, even though each test used the usual 5% error rate. Low theory quality drives this, not the test alone.

## Concepts
- [[pessimistic-induction]] (new) — because most past science was wrong, most science is wrong; philosophers' term (p. 442)
- [[science-as-variation-and-selective-retention]] (new) — science works on populations of hypotheses, so much error is compatible with long-run success (p. 442)
- [[preregistration-and-open-data]] (new) — pre-plan analysis, register it, document changes, share data and scripts online (p. 443)

## Canonical instances
- [[fermi-false-elements]] (new) — Fermi's "discoveries" of ausonium and hesperium were mixtures of lighter known elements (p. 442)
- [[horton-lancet-2015]] (new) — editor's claim that perhaps half of the literature may be untrue (p. 441)
- [[speed-cooking-chemistry]] (new) — Speed: statistics is no closer to mathematics than cooking is to chemistry (p. 443)

## Bridges (candidates)
- [structural-analogy] Science as variation and selective retention ↔ evolutionary biology: natural selection adapts populations though most variants are maladaptive — the author makes this comparison himself.
- [structural-analogy] Publication incentives for positive results ↔ selection bias in data: filtering on "significant" distorts what the literature shows.
- [metaphor] Horoscope vagueness ↔ generic statistical advice: advice built from only basic facts must be general.

## Questions this raises
- How much of the false-discovery problem comes from theory quality (item 1) versus analysis practices (item 4)?
- What social mechanisms could link published papers to later criticism, or reward replication?
- Does a pre-registered plan limit exploratory work, and how should changes from the plan be justified?
- If "context is king," what detail must the scientist provide for a model to be chosen well?

## Reading notes
- Printed page = pdf page − 14 (pdf 455–458 = printed 441–444).
- Printed page 444 (pdf 458) is blank.
- The text mentions footnote numbers 169–184. The notes themselves are not in these pages.
- References to "the Rethinking box on page 51" and "page 51" point to earlier material not in this unit; its content is not summarized here.
- This chapter does not discuss Bayesian versus frequentist inference or posterior predictive checks, so no concept lines are given for them.
- No equations, tables or code appear in this unit.
