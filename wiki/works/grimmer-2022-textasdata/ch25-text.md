---
id: grimmer-2022-textasdata/ch25-text
work: grimmer-2022-textasdata
unit: Chapter 25. Text as Outcome
pages: 429-435
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Text as Outcome

## L0 — One line
When text is the outcome of a causal study, learn a mapping $g$ from text to a low-dimensional outcome on training documents, then estimate the average treatment effect on held-out test documents.

## L1 — The gist (≤ 120 words)
How can we estimate a causal effect when the outcome is text? The authors use a train/test split. A function $g$ is learned on training documents; it turns each text into a low-dimensional outcome. The average treatment effect (ATE) is then estimated on the test documents only, with $g$ held fixed. Two studies show this. In a survey experiment (Egami et al.), a criminal-history vignette changes what respondents write about immigration. In a news study (Franco, Grimmer, and Lim), presidential appeals raise coverage of the appeal's topic. In both, the authors first discover $g$ on training documents and then estimate the effect on test documents.

**Prerequisites:** potential outcomes and the ATE; SUTVA, ignorability, positivity (Ch. 24); train/test splits; topic models (Structural Topic Model, Ch. 13).

## L2 — Key ideas (5–10 bullets)
- Text as outcome is "analytically straightforward": $g$ maps text $y$ to a lower-dimensional outcome $\pi$ (p. 429).
- $g$ is learned on the training set $I$ and then treated as a fixed transformation; the ATE is estimated on the test set $O$ (p. 429).
- The setup assumes SUTVA, ignorability and positivity (Assumptions 1–3 of Ch. 24); Egami et al. (2018) give an identification proof (p. 429).
- Egami et al. refine $g$ over sequential experiments (an old study plus two replications), each with its own train/test split (p. 431).
- In the final experiment, the criminal-history vignette shifts which topics respondents write about, e.g. more on deportation-for-money and punishment, less on "more information needed" (p. 431–432).
- Franco et al. use a 10%/90% training/test split of about 160,000 stories and compare topic coverage before and after speeches (p. 433).
- Appeals to Congress are followed by a 3.4-point rise in coverage. The rise after event announcements is larger but conflated with the event itself (p. 433–434).
- Egami et al. report similar results across their experiments even though $g$ is slightly different in each case, and the conclusion describes relative stability (p. 431, 435).

## L3 — Walkthrough

### Opening: the estimand (p. 429)
- Text is now written $y$, to stress that it is the outcome. $g$ maps $y$ to a lower-dimensional outcome of interest $\pi$ (p. 429).
- Following Chapter 24's train/test approach, $g$ is built on the training documents (subscript $I$). The ATE is estimated on the test set (subscript $O$) (p. 429).
- Assumptions: SUTVA, ignorability, positivity (Assumptions 1–3, Ch. 24). Notation follows Egami et al. (2018) (p. 429):

$$\widehat{ATE}=\frac{\sum_{i\in O} I(t_i=1)\,g_I(y_i(1))}{\sum_{j\in O} I(t_j=1)}-\frac{\sum_{i\in O} I(t_i=0)\,g_I(y_i(0))}{\sum_{j\in O} I(t_j=0)}$$

  (The printed formula is flattened onto running text, but its symbols are readable. It is the treated mean minus the control mean of $g_I(y)$ over $O$.) (added step: $t_i$ is the treatment indicator and $y_i(1), y_i(0)$ are the potential text outcomes; these are not defined on these pages.)
- By learning $g$ on $I$, the authors treat it as a fixed transformation of the data in $O$ and do estimation as they ordinarily would. Egami et al. (2018) provide an identification proof (p. 429).
- Overview (p. 429): the chapter reviews two examples. In each, the authors use the train/test split to discover $g$ and then estimate the causal effect in sequence. Egami et al. also use sequential experiments to iteratively refine $g$ before finally estimating the ATE.

**Intuition note.** The training half is used to decide *how to measure* the text. The test half is used to *test the effect* on that measure. Because $g$ is fixed before the test texts are used, the test texts did not shape the measure. (This reasoning is ours; the text states only the procedure.)

### 25.1 An experiment on immigration (p. 430–432)
- **Design (p. 430).** Respondents were randomly assigned one of two vignettes about a 28-year-old man convicted of illegally entering the US. Treatment: two prior prison sentences, one for a violent crime, and a previous deportation. Control: never imprisoned before. This builds on Cohen, Rust, and Steen (2004).
- **Outcome (p. 430).** Respondents answered "Should this offender be sent to prison?" (yes/no/don't know). They then wrote at least two sentences on what the US government should do and why. The authors must develop a $g$ to turn these answers into a usable quantity.
- **Sequence of studies (p. 431).** (1) Fit a Structural Topic Model to the Cohen et al. data. (2) Replicate with design changes on Mechanical Turk in July 2017. (3) Re-replicate in September 2017. In each, $g$ was developed on a training split and the ATE estimated on the test set only.
- **Final experiment (Table 25.1, p. 431–432).** $g$ gives 11 topics. Each topic has top words, a label by Egami et al., an effect and a confidence interval (CI). Selected results:

| Topic (label) | Effect | CI as printed |
|---|---|---|
| 3 Deport because of money | 0.032 | (0.015, 0.049) |
| 7 Punish to full extent of the law | 0.024 | (0.01, 0.037) |
| 8 Allow to stay, no prison, rehabilitate | −0.015 | (−0.028, −0.001) |
| 6 Crime, small jail time, then deportation | −0.024 | (−0.04, −0.003) |
| 5 More information needed, if violent imprison | −0.024 | (−0.042, −0.006) |

  Topics 4 and 1 have effects 0.012 and 0.01. Topics 11, 9, 10 and 2 have effects of −0.002 to −0.003 (p. 431–432).
- **Authors' reading (p. 431).** Topics range from advocating deportation (Topics 2 and 3) to requesting more information (Topic 5). The authors say the treatment clearly affects the topics written. A criminal history increases writing about deportation and decreases the probability that the respondent argues the person should be able to stay.
- Similar results appear in the original study and the first replication, though $g$ is slightly different in each (p. 431).

**Intuition note.** (Our gloss.) Each topic is one outcome, roughly the amount a response is about it. The effect for a topic compares the treated and control groups on that outcome. The text says $g$ was slightly different in each analysis yet the results were similar (p. 431).

### 25.2 The effect of presidential public appeals (p. 433–434)
- **Problem (p. 433).** The literature on presidents' influence over opinion and news coverage is mixed. The authors state that one reason is that prior studies use different research designs and shifting types of evidence.
- **Data (p. 433).** Only presidential public statements made during prime-time television. Coverage comes from the top ten newspapers and broadcast transcripts for the week before and the week after each speech. The result is nearly 160,000 stories mentioning the president.
- **Method (p. 433).** An STM is fit with 10% of stories as the training set and 90% as the test set. This leaves enough information to discover salient topics and enough content to infer a treatment effect. The salient topic of each appeal is identified, and the effect of the speech on that topic's share of later coverage is estimated.
- **Left plot, Fig. 25.1 (p. 433–434).** Two cases: appeals to Congress (black) and announcements of major world events (gray). The effect is inferred by comparing coverage share on the day just before and just after the speech.
  - After an appeal to Congress, coverage of the topic is 3.4 percentage points higher than just before the speech (p. 433).
  - After an announcement, coverage rises by seven percentage points. Part of this is due to the event, not the speech, so the estimate conflates the two (p. 434).
  - Announcement coverage lasts longer than appeal coverage (p. 434).
- **Right plot (p. 434).** Speech-by-speech estimates. Coverage rises more after announcements, but this may again reflect the news event. Presidents do not appear to get better at influencing coverage over time: later speeches are not more effective than earlier ones.

**Intuition note.** The design compares the same topic's coverage just before and just after a speech. That isolates the speech only if nothing else changes at that moment, which fails for announced events.

### 25.3 Conclusion (p. 435)
- Egami et al. show the value of combining sequential experiments with the train/test split. Over 15 years the relationship between perceived criminal history and opinion is relatively stable (p. 435).
- Franco et al. show text as outcome in an interrupted time series design, again discovering $g$ on a training split (p. 435).

## Toy example (ours)
Suppose $g_I$ was learned on training essays and returns 1 if an essay is mostly about deportation, else 0. The test set $O$ has 6 essays.
- Treated ($t=1$): $g_I$ = 1, 1, 0. Sum = 2, count = 3, mean = 2/3.
- Control ($t=0$): $g_I$ = 0, 1, 0. Sum = 1, count = 3, mean = 1/3.
- $\widehat{ATE} = 2/3 - 1/3 = 1/3$.

Training essays are never used in this calculation.

## Concepts
- [[text-as-outcome]] (new) — text is the dependent variable; $g$ maps it to a low-dimensional outcome $\pi$ (p. 429)
- [[train-test-discovery-of-g]] (new) — $g$ learned on training set $I$, effect estimated on test set $O$ (p. 429)
- [[average-treatment-effect]] (new) — difference in mean $g_I(y)$ between treated and control test documents (p. 429)
- [[structural-topic-model]] (new) — topic model (Ch. 13) used to build $g$ in both studies (p. 431, 433)
- [[sequential-experiments]] (new) — replications used to iteratively refine $g$ before the final ATE (p. 429, 431)
- [[interrupted-time-series]] (new) — compare outcomes just before and just after an event or speech (p. 435)
- [[text-as-data-validation]] — here, the authors report similar results across analyses with slightly different $g$'s and 'relative stability' (p. 431, 435); the text does not call this validation

## Canonical instances
- [[egami-immigration-vignette-experiment]] — criminal-history vignette changes topics in open-ended responses (p. 430–432)
- [[franco-grimmer-lim-presidential-appeals]] — presidential appeals raise topic coverage (p. 433–434)

## Bridges (candidates)
- [structural-analogy] Train/test split for $g$ ↔ ML sample splitting: choose the measure on one half, estimate on the other, so selection does not bias the estimate.
- [structural-analogy] Before/after speech comparison ↔ interrupted time series in policy evaluation: the jump at the event is the effect, if nothing else changes then.
- [metaphor] Announcement effect conflated with the event ↔ confounding by a simultaneous cause.

## Questions this raises
- Does the ATE depend on the choice of $g$, e.g. the number of topics? How should uncertainty about $g$ enter the CIs?
- Why use only 10% of the data for training in Franco et al.? How sensitive are results to the split ratio?
- How could the announcement-vs-appeal comparison be redesigned to separate the speech from the event?
- Several CIs in Table 25.1 include zero. How should one handle many topic-level tests?

## Reading notes
- Printed page = pdf page (429–435).
- The ATE formula appears flattened onto running text in the page image, but its symbols are readable. The transcription above was checked against the image.
- Figure 25.1 caption reads "Grimmer, and Lim (2018)". The caption appears to omit "Franco"; the main text cites Franco, Grimmer, and Lim (2018).
- The text calls Topic 2 ("Deport") deportation-advocating, but its effect in Table 25.1 is −0.003 with a CI containing zero. The text says treatment increases writing about deportation; the table's clearest increases are Topics 3 and 7.
- The text mentions "the bottom plot" and "black, top lines"; the image shows appeal effect on top and announce effect below, matching.
- Table 25.1 continues across pp. 431–432. Figure 25.1's right panel labels presidents (Obama, Bush 2, Clinton, Bush 1) on the vertical axis and has a readable horizontal axis, "Appeal Effect", from −0.2 to 0.3; individual speeches are not labelled.
