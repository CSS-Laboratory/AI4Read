# Independent audit: Gate CC (Claude Code route) vs batch route

Auditor: Claude Opus 5.5. I did not write or verify any of these digests. Date: 2026-10-14.
Route audited: Claude Code Sonnet sessions (digest agent + separate verifier agent, prompts v2.2), all `verified: repaired`.
Units: three parity units (`*.cc.md`, compared with the batch route) and two re-done units (Meadows editor's note, Popper 1959 preface).

**Method.** I read `DIGEST_SPEC.md` and `prompts/digest.md` first. Then, for each unit, I read the whole source and checked the digest claim by claim.
- **Kuhn, Gelman, Popper, Meadows:** full text layer (pdftotext, page breaks marked).
- **Images:** all 15 Dennett spreads (scan, no text layer); all 8 Meadows pages; Popper pdf 7–8 (to confirm the page swap); and the Gelman equation pages, rendered at 110 dpi: pp. 105, 107, 109–111, 114–118, 125, 129. Each Gelman equation was compared with the image symbol by symbol.
- **Recomputed** (by hand and in Python): the Kuhn toy ($\Delta m = 5/9\times10^{16} = 5.6\times10^{-17}$ kg), all three Gelman toy groups (13 / 2; 8.4 / 0.8; 10.8 / 3.2), the Dennett sprinkler toy and the Meadows furnace toy (15, 17.5, 18.75; 18, 19.6).
- **Batch baseline.** As briefed, I compared with the *original* batch audit findings, not the hand-fixed files. For every new-route critical or major error, I also opened the **pre-fix batch digest** at the same spot (git `f87f64b` for Kuhn, `40d4acf` for Gelman and Dennett). This shows whether the batch route got that spot right.

**Severity scale** (as briefed, and as used in the wave-2 audits):
- **Critical:** a wrong, reversed, strengthened or weakened claim; a claim not in the source; a misattributed voice; a wrong equation or number.
- **Major:** a wrong page reference; a missing key argument or result; a dropped hedge or scope qualifier; three or more undefined terms.
- **Minor:** wording or format.

**Calibration with the batch audits.** I scored severities the way the batch auditors did:
- A dropped hedge or scope qualifier is **major**. A swapped degree word in a side remark is **minor**.
- A weakening of a quantifier ("all" → "almost every"; "necessarily, for any y" → "on average") is **major**, not critical. The batch auditors treated slight strengthenings and weakenings this way (G4, U-m3).
- The Dennett batch audit (wave-2 regression) used a rubric in which a misattributed voice is **major**, not critical. For Dennett I therefore give both scorings.

**Note on comparability.** My audit is denser than the batch audits: 75–115 checks per parity digest, against 52 / ~95 / 39. Minor counts are therefore not comparable. The parity verdict rests on critical and major errors, each checked against the batch digest.

---

## Summary

| Digest | Checks | Critical | Major | Minor | Words: digest / target (ratio) | Length vs source |
|---|---|---|---|---|---|---|
| 1. Kuhn ch. IX (cc) | 78 | **1** | **9** | 13 | 3,739 / 2,015 (**1.86×**; 1.39× against the batch-audit target of 2,687) | 0.56× |
| 2. Gelman BDA3 ch. 5 (cc) | ~115 (24 numbered eqs, ANOVA table, ~40 numbers) | **2** | **5** | 12 | 5,891 / 6,000 (0.98×) | 0.28× |
| 3. Dennett ch. 2 (cc) | 85 | **1** (voice; major under the regression rubric) | **3** | 13 | 6,520 / 5,670 (1.15×) | ~0.6× |
| 4. Meadows, editor's note | 38 | **1** (voice) | **2** | 7 | 1,923 / 1,000 (**1.92×**) | **1.25×** (longer than the source) |
| 5. Popper, prefaces 1934/1959 | 72 | **1** | **2** | 10 | 3,211 / 1,344 (**2.39×**) | 0.80× |
| **Total (5 units)** | ~390 | **6** | **21** | 55 | | |

### Parity, side by side (units 1–3)

| Unit | Batch residual (original audit) C / M / m | New route residual C / M / m | New C+M also present in the batch digest | New C+M where the batch digest was **correct** | Batch C+M fixed by the new route |
|---|---|---|---|---|---|
| Kuhn ch. IX | 0 / 5 / 7 | **1 / 9 / 13** | 3 (U-M3, U-M4, U-M5) | **7** | 2 (U-M1, U-M2) |
| Gelman ch. 5 | 0 / 2 / 6 | **2 / 5 / 12** | 1 (G2, undefined terms) | **6** | 1 (G1) |
| Dennett ch. 2 | 0 / 1 / 2 (regression rubric) | **1 / 3 / 13** (brief rubric); 0 / 4 / 13 (regression rubric) | 0 | **4** | 1 (N-D1) |
| **Total** | **0 / 8 / 15** | **4 / 17 / 38** | 4 | **17** | 4 |

**Bottom line.** Across the three parity units the new route leaves 21 critical-or-major errors; the batch route left 8.
- At 17 of the 21 spots, the batch digest was **correct**. These are not errors that a stricter auditor would also have found in the batch files.
- The new route does fix 4 of the 8 batch majors. Those batch errors were idiosyncratic.
- On balance, the new route is clearly **worse**.

---

## 1. Kuhn, *Structure*, ch. IX (pp. 92–110), `ch09-nature.cc.md`

**Checked and correct:**
- Definition of revolution (p. 92); X-rays and Kelvin/Crookes/Roentgen (pp. 92–93).
- Political parallel, mass persuasion; "no standard higher than the assent of the relevant community" (p. 94).
- Moon/galaxy; quantum theory "not exclusively"; energy conservation (p. 95).
- Three types of phenomena, "this type alone" (p. 97); caloric crisis; the "permissible view … historical implausibility" quote (p. 98).
- Positivist objection, voice-tagged (p. 99); phlogiston (pp. 99–100); "logically unexceptionable" (p. 100).
- $E_i$/$N_i$ sketch and $(v/c)^2\ll1$ (p. 101); mass conserved vs convertible; "any sense of 'derive' now generally recognized" (p. 102).
- "Take it for granted … necessary and irreconcilable" (p. 103); "actually incommensurable" (p. 103).
- Molière; collisions (Descartes → Huyghens/Wren/Wallis → Newton); gravity "reversion (not retrogression)" (pp. 104–106).
- Leyden jar, chemistry, Maxwell (pp. 106–108); Einstein / quantum reversals (pp. 108–109).
- Map and map-making; the scope phrase "incompletely but significantly" in L3 (p. 109); "most obviously" in L3 (p. 110).
- All page refs. Toy arithmetic.

**Surviving errors**

| # | Location | Problem | Evidence | Severity | In batch? |
|---|---|---|---|---|---|
| K-C1 | L3 B, last sentence | "cumulative acquisition of unanticipated novelty is **almost without exception**" means cumulation almost always happens. The source says the opposite: it is "an **almost non-existent exception** to the rule of scientific development". | p. 96 | **critical** (reversed) | no; batch: "almost non-existent exception" |
| K-M1 | L0 | "settled only by community assent, **not by neutral logic**". Kuhn: not determined "**merely**" by normal-science procedures, not settled "by logic and experiment **alone**", and we must examine "not only the impact of nature and of logic, but also" persuasion. L0 denies logic any role. L3 A keeps "merely". | p. 94 | major (dropped qualifier; L0 stronger than L3) | no; batch L0: "by the criteria of normal science alone" |
| K-M2 | L2 b3; L3 A | Evaluative procedures "depend on the paradigm being judged". Source: they "depend **in part** upon a particular paradigm". | p. 94 | major (scope qualifier) | no; batch: "depend partly" |
| K-M3 | L2 b7 | "Kuhn **rejects the view that an old theory can always be** rescued as a strict 'special case'". Source concedes: "an out-of-date theory **can always be viewed** as a special case of its up-to-date successor, [but] it must be transformed for the purpose". The whole concession paragraph (hindsight; the result "could only restate what was already known") is absent from L3. | pp. 102–103 | major | yes (= U-M4; worse, because L3 now also lacks it) |
| K-M4 | L2 b8 ("**Because** meaning change is unavoidable, successive paradigms differ in … standards"); L1 ("…changes the meaning of its key terms, **so** paradigm shifts change standards") | A causal link that is not in the source. Kuhn derives the non-substantive differences from paradigms being "directed … back upon the science that produced them", after taking the differences as "necessary and irreconcilable". Meaning change is not the cause. | pp. 102–103 | major (argument structure misreported) | no |
| K-M5 | L2 b10 | "…which is what makes paradigm debates revolutionary". Source: "what **most obviously** makes paradigm debates revolutionary". L3 keeps it. | p. 110 | major (summary hedge) | no |
| K-M6 | L3 H | "Kuhn's reply: this derivation is spurious." Source: "spurious, **at least to this point**". | p. 101 | major (dropped hedge) | no; batch kept it |
| K-M7 | L3 L, last sentence; Questions Q3 | "constitutive of nature too". Source: "display **a sense in which** they are constitutive of nature as well". | p. 110 | major | yes (= U-M3) |
| K-M8 | Whole digest | Undefined terms: logical positivism, phlogiston, caloric theory, ether, charging by induction, Leyden jar, scholastic. | pp. 98–108 | major (≥ 3 undefined terms) | yes (= U-M5) |
| K-M9 | L2 b4 ("almost every new theory"); L3 B ("virtually every new theory") | Source: "the assimilation of **all** new theories and of **almost all** new sorts of phenomena". Kuhn draws the all / almost-all contrast on purpose. | p. 96 | major (quantifier weakened; critical under a literal reading of the rubric) | no; batch: "the rule for new theories and almost all new kinds of phenomena" |
| K-m1 | L1; L2 b2 | "restricted" drops "**often**"; "problems they themselves created" stands for "an environment that they have in part created". | p. 92 | minor | |
| K-m2 | L0; Concepts `anomaly-crisis-revolution` | "the *only* route science actually has" drops "**effective**" ("no other effective way"). L0 also makes the necessity argument a reason for the name "revolution". | p. 97 | minor | |
| K-m3 | L3 F; Toy | In the objector's voice: "engineers and many physicists" drops "most" and "in selected applications". "Whenever relative velocities are small" and the Toy's "**exactly** the condition" drop "this condition **and a few others**". | pp. 99, 101 | minor | yes (≈ U-m3) |
| K-m4 | L3 B | "He first shows it need not be intrinsic". Kuhn says only that such reasons "do not derive from the logical structure" of knowledge. He then argues that there *are* intrinsic reasons. | p. 95 | minor | |
| K-m5 | L3 C | "Normal research is cumulative precisely because…". Source: normal research "owes its **success**" to this ability. | p. 96 | minor | |
| K-m6 | L3 G | The precedent restriction is placed under "pushed further"; the source says "**Even in its present form**". "Science develops" drops "**may**". | p. 100 | minor | |
| K-m7 | L3 K | "was not a judgment that the problem was inherently illegitimate". Kuhn's claim is that the problem *was not* intrinsically illegitimate. Also omitted: "neither a decline nor a raising of standards, but simply a change", and "could be [reversed] again". | p. 108 | minor | |
| K-m8 | L3 K | Footnote 11 "called **ironically**": an interpretation, not in the source. | p. 108 n. 11 | minor | |
| K-m9 | L3 J | Maxwell's ether talk "came to look like mere lip service" drops "**which it emphatically had not been**". | p. 107 | minor | |
| K-m10 | L3 L | "falling short of its rival's" criteria drops "**more or less**" and "**a few of** those". "The guidance needed" stands for "**some of** the directions". | pp. 109–110 | minor | |
| K-m11 | Concepts `incommensurability` | Quotes "incomplete logical contact". Source: "incompleteness of logical contact". | p. 110 | minor | ≈ U-m6 |
| K-m12 | Coverage | Omitted: "Perhaps it is another sort of enterprise" (p. 96); energy conservation came to *seem* logically higher only later (p. 98); "Is it really any wonder that the price of significant scientific advance is a commitment that runs the risk of being wrong?" (p. 101); standards changes "can transform a science … transform the world" (p. 106). | pp. 96–106 | minor | ≈ U-m7 |
| K-m13 | Intuition notes | Only 2 notes (A, H) for at least 4 major results: necessity, standards shift, reversals, constitutive. | — | minor | |

**Toy:** correct ($v/c=3.3\times10^{-8}$; $\Delta m=5.6\times10^{-17}$ kg). It is on target (meaning change of "mass"), but it repeats K-m3. **Coverage:** every part of the argument is present except the p. 102–103 concession (K-M3). **Usefulness:** clearer than the batch L3 and shorter (1.39× vs 1.61× against the same target), but the summaries are less reliable than the batch's.

---

## 2. Gelman et al., BDA3 ch. 5 (pp. 101–138), `ch05-hierarchical.cc.md`

**Checked against the images and correct:**
- (5.1)–(5.10) and (5.12)–(5.24) symbol by symbol, including (5.17), (5.20) and the final line of (5.21). The unnumbered p. 107 covariate formula and both Jacobian results.
- Rat tumor: 4/14, Beta($\alpha$+4, $\beta$+10), 0.136/0.103, (1.4, 8.6), Beta(5.4, 18.6), 0.223/0.083, 0.286, mode (−1.75, 2.8) → (2.4, 14.0), $E(\alpha|y)=2.4$, $E(\beta|y)=14.3$, 0.14.
- Divorce: seven rates, 6.5, 13.9.
- Eight schools: 7.7, 16.6, 4.1, [−0.5, 15.9], 4.6/7, order statistics 26…−9, 28.4/14.9, 93% with 14.5/9.1, 97–99.96%, 22/200, 141/200, "almost twice as wide".
- Beta-blockers: 25%, 0.13, studies 1/6/18 and 2/18 vs 7/14, 0.060/0.071, Table 5.5 intervals, [0.69, 0.90] vs [0.70, 0.85], "just over 10%".
- §5.7: $J\ge3$, $J\ge4$, $s^2=\beta/\alpha$, $\nu=2\alpha$, $A=25$, $\tau<50$.
- Page ref for the Table 5.3 discussion now spans the page break (batch G6 fixed). Exercise numbers and pages (1–2, 3, 5, 9, 12) are correct.
- Toy recomputed.

**Surviving errors**

| # | Location | Problem | Evidence | Severity | In batch? |
|---|---|---|---|---|---|
| G-C1 | L3 §5.4, ANOVA table, "Between groups" SS | Digest: $\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$. The image prints $\sum_i\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$. The SS is off by a factor $n$, so the stated $E(\text{MS})=n\tau^2+\sigma^2$ no longer follows. | p. 114 image | **critical** (wrong equation) | no; batch: $\sum_i\sum_j$ |
| G-C2 | L3 §5.7, inverse-gamma bullet | "for **moderate $\epsilon$** inference is highly sensitive to it". The source's condition is "**for datasets in which low values of $\tau$ are possible**". The condition is dropped and replaced by a different one. | p. 130 | **critical** (dropped/changed condition) | no; batch: "When low $\tau$ is possible" |
| G-M1 | L2 b1 | Exchangeability "**licenses** treating them as a sample from a shared population distribution". Source: the iid mixture "is **usually** all that we need … **in practice**". de Finetti holds only as $J\to\infty$, and L3 itself gives the die counterexample. L2 is stronger than L3. | pp. 104–105 | major | no; batch: "usually all that is needed … in practice" |
| G-M2 | L2 b6 ("three different estimands with different, **increasing** uncertainty"); §5.6 intuition note ("the third is **always** the most uncertain") | The source orders only the new-study effect against the overall mean ("uncertainty is even greater"). The ranking of the observed-study effect, and "always", are not in the source or in L3. Table 5.4 study 1 has the same 95% width (0.69) as the predicted effect. | p. 128 | major (L2 beyond L3) | no |
| G-M3 | L3 §5.7, calibration demo | "increases $\hat\theta$ **on average**". Source: "will **necessarily** increase $\hat\theta$ **for any data y**". | p. 129 | major (quantifier weakened) | no; batch: "necessarily raises $\hat\theta$ for any $y$" |
| G-M4 | L3 §5.1, end | "The author **calls** the point-estimate shortcut 'empirical Bayes'". Source: "which is **sometimes called** empirical Bayes"; the authors avoid the term. The rest of the sentence keeps their stance, so a reader is not seriously misled. | p. 104 | major (voice; self-corrected in the same sentence) | no; batch: "sometimes called" |
| G-M5 | Whole digest | Undefined terms: Jacobian, logit, scaled inverse-$\chi^2$, inverse-gamma, half-$t$, ANOVA F test, order statistics, improper posterior. The Prerequisites line still lacks change of variables and logit. | pp. 110–130 | major (≥ 3 undefined terms) | yes (= G2) |
| G-m1 | L3 §5.3–5.4 | Displayed steps are skipped (rule 6): the first line of (5.6) and of (5.16); the second line of (5.14); and the two intermediate lines of (5.21) (ratio $p(\mu,\tau|y)/p(\mu|\tau,y)$, then the substitution $\mu=\hat\mu$ with $N(\hat\mu|\hat\mu,V_\mu)$). The last of these leaves $V_\mu^{1/2}$ unexplained. | pp. 110, 115, 117 | minor | |
| G-m2 | L3 §5.4; Bridges | (5.18)–(5.19) are on p. 116 but cited only as p. 117. The bridge cites the weighted combination at p. 114; it is on p. 115. | pp. 115–116 | minor (ref across a page break) | ≈ G6 type |
| G-m3 | L3 various | Degree words strengthened: "attributes this to" ("**suggests**", p. 127); "the author argues is too strong" ("**seems** too strong", p. 118); "noticeably different" ("differs **somewhat**", p. 112); half-count "sometimes recommended" ("**often**", p. 125); uniform on $\tau^2$ "worse miscalibration" ("**seems** to have", p. 130); "should lower your estimate" ("would **probably**", p. 104). | pp. 104–130 | minor | ≈ G4 type |
| G-m4 | L3 §5.7, 3 schools | "used precisely **because** it is not meant to represent real prior belief … only as far as the data **demand**". Source: with only 3 schools "we went to the trouble of using a weakly informative prior, a distribution that was not intended to represent our actual prior state of knowledge …, but rather to constrain the posterior distribution, to an extent **allowed** by the data". Invented causal link; changed sense. | p. 132 | minor | |
| G-m5 | L3 §5.7, conjugate-limit bullet | "$p(\tau)\propto\tau^{-1}$ … is an inverse-$\chi^2$ with 0 df". The inverse-$\chi^2$ form is the density on $\tau^2$, and $p(\tau^2)\propto\tau^{-2}$ is omitted. Also omitted: "cannot easily be seen as a limit of proper inverse-$\chi^2$". | p. 129 | minor | |
| G-m6 | L1; L2 b5 | "noisy, small, **or extreme** groups shrink more" (not in the source; in the normal model the shrinkage fraction depends on precision). "**often** 0" for the mode of $\tau$. "neither … is **defensible**" (source: "fully satisfactory"). | pp. 113, 120–122 | minor | |
| G-m7 | Coverage §§5.1–5.3 | Omitted: the common-population assumption, its failure (lab A vs B, time trends) and variance inflation (p. 103); "Unless you are familiar with divorce statistics … fairly vague" (p. 105); the covariate divorce example (p. 106); "both kinds of replications … model adequacy" (p. 108); both grid ranges (pp. 111–112); the attitude meaning of "noninformative" (p. 110). | pp. 103–112 | minor | ≈ G5, G7 |
| G-m8 | Coverage §§5.5–5.7 | Omitted: "no prior reason to believe that any of the eight programs was more effective" (p. 119); "an effect as large as 28.4 points in any school is unlikely" (p. 121); 200 draws adequate; "flexible enough to adapt to the data" (pp. 123–124); "(perhaps misguidedly)" (p. 126); "can, but do not necessarily" (p. 128); "inherently provisional" (p. 129); "realistic upper limit on $\tau$ of 100" (p. 130). | pp. 119–130 | minor | ≈ G8 |
| G-m9 | L3 §5.6 Results | "individual posteriors are skewed, more so for imprecise studies". Source: they are skewed away from the overall mean, and the imprecise studies are **longer-tailed**. | p. 127 | minor | |
| G-m10 | Concepts | `[[credible-interval]]` adds "interpreted as direct probability statements" (not in this unit; no canon-link tag). `[[marginal-likelihood (evidence)]]` has an id with a space and parentheses. | pp. 120, 127 | minor | |
| G-m11 | Reading notes; L3 §5.2 | Verifier residue: "…for hyperparameters. 102, 104, 107, … 131)." A page number is misused as an equation tag (`\tag{p.107}`). | — | minor (format) | |
| G-m12 | Exercises | Ex. 5 gloss: "the formal reason why learning about one group informs another". This interpretation is not in the source. | p. 134 | minor | |

**Toy:** correct and on target (partial pooling, with precision-dependent weights). **Coverage:** §§5.1–5.8 are in order; Table 5.1/5.4 columns are not reproduced. **Usefulness:** good length (0.98×), intuition notes after every section. But G-C1 sits in a table a reader would copy. **The CC verifier returned `pass` with 0 critical on its first pass (GATE-CC.md), with the page images available.**

---

## 3. Dennett, *The Intentional Stance*, ch. 2 (pp. 12–41), `ch02-true.cc.md`

**Checked against the images and correct:**
- Samarra fable; "dark, risky, and imponderable"; counting beans; milk (pp. 13–14).
- Thesis quote exact, "apparently" ×2 (p. 15).
- Astrology, the three stances, liquid helium (pp. 16–17).
- Belief rule, "normally sufficient", snake/barstool (p. 18).
- Desire list, omelette/baked beans (pp. 20–21); rationality and "clutter" (p. 21); clams, chess, thermostat, apples, lightning (pp. 21–22).
- Lectern (p. 23); chess "half a dozen", trader/politician, KGB chain quote (pp. 24–25); Nozick question kept as a question (p. 25); GM / spark plug (p. 26).
- Mrs Gardner: "**the Earthling's** performance would look like magic" (batch N-D1 fixed); fatalists quote; Hampshire (p. 27); "where there are intelligent beings…" (p. 28); strong vs milder realism (pp. 28–29).
- Thermostat de-interpretation, enrichment, "fastened", n. 5, representation quote (pp. 29–32); Twin Earth; both p. 32–33 quotes exact.
- Spencer; "we just do not know"; Skinner; LOT quote exact; "not overwhelming" (batch N-D2 fixed); combinatorial explosion; n. 6 (pp. 33–35).
- Postscript: knife-edge, "a *sort* of realism", Life rule (word for word, bracket flagged), Turing-machine stance, armor, "no backstage", Akins, Anscombe n. 1, Rorty, Quine 1969/1970, Davidson, Parfit's club and "empty", Nagel (pp. 37–41).
- About 25 page refs, all on the correct half-spread. Toy arithmetic.

**Surviving errors**

| # | Location | Problem | Evidence | Severity | In batch? |
|---|---|---|---|---|---|
| D-C1 | L3 "Objection … / **Dennett's reply:**" | Text given as Dennett's reply ("engineers can fully understand a simple thermostat…; … just a more advanced case of human epistemic frailty. He resists classifying such artifacts with 'true believers' … on such variable, parochial grounds") is the **objector's continued urging** after "But, it will be urged": "It may be true that the cleverest engineers … but this is just a more advanced case of human epistemic frailty. We would not want to classify these artifacts with the true believers … would we?" Dennett's own reply begins "That would be a particularly radical version of interpretationism … I now want to discourage it". | pp. 23–24 | **critical** (misattributed voice); major under the regression rubric | no; batch tagged it correctly |
| D-M1 | L1 | "sometimes **only it works**". Source: "often the only strategy that is **at all practical**". L3 says "only practical method". The Laplacean physicist and the Martians *can* predict without it, so L1 contradicts the chapter's central thought experiment. | p. 23 | major (L1 stronger than L3) | no |
| D-M2 | L3 (coverage) | Missing: "The perverse claim remains: *all there is* to being a true believer is being a system whose behavior is reliably predictable … *all there is* to really and truly believing that p is being an intentional system for which p occurs as a belief in the best (most predictive) interpretation". Also its turn: this "apparently shallow and instrumentalistic criterion … puts a severe constraint on the internal constitution of a genuine believer, and thus yields a robust version of belief after all". L0 rests on this passage, but L3 never states it. | p. 29 | major (missing key argument) | no; batch had the "perverse claim" bullet |
| D-M3 | L3 belief rule, last sentence | "**A footnote** adds that this is a *derived* rule: if beliefs could be individuated and counted, Dennett estimates that less than ten percent … would be false". Three faults: (a) the ten-percent claim is main text, not a footnote; (b) the hedge "(**which I doubt very much**)" is dropped; (c) "derived rule" refers to the belief rule as a specification of "attribute those beliefs the system *ought to have*" (pp. 19–20), not to the ten-percent estimate. | pp. 19–20 | major (dropped hedge; misplaced claim) | no; batch: "(Dennett doubts this)" |
| D-m1 | L3 opening | "neither … fairly represents any serious theorist" drops "**so baldly stated**" and "exhaustive". | p. 15 | minor | yes (= D4, still present) |
| D-m2 | L3 physical stance; Concepts | "always available *in principle*", stated as fact. Source: "That it will always work in principle is **a dogma of the physical sciences**". | p. 16 | minor | |
| D-m3 | L3 "Who uses it"; Bridges | "**with decreasing confidence**" (birds … clams) and "**loosely**" (lightning) are added. The bridge says "Dennett himself flags [lightning] as a looser, more metaphorical extension". Not in the source. | pp. 21–22 | minor | |
| D-m4 | Intuition note after "Who uses it" | "It works … **precisely because** so many systems … behave *as if* pursuing goals". This explains why the strategy works, which the chapter treats as an open question ("we just do not know"). | p. 33 | minor | |
| D-m5 | L3 Nozick answer | "the Martians would be missing something perfectly objective" drops the condition "**if they did not also see us as intentional systems**". | p. 25 | minor | |
| D-m6 | L3 milder realism | The "bogey … theoretically important … but practically negligible" sentence is main text, but it is presented as footnote 4. | p. 29 | minor | |
| D-m7 | Coverage | Omitted: Oxford colleges example (pp. 21–22, = D5); fn. 1 "it may be urged" theory-ladenness objection (p. 19); arcane beliefs (p. 19); fn. 2 and the Earthling-disguised-as-Martian twist (pp. 27–28); Hayes 1979 (p. 31); "Martians … can aspire to know the regularities" (p. 40). | pp. 19–40 | minor | partly (D5) |
| D-m8 | Whole digest | Quote budget: about 18 quoted spans of Dennett's own words (≥ 4 words). The limit is 10 (rule 13). | — | minor | yes (= N-D3; worse) |
| D-m9 | L2 b8; L3 heading; Reading notes | "1987 postscript" and "original **1981** lecture text". The pages show a lecture given in November **1979** and reprinted in 1981. "1987" is not printed (rule 14). | p. 13 n. | minor | |
| D-m10 | Toy | Quotes the de-interpreted desire as "A should be more **G**". Source: "if it wants the A to be more **F** it should do K". The toy is also a case the design stance already predicts (lectern-like), so it does not show the stance's added power. | p. 30 | minor | |
| D-m11 | Concepts `[[intentionality]]` | "the 'aboutness' of mental states" is a canon gloss, not in this unit, and has no canon-link tag. | p. 15 | minor | |
| D-m12 | L0; L2 b2 | "To be a true believer is just to be…" (p. 15) and "true believers mostly believe truths" (p. 19) are not in L3 (rule 4). | pp. 15, 19 | minor | |
| D-m13 | L3 wording | "**KGB-defection** announcement" (source: announces he is a paid KGB agent, p. 24); "sheltered people are ignorant" (source: "**tend to be**", p. 18); "frames the main source" (source: "**Perhaps** the major source", p. 37). | pp. 18, 24, 37 | minor | |

**Toy:** arithmetic correct; weaker than the batch toy (see D-m10). **Coverage:** complete apart from D-M2 and D-m7. **Usefulness:** good length (1.15×), good inline glosses. But D-C1 inverts who argues what at the chapter's key objection.

---

## 4. Meadows, *Thinking in Systems*, "A note from the editor" (pp. ix–xvi), `ch02-note.md`

**Checked and correct:**
- 1993 draft; "quite unexpectedly" 2001; Limits to Growth 1972 and the quote "are recognized today as the most accurate warnings" (L3); peak oil / 6.6 billion (p. xi).
- "I think so" (pp. xi–xii); reader types; "erupt in their wake"; Pew / National Geographic / Dartmouth; the quote "the outward behavior of often complex systems" (p. xii).
- 1990s event list including the IPCC report (pp. xii–xiii); Herald Tribune week; trends as symptoms; closing quotes (p. xiii); Pirsig quote (p. xv).
- Blank xiv/xvi. Toy arithmetic.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| E-C1 | L3 "The newspaper method" | "she found them there because, **as she writes**, they are 'all around us every day'". The sentence is Wright's ("She found them in the newspaper because they are all around us every day"), not Dana Meadows's. | p. xiii | **critical** (misattributed voice; low impact) |
| E-M1 | Coverage; Reading notes | The unit includes "A note from the author" (pp. ix–x; `units.csv`: "includes ch01-note"). The digest declares it "a separate unit" and does not digest it. Lost: thirty years of MIT System Dynamics work; non-modelling systems thinkers; "only the core of systems theory here, not the leading edge"; "biased and incomplete"; the two purposes. Questions Q3 even cites it. | pp. ix–x | major (missing key content, ~1/3 of the unit) |
| E-M2 | L0; L1; L2 b3; L3 "Why publish now" | Invented causal link: systems thinking is accepted "**because** systems of any size can behave in similar ways", and "**This is why** Wright … chose to publish". Source: the two facts are side by side; the "that is why" refers to "**Dana was writing this book to bring that concept to a wider audience**" (omitted). The hedged claim "understanding those ways is **perhaps our best hope** for making lasting change" is also dropped. | p. xi | major |
| E-m1 | L2 b2; Instances | "**among** the most accurate". Source (and L3): "**the** most accurate warnings". | p. xi | minor |
| E-m2 | L1 | "The note closes with a Pirsig epigraph". The signed note ends on p. xiii ("Diana Wright, 2008"); the epigraph is a separate page (p. xv). | pp. xiii, xv | minor |
| E-m3 | Intuition note, p. xi | "The editor is not saying growth is bad in itself" is an interpretation; the source speaks of "the devastating consequences of physical growth". It also carries a garbled canon tag ("canon link to feedback-driven growth dynamics"). | p. xi | minor |
| E-m4 | Intuition note, p. xiii | Italicised "*may* open up new options" is presented as the source's hedge. Source: "you **will be able to** consider new ways". | p. xiii | minor |
| E-m5 | L3 "Intended readers" | "Editor's claim: … this book can help" drops "**I think**". | p. xii | minor |
| E-m6 | L0; coverage | "**recurring** … problems" is not in the source. The closing hope ("a useful tool in a world that rapidly needs to shift behaviors arising from very complex systems") is omitted. | pp. xi, xiii | minor |
| E-m7 | Reading notes | Trailing empty bullet. | — | minor (format) |

**Length:** 1,923 words for a ~1,550-word source (1.25× the source; 1.92× the target). This is the clearest length failure in the set, and it still omits the author's note. **Toy:** correct. It illustrates the epigraph, not the editor's note.

---

## 5. Popper, *Logic of Scientific Discovery*, Prefaces 1934 / 1959 and Acknowledgments (pp. xv–xxviii), `front-preface-2.md`

**Checked and correct:**
- Schlick and Kant epigraphs quoted exactly; heap of ruins; "begin afresh" (pp. xv–xvi); Acton (p. xvii).
- Allies and opponents; cosmology; "All science is cosmology" (p. xviii).
- Both theses; "the one method of all rational discussion"; overthrow rather than defend; logical analysis not useless (p. xix); historical method and God talking to Himself (p. xx).
- Paradoxes and self-reference "even from Kant's antinomies" (p. xx); new way of ideas/words; Locke's preliminaries; Berkeley/Hume/determinism (p. xxi).
- Approach (1) vs (2); "invisible" (p. xxii); the Plato-to-Russell lists; Berkeley exception; self-mutilation (p. xxii); convention; Thales to Einstein (p. xxiii).
- Goats/sheep; the three model languages and their defects; "cannot both be upheld"; "heap of observation statements" (pp. xxiii–xxv).
- Sheep's ancestors and representatives; microscope (pp. xxv–xxvi); closing quotes; Penn 1958 (p. xxvi); Acknowledgments (p. xxvii).
- **Reading note on the swapped pages:** verified against the images. Excerpt pdf 7 carries header "xxii" and pdf 8 header "xxi"; the sentence breaks confirm the digest's ordering. A good catch.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| P-C1 | L2 b9 | Thanks "Lakatos, Miller, Musgrave, and **Bernays** for corrections to later printings". Bernays is thanked for checking the axiomatization of the probability calculus (appendix *v), not for corrections. L3 has this right. | p. xxvii | **critical** (wrong statement; low impact) |
| P-M1 | L2 b6; L3 "Example" | "the growth-of-knowledge problem transcends common-sense knowledge, because common sense grows **precisely** by turning into science". Source: "**most problems connected with** the growth of our knowledge must necessarily transcend…", since "**the most important way** in which common-sense knowledge grows is, precisely, by turning into scientific knowledge". L2 drops both qualifiers; L3 drops the first. | p. xxii | major (scope qualifiers) |
| P-M2 | L3, throughout | Popper's epistemic hedges are systematically dropped: "**perhaps** the one fact which is generally accepted" (xvi); "**seem to be almost the only** philosophers left" (xviii); "**might be described as** 'the one method'" → "deserves the name" (xix); "it **seems clear** that the growth of scientific knowledge…" (xxii); "**seem to have** lost this admirable optimism" → "have mostly lost" (xxii); "there **seems** to be no such thing as 'the language of science'" (xxiv); "they all **seem to** claim two things" (xxv). Each alone is minor; seven together are a pattern that rule 2 forbids. | pp. xvi–xxv | major (dropped hedges, systematic) |
| P-m1 | L0 | "Popper argues that philosophy's genuine problems are about things, not words". That is Kant's epigraph claim; Popper's own claim is that there is "at least one" genuine problem (cosmology). | pp. xv, xviii | minor |
| P-m2 | L1; L3 | "three short pieces" omits the Acknowledgments. "two historical reasons": the source says "**several** … reasons" and gives "one such reason" and "the main reason". | pp. xx, xxvii | minor |
| P-m3 | L2 b1; L3 1934 | "Schlick fears … his deeper fear". In the epigraph the fear belongs to "**the philosophic connoisseur**". | p. xv | minor |
| P-m4 | L2 b4 | "The one method he **does accept**" implies exclusivity. This conflicts with thesis 1 ("free … to use any method") and with the historical method he recommends (p. xx). | pp. xix–xx | minor |
| P-m5 | L3 1934 | "philosophy can pose genuine problems" drops "**about things**", the link back to Kant. | p. xvi | minor |
| P-m6 | Coverage | Omitted: "I do not care what methods a philosopher … may use so long as he has an interesting problem" (p. xx); "Few of us … practise this precept; but other people … will supply the criticism" (p. xix); "almost all the problems of traditional epistemology are connected with … growth" (p. xxii); model languages "miss the most exciting problems" and have "no bearing on either science or common sense" (p. xxiv); the "recurrent question" echo of Schlick (p. xvi). | pp. xvi–xxiv | minor |
| P-m7 | Intuition note, 1934 | "he is announcing that his whole book will try to show philosophy *can* pose a real problem, by actually posing one". A claim about the book's plan that the page does not make. | p. xvi | minor |
| P-m8 | Toy | Qualitative only: no numbers or arithmetic (rule 9). | — | minor |
| P-m9 | Concepts `[[analysis]]` | "breaking them into clearer parts" is not this unit's characterization, and has no canon-link tag. | pp. xix–xx | minor |
| P-m10 | Frontmatter | `digested_by: claude-sonnet-5`; the other four say `claude-sonnet-5-5`. | — | minor (format) |

**Length:** 2.39× the target, 0.80× the source. It is close to a paraphrase of the 1959 preface.

---

## Verdict on parity

**The Claude Code route is not yet at least as good as the batch route.**

On the three parity units it leaves **4 critical and 17 major** errors (brief rubric), against **0 critical and 8 major** in the original batch audits. At 17 of those 21 spots, the pre-fix batch digest was correct. In fairness, the new route fixed 4 of the 8 batch majors (U-M1, U-M2, G1, N-D1), plus N-D2 and G6. It also lands closer to the length target on Kuhn and Gelman, and its page references are as clean as the batch's (0 wrong references in ~90 checked). The two re-done units add 2 critical and 4 major, and two length failures (1.92×, 2.39×).

**Systematic weaknesses (pattern across units, not noise):**
1. **Hedges and scope qualifiers are lost in L3 itself**, not only in the summaries. Examples: "at least to this point", "in part", "most obviously", "all" (Kuhn); "usually … in practice", "necessarily, for any y" (Gelman); "which I doubt very much" (Dennett); seven "seem/perhaps" hedges (Popper). The batch digests kept every one of the Kuhn/Gelman/Dennett instances.
2. **Voice errors in 3 of 5 units:** Dennett's objector given as Dennett's reply; Gelman "the author calls … empirical Bayes"; Meadows "as she writes". The batch route had the Dennett and Gelman instances right.
3. **Invented connectives ("because", "so", "this is why")** turn juxtaposition into argument: Kuhn K-M4, Meadows E-M2, Gelman G-m4. The batch audits did not report this pattern.
4. **The verifier checks less deeply.** The clearest evidence is Gelman: the CC verifier returned `pass` with 0 critical on its first pass, and a wrong ANOVA cell (G-C1) and a changed condition (G-C2) survived even though the page images were supplied. Both are exactly the kind of check (equation vs image; condition kept) the verifier's h-checks list. In Dennett, D-C1 survived a "repair" pass; Meadows lost a whole included sub-unit without a flag. The engineer's question in `GATE-CC.md` (fewer verifier criticals: "cleaner digests or a shallower verifier?") is answered by this audit: the digests are **not** cleaner, so the verifier is shallower.
5. **Coverage of pivotal sentences:** the Kuhn concession (pp. 102–103), the Dennett "perverse claim" (p. 29) and the Meadows author's note are all missing.

**What would be needed before switching routes:**
- (a) Make the CC verifier output, for every L0–L2 sentence and every L3 sentence containing a hedge, quantifier or connective, the source sentence next to it. The batch verifier's depth suggests it does this implicitly.
- (b) Add a forced image re-read of every numbered equation and table cell. Do not accept `pass` without a per-equation tick list.
- (c) Re-run this gate on the same three units. Parity means at most 0 critical and at most 8 major in total, with no new-only voice error.

Until then, keep the batch route for deep and reference units. Alternatively, use the CC digest pass only with the batch verifier.
