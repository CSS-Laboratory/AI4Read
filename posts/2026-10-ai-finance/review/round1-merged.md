# Round 1 → round 2: merged required changes (meta-manager, 2026-10-17)

Inputs:
- `review/verify-1.md` (Opus checker: 0 critical / 7 major / 21 minor)
- `review/verify-1b.md` (Sonnet checker: 0 / 4 / 27)
- `review/critic-1.md` (criteria 2–6: 3/3/3/3/2)

**Read all three in full.** Fix every major finding and every minor finding unless a minor fix is impossible; record each decision in `review/response-1.md`. Where the checkers disagree, the stricter reading wins.

## A. Major findings (union of both checkers; all must be fixed)
1. **Danielsson hedge.** Cite the published JBF 2022 version (`sources/danielsson-2022-jbf-published.pdf`) at p. 7: "will likely be unintelligible to humans". Keep "likely". Text and audio must match. Fix the source-list entry (title and version).
2. **Balance: Harari's unhedged capability claims on finance.** Add these, each in a few words, with the reporting verb "asserts":
   - WEF [2:46], the knife line: AI can invent "new kinds of … money".
   - BIS [5:14]: AI "can actually understand finance better than us … it's only data".
   - BIS [16:21]: it "can create new ideas by itself".
   Keep his own limits and remedies: "non-verbal feelings" [8:05]/[11:42]; institutions and humans in the loop [21:37]/[23:00].
   The accurate summary is: **his capability claims are unhedged; his timelines and finance scenarios are hedged.**
3. **Truth Terminal "liability ran to people".** Delete it, in the text, the diagram step and the audio. Cointelegraph says the Bitcoin went "to the bot's wallet". Say what the sources show (people donated, built and promoted it) and that they do not discuss liability.
4. **Arora toy.** The hardness is *not* the number of junk sets: in a plain pool every 10-set gives 45. Say: "with a derivative on top, the seller chooses where the junk goes; detecting that placement is the hard part (under a conjecture)". Cite p. 5 for Δ(n), and pp. 3–4 for the source of the hardness. Keep 45, 5 and C(100,10) only as the "brute force is huge but beside the point" remark.
5. **FSB merge.** "could change this in the future" refers to new-revenue use cases (pp. 28–29), not to the adequacy of frameworks (p. 2). Keep the two statements separate.
6. **Keynes merge.** § IV (convention) and § V (fail conventionally) are separate passages. Do not join them with "since".
7. **Ashby condition.** State the table condition (no outcome repeated in a column, p. 207) before the bound in Lens 2 and Rung 2. In the audio, give "only hope" with its full condition.
8. **Playground answer (2).** At loss rate 1.0, two X banks sink **five** of six, not all six. Correct the answer to "all three at 0.8; at 1.0 two sink five of six, and all three are still needed for six". Verify with check.mjs.

## B. Critic: structural changes (gate needs ≥ 4 on criteria 2–6)
1. **Answer Kunhao's question where he can find it.**
   - After the hook, add a one-line preview.
   - Define "human-centred system" once, in plain words: a system where people can understand, check and be held responsible for the rules that move money.
   - Start §13 with a boxed **Short answer** of 4–5 sentences that answers *both* halves: (a) can AI create new finance; (b) what it would mean for the current social system. Name who would bear losses, who is accountable, and what supervisors can and cannot do.
   - Then give "Our reading" and "Signs to watch". Fold layers, conditionals and critics into one `<details class="deep">`.
   - Add a `diagram` of Harari's chain (money is stories → AI masters words → AI takes over money/finance) with an evidence label on each link: asserted / hedged / supported / not yet evidenced / contested.
2. **Self-contained ladders.**
   - Move the N_eff derivation and the m = 1/A tipping argument into Lens 3, in the text or a "Look inside" fold-out. §9 must not be needed.
   - Lens 1: define "description" with an instance before the counting.
   - Lens 4: a worked principal–agent instance with named roles before Lupia–McCubbins.
   - Define variance and correlation at first use (term boxes).
   - Write the skipped lines in the remaining rungs.
3. **Vocabulary.** Give term boxes, or one-clause definitions, for high-frequency trading, circuit breaker, option, query language, memecoin and Sharpe ratio. Drop any figure whose term you do not explain.
4. **Widgets.**
   - Place `cs-w5` next to Ladder 3 and `it-herding` next to Ladder 4. Keep the Playground section only for the tasks, or merge it.
   - Seed W5 with X1, X2 and X3 by default.
   - N_eff readout: no "1/ρ" ceiling text at ρ = 0.
5. **Concision.**
   - Cut the repetition in §13.
   - Keep about 4 Harari quotes in the main text. Put the full list of his lines, with timestamps and labels, in a fold-out ("All of Harari's lines").
   - Cut Ladder 2 (one voice counted ten times) to one paragraph.
6. **Small fixes.** The §11 heading count; Exercise 4 needs a hint and a folded solution; show the one-line OQL-style contract promised in the LLM section; link each "LLM adds" item to the lens that picks it up.
7. **Audio.** Split the Lens 3 chapter in two. Simplify the dense ladder sentences. Say "variety of disturbances" instead of "V D". The Playground chapter becomes "what to try when you open the page" (do not give answers by ear).

## C. Length rule for round 2
- Main text ≤ 7,500 visible words, **excluding** `details.deep` fold-outs (up to about 1,500 more words in fold-outs).
- Clarity beats brevity: a definition the reader needs is never cut.

## D. Also fix in the brief
Unit F5 contains the same "liability ran to people" inference. Add a line to `review/response-1.md`; the meta-manager will correct the brief.
