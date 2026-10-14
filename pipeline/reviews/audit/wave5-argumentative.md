# Independent audit: wave 5, argumentative prose (Arrow ch. IV, Tractatus prop. 4, Hall 1973)

Auditor: Claude Opus 5.5. I did not write or verify these digests. Date: 2026-10-15.
Pipeline audited: Sonnet 5.5 digest pass (prompt v2.2) plus independent verifier (v2.2). All three digests are `verified: repaired` (verifier issues fixed: Arrow 16, Tractatus 21, Hall 18).

**Method.**
- **Arrow** (scan, no text layer). I read all 12 page images (printed 34–45 = book pdf 45–56, so the digest's "printed = pdf − 11" is right). I checked every definition, equation (1)–(9), property of *C*, the Kaldor and Scitovsky statements, and every number of the p. 44–45 example symbol by symbol. I re-ran the example by hand (x→y: 2.4+1.6 = 4, .7+1.3 = 2; y→z: 2.1+1.4 = 3.5, 1.0+1.4 = 2.4; x vs z: .9+1.2 = 2.1 > 2) and re-checked the ranks against both preference lists.
- **Tractatus.** I extracted the text with `pdftotext` and checked every proposition from 3.344 to 4.5 against it. I checked the images of pp. 47, 50, 51 and 52 (§4.1252 series, §§4.27/4.42 formulas, §4.31 schemata, §4.442 schema and row notation). Printed = extract pdf + 37.
- **Hall.** I extracted the text and mapped each page from its typed "-N-" header (printed = pdf − 1; p. 1 = pdf 2, unnumbered). I checked page images for pdf 1–4, the p. 7 film list and the p. 19 signature date (enlarged crops of title page and p. 19).
- I recomputed all toy arithmetic and ran a 12-gram verbatim-overlap scan of the Tractatus and Hall digests against their sources. Arrow has no text layer, so I could not scan it.
- In every digest I checked against the source sentence: every L0–L2 sentence, every intuition note, every Concepts and Canonical-instances line, every page or § reference, and nearly every L3 sentence.

**Severity scale (from the brief).** *Critical:* a wrong, reversed, strengthened or weakened claim; a claim not in the source; misattributed voice; a wrong formal statement. *Major:* a wrong reference; a missing key argument; a dropped hedge; three or more undefined terms. *Minor:* wording or format. As in waves 3–4, three rules apply. A hedge loss is major when it changes the modal or epistemic status of a summary-level claim, and minor for degree words in side remarks. An added "only" is major when context partly supports it. A Concepts line that drops the condition of a defined term is major.

---

## Summary

| Digest | Claims checked (approx.) | Critical | Major | Minor | Coverage | Words: digest / source / target | Verifier issues fixed |
|---|---|---|---|---|---|---|---|
| Arrow, *Social Choice* ch. IV | 78 | 0 | **4** | 9 | complete; one key reservation missing (A-M1) | 3,209 / ≈5,400 (scan est.) / 2,268 (**1.41×**) | 16 |
| Wittgenstein, *Tractatus* 3.344–4.5 | 115 | **1** | 0 | 14 | complete at section level; 6 small propositions skipped | 4,178 / ≈5,430 / 1,652 (**2.53×**; **0.77× source**) | 21 |
| Hall, "Encoding and Decoding" (1973) | 96 | 0 | **2** | 8 | complete | 4,399 / ≈8,090 / 2,429 (**1.81×**; 0.54× source) | 18 |
| **Total** | **≈289** | **1** | **6** | **31** | | | 55 |

**Estimated surviving error rate.**
- Critical: **1 in ≈289 claims** (wave 4: 0 in ≈418; wave 3: 1 in ≈335). The one critical is a notation error copied from a garbled text layer on a page with no image (T-C1).
- Errors of any severity: about 13 per 100 claims (wave 4: 14).
- Majors by type:
  - Undefined terms: 2 (A-M4, H-M2). The P-4 glossary line has still not been deployed.
  - Summary or Concepts line strengthened or condition dropped: 2 (H-M1 in L0, A-M3 in Concepts).
  - Author's reservation dropped from a summary-level claim: 1 (A-M1, Arrow's fn. 14).
  - Added "only": 1 (A-M2).
- **Formal content is excellent.** Arrow's equations (1)–(9), Definitions 7–8, the *C* properties, the Kaldor and Scitovsky statements and the whole numerical example all match the scan symbol by symbol. The Tractatus $K_n$/$L_n$ formulas and the §4.31 schemata match the images. The only formal error is T-C1.
- **Page and § references.** About 160 were checked; all but three are right. The exceptions are two minor range slips in the Tractatus (T-m8) and Hall's unnumbered p. 1 (H-m5).
- **Voice handling is good.**
  - Arrow is kept apart from Kaldor, Hicks, Baumol, Scitovsky and Samuelson. The one slip is that a Baumol point is reported in Arrow's voice (A-m4).
  - The Tractatus "diagnosed error" (§4.061) is tagged. Frege and Russell are kept as targets. The §4.062 and §4.243 questions are kept with their answers. One rhetorical question is mishandled (T-m2).
  - Hall is kept apart from Gerbner, Himmelweit, Burgelin, Eco, Barthes, Terni and Warshow. His "speculatively", "tentative view" and "suspect" survive in L3.

**Length (the main process problem this wave).** All three digests fail the 1.3× gate, and they fail by more than in wave 4:
- Arrow is at 1.41×.
- Hall is at 1.81×.
- The Tractatus is at **2.53× target and 0.77× source**. Its L3 retells almost every proposition in order, and 536 words of it sit in unquoted 12-gram verbatim spans (T-m13). It is close to a second copy of the source. Aphoristic texts need their own compression rule (see the end of this report).

**Overall verdict: OK to continue the batch with hand-fixes.**
- Fix T-C1 and the six majors now. Five of them are one-line edits; A-M4 and H-M2 each need a Glossary line.
- The Tractatus digest should also be compressed by hand or regenerated before posts are built on it.
- Two process issues recur:
  - Pages with schemata or tables did not get images (T-C1, T-m10).
  - The length gate still only warns.

---

## 1. Arrow, *Social Choice and Individual Values* (1951), ch. IV "The Compensation Principle" (pp. 34–45)

File: `wiki/works/arrow-1951-socialchoice/ch04-iv.md`

**Checked and correct.**
- L0; L1, except A-m3; L2 b1, b2 and b6.
- **§1, the dictum (p. 34):** "if the compensations are made" kept; "not debatable except perhaps…"; the "roundabout" restatement; Bergson.
- **§1, the formal part (pp. 34–35):** (1)–(5) with their sources (Lemma 1(a), Axiom II); Definition 7 and the incomparability remark; the link to *R* (xQy ⇒ xRy but not xPy, with the $xI_iy$ example; xQy and not yQx ⇒ xPy via Lemma 1(e)); Definition 8 (a)–(d) exactly as printed.
- **§1, the critique (pp. 36–37):** "not deducible … but would be … if Condition 2 were slightly modified"; the maximal alternatives and *C(S)*; "possibly a useful preliminary"; Buridan's ass in L3; the Chapter VI forward reference with "somewhat qualified"; the production-side exception.
- **§2, Kaldor and Baumol (pp. 38–39):** the Kaldor rule with "even if … not actually paid"; Kaldor "does not contend" ethical optimality; both Baumol objections; "seems to be somewhat vague"; "assuming that the last proviso makes any sense"; the Modigliani fraction rule and the Bernoulli parallel; the production/distribution objection.
- **§2, total output (p. 40):** "usually" kept in the standard-of-value sentence; "it would appear" kept; the Baumol "measuring rod" quote correctly attributed.
- **§2, formal treatment (pp. 40–41):** Kaldor as $x'Cx,\ x'Qy,\ \neg yQx'$; the Condition 3 violation; *C* properties (1)–(3) and their three reasons ($0$, $-c_i$, $c_i+c_i'$); the equivalence classes; fn. 13 summarised correctly.
- **§2, Scitovsky (pp. 42–44):** the Condition 1 failure with the fn. 16 proof; the Scitovsky "if and only if" with (4)–(5); (6) with "as will usually be the case" and fn. 17; (7)–(9) and the three-case transitivity proof; the double test; the tariff example; Lemma 1(d)/Def. 2.
- **The three-state example:** table, both preference lists, the .9/1.2 floors, all redistributions, and the conclusion "not transitive … not satisfying Condition 1" are exact.
- **Closing points (p. 45):** "suggests strongly" in L3; the status-quo disclaimer; the ethical vs consistency distinction.
- **Concepts** (except A-M3), the tariff and three-state instances, bridges, questions.
- **Reading notes:** the offset and the Def. 8(c) stray mark, which is confirmed in the image.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A-M1 | L2 b5 ("Restricting Condition 3 to admissible alternatives … **repairs this**"); L3 "Kaldor–Hicks spirit" ¶ | Arrow's reservation is dropped. He grants the restricted reading only for argument's sake. Fn. 14: "Of course, the reasoning underlying Condition 3 would be equally applicable to alternatives which are not desired to be ranked; … certainly we would wish that choice to be independent of tastes for alternatives which are not even regarded as admissible. **We are simply waiving the issue here** to get on with other matters." The digest presents the restriction as a fix. Arrow presents it as a concession he does not endorse. This is a summary-level claim, and the reservation is nowhere in the digest. | p. 42 and fn. 14 (image) | major |
| A-M2 | L3 "Further objections": "**Only** in a one-commodity world does the ambiguity vanish" | Adds "only". Source: "In a one-commodity world, i.e., one consumers' good and no labor, **of course**, the ambiguity disappears." The preceding sentence says the standard of value "**usually**" depends on distribution, so Arrow does not claim a one-commodity world is the only escape. "In other words, there is no meaning to total output independent of distribution" gives the "only" partial support, so this is major under the wave-3 rule, not critical. | p. 40 | major |
| A-M3 | Concepts `[[compensation-principle]]` ("rule that x is socially better if compensations **could** make everyone … (pp. 34, 38)") | The condition of the p. 34 sense is dropped, and the chapter's organising distinction is collapsed. Arrow: the term "has been used to denote **two different, though related, methods**". In the p. 34 version, x is preferred "*if the compensations are made*". Only the p. 38 (Kaldor) version uses "could". The line gives the Kaldor sense and cites the page of the other sense. | pp. 34, 38 | major |
| A-M4 | Whole digest (rule 8; reader starts at HS level) | These terms are used without a definition: *marginal rate of substitution* (p. 37); *marginal utility of (real) income* (p. 39, three uses, and the basis of the Bernoulli parallel); *utility indicators* (p. 39); *summation-of-utilities criterion* (p. 39); *optimum conditions on the production side* (p. 37); *Bergson's Fundamental Value Propositions of Individual Preference* (p. 34). The Prerequisites line covers only orderings and indifference curves. | pp. 34–39 | major |
| A-m1 | L2 b3 ("Arrow doubts that maximal-state analysis helps **even for** consumer-choice questions") | Source: "doubt that any study of maximal alternatives will actually be useful in studying **those aspects** of social choice which are directly related to consumer's (and worker's) choice". "Even" adds an a-fortiori reading that is not there. L3 never states the doubt itself; it says only "Arrow goes beyond Samuelson" (rule 4). | p. 37 | minor |
| A-m2 | L2 b7 ("Unaccomplished redistributions also **seem** irrelevant") | Weakens "This **suggests strongly** that unaccomplished redistributions are irrelevant". L3 keeps "suggests strongly". | p. 45 | minor |
| A-m3 | L1 ("Scitovsky's repair gives a weak ordering for two alternatives"; "which **leaves** some pairs … incomparable") | (a) Drops the condition: the two-alternative result needs assumption (6), which L2 b6 keeps. (b) Source: "there **may** be other pairs that are not comparable". | pp. 35, 43 | minor |
| A-m4 | L3 Baumol objection (1) and reply to (2) | (a) Objection (1) is cut to "compensations are measured in money". It drops the point Arrow's reply answers: "the social value of a unit of money is therefore reckoned to be the same in the hands of a rich man as in the hands of a poor man". (b) The reply to (2) reports "'better off' may also depend on others' consumption" in Arrow's voice. It drops "This is especially so if…" and "**as Baumol himself observes** in a footnote". | p. 38 | minor |
| A-m5 | L2 b4 ("has an arbitrary utility rule behind it"); L3 reply to (1) ("This is arbitrary") | Source: "arbitrary **in the sense that** some other rule of choosing utility indicators could have been chosen". Arrow also says the principle is "one of an infinite class, all of which have about the same degree of 'reasonableness'". The flat "arbitrary" reads as a stronger charge. | p. 39 | minor |
| A-m6 | Instance `[[buridans-ass-welfare]]` ("many maximal states, no way to choose among them") | Misplaced. Arrow attaches Buridan's ass to the **nonmaximal** case: "even if the current social state is known to be nonmaximal, so that several other alternatives are known to be better than it, there is no way of knowing which … to change to, **so that** the community will find itself in much the same position as Buridan's ass". L3 gets this right. | p. 37 | minor |
| A-m7 | Coverage | These points are omitted: (a) the motive Arrow attacks, that maximal-alternative work "has been encouraged by the idea that these results are independent of any but the most indisputable value judgments" (p. 36); (b) "a study of maximal social states can be made on other than individualistic assumptions. But clearly it is necessary first to study the assumptions on individual orderings…" (p. 37); (c) fn. 4: maximal alternatives "are precisely those states which would be achieved if each individual acted rationally and selfishly in the presence of prices taken as parameters" (p. 36); (d) "I believe this restatement will carry out the meaning of Kaldor and Hicks", and that the other members of a class "exist only for the purpose of calculation" (pp. 40, 42); (e) the paragraph showing that Scitovsky's argument applies "even if there are only two admissible alternatives" (p. 42). | pp. 36–42 | minor |
| A-m8 | Intuition notes | There are only two (§1 and the three-state example). There is none for the *C*-equivalence/admissible restatement or for the two-alternative weak-ordering result (rule 8: one per major result). | pp. 41–43 | minor |
| A-m9 | Toy example | The arithmetic is correct. But x and y have identical totals (3, 3), so $xCy$: they lie in **one compensatory-equivalent class**, and under Arrow's restatement only one of them would be admissible. The toy therefore illustrates exactly the case that Arrow's restriction removes, and the reader is not told this. It also never reaches the chapter's main result, intransitive Scitovsky indifference with three states. | pp. 41–45 | minor |

**Coverage.**

| Section / key argument | In L3? |
|---|---|
| §1 dictum; roundabout restatement; Bergson | yes |
| Q, (1)–(5), Def. 7, Def. 8; compatibility; not deducible without modifying Cond. 2 | yes |
| Maximal alternatives; new welfare economics; Buridan; Samuelson; Ch. VI impossibility; production-side exception | yes ("indisputable value judgments" motive missing, minor) |
| §2 Kaldor rule; Baumol (1)(2); Arrow's replies; Modigliani/Bernoulli | yes (objection (1) truncated, minor) |
| Production vs distribution; standard of value; measuring rod | yes ("only" added, A-M2) |
| C relation; Cond. 3 violation; (1)–(3); equivalence classes; fn. 13; admissible alternatives | yes |
| — fn. 14 reservation ("simply waiving the issue") | **no (A-M1)** |
| Cond. 1 failure; Scitovsky (4)–(9); double test; tariffs; three-state example | yes |
| Unaccomplished redistributions; status-quo disclaimer; two kinds of objection | yes |

**Usefulness.** This is a strong digest of a scan-only chapter: every formal object is exact. The fixes that matter are A-M1 and A-M3, because posts will reuse the Concepts line and the "Condition 3 repaired" claim. Length is 1.41× target; L3 is complete and does not pad much.

---

## 2. Wittgenstein, *Tractatus* (Ogden tr., Gutenberg PDF), 3.344–4.5 (pp. 38–54)

File: `wiki/works/wittgenstein-1922-tractatus/ch04-proposition.md`

**Checked and correct.**
- L0; L1, except T-m1; L2 b1–b3 and b5–b8.
- **3.344–3.5:** all present and correct.
- **4–4.0031:** clothes and body; "not false but senseless"; Good/Beautiful; Mauthner; Russell.
- **4.01–4.016:** score, phonetic spelling, aRb, ♯/♭, gramophone, law of projection, similes, hieroglyphs.
- **4.02–4.031:** Yes/No; external vs internal properties; scaffolding; understand without knowing truth; translation of constituents; "new sense with old words"; "only … in so far as it is a picture"; the experiment quote.
- **4.0311–4.0412:** living picture; "My fundamental thought" voiced; *ambulo*; multiplicity; the three failed notations; spatial spectacles.
- **4.05–4.0641:**
  - §4.061 correctly tagged as a diagnosed error, not Wittgenstein's view.
  - §4.062: the question is kept and answered "No".
  - §4.0621 ∼∼p = p; the black-spot simile with its breakdown and the anti-Frege verb point; §4.064–4.0641.
- **4.1–4.116:** natural science; above/below; activity; psychology; Darwin; limits of the thinkable; "mean the unspeakable".
- **4.12–4.128:** outside logic/world; mirrors; fa/ga; "What can be shown cannot be said"; internal property and the blues; "as senseless to ascribe … as to deny"; "disappears"; formal series; formal concepts; pseudo-concept "object"; "There are objects"; 100 objects; Frege/Russell "as Frege and Russell thought"; §4.12721; vicious circle; §4.1274; anumerical.
- **4.2–4.28:** all present; §4.243's question kept and answered by the English/German example; "This will be shown later" kept.
- **$K_n$ and $L_n$:** both match the p. 50–51 images symbol by symbol.
- **4.3–4.45:** the §4.31 schemata (image); §4.411 "It seems probable even at first sight" and "palpably" kept; §4.431 Frege "quite rightly … Only … false"; no logical objects; ⊢ meaningless.
- **4.46–4.4661:** all correct, including "without sense" vs "not senseless" and the 0-in-arithmetic analogy.
- **Toy:** $K_2 = 4$, $L_2 = 16$, and (TFFF)/(TTTF) under the author's row order TT, FT, TF, FF are all correct. The added steps are marked.
- **Concepts and instances** (except T-m12) carry correct § and page refs.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| T-C1 | L3 §4.442: "Written as a row for p, q it becomes **(TTT)(p,q)**, or more plainly (TTFT)(p,q)" | Wrong formal notation. The image prints "**(TT–T)(p, q)**". The dash fills the third place, the TF row with no T. The digest's sign has three places for four truth-possibilities, so it is ill-formed as a two-variable propositional sign. The "more plainly" gloss then no longer follows from it. Cause: no image was supplied for p. 52, and the text layer dropped the dash (Reading notes bullet 3 says so). | p. 52 image | **critical** |
| T-m1 | L1 ("Because logical form cannot itself be pictured, it can only be shown. **So** philosophical 'propositions' … are senseless, **and philosophy becomes clarification**.") | The inference chain is not in the source or L3. "Philosophy is an activity … logical clarification" is asserted at §4.112, before the showing doctrine (§4.12ff.). The text does not derive it from that doctrine. §4.115 gives the link partial support. Borderline major. | §§4.112, 4.115, 4.12–4.1212 | minor |
| T-m2 | L3 §4.1121 ("Wittgenstein asks whether his study of sign-language does not correspond… (**the question is left unanswered as such**)") | Rule 3. The next sentence ("**Only** they got entangled … and there is an analogous danger for my method") shows the implied answer is *yes, it corresponds*. The digest should state that answer and cite the clue, not call the question open. | pp. 44–45 | minor |
| T-m3 | L3 §4.112 ("Its result is not philosophical propositions but **clear propositions**") | Source: "The result of philosophy is not a number of 'philosophical propositions', but **to make propositions clear**". The digest turns an activity into a product, against the sentence just before ("not a theory but an activity"). It also drops "Philosophy should make clear and delimit sharply the thoughts which otherwise are … opaque and blurred". | p. 44 | minor |
| T-m4 | L2 b4 ("Taking true and false to be two equal relations … **comes from** overlooking…") | Source: "**If** one does not observe … one **can easily** believe…". A conditional, modal diagnosis becomes a causal claim. L3 is exact. | §4.061, p. 43 | minor |
| T-m5 | L3 §4.31 ("T/F schemata **with $K_n$ rows**") | An unmarked inference: the text does not say the schema has $K_n$ rows. It follows from §4.28 but should be marked `(added step)`. | p. 51 | minor |
| T-m6 | L3 §4.241, §4.1272 | Voice and wording. "If I use two signs with one and the same meaning, **I express** this…" (Wittgenstein's stipulation) becomes "If two signs have one and the same meaning, this is expressed…". "They … are **presented in logical symbolism by** variables" becomes "These are variables". | pp. 48, 50 | minor |
| T-m7 | Intuition note after §4.1212 ("A map can show a region, but it cannot also show **the mapping rule**…") | The analogy conflates logical form (what picture and reality share, §4.12) with a rule of projection (§4.0141). It is not in the source, and it points the reader at the wrong notion. | §§4.0141, 4.12 | minor |
| T-m8 | Refs | Block heading "4.05–4.0641 (pp. 43–44)": §4.05 is on p. 42. "§4.45, p. 53": §4.45 begins on p. 52. | pp. 42, 52 | minor |
| T-m9 | Coverage | §4.1213 lies inside the "4.12–4.1213" heading range but is not covered. Also omitted: §4.1221 ("feature"); §4.1241; §4.3; §4.5's definition of the general form ("a description of the propositions of some one sign language, so that every possible sense can be expressed by a symbol which falls under the description…"); §4.464's probability gradation; §4.021's reason ("for I know the state of affairs presented by it, if I understand the proposition"); §4.116's first sentence ("Everything that can be thought at all can be thought clearly"); §4.122's stated purpose (the confusion of internal and external relations); §4.0411's target, $(x).fx$; §4.27's second sentence. | pp. 40–54 | minor |
| T-m10 | Reading notes, bullets 3–5 | (a) The §4.1252 note says the series "could not [be checked] against images". The p. 47 image confirms the book prints "(∃x, y) : aRx . aRy . yRb" in §4.1252, against "aRx . xRy . yRb" in §4.1273. Under rule 14 this should be reported as an edition misprint. (b) First-person meta: "I checked", "I relied on", "I could not check", "I read these words in full". | p. 47 image | minor |
| T-m11 | Questions, bullet 4 ("…such as colour exclusion") | An outside doctrine not in these pages (rule 1 applies to every section). | — | minor |
| T-m12 | Concepts `[[picture theory of meaning]]` | Canon label not used in the unit. It needs "(canon link; not stated in this unit)" (rule 8; same pattern as wave-4 Q-m7). | — | minor |
| T-m13 | Whole L3 (spec: "your own words"; rule 12) | 31 unquoted verbatim spans of ≥ 12 words, 536 words in total. The longest is 37 words (§§4.113–4.115 run together). Others are 28 words (§3.42), 25 (§4.003) and 24 (§4.5, §4.062). With the 2.53× length, L3 is largely the translation re-typed. | 12-gram scan | minor |
| T-m14 | Whole digest | These terms are used without a gloss: *logical syntax* (§3.344), *logical co-ordinates* (§3.41), *propositional variable* (§4.126), *logical product* (§§3.42, 4.465). They are mostly Wittgenstein's own undefined terms, and the Prerequisites line partly covers them. Borderline P-4. | pp. 38–53 | minor |

**Coverage.**

| Block | In L3? |
|---|---|
| 3.344–3.5 (end of Prop. 3) | yes |
| 4–4.0031 thought, language, clothes, critique | yes |
| 4.01–4.016 picture, score, projection | yes |
| 4.02–4.031 shows/says, Yes/No, understanding, new sense | yes |
| 4.0311–4.0412 names, fundamental thought, multiplicity, failed notations | yes |
| 4.05–4.0641 truth, negation, black spot, sense before assertion | yes |
| 4.1–4.116 science, philosophy as activity, limits | yes (§4.112 result garbled, minor) |
| 4.12–4.1213 showing logical form | yes (§4.1213 missing) |
| 4.122–4.128 internal properties, formal concepts, pseudo-concepts | yes |
| 4.2–4.28 elementary propositions, names, identity, $K_n$ | yes |
| 4.3–4.45 truth-possibilities, schemata, $L_n$, Frege, no logical objects | yes (**§4.442 notation wrong, T-C1**) |
| 4.46–4.4661 tautology and contradiction | yes |
| 4.5 (breaks off) | partly (definition clause missing) |

**Usefulness.** The digest is accurate proposition by proposition, and its voice and question handling is mostly careful. But it is not a guide: at 0.77× source it costs nearly as much to read as the Tractatus itself. A reader gets little from it that the numbered text does not already give. Fix T-C1 and compress L3 by about 55% (see the end of this report).

---

## 3. Hall, "Encoding and Decoding in the Television Discourse" (CCCS stencilled paper, 1973; pp. 1–19)

File: `wiki/works/hall-1973-encoding/main.md`

**Checked and correct.**
- L1; L2 b1–b7.
- **Aim (p. 1):** "absolutely pivotal"; "necessarily … systematically distorted communication"; competences.
- **Halloran and the message form (pp. 1–2):** codes and syntagmatic chains; the raw event becoming a "story"; "in dominance"; "relatively autonomous" but determinate; the message-form paragraph.
- **The circuit (pp. 3–4):** production framed by meanings; not a closed system; Elliott; "skewed and structured" feedbacks; "predominant"; differentiated moments; the decoding precondition; the effects framed by structures (p. 4); the diagram; meanings I/II "may not be the same"; (a)/(b).
- **Western and violence (pp. 5–7):**
  - Gerbner's "messages about violence"; Himmelweit and "boys rather earlier than girls"; "hypothesised"; reciprocity of codes = genre.
  - The test case; the deep-structure list; the ten surface variants; *Hud* (Cadillac, Oldsmobile truck); "reversal of a limited number of lexical items".
- **Burgelin, polysemy and the quick draw (pp. 7–10):**
  - "Arbitrary"; "not to say that violence was not an element"; Burgelin quoted and voiced; the marked/unmarked rules including the proviso about back-shooting.
  - (a)(b)(c); "polysemic"; closure; dominant-to-subordinate scale; "no law to ensure".
  - Quick draw "behavioural"/"instrumental"; "research suggests"; "appear to have the effect"; Berger & Luckmann, Turner, Freud; "speculatively"; Warshow; the p. 10 table.
- **Signs and connotation (pp. 11–13):**
  - The Eco quote; the iconic sign (Peirce, Eco "convincingly argued").
  - "probably give rise to less misunderstandings"; unequal linguistic competence "(predominantly, by the family and the education system)"; the spectrum caveat.
  - /sweater/ with its four connotations; "maps of meaning"; Barthes' "if you like … fragments of ideology"; polysemy ≠ pluralism; "neither univocal nor uncontested"; "dominant, not determined".
- **Preferred readings and selective perception (pp. 14–15):** preferred mappings; denotative vs connotative clarification; logics-in-use; Chile; Terni and Hall's "only quarrel"; "kinks in the communicative chain"; the three possible reasons; "what they really mean"; "own tentative view"; Eco's sub-cultural level.
- **The typology (pp. 16–18):**
  - Gramsci/Parkin with "ideal-type"; noise; "societal, not communicative".
  - Dominant "full and straight … for all practical purposes".
  - Professional "relatively independent", bracketing, NI/Chile/IRB, "It may even be said", "behind men's backs".
  - Negotiated "probably"; hegemony (a)/(b); situated logics; the worker example; "We suspect that the great majority".
  - Oppositional detotalize/retotalize, with crisis points.
- **Policy (pp. 18–19):** "extremely difficult"; "most partisan acts"; "are, or can be"; deep vs surface; "not a technically neutral, but a political one"; "all too prone"; "professional bracket".
- **Toy:** 1+2+1+1 = 5; 20%, 80% and 60% are correct, and the toy is on the main idea.
- **Concepts** (Habermas = note 23 is correct) and instances (except H-m4).
- **Page refs:** all match the "-N-" page map.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| H-M1 | L0 ("…so that beyond the denotative level, making it more effective **is not a neutral technical task but a political one**") | The digest fuses two sentences and drops the hedge on the more general one. (1) "it is **extremely difficult to identify as a neutral, educational goal**, the task of 'improving communications' … once one has passed beyond the strictly denotative level" (p. 18). (2) The categorical sentence has a narrower subject: "The decision to intervene in order to make **the hegemonic codes of dominant elites** more effective and transparent for the majority audience is not a technically neutral, but a political one" (p. 19). The L0 takes the scope of (1) and the verdict of (2), so the central summary claim is stronger than either. L1 ("hard to call neutral") and L3 are correct. | pp. 18–19 | major |
| H-M2 | Whole digest (rule 8; reader starts at HS level) | These terms are used without a definition: *corporate* (Gramsci's "corporate" formations; "negotiated-corporate decodings"; "more corporate positions"); *totalisation / detotalize / retotalize*; *ideological apparatus*; *marked / unmarked*; *deep structure / surface structure*; *sign-vehicle*; *reference-code*; *condensation and displacement*. The Prerequisites line glosses sign, denotation/connotation, polysemy, ideology, message-form and determinate moment, but none of these. | pp. 2, 7–10, 16–18 | major |
| H-m1 | L3 Circuit "Result" ("The lack of fit relates to structural differences… It **also** relates to an asymmetry at the transformation…") | A comparative is lost (rule 2). Source: the lack of fit "has **a great deal** to do with the structural differences between broadcasters and audiences: but also has **something** to do with the a-symmetry … at the moment of transformation". Hall weights the two causes very unequally; the digest makes them parallel. | p. 4 | minor |
| H-m2 | L2 b8 ("Misreading connotative 'misunderstandings' as technical faults is … a type of unconscious collusion") | Object shifted. Hall's "type of unconscious collusion" is misreading "**a political choice** as a technical one", that is, the decision to intervene. Misreading systematic distortions as technical faults is "to misread a deep-structure process for a surface phenomenon". P. 18's "colludes with the re-signification of real conflicts … as if they were simply kinks" gives partial support. L3 is exact. | pp. 18–19 | minor |
| H-m3 | L3 hedges in side remarks | Several hedges are dropped. "Denotation **is** bounded by closed codes": the source says "**may be** bounded" (p. 13). "In advertising almost no communication is 'purely denotative'": drops "**we might say**" (p. 12). "viewers take the image for the thing": the source says "we are **tempted** … to 'misread'" (p. 12). The p. 15 denotative-misunderstanding sentence drops "(if we can make the analytic distinction for the moment)". "through the structure of access": drops "**more intimately**" (p. 17). "violence might be present to warrant the character": drops "It is now perfectly clear" and "**only**" (p. 9). | pp. 9–17 | minor |
| H-m4 | Instance `[[tv-western-violence]]` ("violence as messages about conduct") | Hall's status marker is dropped: "we may **speculatively** formulate an alternative connotative 'reading'"; the message "**would be** understood … as a message about conduct". L3 keeps "speculatively". | p. 10 | minor |
| H-m5 | Reading notes; L3 Western ¶ | (a) "*Left Handed Gun*; **title garbled in the source**": the p. 7 image clearly reads "Left Handed Gun?". Only the text layer is garbled. Hall's own question marks ("Left Handed Gun?", "Butch Cassidy?") are dropped, losing his uncertainty about the examples. (b) "The text layer … reads 'September 1975'; this may be a misprint": an enlarged p. 19 crop shows "1973" in the same typewriter glyph as the title page. This is an OCR artefact, and the image settles it. (c) "The title page (pdf 1) and the notes page … show no printed number": p. 1 (pdf 2) is unnumbered too. (d) "should be checked against the page images" is a process note, not a fact about the pages (rule 14). | pp. 7, 19 images; pdf 2 | minor |
| H-m6 | Coverage | Omitted: "Though the sources of such mystification are both social and structural, the actual process is greatly facilitated **by the operation of discrepant codes**", which ties the paper's two halves together (p. 19). Hall's caveat that how professionals reproduce hegemony "(not without contradiction)" "is a complex matter which cannot be further spelled out here" (p. 17). The negotiated contradictions are "only on certain occasions brought to full visibility" (p. 17). One good act "not only could, but **apparently** had to" change the villain's end (p. 8). "Beginnings and endings have been announced … so we must be cautious" (p. 5). "without being able to take the example very far" (p. 11). The re-translation into societal structures "must be made again for the circuit to be completed" (p. 2). Eco's "logic of cultures" (p. 1). | pp. 1–19 | minor |
| H-m7 | L3 (spec: "your own words") | 15 verbatim spans of ≥ 12 words (237 words). The longest unquoted spans are the 28-word "most partisan acts … kinks in the communicative chain" (p. 18) and the near-verbatim p. 2 "message-form … essential relations of communication, of which it [is] only a part". | 12-gram scan | minor |
| H-m8 | Questions, bullet 3 ("reproduces hegemony **without bias**") | Source: "by **not overtly** biassing their operations in their direction". | p. 17 | minor |

**Coverage.** Complete. Every part of the paper is covered:
- the aim and framework;
- the circuit and diagram;
- the Western (genre, convention, transformations, *Hud*, the Burgelin rules, polysemy, the quick draw and its table, the conclusion);
- the iconic sign;
- denotative competence and its caveats;
- connotation and the /sweater/;
- dominance without determination;
- interpretive work, Chile and Terni;
- selective perception;
- the four positions;
- cultural policy.

The losses are the caveats and the "discrepant codes" link listed in H-m6.

**Usefulness.** Faithful and well voiced. Hall's own epistemic markers ("tentative", "suspect", "speculatively", "probably") all survive in L3, which is what this paper needs. H-M1 matters most for posts, because the L0 line is the one readers will quote. At 1.81× target, L3 keeps near-paraphrase of the p. 1–4 framework that could be halved.

---

## Error patterns across the three digests

1. **Formal transcription is now very good when images are present, and fails when they are not.** Arrow is image-only and has no formal errors. The Tractatus's one critical (T-C1) and its unresolved series misprint (T-m10) both sit on pages that had no image (pp. 47, 52). Hall's misattributed "garbled title" and spurious date discrepancy (H-m5) are also text-layer artefacts that the images settle. This is wave-4 pattern 7 again: image selection misses pages whose decisive content is a schema, a symbol string or a short line.
2. **Summary and Concepts lines still drift from a correct L3.** H-M1 (L0 fuses a hedged and a categorical sentence), A-M3 (a Concepts line drops the defining condition of one of two senses), A-m1, A-m2, T-m4 and H-m2. This is the fourth wave with this pattern; the verifier's summary-vs-source pass is still too loose.
3. **Dropped author reservations, not dropped hedges, are the new major.** In A-M1, Arrow explicitly "waives" an issue in a footnote, and the digest turns his concession into a repair. Footnotes that qualify a body claim need to be read as part of the claim.
4. **Undefined terms: P-4 majors again** (A-M4, H-M2). This is the fifth wave running. A "grad" level label does not protect a digest, because the prompt's reader starts from HS knowledge of the topic.
5. **Length is getting worse, not better** (1.41×, 1.81×, 2.53×; wave 4 median 1.36×). The aphoristic Tractatus is the extreme case: the model treats every numbered proposition as a section to cover (rule 7), so L3 grows to 0.77× source. That rule collides with rule 12 for numbered-remark texts.
6. **Verbatim carry-over** (T-m13, H-m7) rises with length: 536 and 237 words in long 12-gram spans.
7. **First-person meta-commentary in Reading notes** persists (T-m10, H-m5(d)), as in waves 3–4 (P-11 not yet deployed).

## Prompt and pipeline improvements

- **P-10 (pages.py), extended.** Always attach the image of any page whose text layer has any of these:
  - a table or schema: ≥ 3 lines made mostly of single-letter tokens such as T/F;
  - a parenthesised symbol string;
  - an equation number;
  - a quoted formula.

  This would have supplied pp. 47 and 52 of the Tractatus. For typescripts like Hall, attach the signature/date page and any page with underlined titles.
- **Deploy P-4 (Glossary line) now.** Same wording as in the wave-4 report. Apply it regardless of `level`.
- **Rule 7/12 conflict for numbered-remark texts (new, P-12).** Add to rule 7: "For texts made of numbered remarks (Tractatus, *Investigations*, aphorism collections), cover every *block* of remarks, not every remark. Give each block its main claims in your own words and cite the remark numbers. Copy a remark only when it is a famous line, and then quote it." Add a hard regeneration at > 1.6× target, not a warning.
- **P-7 (verifier, quote the source for summaries): add footnotes.** For every L2 bullet that says a condition is "repaired", "satisfied" or "shown", the verifier must check the footnotes on that page for a reservation. That would have caught A-M1. The L0 check should flag any L0 sentence whose verb is stronger than the strongest source sentence it compresses (H-M1).
- **P-9 / rule 14 (misprints):** "Never call a reading 'garbled in the source' or a date 'possibly a misprint' unless the page image shows it. If no image was supplied, write 'text layer garbled; image not checked'."
- **P-11 (first person ban):** still needed.

## Hand fixes needed now (before posts reuse these)

- **T-C1 (Tractatus L3 §4.442):** "Written as a row for p, q it becomes '(TT–T)(p, q)', or more plainly '(TTFT)(p, q)' (§4.442, p. 52)." In Reading notes, replace bullet 3 with: "§4.442 (p. 52): the printed row notation is '(TT–T)(p, q)'; the dash marks the TF row, which has no T." Replace the §4.1252 bullet with: "§4.1252 (p. 47) prints '(∃x, y) : aRx . aRy . yRb'; §4.1273 (p. 48) prints '(∃x, y) : aRx . xRy . yRb'. The second fits the series; the first is a misprint in this edition."
- **A-M1 (Arrow L2 b5 and L3):** add, after "the restricted Kaldor principle satisfies it": "Arrow adds that the reasoning behind Condition 3 would apply equally to nonadmissible alternatives; he is 'simply waiving the issue' to get on (fn. 14, p. 42)." In L2 b5, replace "repairs this" with "satisfies Condition 3 if one waives, as Arrow does for argument's sake, its application to nonadmissible alternatives".
- **A-M2 (Arrow L3):** "In a one-commodity world the ambiguity disappears (p. 40)."
- **A-M3 (Arrow Concepts):** "`[[compensation-principle]]` (new): a name for two related methods. (1) With compensation **paid**: x is preferred to y if, after compensations are made, everyone is at least as well off and someone better off (p. 34); this reduces to unanimity. (2) Kaldor's version: compensation only **possible**, not paid (p. 38)."
- **H-M1 (Hall L0):** "…and Hall argues that communication between broadcasting elites and audiences is necessarily 'systematically distorted'. Beyond the denotative level, 'improving communications' is extremely difficult to call a neutral goal, and making the dominant elites' hegemonic codes more effective is a political, not a technical, choice."
- **A-M4, H-M2:** add a `**Glossary:**` line under Prerequisites with the terms listed in each row (Arrow: MRS, marginal utility of income, utility indicators, summation of utilities, production-side optimum conditions, Bergson's propositions. Hall: corporate, (de/re)totalize, ideological apparatus, marked/unmarked, deep/surface structure, sign-vehicle, reference-code, condensation/displacement).
- **Cheap minors worth doing in the same pass:**
  - T-m2: "(the 'Only…' that follows implies yes: it does correspond)".
  - T-m3: "but to make propositions clear".
  - H-m5: restore "Left Handed Gun?" and "Butch Cassidy?" with Hall's question marks; delete the 1975 bullet.
  - A-m6: move Buridan to the nonmaximal case.
  - T-m8: fix the two page ranges.
- **Tractatus length:** regenerate or hand-compress L3 to about 2,000 words (blocks, not remarks), keeping T-C1's fix and every formula.
