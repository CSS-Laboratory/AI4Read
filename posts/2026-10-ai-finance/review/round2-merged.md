# Round 2 → round 3 (final writer round): merged required changes (meta-manager, 2026-10-17)

Inputs:
- `review/verify-2.md` (checker A, Opus: 0 critical / 3 major / 13 minor)
- `review/verify-2b.md` (checker B, Sonnet: 0 / 2 / 17)
- `review/critic-2.md` (criteria 2–6: 3/3/4/4/3)

Read all three. **This is the last writer round.** Anything still open afterwards is fixed by the meta-manager.

## A. The Harari classification (binding; replaces every earlier summary)
The two rounds keep swinging between "too hedged" and "too strong". From now on, use exactly these four groups, everywhere: section 3, the "All of Harari's lines" fold-out, Lens 4, the short answer, §13, the chain diagram and the audio.

| Group | Reporting verb | Lines (timestamp, venue) |
|---|---|---|
| **1. Capability claims, asserted** | asserts | WEF [2:01] "not just another tool. It is an agent." · WEF [2:46] knife line ("new kinds of … money") · WEF [5:48–5:57] (premise: putting words in order) "AI already thinks better than many of us … anything made of words will be taken over by AI" · WEF [10:36] "Everything made of words…" · BIS [5:14] "can actually understand finance better than us … it's only data" · BIS [16:21] "can create new ideas by itself" · Ynet 2023 "What gives money value is the stories…" |
| **2. Forecasts without a hedge** (undated, or "soon") | predicts / expects | BIS [30:24] "I think we'll see AI creativity … new types of financial devices" · WEF [31:11] "we need to prepare for the moment … when AIs create a new financial system" · WEF [16:28] "They will soon be able to … manage a bank account … operate a corporation" · WEF [19:11–19:23] "Ten years from now, it will be too late … Somebody else will already have decided it for you" · WEF [26:29–26:35] "I don't know how long it will take … it will beat me" (*the timing is hedged, the outcome is not*) |
| **3. Thought experiments, hedged** | imagines / supposes / asks | BIS [9:54] "imagine … maybe in 10 years" (device; works, then fails, nobody knows why) · WEF [17:29] "Suppose some U.S. AI persons invent … financial devices" · WEF [31:59] "Maybe nobody in the room…" · Guardian 2023 "What happens if AI…" · Guardian 2024 Broomstick ("imagine the following scenario") |
| **4. His own limits and remedies** | concedes / proposes | WEF [8:05]/[11:42] non-verbal feelings · BIS [21:37]/[23:00] institutions and humans in the loop · Guardian 2023 "catastrophic … but by itself I wouldn't describe it as existential" · Guardian 2024 "Computers are not yet powerful enough…" |

**One summary sentence, to be used verbatim in the short answer and the audio:**
> Harari *asserts* what AI can do (understand finance, create ideas, take over anything made of words), *predicts* without dates that AIs will soon run accounts and firms and will create new financial devices, and *imagines* his concrete finance disasters as thought experiments ("imagine… maybe", "suppose").

Remove every sentence that says "his timelines are hedged", "his forecasts are conditionals" or "a policy question, not a forecast". The legal-personhood point is **both** a forecast ([16:28], [19:11]) **and** a policy question ([16:51] "Do we want to allow that?").

## B. Majors (all must be fixed)
1. **The classification in A** (covers checker B M1/M2 and checker A M1).
2. **Danielsson and Uthemann balance (A-M2).** Restore their main result in Lens 2 lever 2:
   - AI "amplifies existing financial system vulnerabilities";
   - crises become "faster and more severe";
   - current frameworks "cannot effectively prevent and resolve" AI-induced crises.

   Keep the "can both stabilise and destabilise" concession next to it, not instead of it.
3. **Chain diagram `dg-chain` (A-M3, critic).** Rebuild it with **two kinds of labels**:
   - **Harari nodes only** (H1 money is made of stories, group 1 → H2 anything made of words will be taken over, group 1 → H3 AIs create new financial devices, group 2 → H4 nobody understands finance; crises nobody can explain, group 3). Each edge is labelled with *his* status: asserted / predicted / imagined.
   - **Under each node, an "Evidence in our sources" tag:**
     - H1: contested (Searle via SEP: acceptance and enforcement; Menger);
     - H2: partly (LLMs' command of language, post 01); not shown for institutions;
     - H3: not yet evidenced (FSB pp. 28–29, both halves);
     - H4: in 2008, complexity and a correlation error with human-made instruments (FCIC pp. 28, 149); with AI, not evidenced.
   - Our additions (shared models → correlated failures; hidden reasons) go in a **separate, visibly different branch** labelled "ours / FSB 'could' / Scheurer: one red-team test". Never "shown in toys" for hidden reasons or for invented instruments.
   - Reveal the diagram step by step.

## C. Minors (all from both files; fix each or explain in `review/response-2.md`)
Key items:
- **Scheurer.** The ~0% is the rate of *insider trading* under the strongest prompt; deception given trading "remains high under all prompts".
- **CDO wording.** Write "such as" (FCIC p. 128), not "mostly".
- **Remove "already"** from the BIS [5:14] paraphrase.
- **Correlation** runs from −1 to 1.
- **6.65** (or show the unrounded subtraction).
- **Short answer, Lupia.** If only one condition holds, the worst case is the status quo. Drop the unsourced "could not foresee", or label it ours.
- **OQL diagram.** Remove "Trade"; reword "the LLM proposed; the checker decided" so it matches the source.
- **Truth Terminal.** Who created the token is per Decrypt only. Give the $122M and $214M figures with their dates and outlets. Decrypt's date is 16 Oct 2024.
- **Mik quotes** are from the Introduction, not the abstract.
- **Narayanan & Kapoor.** They reject superintelligence as incoherent; do not write "short of".
- **Label "ours"** on the Lupia table mapping and on the reasoning in §9 and §12.
- **Add WEF [17:29]** to "All of Harari's lines".
- **Restore Harari's premise** at [5:57] ("if thinking means putting words in order").
- **AlphaGo.** Note his extension to science, art and finance.
- **Poole** is paired with the right Harari claim.
- **Source list.** Full titles and complete URLs (no truncation). Remove the unused `cites` in post.json (Calvano, Lopez-Lira, Nexus, Mridul).
- **RegretNet.** Either name it as response-1 claimed, or remove the claim.
- **The audio "one method" sentence.** Do not generalise it to "neural networks".

## D. Critic (criteria 2, 3, 6 must reach 4)
1. **Lens 1, ladder 2.**
   - Add a three-sentence toy for the hardness step: 6 assets, 3 products, the seller puts 2 junk assets into one product, so that product defaults more often while the public rule stays short.
   - Explain "intractable" as "no known fast method (a conjecture)". Define "derivative" at first use.
   - Use short lines in the Instance / Question / Mechanism / Formula / Check paragraphs.
   - Cut the C(100,10) aside and the unused "metaphor" tag. Redraw the seller diagram to show the skew.
   - Compute the toy with Python and record it in numbers.md.
2. **Section 3 repetition.** State the Harari groups once, as the table from A in compact form, with about 3–4 quotes in the body. Everything else goes in the fold-out. Cut the repeats in the trap box, the g4 answer, "Our reading", §9 and §13.
3. **Section 4.** Define or cut "approximately incentive compatible" and "deep hedging". Give the option example a number. Give each "Lens N picks this up" note its link type.
4. **Short answer.**
   - Split it into (a) and (b) paragraphs.
   - Add the literal conditional: "If an AI did invent an instrument nobody can state in a page, then: (i) the seller-side information gap grows (Lens 1); (ii) supervisors lose variety (Lens 2); (iii) if many use it, failures arrive together (Lens 3); (iv) accountability needs someone who can verify and penalise (Lens 4)." Use labels such as ours / conjectured where needed.
   - Name concrete consequences for people: who bears losses (the buyers and lenders exposed), and who can still verify (supervisors, auditors with standard menus). Label them ours.
5. **Covariance and the odds line.** Define covariance in the term box. Add "1:1, 4:1, 16:1" to the main text of Lens 3a.
6. **Wide formulas.** Split the clipped formulas in Lens 1, Lens 3a and Ladder 4 into two lines.

## E. Length (new standard counter)
Run `python3 /home/claude/ai4read/scripts/wordcount.py src/content.html`. It counts the main text only, excluding fold-outs, Sources, English and contents. The round 2 draft is **6,548** words. Cap: **7,500**. That leaves room for D1 and D4; pay for them partly with the cuts in D2.
