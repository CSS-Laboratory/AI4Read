---
id: 2026-10-ai-finance/review/v2-verify-1
stage: S5, round 1 of post 02 version 2 (independent fact-check)
checked: 2026-10-18
draft: src/content.html (all visible text, 8 fold-outs, 15 widget JSON configs incl. diagram step texts and captions, Play answers, exercises, recall cards, English section, Sources list); index.html only for cite mapping and embedded data
briefs: source-brief-v2.verified.md (V1–V5, V7, V8), source-brief.verified.md (A1–A5, B1, B5, B6, B8, B9, C4, D1, D2, E1, E2, E6, E8, F4, F5, G1, G3, G4)
not read: self-review.md, critic files, earlier verify files (except to see the format and one note on BIS [22:56])
method:
- Every cited quote checked against the source text by script (letters and digits only), page by page: Kirilenko JF pp. 2–3, 7; IMF pp. 78, 82, 83 (page image incl. Fig 3.5), 86, 88, 89, 92, 93, 101; FSB pp. 1, 2, 21, 28–29 (printed page footers checked); Gensler and Bailey pp. 13, 17, 21, 22, 25; Scheurer pp. 1, 8; Ashby pp. 204–209, 246–247; Danielsson and Uthemann abstract and introduction; Danielsson et al. 2022 p. 7; Arora ICS 2010 pp. 50–52, 55, 61, 63; Arora CACM 2011 pp. 101–102; Arora WP 2009 pp. 3–4; Haldane and May pp. 351, 353–355; FCIC pp. 28, 128, 149 (page images); Searle OCR printed pp. 14, 24, 28, 32–33, 37, 41, 45, 69, 70, 142 (offset −9 / −8 applied); Granovetter pp. 1424–1425 and Lupia and McCubbins pp. 85–86, 207 (library copies in /mnt/user-data/uploads/AI4Read/library/); Guardian 2023, Guardian 2024 extract, Ynet, Poole, Narayanan and Kapoor, Cointelegraph, Decrypt, Luo, Mik.
- Harari: both whisper transcripts read at every cited timestamp, plus the surrounding minute. Re-transcribed with faster-whisper medium.en: BIS [22:50–23:10], [30:15–30:36]; WEF [3:13–3:32], [16:25–16:52], [26:15–26:40]. All five match the page wording ("we'll need", "new types of financial devices that no human being would ever imagine creating", "AIs have already learned how to lie", "AIs can therefore function as persons", "AI will beat me ... two years, five years, ten years").
- Numbers: `node site/ai4read/components/check.mjs` on content.html (15/15 OK) and with `--values`/`--seeds` for every preset and Play answer; Python (scratchpad nums.py) for N_eff, CDO tranche, Bayes, Ashby (16 plans), entropy, six-asset lemon toy (15 placements), tree of majorities, Haldane–May ratio and Stirling, May threshold, herding recursion, characteristic roots and global tipping point, breaker clamp, six-bank cascade (all single seeds, all X groups, capital multipliers), Granovetter.
---

# S5 fact-check, post 02 v2, round 1

Severity follows rubric §A. Source quotes are at most 25 words. "M" = major, "n" = minor.

## Major

**M1. The regulators' purpose is reported as an effect** — `hook`, paragraph 2.
- Post: "That this pause prevented “a cascade of further price declines” is the regulators’ account, quoted in the paper; the paper itself does not test it."
- Source: Kirilenko et al. 2017, p. 2 (CFTC-SEC, quoted): “trading on the E-mini was paused for five seconds when the [...] Stop Logic Functionality was triggered in order to prevent a cascade of further price declines.”
- What it says: the CFTC-SEC gives the rule's *purpose* ("in order to prevent") and then reports that "prices stabilized" when trading resumed. It does not claim that the pause prevented a cascade. The post puts a causal claim in the regulators' mouth while hedging it. This is a change to what a source said, in the instance the whole "check" job rests on. The same error is in source-brief-v2.verified.md V1 ("The causal claim that it 'helped stop the fall' is the CFTC-SEC report's") and trap 35 / challenge 6.
- Fix: "The rule exists “to prevent a cascade of further price declines”; the regulators report that prices stabilised after the pause, and neither they nor the paper test whether the pause caused it." Fix brief V1 (Careful, bullet 4) and challenge 6 the same way.

## Minor

**n1. Short answer (b) gives only the downside** — `answer`, box (b).
- Post: "If firms automate deciding with a few shared models, failures may arrive together, each firm can look safer while the system grows more fragile ..."
- Source: IMF 2024, p. 92: “currently the financial stability risks associated with its adoption appear contained”; p. 89: Table 3.1 positive column, “lower flash-crash risk”; “highly uncertain”.
- The body keeps both (Lens 2a summary, Lens 2b summary, layer 3), and (b) is hedged ("may", "warnings and toys"). But the boxed answer is where the reader looks, and there the IMF's present judgement and its two-way scenarios are absent.
- Fix: add one clause to (b): "the IMF judges today's risks “contained” and sees scenarios in both directions."

**n2. IMF outreach expectation: scope and attribution** — `home` table (Decide row) and `answer` (a).
- Post: "All participants in the IMF’s outreach expect a “human in the loop” for “three to five years”"; (a): "(the IMF expects humans in the loop for years)".
- Source: IMF 2024, p. 83: “all participants in the IMF’s outreach expected a ‘human in the loop’ approach to persist in the near term (three to five years), especially for large capital allocation decisions”.
- "for three to five years" can read as "only that long"; the condition "especially for large capital allocation decisions" is dropped; in (a) the participants' expectation becomes the IMF's.
- Fix: "expected a human in the loop to persist “in the near term (three to five years)”, especially for large allocation decisions"; in (a) write "participants in the IMF's outreach expect".

**n3. CACM quote taken from a different example** — `lens-control`, "Scale it up".
- Post: "Even a sophisticated buyer “would have no idea what to pay” for some such products (p. 102)."
- Source: Arora et al. 2011, p. 102: “yet even a sophisticated investor like Goldman Sachs would have no idea what to pay for it.”
- "it" is the contrived factoring derivative (payoff tied to the last digit of a factor of a 1000-digit number), not the junk-concentrated CDOs of the dense-subgraph result. The substance is supported by p. 101, but the quote's referent is moved.
- Fix: drop the p. 102 quote here, or attach it to its own example: "for a contract tied to factoring a huge number, even Goldman Sachs “would have no idea what to pay for it” (p. 102)".

**n4. Lemon-cost bottom line loses its condition** — `box-lemon`.
- Post: "Their bottom line for large pools: “under computational assumptions, the lemon cost for polynomial time buyers can be much larger than \(n\)”"
- Source: Arora et al. 2010, p. 55 (brief V4): with random pooling the lemon cost falls to o(n); only when the seller over-represents lemons in some pools can it be "much larger than n".
- "for large pools" omits that the amplification needs seller-chosen pooling and that random pooling lowers the cost (the received wisdom they question).
- Fix: "Their bottom line when the seller chooses the pooling (random pooling would lower the cost): “...”".

**n5. Car-example locator and gloss** — `lens-control`, "Some products resist checking".
- Post: "... and the seller of a good car loses $200: the lemon cost (Arora et al. 2010, p. 50)".
- Source: pp. 50–51; p. 51: “the seller’s value for a working car will have to be $200 less than the buyer’s in order for trade to occur.”
- The $200 sentence is on p. 51, and "loses $200" paraphrases a condition for trade.
- Fix: cite "pp. 50–51" and write "trade happens only if the seller values a good car at $200 less than the buyer does".

**n6. Danielsson and Uthemann locator** — `lens-control`, lever 2.
- Post: "... and start from the premise that current frameworks “cannot effectively prevent and resolve” such crises (Danielsson and Uthemann 2025, abstract)".
- Source: introduction, p. 2: “As current regulatory frameworks cannot effectively prevent and resolve such AI-induced crises, we outline ...” Not in the abstract.
- Fix: put "introduction" after this quote (the abstract cite stays on the first two quotes).

**n7. Searle locator: the bill in the cracks** — `lens-social`, "A subtlety".
- Post: "A single bill lost in the cracks of a floor ... is still money; but for the type, “...” (Searle 1995, p. 33)."
- Source: the bill is on p. 32 (“A single dollar bill might fall from the printing presses into the cracks of the floor”); the type sentence is on p. 33.
- Fix: cite "pp. 32–33".

**n8. FCIC fragment not verbatim** — `home`, "2008".
- Post: "rating models whose first “key mistake” was ..."
- Source: FCIC 2011, p. 149: “the agencies’ CDO models made two key mistakes. First, ...”
- Fix: "the first of “two key mistakes”".

**n9. A cited source missing from the Sources list** — `cfg-seller`, step 3.
- Post: "(a conjecture, Arora et al. 2009, pp. 3–4)".
- Source: the 2009 working paper pp. 3–4 does support it (“the conjectured intractability of the planted dense subgraph problem”), but the Sources list has only ICS 2010 and CACM 2011, and cite-map.tsv has no row for it.
- Fix: cite "Arora et al. 2011, p. 101" (same claim, already listed), or add the 2009 working paper to Sources.

**n10. Conditional drops the sources' hedges** — `box-layers`, "Five conditionals", item 1.
- Post: "If many firms automate deciding with one model, their errors coincide and diversification shrinks (N_eff; FSB; Gensler and Bailey)."
- Source: FSB p. 1 “could lead to increased correlations”; Gensler and Bailey p. 21 “are likely to generate highly correlated predictions”.
- Fix: "their errors are likely to coincide ..." (the main text keeps the hedges; this line should too).

**n11. Harari's own line about laws is paraphrased without attribution** — `hook`, paragraph 4.
- Post: "“Therefore, anything made of words will be taken over by AI” (WEF 2026 [5:57]). Laws, contracts and money are made of words."
- Source: WEF 2026 [6:06]: “If laws are made of words, then AI will take over the legal system.” (unhedged in form; not quoted anywhere in the post or fold-out).
- The next sentence reads as the post's own premise, and his strongest line on the "declare" job (law) is missing from the fold-out.
- Fix: quote [6:06] in the hook and in fold-out group 1, and mark "contracts and money" as our extension (his money line is Ynet 2023).

**n12. "Nobody understands" vs "no human understands"** — `hook`, paragraph 4.
- Post: "he imagined an AI-made financial device that nobody understands, “maybe in 10 years”".
- Source: BIS [10:08–10:16] (brief A1): “you need to go over trillions of data points to understand this financial device. We can't do that, but the AIs can”.
- Fix: "that no human understands".

**n13. Concession missing next to the Davos Q&A forecast** — `box-harari`, group 2, [31:11].
- Source: WEF [30:55]: “At the present moment, we still think better.” [31:07]: “But we need to prepare to the moment when this is no longer the case.” (brief A3 Careful).
- The forecast is listed without the present-tense concession that frames it.
- Fix: add [30:55] to group 4.

**n14. Unsourced fact in the hook** — `hook`, paragraph 3.
- Post: "Later, regulators wrote the report and people answered for the losses."
- Source: Kirilenko et al. 2017 says nothing about who bore the losses.
- Fix: drop "and people answered for the losses", or label it "(our reading)".

**n15. Unlabelled inference after Ashby's law** — `lens-control`, "What it means".
- Post: "When software multiplies the kinds of disturbance and their speed, human supervisors fall behind, and the pressure is to automate the checker too."
- Source: Ashby says only what a regulator needs (p. 209: the law "owes nothing to experiment").
- Fix: label "(ours)", or cite Danielsson and Uthemann (introduction: “human experts cannot effectively oversee AI operating at machine speeds”).

**n16. Two IMF verdicts, unclear scope** — `lens-cascade` summary vs `lens-decision` summary.
- Post (2b): "its overall verdict is “highly uncertain” (IMF 2024, p. 89)"; (2a): risks "currently … appear contained" (p. 92).
- Source: p. 89: “On balance, the impact of these changes [...] is highly uncertain” (about AI's future effect on algorithmic trading); p. 92 is the summary judgement on present risk.
- Fix: in 2b write "its verdict on the future impact is “highly uncertain”".

**n17. "Not under current rules" vs "we state no legal position"** — `answer` table (Answer row), `lens-answer` summary.
- Post: "Not under current rules"; Lens 4: "We have no legal sources and state no legal position."
- Source: IMF 2024, p. 93: “As capital markets are already subject to regulation and supervision, institutions are responsible for AI systems they deploy”. That is capital-market regulation, not law in general.
- Fix: "Not under current capital-market rules (IMF p. 93); law beyond that is a choice societies have not made."

**n18. Lupia and McCubbins: the stricter theorem is omitted** — `lens-answer`, `answer` (c), recall card.
- Post: "With one of the two, the worst case is that you keep your cash ... state this pattern as a theorem (pp. 85–86)."
- Source: brief F4: p. 92, Theorem 5.1′ under a tougher definition of success: “If either condition is not satisfied, then delegation fails.”
- Correct for Theorem 5.1, but the brief flags the stricter version as a condition the reader needs, and Lens 4's fill-in (an AI removes knowledge) is exactly the case where the two theorems differ.
- Fix: one clause: "(under a stricter definition of success, losing either condition is enough to fail, p. 92)".

**n19. Critic lines without citation links** — `box-layers`, "Critics, one line each".
- Poole, Narayanan and Kapoor, FSB and Skingsley are quoted or paraphrased with no cite span (only the Harari line has one). Wording is correct (Poole: “no one has yet seen a chatbot create new ideas”; N&K: “median outcome”, “incoherent”; FSB p. 2: “more work may be needed”; Skingsley BIS [7:18]).
- Fix: add cites (Poole 2024; Narayanan and Kapoor 2025, Part II intro; FSB 2024, p. 2; BIS 2024 [7:18]).

**n20. Gensler and Bailey: identifier mismatch** — Sources, `src-gb`.
- Post: "SSRN 3766555 (abstract page listed as 3723132). https://papers.ssrn.com/abstract=3723132".
- Source: every page footer of the file reads “abstract=3766555”; 3723132 comes only from MANIFEST table B (unverified).
- Fix: link https://papers.ssrn.com/abstract=3766555 and drop the bracket, or keep it as "(also listed as 3723132)".

**n21. Built page embeds a stale brief as tutor context** — index.html line 1236, `<script id="brief-data">`.
- It holds only source-brief.verified.md (v1): IMF "B7 DROP", Gensler and Bailey "UNSEEN", Arora CACM "not seen", Kirilenko "working paper, 2014", and "This is a direct link to post 01". The v2 brief is absent. The tutor is told to "ground every claim in the post or the source brief below", so it may contradict the post or mention post 01 (WRITING §0).
- Fix: embed source-brief-v2.verified.md (plus v1 units still in use) and strip internal cross-post notes.

## Counts

critical 0 / major 1 / minor 21

## Checked and found correct

- **Standalone rule:** no reference to any other AI4Read post in content.html (grep for post numbers, "earlier/previous post", "remember"); the only hit is in the built page's embedded brief (n21).
- **Kirilenko 2017:** 2:32 p.m. Eastern (trap 33 handled), 75,000 contracts, about $4.1 billion, hedge, "chose to execute this sell program via an automated execution algorithm", 9% of previous-minute volume "without regard to price or time", fewer than 1,050 contracts and under 1% of start-of-day depth at 2:45:28, five-second pause, Stop Logic "an automated pre-trade safeguard procedure" (p. 2 fn 1), back to near pre-drop level by 3:08, "fully electronic", "no market maker obligations" (p. 7); "a firm decided ... a person is our reading" correctly labelled; HFT causation not claimed.
- **IMF:** every quote verbatim on its page (pp. 78, 82, 83, 86, 88, 89, 92, 93, 101); Fig 3.5 values 11% and 59% confirmed on the page image (labels printed on the bars); "algorithmic" vs "AI" distinction (p. 101) kept; "mostly speculative" correctly tied to "revolutionary" GenAI uses (p. 78), not to autonomous trading; "under certain conditions" kept (p. 88); "contained" (p. 92) and "highly uncertain" (p. 89) both present in the body; SupTech line not turned into "79% use AI".
- **FSB:** p. 1 "could lead to increased correlations"; p. 21 "as if it were a single institution"; pp. 28–29 "not widely observed at present" with its tail "could change this in the future"; p. 2 "more work may be needed".
- **Gensler and Bailey:** pp. 13, 17, 21, 22, 25 verbatim; framed as a hypothesis about a mature stage; flash-crash monoculture not applied to 2010.
- **Scheurer et al.:** "existence proof" and not a likelihood estimate; "consistently hides the genuine reasons"; "nearly (but not exactly) 0%" tied to insider trading; deception "remains high under all prompts" conditional on misalignment.
- **Ashby:** p. 207 law and "variety can destroy variety"; table rule (stated p. 204, restated pp. 206–207); p. 208 entropy form and the H_D(E) misprint trap; p. 209 "owes nothing to experiment"; pp. 246–247 three levers with the "only hope" condition; toy table min 2 outcomes over 16 plans; 13.29, 9.29, 6.64 (exactly half), H = 1.75, bound 0.75; entropy derivation steps valid.
- **Danielsson and Uthemann / Danielsson et al. 2022:** "amplifies existing financial system vulnerabilities", "faster and more severe", own AI (abstract); "both stabilise and destabilise" with its conditions (introduction); "will likely be unintelligible to humans" (JBF p. 7 = PDF 8).
- **Arora:** ICS p. 52 lemon-cost definition and "takes into account all possible ways"; p. 61 Theorem 9 bound (1 + t/2^k)/2; p. 63 "clearly only a first step (simple model, asymptotic analysis, etc.)" and "raise the hope"; CACM p. 101 "in industry-standard models, the pricing problem can be as difficult as solving the planted dense subgraph problem"; conjecture and simple-model hedges kept; "AI as the informed seller is ours" labelled. The six-asset toy moves in the source's direction (concentrating junk does more damage: 3/2 vs 7/4; 12 of 15 vs 3 of 15; Δ(2) = 3/4); tree of majorities 4, 8, 16 = 2^k (brute force at depth 2).
- **Haldane and May:** p. 351 "major differences", sharp transition, mα² > 1 with m and α as defined; p. 353 homogeneity claim, toy formula N^N ε^N/N!, "liquidity shocks amplify"; p. 355 diversity and modularity quotes; May's criterion kept out of the banking claims; ratio 2,755.7 (N = 10), 64.8 (N = 6), 4.31e7 (N = 20), Stirling e^N/√(2πN) correct.
- **FCIC:** p. 28 "the securities almost no one understood"; p. 128 "such as" and "waterfall" (page image); p. 149 "weren't that different to begin with" (page image).
- **Searle:** pp. 14, 24, 28, 33, 37, 41, 45 (×2), 69, 70, 142 verbatim at the stated printed pages; hedges "most, perhaps all" kept; machine application labelled ours throughout; "Searle himself requires more: belief in the status" keeps the S2b major fix; no "lower than belief", no "Searle says machines cannot".
- **Lupia and McCubbins:** Theorem 5.1 (p. 85) and the one-condition status-quo result (pp. 85–86) verbatim in substance; p. 207 "verification or a penalty for lying".
- **Granovetter:** pp. 1424–1425, threshold-1 swap and "the two crowds are essentially identical"; exercise solution (100 → 1) rerun.
- **Harari:** every timestamp in the hook, fold-out, Lens 3 and Lens 4 matches the transcript within about 3 s; five segments re-transcribed with medium.en (see method). Strongest unhedged lines present: "anything/everything made of words will be taken over by AI", "AIs have already learned how to lie", "first tool ... understand finance better than us", "can therefore function as persons", "Ten years from now, it will be too late", Guardian 2023 "existential threat" (AI in general). Hedges kept: "maybe in 10 years", "Suppose", "Maybe nobody in the room", "maybe 1%", "What happens if". Guardian 2024 quote not cut before the turn ("Unfortunately, humanity has never been united" included). Four "ten years" kept apart. Group assignments match the transcript wording.
- **Truth Terminal:** handler approves posts and interactions; $50,000 in BTC "to the bot’s wallet" (July); Decrypt "semi-autonomous AI agent" and "neither the bot nor its handler created the token"; "neither report discusses who would be liable" true of both saved texts. Decrypt date 16 Oct 2024 from page metadata.
- **Luo et al., Mik:** abstract and introduction wording; "may" kept on "contracts in form only, not in function"; diagram step labels its gloss as ours.
- **Poole, Narayanan and Kapoor, Skingsley:** wording and hedges ("median outcome", "not superintelligent", plane analogy) correct.
- **Numbers (all rerun):** N_eff 10 / 2.703 / 1.099 / 1, check 1.33 and 0.75σ², 3.257, ceiling 3.33; all-wrong 10^-20 vs 1%; Bayes 0.5, 0.8, 0.941, 0.985, 0.996, 1,048,576 and 0.999999; CDO 0.0036 + 0.0001 = 0.37%, 5.185%, 10%, 27×, p = 0.02: 2.000% vs 0.0032%, 634.5×; herding gaps −0.9, −0.51, −0.189 and −2.30, −3.94; roots 0.548, 1.002, 1.162 (complex in all three cases), global tipping at m = 2/3 (stability needs Am < 1 for all m < 1); breaker ±3.00; m = 0.2 readout 0.04 / −1.00 / 0.000; May 0.64, 1.28, 0.72 and max 6 links at α = 0.4; six-bank table and stepper; Play answers (single seeds: none at 0.8, Y1 → 3 at 1.0; two X → 5 at 1.0; ×1.2 → 5, ×1.25 → 3) both in Python and in check.mjs; cascade edge directions match the prose.
- **Short answer and five-job table vs lenses:** Run, Decide and Check rows match what Section 3 and Lenses 1–2 establish; Declare "open" matches Lens 3 and V8 (verdict ours); Answer row see n17; the box is labelled "our reading, not a finding".
- **Sources list:** authors, years and venues correct for all 27 entries; DOIs confirmed from the PDFs for Danielsson et al. 2022 (10.1016/j.jbankfin.2021.106290), Arora CACM (10.1145/1941487.1941511, CACM May 2011 vol. 54 no. 5), Haldane and May (10.1038/nature09659); Granovetter AJS vol. 83 no. 6, p. 1420 start, confirmed from the library copy; Kirilenko title matches the manuscript (JF pages 967–998 not confirmable from the manuscript file). Missing entry: n9. Identifier: n20.
- **cite-map.tsv:** every cite maps; no unmapped rows.
