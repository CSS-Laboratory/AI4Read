# Independent audit, wave 1 social-science digests: Achen & Bartels ch. 4, Axelrod ch. 2, Argyle et al. part 1, Anderson 1972

Auditor: Claude Opus 5.5. I am independent: I did not write or verify these digests. Date: 2026-10-14.
Pipeline audited: Sonnet 5.5 digest prompt v2.1 plus independent verifier v2.1. All four digests are `verified: repaired`.
Method: I read every source page, using the text layer for the full text and page images for the figures, Table 1 (Axelrod), the fluoridation/reelection/effort figures (Achen) and all four Anderson pages. I checked digest claims one by one against the source. I recomputed every number I could: tables, sums, percentages, toy examples.

**Severity rules used** (from the brief):
- **Critical**: a wrong number or statement; a strengthened, weakened or reversed claim; a claim not in the source; a misattributed view.
- **Major**: a wrong page reference; a missing key argument; a dropped hedge; 3 or more undefined terms.
- **Minor**: wording or format.

**One calibration I applied.** A dropped hedge counts as **major** when it sits in L0–L2, in an intuition note, or in a finding that a later post would carry forward. It counts as **minor** when it sits in a peripheral L3 paraphrase. Page offsets were checked against `pipeline/units.csv`: Achen printed = pdf − 19, Axelrod printed = pdf − 8, Argyle printed = pdf.

---

## Summary

| Digest | Checks | Correct | Minor | Major | Critical | Words (target ≈ 0.4 × source) |
|---|---|---|---|---|---|---|
| Achen & Bartels ch. 4 | 64 | 49 | 11 | 3 | 1 | 4,466 (≈ 106 %) |
| Axelrod ch. 2 | 72 | 63 | 8 | 1 | 0 | 4,621 (≈ 140 %) |
| Argyle et al. part 1 | 80 | 73 | 6 | 1 | 0 | 5,469 (≈ 91 % of the 6,000 cap) |
| Anderson 1972 | 46 | 36 | 7 | 3 | 0 | 2,747 (≈ 155 %) |

**Numbers are clean.** Every number I checked against the source was correct. That is roughly 150 numbers: table cells, percentages, coefficients and standard errors, Ns, scores, years and page offsets. Every figure value read from an image was correct. Every arithmetic step marked "added step" was correct. All five toy examples recompute correctly.

**Remaining errors are about strength and voice.** Of the 8 major and critical errors, 6 are hedges that were dropped, or comparatives that became exclusives ("more strongly related to X than to Y" became "follows X, not Y"). Two of them sit in **index lines** (Concepts and Canonical instances), which the verifier apparently checks less carefully. The others are one systematic citation problem (Anderson), one missing key argument (Axelrod) and one undefined-terms problem (Anderson).

**Verdict: OK to continue the batch.** No digest misstates a finding's numbers or reverses an argument. The one critical error is a strengthened claim in an index line of Achen. Two cheap fixes are recommended before or alongside the next wave (see "Improvements"): a hedge-diff check that also covers Concepts and Instances lines, and printed-page detection for papers.

---

## 1. Achen & Bartels 2016, *Democracy for Realists*, ch. 4 (pp. 90–115)

File: `wiki/works/achen-2016-realists/ch04-rational.md`

### A. Faithfulness: 64 checks (L0 1, L1 6, L2 8, L3 38, intuition notes 5, Concepts/Instances 6)

Checked and correct (sample):
- Setting and the Dahl framing (p. 90).
- Key 1958/1966, Fiorina's welfare quote, Kramer's "not 'irrational'", "rough justice", "voters are not fools" (pp. 91–92).
- The two difficulties and "kicking the dog" (pp. 92–93).
- Buchanan 1858/1857, Disraeli 1879, Stokes on valence vs position issues (pp. 93–94).
- Key's vote-switching evidence and n. 4 on prospective judgments (p. 94).
- Fiorina's dozen elections and panel data (p. 95).
- Kramer 1983 on snapshot surveys; n. 5 "the key point" (p. 95).
- Lenz "surprisingly little evidence" (p. 96).
- Aggregate data and the donor caveat in n. 6 (p. 96).
- Gosnell (pp. 96–97).
- Kramer 1971: 34 biennial elections, n. 7 on House races and on later presidential findings (p. 97).
- "Virtual consensus" (pp. 97–98).
- Downs quote, running tally, changing competence, Hibbs "divide and rule" in n. 10 (pp. 98–100).
- Ferejohn moral hazard, the .5 equilibrium, Mayhew's two-thirds in n. 12 (pp. 100–101).
- "Only insofar as voters can discern and set aside" (p. 102).
- Fearon in n. 13 (p. 102).
- **Fig. 4.1** read from the image: at σ/√T = 2.0 the curves are ≈ 0.69 / 0.60 / 0.54. Correct.
- **Fig. 4.2**: γ\* = 1.0 up to ψ ≈ 0.4, ≈ 0.5 at 0.8, ≈ 0.2 at 2.0. Correct.
- n. 14 and n. 15 (pp. 103–104).
- Downs's "errors, false information, and ignorance"; Key 1966 on perception (pp. 105–106).
- The broken-leg example (p. 106). EPA and SAB (pp. 106–107).
- **n. 16**: r = .54 gives r² = .2916, "just under 30 %". Correct.
- Lagged perceptions (p. 107).
- Untested assumption (p. 108). Key 1949 in n. 17 (p. 108).
- Canes-Wrone et al.: model, n. 18, n. 21, n. 22, pandering conditions (pp. 109–110).
- Federalist 71 and governors' terms (p. 110).
- **Fig. 4.3**: 36 / 59 / 70 %, N = 11 / 75 / 54. Correct.
- "Bygones are bygones" (p. 111). Key's derisive use and 1942 passage; n. 24 (p. 112).
- Comet and "hard times" (pp. 112–113). "Murky at best" (p. 113).
- Campello–Zucco, Bartels 2014 (p. 114). "Sadly unimpressive" (p. 114).
- "A proposal, not a settled finding" (p. 115).
- Reading notes: the n. 21/22 name-order observation is correct, and so is the "goes to zero" vs figure-endpoint remark.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A1 | Canonical instances, `crime-perception-gap` | "perceptions of crime follow media coverage, **not** official rates". The source says perceptions "**seem** to be **more strongly** related to local media coverage … **than** to official crime rates". The hedge is dropped and a comparative becomes an exclusive. The matching L3 line ("track local media coverage more than official rates") keeps the comparative but also drops "seem". | p. 107 | **critical** |
| A2 | L2 bullet 1 | "It **rescued** the 'voters are not fools' claim…" This states the proponents' view as fact. The source says the theory's appeal is that it "**seems** to save voters" and made the bleak survey portrait "if not quite irrelevant, at least not fatal". The chapter's thesis is that this rescue is "less unambiguously positive than existing literature tends to suggest". The bullet should be voice-tagged (proponents' view) and keep "seems". | pp. 91–93 | major |
| A3 | L3 Economy sub-bullet; instance `bush-1992-economic-pessimism` | "contributed to pessimism and Bush's defeat"; "hurt the incumbent". The source says discrepancies "can be politically consequential, **as they probably were** in 1992". The hedge is lost in both places. | pp. 107–108 | major |
| A4 | L3 "Voters **may** focus 'inordinately' on recent conditions (shown in ch. 6, promised)" | This weakens the claim. The authors write "in chapter 6 we **shall show** that American voters focus inordinately on recent economic conditions, forgetting or ignoring most of their relevant experience". The bullet also drops the framing that this misleads "**even when** aggregate economic perceptions do track real changes". | p. 108 | major |
| A5 | L1 last sentence | "'blind' retrospection **undermines** accountability". The source says it "poses a significant challenge to democratic accountability". | p. 114 | minor |
| A6 | L3 Introduction, Key 1966 | "mainly 'an appraiser of past events'". The source says "in its great, **and perhaps** principal, role". | p. 91 | minor |
| A7 | L2 bullet 3 | "A rational voter keeps a 'running tally'". The condition (competence constant or purely random) is dropped. L3 has the condition. | p. 99 | minor |
| A8 | L3 Selection | "it grounds durable party identification". The source says "more or less durable partisan preferences". | p. 99 | minor |
| A9 | L3 Kramer 1971 | "Election-year changes in real per capita income account for 'something like half the variance'". In Kramer the half-variance figure belongs to "economic fluctuations — most notably, election-year changes in real per capita income". The canonical instance has it right. | p. 97 | minor |
| A10 | L3 Fiorina | "*Mediated* … versus *simple* evaluations". Fiorina examined how far mediated evaluations "were grounded in" simple ones. The relation is lost. | p. 95 | minor |
| A11 | L3 Authors' caveat | "retrospection selects and disciplines leaders less well". The source says "**much** less well". The paragraph's thesis sentence is also omitted: "these difficulties are more serious than previous scholars … have generally thought". | pp. 92–93 | minor |
| A12 | L3 Wolfers | "He concluded that voters are 'quasi-rational'". The source says he concluded that the "**simplest explanation**" was that voters are quasi-rational. | p. 114 | minor |
| A13 | L1 gloss of *shirk* | "put in less effort for voters than they could". The authors call the shirking image "inapt" and use the term for any competing goal (n. 11). L3 has the broad meaning; L1 uses the image the authors reject. | p. 100 | minor |
| A14 | Concepts, `retrospective-voting-as-kicking-the-dog` | Labelled "Key's idea". "Kicking the dog" is the **authors'** metaphor (pp. 93, 114). Key's own term was "displacement of economic resentment" (p. 112). | pp. 93, 112–114 | minor |
| A15 | Instance `lenz-panel-analysis` | "performance effects, **not** policy effects". The source says "surprisingly little evidence" that policy preferences carried much weight. Lenz's own conclusion ("not ideology") partly supports the wording. | p. 96 | minor |

### B. Toy example
The arithmetic is **correct**. Little luck: reelection 1 vs 0. Much luck: 3/5 = 0.6 vs 1/5 = 0.2. It is **illuminating** for the selection model and Fig. 4.1, including the mirror image in n. 15.

Weakness: the effort sentence ("effort rarely changes the outcome") is asserted, not computed. The same toy computes it in one line. Take c = 0 and threshold W > 0:
- With luck ±0.5: adding 0.5 effort raises reelection from 1/3 to 2/3, a gain of 1/3.
- With luck ±2: it rises from 2/5 to 3/5, a gain of only 1/5.

That is the Fig. 4.2 mechanism in numbers.

### C. Coverage gaps
- p. 91: the authors grant that the theory "accounts for fluctuations in the electoral fortunes of incumbent leaders … much more successfully than any spatial theory of issue voting". This is the empirical credit they give before their critique. Not in L3.
- p. 107: misperceptions are "probably common in domains where voters have very limited personal experience, even (and perhaps especially) when … they care a lot".
- p. 108: "even when aggregate economic perceptions do track real changes, they may provide a misleading basis" (see A4).
- p. 115: "'voters are not fools'—but they are woefully ignorant about much of what is typically taken to be at the heart of democratic politics". This is the conclusion's punch line.
- n. 19 (p. 109): the pandering model "unrealistically" assumes voters can tell whether the one observed policy was right. Minor.

### D. Usefulness
This is the best digest of the four for this reader:
- The section structure follows the chapter.
- The voice tags (**Stimson's view / Authors' reply**, **Key's view**) are used well.
- The figures are described from the images, with an honest Reading note that the formal models are in the book appendix, so no equations appear.
- Length is on target.
- The Prerequisites line is appropriate. The principal–agent idea is explained in the text and in Concepts.
- Undefined at first use: *realignment*, *Keynesian*, *OECD*. All minor; fewer than 3 essential terms.

---

## 2. Axelrod 1984, *The Evolution of Cooperation*, ch. 2 (pp. 27–54)

File: `wiki/works/axelrod-1984-cooperation/ch02-success.md`

### A. Faithfulness: 72 checks (L0 1, L1 7, L2 8, L3 44, intuition notes 5, Concepts/Instances 7)

Checked and correct (sample):
- The three literatures, "E. coli of social psychology", "no more than a few dozen choices" (pp. 28–29).
- Non-zero-sum definition and the two facts (p. 30).
- Round-robin rules, twin, RANDOM, 200 moves, payoffs 3/1/5/0 (pp. 30–31).
- **120,000 moves / 240,000 choices** (p. 31). Recomputed: 15 programs give 105 pairs + 15 twins = 120 games, × 200 × 5 = 120,000. The digest's Reading note gets this right.
- 14 entries from 5 disciplines (p. 31).
- Rapoport (p. 31). Preliminary tournament; Joss and chess (p. 32).
- Benchmarks 600 / 200 / 0–1000 and the average of 504 (pp. 32–33).
- Relaxed "nice" definition (move 199); 8 nice at the top; 472–504 vs 401 (p. 33).
- Kingmakers, "two of the other seven" (p. 34).
- DOWNING's two conditional probabilities, .5 prior with no weight, first two defections (pp. 34–35).
- FRIEDMAN (p. 36). JOSS 10 % (p. 36).
- **Table 1** checked cell by cell (p. 37):
  - moves 1–5 both cooperate; 6–24 alternate (10 even moves "TFT only cooperated", 9 odd moves "JOSS only cooperated"); 25–200 mutual defection.
  - TFT = 15 + 9·5 + 1 + 175 = **236**. JOSS = 15 + 10·5 + 1 + 175 = **241**. The digest's added step is correct.
- Three levels of analysis (p. 38). TF2T, LOOK AHEAD, the DOWNING modification (10th → 1st) (pp. 39–40).
- 62 entries from 6 countries, the ten-year-old (p. 41).
- p = 0.00346, w = .99654 (p. 42). Non-correlates (p. 43).
- 3969 = 63² pairings (p. 43).
- Top 15 all nice but the 8th; bottom 15; r = .58 (pp. 43–44).
- TESTER 46th and TRANQUILIZER 27th, the 2.25 / ¼ rules (pp. 44–46).
- 39 of 62 nice; TF2T 24th (Maynard Smith) (p. 47). "Fewer than one-third" (p. 47).
- Hypothetical tournaments 5 of 6 (p. 48). The offspring-proportional rule (p. 49).
- Bottom 11 halve by generation 5; bottom third gone by generation 50 (p. 50).
- HARRINGTON grows until ≈ generation 200, extinct by 1000 (p. 52).
- The three clarity conditions; nice / retaliatory / forgiving / clear (pp. 53–54).
- Reading notes checked: offset, footnotes absent, "I shall called" misprint, the cautious Figure 2 note. All correct.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| X1 | L3 "Round one: scores and niceness" (coverage) | Missing key argument: "The nice rules did well in the tournament **largely because they did so well with each other, and because there were enough of them** to raise substantially each other's average score." This is Axelrod's own explanation of *why* niceness paid, and it sets up the later ecological argument (success depends on the population). The intuition note covers only the ranking *among* nice rules. | p. 35 | major |
| X2 | L2 bullet 4 | "JOSS's occasional defections set off **endless** mutual retaliation". Table 1 is one "illustrative game"; the retaliation lasts for the rest of that game. | p. 37 | minor |
| X3 | L3 TESTER | "Three REVISED DOWNING variants". The source has two REVISED DOWNING submissions plus one "slightly modified version" (Newman), described as "three variants of Leslie Downing's outcome maximization principle". | p. 45 | minor |
| X4 | L3 round two | "equivalent to $w = .99654$". *w* is not defined in L3. It is defined only via the canon link in Concepts. | p. 42 | minor |
| X5 | L3 lessons | "they were punished enough…". The source says "they **often eventually** got punished enough". | p. 47 | minor |
| X6 | L3 lessons | "The most successful entries were small variations…". The source says they "**tended to be** relatively small variations". | pp. 47–48 | minor |
| X7 | L3 robustness | The concession "While such exploitation is **occasionally fruitful**" is dropped before the three problems. | p. 54 | minor |
| X8 | Concepts, `round-robin-tournament` | The definition folds in the tournament's extra rules (twin, RANDOM). Axelrod defines round robin only as "each entry was paired with each other entry". | p. 30 | minor |
| X9 | L3 "nationality" | The source reports only that "nor did the Americans" do better. | p. 43 | minor |

### B. Toy example
The arithmetic is **correct**:
- TFT echo: 21 / 21 vs 24 / 24.
- TF2T with the same slip: A 26, B 21, joint 47 vs 42.

It is **illuminating** for the echo effect and the value of forgiveness (pp. 37–39).

Weakness: it shows a side mechanism, not the chapter's main result. The main result is that TFT is robust *across environments* because it is nice, retaliatory and forgiving. A toy round robin would show that directly. For example, take ALL-D, ALL-C, TFT and TESTER over 10 moves, where TFT never wins a single game but has the highest total. As written, the toy can leave the reader thinking TF2T is simply better. The text warns that TF2T came 24th in round two; the toy's disclaimer only partly covers this.

### C. Coverage gaps
- p. 35: see X1.
- p. 39: "even expert strategists do not give sufficient weight to the importance of forgiveness"; LOOK AHEAD was "better than any of the rules designed by game theorists". Minor.
- p. 46: the round-one report's explicit conclusion ("not only nice but also forgiving"), which is the bridge to the two lessons. Partly covered.
- p. 35: TIDEMAN AND CHIERUZZI was the *second-ranking* rule. Minor.

### D. Usefulness
Very faithful and well pitched at HS level:
- Short definitions (nice, forgiving, retaliatory, kingmaker, echo) and good intuition notes.
- The Prerequisites line correctly points to ch. 1's Proposition 1.

Weakness: length is ≈ 140 % of target. L3 (≈ 3,000 words) is close to a move-by-move paraphrase of a chapter that is already plain prose. The TESTER/TRANQUILIZER and simulation sections could be cut by a third with no loss.

---

## 3. Argyle et al. 2023 (arXiv v1, 2022), "Out of One, Many", part 1 (pp. 1–29)

File: `wiki/works/argyle-2023-silicon/main-p1.md`

### A. Faithfulness: 80 checks (L0 1, L1 6, L2 8, L3 40, intuition notes 6, Concepts/Instances 6, Reading notes 13)

Checked and correct (sample):
- Abstract's "fine-grained and demographically correlated" (p. 1). "Not just one bias, but many" (p. 2).
- Five contributions (p. 3). 175 B parameters / 45 TB; the "Can you come / eat" example (pp. 3–4).
- Definition, core assumption and limits of algorithmic fidelity; four criteria verbatim in substance; "no thresholds" (pp. 4–5).
- Silicon-sampling equations, Simpson's paradox analogy and caveat (p. 5).
- Study 1:
  - 2,873 evaluators, 7,675 lists, 8 lists each, 3 ratings per list (p. 6).
  - 61.7 vs 61.2 %, p = 0.44, "nearly 40 %" (p. 8).
  - 72.3 / 66.5 and 39.8 / 41.0 % (p. 8).
  - 60.1 vs 52.8 %, p < .001 (p. 9).
- Study 2:
  - 10 conditioning variables, with 9 and 10 missing in 2020 (p. 10).
  - Toplines 0.391/0.404, 0.432/0.477, 0.472/0.412, and the "against Biden in 2020" reading (p. 10).
  - **All 30 Table 1 cells reproduced in the digest are correct** (p. 11).
  - "More than half ≥ 0.90" verified: 12 of 23 rows in 2012.
- Study 3: 11 + 1 items, Cramér's V, −0.026, "stunning", individual-level limits (pp. 12–13).
- $29 (p. 15). Misuse warning and domain restriction (pp. 15–16).
- Appendix A: Davinci, temperature 0.7, log-sum-exp token sets (p. 16).
- B.1:
  - N = 2,107.
  - Age and income mappings.
  - 128 tokens.
  - 3,592 human texts: 3,592 / 2,107 = 1.70.
  - 4,083 GPT-3 texts: 4,083 / 2,107 = 1.94.
  - Mean lengths 4.54 / 7.78 (pp. 17–19).
- B.2: 120 / 7,675 = 1.56 % ("1.5 %") (p. 19).
- **Table 2, Table 3, and all 28 coefficient/SE pairs and 14 Ns in Tables 4–7** match the text layer (pp. 24–29).
- The Reading notes are excellent and all verified:
  - Moderates 2012 = 0.65, so "exceed 0.65" is loose.
  - 9,469 + 9,446 = 18,915 ≠ 18,903.
  - "Panel B of Figure 4" should be Figure 3.
  - "Appendix 3 / 5" cross-references.
  - "these these".
  - 7.3 % is really 7.3 percentage points.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| R1 | L3 §9 Discussion | "GPT-3 **replicates** viewpoints of demographically varied sub-populations". The source says "in all studies, we **find evidence that** GPT-3 **is capable of** replicating the viewpoints…". The bullet is not inside the "authors summarise" tag, so it reads as the digest's own claim. Readers will copy this headline claim. | p. 15 | major |
| R2 | L3 B.2 | "No text was seen in both parts". The source says "No **respondents** evaluated the same texts in both parts". Each text was meant to be rated about 3 times in *each* portion. The digest wording implies the opposite design. | p. 19 | minor |
| R3 | L3 §9 | "Study 1 supports Criteria 1, 2 and 4". The authors write that Study 1 "**shows** that GPT-3 **passes**" the Turing test and "exhibits both **strong**" backward continuity and pattern correspondence. Softening the authors' wording here also hides a point a critical reader needs: on p. 10 the same Study 1 gave only "**some initial evidence**" for Criterion 4. The digest should report both strengths and note the escalation. | pp. 10, 15 | minor |
| R4 | §3 intuition note | "The last is the one most directly about structure across many respondents". This is the digest's own interpretation and is not flagged (prompt rule 1). | p. 4–5 | minor |
| R5 | L1 | "GPT-3 output matches human data closely". This is the authors' evaluative claim, given in narrator voice. L0 correctly says "The authors argue". | pp. 8–13 | minor |
| R6 | Concepts, `zero-shot-few-shot-prompting` | "without examples". This gloss is not in the source, which says only "leveraging the zero-shot learning property". It is harmless, but it is outside knowledge. | p. 12 | minor |

The §6 intuition note's own inference about party ID and ideology is **flagged** as the digest's own reading, and the flag is repeated in the Reading notes. That is good critical practice, so I do not count it as an error.

### B. Toy example
The arithmetic is **correct**:
- Silicon sampling: 0.7·0.2 + 0.3·0.7 = 0.35, and 0.4·0.2 + 0.6·0.7 = 0.50.
- Dichotomizing: agreement 3/4; means 0.375 vs 0.50.

The first part is **very illuminating**. It is exactly the §4 mechanism, and it states the load-bearing assumption (that P(V|B) is right). The second part is fine, but it calls a 0.125 gap a "mild bias", while the paper's "mild" gaps are 0.013–0.06 (p. 10). Use numbers whose gap is closer to 0.03.

### C. Coverage gaps
- p. 15: the Discussion's framing sentence: fidelity justifies LLMs "as proxies for human cognition **at an aggregate level**". The aggregate-level restriction appears only in Study 3 limits.
- pp. 10 vs 15: the escalation of the Criterion 4 claim (see R3).
- p. 15: the §8 suggestion that GPT-3 findings be followed by "an experiment or observational study to confirm and dissect this relationship in a rigorous and causal way". This is the authors' own limit on what silicon results establish.
- Abstract (p. 1): "goes far beyond surface similarity … nuanced, multifaceted". These are the authors' strongest words. They are worth keeping, voice-tagged, so the reader can weigh them.
- Not noted anywhere: Table 5 shows significant GPT-3 source coefficients for Independent (0.089, SE 0.027) and Liberal (−0.099, SE 0.020) writers describing Democrats. This sits uneasily with the "striking" similarity claim on p. 8. The digest transcribes the numbers neutrally, which is correct, but it adds no comment. That is acceptable, but a Question pointing at it would help a critical reader.

### D. Usefulness
Highly faithful, and the Reading notes are the best critical apparatus in the wave. However:
- ≈ 30 % of the digest (B.1–B.3, especially the 28-cell Tables 4–7) is transcription. The text never discusses these numbers, and an HS-start reader gains nothing from them. A one-line summary plus "full table on pp. 26–29" would do.
- Level is set to `grad` while the reader starts at HS. The Prerequisites line is honest (OLS, fixed effects, clustered SEs, tetrachoric) but heavy. Inline glosses for tetrachoric, Cramér's V and proportion agreement are good.
- Undefined: *log-sum-exp*, *RMSE*, *Lucid / Qualtrics* (platforms), *ablation* (only glossed in passing). All minor.

---

## 4. Anderson 1972, "More Is Different" (Science 177: 393–396)

File: `wiki/works/anderson-1972-moreisdifferent/main.md`

### A. Faithfulness: 46 checks (L0 1, L1 7, L2 8, L3 22, intuition notes 2, Concepts/Instances 6)

Checked and correct (sample):
- The reductionist hypothesis "accepted without question" (p. 393).
- Weisskopf's intensive/extensive split; the materials-science leader's "few or no such problems" and device engineering (p. 393).
- "Does not by any means imply a 'constructionist' one" (p. 393).
- The X/Y table (p. 393). "Psychology is not applied biology, nor is biology applied chemistry" (p. 393).
- Both clarifications, including "whether a deep or a specious one" (p. 394).
- Ammonia: 3 × 10¹⁰ s⁻¹, the stationary-state theorem and its reason, parity (p. 394).
- PH₃ at one-tenth; PF₃ (p. 394).
- Sugar (~40 atoms). Pyroelectric and ferroelectric crystals; "age of the universe" (p. 394).
- The three inferences; Newton; "only slightly overstating" (pp. 394–395).
- The N → ∞ nucleus and "two impossible things" (p. 395).
- Mid-19th-century crystals; 30 years for superconductivity (p. 395).
- "In a sense violated"; breaking, not violating; rigidity (p. 395).
- Information-bearing crystallinity; ordering in time and its roles (pp. 395–396).
- Functional structure; "pile speculation on speculation" (p. 396).
- Josephson. Pippard's "cultivate our own valley" (ref. 7) (p. 396).
- Positron discoverer; molecular biologists (p. 396).
- Marx and Fitzgerald–Hemingway (p. 396).
- Reading notes verified: the OCR slips "Referces", "ifim", "ali" and "Cl-mento" are all present in the text layer; the unrelated *Natural Areas* article; printed = pdf + 392.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| N1 | All citations; frontmatter | The digest cites `(pdf N)` although printed page numbers **393–396 are clearly visible** on every page image. The Reading note even computes the offset. The prompt (rule 5) says to use the printed numbers in that case. Root cause: `units.csv` has an empty `printed_pages` for this paper, so the page labels carried no printed number. | all pages | major (systematic) |
| N2 | L1 last sentence; L2 bullet 8 | "The relation of whole to parts is 'a one-way street': analysis is possible, synthesis rarely." Anderson heavily hedges this: "There **may well be no useful parallel** … **except perhaps** to say that, **in general**, the relationship … is intellectually a one-way street". Analysis "**may be** not only possible but fruitful". L1 states a general law. L2 drops the "no useful parallel" frame. L3 has it right. | p. 396 | major |
| N3 | Whole digest | 3 or more technical terms are used without definition for an HS-start reader: *optical rotating power*, *homogeneous and isotropic*, *superconductivity*, *superfluidity*, *phase transition*, *quantum electrodynamics*, *ethology*. *Superposition* appears only in Prerequisites. | pp. 394–396 | major |
| N4 | L0; L3 opening | "need research as fundamental as any other". Anderson writes "research which **I think** is as fundamental…". His opinion is stated as fact. | p. 393 | minor |
| N5 | L3 "Beyond simple phase transitions" and "Speculative ladder" | Three hedges in the speculative section are dropped: "**It seems to me** that the next stage…"; ordering in time "**seems to be** identifiable"; "**In some sense**, structure … must also be considered a stage". The Reading note keeps the "speculative" status in general terms, so this is minor. | pp. 395–396 | minor |
| N6 | L2 bullet 6; L3 | Crystal rigidity is listed alongside sound and superconductivity as the symmetry's expression. Anderson introduces it "**in a very deep analogy**". | p. 395 | minor |
| N7 | Concepts, `information-bearing-crystallinity` | "spatial regularity whose elements vary from cell to cell, **so it can be read out**". This inverts the logic. In the source the system is *regular* so that it can be read out, *but* contains elements that vary from cell to cell. | p. 395 | minor |
| N8 | L3 order | The third inference ("a really big system … usually has less symmetry") is placed before the "basic reason" (N → ∞) paragraph. In the source it comes after. | p. 395 | minor |
| N9 | Instance `sugar-chirality` | "**only** living matter makes populations asymmetric". The source says "We needed living matter to produce an actual unsymmetry in the populations" for *free molecules*. The very next paragraph describes large inanimate aggregates (crystals) with a net dipole. | p. 394 | minor |
| N10 | Concepts | `[[emergence]]` and `[[criticality-phase-transition]]` are canon ids for words Anderson does not use. They are not flagged "(canon link; not stated in this unit)". | — | minor |

### B. Toy example
The arithmetic is **correct**. I re-derived it:
- eigenvalues ∓t;
- ψ(τ) = cos φ |L⟩ + i sin φ |R⟩;
- ⟨dipole⟩ = −d cos 2φ.

It is **only partly useful** for this reader:
1. It needs Dirac notation, Hamiltonians and complex phases. Those are far beyond "basic quantum ideas" and an HS start, and they are not in Prerequisites.
2. It illustrates the ammonia sub-point (stationary states are symmetric). It does not illustrate the main idea, that large N makes the asymmetric state effectively permanent. The final sentence asserts this without computing it.

A better toy: N independent two-state units that must all flip together, each with probability p per tick. The joint flip probability pᴺ falls from 0.5 (N = 1) to 0.001 (N = 10) to ~10⁻³⁰ (N = 100). That is hand-computable, and it shows "more is different".

### C. Coverage gaps
- p. 394: "(As I said, we must all start with reductionism, **which I fully accept**.)". This is the single sentence that blocks the common misreading of Anderson as anti-reductionist. L1 implies it ("opposes the apparent corollary"), but L3 never states it.
- p. 395: on nuclear shape, "In my opinion, whether or not one calls this intensive research, it is as fundamental in nature as many things one might so label". This is the direct application of the paper's thesis to Weisskopf's split.
- p. 395: the framing question of the second half: whether "an even more complete destruction of the fundamental symmetries of space and time is possible" and gives intrinsically new phenomena.
- p. 395: the crystal "suddenly and unpredictably displays an entirely new and very beautiful symmetry"; the list of antiferromagnets, liquid crystals and so on; London; the Jupiter citizen. Minor.

### D. Usefulness
L0–L2 are good stand-alone summaries, and the voice is mostly clear (Weisskopf's view vs Anderson's reply). However:
- The digest is ≈ 155 % of target. L3 (≈ 1,570 words) for a ≈ 3,800-word essay is close to a paraphrase.
- Only 2 intuition notes, and none after the major "breaking vs violating" result.
- The physics vocabulary (N3) and the bra-ket toy make this the least accessible digest for an HS-start B2 reader. The Prerequisites line understates what the toy needs.

---

## Cross-digest patterns

1. **Hedges and comparatives are lost mostly in index lines and peripheral L3 bullets.** The L0–L2 checks clearly worked: the strong-word regex (`STRONG` in `build.py`) catches "only / always / never". It does not catch the *loss* of "seems / probably / perhaps / I think / simplest explanation / in some sense / more … than". Two of the most visible errors (A1, A3) are in Canonical instances, which later posts are likely to reuse as one-line facts.
2. **Voice tags are good where the text argues against a named person** (Stimson, Key, Weisskopf). They slip where the text reports a *theory's* appeal (A2) or where the digest restates the authors' summary (R1, R5).
3. **Over-length correlates with transcription**: Axelrod's move-by-move retelling, Anderson's near paraphrase, Argyle's appendix tables. Only Achen is on target.
4. **Toy examples are arithmetically perfect.** They do not always target the main result (Axelrod, Anderson) and do not always match the reader's level (Anderson).

## Improvements (max 3)

1. **Hedge-diff verifier check, extended to index lines.** For every sentence in L0–L2, every intuition note and every Concepts/Instances line, make the verifier quote the source sentence and confirm two things:
   - Every hedge in the source sentence (may, might, seems, appears, probably, perhaps, I think, suggests, simplest explanation, in some sense, more or less, tends to, often) survives.
   - No comparative ("more strongly related to X than Y") has become an exclusive ("X, not Y").

   This would have caught A1–A4, N2, N4, R1 and X5–X7.
2. **Printed-page detection for papers.** When `printed_pages` is empty in `units.csv` (Anderson), either fill it from the footer or add a `checks.py` rule: if Reading notes state an offset ("printed = pdf + K"), reject `(pdf N)` citations. Also backfill `printed_pages` for every `kind=paper` row before wave 2.
3. **Length and toy discipline.**
   - Regression tables the text does not discuss get one summary line plus a page pointer, unless a coefficient contradicts the text, in which case say so in Questions.
   - Fail the length check above 1.3 × target.
   - The Toy example must (a) illustrate the L0 idea, (b) compute every effect it claims, and (c) use only math listed in Prerequisites.
