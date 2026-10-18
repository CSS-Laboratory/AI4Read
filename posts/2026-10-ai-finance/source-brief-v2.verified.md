---
id: 2026-10-ai-finance/source-brief-v2.verified
type: source-brief-additions-verified
stage: S2b (independent fact-check) of the S1b additions, post 02 v2
verified: 2026-10-18 by the S2b fact-checker against the source files (text layer re-extracted with pdftotext; Searle quotes on rendered page images at 110 dpi; numbers rerun in Python). Findings and evidence: review/s2b-check.md
post: "Could a society run itself on AI?" (topic-card-v2.md: five jobs, run, decide, check, declare, answer)
built_from: the seven sources added by Kunhao on 2026-10-18, read in posts/2026-10-ai-finance/sources/ (PDF plus text extract each)
checked: 2026-10-18
companion: source-brief.verified.md (S2). This file ADDS units; it does not replace units that are not named below.
grounding: Every unit marked SEEN was read at the source page. Quotes were matched against the text layer by script (letters and digits only) and are at most 25 words. Quotes whose text layer is lossy, and all Searle quotes (OCR), were also checked against the rendered page image; those are marked [img].
---

> **S2b status key.** Each unit header carries [OK] (checked, no change), [FIXED] (checked; corrections are written in and marked "S2b:"), [DROP] (the source does not support it) or [WITHDRAWN]. Counts: 1 critical, 2 major, 20 minor (see review/s2b-check.md). The **writer-must-not-use list** is in review/s2b-check.md and repeated at the end of this file.

> **Meta-manager notice (2026-10-18): units V6a–V6e are WITHDRAWN.** The *Nexus* PDF they were drawn from carries OceanofPDF marks (a pirate e-book site). Under the project's source policy (no shadow libraries), the file was deleted and nothing from it may be cited. Re-verify these units from a legitimate copy (Kunhao's own purchased copy, the publisher's sample, or the Guardian extract) before use. Until then, *Nexus* is cited only from the Penguin sample (Prologue) and the Guardian extract already in the verified brief.

# Source brief, v2 additions

**Status tags.**
- SEEN = read at the source page (page range given in the unit).
- UNSEEN = not obtained or not read. Do not quote.
- Where a unit replaces or corrects a unit of the S2 brief, the old unit is named under **Changes vs S2**.

**Page offsets (printed page = PDF page + offset).** Cite printed pages. Where a book has none, the unit says so.

| Source | File | Offset and notes |
|---|---|---|
| Kirilenko, Kyle, Samadi, Tuzun (JF 72(3), 2017) | kirilenko-2017-flashcrash-jf.pdf | 0. This is the accepted manuscript (text pp. 1-28; "Initial submission: December 30, 2010; Accepted: June 8, 2016", p. 29). The page numbers are the manuscript's, not the journal's. JF pagination is UNSEEN. |
| IMF GFSR Oct 2024, ch. 3 | imf-2024-gfsr-ch3.pdf | +76 (PDF 1 = p. 77; 30 PDF pages = pp. 77-106). Footers confirm it on every page. Two-column layout: the text layer prints the footer in the middle of a page, so read "page 87" as the whole PDF page. |
| Gensler and Bailey (SSRN 3766555) | gensler-bailey-2020-deeplearning.pdf | 0. Working paper "as of November 1, 2020". |
| Arora, Barak, Brunnermeier, Ge | arora-2011-cacm.pdf | +48 (PDF 1 = p. 49; pp. 49-65). **This file is the ICS 2010 extended abstract, not CACM** (see V4). |
| Haldane and May (Nature 469) | haldane-may-2011-nature.pdf | +350 (PDF 1 = p. 351; pp. 351-355). |
| ~~Harari, *Nexus* (2024)~~ | ~~harari-2024-nexus.pdf~~ | **WITHDRAWN (S2b).** The file was deleted (pirate e-book site). Nothing cited by "PDF n" of it may be used anywhere in this brief. *Nexus* is citable only from `nexus-penguin-sample.pdf` (Prologue, paperback roman pages) and `guardian-2024-nexus-extract.txt`. |
| Searle (1995) | searle-1995-construction.pdf (scan) + searle-1995-construction.txt (OCR, "=== PDF PAGE n ===" headers; there is no `ocr-searle/` folder) | **The offset changes inside the book.** PDF 23 to 66 = printed 14 to 57 (offset -9). PDF 67 is the chapter 3 opener, printed 59; from there printed = PDF - 8. S2b verified this on the running heads (PDF 23 = 14, 33 = 24, 65 = 56, 66 = 57, 67 = 59, 118 = 110, 149 = 141). **Printed p. 58 is not in the scan** (no PDF page carries it). |

**New traps (continuing the S2 numbering; 1-31 are in source-brief.verified.md).**

32. [OK] *Kirilenko JF 2017 is not the 2014 working paper.* Four things the writer may have taken from the working paper are NOT in the JF text: "did not cause the Flash Crash, but contributed to it"; the recommendation of short trading pauses; "temporarily shake the confidence of some market participants"; "about 36 minutes". Cite the version you quote. See V1.
33. [OK; "[CT]" confirmed on the p. 2 image] *The time zone in the JF's block quote is internally inconsistent.* p. 2 prints "At 2:32 [CT] p.m." inside the CFTC-SEC quotation (the "[CT]" is the authors' insertion, checked on the page image). The paper's own analysis windows begin at 13:32:00 CT (p. 22). The working paper says "2:32pm ET". 13:32 CT is 14:32 ET. So 2:32 p.m. in the quotation is Eastern time. Say "2:32 p.m. Eastern", and do not repeat "[CT]".
34. [OK] *"About 36 minutes" is ours.* It is 2:32 to 3:08 p.m. in the CFTC-SEC times that the JF quotes. The JF itself never says "36 minutes". The E-mini windows in the JF (13:32:00 to 14:08:00 CT) also add up to 36 minutes.
35. [FIXED] *Who decided to sell in 2010?* A mutual fund complex (a firm; the source does not describe who or what inside the firm made the call, so "a person decided" is our reading) decided to sell 75,000 contracts as a hedge and chose an automated execution algorithm. The algorithm set only the pace (9% of previous-minute volume). The JF's finding about high-frequency traders is "did not change", not "caused". The hook "computer programs ran a market into a crash" overstates; use "an automated sell program, started by a fund, met a market with little buy-side depth".
36. [OK] *"Algorithmic" is not "AI".* The IMF glossary (p. 101) defines algorithmic trading as "an algorithm independently executes trading decisions" and says it can be as simple as "basic trading rules". The IMF's 70% is algorithmic trading, not AI trading. Never write "70% of trading is AI".
37. [FIXED] *IMF figures read from charts are approximate* (+-2 points): Fig 3.5 and Fig 3.8 below (S2b re-read both images: values confirmed). The text itself gives two numbers (p. 86): "about 70 percent" of US equities trading and "more than half" of US futures trading. Panel 1 of Fig 3.8 draws US equities at about 67%.
38. [FIXED] *"Human in the loop" at the IMF has three scopes.* p. 78: "most participants" see it as essential for "regulatory, risk management, liability, and ethical reasons". p. 83: "all participants" expect it to persist "in the near term (three to five years), especially for large capital allocation decisions". The evidence is an outreach: many meetings, "detailed responses from 27 stakeholders" whose answers staff "tabulated", and a regulatory outreach with 10 supervisors (Box 3.1, p. 98). It is not a representative survey of practice.
39. [OK] *Gensler and Bailey: channels versus pathways.* The paper has three channels (monocultures and herding, network interconnectedness, regulatory gaps; pp. 3, 17) and five pathways (data, model design, regulatory, algorithmic coordination, user interface; p. 3). "Model design" is a pathway, not a fourth channel. The line "AI can easily mask who's at fault" is MIT Sloan's gloss; it is not in the paper (trap 15 stands, but the paper is now SEEN).
40. [OK] *Gensler and Bailey versus Kirilenko et al. on flash crashes.* G&B write "It is hypothesized that herding and crowding in high frequency algorithmic trading is partially responsible for causing flash crashes" (p. 22). KKST find that the high-frequency traders' inventory behaviour did not change. Do not present 6 May 2010 as an instance of model monoculture.
41. [OK; md5 460f8a74… identical] *The file `arora-2011-cacm.pdf` is the ICS 2010 extended abstract* (same md5 as arora-ics2010.pdf). The CACM text of 2011 is UNSEEN. `arora-2011-cacm-authorcopy.pdf` is the 2009 working paper (S2 units C3, C4). Cite the ICS paper as "Arora et al., ICS 2010, extended abstract".
42. [OK] *May's criterion is ecology.* Haldane and May state "mα² > 1" for random assemblies of species (for N much larger than 1; m links per species, α their average strength). They do NOT apply it to banks. Their banking results come from the interbank toy model (z, c, h, f), and there connectivity cuts both ways (V5).
43. [OK; re-checked on the p. 351 image] *The text layer drops Greek letters* in Haldane and May (ε as "e", α as "a", θ and γ as "h" and "c" in running text; ">" as "."). The "mα² > 1" line was checked on the page image [img]. Re-check any symbol before print.
44. [WITHDRAWN] *Nexus provenance.* Superseded: the ebook file came from a pirate site and was deleted. Do not cite any edition detail or page taken from it. Trap 7 (paperback sample, roman numerals) still applies to the Penguin sample.
45. [FIXED] *"Anything made of words" is from Davos 2026 (S2 unit A3b), not from the Nexus texts we may cite.* S2b searched the permitted *Nexus* sources (Penguin sample, Guardian extract): no hit. Whether the full book contains it is UNSEEN; do not say "it is not in *Nexus*".
46. [WITHDRAWN] *Chapter placement.* Drawn from the deleted file; unverifiable. Do not cite any *Nexus* chapter, subheading or passage that is not in the Penguin sample or the Guardian extract.
47. [WITHDRAWN in part] The evidence for "Harari does not cite Searle" and for the "cannot ‘believe’" line came from the deleted file; do not use either. What stays: any comparison between Harari's ideas and Searle's status functions is ours and must be labelled so.
48. [OK; S2b reran the search: "Turing" hits are OCR noise inside "capturing"/"picturing"; "computer" also occurs in the acknowledgements] *Searle on AI.* A search of the whole OCR text for robot, artificial intelligence, Turing, Chinese room and strong AI finds nothing. "Computer" occurs only in passing (printed pp. 14, 34, 56, 84, 140, 168; an endnote). The book does not say whether a machine can be one of the "we". Any such claim is ours.
49. [FIXED: Harari half WITHDRAWN] *FX.* IMF Fig 3.8 (p. 86): algorithmic share of US foreign exchange trading about 27% (read from the chart). The Harari "more than 90 percent" forex line came from the deleted file: do not use it.
50. [OK, wording softened] *Searle on tokens versus types.* A token can be money though nobody thinks it is (the bill in the cracks of the floor, p. 32); for the type, "the belief that the type is a type of money is constitutive of its being money" (p. 33). This bears directly on the card's guess 3 ("Can a token become money with no human accepting it?"): a token, yes, but only because people accept the codified type (p. 53).

---

## V1. Kirilenko, Kyle, Samadi and Tuzun (2017), JF 72(3): the Flash Crash [SEEN, pp. 1-29] [FIXED]

**Source.** `kirilenko-2017-flashcrash-jf.pdf`, accepted manuscript (offset 0). Read in full (text pp. 1-28; tables and figures skimmed). Authors' disclaimer: three were CFTC staff or contractors; views are theirs.

**Claims**

*Timeline (the CFTC-SEC narrative quoted on pp. 2-3; fn 3, p. 5 says the CFTC-SEC narrative was "based in part on the preliminary analysis contained in the original version of this paper" (S2b: the brief had dropped "contained")).* All clock times are as quoted (Eastern; see trap 33).
- 2:32 p.m.: "a large fundamental trader (a mutual fund complex)" starts a sell program of 75,000 E-mini contracts, about $4.1 billion, "as a hedge to an existing equity position". It "chose to execute this sell program via an automated execution algorithm" (the "Sell Algorithm"), set to 9% of the previous minute's volume "without regard to price or time". It was the largest net daily position change of any trader in the E-mini since 1 January 2010.
- The pressure was first absorbed by HFTs and other intermediaries, fundamental buyers, and cross-market arbitrageurs, who passed it to equities (SPY, individual stocks).
- 2:32 to 2:45: the algorithm sold about 35,000 of the 75,000 contracts (about $1.9 billion). By 2:45:28 there were fewer than 1,050 contracts of buy-side resting orders, "less than 1%" of the depth at the start of the day.
- 2:45:28: CME Stop Logic Functionality triggers; trading is paused five seconds; resumes at 2:45:33; prices stabilise and the E-mini recovers, then SPY.
- 2:40 to 3:00: over 20,000 trades across more than 300 securities were executed at prices 60% or more away from their 2:40 prices.
- By 3:08: the E-mini is back to nearly its pre-drop level.
- The paper's own windows (p. 22 and fn 29): "down" 13:32:00 to 13:45:28 CT; pause 13:45:28 to 13:45:33; "up" 13:45:33 to 14:08:00 CT; observations after 14:08:00 CT are excluded.

*The CME Stop Logic pause (p. 2, footnote 1).*
- It is "an automated pre-trade safeguard procedure". "Excessive" means outside a "predetermined" "no bust" range: 6 index points (24 ticks) in either direction for the E-mini.
- After it triggers, the matching engine goes into a "reserve state": orders can be submitted, modified or cancelled but no executions take place. The pause is 5 seconds for the E-mini (5 to 20 seconds across contracts). The engine leaves the reserve state through the same auction opening procedure used at the start of each trading day, then returns to continuous matching.
- **Human decision or pre-set rule?** A pre-set rule, triggered automatically. The paper describes no human decision at the moment of the pause, and it does not say who, if anyone, was watching. The human part is the earlier design of the rule and its parameters (our reading of "predetermined").
- **Did the pause stop the fall?** The paper reports that prices stabilised after the pause (quoting the CFTC-SEC report that the pause was "in order to prevent a cascade of further price declines"). The JF paper tests nothing about the pause's causal effect; "no changes in prices or inventory during the five-second pause" is a note on its regression windows (Table IV caption).

*Role of automated selling and of the HFTs.*
- Abstract: "a large automated selling program was rapidly executed". p. 3: "Theory suggests that a period of large and temporary selling pressure can trigger a market crash even in the absence of a fundamental shock" (Huang and Wang 2008; Weill 2007).
- Classification (pp. 11-15): over 15,000 accounts. Intraday intermediaries are accounts with small end-of-day and intraday net positions relative to volume on May 3-5 (three criteria; cutoffs "may need to be adjusted if applied in other markets", p. 13). The 16 most active are High Frequency Traders; the other intermediaries are Market Makers (189 on average). An HFT trades about 30 times as often as a Market Maker (fn 14, p. 14).
- Shares of volume (p. 17): HFTs 34.22% on May 3-5, 28.57% on May 6; Market Makers 10.49% and 9.00%. (S2b: p. 17 says "15 High Frequency Traders on average" were active on May 3-5; 16 accounts are so classified.)
- Inventories (p. 18): HFTs never held more than about 4,000 contracts; Market Makers never more than 1,500; combined intermediary net inventories did not exceed 6,000 contracts on any of the four days (p. 5), "an order of magnitude smaller" than the 75,000 sell program. In the "down" phase Fundamental Sellers out-sold Fundamental Buyers by 33,944 contracts (fn 30, p. 22).
- Behaviour (pp. 19-23): shortly before the pause the HFTs "aggressively liquidated approximately 2,000 contracts accumulated earlier, which coincided with significant additional price declines" (p. 19, as discussed in CFTC-SEC). Market Makers did not liquidate until after the pause. The HFTs' inventory-price relationship "did not significantly change" in the crash; the Market Makers' relationship did change (F-test rejects at 1%, p. 23).
- HFTs behave "more consistent with the theories of quote sniping or latency arbitrage" than with traditional market making (pp. 24-28): when HFTs are net buyers, prices rise 17% of a tick in the next second (May 3-5).

*Conclusions and hedges (p. 28).*
- Consistent with "the theory of limited risk-bearing capacity". The most active intermediaries "did not significantly alter their inventory dynamics when faced with large liquidity imbalances", unlike textbook market makers. ("Our results suggest": keep the hedge.)
- The October 15, 2014 US Treasury flash events "reignited discussion about the vulnerability of liquid automated markets"; such systemic events "may be a feature of the ‘new normal’". p. 28 calls the E-mini "fully automated".
- Hedges: the HFT category "might be representative of a subset of all high frequency trading strategies" (fn 5, p. 5; fn 15, p. 14). No message-level data, so they "cannot determine" what drove HFT aggressiveness (fn 36, p. 28). The regressions are run "without making causal inferences, as prices and inventories are jointly determined" (p. 20). The E-mini has "no market maker obligations", so the paper speaks to "the potential implications of not imposing market making obligations as markets become more automated" (p. 7).

**Quotes (at most 25 words)**
- p. 2 (CFTC-SEC, quoted): “chose to execute this sell program via an automated execution algorithm”
- p. 2 (fn 1): “an automated pre-trade safeguard procedure designed to prevent the execution of cascading stop orders”
- p. 3: “Theory suggests that a period of large and temporary selling pressure can trigger a market crash even in the absence of a fundamental shock”
- p. 19: “aggressively liquidated approximately 2,000 contracts accumulated earlier, which coincided with significant additional price declines”
- p. 28: “they did not take on large risky inventories relative to the large and temporary selling pressure on May 6”
- p. 28: “reignited discussion about the vulnerability of liquid automated markets to severe dislocations and disruptive trading”
- p. 7: “there are no market maker obligations in the fully electronic E-mini”

**Numbers.** 75,000 contracts; about $4.1 billion; 9% of previous-minute volume; 2:32 start; 35,000 sold (about $1.9 billion) by 2:45; fewer than 1,050 contracts (under 1%) of buy-side resting orders at 2:45:28; pause 5 seconds, 2:45:28 to 2:45:33; no-bust range 6 points (24 ticks); over 20,000 trades in more than 300 securities at 60% or more from the 2:40 price; E-mini back by 3:08; 16 HFT accounts, 189 Market Makers, over 15,000 accounts; HFT inventory at most about 4,000, Market Maker at most 1,500, combined at most 6,000; imbalance 33,944; HFT volume share 34.22% to 28.57%.

**Instance.** A fund-chosen automated sell program, a market with almost no buy-side depth, and an automatic, pre-set pause. Two jobs are visible: "run" (the algorithm and the matching engine) and "check" (the Stop Logic rule). "Decide" (sell 75,000 as a hedge) was made by the firm, not by the algorithm; that a human made it is our reading (the source says "a large fundamental trader (a mutual fund complex)").

**Careful!**
- Traps 32 to 35 and 40.
- The paper does not say that HFTs caused, or did not cause, the crash. Its statement is about their inventory behaviour. The "did not cause ... but contributed" sentence belongs to the 2014 working paper only.
- The paper does not show that shared models or herding drove 6 May 2010.
- The 5-second pause is a pre-set rule, not a human decision. The CFTC-SEC text quoted by the paper gives only the rule's purpose ("in order to prevent a cascade of further price declines") and reports that prices stabilised afterwards; neither it nor the JF paper claims or tests that the pause caused the recovery. (Corrected after S5 v2 round 1, Opus M1.)
- The nearest the JF comes to "HFTs contributed" is p. 19 (the 2,000-contract liquidation "coincided with" further declines). It is a coincidence in time, not a causal claim.

**Differences from the 2014 working paper (S2 unit B2)**

| In the 2014 WP (B2) | In the JF 2017 manuscript |
|---|---|
| Abstract: HFTs "did not cause the Flash Crash, but contributed to it by demanding immediacy ahead of other market participants" | Absent. Abstract says the HFTs' pattern "did not change when prices fell during the Flash Crash". |
| "in the course of about 36 minutes starting at 2:32pm ET" | Absent. 2:32 appears only inside the CFTC-SEC quotation, with the "[CT]" insertion (trap 33). |
| Recommendation: short trading pauses followed by coordinated re-opening; the five-second pause is "one example" | Absent. |
| "temporarily shake the confidence of some market participants but probably have little impact on the ability of financial markets to allocate resources" | Absent. |
| Footnote on "unrelated trading algorithms ... can cascade into a systemic event" | Not seen in the JF text. |

**Changes vs S2.** B2 stays valid as a unit about the working paper; label every quote from it "working paper, 2014". For the hook, use the JF text for what happened and the quoted CFTC-SEC sentences for the pause. The $4.1 billion, the 9% rule, the five seconds and the 2:45:28 time are in both versions.

**Toy idea.** The clamp toy (E8) with the pause as a pre-set rule with a no-bust range and a re-opening auction (a threshold that, once crossed, freezes execution for a fixed time). Say "toy, ours".

---

## V2. IMF, Global Financial Stability Report, October 2024, ch. 3 [SEEN, pp. 77-106] [FIXED]

**Source.** `imf-2024-gfsr-ch3.pdf`: "Advances in Artificial Intelligence: Implications for Capital Market Activities", GFSR October 2024 ("Steadying the Course: Uncertainty, Artificial Intelligence, and Financial Stability"). Authors: Abbas, Conde Vitureira, Diaby, Fernandez Dionis, Ferrante, Grolleman, Kramer, Lim, Mosk, Singh, Stobo (p. 77). Offset +76. Read: the whole chapter text, Boxes 3.1 and 3.2, the glossary; Fig 3.5 and Fig 3.8 viewed as images [img]. The references pages were skimmed.

**Claims**

*What counts as "algorithmic" and "AI".*
- p. 101 (glossary): algorithmic trading is "Trading in financial instruments whereby an algorithm independently executes trading decisions"; it can be execution, market-making or proprietary strategies; "in its simplest guise" it can be "basic trading rules or instruction to feed portions of an order into the market at preset intervals". HFT is a type of algorithmic trading, "not all forms of algorithmic trading can be described as high frequency" (p. 102).
- p. 78, fn 1: "AI/ML models" means well-established predictive analytics (shallow neural networks, clustering, decision trees); "sophisticated AI models" means deep networks, reinforcement learning and language models, including generative AI.

*Share of trading that is algorithmic or AI-driven.*
- p. 86: "In the United States, algorithmic trading now constitutes about 70 percent of equities trading and more than half of futures trading (Figure 3.8, panel 1)". Fig 3.8, read from the image [img] (approximate): US share of algorithmic trading activity by asset class in 2022-23: equities about 67%, futures about 52%, options about 44%, foreign exchange about 27%, fixed income about 8%. Equity algorithmic share by region, 2023: United States about 68%, Europe about 50%, Asia about 42%, Latin America about 30%. Euronext equity activity: the most active participant about 28%, the ten most active together about 89%.
- AI-specific adoption is "still nascent" (Fig 3.5, p. 83; Mercer Investments 2024 survey of investment managers). Read from the image [img]: "Executing investment decisions": 11% already integrated, 11% partly integrated, 59% do not plan to integrate. "Allocating assets": 10%, 9%, 59%. Dutch energy market algorithms using machine learning: about 88% of signal generators, about 33% of trading algorithms, about 11% of execution algorithms (approximate; Authority for Consumers and Markets 2024).
- **p. 82** (S2b: not p. 83): sophisticated AI "has not yet been implemented widely to build autonomous AI trading agents"; it is "more frequently used to generate a signal" that feeds "an existing analytical system where a human trader may ultimately make the trading decision". Dutch Authority for the Financial Markets: machine learning is used "implicitly or explicitly" in 80 to 100 percent of trading algorithms on Euronext, but "explicit" cases "may include applications that are not autonomous, such as signal generators" (fn 8, p. 82).
- Outlook (p. 83): participants expect "high-frequency, AI-driven trading" to account for "a more substantial share" in equities.

*Key findings.*
- Efficiency and liquidity (p. 87): algorithmic trading "enhances liquidity and informational efficiency, albeit at the cost of increased short-term volatility"; it can also raise volatility after macro news and discourage informed traders. In US Treasuries, liquidity improved on aggregate but "rare but extreme bouts of illiquidity under stress" may be the cost. Idiosyncratic price jumps in US stocks have become less frequent (Fig 3.10, 235 stocks, 2007-2024).
- Volatility under stress (p. 88): "Algorithmic trading strategies are often programmed to de-risk or even shut down during periods of high volatility". These limits protect each firm, "However, under certain conditions they could contribute to market destabilization" through cascading triggering of limits, feedback loops and "the sudden evaporation of liquidity" (S2b: the hedge "under certain conditions" restored). The evidence is "some evidence": order cancellation rates fall and hidden-order rates rise as implied volatility rises ("flighty liquidity-under-stress"). AI-driven strategies are "also subject to the same measures" according to outreach feedback.
- Scenarios (Table 3.1, p. 89): negative (AI "magnifies existing risks", more leverage, more interconnectedness) and positive (AI "increases the stability of algorithmic trading under stressed conditions", "lower flash-crash risk"). "On balance, the impact of these changes from a financial stability perspective is highly uncertain." (p. 89)
- Speed (p. 89; Fig 3.11): after large language models, the first 45 seconds of the market reaction to FOMC minutes reflect the eventual impact "more accurately" (events with a move over 0.2% at 15 minutes: 15 before, 15 after). AI-driven ETFs have "significantly higher turnover"; three sample AI ETFs raised turnover in March 2020 ("some evidence for procyclicality").
- Concentration (pp. 86, 91, 93): "Increasing returns to scale seem to have resulted" in markets with high algorithmic shares also having activity concentrated among few players (Euronext). Participants in the outreach cited "herding and market concentration" as a key stability risk (a question about generative AI, Fig 3.12 panel 1), viewed as "especially pertinent" "if trading and investment strategies were to become largely derived from open-source AI and trained on similar data sourced from the same set of vendors" (p. 91; S2b: the brief's "especially if trading…" was not verbatim). Vendor concentration: failure of a few model or data providers "may lead to market stress akin to the failure of key financial market utilities such as clearing houses" (p. 93).
- Herding (p. 93): see quotes. In normal times models "may uncover new trading opportunities, leading to more diverse investment strategies"; in adverse shocks they "could simultaneously rebalance portfolios toward safe assets, creating a self-fulfilling spiral of fire sales".
- Collusion or manipulation (pp. 89, 91): risks "are currently being investigated through theoretical models" (p. 89). "In some cases, tacit algorithmic collusion could emerge" (Dou, Goldstein and Ji 2024); "By contrast, the empirical literature points to the possibility of a ‘winner takes all’ scenario" (Baron and others 2017) (p. 91). Manipulation is more likely with an information or latency advantage and fewer players, illustrated by Fan, Pelger and Yu's simulations (Fig 3.11 panel 4, fn 19, p. 91). (S2b: the brief had pinned winner-takes-all on the simulations and given p. 89 only.)
- Overall (p. 92): "currently the financial stability risks associated with its adoption appear contained". The chapter "finds indicative evidence" for four risk categories (p. 78): speed and volatility; opacity and monitoring (including migration to nonbanks); operational (third-party providers); cyber and manipulation.

*Humans in the loop.*
- p. 78 (S2b, **major fix**): what "remain mostly speculative" is "the more ‘revolutionary’ uses of GenAI—radically new investment strategies and processes using cutting-edge AI technology". Separately: "many observers envision scenarios involving autonomous AI generating and executing trades without human oversight", but most outreach participants "are quite uncomfortable with this idea" and see AI strategies "not understood by humans" as "a nonstarter". Do not write that the IMF calls autonomous AI trading "mostly speculative". (The first sentence is directly relevant to the post's question: radically new AI-made strategies are, for the IMF in 2024, "mostly speculative".)
- p. 83: "all participants" expected a "human in the loop" for three to five years, "especially for large capital allocation decisions"; "complete autonomy is not anticipated soon". "Some participants mentioned the potential for agent-to-agent trading and the development of complete AI-driven workflows in trading."
- p. 93: in novel events, "models may simply shutdown, requiring humans to make decisions on and process a voluminous number of trades". Models may also produce outcomes "difficult to comprehend".
- p. 93: "institutions are responsible for AI systems they deploy, whether internally developed or externally sourced"; existing capital-market frameworks "are largely technology-neutral".
- Fig 3.12 panel 2 (p. 91): participants expect regulators to ensure market integrity and "maintain human oversight of decision making".

*Policy recommendations (pp. 95-97).*
- Cross-sector: balanced approach; request "risk mapping" of interdependencies between data, models and technology infrastructure (p. 95-96).
- Speed and volatility (p. 96): determine whether to design or modify "volatility response mechanisms"; "Existing circuit breakers may need to be re-parameterized"; "poorly designed circuit breakers may exacerbate volatility"; test algorithms "in controlled environments"; review margining and buffers.
- Opacity (p. 96-97): ask institutions to map dependencies; models "may feed on shared or interdependent data sources; share a common architecture; and rely on a small number of providers"; monitor "large traders", each "uniquely identified"; strengthen oversight of nonbanks.
- Third parties (p. 96; S2b: not p. 97): coordinated approach to critical service providers; the definition should be broad enough to "capture the systemic use of common AI models".
- Over-the-counter markets (p. 97): more transaction data, incentives for market makers, central clearing, margin for uncleared derivatives; central bank liquidity as a backstop.
- Supervisors' own tools (pp. 83, 95): supervisors in the outreach "use AI-driven SupTech tools" (p. 83). The adoption numbers are for SupTech in general ("new and emerging technology for supervisory processes"), not AI specifically: in 2023, 79% of advanced economies and 54% of emerging market and developing economies had adopted SupTech tools (50% and 31% in 2022; fn 24, p. 95, citing Cambridge SupTech Lab 2023). Upskilling "should help" authorities identify models designed to "game the regulation" and detect "algorithmic coordination" (p. 95).
- Evidence base and hedges: Box 3.1 (p. 98): IMF staff held many meetings and "received detailed responses from 27 stakeholders" (answers "tabulated"); regulatory outreach with 10 capital market supervisors. The chapter "finds indicative evidence" for the risk list (p. 78, not Box 3.1).

**Quotes (at most 25 words)**
- p. 86: “algorithmic trading now constitutes about 70 percent of equities trading and more than half of futures trading”
- p. 101: “Trading in financial instruments whereby an algorithm independently executes trading decisions”
- p. 78: “most participants view having a ‘human in the loop’ as an essential part of any AI-based strategy”
- p. 83: “all participants in the IMF’s outreach expected a ‘human in the loop’ approach to persist in the near term (three to five years)”
- p. 83: “Although the trend is toward less human interaction, complete autonomy is not anticipated soon, and models will continue to operate within predefined rules.”
- p. 87: “Research suggests that algorithmic trading enhances liquidity and informational efficiency, albeit at the cost of increased short-term volatility”
- p. 88: “Algorithmic trading strategies are often programmed to de-risk or even shut down during periods of high volatility”
- p. 89: “On balance, the impact of these changes from a financial stability perspective is highly uncertain.”
- p. 93: “AI models may herd and produce rather similar decisions, especially during stress periods resulting in procyclical financial stability risks.”
- p. 93: “models may simply shutdown, requiring humans to make decisions on and process a voluminous number of trades”
- p. 93: “institutions are responsible for AI systems they deploy, whether internally developed or externally sourced”
- p. 92: “currently the financial stability risks associated with its adoption appear contained”

**Numbers.** About 70% of US equities trading and over half of US futures trading are algorithmic (p. 86). Fig 3.8 and 3.5 values above (approximate; S2b re-read both images: Fig 3.5 "Executing investment decisions" bars are 11 / 11 / 15 / 4 / 59 = already integrated / partly integrated / planning / used but not integrated / do not plan; they sum to 100). 27 detailed stakeholder responses; 10 supervisors; 26 authorities reviewed (p. 95). Near term = three to five years (p. 83). NBFIs hold "over half of all financial market assets globally" (p. 86).

**Instance.** The chapter's own instance is the "flighty" liquidity of algorithmic market makers under stress, and the possibility of simultaneous shutdown. It names no episode.

**Careful!**
- Traps 36, 37, 38 and 49.
- The IMF is balanced: "AI may actually reduce financial stability risks" (p. 77) and the positive column of Table 3.1 give a case for lower flash-crash risk. The card's "the cost is correlated failure" is one of two scenarios in the IMF text, not its finding.
- "Herd" is a hedged "may". The evidence for herding of AI models is the outreach (what participants fear) plus theory; the chapter reports no measured herding of AI models.
- The 70% says nothing about who decided what to trade; under the glossary definition it includes simple execution rules.

**Changes vs S2.** Replaces B7 (DROP). All three phrases B7 reported are now SEEN and correct: "AI models may herd..." (p. 93); "about 70 percent of equities trading" (p. 86); "human in the loop" for "three to five years" (p. 83). The "remain mostly speculative" line is on **p. 78**, and its subject is the "revolutionary" GenAI uses (radically new strategies), not autonomous trading (S2b).

**Toy idea.** The shut-down toy: N trading rules each with a pre-set loss limit; one shock trips them in the same minute; liquidity (the sum of what is left) falls by the count of tripped rules. Compare limits that are identical with limits that differ. Say "toy, ours". It goes with the six-bank cascade.

---

## V3. Gensler and Bailey (2020), "Deep Learning and Financial Stability" [SEEN, pp. 1-32] [FIXED]

**Source.** `gensler-bailey-2020-deeplearning.pdf`: SSRN 3766555 (every page footer; MANIFEST table B lists 3723132 for the abstract page: cite the number on the file), "Working Paper as of November 1, 2020", MIT AI Global Policy Forum. Offset 0. Read: abstract to the conclusion (pp. 1-32); references skipped. This is the paper itself, not the MIT Sloan article (S2 unit E3).

**Claims**

*Structure (pp. 2-5).* Three acts. Act 1: nine key characteristics of deep learning (hyper-dimensionality, non-linearity, non-determinism, dynamism, complexity; limited explainability, bias or fairness, lack of robustness; an "insatiable hunger" for data). Act 2: systemic risk through three channels. Act 3: five pathways. Coda: policy.

*The three channels (pp. 3, 17-18).*
- Uniformity and monocultures, including herding. "Herding is characterized by multiple individual actors making similar decisions, either rational or behavioral, resulting in a monoculture." Uniformity can also arise when many actors "rely on a centralized dataset or model." (p. 17; S2b: split, the brief's single quote was 38 words)
- Network interconnectedness: "either the emergence of a dependency on some concentrated infrastructure, data, or operational service provider or an intricate web of firm-to-firm relationships" (p. 17). Cites Haldane (2009) on the financial system as a complex adaptive network "both fragile and robust at the same time".
- Regulatory gaps: the rules themselves fall short.

*The five pathways (pp. 20-27).*
- Data (pp. 20-22): concentrated data providers add herding and interconnectedness. "Models built on the same datasets are likely to generate highly correlated predictions that proceed in lockstep, causing crowding and herding." The risk rises as the provider moves up the value chain from raw data to "analytics and insights". Alternative data have "short sample sizes" that do not cover "even a single, complete financial cycle" (p. 21).
- Model design (pp. 22-24): possible convergence on a few model types ("mono-models", pp. 4, 25); human factor: few people are trained to build these models, with "fairly similar backgrounds" and an "apprentice effect"; AI-as-a-Service providers (named: BlackRock's Aladdin, Two Sigma's Venn, OpenAI) add interconnectedness. Models may have "fat tails" because of non-linearity and short data (p. 24). "Initially" different initialisations and hyperparameters "may lead to a greater diversity of outcomes", which later consensus erodes (p. 22).
- Regulatory (pp. 24-25): standards for explainability, fairness and robustness "may risk being uniformly internalized"; "Regulatory deep learning models may unknowingly promote uniformity in the agents they regulate"; a supervisory model that "is perturbed or fooled" could cause "outsize risk"; activity may migrate to less regulated actors.
- Algorithmic coordination (pp. 25-27): "by design one firm's models are going to be adapting to the signals from other firm's models"; "Models may add fragility through an invisible, machine-based, form of coordination and possible collusion." Collusion risk depends on number of firms, entry barriers, transparency and frequency of interaction (OECD); regulators "may not be able to discern deep learning coordination until after the fact".
- User interface (p. 27): standardised advice from virtual assistants may cause "herding of client decision making".

*Opacity and humans (pp. 9, 12, 13).*
- "Despite the highly automated nature of neural networks, there is still much human involvement in the modeling process" (p. 9: developers set hyperparameters, which create "inductive bias").
- Many models "automatically rebuild themselves" (continuous learning), adjusting "without any human oversight" (p. 12).
- "Human agency and traditional intervention approaches may be lost as a consequence of lack of model explainability and transparency" (p. 13). Their argument: "if deep learning predictions were explainable, they wouldn’t be used in the first place".

*Flash crashes (p. 22).* "It is hypothesized that herding and crowding in high frequency algorithmic trading is partially responsible for causing flash crashes" (citing Lo and Kirilenko and Lo). See trap 40.

*Policy (pp. 28-32).* Micro-prudential: internal mapping of dependencies; updated model-risk guidance (SR 11-7 of 2011, TRIM 2017, E-23 2017); firm buffers, including back-up non-deep-learning models run in parallel; regulatory diversity (more than one way to comply). Macro-prudential: external mapping of data and AI-as-a-Service dependencies; coordinated stress tests and "war games"; bringing material third-party providers inside the regulatory perimeter; horizontal reviews; network buffers. Ex post: circuit breakers, "kill switches", central bank last-resort roles, recovery and resolution plans for providers (p. 32). Their summary: updated model-risk guidance "will not be sufficient" for herding, interconnectedness or regulatory gaps (p. 28, also p. 4; S2b: not p. 32); existing regimes "are likely to fall short"; "Adequately mitigating such risks will require additional research and discussion" (p. 32).

*Hedges.* The paper says "we hypothesize" (p. 2) and speaks throughout of what "may" or "is likely" to happen "as it moves to a mature stage of broad adoption"; it is a working paper; it says the policy levers "may be insufficient" (p. 32).

**Quotes (at most 25 words)**
- p. 21: “Models built on the same datasets are likely to generate highly correlated predictions that proceed in lockstep, causing crowding and herding.”
- p. 17: “Herding is characterized by multiple individual actors making similar decisions, either rational or behavioral, resulting in a monoculture.”
- p. 22: “It is hypothesized that herding and crowding in high frequency algorithmic trading is partially responsible for causing flash crashes”
- p. 26: “Models may add fragility through an invisible, machine-based, form of coordination and possible collusion.”
- p. 25: “Regulatory deep learning models may unknowingly promote uniformity in the agents they regulate.”
- p. 13: “Human agency and traditional intervention approaches may be lost as a consequence of lack of model explainability and transparency.”
- p. 12: “They adjust their parameters given more recent data and feedback without any human oversight, and automatically redeploy to production.”
- p. 9: “Despite the highly automated nature of neural networks, there is still much human involvement in the modeling process.”

**Numbers.** 3 channels, 5 pathways, 9 characteristics. SR 11-7 is from 2011 (p. 24, 28). No empirical estimates in the paper.

**Instance.** Quant crisis of August 2007: "As hypothesized by Khandani and Lo", it "was a consequence of model herding"; funds "unknowingly developed highly similar optimization functions" (p. 22; S2b: keep "as hypothesized"). Credit-rating agencies used "models with similar methodologies" for CDOs (p. 22).

**Careful!**
- Traps 39 and 40. The wording on correlated predictions is "likely to generate", conditional on shared data.
- The paper is a hypothesis about a *future mature stage*, not a finding about 2020. Its firmest (unhedged) lines are on policy: current guidance "will not be sufficient" (p. 28) and "if deep learning predictions were explainable, they wouldn’t be used in the first place" (p. 13).
- It says early-stage technology "often" shows diversity, then "often recedes to more technological uniformity" (p. 4). Do not cite it for present uniformity.
- It names the *checking* job as exposed: a supervisor's own model "may unknowingly promote uniformity" (p. 25). That is a quotable bridge to "who checks the checker".

**Changes vs S2.** E3 (secondary, via MIT Sloan) can be dropped as a source for the paper's content; keep it only for the MIT Sloan article's own gloss. Trap 15 is resolved: the paper is SEEN.

**Toy idea.** The effective-number-of-opinions toy (E8): ten models trained on one dataset; show N_eff near 1 when correlation is high. Say "toy, ours".

---

## V4. Arora, Barak, Brunnermeier and Ge: ICS 2010 extended abstract (the file labelled "cacm") [SEEN, pp. 49-65; the CACM text is UNSEEN] [FIXED]

**Source.** `arora-2011-cacm.pdf` = `arora-ics2010.pdf` (same md5): "Computational Complexity and Information Asymmetry in Financial Products (Extended Abstract)", Innovations in Computer Science 2010, printed pp. 49-65 (offset +48). It says it is "geared to a CS audience" and proves simple cases "for binary CDOs only"; a "companion paper" (economists' version, with tranching) is the 2009 working paper behind S2 units C3 and C4. The 2011 CACM article (54(5): 101-107) is UNSEEN: the one attempt to fetch the Princeton copy returned an HTML error page. Read pp. 49-65; pp. 59 and 63 also viewed as images [img].

**Claims**

- Abstract, p. 49: "Assuming reasonable complexity-theoretic conjectures, we show that derivatives can actually amplify the costs of asymmetric information instead of reducing them." The results are proved "both in the worst-case setting, as well as the more realistic average case setting", with "computational indistinguishability" used to argue the constructions "look like" real derivatives.
- Lemon cost (pp. 50-51; S2b: the example starts on p. 50): Akerlof's car example ($1000 working car, 20% lemons worth $0, expected $800; the seller's value must be $200 below the buyer's, so "the ‘lemon cost’ of this market is $200"). Defined for derivatives on p. 52: Δ(n) = E[F(X)] minus the minimum over n-subsets S of E[F(X) | X_i = 0 for all i in S]. The seller "positions" the junk assets to his advantage.
- Derivatives amplify asymmetric information (pp. 51, 55). Received wisdom (DeMarzo): cherry-picking can be mitigated by tranching because the buyer holds the information-insensitive part; "This belief is questioned by our paper" (p. 51). With random pooling the lemon cost falls from n to o(n); with pooling that over-represents lemons by about √D, "under computational assumptions, the lemon cost for polynomial time buyers can be much larger than n" (p. 55).
- Worst case (Section 3, pp. 53-54): approximating the lemon cost is NP-hard (Theorem 1: DLC[1] within 1+ε; Theorem 3: DLC[2] within Ω(2^((log N)^(1/3 - ε))), via Label Cover). This part is new relative to the working paper units.
- Hardness assumption (Section 4.3, p. 56): the "Densest subgraph assumption": no polynomial-time algorithm distinguishes the random graph R from the planted graph P with non-negligible advantage, for stated parameter ranges. Status: "consistent with current knowledge" (state of the art: Bhaskara et al.), "the (almost) strongest possible form consistent with current knowledge", and "quantitative improvements in algorithms for this problem will result in corresponding quantitative degradations to our lower bounds on the lemon cost".
- Cost of complexity (pp. 55, 59): CoC defined by a "pricing game" over computationally indistinguishable distributions; CoC = Ω̃(n√(N/M)) for the binary CDO (p. 59).
- No proof of an untampered product (p. 55): "there seems to be no direct way for seller to prove that the financial product is untampered" (related to NP vs coNP); for suitable parameters tampering is undetectable "ex post". A lemon law may not help: "in many models, even the problem of detecting the tampering ex post may be intractable" (p. 51; Section 5.1, p. 59).
- Tamper-resistant designs (Section 6, pp. 60-62): "The XOR function is not too natural in real life" and is not monotone (p. 60-61). The tree of majorities: TM^k on 3^k inputs, defined recursively by majorities of three; Theorem 9 (p. 61): fixing any t inputs to 0, with the others independent fair bits, the probability that TM^k is 0 is at most (1 + t/2^k)/2; Theorem 10: with D = 3^k and D much larger than log^3 M, any manipulation that significantly changes a product's expectation is detectable ex post. The tree is not securitizable by itself; the fix is F = TM^k AND Threshold(0.4 * 3^k).
- Faulty models and the "first step" caveat (Conclusions, p. 63): see quotes. Positive results are "Section 6" (the working paper's "Section 5").
- Rating agencies "use simple simulation-based approaches" and "may fail to detect tampering even in the parameter regime where the densest subgraph can be solved in polynomial-time" (fn 1, p. 50).

**Quotes (at most 25 words)**
- p. 49: “derivatives can actually amplify the costs of asymmetric information instead of reducing them”
- p. 50: “yet even sophisticated buyers like Goldman Sachs would have no idea what to pay for it”
- p. 50: “information that is in plain view yet cannot be understood with any foreseeable amount of computational effort”
- p. 56: “we chose to present the assumption in the (almost) strongest possible form consistent with current knowledge”
- p. 55: “there seems to be no direct way for seller to prove that the financial product is untampered”
- p. 63: “Our results can be seen as some cause of concern, even though they are clearly only a first step (simple model, asymptotic analysis, etc.)”
- p. 63: “and we do not dispute that effect”
- p. 63: “one fears that such pricing problems will not go away even with better models”
- p. 63: “Our few positive results in Section 6 raise the hope that it may be possible to circumvent at least the tampering problem with better design.”
- p. 60: “it remains to be seen how to adapt these ideas to more realistic scenarios with more complicated input correlations, timing assumptions, etc.”

(The "and we do not dispute that effect" fragment ends the conclusion's "faulty models" sentence: most analysis blames "‘faulty models’ in pricing derivatives rather than computational complexity", and the authors do not dispute that effect. Quote it in these two pieces; the full sentence is 27 words.)

**Numbers.** $1000, $800, $200 (lemon cost); Δ(n) as above; Theorem 9 bound (1 + t/2^k)/2; CoC = Ω̃(n√(N/M)); threshold 0.4 * 3^k; assets pay 0 or 1 with probability 1/2 in the model.

**Instance.** The "factoring derivative": a 1000-digit integer n in the contract and a payoff that depends on the last digit of a factor of n and next January's unemployment rate (p. 50). Binary CDOs in the model; CDO² only in the working paper.

**Careful!**
- Trap 41. Also, every S2 caveat on C3 still holds: conjectured assumption, simple model (independent 0/1 assets), asymptotic, "only a first step".
- Wording differs from the working paper: (i) abstract opens "Assuming reasonable complexity-theoretic conjectures" (the working paper abstract, as in C3, has no such clause and adds "Computational complexity is only a small departure from full rationality", which is absent here); (ii) "even sophisticated buyers like Goldman Sachs" here versus "even Goldman Sachs" there; (iii) on faulty models the working paper says "this analysis is probably correct" (C4), the extended abstract says "we do not dispute that effect" and adds "rather than computational complexity"; (iv) positive results are Section 6 here, Section 5 there; (v) the table of results for CDO², tranched CDO and CDO² is not in this version (binary CDOs only), and Theorems are numbered differently (here: Theorems 1-3 worst case, 7-8 XOR, 9-10 tree).
- The "first step" sentence and the "one fears" sentence are word-for-word the same in both versions.
- CACM wording is UNSEEN; do not call any of this "the CACM paper".
- The hardness is for *pricing and detecting tampering by a computationally bounded buyer* in a model where the seller plants a pattern. It is not a statement that a human cannot understand a short contract. Reading an AI designer as the informed seller is ours.

**Changes vs S2.** C3 and C4 remain valid for the working paper. For the post, prefer the ICS text for the hedges (they are stronger in print) and say "extended abstract, ICS 2010". The lemon-cost definition and the tree of majorities are in both.

**Toy idea.** As C3: 100 assets, 10 junk. Add the XOR-versus-sum contrast: shifting a sum needs about √D fixed inputs, shifting an XOR needs almost all of them. Say "toy, ours".

---

## V5. Haldane and May (2011), "Systemic risk in banking ecosystems", Nature 469 [SEEN, pp. 351-355] [FIXED]

**Source.** `haldane-may-2011-nature.pdf`: Nature 469, 351-355 (20 January 2011), a Perspective; doi:10.1038/nature09659. Offset +350. Read in full; p. 351 viewed as an image [img]. Authors: Haldane (Bank of England), May (Oxford Zoology). Policy is stated as "explicit aim of minimizing systemic risk".

**Claims**

*May's criterion (p. 351).*
- Background: Hutchinson (1959) thought more links meant more stability, "based on a misunderstanding of MacArthur’s paper". "To the direct contrary", model ecosystems showed that a random assembly of self-stable species "showed a sharp transition from overall stability to instability as the number and strength of interactions among species increased" (S2b: quote trimmed to 25 words).
- Exact statement [img; S2b re-checked]: "for N ≫ 1 this transition occurs once mα² > 1, where m is the average number of links per species" and "(±) α their average strength" (ref. 4: May 1972, *Nature* 238, 413-414; UNSEEN).
- Conditions: random assembly; N much greater than 1; each species self-stable when alone; interaction strengths of either sign (the ± before α; "random sign" is our gloss of May's setup). It is an ecology result; Haldane and May do not apply it to banks. In ecology it prompted a search for special structures (modularity, nested hierarchies) that reconcile complexity with persistence; "tentative evidence" is given (p. 351).
- Differences between ecosystems and finance are acknowledged: "There are, of course, major differences between ecosystems and financial systems." (p. 351)

*Derivatives and complexity (pp. 351-352).* About two-thirds of the growth in banks' balance sheets reflected claims within the financial system ("perhaps as much as"). Derivatives outgrew world GDP "by a factor of three" (Fig. 1). Caccioli, Marsili and Vivo (2009): arbitrage pricing theory assumes "perfect competition, market liquidity, no-arbitrage and market completeness", i.e. that trading has no feedback on prices; when feedback is included, "the road to efficient, arbitrage-free, complete markets can be plagued by singularities which arise upon increasing financial complexity". In their model, as n (the number of derivative types) approaches n* (here 4.14) "there is a sharp singularity" at zero risk premium (S2b: the brief said "once n passes"). Haldane and May's own gloss, "in grossly simplified terms": once the market is "essentially complete", extra trades are "essentially redundant", raising complexity "at a cost in terms of stability, with no welfare gain" (p. 352).

*The banking-network model (p. 352-353).*
- A bank has assets (interbank loans l_i, external assets e_i) and liabilities (interbank borrowing b_i, deposits d_i); solvency requires net worth c_i = (e_i + l_i) - (d_i + b_i) ≥ 0. Banks are linked at random (Erdős-Rényi), each pair with probability p; the average number of links is z = p(N - 1).
- Mean-field simplification: all banks the same size (1), each linked to exactly z others, loans of equal size, equal capital c, loans-to-assets ratio h (the text layer shows h and c; the figures show θ and γ). A shock wipes out a fraction f of one bank's external assets; the bank fails if f(1 - h) > c.
- Loan-driven shocks are attenuated, by about the factor z, because a failing bank's losses are split among z creditors. Fragility is greatest for intermediate h. An increase in connectivity z "causes the coloured region of instability to shrink; high connectivity distributes, and thereby attenuates risk." But "when later-phase failures do occur, they will then involve more banks." (p. 353; S2b: split, the brief's single quote was 37 words)
- Liquidity shocks are different: "in sharp contrast to the attenuation in interbank loan shocks, liquidity shocks amplify as more banks fail"; funding-liquidity hoarding "is not subject to the attenuation" (p. 353).
- Real networks are "far from random", with long-tailed degrees; "disassociative" wiring (big banks tied to small) maximises the number infected by a contagion but "can make the network more robust to random losses" (p. 353).

*Homogeneity and diversity (p. 353; policy p. 355).*
- Claim: "all the banks doing the same thing—can minimize risk for each individual bank, but maximize the probability of the entire system collapsing" (the subject is "excessive homogeneity within a financial system"; S2b: trimmed to 22 words). Source cited: earlier work and N. Beale and colleagues, "manuscript in preparation" (UNSEEN).
- Toy: N banks and N distinct, uncorrelated asset classes, each with a very small probability ε of a loss big enough to fail a bank holding only that asset. Inhomogeneous extreme: each bank holds one whole asset; a given bank fails with probability ε and the system with ε^N. Homogeneous extreme: each bank holds 1/N of every asset; one bank fails (and so all N do) with probability N^N ε^N / N!. "This homogeneous, ‘herding behaviour’ limit clearly makes each individual bank safer, but the systemic risk is much larger." "More realistic versions of this scenario consistently show the same unhappy conclusion." (pp. 353-354)
- Evidence: "Tentative evidence" is that the world's five largest banks showed increasing concentrations of assets, in contrast to the top five hedge funds, "whose less concentrated systems can give greater scope for diversity" (p. 354). Policy: "this systemic diversity objective should probably be given much greater prominence by the regulatory community" (p. 355); "Homogeneity bred fragility" (p. 355, citing Beale et al.).

*Policy lessons (pp. 354-355), all labelled "tentative" and drawn from "deliberately oversimplified models".*
- Capital and liquidity ratios, read as protection of the whole system, not only of each bank.
- Systemic calibration: set requirements "to equalize the marginal cost to the system as a whole" of failure, so "higher for those banks bringing greatest risk to the system" (the "super-spreaders", after Anderson and May).
- Countercyclical buffers (a "new departure").
- Central counterparties replace a "cat’s-cradle" with a "hub-and-spokes" structure, "Provided the central counterparty is extremely robust—to prevent it becoming a super-spreader itself" (pp. 354-355); netting cut the CDS stock by "around $25 trillion since December 2007".
- Topology: diversity (above) and modularity: "Modular configurations prevent contagion infecting the whole network in the event of nodal failure." Examples: the Volcker rule; a UK Royal Commission. Closing line: "It took a generation for ecological models to adapt. The same is likely to be true of banking and finance."

**Quotes (at most 25 words)**
- p. 351 [img]: "this transition occurs once mα² > 1, where m is the average number of links per species, and (±) α their average strength"
- p. 351: “There are, of course, major differences between ecosystems and financial systems.”
- p. 353: “all the banks doing the same thing—can minimize risk for each individual bank, but maximize the probability of the entire system collapsing”
- p. 353: “liquidity shocks amplify as more banks fail”
- p. 354: “regulatory requirements would be set higher for those banks bringing greatest risk to the system”
- p. 355: “Modular configurations prevent contagion infecting the whole network in the event of nodal failure.”
- p. 355: “this systemic diversity objective should probably be given much greater prominence by the regulatory community”

**Numbers.** n* = 4.14 (Caccioli et al.); z = p(N - 1); fail if f(1 - h) > c; loan shocks attenuate by about z. Homogeneity toy (ours, computed; S2b reran in Python: ratios 64.8, 2,755.7, 4.31e7; Stirling 65.7, 2,778.8, 4.33e7): with ε = 0.01 and N = 10, the heterogeneous system fails with probability ε^N = 1e-20 and the homogeneous system with N^N ε^N / N! = 2.76e-17, about 2,756 times larger, while one diversified bank's chance of failing falls from 0.01 to 2.76e-17. For N = 6 the ratio is 64.8; for N = 20, about 4.3e7. The ratio N^N / N! is about e^N / √(2πN).

**Instance.** The 2007-8 crisis as a banking ecosystem; Lehman as a super-spreader (p. 354).

**Careful!**
- Traps 42 and 43.
- The card's lens 2 says "complexity and homogeneity versus stability, by analogy with ecology". Complexity is the ecological and Caccioli et al. result; homogeneity is the banking toy; the paper does NOT show that connectivity always lowers stability (loan shocks attenuate with z, liquidity shocks amplify).
- The homogeneity toy's "each bank is safer" depends on the N asset classes being independent and each bank holding all of them. It is an extreme-case toy with "oversimplified" built in.
- Two of the main supports for homogeneity are manuscripts in preparation in 2011.

**Toy idea.** A new lab widget with two sliders (m and α) showing mα² against 1 for a random web (ecology, labelled as such) and, separately, the N-bank homogeneity toy with the two probabilities above. Say "toy, ours" and keep the ecology widget out of the banking claims.

---

## V6. Harari, *Nexus* (2024) [WITHDRAWN]

V6a–V6e were drawn from a file that came from a pirate e-book site; it was deleted and was not consulted at S2b. Nothing from V6 may be used, and every cross-reference to V6 or to "Nexus PDF n" elsewhere in this file has been removed or marked WITHDRAWN (traps 44–47, 49; V8; challenges 3, 4, 5, 9, 10). *Nexus* may be cited only from `nexus-penguin-sample.pdf` (Prologue; paperback roman pages, trap 7) and `guardian-2024-nexus-extract.txt` (no pages), through S2 unit A4. Re-verify any further *Nexus* claim from a legitimate copy before use.

---

## V7. Searle (1995), *The Construction of Social Reality* [FIXED] [SEEN, printed pp. 14-57 (p. 58 is not in the scan), 68-85, 88-89, 93, 95-97, 99-100, 104, 106-111, 114, 117-124, 140-142 (p. 142 read at S2b); the rest UNSEEN]

**Source.** `searle-1995-construction.pdf` (scan) with OCR in `searle-1995-construction.txt` ("=== PDF PAGE n ===" headers). Offset: see the table above (-9 to printed p. 57, then -8). **Every quote below was checked against the rendered page image [img].** S2b re-checked every quote against the OCR text and re-read the page images of printed pp. 14, 22, 24, 25, 27, 28, 33, 34, 37, 41, 42, 43, 45, 47, 48, 51, 55, 56, 69, 70, 96, 100, 111, 117, 118, 141. UNSEEN printed pages (not read): 1-13, 59-67 (the opening of ch. 3), 86-87, 90-92, 94, 98, 101-103, 105, 112-113, 115-116, 125-139, 143 onward (S2b read p. 142). A full-text search of the OCR for robot, artificial intelligence, Turing, Chinese room and strong AI finds nothing (trap 48).

### V7a. Collective intentionality and what can have it [OK]
- *Asserts.* "Many species of animals, our own especially, have a capacity for collective intentionality" (p. 23): not only cooperation but "that they share intentional states such as beliefs, desires, and intentions". It is "a biologically primitive phenomenon that cannot be reduced to or eliminated in favor of something else" (p. 24). "No set of ‘I Consciousnesses,’ even supplemented with beliefs, adds up to a ‘We Consciousness’" (p. 24); "the individual intentionality that each person has is derived from the collective intentionality that they share" (p. 25). The "we" lives in individual heads: "all my mental life is inside my brain" yet its form is "we intend" (pp. 25-26). A "social fact" is "any fact involving collective intentionality"; institutional facts are a subclass (p. 26).
- *What can have it.* Hyenas hunting a lion are a social fact but not an institutional one (p. 38). For institutions, "only beings that have a language or some more or less language-like system of representation can create most, perhaps all, institutional facts" (p. 37; stated as an "apparent feature", hedged "perhaps all"; defended in ch. 3, p. 69). Animals in a pack "can have all the consciousness and collective intentionality they need" yet cannot have money (p. 70): the barrier is representing deontic powers, not collective intentionality. Ant colonies "have slaves" or hives "have queens" are "harmless metaphors" (p. 37). Animals can "cooperate in the hunt, share their food, and even have pair bonding. But they cannot have marriages, property, or money" (p. 70), because they cannot represent the deontic phenomena: "He still is not buying the food and the bills are not money to him" (p. 70, the dog trained to fetch dollar bills).
- *Hedge.* Searle is "not certain that the ethologists are justified in attributing so much collective intentionality to the animals" (footnote, p. 40).
- *Machines.* Not discussed (trap 48). The nearest passage is pp. 140-141 (V7g).
- **Quotes.** p. 24: “Collective intentionality is a biologically primitive phenomenon that cannot be reduced to or eliminated in favor of something else.” | p. 24: “No set of ‘I Consciousnesses,’ even supplemented with beliefs, adds up to a ‘We Consciousness.’” | p. 25: “the individual intentionality that each person has is derived from the collective intentionality that they share” | p. 37: “only beings that have a language or some more or less language-like system of representation can create most, perhaps all, institutional facts” | p. 70: “He still is not buying the food and the bills are not money to him.”

### V7b. Assignment of function [FIXED]
- *Asserts.* "functions are never intrinsic to the physics of any phenomenon but are assigned from outside by conscious observers and users" (p. 14); "Functions, in short, are never intrinsic but are always observer relative." Examples include "Chairs, bathtubs, and computers" as artefacts built to serve a function (p. 14). Three kinds: nonagentive (the heart pumps blood), agentive (a screwdriver), and a special subclass of agentive functions whose function is to represent or mean something (pp. 20-23).
- *Condition on agentive functions.* "for all cases of agentive function, someone must be capable of understanding what the thing is for, or the function could never be assigned" (p. 22). Money "may simply have evolved without anyone ever thinking, ‘We are now imposing a new function on these objects’" (p. 22; S2b: word order corrected). But the same paragraph adds: "At least some of the participants in the system of exchange must understand, consciously or unconsciously, that money is to buy things with" (p. 22; S2b addition, an unhedged condition directly relevant to any machine "participant").
- *Hedges.* The nonagentive/agentive line has "no sharp dividing line" (p. 20).
- **Quotes.** p. 14: “functions are never intrinsic to the physics of any phenomenon but are assigned from outside by conscious observers and users” | p. 22: “someone must be capable of understanding what the thing is for, or the function could never be assigned” | p. 41: “the collective intentional imposition of function on entities that cannot perform those functions without that imposition”

### V7c. Status functions and "X counts as Y in C" [FIXED]
- *Asserts.* Constitutive rules "create the very possibility of playing chess", and "characteristically have the form ‘X counts as Y’ or ‘X counts as Y in context C.’" (p. 28). "institutional facts exist only within systems of constitutive rules" (p. 28). Rules versus conventions: "constitutive rules in general are not in that sense arbitrary" (p. 28).
- *The step.* The key element in the move from imposed function to institutional facts is "the imposition of a collectively recognized status to which a function is attached" (p. 41), labelled "status functions". The Y term "has to assign a new status that the object does not already have", and "there has to be collective agreement, or at least acceptance" (p. 44). "Collective agreement about the possession of the status is constitutive of having the status" (p. 51), and the status is essential to performing the function.
- *Iteration.* The formula iterates: the X term at a higher level can be the Y term of a lower level (citizen, then President) (p. 80); promise, then contract, then marriage (pp. 82-83).
- *The basic structure.* "We collectively accept, acknowledge, recognize, go along with, etc., that (S has power (S does A))" (p. 111). **Hedge on this very claim:** "There is exactly one primitive logical operation by which institutional reality is created and constituted" is introduced as "the following hypothesis. I do not know if it is true and I certainly have not demonstrated it, but it is worth further exploration" (pp. 110-111).
- *Deontic powers.* Status functions confer "conventional power": "all deontic status-functions are matters of conventional power" (p. 100); "roughly speaking, everything turns out to be deontic" (p. 109; S2b: hedge restored). Honorific statuses are "an interesting class of exceptions" to the claim that all institutional facts involve power (p. 96). Searle calls the limit on what statuses can be created (only those whose function can be guaranteed "simply by collective agreement or acceptance") "perhaps, the most mysterious feature of institutional facts" (p. 47).
- **Quotes.** p. 28: “‘X counts as Y’ or ‘X counts as Y in context C.’” | p. 28: “institutional facts exist only within systems of constitutive rules” | p. 41: “the imposition of a collectively recognized status to which a function is attached” | p. 51: “Collective agreement about the possession of the status is constitutive of having the status” | p. 111: “We collectively accept, acknowledge, recognize, go along with, etc., that (S has power (S does A)).” | p. 100: “let us say that all deontic status-functions are matters of conventional power”

### V7d. Institutional facts: brute and institutional; language [OK]
- *Asserts.* "Brute facts exist independently of any human institutions; institutional facts can exist only within human institutions." (p. 27). Institutional facts "exist, so to speak, on top of brute physical facts" (p. 35). "Thus there are no institutional facts without brute facts" (p. 56): the substrate can be "a bit of paper or a blip on a computer disk" (p. 56); "Most money is now in the form of magnetic traces on computer disks" (p. 34).
- *Self-reference.* "for social facts, the attitude that we take toward the phenomenon is partly constitutive of the phenomenon" (p. 33). "Part of being a cocktail party is being thought to be a cocktail party" (p. 34).
- *Language.* The status "exists only if people believe it exists, and the reasons function only if people accept them as reasons" (p. 69); it needs a symbolic vehicle because "empirically speaking, there isn’t anything else there" (p. 69).
- *Declarations.* Many institutional facts are created by performative utterances (p. 34); when the Treasury says a note is legal tender, "they are declaring it to be legal tender, not announcing an empirical fact that it already is legal tender" (p. 55); "You cannot, for example, make a touchdown just by saying you are making it" (p. 55): not all can be declared.
- **Quotes.** p. 27: “Brute facts exist independently of any human institutions; institutional facts can exist only within human institutions.” | p. 33: “the attitude that we take toward the phenomenon is partly constitutive of the phenomenon” | p. 56: “Thus there are no institutional facts without brute facts.” | p. 34: “Most money is now in the form of magnetic traces on computer disks.” | p. 69: “The status exists only if people believe it exists, and the reasons function only if people accept them as reasons.” | p. 55: “they are declaring it to be legal tender, not announcing an empirical fact that it already is legal tender”

### V7e. Money as the central example [FIXED]
- The three kinds (p. 41-42): commodity money, contract money, fiat money; "in the case of fiat money the stuff is valuable because it is a medium of exchange" (p. 42; the first half of the sentence says commodity money is a medium of exchange because it is valuable).
- The medieval story (pp. 42-43), which Searle says he is "using ... only to illustrate certain logical relations" (p. 42; S2b: not p. 43): certificates as good as gold; "we can forget about the gold and just have the certificates" (p. 43). A Federal Reserve note redeemed for "another twenty dollar Federal Reserve note" (p. 43).
- The bill: the X term (right material, pattern, issued by the Bureau of Engraving and Printing) counts as the Y term "money, i.e., U.S. paper currency" (pp. 45-46; S2b: the Y term is not "legal tender"). The printed line "This note is legal tender for all debts, public and private" is a declaration (p. 55; also p. 48).
- Tokens and types (pp. 32-33, 53): a bill that fell into the cracks of the floor and was never used or thought of "would still be money"; a counterfeit that no one knows is counterfeit is not money though all think it is; "where the type of thing is concerned, the belief that the type is a type of money is constitutive of its being money" (p. 33). The reason, by p. 53, is codification: an official, codified institution makes self-reference "a feature of the type".
- Abuses the rule makes possible: "the general rule creates the possibility of abuses that could not exist without the rule, such as counterfeit money" and hyperinflation (p. 48).
- Evolution without awareness *of the mechanism*: participants may think "This is money" but "need not think, ‘We are collectively imposing a value’" (p. 47), and "do not in addition have to recognize that they are so recognizing" (p. 47). What they lack is awareness of the structure, not recognition of the status: "As long as people continue to recognize the X as having the Y status function, the institutional fact is created and maintained" (p. 47).
- **Quotes.** p. 42: “in the case of fiat money the stuff is valuable because it is a medium of exchange” | p. 43: “we can forget about the gold and just have the certificates” | p. 48: “the general rule creates the possibility of abuses that could not exist without the rule, such as counterfeit money” | p. 47: “They do not in addition have to recognize that they are so recognizing”

### V7f. Continued acceptance, and whether rules can work without it [FIXED]
- *Asserts.* "there must be continued collective acceptance or recognition of the validity of the assigned function; otherwise the function cannot be successfully performed" (p. 45, "continued" in italics). Agreeing with the original assignment is not enough: "we must continue to accept it as money or it will become worthless" (p. 45). "the individuals directly involved and a sufficient number of members of the relevant community must continue to recognize and accept the existence of such facts" (p. 117). "Because institutions survive on acceptance, in many cases an elaborate apparatus of prestige and honor is invoked to secure recognition and maintain acceptance" (p. 118). Property rights "cease to exist" if most members refuse to acknowledge them (p. 117).
- *What acceptance needs.* The participants need not "be aware of what is actually happening" (p. 96): "as long as they continue to recognize his authority, he has the status-function of king, regardless of whatever false beliefs they may hold" (p. 96). The false beliefs are about *why* (divine anointing), not about *whether* he is king. The bar is still recognition: "The status exists only if people believe it exists" (p. 69). "Sheer physical power is unaffected by collective agreement" (p. 96).
- *Can force replace it?* No, for the institutional fact: "In fact power grows out of organizations, i.e., systematic arrangements of status-functions" (p. 117), and guns are ineffectual except to those who use them "in cooperation with others and in structures" with recognized lines of authority (p. 117, paraphrase with a short quote). On force, p. 118 says that where "consent is essential" institutions use "pomp, ceremony, and razzmatazz" to keep acceptance, and "Jails find these devices less necessary because they have brute force." Reading this as "where consent is not essential, force can do the work" is ours (S2b); Searle's claim is only that jails need fewer prestige devices.
- *Can a rule work without acceptance?* Regulative rules can bind by sanction, but sanction itself needs a status: the criminal law is "regulative, not constitutive", yet to make it work "there must be sanctions, and that requires the imposition of a new status" (p. 50). Constitutive rules cannot: "If you don't follow at least a large subset of the rules, you are not playing chess" (p. 28). An institution can be started by acting "as if it did exist" (the Declaration of Independence), but it succeeded because the founders "created and sustained acceptance" with community support and force (pp. 118-119).
- **Quotes.** p. 45: “there must be continued collective acceptance or recognition of the validity of the assigned function; otherwise the function cannot be successfully performed” | p. 45: “we must continue to accept it as money or it will become worthless” | p. 117: “the individuals directly involved and a sufficient number of members of the relevant community must continue to recognize and accept the existence of such facts” | p. 117: “In fact power grows out of organizations, i.e., systematic arrangements of status-functions.” | p. 118: “Because institutions survive on acceptance, in many cases an elaborate apparatus of prestige and honor is invoked to secure recognition and maintain acceptance.” | p. 118: “One way to create institutional facts in situations where the institution does not exist is simply to act as if it did exist.” | p. 96: “as long as they continue to recognize his authority, he has the status-function of king, regardless of whatever false beliefs they may hold”

### V7g. The nearest Searle comes to machines (printed pp. 140-141, the Background) [OK, one addition]
- *Asserts.* The Background "can be causally sensitive to the specific forms of the constitutive rules of the institutions" without "actually containing any beliefs or desires or representations of those rules" (p. 141; one 29-word sentence, quoted in two parts). He says the Background is "more in tune with ... the connectionist model of cognition" than with a serial program, and "I think that’s right", **but** he adds that this "still leaves us with the challenge posed by those who oppose connectionism", namely what internal structure gives structured output (p. 141).
- *Hedge.* He says he is "not satisfied" with either way of thinking of the Background (p. 140).
- *S2b addition (p. 142, read at S2b; the brief listed it as UNSEEN).* Money users "do not know those rules", and "in general, I am arguing", they "do not apply them consciously or unconsciously"; they have "a set of dispositions that are sensitive and responsive to the specific content of those rules" (p. 142 [img]). This is the strongest passage for the view that following an institution does not need a representation of its rules. It is about human users and does not touch the machine case.
- **Careful.** This is about how humans follow institutional rules without representing them. It does not say a machine can accept a status. Whether a system without consciousness can be part of the "we" is ours.
- **Quotes.** p. 141: “the Background can be causally sensitive to the specific forms of the constitutive rules of the institutions” | p. 141: “without actually containing any beliefs or desires or representations of those rules”

**Numbers.** None. Classifications: Searle's fiat/contract/commodity money; his count "exactly one primitive logical operation" (hypothesis).

**Instance.** Money (the dollar bill, fiat money), the Declaration of Independence (pp. 118-119), the Korean "police action" versus "war" (p. 89).

**Careful! (Searle overall)**
- Traps 47, 48 and 50.
- Searle's claim that institutional reality needs the "we" is about *human and animal* minds. That a machine cannot be in the "we" is an inference that Searle does not draw.
- **S2b, major fix.** Acceptance can be implicit in form ("go along with", p. 111) and participants can be unaware of the *mechanism* (pp. 47, 96). But Searle does not lower the bar below belief: "The status exists only if people believe it exists" (p. 69); for types, "the belief that the type is a type of money is constitutive of its being money" (p. 33); "at least some of the participants" must understand what money is for (p. 22). Do not write that for Searle the bar is "lower than belief". What does cut against the card's flat "no (Searle 1995)": Searle never raises the machine case, and his Background passage (pp. 141-142) shows rule-following without represented rules in humans.
- The card's line "Can a token become money with no human accepting it?" has Searle's answer: a *token* yes if the *type* is accepted (and codified); the type, no (trap 50).
- "X counts as Y" on the bill is a declaration by an authority; Searle does not say who or what may declare (a person, an office, a machine) beyond "appropriate circumstances" and "the wrong person or in the wrong circumstances" (p. 54).

**Changes vs S2.** Replaces F1 (Searle via the SEP) with the book itself for status functions, "X counts as Y in C", continued acceptance and the money story. Keep F1 only for the SEP's one-paragraph summary.

**Toy idea.** The "X counts as Y in C" table: three X-terms, a C-term, and a Y-term (a status with a power); then a second table that iterates (citizen, then President). A "who declares?" column makes the card's "declare" job concrete. Say "toy, ours".

---

## V8. What would "fully automated" require, job by job [partly sourced, mostly OURS] [FIXED]

The five-job table is ours (topic card section 2). The sources below support only the cells marked. S2b removed every citation to the withdrawn *Nexus* file and corrected the IMF scopes.

| Job | What "no human intervention" would require | Support in the sources | Status |
|---|---|---|---|
| **Run** (carry out the work) | Matching, settlement, execution done by software. | The E-mini is "fully electronic" with "no market maker obligations" (KKST p. 7) and "fully automated" (p. 28). US algorithmic share about 70% of equities, over half of futures (IMF p. 86); "algorithmic" includes simple execution rules (IMF p. 101). | Sourced: largely automated in some markets. |
| **Decide** (choose what to do) | Software chooses the objective and the trades, with no human setting the goal or approving size. | Not yet: in 2010 a firm (a mutual fund complex) chose to sell, as a hedge, and chose the algorithm (KKST p. 2); that a person decided is our reading. IMF: most outreach participants are "quite uncomfortable" with autonomous AI trading "without human oversight" (p. 78); "all participants" expect a human in the loop "in the near term (three to five years)" (p. 83); "complete autonomy is not anticipated soon" (p. 83); sophisticated AI is mostly a signal into a system where "a human trader may ultimately make the trading decision" (p. 82); 59% of investment managers do not plan to integrate AI into executing investment decisions (Fig 3.5, p. 83, Mercer survey). Radically new AI-made strategies "remain mostly speculative" (p. 78). Counter-trend: many deep-learning models retrain "without any human oversight" (G&B p. 12), yet developers still set hyperparameters (G&B p. 9). | Sourced: deciding *what to trade at scale* is not automated; execution rules are. |
| **Check** (verify and regulate) | Software verifies and halts; and something verifies that software. | A pre-set automated safeguard already ran in 2010 (CME Stop Logic, KKST p. 2). Supervisors in the outreach "use AI-driven SupTech tools" (IMF p. 83); SupTech (not only AI) adoption 79% of advanced economies in 2023 (IMF fn 24, p. 95); the IMF asks whether circuit breakers "may need to be re-parameterized" (p. 96). A supervisory model "may unknowingly promote uniformity" and, if "perturbed or fooled", could cause "outsize risk" (G&B p. 25). Arora et al.: under a conjecture, in a simple model, a bounded buyer may be unable to detect tampering even ex post (pp. 51, 55, 59), and tamper-resistant designs exist only in the simple model (pp. 60-61). Harari (Guardian extract, S2 A4): "As long as humanity stands united, we can build institutions that will regulate AI" followed at once by "Unfortunately, humanity has never been united" (quote both; WRITING §9). | Sourced: partly automated already; each automated checker raises a further check. "The end of the regress is a human institution" is OURS (the Harari passage for it was withdrawn). |
| **Declare** (say what counts: money, law, a person) | Software creates statuses that people (or other software) treat as binding. | Searle: statuses exist through collective acceptance and need language-like representation (pp. 37, 69); the status "exists only if people believe it exists" (p. 69); the book does not say whether machines can be in the "we" (trap 48). | **OURS** as a verdict. Sources give the criteria (acceptance, representation, continued acceptance), not a ruling on machines. |
| **Answer** (bear losses; be held responsible) | Something that can be fined, jailed, sued or blamed takes the loss. | The IMF: "institutions are responsible for AI systems they deploy" (p. 93); most participants want a human in the loop partly for "liability" reasons (p. 78). G&B: "Human agency and traditional intervention approaches may be lost" with low explainability (p. 13). | Sourced for the *current* legal position; whether an AI could ever "answer" is OURS. |

**What the sources add to "fully automated".**
- Run: yes, in places. Decide: not by the evidence of 2024. Check: partly. Declare and answer: the sources describe the human position and do not test the machine case.
- The post must label as ours: (a) the five-job split; (b) any sentence that a machine "could not" declare or answer; (c) "a human institution ends the regress of checkers".

---

## Challenges to the card's provisional thesis (section 5 of topic-card-v2) [FIXED]

1. **"Run and decide can be automated, and in markets largely are."** "Run" yes. "Decide" no, on the IMF's evidence (pp. 78, 82, 83) and in KKST (a fund chose to sell). The IMF's "algorithmic" lumps execution rules with decisions (p. 101), so the card's two rows cannot be filled from one IMF number (traps 35, 36).
2. **"The cost is correlated failure."** One of two IMF scenarios (Table 3.1, p. 89: "highly uncertain"); IMF finds risks "appear contained" now (p. 92) and credits efficiency and liquidity gains (p. 87). KKST's 2010 event is a sell program meeting thin depth, not shared models (trap 40). G&B's herding is a hypothesis about a future mature stage.
3. **"Check can be partly automated."** Understated: a pre-set automatic check already acted in 2010 (CME Stop Logic) and supervisors in the IMF outreach already use AI-driven SupTech tools (IMF p. 83; the 79% figure is SupTech in general, p. 95). The new point from the sources: G&B's "Regulatory deep learning models may unknowingly promote uniformity in the agents they regulate" (p. 25). (S2b: the Harari "human institution at the end of the regress" support was from the withdrawn file; that claim is now ours.)
4. **"Declare ... cannot be handed over ... (Searle 1995)."** Searle says status functions need continued collective acceptance and a language-like representation; he does not say machines cannot join it, and the book never raises the case. So the flat "cannot (Searle 1995)" is ours and the post should say so. But do **not** argue that his bar is "lower than belief": "The status exists only if people believe it exists" (p. 69); unawareness in Searle is about the mechanism, not the status (pp. 47, 96). (S2b: major fix; the Harari sentence that closed this item was withdrawn.)
5. **"Machines that treat each other as persons."** No source in the verified set says machines would accept each other as persons, and Searle does not discuss machines (trap 48). (S2b: the Harari legal-personhood and "cannot believe" support was from the withdrawn file; removed.)
6. **Hook: "People had built a pause into the market's own rules, and that pause helped stop the fall."** Fine as "prices stabilised after a five-second pause that a pre-set rule triggered" (KKST p. 2, quoting the CFTC-SEC). The JF paper does not test whether the pause caused the recovery, and the authors' pause recommendation is in the 2014 working paper only (trap 32). "About 36 minutes" is ours (trap 34). "Computer programs ran a market into a crash and back" overstates (trap 35).
7. **Lens 2: "m·a² > 1 ... complexity and homogeneity versus stability, by analogy with ecology."** True of May's random webs only (write mα² > 1). In Haldane and May's own banking toy, more connectivity *attenuates* loan shocks and *amplifies* liquidity shocks; homogeneity is the stronger result. Keep the widget in the ecology panel (traps 42, 43).
8. **Lens 1: "Arora et al.: some products cannot be checked by any realistic checker."** Overstated: under a conjecture, in a simple model, asymptotically, "only a first step" (V4). The authors also offer designs (tree of majorities) that a checker *can* check in the simple model.
9. **Harari's own limits.** [WITHDRAWN as written; it rested on V6.] What stays: the card says Harari "asserts" that "anything made of words will be taken over by AI": that line is Davos 2026 (S2 A3b); cite it there. The *Nexus* lines usable in the fold-out are only those in S2 unit A4 (Penguin sample Prologue, Guardian extract), sorted by firmness (WRITING §9).
10. **Number tension.** [WITHDRAWN in part.] The Harari "more than 90 percent" forex figure came from the withdrawn file. Keep only the IMF figure (US FX algorithmic share about 27%, read from Fig 3.8) and do not pair it with any unchecked forex number.

## Open items

- The CACM 2011 text (V4) is UNSEEN; ask Kunhao for a copy if the post will cite the published article.
- The JF's journal pagination (V1) is UNSEEN; the page numbers here are the manuscript's.
- Nexus: V6 WITHDRAWN (pirate file deleted). Any new *Nexus* claim needs a legitimate copy (Kunhao's purchased copy) and a fresh S2 check.
- IMF figure values are read from images (trap 37).
- Searle: printed pages 1-13, 59-67, 86-87, 90-92, 94, 98, 101-103, 105, 112-113, 115-116, 125-139, 143 onward not read (S2b read p. 142); chapters 6-8 (the Background in full, realism, truth) are UNSEEN. Printed p. 58 is absent from the scan.
- Gensler and Bailey: SSRN number on the file is 3766555; MANIFEST table B says 3723132. Cite 3766555 with the "November 1, 2020" working-paper date.
- Cited but unseen: May (1972), Caccioli et al. (2009), Beale et al. (in preparation), Khandani and Lo, Lo (2012), Kirilenko and Lo.

## Writer must not use (S2b)

1. Anything cited to "Nexus PDF n", V6a–V6e, or the deleted `harari-2024-nexus.pdf` (including "computer-to-computer chains", "inter-computer realities", "cannot ‘believe’", "no purely technological solution", "bots don’t have rights", "more than 90 percent" forex, any chapter placement).
2. "The IMF says autonomous AI trading is mostly speculative" (the phrase is about radically new GenAI strategies, p. 78).
3. "For Searle the bar is lower than belief" (contradicted by pp. 33, 69).
4. "Searle says machines cannot be part of the we" (he never discusses it; ours).
5. "Anything made of words … is not in *Nexus*" (only: not in the sample or extract; it is Davos 2026).
6. "70% of trading is AI" (algorithmic, US equities, includes simple rules).
7. "Supervisors use AI: 79%" (79% is SupTech adoption in general).
8. "A person decided to sell in 2010" without "our reading" (the source says a mutual fund complex).
9. "The pause stopped the crash" as the JF's finding (it is the CFTC-SEC narrative; untested in the JF).
10. "The IMF's winner-takes-all comes from simulations" (empirical literature, Baron et al. 2017).
11. The Searle Y term "legal tender" for the bill (Y = money, U.S. paper currency; "legal tender" is the declaration).
12. "Searle concedes force can replace acceptance" (ours; he says jails need fewer prestige devices).
13. Any Haldane–May claim that connectivity always lowers stability, or mα² > 1 applied to banks.
14. "Arora et al. show some products cannot be checked by any realistic checker" (conjecture, simple model, asymptotic, "only a first step").

