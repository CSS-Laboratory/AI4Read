# Independent audit: wave 3, argumentative prose (Popper ch. 4, Lycan ch. 13, Kahneman ch. 26, Keynes ch. 12, Ashby ch. 10)

Auditor: Claude Opus 5.5. I did not write or verify these digests. Date: 2026-10-14.
Pipeline audited: Sonnet 5.5 digest pass (prompt v2.2) plus independent verifier (v2.2). All five digests are `verified: repaired`.

**Method.** For Popper, Lycan and Kahneman I extracted the text page by page (`pdftotext`) and checked each digest claim against the page it cites. Page mapping: Popper pdf N = printed 56+N; Lycan pdf N = printed 161+N; Kahneman excerpt pdf N = book pdf 269+N (no printed numbers). I checked these images: Popper p. 71 (equations (1)–(3) are correct), Kahneman book pdf 274–277 (Figure 10 axes, the Rabin garble) and all four Ashby spreads. Ashby has text only inside the spread images, so I read all four. Keynes I read in full from the HTML text. In every digest I checked every L0–L2 sentence, every intuition note, and every Concepts and Canonical-instances line. I also checked nearly every L3 bullet, the toy arithmetic, the exercises and the Reading notes. The Reading-notes offsets refer to the parent PDFs, and I did not re-check them.

**Severity scale (from the brief).** *Critical:* a wrong, reversed, strengthened or weakened claim; a claim not in the source; misattributed voice. *Major:* a wrong page reference, a missing key argument, a dropped hedge, three or more undefined terms. *Minor:* wording or format. Hedges follow the wave-2 rule. **Major:** losing the hedge changes a claim's modal status, scope, condition or epistemic status, or the claim is a summary-level central claim. **Minor:** a degree word changes in a side remark.

---

## Summary

| Digest | Claims checked (approx.) | Critical | Major | Minor | Words: digest / source / target | Verifier issues fixed |
|---|---|---|---|---|---|---|
| Popper, *LScD* ch. 4 | 74 | **1** | 3 | 9 | 4,008 / 6,718 / 2,687 (**1.49×**; 0.60× source) | 26 |
| Lycan, *Phil. of Language* ch. 13 | 82 | 0 | 4 | 8 | 5,245 / 9,015 / 3,606 (**1.45×**; 0.58× source) | 20 |
| Kahneman, *TFS* ch. 26 | 61 | 0 | 0 | 10 | 2,861 / 4,037 / 1,615 (**1.77×**; 0.71× source) | 15 |
| Keynes, *GT* ch. 12 | 66 | 0 | 5 | 11 | 3,396 / 5,362 / 2,145 (**1.58×**; 0.63× source) | 12 |
| Ashby, *Intro. Cybernetics* ch. 10 | 52 | 0 | 3 | 6 | 2,446 / 2,913 / 1,602 (**1.53×**; **0.84× source**) | 15 |
| **Total** | **≈335** | **1** | **15** | **44** | | 88 |

**Estimated surviving error rate.**
- Critical errors: 0.2 per digest, which is 0.3 per 100 claims checked (wave 2: 0.6 per digest, 1 per 100). The only critical is in a Toy example, not in L0–L3.
- Errors of any severity: about 18 per 100 claims, the same as wave 2.
- Majors by type:
  - Four are undefined-term majors (P, L, KE, A).
  - Five are lost hedges, scope or conditions in the body (P-M1, P-M2, L-M2, L-M3, KE-M1). Two more are a hedge or condition dropped in a **Concepts line** (KE-M3, A-M2).
  - One is a voice drop (L-M1), one is a strengthened "only so long as" (KE-M2), one is a weakened central claim (KE-M5), and one is a wrong-page cluster (A-M1).
- Page references are good: about 230 checked, one wrong cluster (A-M1, Ashby §10/3 on a spread page) and two incomplete ranges.
- Voice handling is good across the board: the conventionalist objector, Popper's replies, Grice, Davis, the relevance theorists, the reader's objection to Keynes, Rabin. Only one de-attribution survived (L-M1).

**Overall verdict: OK to continue the batch, with hand-fixes.** Fix P-C1 and the 11 majors that are not term or length majors, using the list at the end. The bigger issue is process. **None of the wave-2 patches P-1 (hedge list), P-3 (1.3× length gate) or P-4 (glossary fallback) has reached `prompts/digest.md`, `prompts/verify.md` or `checks.py`.** The length gate still only warns above 1.5×. As a result, all five digests are over 1.3× target, and Ashby is over the 0.8×-source hard cap. All four undefined-term majors are the P-4 pattern, and most hedge majors are P-1 words (*in a sense, in a way, most cases, probably, as a rule*). Deploy P-1, P-3 and P-4 before wave 4.

---

## 1. Popper, *The Logic of Scientific Discovery*, ch. 4 "Falsifiability" (pp. 57–73)

File: `wiki/works/popper-1959-logic/ch04-falsifiability.md`

**Checked and correct.** L0, L1 and L2 bullets 1–3 and 5–8 are correct. The L3 material below is also correct:
- §19: the sources of conventionalism (with Popper's hedge "would seem"); Kant; implicit definition; the clock/rod; Duhem and Cornelius notes; "self-contained and defensible"; Dingler's "ultimate grounds"; the crisis behaviour; simplicity as "classical system of the day".
- The imaginary conventionalist's four routes, correctly voiced.
- §20: Popper concedes the objection and limits it to "cannot be applied immediately". Black's quote; the auxiliary-hypothesis rule as a necessary condition; Pauli; Fitzgerald–Lorentz with footnote *1 (Grünbaum, "degrees of adhocness"); the two kinds of undefined universal names; the experimenter/theoretician rules.
- §21: the three failed attempts with both examples; the definition by two non-empty subclasses; "asserts only the falsity"; footnotes *1 and *2.
- §22: "only if … necessary, but not sufficient"; falsifying hypothesis; white ravens; the two roles of basic statements; Woodger and the regress footnotes.
- §23: occurrence/event definitions; homotypic; the circle diagram; existential statements; contradictions; equations (1)–(3) against the p. 71 image; the "advantage of falsifiers" remark (hedge kept).
- §24: consistency, Nernst, "to a large extent analogous".

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| P-C1 | Toy example, bullet 4 ("It forbids more, so by Popper's rule it is acceptable (p. 62)") | Reverses the rule's logic: the necessary condition becomes a sufficient one. Popper's rule says auxiliary hypotheses are acceptable **only if** they raise falsifiability, and the new system "should then always be judged on the issue of whether it would … constitute a real advance". The toy cites p. 62 for a "therefore acceptable" that Popper never gives. A reader will carry away the wrong rule. L2 b4 and L3 state it correctly. | p. 62: "only those are acceptable whose introduction does not diminish … but … increases it" | **critical** |
| P-M1 | L2 b4 ("harmless singular statements … are an exception"); L3 §20 ("The rule is qualified. Some singular 'auxiliary hypotheses' are harmless"); §20 intuition note ("harmless singular statements excepted") | The scope of Popper's qualification is narrowed. His qualification is general: "we need not reject, as conventionalistic, **every** auxiliary hypothesis that fails to satisfy these standards. **In particular**, there are singular statements…". The singular statements are one example, not the only exception. Also "need not reject" ≠ "acceptable". | p. 63 | major |
| P-M2 | L3 §20, Definitions ("changes in explicit definitions are permissible but count as modifications") | Drops the condition: changes are permissible **if useful**. | p. 63: "Changes in these definitions are permissible if useful; but they must be regarded as modifications" | major |
| P-M3 | Whole digest (reader level, `level: UG`) | These terms are used without a definition: *ostensive definition*, *crucial experiment*, *synthetic*, *Russell's primitive propositions*, *importation*, *modus ponens*, *materially implies*. | pp. 58–60, 67, 71 | major |
| P-m1 | L2 b1 "Conventionalism (Poincaré, Duhem) … (pp. 58–59)" | The names come from note 1 on **p. 57**. | p. 57 n. 1 | minor |
| P-m2 | L3 §19 bullet 3 ("Hence laws are not falsifiable by observation") | This is the conventionalist's view ("According to this conventionalist point of view"), but the bullet states it untagged. Only bullet 1 carries the voice label. | p. 58 | minor |
| P-m3 | L3 §21, footnote *1 | "Both criticisms are **said to be** harmless": Popper says it in his own voice ("they both prove harmless"). The equivalence holds "if used as a criterion of demarcation", and the digest drops that condition. It also omits the note's own point that critics proposed equivalent criteria of *meaning*. | p. 65 n. *1 | minor |
| P-m4 | L3 §22 footnotes | "How often must an effect be reproduced?" is Woodger's question, but the digest leaves it unattributed. "As a rule" is dropped from the tester's means of judging. | p. 67 n. *1 | minor |
| P-m5 | L3 §24 bullet 2 ("actually false statements that give adequate results") | Drops "adequate **for certain purposes**". | p. 72 | minor |
| P-m6 | L2 b8, L3 §23 ("assert 'too little'"); §23 Event ("what is typical"); §19 ("says instead that nature is not simple") | Degree and epistemic hedges are dropped or shifted. Source: "assert, **as it were**, too little"; "what **may be** typical"; "he **does not believe** that nature is simple". | pp. 58, 69, 71 | minor |
| P-m7 | Coverage | Omitted points: §19, "This goal is attainable; for it is possible to interpret any given scientific system as a system of implicit definitions" (this is why conventionalism is defensible); §23, the objection to the word "occurrence" (Keynes, Ancillon) and Popper's choice to keep it; §24, consistency is "the most general requirement … if it is to be of any use at all". | pp. 59, 68, 72 | minor |
| P-m8 | L3 §23, last bullet | The Tarski footnote (p. 68) sits at the end of §23 after the p. 72 material, out of the author's order. | p. 68 n. 1 | minor |
| P-m9 | Toy example, bullet 5 | "Redefining 'on' … would be rejected as conventionalist". Popper allows definitional changes if useful but treats the result as a new system to re-examine. He forbids only *surreptitious* changes of usage. The toy oversimplifies this. | p. 63 | minor |

**Coverage.** Every section 19–24 and every footnote with argumentative content is present. Only the gaps in P-m7 remain.
**Usefulness.** Faithful and well voiced, but 1.49× the target. L3 paraphrases nearly every footnote. The toy is well chosen, apart from P-C1.

---

## 2. Lycan, *Philosophy of Language* (3rd ed.), ch. 13 "Implicative Relations" (pp. 162–180)

File: `wiki/works/lycan-2019-language/ch13-implicative.md`

**Checked and correct.** L0, L1 and all eight L2 bullets are correct. In L3, the following are correct:
- Conveyed meaning: "There's the door", Smedley (1a)/(1b), the foreigner.
- Invited inference (2)–(4).
- CP and M1–M7 as Lycan numbers them.
- Grice's six-step template; the "There's the door" derivation and the psychological-model caveat; the context cues and "common ground".
- The applications to (1), (2), (3) and (4a), with hedges kept (*probably*, *may*).
- Flouting (5) with Grice's "presumably"; metaphor and the p. 34 quote; the two features; notes 2–3.
- Lycan's reply to Strawson (voice correct); the three objections, with Davis's two stages and the Atlas/Levinson intrusive constructions (6)–(7).
- Explicature (8) and Lycan's "tenable arguments on both sides".
- Relevance Theory: core claim, the relevance definition, optimal relevance, loose talk, the simultaneous-processing argument.
- Saturation and Lycan's α comment; free enrichment (9)–(15), with arguments for and against; ad hoc concepts (16)–(20).
- Semantic presupposition: the formal version, note 9, the candidate pairs (21)–(25), and Lycan's verdict on each, including his own hearing of (24).
- Direct Reference; pragmatic presupposition; conventional implicature with Grice's example and note 11 (Lycan's own doubt, correctly voiced); note 12.
- The penalty catalogue, illocutionary implication and the champagne glasses.
- Indirect force (26)–(30); Searle's generalisations and the (27) derivation; the problems; Morgan and Bach/Harnish; Gordon/Lakoff (31)–(35); Millikan notes 8/13.
- The toy (correct, on the main idea) and the exercises (pp. 178).

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| L-M1 | L3 Overview, sentence 2 ("Hearers pick up such implications either by assuming that speakers are cooperative or by noticing that they are deliberately uncooperative…") | Voice dropped. In the source this is **Grice's theory**: "According to Grice's theory … Hearers pick up the implications…". The chapter then reports challenges to exactly this mechanism ("the details of the theory … have been challenged, particularly by relevance theorists"). Here it reads as Lycan's own plain claim. Borderline critical; later sections attribute the view correctly. | p. 162 | major |
| L-M2 | L3 Free enrichment ("it adds explicitly conveyed material not merely implied"); L2 b5 ("adding unmandated explicit content"); Concepts `[[free-enrichment]]` ("explicit enrichment") | Drops the qualifier that Lycan flags as **important**. He writes "there **seems** to be an 'unarticulated' constituent" and "it is explicit **in a way** that conversational implicatures are not". Note 6 adds: "'In a way' is an important qualification … as Bach notes, the examples are hardly ever that [explicit]". The digest states plain explicitness three times and omits note 6. | p. 171 and n. 6 (p. 179) | major |
| L-M3 | L3 Objection 2 ("Gricean reasoning has a negative stage and a positive stage") | Scope quantifier dropped. The source says "**Most cases** of Gricean reasoning divide into two stages". | p. 168 | major |
| L-M4 | Whole digest (reader level, `level: UG`) | These terms are used without a definition: *logical form* (saturation, free enrichment), *Harman's function α*, *Direct Reference Theory*, *Apparent Reference to Nonexistents / Negative Existentials*, *illocutionary*, *preparatory / sincerity condition*. Prerequisites name "speech acts and felicity conditions" but do not gloss them. | pp. 170–176 | major |
| L-m1 | L3 CP ("Its corollaries are the maxims. Lycan's numbering…") | Drops "Here are **a few**". The seven are a selection of Grice's maxims. | p. 165 | minor |
| L-m2 | L2 b5 ("'Henry is ready' — for what?") | The "(for what?)" gloss belongs to "I am too old". "Henry is ready" is listed without a gloss (the digest's L3 is correct). | p. 170 | minor |
| L-m3 | L3 Relevance Theory, bullet 1 ("Sperber and Wilson (1986) and Carston (2002) began by developing Grice") | Lycan: "originally Sperber and Wilson 1986; see especially also Carston 2002". Carston 2002 is not part of the beginning. | p. 169 | minor |
| L-m4 | L3 (19) gloss "[not a sane, compassionate person]" | The source glosses the narrowed or broadened concept: "[a sane, mature, reasonably compassionate person, **including an android**]". The digest drops the broadening half of "loosening and tightening". | p. 172 | minor |
| L-m5 | L3 Penalty table, last row | Lycan offers this row tentatively ("**might** be called 'illocutionary implication'", "we **might** add"). The table presents it as a full row. | p. 175 | minor |
| L-m6 | L3 (21) ("is peculiar but not self-contradictory") | Source: "though **perhaps** peculiar". | p. 173 | minor |
| L-m7 | Coverage | Omitted points: note 7 (Lycan's own objection that (15) is simple quantifier restriction, not free enrichment); "Searle acknowledges the problem" (p. 176); "And he is right about that" (Lycan grants Strawson's premise) and "Grice is in part concerned to eradicate that argument form" (p. 167); "Nor is the point merely psychological" (p. 170). | pp. 167, 170, 176, 179 | minor |
| L-m8 | Reading notes, bullet 2 ("I read them as primes") | Meta-commentary in the first person. | — | minor |

**Coverage.** Complete for the main text, notes and questions, apart from L-m7.
**Usefulness.** Accurate and well tagged; Lycan versus Grice versus the relevance theorists is always clear. But the digest is 5,245 words: 1.45× the target and 0.58× a chapter that is itself a survey. L3 repeats almost every example sentence. The quote budget (rule 13) cannot be checked: 72 quoted spans of four or more words, mostly the numbered example sentences.

---

## 3. Kahneman, *Thinking, Fast and Slow*, ch. 26 "Prospect Theory" (book pdf 270–280)

File: `wiki/works/kahneman-2011-thinking/ch26-prospect.md`

**Checked and correct.** L0, L1 and all eight L2 bullets are correct. In L3, the following are correct:
- The penny-gambles story; psychophysics; Markowitz; theory-induced blindness; the $1,000,500 example; "only in their sign".
- Problems 1–2 ("certainly"/"much more" than 90%); the deferred probability point.
- Problems 3–4: final-wealth equivalence, majority choices, reference points +$1,000/+$2,000; the gift barely noticed; "unless abjectly poor"; the complexity-as-cost criterion.
- The three-bowls demonstration; diminishing sensitivity ($900/$1,000 vs $100/$200); loss aversion and the evolutionary remark; the Figure 10 description (checked against the image: axes ±100/±200, steeper loss side).
- Problem 5 and its System 2/System 1 split; "about $200"; ratio 1.5–2.5; traders ("probably" kept); the self-test ("but not dramatically", "may even be infinite"); the two claims, no contradiction.
- The 250-year blindness; Rabin's two gambles exactly; Rabin–Thaler "ex-hypothesis".
- Textbook omission ("truly necessary", "often irrelevant", "in some contexts"); prospects A/B/C and disappointment; Problems 6–7 and regret; why regret models had less influence; "We were lucky".
- Toy arithmetic: −25, +25 and G = 200; √500 ≈ 22.36, 0.5√1000 ≈ 15.81, −44.72 and −31.62 are all correct. The toy illustrates the main idea.
- Reading notes: the garbles, "pf" and "flow" match the images.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| KA-m1 | L2 b2 "(pdf 272–273)" | "Carriers of value" is on pdf **274**. | pdf 274 | minor |
| KA-m2 | L2 b4; L3 heading "Three features of System 1" | Drops Kahneman's retrospective framing: "**Although Amos and I were not working with the two-systems model** of the mind, **it's clear now** that there are three cognitive features…". The System 1 reading is a later interpretation, not part of the original theory. | pdf 273 | minor |
| KA-m3 | L3 feature 1; Concepts `[[reference-dependence]]` | "**perhaps** the outcome to which you feel entitled" loses its "perhaps". | pdf 273–274 | minor |
| KA-m4 | L1 ("Rabin's theorem shows that utility of wealth cannot explain small-stakes loss aversion") | Faithful to the source ("proved … attempts to explain loss aversion by the utility of wealth are absurd and doomed to fail"). But L3 never states this sentence, so L1 goes beyond L3 (rule 4). | pdf 277 | minor |
| KA-m5 | L3 Rabin–Thaler bullet ("saw this as blasphemy") | Source: "as **little short of** blasphemy". | pdf 278 | minor |
| KA-m6 | Loss-aversion intuition note ("Kahneman's own account is different") | Suggests a conflict between Rabin and Kahneman. In the text they are complementary: Rabin's proof supports Kahneman's point that the utility of wealth cannot explain small-stakes aversion. | pdf 277 | minor |
| KA-m7 | L3 Problems 3–4, last bullet | 29-word verbatim copy without quotation marks ("In science complexity is considered a cost, which must be justified by a sufficiently rich set of new and (preferably) interesting predictions…"). | pdf 273 | minor |
| KA-m8 | Exercises worth doing | The chapter has no numbered exercises. The items do not follow the `Ex. <number> (p. N)` format, and "Problems 3 vs 4 — compute final-wealth outcomes" repeats the text's own computation. | spec | minor |
| KA-m9 | Coverage, Blind spots | Omits *why* prospect theory cannot handle disappointment: it "does not allow the value of an outcome … to change when it is highly unlikely, or when the alternative is very valuable". Also omits Kahneman's verdict that ignoring disappointment is "as obvious a flaw as the counterexamples that I invoked to criticize Bernoulli's theory". | pdf 279 | minor |
| KA-m10 | L3 Loss Aversion bullet 2 | *System 2* is used undefined. The Prerequisites line defines only System 1. | pdf 276 | minor |

**Coverage.** Complete.
**Usefulness.** The most faithful digest in the wave: numbers exact, hedges mostly kept, toy example excellent. But at **1.77× target (0.71× source)** it is close to a paraphrase of an easy, popular chapter. L3 could lose a third of its length without losing any argument.

---

## 4. Keynes, *The General Theory*, ch. 12 "The State of Long-Term Expectation" (HTML, §§ I–VIII)

File: `wiki/works/keynes-1936-general/ch12-state.md`

**Checked and correct.** L0, L2 b2–b9 and the L1 sentences not listed below are correct. In L3, the following are correct:
- §I: the set-up and the two kinds of considerations.
- §II: confidence as part of the MEC schedule (not a second factor), "a priori", the constant-rate assumption.
- §III: "usually very slight and often negligible"; former times ("probable … disappointed"); the new factor; the decisive influence of revaluations; the convention, with "do not really believe" and the equi-probability absurdity; "philosophically speaking"; the reliance chain ending in "fixed for the community … liquid for the individual".
- §V (1)–(5): ice shares and bank holiday; 25/30/20; the fetish of liquidity; Snap/Old Maid/Musical Chairs; the beauty contest and higher degrees ("I believe" kept); the reader's objection and Keynes's four replies, correctly tagged; credit necessary but not sufficient.
- §VI: speculation/enterprise; Wall Street with "if I am right" kept; the casinos and the London costs; the transfer tax limited to the US; marriage and the dilemma; the "only radical cure"; the hoarding writers.
- §VII: animal spirits with "Most, probably" kept; the South Pole; Labour Government/New Deal; the caveat.
- §VIII: the mitigating factors; "great, though not decisive"; "somewhat sceptical"; the State.
- The section-IV note is correct: the HTML has no heading IV.
- Toy arithmetic: 39 and 41 are correct.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| KE-M1 | L2 b1 ("The known present is over-weighted and projected forward (§ II)"); L3 §II ("present facts enter 'disproportionately'") | Drops "**in a sense**" ("enter, in a sense disproportionately"). Keynes presents leaning on confident facts as **reasonable** ("It is reasonable, therefore…"). "Over-weighted" in L2 turns it into a bias. L2 b1 also cites only § II for the known/forecast split, which is in § I. | § II, § I | major |
| KE-M2 | §III intuition note ("compatible with stability **only** so long as it can be relied on") | Adds "only": a sufficient condition ("will be compatible with … stability … so long as we can rely on the maintenance of the convention") becomes a necessary one. This reading fits Keynes's emphasis on precariousness, but the logical form is changed in a summary-level note, which rule 2 forbids. | § III | major |
| KE-M3 | Concepts `[[animal spirits]]` ("drives **most** positive decisions") | Drops "**probably**": the source says "**Most, probably,** of our decisions to do something positive…". L3 keeps the hedge; the Concepts line does not. | § VII | major |
| KE-M4 | Whole digest (reader level, `level: UG`) | These terms are used without a definition: *wage-unit*, *effective demand*, *hoarding*, *actuarial expectation*, *jobber's turn*, *half-crown*, *laissez-faire*. | §§ I, III, V, VI | major |
| KE-M5 | L1 ("the knowledge behind long-term forecasts is **often slight**") | Weakens the chapter's "outstanding fact". Source: "**usually very slight and often negligible**", "**extreme** precariousness". L0 ("very weak") and L2 ("very precarious") are right; L1 understates. | § III | major |
| KE-m1 | L1 ("Keynes suggests a transfer tax might help") | Drops "in the United States" (L2 and L3 keep it). | § VI | minor |
| KE-m2 | L3 §II ("different level of abstraction from the rest of the book") | Source: "from **most** of this book". | § II | minor |
| KE-m3 | L3 §III convention and close | Hedges dropped: "we have tacitly agreed, **as a rule**"; "though it does not, of course, work out quite so simply"; "**no small** part" → "part"; "in an absolute view of things so arbitrary" → "so arbitrary". | § III | minor |
| KE-m4 | L3 §III ("our knowledge gives **no** basis for a calculated mathematical expectation") | Source: "does not provide a **sufficient** basis". § VII does say "the basis … does not exist", so this is a slight strengthening, not a new claim. | § III | minor |
| KE-m5 | Coverage | Omitted points: "When the capital development of a country becomes a by-product of the activities of a casino, the job is likely to be ill-done" (§ VI); the § VII conclusion ("cannot depend on strict mathematical expectation, since the basis … does not exist … our innate urge to activity … makes the wheels go round"); § III "If human nature felt no temptation to take a chance … not much investment merely as a result of cold calculation"; § VI "liquidity … often facilitates, though it sometimes impedes" new investment. | §§ III, VI, VII | minor |
| KE-m6 | Canonical instances `[[farmer-and-barometer]]` | The instance is listed, but L3 never mentions the farmer. | § III | minor |
| KE-m7 | L3 §VII bullets 3–4 | Order reversed. "This means, unfortunately… slumps … exaggerated" follows from the "individual initiative … animal spirits" sentence, but the digest places it before. | § VII | minor |
| KE-m8 | L3 §VIII ("responsibility for organising investment"); buildings bullet | Drops "**directly** organising" (L1 and L2 keep "direct") and "the risk can be **frequently** transferred". | § VIII | minor |
| KE-m9 | L3 §V ("Keynes says that, of the maxims of orthodox finance, none, surely, is more anti-social than the fetish of liquidity") | 16-word verbatim copy without quotation marks. | § V | minor |
| KE-m10 | L3 §V beauty contest ("So each picks what he thinks others will choose. This is the 'third degree'") | Merges the second and third degrees. Keynes separates "what average opinion genuinely thinks the prettiest" from the third degree. The text after the colon is correct. | § V | minor |
| KE-m11 | Reading notes, bullets 1 and 3 | Meta-commentary about the pipeline ("The metadata asked for (pdf N), but no pdf pages were provided"; "I took the intended sense"). | — | minor |

**Coverage.** All sections are present; KE-m5 lists the gaps.
**Usefulness.** Good structure and the best voice handling in the wave. The reader's objection and Keynes's four replies are clearly tagged. But at 1.58× the target, L3 paraphrases most paragraphs. Fixing KE-M1, KE-M2 and KE-M5 matters, because the "reasonable convention vs precarious knowledge" balance is the chapter's point.

---

## 5. Ashby, *An Introduction to Cybernetics*, ch. 10 "Regulation in Biological Systems" (pp. 194–201)

File: `wiki/works/ashby-1956-cybernetics/ch10-regulation.md`

**Checked and correct.** L0, L1 and L2 b1 and b3–b7 are correct. In L3, the following are correct:
- 10/1–10/2: chapter plan, Markovian machine, S.13/10, Cannon, the "chief purpose".
- 10/3: autocatalysis and S.4/23, the unstable "lifeless" equilibrium, elimination (but see A-M1 for the page).
- 10/4: the mouse/cat formalisation, $C(M_1),\dots,C(M_k)$ in the set, "identical" to stability under the always-survives condition, essential variables.
- 10/5: gene-patterns, *Testudo*/*Homo*, $D\to F\to E$, burrow, η/not-η, the three examples, the selection summary.
- 10/6: the two characteristics; η has less variety; "an essential function … block"; Fig. 10/6/1 checked against the image (A wanders, B flat); pilot, air-conditioner, hunter/provider; the italic conclusion.
- 10/7: passive/active; the fencer, with information flowing to non-essential variables only.
- Exercises 1–3 and the unnumbered one; the toy (both parts correct and on the main idea).
- Reading notes on "∇" and ",1" (both visible in the image).

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A-M1 | L2 b2 "(p. 197)"; L3 §10/3, all four bullets "(p. 197)"; Concepts `[[autocatalytic property]]` "(p. 197)" | Wrong page. Section 10/3 is wholly on the **left half of spread 2, printed p. 196**. Page 197 starts with 10/4. This is the spread-labelling pattern: the left-half label was not used. | spread image 2: p. 196 (left) holds 10/3 | major |
| A-M2 | Concepts `[[stability]]` ("Survival is identical to this") | Drops the condition. Ashby: "If now a particular mouse is very skilled and **always** survives … this **representation** of survival is identical with that of the 'stability' of a set". A single survival only means $C(M_i)$ lands in the set. L1 and L2 b3 keep "always survives"; the Concepts line does not. | p. 197 | major |
| A-M3 | Whole digest (reader level, `level: HS`) | These terms are used without a definition: *Markovian machine*, *equilibrium* / *unstable equilibrium*, *trajectory*, *vegetative*, *yaw/pitch/roll*. Rule 8 is strict for an HS-level digest. | pp. 195–199 | major |
| A-m1 | L3 §10/5 bullet 1 ("those that make an individual carrying the pattern well protected") | Garbled. Ashby says the individual "carries the gene-pattern well protected **within itself**", so it is the pattern that is protected. | p. 198 | minor |
| A-m2 | L3 §10/7 ("Higher organisms mostly use this") | Source: "This is the defence used mostly by the higher organisms", i.e. its users are mainly higher organisms. The digest's reading reverses the quantifier. The source is mildly ambiguous. | p. 201 | minor |
| A-m3 | §10/3 intuition note ("almost every feature of it bears the marks…") | Source: "the features of **almost every form**". The quantifier moves from forms to features. | p. 196 | minor |
| A-m4 | Coverage, §10/6 and §10/7 | Omits Ashby's framing of information-blocking as a **thesis to be tested** ("Since this characteristic also implies that the regulator's function is to block the flow of information, let us look at the thesis more closely to see whether it is reasonable"). Also omits that the shell "reduces a variety of impacts, blows, bites … to a negligible disturbance", which is the variety link for the passive case. | pp. 199, 201 | minor |
| A-m5 | Concepts `[[regulator-between-D-and-E]]` ("whose function is to block variety") | Source: "**an essential** function of F". | p. 199 | minor |
| A-m6 | Concepts `[[homeostasis]]` ("maintenance of essential variables within limits") | Ashby uses "homeostatic" without defining it on these pages. The definition is inferred, not marked "(canon link; not stated in this unit)". | p. 196 | minor |

**Coverage.** Complete.
**Usefulness.** Clear and correct, and the toy is good. But the digest is **0.84× the source**, over the wave-2 hard cap of 0.8× source. An 8-page chapter that is itself mostly motivation does not need 2,400 words.

---

## Error patterns across the five digests

1. **Wave-2 patches were not deployed.** `prompts/digest.md` and `prompts/verify.md` still lack the P-1 scope/degree hedge words. `checks.py` still warns only above 1.5× target (P-3 wanted a compression pass above 1.3× and a hard fail above 0.8× source). No digest has the P-4 glossary line. Each of these gaps produced errors here:
   - Hedge majors KE-M1 (*in a sense*), L-M2 (*in a way, seems*), L-M3 (*most cases*) and KE-M3 (*probably*) are P-1 words.
   - All four undefined-term majors are P-4.
   - All five digests are 1.45–1.77× target, and Ashby is 0.84× source.
2. **Concepts lines drop conditions and hedges that L3 keeps** (A-M2, KE-M3, L-M2 partly, A-m5, KA-m3). The verifier's index pass exists, but it compares the line with L3 loosely. It should quote the source sentence.
3. **Toy examples are not checked for claims about the author's rules.** P-C1 cites a page for a "therefore acceptable" that reverses Popper's only-if. The toy is "ours", but sentences in it that say "by Popper's rule…" are claims about the source.
4. **Spread pages.** A-M1 is the first wrong-page cluster in two waves. It comes from a two-page spread where the left half holds a whole section.
5. **Strengths.** Voice tagging is excellent; L-M1 is the only de-attribution. Numbers are exact in all five, including Kahneman's gambles and Keynes's 25/30/20, and the toy arithmetic is all correct. L0–L2 have no invented facts. One critical in ≈335 claims is the lowest rate so far.

## Prompt and pipeline improvements

- **Deploy wave-2 P-1, P-3 and P-4 now**, as written in `wave2-argumentative.md`. Add *in a way, seems, most cases, as a rule, no small part, in an absolute view, perhaps* to the P-1 list.
- **P-6 (verifier, mandatory items): toy-example rule sentences.** Treat every Toy-example sentence that names the author or cites a page ("by X's rule", "(p. N)") as a strength item. Check it against the source sentence; *only if* must not become *so*.
- **P-7 (verifier, index items): quote the source for Concepts and Instances lines.** Require the verifier to quote the source definition and list its conditions and qualifiers (*always, an essential, probably*) before it accepts a Concepts line.
- **P-8 (pages.py / prompt rule 5): spread halves.** When a spread has one half that is blank or holds a whole section, the prompt should repeat both half-labels at the section start. The verifier should check that the first page reference after each section heading matches the half-page where that heading appears.

## Hand fixes needed now (before posts reuse these)

- **P-C1 (Popper, toy bullet 4):** "Then $t \wedge h$ forbids (on,off) and (off,on): 2 statements instead of 1. It forbids more, so it passes Popper's necessary condition. Whether to adopt it still depends on whether the new system is a real advance (p. 62)."
- **P-M1:** L2 b4 → "…; Popper adds that not every auxiliary hypothesis failing this standard must be rejected as conventionalist, e.g. harmless singular statements (pp. 62–63)." Make the matching change in L3 and the intuition note.
- **P-M2:** "changes in explicit definitions are permissible if useful, but count as modifications…"
- **L-M1:** "According to Grice's theory, hearers pick up such implications either by assuming… (p. 162)."
- **L-M2:** Free enrichment → "…adds material that is, in a way, explicitly conveyed; there seems to be an 'unarticulated' constituent. Lycan stresses 'in a way': as Bach notes, the examples are hardly ever explicit (n. 6, p. 179)." Make the matching change in L2 b5 and the Concepts line.
- **L-M3:** "Most cases of Gricean reasoning have a negative stage and a positive stage."
- **KE-M1:** L2 b1 → "…The present facts enter, in a sense disproportionately, because it is reasonable to rely on what we feel somewhat confident about (§§ I–II)." In L3, add "in a sense".
- **KE-M2:** Intuition note → "…It is compatible with considerable stability so long as it can be relied on."
- **KE-M3:** `[[animal spirits]]` → "…that probably drives most positive decisions…"
- **KE-M5:** L1 → "…the knowledge behind long-term forecasts is usually very slight and often negligible…" Re-count L1 (currently 112 words).
- **A-M1:** Change every §10/3 reference, the L2 b2 reference and the `[[autocatalytic property]]` reference from p. 197 to p. 196.
- **A-M2:** `[[stability]]` → "…For a mouse that always survives C, the representation of survival is identical to the stability of the set (p. 197)."
- **Term majors (P-M3, L-M4, KE-M4, A-M3):** Add a `**Glossary:**` line under Prerequisites (P-4).
