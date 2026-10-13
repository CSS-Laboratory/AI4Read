# Independent audit: Akerlof 1970 + Cover & Thomas ch. 2 (pipeline v0.1 vs reference)

Auditor: Claude Opus 5.5 (independent; wrote none of these files) · 2026-10-13
Sources checked against page images: `audit/akerlof.pdf` (all 14 pdf pages read as images), `audit/cover-ch02.pdf` (all 38 pages read as images).
Toy examples and every source number recomputed in Python (`python3 -I`, script in session scratchpad).

Severity rubric (as briefed): **critical** = wrong statement / wrong equation / claim not in source; **major** = wrong page ref, missing key content, misleading emphasis; **minor** = wording / format / small imprecision.

---

## 1. Check counts

| Digest | Items checked | Correct | Minor | Major | Critical |
|---|---|---|---|---|---|
| **Akerlof — pipeline** (`main.pipeline.md`) | 45 | 33 | 12 | 0 | 0 |
| **Cover ch. 2 — pipeline** (`ch02-entropy.pipeline.md`) | 66 | 56 | 7 | 1 | **2** |
| Akerlof — reference (`main.md`), lighter pass | 28 | 22 | 6 | 0 | 0 |
| Cover ch. 2 — reference (`ch02-entropy.md`), lighter pass | 30 | 26 | 4 | 0 | 0 |

What "checked" covered:
- Akerlof pipeline: every displayed equation (U1, U2, D1, (1), (2), D2, S2, total demand, symmetric S/D, (3)–(5)), every number (65.7 %/66 %, 1911/1931/1951 table incl. sums, 2,809/8,898, 63→31 %, \$88/\$77, \$66→\$80, \$105→\$70, 85 %, 15/25/50 vs 6/8/10, ½ unit/N→0), all L2 bullets, ~25 L3 claims with page refs, concepts/instances, reading notes.
- Cover pipeline: equations (2.1)–(2.153) (all displayed ones, symbol by symbol, incl. tags), all 5 worked examples (numbers recomputed), all 9 L2 bullets, L0/L1, all intuition notes, summary/problems/historical notes, exercise page refs, concepts, bridges, questions, reading notes (OCR claims verified against the text layer: header "36" on printed p. 16 and "Z = X0" on p. 30 are real).

**Equation fidelity is excellent**: zero equation errors in ~110 displayed equations across the two pipeline digests; both pipeline digests also caught real source misprints (Akerlof eq. (1) labelled $S_2$; the 1911 column summing to 340 not 341; Cover (2.120)/(2.121) duplicate RHS; "four" vs five second-law interpretations).

**Toy examples: all numbers correct** (pipeline and reference, both units). Details in §5.

---

## 2. Surviving errors — pipeline digests

### 2a. Cover & Thomas ch. 2 — pipeline

| # | Location | What is wrong | Evidence | Severity |
|---|---|---|---|---|
| C1 | **L2**, bullet "Second law for Markov chains" | "plain entropy increases **only if** the stationary law is uniform". The source gives a *sufficient* condition ("Entropy increases **if** the stationary distribution is uniform"). "Only if" is false: a chain with stationary law (5/6, 1/6) started from a point mass has $H(X_n)$ = 0 → 0.469 → 0.584 → 0.625 bits (verified numerically). This is the bullet later posts are most likely to quote. | p. 35, item 3 heading and text; summary p. 42 item 3 | **critical** |
| C2 | **Reading notes**, "Edition" | "Numbering and content differ from the 2nd edition (e.g. no universal source coding or portfolio-theory chapters)". Not on any supplied page (outside knowledge), and very likely false: the 1st edition has a stock-market/portfolio chapter and a universal-source-coding section; the chapter's own intro (p. 12) promises answers in "gambling". | p. 12 (only the copyright line supports "1991 edition") | **critical** (low propagation: Reading notes) |
| C3 | L3 §2.9 closing **Intuition note** | "Entropy rises only toward the uniform law, the maximum." Same inflation as C1, stated as a general truth; contradicts the counterexample above. | p. 35 | **major** (misleading emphasis; same root cause as C1) |
| C4 | Bridges, 4th item | "only for uniform stationary laws is $H$ itself monotone" — should be "guaranteed monotone". Same root cause. | p. 35 | minor |
| C5 | L3 §2.1, Lemma 2.1.1 proof | Writes "$0<p(x)\le1$"; the book prints "$0\le p(x)\le1$". Silent correction, not marked. | p. 14 | minor |
| C6 | L3 §2.1, Intuition note | "Entropy **is** the average number of yes/no questions needed" — the line just above says the minimum lies **between** $H$ and $H+1$ (equality only for this dyadic example). Hedge dropped. | p. 15 | minor |
| C7 | Concepts, `[[self-information]]` | Defined as $\log\frac1{p(x)}$ "as used here"; the book uses "self-information" for $H(X)=I(X;X)$, never for the per-outcome term. (The reference digest flags exactly this.) | pp. 12, 20 | minor |
| C8 | Exercises, Ex. 15 | Adds a solution hint "use the triangle inequality and data processing" that is not in the problem (spec: do not solve). | pp. 45–46 | minor |
| C9 | Questions, 1st item | Presents $H(X|Y)+H(Y|X)$ (Problem 15) as a "symmetrized version" of $D(p\|q)$; it is a metric between random variables, not a symmetrized divergence. | p. 46 | minor |
| C10 | Language (L0–L2) | "Markov chain", "pmf", "stationary law", "i.i.d.", "functional" used before (or without) definition; for an HS-start reader L0/L2 are opaque. | — | minor |

**Verifier performance on this unit:** the verifier reported 4 minor issues only and missed C1–C3. `pipeline/reviews/prompt-proposals.md` item 6 already names the "only if" for "if" pattern from the A/B test — it recurred and survived verification.

### 2b. Akerlof — pipeline

| # | Location | What is wrong | Evidence | Severity |
|---|---|---|---|---|
| A1 | L2 "Bad drives out good"; L3 II.A last bullet | "both sides can tell good money from bad" — source: "**presumably** both buyer and seller can tell". Hedge dropped. | p. 490 | minor |
| A2 | L2 "Worked model" | "Under symmetric information, trade happens and gains $N/2$" — the condition "if $N<Y_2$" is dropped (L3 has it). | p. 492 | minor |
| A3 | L2 "Private and social returns differ" | Adds the label "externality" (not on p. 488) and drops "in some cases" before "governmental intervention may increase the welfare of all parties". | p. 488 | minor |
| A4 | L2 "Applications" | "moneylenders charge far more than **central banks** (p. 498)" — p. 498 compares with "large banks in the central cities"; "central bank" appears only on p. 499 (arbitrage sentence). | pp. 498–499 | minor |
| A5 | L3 III.D(2) | "high rates have been **a** leading factor in landlessness" — source: "**the** leading factor". Softened. | p. 498 | minor |
| A6 | L3 III.D(2), footnote 7 summary | "Secured loans are around 6–12 %, … grain loans 25–50 %" — table shows Orissa secured 12–18¾ and Madras grain 20–50. | p. 498 n. 7 | minor |
| A7 | L3 II.C | "everyone knows each car's quality" — unmarked interpretation; the source says only "symmetric information" with a uniform distribution. | p. 492 | minor |
| A8 | Concepts, `[[adverse-selection]]` | Page ref "(pp. 489, 493)" — the term does not occur on p. 489; mechanism is on p. 490, term on pp. 493–494. | pp. 490, 493 | minor |
| A9 | Canonical instances, `[[used-car-market-lemons]]` | "the four-type car model with uniform quality" conflates II.A (four kinds: new/used × good/lemon) with II.B (continuum on [0,2]). | pp. 489–491 | minor |
| A10 | L3 IV "Chains" | Omits the author's reason: chains "offer a better hamburger than the *average* local restaurant". | p. 500 | minor (coverage) |
| A11 | L3 II.A / III.C | Omits the "lunch table" new-car-joy explanation Akerlof argues against, and the street-market vs canned-supermarket comparison. | pp. 489, 496 | minor (coverage) |
| A12 | Language | Undefined at first use: "non-atomistic", "von Neumann–Morgenstern", "Gresham's law" (L2), "externality", "numeraire" (toy), "adverse selection" in L3. | — | minor |

No critical or major error survived in the Akerlof pipeline digest. The verifier's 4 minors were fixed; A1–A12 were not flagged.

---

## 3. Errors found in the reference digests (for the comparison)

**Akerlof reference** (6 minor): drops "presumably" (p. 490); L2 "this is **the** argument Akerlof gives for Medicare" vs "one major argument" (p. 494); L2 "the market underinvests in quality" (not in source); II.C "both sides know only that quality is uniform… owner values any car at expected quality 1" is an unmarked interpretation; toy example misses the second equilibrium (car 1 alone trades at any $p\in[1,1.4]$) and gives the trade range as "about (2, 2.1]" (it is [2, 2.1]); "(Spence, 1973, takes this up)" is outside knowledge in Questions.

**Cover reference** (4 minor): §2.1 intuition note "the answer 'a' resolves half the uncertainty with one question" (it resolves 1 of 1.75 bits; the book says it splits the *probability* in half, p. 15); alternative proof of Thm 2.5.1 and several proofs compressed, displayed steps (2.55–2.58, 2.71) and most equation tags dropped (spec: never skip a step); no "Exercises worth doing" section although the unit has problems (spec); bridge equates Problem 22's $\log k$ bound with the ML "information bottleneck" (name coincidence, different object).

---

## 4. Coverage gaps (pipeline L3)

**Cover pipeline** — essentially complete. Every section 2.1–2.11, every theorem, corollary, example, figure reference, the summary, all 35 problems (sampled), historical notes. Only trivial omissions: the one-line motivation opening §2.8 ("no clever manipulation of the data can improve the inferences", p. 32); the informal sufficiency sentence on p. 37; the Markov-modelling assumption sentence on p. 33 ("knowing the present state, the future … is independent of the past"); the summary's "positive numbers" wording of the log-sum inequality (p. 41), which the reference flags as a source inconsistency.

**Akerlof pipeline** — all five sections and all sub-sections present, incl. footnotes 1, 5 (both), 7. Gaps: A10, A11 above. Neither digest's L3 is missing a key result. (The reference alone notes that "liquidity of durables", promised on p. 488, is never developed — a useful reading note the pipeline lacks.)

---

## 5. Toy examples (recomputed)

| Digest | Result |
|---|---|
| Akerlof pipeline (qualities 1–4, buyer 1.2x) | All rows correct: 2.5→3.0<4; 2→2.4<3; 1.5→1.8<2; car 1 trades for $p\in[1,1.2]$ (unique equilibrium set, verified on a fine grid). Gains 2.0 vs 0.2, loss 1.8 = 90 %. ✔ |
| Akerlof reference (buyer 1.4x) | Numbers correct (3.5<4, 2.8<3, 2.1≥p on [2,2.1], gains 4 vs 1.2, loss 2.8, values 4.2/5.6). Incomplete: a second equilibrium exists (car 1 only, $p\in[1,1.4]$). |
| Cover pipeline (BSC ¼ twice) | $H(¼)=0.8113$, $\log_2\frac43=0.41504$, $I(X;Y)=0.1887$, crossover 3/8, $H(3/8)=0.95443$ (terms 0.53064, 0.42379), $I(X;Z)=0.0456$, Fano with equality. ✔ |
| Cover reference (same channel) | Same numbers plus the $D(p_{XY}\|p_Xp_Y)$ cross-check $=0.4387-0.25=0.1887$. ✔ |

Source numbers re-derived: Ex. 2.1.2 = 1.75; Ex. 2.2.1 $H(X|Y)=11/8$, $H(Y|X)=13/8$, $H(X,Y)=27/8$, $I=0.375$; Ex. 2.3.1 0.2075 / 0.1887; Ex. 2.6.1 0.544 / 0.25; Akerlof table sums 340 (printed 341), 510, 619. All digests report them correctly.

---

## 6. Usefulness for a B2 reader starting at high-school level

**Akerlof pipeline.** Length is right (≈4.4k words; L1 113 words; 8 L2 bullets). L3 is a faithful bullet list — easy to scan, but it reads as notes, not explanation. The II.B intuition note ("he then values the car at only 0.75p") is the best single explanation in either digest. Weaknesses: only 4 intuition notes (none for insurance, dishonesty, institutions), and several terms are never defined (A12). The toy example is clean and lands the "90 % of the gains lost" point well.

**Akerlof reference.** Similar length (≈4.7k). More narrative; defines "nonatomistic", explains Gresham's law, explains *why* group two's 3/2 premium matters, adds the useful $k\ge2$ threshold (correctly marked added step). Better for a first reader; slightly looser with hedges (§3).

**Cover pipeline.** ≈4.9k words, but L3 is a near-transcription of every derivation with tags. Excellent as a reference sheet for later posts that need exact equation numbers; heavy for an HS-start reader. Intuition notes (8) are good where present (Fano's "one bit for 'was I wrong?' plus log(|X|−1) for 'which other value?'" is excellent), but L0–L2 lean on undefined jargon (C10) and two of the notes carry the C1/C6 overstatements.

**Cover reference.** ≈5.9k words, 12 intuition notes, more marked added steps (why (2.145) follows from (2.144), why (2.153) attains equality, why $Z=X+Y$ gives ½ bit). Friendlier for the stated reader, and its reading notes flag terminology clashes with the canon (self-information, "cross entropy" as a name for $D$), which matter for a knowledge base. Weaker on spec compliance (steps compressed, tags dropped, no Exercises section).

Neither Cover digest is pitched at HS level; both are honest "grad" digests. A separate HS-level primer post would be needed regardless.

---

## 7. Pipeline vs reference

| Criterion | Akerlof | Cover ch. 2 |
|---|---|---|
| A. Faithfulness & math | Tie on equations. Pipeline slightly more complete on footnotes/tables and caught the 1911 sum; reference slightly worse on hedges ("the argument", "underinvests"). Pipeline slightly ahead. | **Reference clearly better**: pipeline has 2 critical + 1 major surviving; reference has none. Pipeline better on equation tags / full steps. |
| B. Toy example | Pipeline better (clean, unique equilibrium); reference has an unmentioned second equilibrium. | Tie (both correct; reference adds a useful KL cross-check). |
| C. Coverage | Tie (pipeline: more footnotes; reference: "liquidity of durables" note, lunch-table point, hamburger reason). | Tie on content; pipeline closer to spec (all steps, Exercises section). |
| D. Usefulness | Reference better (definitions, narrative, more intuition). | Reference better (more intuition notes, marked added steps, canon-terminology flags). |
| **Overall** | Roughly equivalent; neither clearly superior. | **Reference superior** — because the one claim that matters most for reuse (the L2 second-law bullet) is wrong in the pipeline version. |

---

## 8. Verdict

- Equation-level fidelity of the pipeline is high and its misprint-spotting is genuinely good.
- The surviving errors are **not random**: all serious ones are **logical-strength inflation** ("if" → "only if", dropped "presumably"/"in some cases"/"if $N<Y_2$", "is" for "between H and H+1") or **outside knowledge in non-L3 sections** (Reading notes, Concepts, Exercises hints, Questions). The verifier, as prompted, checks symbols and page refs well but does not check quantifiers, and treats Reading notes/intuition notes/bridges as low-risk.
- Estimated surviving rate from these two units: ~1 critical per math-heavy chapter, ~0 per prose paper; ~6–12 minors per unit.
- **Acceptable for the knowledge base only after the fixes below** (or a targeted hedge/quantifier re-check of L0–L2 and intuition notes for already-produced units). As-is, an L2 bullet in a foundational chapter states a false theorem, and later posts will cite L2 first.

---

## 9. Prompt improvements (concrete)

1. **Digest prompt — logical-form rule (new rule 1b).** "Keep the author's logical strength exactly. 'if' is not 'only if' or 'iff'; 'may', 'presumably', 'in some cases', 'quite possible', 'between A and B' must survive paraphrase. When L2 compresses a conditional result, keep the condition ('gain $N/2$ if $N<Y_2$'). Before output, find every *only, always, never, iff, exactly, all, every, is the* in L0–L2 and in intuition notes and check it against the source sentence." (Would have prevented C1, C3, C4, C6, A1–A3, A5.)
2. **Verifier prompt — new check H "Logical strength", severity critical.** "For each L0–L2 sentence and each intuition note, locate the source sentence it paraphrases and compare quantifiers, conditions and hedges. Any strengthening (if→only if, may→does, sufficient→necessary, dropped condition) is critical. Intuition notes, bridges and questions are NOT exempt from check A." Add a deterministic pre-check in `checks.py` that greps L0–L2 and intuition notes for `only if|iff|only|always|never` and passes the list to the verifier as mandatory items.
3. **Both prompts — outside knowledge outside L3.** "Reading notes may state edition facts only as shown on the pages (copyright line, ISBN, printed headers). Do not describe other editions, other chapters, or later literature from memory. Exercises: describe what the problem asks; do not add hints. Questions: no citations not in the source." Verifier check A must explicitly cover Reading notes, Concepts, Exercises and Questions. (C2, C8; reference's "Spence 1973".)
4. **Concepts — usage fidelity.** "The one-line definition must state how *this author* uses the term. If the canon id means something different (e.g. self-information = $-\log p(x)$ in the canon, $H(X)$ in Cover), say so in the line and in Reading notes." Also: "page refs in Concepts must point to where the term or its definition appears." (C7, A8, A9.)
5. **Reader-level definitions.** Add to the digest prompt: "List every technical term used in L0–L2 that a high-school reader would not know (e.g. pmf, Markov chain, stationary, externality, non-atomistic, von Neumann–Morgenstern) and define each in ≤ 12 words at its first use." Add to verifier check G: "Name each undefined term; ≥ 3 undefined terms in L0–L2 is major." (A12, C10.)
