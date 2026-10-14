# Independent audit: wave 1, argumentative prose (Gettier 1963, Godfrey-Smith ch. 5, Carey ch. 1, Apperly & Butterfill 2009 part 1)

Auditor: Claude Opus 5.5. I did not write or verify these digests. Date: 2026-10-14.
Pipeline audited: Sonnet 5.5 digest pass (prompt v2.1) plus independent verifier (v2.1). All four digests are `verified: repaired` (verifier issues: 7 / 13 / 14 / 14).
Method: I read the full source of each unit as text (pdftotext, checked against page breaks), plus the page-1 image for Gettier. I then checked digest claims one by one against the source page. Page mapping: Gettier excerpt page N = printed 120+N. Godfrey-Smith excerpt page N = printed 74+N. Carey excerpt page N = printed 10+N. Apperly printed = excerpt page. The digests' own offsets in Reading notes refer to the parent PDFs, and I did not re-check those. **Every page reference I checked lands on the correct printed page.**

Severity scale (from the brief). **Critical:** wrong, reversed, strengthened or weakened claim; a claim not in the source; misattributed voice. **Major:** wrong page reference, missing key argument, misleading emphasis, three or more undefined terms, or a hard format rule broken. **Minor:** wording or format.

---

## Summary

| Digest | Claims checked | Correct | Minor | Major | Critical | Words (digest / source / target) |
|---|---|---|---|---|---|---|
| Gettier 1963 | 26 | 23 | 3 | 0 | 0 | 1,867 / ~1,000 / 1,200 |
| Godfrey-Smith ch. 5 | 34 | 25 | 6 | 2 | 1 | 2,576 / ~5,000 / 2,131 |
| Carey ch. 1 | 45 | 31 | 10 | 4 | 0 | 4,533 / ~8,000 / 3,308 |
| Apperly & Butterfill p1 | 40 | 29 | 8 | 1 | 2 | 3,277 / ~5,800 / 2,323 |

**Overall verdict: OK to continue the batch, after two small verifier patches (P-1, P-2 below) and hand fixes to the three critical lines listed here.** At the level of "what the page says", the digests are faithful: 108 of 145 checked claims are fully correct, there are no page errors, and there are no invented facts in L2 or L3. Every surviving critical error is one of the types the prompt already names: a summary line drifting from a correct L3, a necessary/sufficient flip, and a conflated voice. The verifier does not check for these line by line. Two of the three criticals sit in L1 while L3 has the same point right, so a mechanical L1↔L3 entailment check would have caught them. Carey also shows a separate, systematic problem: quote density and undefined terms (P-3).

---

## 1. Gettier 1963, "Is Justified True Belief Knowledge?"

File: `wiki/works/gettier-1963-jtb/main.md`

### A. Faithfulness: 26 claims checked (L0 1, L1 6, L2 7, L3 9, Concepts/Notes 3)
Correct: 23. Minor: 3. Major: 0. Critical: 0.

Checked and correct: the (a)/(b)/(c) analyses and their attributions, with footnote sources (p. 121); the thesis that the conditions fail as *sufficient* (italic in the source) and the substitution clause for (b) and (c) (p. 121); both preliminary points, word for word in substance (p. 121); the Plato footnote, *Meno* 98 (confirmed in the page image); Case I evidence, the (d)→(e) entailment, "clearly justified", the reason Smith does not know (p. 122); Case II evidence, (g)/(h)/(i), "completely justified", the rented car, "sheerest coincidence" (pp. 122–123); the conclusion "with appropriate changes" (p. 123); L2's "does not argue that any condition is unnecessary"; the epistemic-luck concept, correctly flagged as "our label, not Gettier's"; the Reading note on the Achinstein article that follows on p. 123.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| G1 | L1, last sentence | "This matters because, if Gettier is right, these conditions do not add up to knowledge" is circular. It gives no reason why the result matters. | — | minor |
| G2 | Concepts | `[[justified true belief (JTB)]]` uses the canon display name, with spaces and parentheses, as an id. The other digests use slugs. | — | minor |
| G3 | Reading notes | "The unit metadata suggested (pdf N) references" is pipeline meta-commentary, not a reading note. | — | minor |

### B. Toy example
Correct, and the arithmetic of "false or true = true" is right. But it is a near-copy of Case II with new names, so it adds little. A better toy would add the counterfactual: if Cy were *not* in Rome, Ann's evidence and belief would be exactly the same, yet D would be false. That isolates "truth disconnected from evidence".

### C. Coverage
Complete. Nothing in the paper is missing.

### D. Usefulness
The digest (1,867 words) is **1.8× the length of the paper** (~1,000 words). The 1,200-word floor in `target_words()` forces this. L3 is effectively a paraphrase of the whole paper, so for a 3-page paper it is a copy, not a guide. The reader would do better with the original, L0–L2, the toy and the questions. The Prerequisites line is sensible. The B2 language is clean.

---

## 2. Godfrey-Smith 2003, *Theory and Reality*, ch. 5 "Kuhn and Normal Science"

File: `wiki/works/godfreysmith-2003-theory/ch05-kuhn.md`

### A. Faithfulness: 34 claims checked (L0 1, L1 7, L2 8, L3 14, Concepts/Toy 4)
Correct: 25. Minor: 6. Major: 2. Critical: 1.

Checked and correct: the "greatly exaggerated" reading of Kuhn as a myth-breaker, the Trojan horse, and the Encyclopedia series (p. 75); data and logic cannot force a paradigm change, and Kuhn "definitely did not" think it irrational (p. 76); Masterman's 21 senses, broad vs narrow correctly marked as Godfrey-Smith's terms (p. 77); Point 1 and Point 2 contrasts with Popper, crisis science as a bridge (p. 78); Godfrey-Smith's agreement on the role of history (p. 79); the "most fascinating" relationship (p. 79); examples correctly marked as the author's and not Kuhn's (p. 80); one paradigm per field per time (p. 80); Godfrey-Smith's "I think it is clear" that the normative claim holds, and Popper's 1970 criticism (p. 81); puzzle vs problem (p. 81); the rejection conditions (1) and (2), with "only" kept (p. 82); phase transition, critical mass and the bomb (pp. 82–83); "should not" treat anomalies as refutations, and the balance not reducible to explicit rules (p. 83); Problem 1 and Criticism 2, "surely this is possible" (pp. 84–85); the Alife hedges "might be another case" and "maybe it will revitalize" (p. 85); premature commercialization (pp. 85–86). Voice tracking between Kuhn and Godfrey-Smith in L3 is good throughout.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K1 | L1, last sentence | "He also says Kuhn's argument mixes description and recommendation, and that it uses history to address philosophical questions." This conflates two separate points and gives the wrong voice. (i) What Godfrey-Smith says Kuhn mixes is **history/psychology with evidence/justification**, the distinction the logical empiricists drew (p. 78). (ii) The descriptive/normative point is a question "one should always ask", and the complaint that "it's often hard to tell" comes from **"some commentators"**, not from Godfrey-Smith. His own reading simply "stresses the normative element" (p. 79). (iii) The sentence follows his criticisms, so the history point reads as a criticism, but Godfrey-Smith says "I agree with Kuhn about the useful role of history" (p. 79). L3 has all of this right, so L1 goes beyond L3 (rule 4). | pp. 78–79 | **critical** |
| K2 | Toy example | It models Kuhn's "critical mass" as a numerical count of failed experiments (threshold 30). This conflicts with the source in three ways. (a) Within normal science, failures are blamed on the scientist, and hypotheses are refuted routinely; an *anomaly* is a puzzle that has resisted solution (p. 82). (b) What triggers a crisis is problems that are "deep rather than superficial" (p. 83), not a number of them. (c) The balance "is not something we can describe in terms of a set of explicit rules" (p. 83). The disclaimer "Kuhn gives no threshold" does not repair a toy whose whole mechanism is an explicit counting rule. | pp. 82–83 | major |
| K3 | Whole digest | Undefined technical terms for a high-school reader: *logical empiricism/empiricists* (used 4×), *simple empiricism*, *cellular automata* (the source defines it on p. 85, but the digest drops the definition), *Trojan horse* (it is not explained what was smuggled in), *epistemological*. The Prerequisites line omits logical empiricism, which the chapter relies on ("as we saw in chapter 2"). | pp. 75, 78, 85 | major |
| K4 | L3 5.2 | "later writing mostly means the broad sense". The source says "in much of his writing, and in most of the work written after *Structure* using the term" (much of Kuhn's own writing, and most of *other people's* later work). | p. 77 | minor |
| K5 | L3 5.4 | "scientists tend to become interested in philosophy" loses the voice and the hedge: "Amusingly, *Kuhn even suggests* that during crises…". It also drops the point that Kuhn sees philosophy as "quite useless for normal science". | p. 82 | minor |
| K6 | L2 bullet 1 | It states broad/narrow as if these were the senses of "paradigm", without saying the terms are Godfrey-Smith's (L3 does say so). | p. 77 | minor |
| K7 | Concepts | `[[falsifiability]]` is defined as "Popper's permanent openness to refutation". Falsifiability (the canon meaning: a criterion of what counts as scientific) is not mentioned in the chapter. What the chapter discusses is Popper's *critical attitude*. The digest does not flag that its meaning differs from the canon's. | p. 78 | minor |
| K8 | L3 5.3 | It omits Popper's concession, "Popper can certainly allow that not everything can be criticized at once", so Popper comes out more absolute than in the source. | p. 81 | minor |
| K9 | L3 5.4 | "simple empiricism, for which too much willingness to revise is unexpected" garbles the source: the *idea that* willingness to revise can go too far is unexpected for empiricism. | p. 83 | minor |

### B. Toy example
Misleading (see K2). Better: two labs facing the same unexpected result. A normal-science lab first checks its own equipment and calculations ("poor workman"). It changes framework only when a *deep* puzzle survives the best workers *and* a rival exists. No number is involved.

### C. Coverage gaps
- "Normal science is structured in a way that makes its own destruction inevitable, but only in response to the right stimulus" (p. 83). This is the core of the bomb analogy, and it is only half there.
- Kuhn's own examples, Newton's and Einstein's paradigms (p. 80), and "Kuhn does not think that all science needs a paradigm" (p. 79).
- Why commentators criticised Kuhn's descriptive/normative ambiguity (p. 79). This loss is the root of K1.

### D. Usefulness
Good guide: 0.5× the source, clear structure, short sentences and careful voice tags in L3. Intuition notes are brief and correct. Prerequisites need "logical empiricism (ch. 2): the idea that theories are judged by logic and observation alone".

---

## 3. Carey 1989, *Communication as Culture*, ch. 1 "A Cultural Approach to Communication"

File: `wiki/works/carey-1989-cultural/ch01-cultural.md`

### A. Faithfulness: 45 claims checked (L0 1, L1 7, L2 8, L3 25, Concepts/Toy/Notes 4)
Correct: 31. Minor: 10. Major: 4. Critical: 0.

Checked and correct: the Dewey puzzle and "excessive masochism" (p. 11); the "I think" hedge on the two-senses thesis, both views with religious origins (p. 12); the transmission summary sentence (p. 13); the religious-roots illustration, "devious though, in detail, inadequate", the age of exploration and redemptive movement (p. 13); Batchelder and Morse (pp. 13–14); Miller's "Christianized technology", the secularisation step, Calhoun (p. 14); "only assert here rather than demonstrate", correctly kept (p. 15); the ritual view, archetype and Durkheim (p. 15); the three roots of America's aversion to "culture" (p. 16); both newspaper analyses and news as a historic form (pp. 16–17); "neither… necessarily denies", "origins determine endings" (p. 17); the Dewey 1916 passage and "untrue to his own thought" (p. 18); the definition (p. 19); the inversion of realism with "not to make any large metaphysical claims" kept, fn. 5 kept (pp. 20, 28); "entropic—that is, not strictly ordered", latitude/longitude (p. 20); Young, Vogelin, Cassirer (p. 21); the map example, displacement and productivity (pp. 21–22); thought as public in two senses (pp. 22–23); of/for, the blueprint, ritual, "squaring the circle", fn. 6 Geertz (p. 23); maintenance, repair and transformation, Skinner→Chomsky, fns. 7–8 (pp. 23–24, 28); the "insufficiently empirical" objection and reply, correctly tagged (p. 24); the power and anxiety models (p. 25); Gouldner's reflexive science (p. 25); Williams (p. 26); the diagnosis and the political, economic and ritual orders (pp. 26–27); the three examples (p. 27); fn. 4 (pp. 27–28). Voice tracking between the transmission and ritual views is clean: no sentence reports the transmission view as Carey's own.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| C1 | Concepts | `[[entropy]]` links Carey's loose "entropic—that is, not strictly ordered" to the canon id whose definition is Shannon's $H=-\sum p\log p$ (communication-theory and information-theory canons). Rule 10 requires saying when the meaning differs. The Knowledge Manager will join Carey to Shannon entropy, which is a false same-math link. | p. 20 | major |
| C2 | L3 II "Sources and definition" | "The most viable tradition he finds is the Chicago School" drops "**though still inadequate**". Carey's hedged endorsement becomes an unhedged one, and L3 is the only place this point appears. | p. 19 | major |
| C3 | Whole digest | It quotes the source **153 times (~500 quoted words)**. Rule 13 allows "at most a few short quotes". L3 reads as a quote collage of every paragraph, closer to a copy than a guide. | — | major (format) |
| C4 | Prerequisites + body | "Prerequisites: none" is not sensible. Terms used without definition: *phatic communion*, *terministic systems*, *scientific realism*, *metaphysical*, *operant conditioning*, *deep structures*, *functionalism*, *uses and gratifications*, *dissonance*, *balance theory*, *fiduciary*, *Galilean paradigm*, *Chicago School*. | pp. 17, 20, 24, 25, 28 | major |
| C5 | L3 I, Transmission | "the old wish to speed up messages in space, from Egypt's First Dynasty to the telegraph". In the source, the First Dynasty→telegraph span is when "transportation and communication were inseparably linked", not the span of the wish. | p. 12 | minor |
| C6 | L3 I, sources | "Gardner Spring called thought's travel by 'steam and magnetic wires' a border of a 'spiritual harvest'" garbles the logic. Spring said we are on "the border of a spiritual harvest *because* thought now travels by steam and magnetic wires". | p. 13 | minor |
| C7 | L3 II, blueprint | "one points at it and says 'That's the house'". Here "it" reads as the house, but Carey points at the **blueprint**. This is the very example that defines "of". | p. 23 | minor |
| C8 | L2 bullet 8 | "widespread **worry** about communication". The source says "widespread social **interest**". | p. 26 | minor |
| C9 | L3 II "Thought is public" | "Carey says instead" replaces "I wish to suggest, in contradistinction". The hedge is lost. | p. 22 | minor |
| C10 | L3 II "familiar strange" | The fish-and-water image is McLuhan's ("There is truth in Marshall McLuhan's assertion"), but the attribution is dropped. | p. 19 | minor |
| C11 | L3 II power/anxiety | "institutions' policies and programs create the abstract motives…". In Carey, **the models** create them "through policy and program". The subject is swapped. | p. 25 | minor |
| C12 | L1, last sentence | "today's power and anxiety models help produce the troubles" rests on "Our existing models… are less an analysis than a contribution to the chaos of modern culture" (p. 27), which L3 never reports. This is a slight rule-4 breach. | p. 27 | minor |
| C13 | Reading notes | It reports the 1975 original date "from source metadata". Rule 14 allows only what is visible on the pages. The provenance is honest, so this is minor. | — | minor |
| C14 | Toy | The percentages (2/6 ≈ 33%, 3/6 = 50%) do no work, and they quietly frame the maps in transmission terms ("information kept"). | — | minor |

### B. Toy example
Correct, and it illustrates *of/for* and "different maps, different realities" (pp. 22–23). It does **not** touch the chapter's headline contrast (transmission vs ritual). A newspaper toy would hit the main idea: the same front page read once for new facts and once as a confirming drama in which the reader takes a role.

### C. Coverage gaps
- "Reality is not there to discover in any significant detail" (p. 20). This is the plainest statement of the inversion.
- "It could no longer go forward without disastrous intellectual and social consequences" (p. 18). This is Carey's reason for changing course.
- "Our existing models of communication are less an analysis than a contribution to the chaos of modern culture" (p. 27). This is the key concluding claim, and its absence is behind C12.
- The ritual order is "not to perform functions but to manifest an ongoing and fragile social process" (p. 15). The two views "correspond to particular historical periods, technologies, and forms of social order" (p. 18).

### D. Usefulness
At 0.55× the source and 1.37× the target, it is too long. Its 3,354-word L3 paraphrases nearly every paragraph and carries a parade of names (Spring, Batchelder, Calhoun, Vogelin, Young, Portman…) that a B2 reader cannot use. L0–L2 are good and could stand alone. The intuition notes are correct. With half the quotes and a glossary of eight to ten terms, this would be a strong entry.

---

## 4. Apperly & Butterfill 2009, "Do humans have two systems to track beliefs and belief-like states?" (part 1, pp. 1–19)

File: `wiki/works/apperly-2009-two-systems/main-p1.md`

### A. Faithfulness: 40 claims checked (L0 1, L1 7, L2 7, L3 21, Concepts/Toy 4)
Correct: 29. Minor: 8. Major: 1. Critical: 2.

Checked and correct: the abstract's proposal with "may be best explained" (in L3) (p. 2); the competing demands (p. 3); the modular vs general-reasoning views, and "neither is likely to be fully correct" for *that* pair (p. 4); the benchmarks at 4 and at 5–6 years (p. 5); Garnham and Southgate (pp. 5–6); Onishi & Baillargeon's design and its reversal (p. 6); the two camps and the parsimony stalemate, "both sides… mistaken" (pp. 6–7); Piaget and conservation (p. 8); the 3-item limit, Feigenson & Carey, the 8 vs 16 ratio limit with "perhaps" kept (p. 9); animal and adult convergence, the ratio shrinking with age (pp. 9–10); the three disagreements (pp. 10–11); the four points of agreement, including "only… if and when" (pp. 11–12); systems vs concepts, and belief-like states (pp. 12–13); the prima facie case with "at least reasonable" kept (p. 14); the two readings of infant success (p. 15); content limits and the propositional-content conclusion (p. 16); "falls well short… several criteria", "underestimates" (p. 17); chimpanzee boundaries and scrub-jay findings, with "We regard these…" correctly voiced (pp. 18–19).

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A1 | L3 "Role" bullet | It says infants do not expect belief "**from close proximity alone**", which is a *sufficiency* claim. The source says infants "do not take close proximity to an object to be a **necessary** condition for having a belief about it". This is a necessary/sufficient flip, the exact error rule 2 names. | p. 17 | **critical** |
| A2 | L1, sentence 3 | "neither 'infants understand belief' nor 'infants just use behaviour rules' is likely to be fully right" weakens and transplants a claim. For the infant debate the authors say "In our view **both sides of this conflict are mistaken**" (p. 7). "Neither is likely to be fully correct" is their verdict on a *different* pair, modular vs general reasoning (p. 4). L3 has both right. | pp. 4, 7 | **critical** (low impact) |
| A3 | Whole digest | Undefined terms in a grad-level text for a high-school-level reader: *executive function* (central to the argument and never defined), *habituation*, *preferential looking*, *conservation (of number)* (the source explains it, p. 8), *parallel individuation*, *object files*, *analogue number representation*, *modes of presentation*, *level-1 perspective-taking*, *quantifier*, *central process*, *parsimony*. The Prerequisites line omits executive function and working memory. | pp. 7–17 | major |
| A4 | L3 Abstract | "Four puzzles" is followed by three contrasts (infants/children, animals, adults). | p. 2 | minor |
| A5 | L0 | "belief reasoning uses an efficient but inflexible system (found in infants and animals)" drops the abstract's hedge "**may be best explained** by". | p. 2 | minor |
| A6 | L1, L2 bullet 4 | "infants, adults and animals **share an efficient system**". The source says "one or more systems", "analogous capacities in some non-human animals", "similarity of these systems". | pp. 11–12 | minor |
| A7 | L2 bullet 7 | It limits "believe" to scrub-jays. For chimpanzees too, the authors say the behaviour is "beneficial in virtue of controlling what others see **and believe**". | p. 19 | minor |
| A8 | L3 Number | "(5–8 months is given for the first example)". In the source, "young infants (5–8 months of age)" is the subject of all four abilities in that sentence. | p. 8 | minor |
| A9 | L3 Onishi & Baillargeon | The infants' age (**15 months**) is missing in L3, though L1 relies on it. The hedge "looking times **may correlate** with whether…" is also dropped. | p. 6 | minor |
| A10 | Toy | The tracker's stated limit is "fails for any belief that needs a negation", but the table column says "quantifier". The authors' example is a quantifier ("There is no red ball"). | p. 16 | minor |

### B. Toy example
Mostly correct and the most illuminating of the four. It shows how a pattern of failures, unchanged by memory load, diagnoses a separate system, and it ties back to the 3-item search. Fix the negation/quantifier mismatch (A10). Also note that some existing studies may already require tracking features (p. 16), so the "location-only" tracker is a hypothetical, not the authors' claim. The toy says "hypothetical", which is enough.

### C. Coverage gaps
- The authors' explicit target: "our point is to question whether it is plausible that infants' abilities are limited only by their general knowledge and the concepts they can apply" (p. 17), with the "global warming, quarks or nativism" illustration (p. 15). This is what makes "signature limits" a real test.
- The summary sentence that number judgements exist in participants "with limited or no access to language and executive processes" (p. 10). Also: a conventional number system "transform[s] the representational powers… adding new concepts" (p. 12).
- Scrub-jays "deny others perceptual experience", the step before the "more impressive" recovery findings (p. 19).

### D. Usefulness
0.56× the source, 1.41× the target. The structure is excellent: the L3 headings follow the paper's own, and voice tags (Camp 1, Camp 2, Authors) are clear. It is too dense in jargon for the stated reader (A3). `level: grad` is honest, but then the digest needs a short glossary.

---

## Error patterns across the four digests

1. **Summary drift past a correct L3.** Two of the three criticals (K1, A2) are L1 sentences whose L3 counterpart is correct. The verifier's mandatory items cover L0, L1, L2 and intuition-note sentences only when they contain a STRONG word. Neither K1 nor A2 contains one.
2. **Condition words outside the STRONG list.** A1 turns on "necessary" vs "alone", and neither word is in `STRONG`. A1 is also in L3, which the strength check does not scan.
3. **Hedges and qualifiers lost in paraphrase.** Examples: C2 "though still inadequate", C9 "I wish to suggest", A5 "may be best explained", A9 "may correlate", K5 "Kuhn even suggests". Each is small, but they recur in every digest except Gettier.
4. **Readability failures are systematic, not random.** Three of four digests leave many technical terms undefined. Carey quotes heavily. Gettier is longer than its source.

## Prompt and pipeline improvements (3)

**P-1 (verifier, highest value): an L0–L2 ⇄ L3 entailment pass for every sentence.** Make *every* L0/L1/L2 sentence a mandatory item, not only those with STRONG words. For each one, the verifier names the L3 line that supports it and checks two things: (a) same strength; (b) same voice. "X says/thinks/criticises" must match who says it in L3 and on the cited page. This would have caught K1 and A2, and also C12.

**P-2 (checks.py + verifier): widen the strength trigger and scan L3.** Extend `STRONG` with `necessary|sufficient|alone|merely|only if|unless|condition|suffice` and apply it to L3 sentences as well. For each flagged sentence, the verifier quotes the source sentence and confirms the logical form, especially necessary vs sufficient. Add a hedge-survival instruction: "list qualifiers in the cited source sentence (may, perhaps, I think, I suggest, though…, still inadequate) and confirm each survives". This catches A1, C2, C9 and A5.

**P-3 (deterministic checks): readability and length.**
- (a) Quote budget: flag a digest with more than ~10 quoted spans or more than 3% quoted words (Carey: 153 spans).
- (b) A term check: the verifier lists technical terms used without a ≤15-word definition at first use; three or more triggers repair. Also check that the Prerequisites line names what L3 assumes (C4, K3, A3).
- (c) A length cap for short sources: `target = min(max(1200, 0.4·sw), 0.8·sw)`, so a 3-page paper does not get a digest longer than itself (Gettier).
- (d) A Concepts check: when a reused canon id's canon definition is technical and the digest's definition differs (entropy, falsifiability), require "(differs from canon: …)".

## Hand fixes needed now (before later posts reuse these)
- K1: rewrite the last sentence of Godfrey-Smith's L1, e.g. "He also notes that Kuhn mixes history with questions of justification, which he welcomes, and that one must ask which of Kuhn's claims are descriptive and which normative."
- A1: change to "they do not take close proximity to be **necessary** for having a belief about an object".
- A2: change to "The authors think both camps are mistaken".
- C1: change to `[[entropy]]` with "(differs from canon: Carey means only 'not strictly ordered', not Shannon entropy)", or drop the link.
- K2: replace the Godfrey-Smith toy example.
