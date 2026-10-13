# Independent audit: philosophy and prose digests (Dennett ch. 2, Wittgenstein PI §§243–315, Kahneman ch. 3)

Auditor: Claude Opus 5.5 (independent; did not write or verify these digests). Date: 2026-10-13.
Pipeline audited: Sonnet 5.5 digest pass (P1) plus independent verifier pass (P2). All three digests are `verified: repaired`.
Method: I read every source page (Dennett as page images, since there is no text layer; Wittgenstein and Kahneman as text layer, checked against the page breaks) and checked digest claims one by one against the source.

**Page-number mapping used in this audit.** All three digests cite `(pdf N)` using the page index of the *parent book* file, not the page index of the excerpt in `/home/claude/audit/`. Offsets: Dennett pdf N = excerpt page N−11 (pdf 12 = excerpt p. 1 = printed 12–13; each excerpt page is a two-page spread); Wittgenstein pdf N = excerpt page N−123 = printed (N−29)e (pdf 124 = 95e … pdf 139 = 110e); Kahneman pdf N = excerpt page N−40. With these offsets, **every page reference I checked lands on the correct page** (±1 at page breaks). The errors are elsewhere.

---

## Summary

| Digest | Claims checked | Correct | Minor | Major | Critical |
|---|---|---|---|---|---|
| Dennett ch. 2 | 52 | 46 | 4 | 2 | 0 |
| Wittgenstein §§243–312 | 58 | 43 | 8 | 6 | 1 |
| Kahneman ch. 3 | 47 | 44 | 3 | 0 | 0 |

(The citation-scheme problem is counted once per digest as a major issue, not once per citation.)

**Overall verdict.** Kahneman: acceptable as-is. Dennett: acceptable after two fixes. Wittgenstein: **not yet acceptable** as a foundation for later posts. Its surviving errors are the ones the audit was asked to watch for: (i) whose voice a sentence reports, (ii) hedges, and (iii) one imported slogan. These are exactly the errors a later post would copy and amplify. All three digests are faithful at the level of "what is said on the page". Where they fail, they fail at the level of "who is saying it, and how strongly". The verifier prompt does not check for this at all (see Prompt improvements).

---

## 1. Dennett 1987, ch. 2 "True Believers" (+ Reflections)

File: `wiki/works/dennett-1987-intentional-stance/ch02-true.md`

### A. Faithfulness: 52 claims checked (L0 1, L1 6, L2 9, L3 32, Concepts/Instances 4)
Correct: 46. Minor: 4. Major: 2. Critical: 0.

Checked and correct (sample): realism/interpretationism framing and Dennett's two-sided thesis (p. 15); astrology contrast and "Having a good strategy is one thing…" (p. 16); physical/design/intentional stance definitions, alarm clock, liquid helium (pp. 16–17); four-step recipe (p. 17); exposure rule, spectacle-wearers, "special genealogy", Jones and snake cases, "less than ten percent", "which I doubt very much" (pp. 18–19); footnote 1 belief vs opinion and Democritus (p. 19); fundamental rule, desire list, derived desire rules (p. 20); omelette and baked beans (pp. 20–21); perfect rationality revised downward, Cherniak (p. 21); Oxford colleges, clam, chess computer, thermostat, apple trees, lightning (pp. 21–22); "Sisyphean labor", lectern (p. 23); the Laplacean objection correctly marked as an objection, "human epistemic frailty" (p. 23); "The decision to adopt the intentional stance is free…" (p. 24); chess's half a dozen moves, trader/politician, KGB chain (pp. 24–25); Nozick's Martians, stockbroker, spark plug, societal sockets/pivot points (pp. 25–26); Mrs. Gardner contest, intersection A, fatalism "almost right", unavoidability of the stance, Hampshire (pp. 26–27); melted amplifier, strong vs milder realism, "*when* and *why* there is no fact of the matter…", interest relativity, McCarthy footnote (pp. 28–29); perverse claim, de-interpreted thermostat, Winnipeg, shrinking class of models, *de re* footnote, two-way constraint (pp. 29–31); italic principle, Twin Earth, "no magic moment" (pp. 32–33); Spencer, Skinnerian answer, LOT, the two empirical claims, combinatorial explosion, footnote 6 (pp. 33–35); Reflections: knife-edge, Life rule (verified word by word), Turing machine stance, "no backstage", Akins, Anscombe footnote, Rorty, Quine 1960/1969/1970, "Brain Writing and Mind Reading", Wheeler/Derrida footnote, Davidson, Parfit's club, Nagel (pp. 37–41).

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| D1 | All citations; frontmatter `pages`; Reading notes | Spec requires **printed** page numbers. Every page image shows them clearly (13–41), but the digest cites `(pdf N)`. Each pdf number covers **two** printed pages, so every citation is only accurate to a spread. The digest works out the correct mapping in Reading notes, which shows it could have cited printed pages. (The root cause is in the pipeline: the `printed=` attribute was missing; see P-1.) | all pages | major (systematic) |
| D2 | L3 "Footnote 2 (pdf 20)" | Misreads Dennett's reply. The digest says "the Martian's output would read like a Ouija board, and would be baffling as a *true sentence of Martian*." In the source, the *Earthling's* prediction would appear in the Martian's calculations "word by Martian word, as on a Ouija board", and what baffles the Martian is *how this chunk of mechanism… was able to yield this true sentence of Martian* when it was informationally isolated. The digest gets the subject, the object and the source of the bafflement wrong. | p. 28 fn. 2 | major |
| D3 | L2 "Why it works" | "Dennett thinks some version of the language-of-thought hypothesis **may be right**". The source is stronger: "I think some version of it **will prove correct**" (given attenuation). L3 has it right; L2 weakens the modal. | p. 34 | minor |
| D4 | L3 "Two opposing views" | Drops the hedge "These two opposing views, so baldly stated, do not fairly represent any serious theorists' positions". Also drops "apparently" from "that apparently makes me a realist / an interpretationist". As a result, Dennett's ironic self-placement reads as a flat self-labelling. | p. 15 | minor |
| D5 | L3 Oxford colleges | "it consists of reasons people have for giving others reasons for acting". Dennett's point is a *recursive* chain of reasons ("…to give others reasons for acting in such ways as to give others reasons for…"), which leads to a circumstance we would not want. The paraphrase loses the recursion, and the recursion is the point. | pp. 21–22 | minor |
| D6 | L1 | "works … a little, even thermostats". Dennett says the strategy works "at least a little bit" even in the *worst* cases (frauds, metaphors). The thermostat is introduced as a modest but genuine case ("More modestly, the thermostat will turn off…"). Small shift in emphasis. | pp. 22–23 | minor |

### B. Toy example
The arithmetic is **correct**. I re-did the blinker (period-2 oscillator) neighbour counts, and every count is right. It is only **partly illuminating**. It shows a higher-level, *design-stance* pattern ("a thing that blinks"). It does not show an *intentional-stance* pattern, which is the chapter's subject. The claim that the pattern is "visible only if one adopts that description" is overstated for a blinker, which anyone can see. A better toy would show predictive leverage from belief/desire attribution: for example, Dennett's own chess point turned into numbers (≈30 legal moves → ≈6 sensible ones → a prediction with probability ≈1/6 instead of 1/30), or a thermostat whose behaviour is predicted by "wants 20 °C, believes it is 17 °C".

### C. Coverage gaps (L3)
- **Missing key conclusion of the Martian section (p. 28):** "we cannot suppose them to lack the requisite concepts. If they observe, theorize, predict, communicate, they view *themselves* as intentional systems. Where there are intelligent beings, the patterns must be there to be described, whether or not we care to see them." This is the step that turns "the Martians miss a pattern" into "the pattern is objective". Only footnote 3 is summarised.
- The "Earthling disguised as a Martian" twist (species-chauvinism) is omitted (p. 27). Minor.
- The lectern's contrast case is omitted: for people, animals and computers the intentional strategy is "often the only strategy that is at all practical" (p. 23). This is the positive criterion that disqualifies the lectern.
- Hayes 1979 is not mentioned (p. 31). Minor.

### D. Usefulness (B2 reader, high-school start)
Strong points: faithful order, good intuition notes (the three stances "ignore different amounts of detail"; "beliefs get more specific the more tightly a system is tied to its surroundings"). L0–L2 are good stand-alone summaries.
Weak points: L3 is long (~170 lines) and close to a paraphrase. Several technical terms are **not defined at first use**, which the spec requires: *Laplacean*, *hermeneutics/Verstehen*, *de re*, *instrumentalistic*, *Twin Earth* (defined only by example), *indeterminacy of radical translation*, *façons de parler*. The "map/coastline" intuition note is a little confusing. The two-page-per-citation problem (D1) makes checking slow.

---

## 2. Wittgenstein, *Philosophical Investigations* (4th ed.), §§243–312

File: `wiki/works/wittgenstein-1953-investigations/ch04-private.md`

### A. Faithfulness: 58 claims checked (L0 1, L1 6, L2 10, L3 33, Concepts/Instances/Bridges/Questions 8)
Correct: 43. Minor: 8. Major: 6. Critical: 1.

Checked and correct (sample): §243 the monologue language is not at issue; §244 natural expression, "replaces crying, it does not describe it"; §246 "false in one way and nonsense in another", the joke; §247; §248 patience; §250 the dog; §251 the rod example; §253 criterion of identity, Siamese twins, breast-striking; §254 raw material and the mathematician; §256; §257 child genius and "post where the new word is stationed"; §258 the full diary argument and "we can't talk about 'correct'"; §259 the balance; §260; §261; §265 independent authority, timetable, newspapers; §§266–268; §269; §270 manometer and knob; §271 idle wheel; §§273–280; §281; §§282–288; §§290–295 (beetle wording is accurate, including "divide through" and "object drops out of consideration as irrelevant"); §§296–299; §302; §303; §304 "not a Something, but not a Nothing either"; §§305–309 (voices handled correctly here); §§310–312. The § numbering is correct throughout.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| W1 | L3 §§249–250 | **Reverses a rhetorical question.** The digest has "We may be too hasty in assuming a baby's smile is not pretence." The source asks: "Are we perhaps over-hasty in our assumption…? — And on what experience is our assumption based? (Lying is a language-game that needs to be learned like any other one.)" The parenthesis shows the thrust: an infant *cannot* pretend, and our "assumption" is not an empirical assumption at all. The digest states the opposite as a live possibility and then puts the incompatible parenthesis directly after it. (Reading-dependent, but the flat assertion is not supported by the text.) | §249, 96e | critical |
| W2 | L3 §§262–263 | **Voice misattributed and the author's verdict dropped.** The digest has "'Surely I can resolve inwardly…' Reply: how do you know the resolution succeeded…?" In the source the second line is itself a quoted challenge, and Wittgenstein then comments "**An odd question.**" Everywhere else in the digest, "Reply:" means Wittgenstein's own answer, so this presents the challenger's question as his view. It also omits his remark that the question is odd, which links to §246/§288: doubt has no place here. | §263, 100e | major |
| W3 | L3 §264 | **Interlocutor's thesis given without attribution.** "'Once you know what the word signifies, you understand it, you know its whole application' (pdf 129)" stands alone as the whole content of §264. It is a quoted claim of the view under examination (meaning grasped at a stroke, by inner attention). A reader will take it as Wittgenstein's thesis. | §264, 100e | major |
| W4 | L3 §272; Canonical instances `[[red-impression-spectrum-possibility]]`; Bridges | **Voice.** §272 ("The essential thing about private experience is really not that each person possesses his own specimen, but that nobody knows…"; "The assumption would thus be possible — though unverifiable…") states the *private-linguist's* conception, which §§273–277 then take apart. The digest reports it as a plain finding and promotes it to a canonical instance ("it is possible but unverifiable that people have different impressions of red") and to a bridge with the "inverted spectrum". Later posts would cite Wittgenstein as *endorsing* an unverifiable inverted spectrum. | §§272–274, 102e | major |
| W5 | L0 | **Hedge dropped at the most-read level.** L0 says a sensation word "gets its meaning from a public language-game with natural pain-behaviour". The text offers this as "**Here is one possibility**" (§244). L2 keeps the hedge; L0 turns a suggestion into the thesis of the unit. | §244, 95e | major |
| W6 | Intuition note after §295 ("Meaning is use."); Concept `[[meaning as use]] (pdf 135–136)` | **Imported, unhedged slogan.** "Meaning is use" does not appear in §§243–312. The project's own canon (`canon/analytic-philosophy.md:328`) gives it as "for a *large class of cases*, a word's meaning is its use". The note imports the slogan from outside the unit and drops that hedge. The concept line attaches it to pp. 106e–107e as if it were stated there. | 106e–107e; canon l. 328 | major |
| W7 | Frontmatter `pages`; all citations; Reading notes | Spec requires printed pages. The digest says "printed page numbers unknown", yet admits the running heads show 95e–110e (they are in the text layer on every page). For PI the § number is the real standard. The digest uses § headings in L3, so a reader can recover the place, but the frontmatter statement is false and L2/L1 cite only pdf numbers. | every page | major (systematic) |
| W8 | L3 §243 | "An explorer could translate such a language, **because** he also hears their resolutions and decisions". In the source, hearing resolutions explains why translation would let him *predict their actions*, not why he could translate. | §243, 95e | minor |
| W9 | L3 §252 | "tempts us to answer both 'Nonsense!' and 'Of course!'" The source says we *could* respond "Nonsense!" but are *inclined* to reply "Of course!". The asymmetry is the point. | §252, 97e | minor |
| W10 | L3 §265; L2 "Private justification" | §265: "Looking up a table only in the imagination is a 'subjective justification'" reports the interlocutor's suggestion as fact (the reader can recover the voice only from the next "But"). L2: "Checking one imagined table against another". The source case is checking *one memory against another* (the remembered timetable page). | §265, 100e | minor |
| W11 | L3 §281 | "Isn't pain then nothing without pain-behaviour?" Source: "doesn't what you say amount to this: that there is no pain … without pain-behaviour?" Paraphrase shifts the question. | §281, 103e | minor |
| W12 | L3 §289 | "someone who **knew** what I call 'pain'". Source: "If someone else **could** know…" The counterfactual matters, because on the private view no one else could. | §289, 106e | minor |
| W13 | L3 §§300–301 | Omits the qualification "Imagined pain certainly enters into the language-game in a sense; only not as a picture." Without it the passage reads more eliminativist than it is. | §300, 108e | minor |
| W14 | Questions | "§292 … applying any rule needs no further guidance". Source: "you would still have to apply the rule in the particular case **without guidance**". The source makes a point about the absence of a further rule, not about need. | §292, 106e | minor |
| W15 | Reading notes | "The source notes also say Part II is renamed 'Philosophy of Psychology – A Fragment'". This is not in the supplied pages. It is either pipeline metadata or memory, and cannot be verified from the source. | — | minor |

### B. Toy example
The arithmetic is trivially correct, but the example **is not illuminating, and it begs the question**. It *stipulates* that each person makes the same 5 utterances whatever is in the box, then "computes" 15 − 15 = 0 differences. The conclusion is built into the setup, and the numbers add nothing. (Also, "15 − 15" is not a count of differences.) The manometer paragraph is better. A more useful toy would contrast two games. In game 1, "beetle" is used to *report on* the box and others can check it (open-box days), so swapping contents changes correct use. In game 2, no checking is ever possible, so swapping changes nothing. That shows what checkability adds, which is §258's point.

### C. Coverage gaps
- §§313–315 are not covered because the supplied pages end inside §312. The digest flags this correctly; it is a source-slicing problem (the unit TOC says §§243–315).
- §§242/243 boundary: the end of §242 is skipped, which is fine.
- **No map of the argument.** L3 is a remark-by-remark paraphrase, accurate but flat. It never states the structure of the private-language argument (§243 definition → §258 diary → §§265–271 the justification and idle-wheel arguments → §293 beetle → §§304–308 "not a Nothing" and the anti-behaviourist clarification). A reader cannot tell which remarks carry the argument and which are asides.
- The interlocutor's voice is marked only sporadically (it is done well in §§244, 296, 304–307 and badly in §§246, 263–265, 272).

### D. Usefulness (B2 reader, high-school start)
Weakest of the three. The intuition notes are good (especially after §258 and §304). But W's technical vocabulary is not defined at first use in L3: *grammar / grammatical proposition* (used at §251, defined only under Concepts), *language-game*, *criterion*, *private* in W's sense. Paraphrasing a dialogical text without voice markers produces a text that *sounds* like Wittgenstein asserting things he is questioning. That is the worst possible failure for a knowledge base that later posts quote. Length is reasonable.

---

## 3. Kahneman 2011, ch. 3 "The Lazy Controller"

File: `wiki/works/kahneman-2011-thinking/ch03-lazy.md`

### A. Faithfulness: 47 claims checked (L0 1, L1 6, L2 10, L3 26, other 4)
Correct: 44. Minor: 3. Major: 0. Critical: 0.

All numbers verified: 17 and 14 min/mile; 23 × 78; seven and six digits; dynamometer; radishes; both lists of 6 and 5 items; glucose vs Splenda design and result; 8 judges, 6 minutes, 35%, three breaks, ~65% → ~0; >50% (Harvard/MIT/Princeton) and >80%; roses syllogism; Michigan < Detroit average; Mischel (one Oreo, 15 min, about half, 10–15 years); Oregon (five 40-minute sessions, ages 4–6, cat and mud); CRT 63% vs 37%, $3,400/$3,800, ×2 delivery; Stanovich and West's terms and the algorithmic vs reflective mind; "somewhat better"; "Time will tell"; the four "Speaking of Control" lines. The digest also flags correctly that "the questions are shown here" refers to missing material.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K1 | L3 Opening | "Heavy demands on short-term memory cannot be combined with other effort." Kahneman reports *his own experience* ("My experience is that I can think while strolling but cannot engage in mental work that imposes a heavy load…"). The digest turns this into a general law. | pdf 41 | minor |
| K2 | L2 bullet 1; L3 | Hedges thinned. "at the extremes these activities **appear to** compete" becomes "compete". "Self-control and deliberate thought **apparently** draw on the same limited budget" becomes "draw on the same budget" (L2, L0). "Although I have not conducted a systematic survey, I suspect…" becomes "probably". Each change is small; together they make the chapter sound more settled than Kahneman wrote it. | pdf 41–42 | minor |
| K3 | Concepts | `[[heuristic]]`, `[[satisficing]]` and `[[bounded-rationality]]` are canon ids (fine), but carry page refs (pdf 46, 48, 41–42) as if the text used these terms. It does not. A "(mapped; term not in text)" tag is needed. | pdf 41–48 | minor |

### B. Toy example
**Correct and useful.** (A) The pen/notebook isomorph of bat-and-ball is right (10¢) and shows the one-addition check. (B) The rose/tulip counter-model correctly shows invalidity, and it is the most illuminating item of the three digests. (C) 400/3400 = 11.76% per month is right. It would be more striking with the annualised figure added (≈ 1.1176¹² − 1 ≈ 280%/yr), which shows how impatient the 63% are.

### C. Coverage gaps
Essentially none. All four sections and the closing quotations are covered, in order. Two small omissions: "People who say 10¢ appear to be ardent followers of the law of least effort" (which links back to the opening), and Kahneman's own evaluation of Stanovich ("an attractive and thought-provoking idea").

### D. Usefulness
Best of the three: HS level, clear, the right length, and good intuition notes. One **knowledge-base risk the spec itself creates**: ego depletion, the glucose effect and the parole-judges result are reported exactly as Kahneman reports them ("shown conclusively"). The Reading notes say the pipeline deliberately did not check later work, and the Questions section raises the issue gently. Under the current spec that is correct behaviour. But a post built on this digest would present three findings whose robustness was later strongly disputed as settled fact. Fixing this is a spec decision (see P-5), not a digest error.

---

## Cross-cutting diagnosis

1. **The verifier does not test voice or hedges.** `prompts/verify.md` checks A (faithfulness), B (math), C (pages), D (coverage), E (toy), F (labels) and G (format). Its "faithfulness" check asks whether a statement is *supported by the source*. A sentence that faithfully copies an interlocutor's line passes that check even when it is reported as the author's view (W2–W4), and so does a rhetorical question turned into a statement (W1). Nearly all surviving major and critical errors in the two philosophy digests are of this type.
2. **Hedges drift at the summary levels.** In all three digests L3 keeps the hedge more often than L0/L2 do (D3, W5, K2). Summaries compress and lose modality, and the verifier does not compare L0–L2 against L3.
3. **Imported slogans in intuition notes** (W6). Intuition notes are "our words", so the writer treats them as exempt from the only-the-source rule.
4. **Page scheme.** The `printed=` attribute was missing for all three units. The prompt's fallback ("If the printed number is unknown, use (pdf N)") was followed even where printed numbers were plainly visible (Dennett images; Wittgenstein's 95e–110e running heads). For PI, § is the right citation key in any case.
5. **Toy examples for philosophy** tend to be either off-target (Dennett: design rather than intentional stance) or circular (Wittgenstein). The toy-example rule ("hand-computable") pushes toward numbers even where a contrast case would teach more.

---

## Prompt improvements (concrete, ordered by expected error reduction)

**P-1. Voice tagging (digest prompt, philosophy and dialogue texts).** Add:
> "Many philosophical texts argue through other voices (interlocutor, opponent, objector, a view under examination). For every sentence in L0–L3, the reader must be able to tell whose view it is. Use explicit tags: **Interlocutor:** / **W. replies:** / **Objection (Nozick):** / **Dennett:**. Never report a quoted line as a plain statement. Keep rhetorical questions as questions. If you paraphrase one as a statement, state the answer the text implies and cite the clue (e.g. the parenthesis in §249). If the voice is unclear, write `(voice unclear)`."

**P-2. Add a verifier check H, "Voice & hedges", with its own severity rule.** Add to `verify.md`:
> "H. For every L0–L2 sentence and every L3 sentence that reports a view: (1) is the speaker correct (author vs interlocutor vs criticised view)? Misattribution = critical. (2) Is the modal strength the same as the source? Compare words like *may / will / apparently / I suspect / one possibility / at least partly / somewhat*. Weakening or strengthening that changes the claim = major. (3) Compare L0, L1 and L2 against L3: no summary sentence may be stronger than the L3 sentence it summarises."
Also make the verifier list, for each L0–L2 sentence, the L3 line it depends on. This makes hedge drift visible.

**P-3. Intuition notes are not exempt.** Add:
> "Intuition notes and Toy examples may use your own words but **may not introduce doctrines, slogans or results from outside the unit** (e.g. 'meaning is use' when the unit does not say it). If you link to a canon concept, use the canon's exact wording, including its hedges, and add `(canon link; not stated in this unit)`."
Apply the same tag to concept lines whose term is not in the text (K3, W6).

**P-4. Printed pages and section keys.** Replace rule 2 with:
> "Cite printed pages. If `printed=` is missing, read the printed number from the page image or the running head (e.g. '95e', '24'). For two-page spreads, cite the half you used. Use `(pdf N)` only if no number is visible anywhere, and then say so in Reading notes. For works with standard section numbers (Wittgenstein §, Spinoza proposition, Aristotle Bekker numbers), give the section as the primary reference: `(§258, p. 98e)`."
Also fix the pipeline's page tagging so that the `printed=` attribute is filled from the running heads before P1 runs.

**P-5. Argument map and evidence status.** (a) For argumentative texts, require at the top of L3 a 4–8 line **argument map**: the numbered steps, the remarks/pages that carry them, and which remarks are asides. (b) Add an optional section `## Status of findings (added, not from the source)`, filled by a *separate* step allowed to use outside knowledge, for empirical claims later contested (ego depletion, glucose, parole judges). Keep it clearly fenced off from the source digest, so the only-the-source rule stays intact and the knowledge base does not present disputed findings as settled.

(Optional P-6, toy examples: "For conceptual or philosophical units, the Toy example may be a *contrast pair* (two minimal cases that differ in exactly the feature the argument turns on) instead of a numerical computation. It must not build the conclusion into its own setup.")

---

## Verdict

- **Kahneman:** acceptable as a base for later posts (3 minor errors). Add the evidence-status note (P-5b) before posts rely on the depletion or glucose claims.
- **Dennett:** acceptable after fixing D2 (footnote 2) and re-citing printed pages (D1). The content is otherwise accurate and thorough.
- **Wittgenstein:** **not acceptable yet.** 1 critical and 5 content-level major errors (W1–W6) survived verification, all of the voice, hedge or import type. Re-run with P-1 to P-3, or hand-fix W1–W6. Then add voice tags and an argument map before any post builds on it.
- **The pipeline:** the two-pass design catches surface errors well: across ~157 checked claims I found no wrong numbers, wrong § numbers or misplaced pages once offsets are applied. It is blind to *attribution and modality*, and in philosophy those are the errors that matter most. Of the seven severe content errors that survived (W1–W6, D2), six are of this type (the seventh, D2, is a misread footnote); the remaining two majors are citation-scheme problems (D1, W7). In the Wittgenstein digest, about 1 in 8 checked claims (7/58) survived with the wrong speaker, modality or provenance. Expect similar rates for other dialogical texts (Plato, Hume's *Dialogues*, Galileo) unless check H is added.
