# Independent audit: wave 4, argumentative prose (Schelling ch. 8, Zaller ch. 8, Quine 1951, Pearl ch. 6, Rogers ch. 6 part 1)

Auditor: Claude Opus 5.5. I did not write or verify these digests. Date: 2026-10-14.
Pipeline audited: Sonnet 5.5 digest pass (prompt v2.2) plus independent verifier (v2.2). All five digests are `verified: repaired`. In this wave the length target was lowered (`build.target_words`: min(max(1000, 0.30·sw), 0.70·sw); 0.42·sw for image-heavy units; cap 6,000).

**Method.** I extracted every source page with `pdftotext -layout` and mapped the pages:
- Schelling: pdf N = printed 216+N.
- Zaller: pdf N = printed 150+N.
- Quine: pdf N = printed 18+N; pdf 1 is the JSTOR cover.
- Pearl: excerpt pdf N = book pdf 176+N.
- Rogers: excerpt pdf N = book pdf 284+N.

I checked every digest claim against the page it cites. I checked these page images as ground truth:
- Schelling pp. 218, 229, 234 (the "threateneds" misprint, "i per cent", "suits as").
- Zaller p. 154 (Eq. 7.5) and p. 179 (Fig. 8.9 cohort labels).
- Quine pp. 29–30 ("unmarried men"; the pdf/printed offset).
- Pearl Tables 6.1–6.6 and Figs. 6.5 and 6.8 (book pdf 179–180, 184, 187–189, 192–193, 199).

I recomputed every number: Zaller Tables 8.1–8.7, all twelve Table 8.4 change rates, Pearl's percentages and averages, all toy arithmetic, Rogers's figures, and Schelling's 0.98ⁿ. I also ran a 12-gram verbatim-overlap scan of each digest against its source.

In every digest I checked these against the source sentence:
- every L0–L2 sentence;
- every intuition note;
- every Concepts and Canonical-instances line;
- nearly every L3 bullet.

**Severity scale (from the brief).**
- *Critical:* a wrong, reversed, strengthened or weakened claim; a claim not in the source; misattributed voice.
- *Major:* a wrong page reference; a missing key argument; a dropped hedge; three or more undefined terms.
- *Minor:* wording or format.

Hedges follow the wave-2/3 rule:
- **Major:** losing the hedge changes a claim's modal status, scope, condition or epistemic status, or the claim is a summary-level central claim.
- **Minor:** a degree word changes in a side remark.

As in wave 3, an added "only" that turns a sufficient condition into a necessary one is rated **major** when the context supports the stronger reading, and critical when it does not.

---

## Summary

| Digest | Claims checked (approx.) | Critical | Major | Minor | Coverage | Words: digest / source / target | Verifier issues fixed |
|---|---|---|---|---|---|---|---|
| Schelling, *Strategy of Conflict* ch. 8 | 72 | 0 | **4** (1 coverage) | 10 | 8/8 sections; 1 key argument missing | 3,198 / 6,326 / 1,898 (**1.68×**; 0.51× source) | 23 |
| Zaller, *Nature and Origins* ch. 8 | 98 | 0 | 1 | 9 | complete | 5,904 / 14,302 / 6,000 (0.98×; 0.41× source) | 18 |
| Quine, "Two Dogmas" | 86 | 0 | 3 | 10 | complete | 4,209 / 10,354 / 3,106 (**1.36×**; 0.41× source) | 19 |
| Pearl, *Book of Why* ch. 6 | 82 | 0 | 1 | 7 | complete | 4,858 / 9,285 / 3,900 (1.25×; 0.52× source) | 17 |
| Rogers, *Diffusion* ch. 6 pt 1 | 80 | 0 | 3 | 10 | complete | 3,852 / 9,438 / 2,831 (**1.36×**; 0.41× source) | 17 |
| **Total** | **≈418** | **0** | **12** | **46** | | | 94 |

**Estimated surviving error rate.**
- Critical errors: **0** in ≈418 claims (wave 3: 1 in ≈335; wave 2: about 1 per 100). This is the first wave with no critical errors.
- Errors of any severity: about 14 per 100 claims (wave 3: 18).
- Majors by type:
  - Three are undefined-term majors (Q, PE, R). The P-4 glossary line is still absent.
  - Four are a strengthened, dropped or narrowed condition or scope in a summary line or Concepts line (S-M2 "only so long as", Q-M1, Q-M2 "sufficient only", Z-M1).
  - Two are a scope or condition dropped in the L3 body (S-M3 "some of the most momentous", R-M2).
  - One is a key sentence garbled from a misprint (S-M1).
  - One is a missing key argument (S-M4).
  - One gives a reason the source does not give (R-M1).
- Page references are good. About 300 were checked, and all fall on the right page or a correct range. One L2 bullet cites the wrong range for two definitions (R-m1).
- Voice handling is very good in all five:
  - Schelling's rhetorical questions are kept as questions or answered with their clue.
  - Quine is kept apart from Kant, Carnap, the verification theorists and the "it is often hinted" view.
  - Pearl is kept apart from vos Savant, the critics, Savage, Lindley/Novick, Lord, both statisticians and Wainer/Brown.
  - Rogers is kept apart from Greenberg, seat-belt nonadopters, IRRI breeders and the defenders of clitoridectomy.
  - Zaller is kept apart from his simulations and footnotes.
  - No de-attribution survived.
- Numbers are exact in all five. That covers every Zaller table cell I checked, all of Pearl's tables, and Rogers's and Schelling's figures. All toy arithmetic is correct.

**Length and coverage under the lowered target (the question for this wave).**
- **Shortening did not cost much content.** Every section of every unit is covered. Only Schelling loses a key argument: the two-sided calibration of the risk, p. 232 (S-M4).
  - The other losses are minor: memorable lines and secondary examples.
  - Zaller at 0.98× target and Pearl at 1.25× show that full coverage fits the new targets, including all numbers and tables.
- **But the lower target is not being met.** Three of five digests are still above 1.3× target (Schelling 1.68×, Quine 1.36×, Rogers 1.36×). All five are at or below 0.52× source.
- Content loss does not track length:
  - Schelling is the longest relative to target, yet it is the one that drops a key argument. Its words go to near-paraphrase of the inadvertent-war and Hungary passages.
  - Zaller is on target and complete.
- The problem is budget allocation inside L3, not the target itself.

**Overall verdict: OK to continue the batch, with hand-fixes.**
- Fix the 12 majors, using the list at the end. Nine are one-line edits; the three glossary majors each need a Glossary line.
- Process issues to fix before wave 5:
  - (a) The P-4 glossary line has still not been deployed.
  - (b) The length gate still only warns, and three of five digests are above 1.3×.
  - (c) Page-image selection missed Zaller's equation page. The digest then reconstructed Eq. 7.5 from a garbled text layer. The reconstruction was correct, but the L3 meta-commentary about it has to go.

---

## 1. Schelling, *The Strategy of Conflict*, ch. 8 "The Threat That Leaves Something to Chance" (pp. 217–238)

File: `wiki/works/schelling-1960-conflict/ch08-threat.md`

**Checked and correct.** L0, L1 (except S-m1), L2 b1–b5 and b8 are correct. In L3, the following are correct:
- Opening: ex ante vs ex post; the two ways to make a threat credible; the trip-wire purpose; "As a rule"; the bluff-confirmation argument.
- The "I can't be altogether sure" quote; the sources of uncertainty.
- Inadvertent war:
  - "It seems likely" kept as "probably".
  - The rhetorical question answered with its clue ("May they not perceive…").
  - "as far as this particular mechanism is concerned".
  - The three features and Russian roulette.
- Limited war:
  - The sequence-of-decisions view vs the "another interpretation" view, with "almost certainly" kept.
  - The two-part threat; "odds … a matter of judgment".
  - The three reasons, including one-in-twenty/nineteen-to-one; the scaling caveat; new weapons.
  - The trip wire as a graduated series, "at least to some extent" kept; Quemoy with "may" kept.
- Risky behavior: "within moderate limits above zero" and its scope "for the side that is in danger of losing"; the list of actions.
- Reprisal: "might be considered" and the parenthetical alternative; "the odds may still be against it"; "not necessarily to propose them".
- Compellence:
  - The bridge/grass and car examples; "often" kept.
  - The 1 per cent equivalence with "somewhat"/"equivalent" read flexibly; rocking the boat.
  - The black box, verified against the p. 229 image; the "too big a threat can defeat its purpose" quote.
  - The Hungary missile example; Berlin as "may be read"; "potent even … little expectation that we would win".
- Brinkmanship: the definition; the curved slope; the keep-them-guessing argument, with "as long as" correct in L3.
- Imperfect decision: the three reasons; "no 'firm' plan"; the extrication sentence; "used against us"; the trip-wire close.
- Toy:
  - 0.98⁵ = 0.9039, so the cumulative risk is 0.096.
  - 0.98¹⁰ = 0.8171, so the cumulative risk is 0.183.
  - p = 1 is self-defeating.
  - The toy is on the main idea.
- Concepts and instances: correct (apart from S-M2's L2 twin).
- Reading notes: "i per cent" and "suits as" match the images.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| S-M1 | L3 Opening ¶3: "The key is that the final decision is 'not altogether under the threatened's control'." | The book prints the misprint "threatened**s**" (italic). The digest turns it into "threaten**ed's**", which means the *threatened party*. That is the opposite of the chapter's key idea: the *threatener* does not fully control the decision, as the next paragraph says ("outside of the threatener's control"). The misprint is not flagged in Reading notes. L0–L2 have it right, but the defining sentence of the chapter now reads wrongly. Borderline critical. | p. 218 image: "*the final decision is not altogether under the threateneds control.*" | major |
| S-M2 | L2 b7: "Leaving the enemy guessing may make sense **only** so long as the uncertainty is not about our own motivation" | Adds "only". Schelling's sentence is a sufficient condition: "it may make sense to try to keep the enemy guessing as long as we are not trying to keep him guessing about our own motivation". The preceding paragraph does support the stronger reading ("This idea may be misconceived if…"), so this is the wave-3 KE-M2 pattern. L3 states it correctly. | p. 234 | major |
| S-M3 | L3 Imperfect decision ¶1: "The threat rests on the view that momentous decisions are made by a process that is not fully predictable" | Scope quantifier dropped. Schelling says "**some of** the most momentous decisions of government are taken by a process that is not entirely predictable". He also adds "**somewhat** inadvertently". The digest turns a claim about some decisions into a claim about all of them. | p. 235 | major |
| S-M4 | Coverage, L3 compellent section ("Either way, even small-scale war may work if it adds a small but appreciable probability of enormous war") | Missing key argument: the **two-sided calibration** of the risk. The probability must be "small enough that the Russians believe the West could bring itself to create it, large enough to make it unprofitable for them to let it occur". This is the chapter's design rule for the size of the threat. It is the credibility half that pairs with the p. 230 "too big a threat" point. The digest also turns "an important reason why … might be effective is that…" into a condition ("may work if"). | p. 232 | major |
| S-m1 | L1, last sentence ("even if we never use it … may explain our own tactics") | Source: "even if we do not **consciously** use it ourselves, even tacitly", and "we may **misjudge** some of the tactics we do use if we fail to recognize" the risk ingredient. "Never use it" loses the point that we may use it without knowing. | pp. 237–238 | minor |
| S-m2 | L2 b6, last sentence ("When the threat starts fulfilling itself over time, Schelling calls **it** a superior and necessary alternative") | "It" reads as the self-fulfilling threat. Schelling's subject is "the small-probability threat". | p. 230 | minor |
| S-m3 | L3 inadvertent war ("This threat can be highly credible") | Drops the condition "Here is a threat—**if a mechanism like this exists**—…" and turns "could be most credible" into "can". The earlier "Suppose…" framing softens the effect. | p. 220 | minor |
| S-m4 | L3 Risky behavior ("Otherwise it becomes a contest of nerves") | Source: "otherwise it **may turn out** to be a contest of nerves". This modal hedge sits in a side remark. | p. 226 | minor |
| S-m5 | L3 Imperfect decision ("three reasons this is not cynical"); keep-guessing ("events manifestly beyond our comprehension") | Degree words dropped: "not … an **unusually** cynical view"; "manifestly **somewhat** beyond". | pp. 234–235 | minor |
| S-m6 | L3 compellent ¶1 ("Deterring (stopping a move)") | The gloss is ambiguous. "Stopping a move" can mean making him *cease* doing something, which Schelling classes as compellence ("do something (or cease doing something)"). Deterrence is keeping him "from starting". The Concepts line is correct. | p. 228 | minor |
| S-m7 | Coverage (author's examples and lines) | Omitted points: the 2 per cent → 7 per cent announcement example ("one cannot raise the risk just by saying so") and "a limited war can get out of hand by degrees" (p. 225); "the less likely … contained by local resistance, the more reason … to fall back upon the deliberate creation of mutual risk" (p. 225); the city-a-day reprisal idea (p. 226); "a 'little bit' of death … is a near equivalent" (p. 229); "not a small bit of retaliation, but a small probability of a massive war" (p. 232); "the more moderate risk may deter anything that is still within his control" (p. 223); the roped adversary on the slope (p. 233). | pp. 223–233 | minor |
| S-m8 | L3 Imperfect decision, last paragraph | Out of order. The "extricate itself … appreciable risk" sentence comes **before** "One does not expect a government…" in the source. The digest reverses them. | p. 237 | minor |
| S-m9 | Whole digest (`level: UG`) | *Massive retaliation*, *graduated reprisal*, *satellites* and *Quemoy* are used without a gloss. These are below the three-technical-term threshold because two are proper nouns. | pp. 222–226 | minor |
| S-m10 | Reading notes, bullet 4 ("Only the text layer was available to me…") | First-person meta-commentary. (The unit has `image_pages = 0`, so the statement is true, but it belongs in pipeline logs.) | — | minor |

**Coverage.**

| Section / key argument | In L3? |
|---|---|
| Opening: "will" vs "may"; bluff confirmation; key = decision not under threatener's control; sources of uncertainty | yes (key sentence garbled, S-M1) |
| Inadvertent war: rises with crisis; is it a threat?; three features; Russian roulette | yes |
| Limited war as risk generator: two-part threat; three reasons; trip wire as graduated series; Quemoy | yes (p. 223 "moderate risk may deter…" missing, minor) |
| Risky behavior in limited war: moderate risk above zero; can't announce risk; irreversible moves | yes (2%/7% example and "by degrees" missing, minor) |
| Reprisal and harassment: shared risk might be considered; nuclear reprisal's two costs | yes |
| Compellent threats: timing; punishment until compliance; moderate risk; boat; black box; small probability superior; Hungary; Berlin | yes |
| — calibration "small enough … large enough" (p. 232) | **no (S-M4)** |
| Brinkmanship: slope; definition; keep-guessing argument | yes |
| Imperfect decision: three reasons; no firm plan; importance even if unused | yes |

**Usefulness.** Faithful, well voiced and good on hedges in the body. But at **1.68× target** the length is spent on near-paraphrase of the inadvertent-war and Hungary passages, while the calibration rule and several memorable lines are dropped. Fixing S-M1 matters most, because posts will quote the defining sentence.

---

## 2. Zaller, *The Nature and Origins of Mass Opinion*, ch. 8 "Tests of the one-message model" (pp. 151–184)

File: `wiki/works/zaller-1992-massopinion/ch08-tests.md`

**Checked and correct.** L0, L1 (except Z-m8), L2 b1–b6 (except Z-m1 and Z-m2) and b8 are correct. In L3, the following are correct:
- Introduction: the three parts; "hodgepodge" → "somewhat disjointed".
- Intensity:
  - The definition; WWII as an example; "as we shall see".
  - The NES pilot: 75/45/25 percent, the reception criterion, the horse incident.
  - "may be as much a property of the audience"; fn. 2; Fig. 8.1/Table 8.6; the DC-10.
- Familiarity: "all else equal"; fn. 4.
- **Eq. 7.5:** checked symbol by symbol against the p. 154 image. The reconstruction is **correct**: $(1-(1+f+e^{a_0+a_1A})^{-1})\times(1+e^{-b_0-b_1A-b_2P})^{-1}$.
- The fn. 5 parameters; panels A–F; "even more intense / even less familiar"; Fig. 8.3 with "±10" and the proviso.
- Presidential popularity:
  - The measurement problems; the Central America baseline and 38%; 32→48%.
  - The cell B vs F logic; Fig. 8.4 (Eq. 7.7, controls, centrist definitions).
  - The liberal-Democrat compositional explanation with fn. 8; Fig. 8.5 "louder"/"more familiar"; the inertial-resistance "alternative explanation".
- New issues: the attitude-formation assumption; *Brown* as a "nonissue"; fn. 10; the freeze and economy items; the intensity and familiarity judgments ("casual examination"); cells B/E/A–D; Fig. 8.6 "reasonable" and its valence reversal.
- The four deductions (verbatim scope "at least … relatively unfamiliar"); "seems quite strong"; "less strongly supported" and its two reasons; fn. 13; the one-message caveat and "robust".
- Microfoundations:
  - The three mechanisms and the deferral.
  - fn. 14 (priming half-sample dropped); the three codes plus hostages; the three reasons the index understates.
  - Table 8.1, all 20 cells, and the note that the ratio row is an individual-level average.
  - fn. 16; "in part"; 9%.
  - Partisan resistance: logic and test; Table 8.2 unweighted means (12 cells); fn. 17; Table 8.3 (16 cells); fn. 18 (.5⁴ ≈ .06, small N); "helpful but not clinching".
- Age:
  - "by no means obvious"; the race rationale.
  - Korea: background, expectation, the 1951 item, the 5-point cohort variable from Table 8.7 note a, "presumably", and .07 with −1.60 (1.09).
  - Vietnam: lessons of Munich; fn. 20; the item coding; **Table 8.4 all 12 change rates recomputed** (e.g. 73→21 gives 71; 32→34 gives −6); fn. 21; the anomaly with "probably quite real".
  - Race: the triple interaction; Fig. 8.9 at 20/50/75 years (image checked); fn. 22; the judicial-activism explanation; the affirmative-action parallel.
  - General effects of age, with the Medicare example.
- Summary and appendix:
  - The Nov. 28 break, 32/39/48%, 457, fn. 24.
  - The two constraints and F[2,1905] = 1.6.
  - **Table 8.5 two-constraint column (all 15 values)** and **Tables 8.6–8.7**; Krosnick–Kinder.
- Toy: 0.425, 10.6%, 1.213, 44.5% and the logistic 0.5 are all correct, and the toy is on the main idea.
- Reading notes: the fn. 17 vs p. 154 tension is a good catch.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| Z-M1 | L2 b7, bold lead: "**Age is not generally linked to resistance.**" | The epistemic status is strengthened into an empirical finding. Zaller: "There is, I should add, **no reason to believe** that age will be generally associated with **greater** resistance to change" and "My argument … is **not that** age is associated with resistance". He declines a claim; he does not report a negative finding. The body sentence that follows is correct, but the bold lead is what readers carry away. | p. 180 | major |
| Z-m1 | L2 b6 ("**Older highly aware Republicans** (Korea), older liberals … show nonmonotonic patterns, which Zaller **attributes** to…") | Garbled. A nonmonotonic awareness pattern belongs to *older Republicans* across awareness levels, not to the highly aware subgroup. "Attributes" also drops Zaller's "**presumably**", which L3 keeps. | pp. 175, 177 | minor |
| Z-m2 | L2 b2 ("a typology of **six change curves**") | Fig. 8.2 has six *panels* (cells A–F), each with three curves (liberals, centrists, conservatives). | p. 155–156 | minor |
| Z-m3 | L2 b5 ("Zaller calls **this support** helpful but not conclusive") | Scope. "Helpful but not clinching" refers to evidence for *partisan* resistance at the level of considerations. It does not cover the inertial-resistance finding, which Zaller calls "strongly supported" (expectation 1) and "supported" (expectation 2). | pp. 168, 172 | minor |
| Z-m4 | L3 "The model (Eq. 7.5…)": "The text layer for this page is garbled, and no page image was supplied. The following is my reconstruction…"; Reading notes bullet 2 | First-person meta-commentary inside L3. The page image exists (the unit's 19 image pages did not include p. 154), and the reconstruction matches it exactly. Remove the caveat and the "should be checked" note. | p. 154 image | minor |
| Z-m5 | L3 typology, bottom row ("Fn. 6 gives the reason: awareness has both reception and acceptance effects") | Fn. 6 is a **condition** ("Given that awareness has both…"), not a reason. | p. 157 n. 6 | minor |
| Z-m6 | Reading notes / L3 typology | A source inconsistency is not flagged. The text says the bottom panels set "the b0 coefficient … **higher**" for more familiar topics (p. 155), but fn. 5 uses b0 = 0 (high familiarity) vs +3 (low), which is lower. The digest silently follows fn. 5. | p. 155 and n. 5 | minor |
| Z-m7 | L3 Korea results | Drops the small-N caveat: "The results, **although based on a small number of cases in the critical cells**, sustain expectations". | p. 175 | minor |
| Z-m8 | L1 ("The evidence is cumulative and supportive, **not conclusive**") | Zaller: "A variety of different kinds of evidence, **no one piece of which is conclusive**, is accumulating". This is a per-piece claim, not a verdict on the whole. L3 is correct. | p. 180 | minor |
| Z-m9 | Coverage | Omitted points: audience interest is "a factor that is **at least as important**" as coverage (p. 152); the DC-10 inference (the unaware "must be persons … entirely cut off"; p. 154); the tests are "rather demanding" by social-science standards (p. 158); "If so" in the Reagan familiarity judgment (p. 159); why the floor parameter was removed (p. 181); why liberals once favoured judicial restraint (state economic regulation; p. 179). Two unquoted 17-word verbatim spans (pp. 175–176, 177). | various | minor |

**Coverage.** Complete. All sections are covered: intro; intensity; familiarity; typology; Fig. 8.3; presidential popularity; new issues; evaluating the typology; caveat; inertial; partisan; age (Korea, Vietnam, race, general); summary; appendix. So are the key arguments, the four deductions, every table and the main footnotes.
**Usefulness.** The best digest in the wave. It is **on target (0.98×)** with full coverage and exact numbers. It shows the lowered target is workable for a data-heavy chapter.

---

## 3. Quine, "Two Dogmas of Empiricism" (*Phil. Review* 60, pp. 20–43)

File: `wiki/works/quine-1951-dogmas/main.md`

**Checked and correct.** L0, L1 (except Q-m1), L2 b1–b3, b5–b6 and b8 (except Q-m6) are correct. In L3, the following are correct:
- Opening and §I:
  - Hume, Leibniz, "two sides of a single dubious coin"; Kant's two shortcomings and the restatement.
  - Evening/Morning Star; Scott/Waverley; 9/planets (Quine's "presumably" softened to "parallel cases", which is acceptable); heart/kidney with "perhaps".
  - The essence quote; meanings as entities; "may well be abandoned".
  - The two classes, (1) and (2); state-descriptions with the independence condition; "reconstruction at best of logical truth"; Carnap's purpose.
- §II: lexicographer; explication and favoured contexts; synonymy "by fiat"; the transparent extreme case; the two economies; the three relations; the conclusion with its exception.
- §III:
  - *salva veritate*; matching vagueness; counterinstances with "perhaps"; wordhood.
  - Cognitive synonymy and (3); the (4)/(5) argument; "not flatly circular, but something like it".
  - The extensional language "except … debatable devices"; the two-sided conclusion; the reversal.
- §IV: green/extended; the "often hinted" view voiced; rule forms 1 and 2; *K*; ordered pairs and "bootstraps"; translation rules; *feu follet*; "unlikely to throw light"; Brutus/begat; the "metaphysical article of faith" quote.
- §V:
  - The verification theory; synonymy with a logical truth; "saved after all".
  - Radical reductionism; Locke/Hume/Tooke; "unnecessarily and intolerably restrictive"; the two developments.
  - The Aufbau: higher set theory, "first empiricist", the laziest world, "is at", the later abandonment.
  - The lingering notion; "corporate body"; "at root identical"; "nonsense, and the root of much nonsense"; "the whole of science".
- §VI:
  - The fabric and the field; "if this view is right" kept; the excluded middle and the rhetorical question kept as a question.
  - Germaneness as a "loose association"; Elm Street/centaurs; "central … merely".
  - Posits and Homer's gods, including the lay-physicist interjection and "degree, not kind".
  - The irrational-number analogy and the two salient differences ("I expect" kept); classes and forces; underdetermination.
  - Ontology and Carnap's proviso; "vaguely pragmatic inclination"; conservatism/simplicity; "more thorough pragmatism … where rational".
- Toy: on the main idea (holism) and correct.
- Reading notes: the OCR list matches; the "unmarried men" misprint is confirmed in the p. 29 image.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| Q-M1 | L2 b7: "Any statement can be held true come what may, and none is immune to revision (p. 40)." | Drops the condition on a summary-level central claim. Quine: "Any statement can be held true come what may, **if we make drastic enough adjustments elsewhere in the system**". The whole passage is also conditional on "**If this view is right**". Without the condition the bullet reads as a free-standing paradox; with it, it is holism. L3 keeps both. | p. 40 | major |
| Q-M2 | Concepts `[[interchangeability-salva-veritate]]` ("not sufficient in an extensional language, and **sufficient only** in a language that already presupposes analyticity") | Adds "only". Quine examines two languages and says interchangeability "does afford a sufficient condition" in a language with 'necessarily'. He does not claim that this is the *only* kind of language where it is sufficient. This is the wave-3 pattern of a Concepts line strengthening what L3 states correctly (L3 §III "Conclusion" is exact). | p. 30 | major |
| Q-M3 | Whole digest (`level: UG`) | These terms are used without a definition: *definiendum/definiens* (§II, used five times), *sense datum / sense-datum language*, *truth functions* and *quantification* (§III extensional language, §VI "quantify over class-valued variables"), *contextually definable singular terms*, *incomplete symbols defined in use*, *Platonic ideas*, *biconditional* (given only in parentheses). The Prerequisites line covers none of these. | pp. 22–36, 43 | major |
| Q-m1 | L1 ("**Radical reductionism is gone**, but a weaker form survives") | Scope widened. Quine says radical reductionism "has long since ceased to figure **in Carnap's philosophy**". The subtler form "continued to influence the thought of empiricists". | p. 38 | minor |
| Q-m2 | L2 b4 ("**each** either presuppose synonymy or analyticity, or fail to capture it. Quine finds that the effect is something like a circle"); §IV intuition note ("Quine says the result is something like a circle … (p. 31)") | Two problems. (a) "Something like [circular]" is Quine's verdict on the **interchangeability** argument (p. 29), not on the whole series; p. 31 summarises the circle in other words. (b) Definition has Quine's own exception, the explicitly conventional introduction of new notations, a "really transparent case" (L3 keeps it). | pp. 26, 29, 31 | minor |
| Q-m3 | §V intuition note ("there are brick houses on Elm Street is one that **seems to have a sharp** empirical reference (p. 41)") | A comparative becomes an absolute. Source: "These statements are felt … to have a **sharper** empirical reference **than** highly theoretical statements". The note also omits Quine's own stronger example: "Even a statement very close to the periphery can be held true … by **pleading hallucination**" (p. 40). | pp. 40–41 | minor |
| Q-m4 | L2 b5 ("Quine says its treatment of physical objects **fell short in principle**") | Correct against the source (p. 37), but L3 never states "in principle". It says only that 'is at' stays undefined (rule 4). | p. 37 | minor |
| Q-m5 | L3 §V countersuggestion; L2 b6 | Scope and attribution dropped: "**our statements about the external world** face the tribunal…". Quine also says the countersuggestion issues "essentially from **Carnap's** doctrine of the physical world in the Aufbau". | p. 38 | minor |
| Q-m6 | L2 b8 ("Ontology is on a par with science") | Drops "**under this view**" ("Ontological questions, under this view, are on a par…"). | p. 43 | minor |
| Q-m7 | Concepts `[[use vs. mention]]`, `[[web of belief]]`, `[[Frege's puzzle]]` | Canon ids for notions that this paper does not name. Quine never says "use/mention" or "web", and he names "Frege's example", not a puzzle. Each needs "(canon link; not stated in this unit)" (rule 8). | pp. 21, 27, 39 | minor |
| Q-m8 | Coverage | Omitted points: "Science is a continuation of common sense, and it continues the common-sense expedient of swelling ontology to simplify theory" (p. 42); semantical rules "distinguishable … only by … appearing on a page under the heading 'Semantical Rules'" (p. 33); "For most purposes extensional agreement is the nearest approximation to synonymy we need care about" (p. 30); Quine's admission that a theory of confirmation of a synthetic statement has always been "baffling" (p. 39); "Both sorts of entities enter our conception only as cultural posits" (p. 41). | pp. 30–42 | minor |
| Q-m9 | L3 §VI Posits | 17-word verbatim span without quotation marks ("The myth of physical objects is epistemologically superior to most in that it has proved more efficacious…"). | p. 41 | minor |
| Q-m10 | Reading notes, bullet 1 ("printed = pdf − 18") | Wrong sign. pdf 2 = printed 20, so printed = pdf **+** 18 (confirmed: pdf 12 shows printed 30). | pdf 2, 12 | minor |

**Coverage.**

| Section / key argument | In L3? |
|---|---|
| Opening: two dogmas; effects (blurring metaphysics/science; pragmatism) | yes |
| I: meaning ≠ naming ≠ extension; meanings abandoned; two classes; state-descriptions | yes |
| II: lexicographic definition; explication; conventional abbreviation; formal definitions | yes |
| III: interchangeability; cognitive synonymy; (4)/(5) quasi-circle; extensional language; reversal | yes |
| IV: green/extended; S-for-L; two rule forms; ordered pairs; *feu follet*; linguistic/factual components | yes |
| V: verification theory; radical reductionism; Aufbau and "is at"; surviving dogma; dogmas identical; whole of science | yes (Carnap-credit, minor) |
| VI: field of force; revisability; periphery; posits; irrationals; ontology on a par; degree not kind; thorough pragmatism | yes ("continuation of common sense", minor) |

**Usefulness.** Accurate, and Quine's voice is cleanly separated from the views he examines. At 1.36× target, L3 is a close section-by-section paraphrase. Q-M1 matters most for later posts: "any statement can be held true come what may" without its condition is the most misquoted line in the paper.

---

## 4. Pearl & Mackenzie, *The Book of Why*, ch. 6 "Paradoxes Galore!" (book pdf 177–202)

File: `wiki/works/pearl-2018-bookofwhy/ch06-paradoxes.md`

**Checked and correct.** L0, L1, L2 b2–b8 are correct. In L3, the following are correct:
- Opening ("whiffed rather badly", voiced).
- Monty Hall:
  - The puzzle; 10,000 letters; Table 6.1 (image); the row-2 inference plus the marked added step; telepathy as "most compelling" reason.
  - The data-generating process and Fisher; Table 6.2 rows 2 and 4 (image: (1,3 goat) and (2,3 goat)).
  - Figs. 6.1/6.2; the collider; "no cause"; the Bayesian "survived a test" theme; belief propagation 2/3 and 1/2; Erdős, Diaconis, "rewired our brains".
- Berkson and colliders:
  - The Berkson diagram and positive vs explain-away; **Table 6.3, all 12 cells** (image).
  - Sackett "admits"; Pigou/Burks/Simon; the two-coin experiment (~75); Reichenbach, voiced, "too strong"; "too ethereal"; unconscious selection; the dating example.
- Simpson:
  - The BBG story; Novick, voiced; **Table 6.4** (image) and the 5/7.5/30/40/22/18 percentages; the four criteria.
  - Reversal vs paradox; the fraction inequality; **Table 6.5** (image; .298/.300, 1,046/1,284).
  - "Prove it mathematically"; Savage, with the 8% vs 7.5% discrepancy correctly flagged; the flaw; the corrected principle with its proviso; do-operator; the three statements.
  - Fig. 6.4 and 17.5/23.75; BBB with the misprint flagged; **Table 6.6** (image: Low/High BP rows); Fig. 6.5 (image: direct arrow present); "maybe the main".
  - Simpson 1951; Lindley/Novick and 2009; the temporal-order objection and Pearl's reply (M-bias), voiced; kidney stones; thyroid; the "symptom vs disease" warning signs.
- Pictures and Lord:
  - Exercise/cholesterol with "may" kept.
  - Lord's two statisticians, voiced; Lord's quotes; the sure-thing "works only" condition.
  - Fig. 6.8 (image: S→W_I, S→W_F, W_I→W_F, −1/+1); "out of habit" hedged; no control diet.
  - Wainer/Brown and the arrow reversal; "unambiguously correct"; the summary.
- Toy: Bayes for both games; every fraction is correct.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| PE-M1 | Whole digest (`level: HS`) | These terms are used without a definition: *explain-away effect* (Berkson), *M-bias* (Pearl's reply), *belief propagation*, *do-operator / do-calculus*, *Bayesian network*, *direct effect*. The Prerequisites line names collider, confounder, mediator and back-door path as earlier-chapter ideas, but an HS-level digest still needs the P-4 glossary. | book pdf 182, 184, 191, 194, 199 | major |
| PE-m1 | L2 b1 ("Studying them shows how the brain reasons (pdf 177)") | Correct against the source ("Like optical illusions, they also reveal the way the brain works"), but the L3 Opening omits it (rule 4). | pdf 177 | minor |
| PE-m2 | L3 Berkson ("The debate continues, now about how large the bias is") | Drops "**to some extent**" ("The debate is, to some extent, ongoing"). It also omits that epidemiologists "refused to believe" Berkson until Sackett's "strong evidence" in 1979, which is the point of the story. | pdf 184 | minor |
| PE-m3 | L3 Savage ("says it rests on causal logic") | Drops "**when properly interpreted**" ("when properly interpreted it is based on causal, not classical, logic"). | pdf 190 | minor |
| PE-m4 | L2 b7 ("A confounder (Gender) means stratify. A mediator (Blood Pressure) means pool.") | Stated as general rules. Pearl argues from each diagram (no back-door path; conditioning disables a causal path). L1's "In his examples" is the right hedge, and L2 should match it. | pdf 191–193 | minor |
| PE-m5 | Coverage | Omitted points: "Our strong intuitive belief that a BBG drug is impossible **suggests** that humans … use something like the do-calculus" (pdf 191; Pearl's thesis about causal wiring); Simpson "did not suggest that … statisticians should embrace that extra information" (pdf 193); Simpson's paradox "probably happens more often than journal articles report" (pdf 194); Pearl's framing of *two* explanations, causal and Bayesian, where the Bayesian one "does not really explain why we perceive it as so paradoxical" (pdf 183). | pdf 183–194 | minor |
| PE-m6 | L3 Opening | 17-word verbatim span without quotation marks ("…a warning sign that something might be amiss with viewing the world without a causal lens"). | pdf 177 | minor |
| PE-m7 | Reading notes, bullets 1 and 6 ("I did not digest it"; "I checked the arithmetic") | First-person meta-commentary. | — | minor |

**Coverage.** Complete. All five parts are covered: opening; Monty Hall; Berkson; Simpson (story, reversal vs paradox, sure-thing, Drug D/B, history, real cases, warning signs); pictures and Lord, including Wainer/Brown. So are all six tables and the diagrams that carry arguments.
**Usefulness.** Excellent. Every number matches the table images, and the voice tags are exemplary. It is inside the 1.3× gate (1.25×) despite six tables. The glossary is the only real gap for an HS-level reader.

---

## 5. Rogers, *Diffusion of Innovations* (5th ed.), ch. 6 part 1 (book pdf 285–312)

File: `wiki/works/rogers-2003-diffusion/ch06-attributes-p1.md`

**Checked and correct.** L0, L1, L2 b2–b5 and b7 are correct. In L3, the following are correct:
- Opening and rap: 71%/<20%; "dangerously incorrect"; naming and positioning; the rap case (radio embargo, Greenberg voiced, cassettes, compatibility with rebellion).
- Rate of adoption: the definition; 49–87% vs "about half", with both reported and the discrepancy noted; the four other variables; individual-optional; interpersonal channels; 3–16% and critical mass; "little research".
- Measurement:
  - The classification goal; perceptions vs experts.
  - Holloway, including the sixth dimension; Moore & Benbasat (75, four rounds, 540/7, 28/15, three extra attributes, sample items, the simplicity note, validity).
  - "Generally discourages"; Goldman 116; Kearns 127/8/25 and 27% vs 26%; the open-mind conclusion; t₁/t₂ and the three approaches.
- N-Trak: $125; 1,700→17; 500 acres → ~1,000 samples; labs; anhydrous ammonia; observability; design.
- Relative advantage:
  - Definition; PalmPilot 65%; VCR $1,200→$50 and 24×, "partial picture".
  - Tarde, fashions and fads; Harvestore $50,000; status motives "seem", "likely to underestimate".
  - Overadoption: definition, causes, objective rationality, the hand calculator.
  - The ratio quote; subdimensions; Gen. 6-1; Kivlin/Fliegel; Fliegel 1968 with "apparently".
- Preventive innovations: definition; nonevent; hybrid corn 20%; births averted; seat belts 9,238/73%/30,000/60%, with nonadopters voiced; Fig. 6-2; Stanford with the "1970s and 1980" misprint flagged.
- Incentives and mandates: definition and five contrasts (Singapore); trial incentives; Rogers 1973 points 1–3; China; Article XV 100+/1.5; the mandates sentence.
- Compatibility:
  - Definition and the three objects; Los Molinos; soil conservation; the left hand.
  - IRRI's 1960s reply voiced; 40 years and 20% cheaper; bar codes $9,999.99; Lotus.
  - Clitoridectomy: WHO 130 million, objections and "defenders claim" voiced; Ghana 1994/1998, one fourth; the side effects.
  - Fals Borda.
- Toy arithmetic: 6/2 = 3, 1/2 = 0.5, 60/3 = 20, 6/3 = 2.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| R-M1 | L3 Incentives, bullet 3 ("U.S. solar-heating tax rebates in the 1970s were halted at 5–10 percent adoption, **expecting** self-generating diffusion") | The reason given is not the source's reason. Rogers: "The **cost of such incentives became too large to be affordable**, and the incentive payments were halted once a level of 5 or 10 percent adoption was reached." The self-generating expectation is why pump-priming incentives are *used*. The digest drops the stated cause and puts the design rationale in its place. Rogers's own hypothetical ("say, 20 percent … the economic incentive is discontinued") is also lost. | pdf 306–307 | major |
| R-M2 | L3 Compatibility, Miracle rice ("it often tripled yields") | Condition dropped. Rogers: "These improved rice varieties, **when accompanied by heavy applications of chemical fertilizers, the use of pesticides, thicker planting, and other management practices**, often tripled a farmer's rice yields." | pdf 310 | major |
| R-M3 | Whole digest (`level: UG`) | These terms are used without a definition: *cue-to-action* (the source defines it; the digest does not), *side-dressing*, *anhydrous ammonia* (not even identified as a fertilizer), *objective vs subjective rationality* (the source defines rationality; the digest does not), *individual-optional innovation-decision*, *awareness-knowledge*, *pump-priming*. | pdf 288, 295–296, 300, 306–307 | major |
| R-m1 | L2 b1 ("Relative advantage means … compatibility means … (pdf 287–289)") | The two definitions are on **pdf 297** and **pdf 309**. pdf 287–289 only list the names. | pdf 297, 309 | minor |
| R-m2 | L2 b6 ("may change who adopts") | Weakens Rogers's conclusion 2, "Adopter incentives **lead to** adoption … by individuals different from those who would otherwise adopt". (Conclusion 3's "may be relatively low" quality is correctly hedged.) | pdf 307 | minor |
| R-m3 | L3 Overadoption ("a change agent's role **may include** preventing 'too much' adoption"; "CAT scanners bought without justification") | Source: "The notion of overadoption **implies that one role** of the change agent is to prevent…" (weakened). CAT scanners are "**sometimes** purchased when its use cannot be justified" (hedge dropped). "Overadoption is a major problem in some fields" is also omitted. | pdf 300 | minor |
| R-m4 | L3 Economic factors ("Initial cost **matters**"); Incentives ("Incentives raise serious ethical issues") | Hedges dropped: "**may** affect its rate of adoption"; "**often** involves serious ethical issues". | pdf 297, 307 | minor |
| R-m5 | L3 Opening ("Diffusion research has studied 'people' differences much more than 'innovation' differences") | Drops Rogers's qualifier: "although the imbalance … **may be disappearing in recent years**". | pdf 285 | minor |
| R-m6 | Coverage | Omitted points: rap's success itself ("has become enormously popular in white America, and throughout the world"), which is the point of a case that begins "an innovation that would not diffuse" (pdf 286); the mandate rationale (system vs individual interests: government wants slower population growth, parents want large families; pdf 308); "The nature of the innovation determines what specific type of relative advantage … is important" (pdf 297); "When the price … decreases so dramatically … a rapid rate of adoption is encouraged" (pdf 298); the definition of a communication campaign (pdf 304). | pdf 286–308 | minor |
| R-m7 | Concepts `[[adopter-categories]]` ("status motives seem stronger for earlier categories") | A finding, not a definition as used here. | pdf 299 | minor |
| R-m8 | Toy example | The rate numbers (10/20/30 vs 1/2/3) are stipulated, not derived from the benefit–cost ratios, so the toy only restates Generalization 6-1. It is labelled "illustrative only". | — | minor |
| R-m9 | Reading notes, bullets 4–5 ("I did not check or correct this"; "I did not use them") | First-person meta-commentary. On lakhs: the source's "lakhs (10,000)" is an error in the source (a lakh is 100,000). Rule 14 allows a misprint note when it says what the page shows, and that is what is needed here. | pdf 311 | minor |
| R-m10 | L3 IBM bar code ("which was inadequate in Italy under high inflation") | It drops the reason the six-digit limit failed in Italy: 10,000 lire "would hardly buy a loaf of bread". | pdf 311 | minor |

**Coverage.** Complete. Every section and subsection through the cut point is present: opening/rap; rate of adoption; research on attributes (measurement, organizations, eliciting, postdiction); the N-Trak case; relative advantage (economic, status, overadoption, RA and rate, preventive, Stanford, incentives, mandates); compatibility (values, previously introduced ideas). The gaps are the minor items in R-m6.
**Usefulness.** Clear and accurate, with numbers exact. At 1.36× target, L3 keeps nearly every example and figure. The extra words do not protect the rationales that R-M1 and R-m6 lose.

---

## Error patterns across the five digests

1. **No critical errors, and voice handling is solid.** All five units argue through other voices: opponents, interlocutors, quoted critics, defenders. No de-attribution survived. Rhetorical questions are kept as questions or answered with their clue (Schelling p. 219; Quine p. 40; Pearl's Lord question).
2. **Summary and Concepts lines still strengthen what L3 states correctly.** S-M2 (L2 "only so long as"), Q-M2 (Concepts "sufficient only"), Q-M1 (L2 drops "if … drastic enough adjustments"), Z-M1 (L2 bold lead) and Z-m3 all follow this pattern. In every case the L3 sentence is right. This is wave 3's pattern 2, and the verifier's index pass still compares summaries with L3 loosely.
3. **Scope quantifiers and conditions dropped in the L3 body:** S-M3 "some of the most momentous", R-M2 "when accompanied by", Q-m1 "in Carnap's philosophy", Q-m5 "statements about the external world".
4. **Undefined terms.** This is the third wave in a row with P-4 majors (Q, PE, R). HS- and UG-level digests are the ones hit.
5. **Length.** The lowered target has not been met: the median is 1.36× target and 3/5 digests are above 1.3×. The content lost does not match the words saved. Schelling (1.68×) is the one digest missing a key argument. Zaller (0.98×) is complete. The model compresses evenly instead of keeping the arguments and cutting re-narration.
6. **Misprints passed through into quotes.** S-M1: the model "corrected" a misprint into the wrong word inside a quotation. Rule 14 asks for misprints to be reported; it should also say *never silently emend inside quotation marks*.
7. **Image coverage.** Zaller's 19 image pages left out p. 154 (Eq. 7.5). The model said so in L3 itself (Z-m4). Schelling and Quine have no image pages. The OCR text was usable for both, but Schelling's misprint (S-M1) would have been visible in an image only as italic emphasis.
8. **First-person meta-commentary** persists in Reading notes and once in L3 (S-m10, Z-m4, PE-m7, R-m9; also wave 3 L-m8 and KE-m11).

## Prompt and pipeline improvements

- **Deploy P-4 (glossary line) now.** Three of five digests fail on undefined terms, as in waves 2 and 3. Proposed wording: "After Prerequisites, add `**Glossary:**` with every technical term used in L2–L3 that is not in Prerequisites, each ≤ 15 words."
- **Turn the length gate into a compression pass at > 1.3× target (P-3), with an allocation rule.** Add to rule 12: "When compressing, first cut re-narration of examples. Never cut a stated condition, a rule, or a sentence that says how large or small something must be." Schelling shows that uniform compression loses the rule and keeps the anecdote.
- **P-7 (verifier, quote-the-source for summaries and Concepts lines): extend to L2 bold leads.** For every L2 bullet and Concepts line containing *only, not, never, all*, a modal, or a bold lead, the verifier must quote the source sentence and confirm that its condition, scope and epistemic verb (*no reason to believe*, *if*, *some of*) survive. This would have caught S-M2, Q-M1, Q-M2 and Z-M1.
- **P-9 (prompt rule 14 + verifier): misprints inside quotations.** "Inside quotation marks, copy the printed text exactly, followed by [sic] or a bracketed correction, and log the misprint in Reading notes. Never emend silently." Verifier: compare every quoted span with the page text.
- **P-10 (pages.py): always include the image of any page whose text layer contains equation-like garble.** The trigger is a line with a parenthesised equation number, like `(7.5)`, plus ≥ 3 non-ASCII or stray-symbol tokens. This applies even when the image-page budget is used up elsewhere.
- **P-11 (prompt rule 15): ban first person in all sections.** Add: "Reading notes state facts about the pages. They do not describe what you did or could not do." Waves 3 and 4 both have several of these.

## Hand fixes needed now (before posts reuse these)

- **S-M1 (Schelling L3 Opening ¶3):** "The key is that the final decision is not altogether under the threatener's control (p. 218; the book misprints 'threateneds')." Add to Reading notes: "p. 218: 'threateneds control' is a misprint for 'threatener's' (cf. 'outside of the threatener's control', same page)."
- **S-M2 (L2 b7):** "…Leaving the enemy guessing may make sense as long as we are not trying to keep him guessing about our own motivation (pp. 233–235)."
- **S-M3 (L3 Imperfect decision):** "The threat rests on the view that some of the most momentous decisions of government are taken by a process that is not entirely predictable, so a nation can get into major war somewhat inadvertently (p. 235)."
- **S-M4 (L3 compellent, after Berlin):** "An important reason why even small-scale war might be effective is that it adds a small but appreciable probability of enormous war: small enough that the Russians believe the West could bring itself to create it, large enough to make it unprofitable for them to let it occur (p. 232)." Optionally echo this in L2 b6.
- **Z-M1 (L2 b7 lead):** "**Age need not mean resistance.** Zaller sees no reason to believe age will generally be associated with greater resistance; his claim is that the RAS model can specify age's effects, whatever their direction (p. 180)."
- **Q-M1 (L2 b7):** "If Quine's view is right, any statement can be held true come what may, given drastic enough adjustments elsewhere in the system, and no statement is immune to revision (p. 40)…"
- **Q-M2 (Concepts `[[interchangeability-salva-veritate]]`):** "…not a sufficient condition of cognitive synonymy in an extensional language; sufficient in a language with 'necessarily', but such a language is intelligible only if analyticity is already understood (pp. 27–30)."
- **R-M1 (Rogers Incentives b3):** "U.S. solar-heating tax rebates in the 1970s became too costly and were halted once 5 or 10 percent adoption was reached. Such pump-priming incentives are used in the expectation that further diffusion becomes self-generating (pdf 306–307)."
- **R-M2 (Miracle rice):** "When accompanied by heavy fertilizer, pesticides, thicker planting and other practices, it often tripled yields…"
- **Term majors (Q-M3, PE-M1, R-M3):** add a `**Glossary:**` line under Prerequisites with the terms listed in each row.
- **Cheap minors worth doing in the same pass:**
  - Z-m4: delete the L3 meta sentence and Reading-notes bullet 2, because the image confirms Eq. 7.5.
  - Q-m10: change to "printed = pdf + 18".
  - R-m1: cite pdf 297 and 309 for the definitions.
  - PE-m4: add "In his examples" to L2 b7.
