---
id: 2026-10-ai-finance/review/v2-verify-3
stage: S5, round 3 (final) of post 02 version 2 (independent fact-check, Opus)
checked: 2026-10-18
draft: src/content.html, 653 lines, modified 18:37 (110,310 bytes). The file changed during this check (it was 18:29 when I started); every finding and every "correct" item below refers to the 18:37 text. I checked all visible text, every fold-out, all 15 widget JSON configs (step texts, notes, captions), the new two-bank SVG figure, quiz options and reveals, Play answers, exercises, recall cards, English section and Sources.
round-2 inputs: review/v2-verify-2.md (Opus 0/2/17), review/v2-verify-2b.md (Sonnet 0/2/22), review/v2-critic-2.md, review/v2-response-2.md
method:
- Quotes matched against the source text, page by page. Kirilenko et al. 2017 manuscript pp. 2, 3, 7. IMF printed pp. 78, 82, 83, 86, 88, 89, 92, 93, 101 (PDF + 76; footers read). FSB pp. 1, 2, 21. Gensler and Bailey pp. 2, 13, 17, 21, 22, 25. Danielsson and Uthemann: abstract, introduction, §3.1, p. 10. Danielsson et al. 2022 p. 7. Arora CACM pp. 101–102 (PDF + 100). Arora ICS pp. 50–52, 55, 61–63 (PDF + 48). Haldane and May pp. 351, 353, 355, ref. 4. Ashby pp. 204–209, 246–247 (two book pages per sheet; footers read). Searle OCR (printed = OCR − 9 to p. 57, then − 8): pp. 14, 24, 28, 32–33, 37, 41, 45, 56, 69, 70, 84, 140–142, 168. Library copies: Lupia and McCubbins pp. 79, 85–86, 91–92; Granovetter pp. 1424–1425. Also FCIC pp. 28 and 149, Scheurer p. 1, Luo, Mik, Cointelegraph, Decrypt, Guardian 2023, Guardian 2024 extract, Ynet, Poole, and Narayanan and Kapoor.
- Harari and Skingsley: every timestamp in the post checked against both whisper transcripts. No new audio run; "we'll need" at BIS [22:56] and the [30:24] wording rest on the earlier medium.en re-runs.
- Numbers: `node site/ai4read/components/check.mjs posts/2026-10-ai-finance/src/content.html` gives 15/15 OK on the 18:37 file. I ran `--id/--values/--seeds` for every preset and every Play answer, and Python (scratchpad n3.py) for the rest.
- No Nexus file was used.
---

# S5 fact-check, post 02 v2, round 3 (final)

Severity follows rubric §A. Source quotes are at most 25 words.

## Critical (0)

None.

## Major (0)

None. All four round-2 majors are fixed correctly (see the verification section).

## Minor (12)

**n1. "Only" is still false in the Searle reveal** (`reveal` g3; residual of round-2 Sonnet m7)
- Post: "he mentions computers only as artifacts and as models of human cognition, pp. 14, 140–141".
- Source: Searle 1995, p. 56: money needs "some physical realization … even if it is only a bit of paper or a blip on a computer disk". Computers also appear on p. 84 (property) and p. 168 (realism).
- Why it matters: p. 56 is the one place where Searle says money's X term can be digital, which bears directly on Prediction 3.
- Fix: drop "only" and add p. 56: "computers appear as artifacts (p. 14), as one possible physical form of money, 'a blip on a computer disk' (p. 56), and as models of cognition (pp. 140–141)".

**n2. The Narayanan and Kapoor quote is attached to the wrong noun** (`box-layers`, critics; introduced by the round-2 m16 fix)
- Post: "adoption is slow (“on the timescale of decades”)".
- Source: introduction: "transformative economic and societal impacts will be slow (on the timescale of decades)". The authors also say that methods, applications and adoption "happen at different timescales".
- The round-1 wording ("impacts are slow") was right. The present tense also turns their forecast ("will be") into a statement of fact.
- Fix: "transformative economic and societal impacts will be slow (“on the timescale of decades”)".

**n3. A widget step still cites CACM p. 101 for the conjecture** (`cfg-seller` step 3; residual of round-2 Sonnet m4)
- Post: "finding the few where junk was concentrated is the hard part (a conjecture; Arora et al. 2011, p. 101)".
- Source: CACM p. 102: "Our result relies on the conjecture that there does not exist a tractable algorithm to detect large dense subgraphs". The main text already cites p. 102.
- Fix: "p. 102".

**n4. The gloss on "liquidity shocks" describes a different mechanism** (`lens-cascade`, Ladder 3, "What it means")
- Post: "“liquidity shocks” (banks suddenly unable to borrow cash) “amplify as more banks fail”".
- Source: Haldane and May 2011, p. 353. The shocks that "amplify as more banks fail" are market liquidity shocks: "discount factors that, for a given asset class, are proportional to the number of failing banks holding the asset". Being unable to borrow is their separate "third mechanism", "funding liquidity shocks".
- The main text also no longer gives the contrast ("in sharp contrast to the attenuation in interbank loan shocks"); only the May fold-out keeps it.
- Fix: "(falls in the prices of assets that failing banks hold)". Optionally add "unlike losses on loans, which more links soften".

**n5. The broker toy's two definitions of success are not Lupia and McCubbins'** (`lens-answer`, Mechanism)
- Post: "Here delegation “succeeds” if you never end up below your cash"; "If success means getting the good bond, losing either condition is enough to fail <cite p. 92>".
- Source, Lupia and McCubbins 1998:
  - p. 79: "delegation succeeds when an agent's actions improve a principal's welfare"; keeping the status quo is "no effect" (p. 3).
  - pp. 91–92: the tougher definition requires that the agent's actions "enhance the principal's welfare by more than K", where K is the cost of delegating.
- The toy calls the status quo a success, which the authors do not. The p. 92 sentence drops K, which is the reason the stricter theorem holds.
- Fix: "As in Lupia and McCubbins, delegation succeeds if you end up above your cash and fails if you end up below it; keeping your cash is ‘no effect’ (p. 79)", and "If success must also cover the cost of delegating, losing either condition is enough to fail (p. 92)."

**n6. Danielsson and Uthemann's two-sided finding was cut** (`lens-control`, lever 2; Balance check)
- Post: "In a game-theoretic model, Danielsson and Uthemann find that AI “amplifies existing financial system vulnerabilities” and makes crises “faster and more severe”".
- Source: introduction: the model finds AI "can both stabilise and destabilise the financial system, depending on the severity of the shocks it faces and how prepared the financial authorities are". The abstract adds: "the likelihood of a crisis is directly affected by how effectively the authorities engage with AI".
- The quoted words are verbatim from the abstract, but the condition and the stabilising side were removed this round, as a concision cut. As a result the authors read as more one-sided than they are.
- I kept this minor, not major, because the next sentence ("So they propose that authorities build their own AI") partly carries the condition.
- Fix: add ", and that how likely a crisis is depends on “how effectively the authorities engage with AI” (abstract)".

**n7. Our extension is credited to Lens 1** (`answer` (b), "Who gains and who bears")
- Post: "power would tend to move to whoever writes the models and the rules, since the regulator with more variety sets the terms for the rest (Lens 1)".
- Source: Ashby's law (pp. 206–207) is about how a regulator's variety limits the outcomes that disturbances cause. Neither Ashby nor Lens 1 says that one party's variety lets it set terms for other parties.
- The "(ours)" label covers the sentence, but the pointer presents the step as something Lens 1 shows.
- Fix: "(our extension of Ashby’s law, Lens 1)".

**n8. IMF Decide row: "mostly" and "All participants" overstate the source** (`home`, table, Decide row)
- Post: "it mostly feeds a signal to a system where …" and "All participants … expected a 'human in the loop' … while expecting more AI in investment and trading decisions over the same horizon <cite p. 82>".
- Source: p. 82: "It is instead more frequently used to generate a signal", a comparison, not "mostly". The p. 82 forecast belongs to "participants", not "all participants"; "all participants" is p. 83's wording for the human-in-the-loop expectation.
- Fix: "it is more often used to feed a signal into a system where …", and start a new clause: "Participants also expect more AI in investment and trading decisions over the same horizon (p. 82)."

**n9. "A pre-set rule checked the fall" reads as an effect** (`hook`, paragraph 3)
- In English, "checked the fall" means "halted the fall". That is an effect claim (WRITING §9, purpose ≠ effect), and it comes one paragraph after "The quoted passage does not say the pause caused this, and the paper does not test it" (Kirilenko et al. 2017, pp. 2–3).
- Fix: "A pre-set rule did the <i>checking</i>: it paused trading."

**n10. Two sources in one cited sentence** (`lens-control`, lever 2; WRITING §9)
- Post: "A supervisor’s own model “may unknowingly promote uniformity …” <cite Gensler and Bailey 2020, p. 25>, and an AI’s knowledge of the system “will likely be unintelligible to humans” <cite Danielsson et al. 2022, p. 7>."
- Both quotes are verbatim and on the cited pages; only the one-source-per-sentence rule is broken.
- Fix: split the sentence at "and".

**n11. Ashby's no-repeat rule is a restriction he chooses, not a property of all his tables** (`lens-control`, Mechanism)
- Post: "Ashby’s tables assume that in each column (each check), no state appears twice <cite p. 207>".
- Source: Ashby 1956, p. 205 (S.11/5): "let us consider, then, only those tables in which no column contains a repeated outcome". His own Table 11/4/1 (p. 204) has repeats. P. 207 restates "the condition introduced in S.11/5".
- Fix: "Ashby states his law for tables in which, in each column (each check), no state appears twice (pp. 205, 207)".

**n12. The general step of the two-bank derivation lost its density factor** (`lens-cascade`, Ladder 4, Formula)
- Post: "the triangle becomes a corner of an N-dimensional cube …, with volume \((Nc)^N/N!\). So plan B fails with chance \(N^N\varepsilon^N/N!\)".
- The round-2 text had "each unit of volume has chance \((\varepsilon/c)^N\)". Without it, "So" does not follow, because the volume still carries \(c^N\).
- The N = 2 bullet still states the density, so the arithmetic is right. Only the stated step is missing.
- Fix: restore "and each unit of volume has chance \((\varepsilon/c)^N\)" before "So".

## Counts

critical 0 / major 0 / minor 12

Rubric criterion 1: 0 major and 12 minor findings, which is more than five minors, so criterion 1 is 3 by the table. Every fix is one phrase or one sentence. n1, n2, n4, n5 and n6 are the ones that change what a source is reported to say.

## Round-2 findings: verification

**Opus round 2 (v2-verify-2):**
- **M1** (AI vs rule-based software in (a)): fixed correctly. (a) now says "mostly by rule-based software rather than AI … AI deciding at scale is mostly not here yet". The Run row says "on rules written by people".
- **M2** (two routes to the incentive condition): fixed correctly.
  - The instance names common interests and outside forces.
  - "Applied to AI" quotes p. 85 ("external forces") and Danielsson and Uthemann §3.1, p. 10 ("lose traction …", verbatim, p. 10).
  - The lens summary reads "from its objective or from pressure on its deployer".
- **n1** fixed ("find a constraint, and regulation may become possible; imposing one … is our mapping").
- **n2** fixed (conditional, users' gains, IMF "lower flash-crash risk"). The new "(Lens 1)" pointer is n7 here.
- **n3** fixed (condition and full clause at [3:09], [3:30]).
- **n4** fixed (§3, p. 10, confirmed in §3.1).
- **n5** fixed ("neither know the rules nor apply them, consciously or unconsciously").
- **n6** fixed ("restating his point, she grants").
- **n7** fixed for "as usually conceptualized"; see n2 here.
- **n8** fixed ("worse than your cash: 90").
- **n9** fixed ("Accountability", "In organisations and regulators").
- **n10** fixed (Lens 4 "most participants in the IMF’s outreach"; English "Most firms the IMF asked"; Signs "the outreach participants’ expected …").
- **n11** fixed ("in our question’s words", no quotation marks).
- **n12** fixed ("one of the most automated corners"; "among the places … (our judgement)").
- **n13** fixed ("paused trading during the 2010 crash").
- **n14** fixed ("The quoted passage does not say the pause caused this").
- **n15** fixed. The text now says "the triangle below the slanted line", and the new SVG figure is geometrically right: the triangle is (0,0), (0,2c), (2c,0), and the plan-A square is [0,c]², area c² against 2c². \(N\varepsilon\le1\) is stated.
- **n16** fixed (p. 82 expectation added; scope slip n8).
- **n17** fixed.
  - index.html and cite-map.tsv were rebuilt at 18:37, the same time as content.html; cite-map has 148 rows and 0 unmapped.
  - numbers.md has the two-bank, broker, Haldane–May and pyramid rows.
  - The tutor brief opens with "Updates after S5", which marks CACM as seen, supersedes v1 B7, E3 and Kirilenko 2014, and states purpose vs effect.

**Sonnet round 2 (v2-verify-2b):**
- **M1** fixed. **M2** fixed.
- **m1** fixed ("By 2:45 p.m. … less than 1% of their level at the start of the day").
- **m2** fixed. **m3** fixed (algorithmic trading vs AI split).
- **m4** partly fixed: main text p. 102; the step text is n3.
- **m5** fixed ("may resist" in the heading, layer 2 and the lens summary).
- **m6** fixed (a, a, c, c; also checked by code).
- **m7** partly fixed: see n1.
- **m8** fixed. **m9** fixed (chair, bathtub, computer; "our contrast").
- **m10** fixed ("through penalties for lying (our reading)").
- **m11** fixed (both sentences labelled).
- **m12** fixed. **m13** fixed (recall card; (c) now says "knowledge and … an incentive").
- **m14** fixed ("appear contained" in (b), layer 3 and the English pattern).
- **m15** fixed (the absolute is gone).
- **m16** "as usually conceptualized" fixed; "adoption is slow" is a misquote (n2). The round-2 suggestion itself had the wrong noun.
- **m17** fixed. **m18** fixed. **m19** fixed ("two sentences later" is correct: one sentence lies between).
- **m20** fixed (date dropped). **m21** fixed (m < 0.067: real roots, both below 1).
- **m22** fixed (notebook headers now say Lens 2a and Lens 2b, Ladder 5; no "W5").

**Critic items with factual content (v2-critic-2):**
- F6: the counter-case is present and labelled ours.
- F7: the figure was added (correct) and the N = 3 pyramid is right (27c³/6 = 4.5c³), but the density step was lost (n12).
- F8: the Check now tests the toy, and the stated outcome is right under Theorem 5.1 (pp. 85–86).
- F5: the preview and (c) were rewritten. "contest" is now grounded as "our reading of Searle" (p. 45 continued acceptance), which is labelled correctly.

## Checked and found correct

**Hook.** All of these match Kirilenko et al. p. 2 (fn. 1) and p. 3:
- "a mutual fund complex"; "approximately $4.1 billion"; "as a hedge"; "chose to execute this sell program via an automated execution algorithm"; "without regard to price or time"; 9% of volume (rendered as "a fixed share").
- "less than 1% of buy-side market depth observed at the beginning of the day" by 2:45:28; paused "for five seconds".
- "an automated pre-trade safeguard procedure"; "in order to prevent a cascade of further price declines" (purpose, correctly reported); "prices stabilized" (the report as quoted).
- By 3:08, "back to nearly their pre-drop level" (≈ 23 min, so "about twenty minutes" holds).

**Five jobs table.**
- p. 7 (manuscript): "no market maker obligations in the fully electronic E-mini".
- IMF p. 86: "In the United States … about 70 percent of equities trading and more than half of futures trading".
- p. 82: "Concentrating on the more specialized area of algorithmic trading, evidence is mixed"; "sophisticated AI has not yet been implemented widely to build autonomous AI trading agents"; "a human trader may ultimately make the trading decision".
- p. 83: "all participants … expected a 'human in the loop' approach to persist in the near term (three to five years)"; "use AI-driven SupTech tools".
- p. 93: "institutions are responsible for AI systems they deploy". p. 101: definition and "in its simplest guise … basic trading rules".

**FCIC.** p. 28 "the securities almost no one understood" (PDF 57). p. 149 "two key mistakes" and "weren't that different to begin with" (PDF 178).

**§4.**
- Luo abstract: "translating natural-language trading intents into correct option strategies remains challenging"; "validated and executed deterministically by an engine".
- Mik: "may turn out to be contracts in form only, not in function".
- Cointelegraph: the handler only approves posts; "sent $50,000 worth of Bitcoin (BTC) to the bot’s wallet". Decrypt: "semi-autonomous AI agent"; "neither the bot nor its handler created the token".
- Gensler and Bailey p. 21 is verbatim.
- Scheurer p. 1: "consistently hides the genuine reasons"; "we do not aim to draw conclusions about the likelihood … existence proof".
- IMF p. 78: "revolutionary" uses "remain mostly speculative".

**Lens 1.**
- The Ashby toy: the minimum over all 16 plans is 2 outcomes, and only a, a, c, c and its relabellings reach it. The new "4/2 = 2" step matches Ashby's r/c bound (p. 206).
- Ashby quotes: p. 207 "Only variety in R can force down the variety due to D; variety can destroy variety"; p. 209 "owes nothing to experiment"; p. 246 "ways that may make regulation possible" and "a somewhat trivial solution"; p. 247 "only hope" with its condition.
- Numbers: 13.29, 9.29, 6.64 and 4.29. H(D) = 1.75 with bound 0.75. Cover and Thomas Thm 2.6.5 (round-2 library check stands). The Ashby caption pp. 206–207 is right.
- Danielsson and Uthemann: abstract "amplifies …", "faster and more severe", "develop their own AI systems"; §3.1, p. 10 "human experts cannot effectively oversee AI operating at machine speeds" (see n6 for balance).
- Gensler and Bailey p. 25 "may unknowingly promote uniformity in the agents they regulate". Danielsson et al. 2022 p. 7 "will likely be unintelligible to humans".
- Arora CACM p. 101: "even in industry-standard models, the pricing problem can be as difficult as solving the planted dense subgraph problem". p. 102: the conjecture and "computationally intractable". The referent is the realistic derivatives, not the factoring example.
- Arora ICS: pp. 50–51 lemon car; p. 52 Δ(n) and "position"; p. 55 "much larger than n"; p. 61 Theorem 9 bound (1 + t/2^k)/2; pp. 61–62 Theorem 10 and "currently does not exist"; p. 63 "clearly only a first step (simple model, asymptotic analysis, etc.)". "hope that better design could at least stop tampering" is a fair paraphrase of "raise the hope that it may be possible to circumvent at least the tampering problem with better design".
- The new main-text sentence "Concentrating the junk … costs the buyer more than spreading it" points the same way as the source and the toy (7/4 vs 3/2; 12 vs 3 of 15; Δ(2) = 3/4). The tree toy needs 4, 8 and 16 flips.

**Lens 2a.**
- Gensler and Bailey: p. 17 monoculture; p. 2 "hypothesize … more mature stage of broad adoption"; p. 22 "models with similar methodologies".
- FSB p. 21: "Shocks that act upon a segment … using the same models and data could affect the segment as if it were a single institution".
- IMF p. 92 "currently the financial stability risks associated with its adoption appear contained"; p. 93 "may herd …".
- N_eff 2.703, 1.099, 3.257; ceiling 3.33; check 1.33 / 0.75σ². Bayes 0.5 … 0.996; 1,048,576; 0.999999. CDO 0.0036, 0.0001, 0.37%, 5.185%, 10% (27.0×); p = 0.02 gives 2.000% vs 0.0032% (634.5×).

**Lens 2b.**
- Six banks: rounds 12/10, 12/9, 12/11 and 6 of 6 in 3 rounds. Single seeds: 1 failure each at 0.8; at 1.0 Y1 gives 3 of 6. Two X: 2 of 6 at 0.8, 5 of 6 at 1.0. Capital ×1.2 gives 5; ×1.21, ×1.25 and ×1.5 give 3. lgd 1 gives 6. Every Play answer is right.
- Haldane and May p. 351: "major differences", "sharp transition", mα² > 1 (May 1972 = their ref. 4).
- p. 353: the toy setup, "all the banks doing the same thing … minimize risk … maximize the probability", N^N ε^N/N!, "high connectivity distributes, and thereby attenuates risk".
- p. 355: "this systemic diversity objective should probably be given much greater prominence" (hedge kept) and "Modular configurations …".
- Two-bank Monte Carlo (4M draws): N = 2, ε = 0.1 gives 0.0199 (formula 0.02); N = 3 gives 0.00447 (0.0045). At ε = 0.01: 0.01 → 0.0002 and 0.0001 → 0.0002.
- Presets: N = 6 gives 65 (64.8), N = 10 gives 2,756 (Stirling 2,779), N = 20 gives 43,099,804. May: 0.64, 1.28, 0.72; max 6 and 11 links.
- Trend toy: −0.9, −0.51, −0.189 and −2.30, −3.94; m = 0.2 readout 0.04 / −1.00 / 0.000; breaker ±3.00; root sizes 0.548, 1.002, 1.162. Real roots exist for m < 0.067 and m > 0.933 (m = 0.95 gives 1.32 and 1.08). The tip is at 2/3.

**Lens 3.** Searle at the stated printed pages:
- p. 14 (chairs, bathtubs, computers; "never intrinsic … conscious observers and users"); p. 24 "biologically primitive phenomenon"; p. 28 "X counts as Y in context C"; pp. 32–33 the bill in the cracks and "the type is a type of money is constitutive".
- p. 37 "most, perhaps all" (hedge kept); p. 41 "imposition of a collectively recognized status"; p. 45 (×2); p. 69; p. 70 dog; p. 142 "do not know those rules … consciously or unconsciously … a set of dispositions".
- Ynet money line verbatim. The applications to machines are labelled ours.

**Lens 4.**
- Lupia and McCubbins p. 85: the knowledge and incentive conditions, including "common interests or … external forces". Theorem 5.1 and "the worst that can happen … is the retention of the status quo" (pp. 85–86). Theorem 5.1′ "If either condition is not satisfied, then delegation fails" (p. 92).
- Scheurer abstract. IMF p. 78 "liability" among the reasons of "most participants". Gensler and Bailey p. 13.
- Harari WEF [15:14], [16:27]/[16:36], [16:47] verbatim. "We have no legal sources" is honest.

**Short answer, tension, signs, layers, critics.**
- IMF Table 3.1 (p. 89) positive column: "lower flash-crash risk". p. 89 "highly uncertain".
- Harari [3:09]–[3:30]. Skingsley [7:18] airplane and [7:35] restatement.
- Harari [21:37] institutions and [22:56] "we’ll need to keep humans in the loop". Guardian 2024: "Unfortunately, humanity has never been united" followed two sentences later by "The rise of AI …".
- Poole verbatim. Narayanan and Kapoor: "incoherent as usually conceptualized", "primarily in the hands of people and organizations", "median outcome" (n2 aside). FSB p. 2 "more work may be needed".

**Harari fold-out (balance check).**
- Every timestamp is within 3 s of the transcripts.
- The strongest unhedged lines are present: "anything made of words will be taken over by AI", "AIs have already learned how to lie", "understand finance better than us", "can therefore function as persons", "Ten years from now, it will be too late".
- The hedges and concessions are present: [3:00] "maybe 1%", [8:41] condition, [9:21] concession, [30:55], the Guardian 2023 "catastrophic … not existential".
- The four "ten years" are kept apart. No separate passages are joined. Guardian 2023, 2024 and Ynet quotes are verbatim.

**Grep and build checks.**
- **Standalone (WRITING §0):** no sentence in content.html refers to another AI4Read post. "Lens 2a estimated" and "section 7" are internal pointers.
- **Tutor brief** (index.html `brief-data`, 18:37): no reference to another post, and nothing that overrides the post. Its "Updates after S5" header supersedes the stale v1 units. The old V4 line "The CACM text of 2011 is UNSEEN" still stands lower down, but the header says to read the update first. Not counted.
- **Numbers and length:** check.mjs 15/15. numbers.md matches. Main text is 7,402 words (cap 7,500).
- **Sources list:** every cited work has an entry, and authors, years and venues are right.
