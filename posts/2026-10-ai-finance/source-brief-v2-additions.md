---
id: 2026-10-ai-finance/source-brief-v2-additions
type: source-brief-additions
stage: S1b (planner), post 02 v2
post: "Could a society run itself on AI?" (topic-card-v2.md: five jobs, run, decide, check, declare, answer)
built_from: the seven sources added by Kunhao on 2026-10-18, read in posts/2026-10-ai-finance/sources/ (PDF plus text extract each)
checked: 2026-10-18
companion: source-brief.verified.md (S2). This file ADDS units; it does not replace units that are not named below.
grounding: Every unit marked SEEN was read at the source page. Quotes were matched against the text layer by script (letters and digits only) and are at most 25 words. Quotes whose text layer is lossy, and all Searle quotes (OCR), were also checked against the rendered page image; those are marked [img].
---


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
| Harari, *Nexus* (2024) | harari-2024-nexus.pdf | **No printed pages** (a reflowed ebook, 592 PDF pages, "OceanofPDF.com" marks on the pages). Cite chapter, subheading and PDF page of this file. |
| Searle (1995) | searle-1995-construction.pdf (scan) + ocr-searle/p-NNN.txt | **The offset changes inside the book.** OCR p-023 to p-066 = printed 14 to 57 (offset -9). From p-067 (chapter 3 opener, printed 59) on, printed = OCR page - 8. Always use the printed number in the page header, not the arithmetic. The combined OCR file is now complete (247 pages). |

**New traps (continuing the S2 numbering; 1-31 are in source-brief.verified.md).**

32. *Kirilenko JF 2017 is not the 2014 working paper.* Four things the writer may have taken from the working paper are NOT in the JF text: "did not cause the Flash Crash, but contributed to it"; the recommendation of short trading pauses; "temporarily shake the confidence of some market participants"; "about 36 minutes". Cite the version you quote. See V1.
33. *The time zone in the JF's block quote is internally inconsistent.* p. 2 prints "At 2:32 [CT] p.m." inside the CFTC-SEC quotation (the "[CT]" is the authors' insertion, checked on the page image). The paper's own analysis windows begin at 13:32:00 CT (p. 22). The working paper says "2:32pm ET". 13:32 CT is 14:32 ET. So 2:32 p.m. in the quotation is Eastern time. Say "2:32 p.m. Eastern", and do not repeat "[CT]".
34. *"About 36 minutes" is ours.* It is 2:32 to 3:08 p.m. in the CFTC-SEC times that the JF quotes. The JF itself never says "36 minutes". The E-mini windows in the JF (13:32:00 to 14:08:00 CT) also add up to 36 minutes.
35. *Who decided to sell in 2010?* A mutual fund complex (people) decided to sell 75,000 contracts as a hedge and chose an automated execution algorithm. The algorithm set only the pace (9% of previous-minute volume). The JF's finding about high-frequency traders is "did not change", not "caused". The hook "computer programs ran a market into a crash" overstates; use "an automated sell program, started by a person, met a market with little buy-side depth".
36. *"Algorithmic" is not "AI".* The IMF glossary (p. 101) defines algorithmic trading as "an algorithm independently executes trading decisions" and says it can be as simple as "basic trading rules". The IMF's 70% is algorithmic trading, not AI trading. Never write "70% of trading is AI".
37. *IMF figures read from charts are approximate* (+-2 points): Fig 3.5 and Fig 3.8 below. The one number in the text is "about 70 percent" (p. 86), for US equities only. Panel 1 of Fig 3.8 draws US equities at about 67%.
38. *"Human in the loop" at the IMF has three scopes.* p. 78: "most participants" see it as essential for "regulatory, risk management, liability, and ethical reasons". p. 83: "all participants" expect it to persist "in the near term (three to five years), especially for large capital allocation decisions". The evidence is an outreach with 27 detailed stakeholder responses and 10 supervisors (Box 3.1, p. 98): qualitative, not a survey of practice.
39. *Gensler and Bailey: channels versus pathways.* The paper has three channels (monocultures and herding, network interconnectedness, regulatory gaps; pp. 3, 17) and five pathways (data, model design, regulatory, algorithmic coordination, user interface; p. 3). "Model design" is a pathway, not a fourth channel. The line "AI can easily mask who's at fault" is MIT Sloan's gloss; it is not in the paper (trap 15 stands, but the paper is now SEEN).
40. *Gensler and Bailey versus Kirilenko et al. on flash crashes.* G&B write "It is hypothesized that herding and crowding in high frequency algorithmic trading is partially responsible for causing flash crashes" (p. 22). KKST find that the high-frequency traders' inventory behaviour did not change. Do not present 6 May 2010 as an instance of model monoculture.
41. *The file `arora-2011-cacm.pdf` is the ICS 2010 extended abstract* (same md5 as arora-ics2010.pdf). The CACM text of 2011 is UNSEEN. `arora-2011-cacm-authorcopy.pdf` is the 2009 working paper (S2 units C3, C4). Cite the ICS paper as "Arora et al., ICS 2010, extended abstract".
42. *May's criterion is ecology.* Haldane and May state "mα² > 1" for random assemblies of species (for N much larger than 1; m links per species, α their average strength). They do NOT apply it to banks. Their banking results come from the interbank toy model (z, c, h, f), and there connectivity cuts both ways (V5).
43. *The text layer drops Greek letters* in Haldane and May (ε as "e", α as "a", θ and γ as "h" and "c" in running text; ">" as "."). The "mα² > 1" line was checked on the page image [img]. Re-check any symbol before print.
44. *Nexus provenance.* The PDF is an ebook with OceanofPDF.com marks and no printed pages. The copyright page reads "First edition. | New York: Random House, [2024]" (US) and lists a Fern Press (UK) edition; the ebook ISBN is 9780593734247. Trap 7 (paperback sample, roman numerals) still applies to those pages. Tell Kunhao the file's provenance is unclear.
45. *"Anything made of words" is not in Nexus.* A text search of the ebook for "made of words" finds nothing. That line is from Davos 2026 (S2 unit A3b).
46. *Chapter placement.* "Inter-computer realities" (Pokémon, Google rank, financial devices) are in ch. 8, subheading COMPUTER MYTHOLOGY, not ch. 7. The passage "computers dominate the financial markets" is in ch. 6 (subheading LINKS IN THE CHAIN), not ch. 7. Ch. 7 (RELENTLESS) is about surveillance.
47. *Harari does not cite Searle* (no hit in the text), and Harari's inter-computer realities are not Searle's status functions: Harari concedes computers "cannot ‘believe’" (ch. 8). The match between the two is ours.
48. *Searle on AI.* A search of the whole OCR text for robot, artificial intelligence, Turing, Chinese room and strong AI finds nothing. "Computer" occurs only in passing (printed pp. 14, 34, 56, 84, 140, 168; an endnote). The book does not say whether a machine can be one of the "we". Any such claim is ours.
49. *FX: IMF versus Harari.* IMF Fig 3.8 (p. 86): algorithmic share of US foreign exchange trading about 27%. Harari (ch. 6, PDF 227): "More than 90 percent of this trading is already done by computers talking directly with other computers" (forex). The definitions differ (share of algorithmic activity versus computer-to-computer trading) and the geography differs (US versus global); Harari's endnote 43 cites a textbook, a Forbes explainer and the BIS triennial survey. We did not check the 90% in them. Do not put the two numbers side by side as if they measured the same thing.
50. *Searle on tokens versus types.* A token can be money though nobody thinks it is (the bill in the cracks of the floor, p. 32); the type cannot be (p. 33). This is the exact answer to the card's guess 3 ("Can a token become money with no human accepting it?").

---

## V1. Kirilenko, Kyle, Samadi and Tuzun (2017), JF 72(3): the Flash Crash [SEEN, pp. 1-29]

**Source.** `kirilenko-2017-flashcrash-jf.pdf`, accepted manuscript (offset 0). Read in full (text pp. 1-28; tables and figures skimmed). Authors' disclaimer: three were CFTC staff or contractors; views are theirs.

**Claims**

*Timeline (the CFTC-SEC narrative quoted on pp. 2-3; fn 3, p. 5 says the CFTC-SEC narrative "was based in part on the preliminary analysis in the original version of this paper").* All clock times are as quoted (Eastern; see trap 33).
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
- Shares of volume (p. 17): HFTs 34.22% on May 3-5, 28.57% on May 6; Market Makers 10.49% and 9.00%.
- Inventories (p. 18): HFTs never held more than about 4,000 contracts; Market Makers never more than 1,500; combined intermediary net inventories did not exceed 6,000 contracts on any of the four days (p. 5), "an order of magnitude smaller" than the 75,000 sell program. In the "down" phase Fundamental Sellers out-sold Fundamental Buyers by 33,944 contracts (fn 30, p. 22).
- Behaviour (pp. 19-23): shortly before the pause the HFTs "aggressively liquidated approximately 2,000 contracts accumulated earlier, which coincided with significant additional price declines" (p. 19, as discussed in CFTC-SEC). Market Makers did not liquidate until after the pause. The HFTs' inventory-price relationship "did not significantly change" in the crash; the Market Makers' relationship did change (F-test rejects at 1%, p. 23).
- HFTs behave "more consistent with the theories of quote sniping or latency arbitrage" than with traditional market making (pp. 24-28): when HFTs are net buyers, prices rise 17% of a tick in the next second (May 3-5).

*Conclusions and hedges (p. 28).*
- Consistent with "the theory of limited risk-bearing capacity". The most active intermediaries did not change their inventory dynamics "when faced with large liquidity imbalances", unlike textbook market makers.
- The October 15, 2014 US Treasury flash event "reignited discussion about the vulnerability of liquid automated markets"; such events "may be a feature of the ‘new normal’".
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

**Instance.** A person-chosen automated sell program, a market with almost no buy-side depth, and an automatic, pre-set pause. Two jobs are visible: "run" (the algorithm and the matching engine) and "check" (the Stop Logic rule). "Decide" (sell 75,000) was human.

**Careful!**
- Traps 32 to 35 and 40.
- The paper does not say that HFTs caused, or did not cause, the crash. Its statement is about their inventory behaviour. The "did not cause ... but contributed" sentence belongs to the 2014 working paper only.
- The paper does not show that shared models or herding drove 6 May 2010.
- The 5-second pause is a pre-set rule, not a human decision. The causal claim that it "helped stop the fall" is the CFTC-SEC report's, quoted by the paper; the JF paper does not test it.
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

## V2. IMF, Global Financial Stability Report, October 2024, ch. 3 [SEEN, pp. 77-106]

**Source.** `imf-2024-gfsr-ch3.pdf`: "Advances in Artificial Intelligence: Implications for Capital Market Activities", GFSR October 2024 ("Steadying the Course: Uncertainty, Artificial Intelligence, and Financial Stability"). Authors: Abbas, Conde Vitureira, Diaby, Fernandez Dionis, Ferrante, Grolleman, Kramer, Lim, Mosk, Singh, Stobo (p. 77). Offset +76. Read: the whole chapter text, Boxes 3.1 and 3.2, the glossary; Fig 3.5 and Fig 3.8 viewed as images [img]. The references pages were skimmed.

**Claims**

*What counts as "algorithmic" and "AI".*
- p. 101 (glossary): algorithmic trading is "Trading in financial instruments whereby an algorithm independently executes trading decisions"; it can be execution, market-making or proprietary strategies; "in its simplest guise" it can be "basic trading rules or instruction to feed portions of an order into the market at preset intervals". HFT is a type of algorithmic trading, "not all forms of algorithmic trading can be described as high frequency" (p. 102).
- p. 78, fn 1: "AI/ML models" means well-established predictive analytics (shallow neural networks, clustering, decision trees); "sophisticated AI models" means deep networks, reinforcement learning and language models, including generative AI.

*Share of trading that is algorithmic or AI-driven.*
- p. 86: "In the United States, algorithmic trading now constitutes about 70 percent of equities trading and more than half of futures trading (Figure 3.8, panel 1)". Fig 3.8, read from the image [img] (approximate): US share of algorithmic trading activity by asset class in 2022-23: equities about 67%, futures about 52%, options about 44%, foreign exchange about 27%, fixed income about 8%. Equity algorithmic share by region, 2023: United States about 68%, Europe about 50%, Asia about 42%, Latin America about 30%. Euronext equity activity: the most active participant about 28%, the ten most active together about 89%.
- AI-specific adoption is "still nascent" (Fig 3.5, p. 83; Mercer Investments 2024 survey of investment managers). Read from the image [img]: "Executing investment decisions": 11% already integrated, 11% partly integrated, 59% do not plan to integrate. "Allocating assets": 10%, 9%, 59%. Dutch energy market algorithms using machine learning: about 88% of signal generators, about 33% of trading algorithms, about 11% of execution algorithms (approximate; Authority for Consumers and Markets 2024).
- p. 83: sophisticated AI is "more frequently used to generate a signal that is then used as an input in an existing analytical system where a human trader may ultimately make the trading decision". Dutch Authority for the Financial Markets: machine learning is used "implicitly or explicitly" in 80 to 100 percent of trading algorithms on Euronext, but "explicit" cases "may include applications that are not autonomous, such as signal generators" (fn 8, p. 82).
- Outlook (p. 83): participants expect "high-frequency, AI-driven trading" to account for "a more substantial share" in equities.

*Key findings.*
- Efficiency and liquidity (p. 87): algorithmic trading "enhances liquidity and informational efficiency, albeit at the cost of increased short-term volatility"; it can also raise volatility after macro news and discourage informed traders. In US Treasuries, liquidity improved on aggregate but "rare but extreme bouts of illiquidity under stress" may be the cost. Idiosyncratic price jumps in US stocks have become less frequent (Fig 3.10, 235 stocks, 2007-2024).
- Volatility under stress (p. 88): "Algorithmic trading strategies are often programmed to de-risk or even shut down during periods of high volatility", which "could contribute to market destabilization through a cascading and simultaneous triggering of limits, feedback loops, and the sudden evaporation of liquidity". The evidence is "some evidence": order cancellation rates fall and hidden-order rates rise as implied volatility rises ("flighty liquidity-under-stress"). AI-driven strategies are "also subject to the same measures" according to outreach feedback.
- Scenarios (Table 3.1, p. 89): negative (AI "magnifies existing risks", more leverage, more interconnectedness) and positive (AI "increases the stability of algorithmic trading under stressed conditions", "lower flash-crash risk"). "On balance, the impact of these changes from a financial stability perspective is highly uncertain." (p. 89)
- Speed (p. 89; Fig 3.11): after large language models, the first 45 seconds of the market reaction to FOMC minutes reflect the eventual impact "more accurately" (events with a move over 0.2% at 15 minutes: 15 before, 15 after). AI-driven ETFs have "significantly higher turnover"; three sample AI ETFs raised turnover in March 2020 ("some evidence for procyclicality").
- Concentration (pp. 86, 91, 93): "Increasing returns to scale seem to have resulted" in markets with high algorithmic shares also having activity concentrated among few players (Euronext). Participants in the outreach cited "herding and market concentration" as the key stability risk, "especially if trading and investment strategies were to become largely derived from open-source AI and trained on similar data sourced from the same set of vendors" (p. 91). Vendor concentration: failure of a few model or data providers "may lead to market stress akin to the failure of key financial market utilities such as clearing houses" (p. 93).
- Herding (p. 93): see quotes. In normal times models "may uncover new trading opportunities, leading to more diverse investment strategies"; in adverse shocks they "could simultaneously rebalance portfolios toward safe assets, creating a self-fulfilling spiral of fire sales".
- Collusion or manipulation (p. 89): "tacit algorithmic collusion could emerge" in some theory models; a "winner takes all" outcome in others (Fan, Pelger and Yu simulations, Fig 3.11 panel 4).
- Overall (p. 92): "currently the financial stability risks associated with its adoption appear contained". The chapter "finds indicative evidence" for four risk categories (p. 78): speed and volatility; opacity and monitoring (including migration to nonbanks); operational (third-party providers); cyber and manipulation.

*Humans in the loop.*
- p. 78: autonomous AI "generating and executing trades without human oversight" is "mostly speculative"; most participants "are quite uncomfortable with this idea" and see AI strategies "not understood by humans" as "a nonstarter".
- p. 83: "all participants" expected a "human in the loop" for three to five years, "especially for large capital allocation decisions"; "complete autonomy is not anticipated soon". "Some participants mentioned the potential for agent-to-agent trading and the development of complete AI-driven workflows in trading."
- p. 93: in novel events, "models may simply shutdown, requiring humans to make decisions on and process a voluminous number of trades". Models may also produce outcomes "difficult to comprehend".
- p. 93: "institutions are responsible for AI systems they deploy, whether internally developed or externally sourced"; existing capital-market frameworks "are largely technology-neutral".
- Fig 3.12 panel 2 (p. 91): participants expect regulators to ensure market integrity and "maintain human oversight of decision making".

*Policy recommendations (pp. 95-97).*
- Cross-sector: balanced approach; request "risk mapping" of interdependencies between data, models and technology infrastructure (p. 95-96).
- Speed and volatility (p. 96): determine whether to design or modify "volatility response mechanisms"; "Existing circuit breakers may need to be re-parameterized"; "poorly designed circuit breakers may exacerbate volatility"; test algorithms "in controlled environments"; review margining and buffers.
- Opacity (p. 96-97): ask institutions to map dependencies; models "may feed on shared or interdependent data sources; share a common architecture; and rely on a small number of providers"; monitor "large traders", each "uniquely identified"; strengthen oversight of nonbanks.
- Third parties (p. 97): coordinated approach to critical AI service providers; the definition should "capture the systemic use of common AI models".
- Over-the-counter markets (p. 97): more transaction data, incentives for market makers, central clearing, margin for uncleared derivatives; central bank liquidity as a backstop.
- Supervisors' own use of AI (pp. 83, 95): SupTech adoption in 2023: 79% of advanced economies and 54% of emerging markets (50% and 31% in 2022); supervisors should be able to detect models designed to "game the regulation" and "algorithmic coordination".
- Evidence base and hedges: Box 3.1 (p. 98): IMF staff held many meetings and "received detailed responses from 27 stakeholders"; regulatory outreach with 10 capital market supervisors. The risk list is "indicative".

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

**Numbers.** About 70% of US equities trading and over half of US futures trading are algorithmic (p. 86). Fig 3.8 and 3.5 values above (approximate). 27 detailed stakeholder responses; 10 supervisors; 26 authorities reviewed (p. 95). Near term = three to five years (p. 83). NBFIs hold "over half of all financial market assets globally" (p. 86).

**Instance.** The chapter's own instance is the "flighty" liquidity of algorithmic market makers under stress, and the possibility of simultaneous shutdown. It names no episode.

**Careful!**
- Traps 36, 37, 38 and 49.
- The IMF is balanced: "AI may actually reduce financial stability risks" (p. 77) and the positive column of Table 3.1 give a case for lower flash-crash risk. The card's "the cost is correlated failure" is one of two scenarios in the IMF text, not its finding.
- "Herd" is a hedged "may". The evidence for herding of AI models is the outreach (what participants fear) plus theory; the chapter reports no measured herding of AI models.
- The 70% says nothing about who decided what to trade; under the glossary definition it includes simple execution rules.

**Changes vs S2.** Replaces B7 (DROP). All three phrases B7 reported are now SEEN and correct: "AI models may herd..." (p. 93); "about 70 percent of equities trading" (p. 86); "human in the loop" for "three to five years" (p. 83). The "remain mostly speculative" line is on **p. 78** (B7 had it as p. 78 or 79).

**Toy idea.** The shut-down toy: N trading rules each with a pre-set loss limit; one shock trips them in the same minute; liquidity (the sum of what is left) falls by the count of tripped rules. Compare limits that are identical with limits that differ. Say "toy, ours". It goes with the six-bank cascade.

---

## V3. Gensler and Bailey (2020), "Deep Learning and Financial Stability" [SEEN, pp. 1-32]

**Source.** `gensler-bailey-2020-deeplearning.pdf`: SSRN 3766555, "Working Paper as of November 1, 2020", MIT AI Global Policy Forum. Offset 0. Read: abstract to the conclusion (pp. 1-32); references skipped. This is the paper itself, not the MIT Sloan article (S2 unit E3).

**Claims**

*Structure (pp. 2-5).* Three acts. Act 1: nine key characteristics of deep learning (hyper-dimensionality, non-linearity, non-determinism, dynamism, complexity; limited explainability, bias or fairness, lack of robustness; an "insatiable hunger" for data). Act 2: systemic risk through three channels. Act 3: five pathways. Coda: policy.

*The three channels (pp. 3, 17-18).*
- Uniformity and monocultures, including herding. "Herding is characterized by multiple individual actors making similar decisions, either rational or behavioral, resulting in a monoculture. Uniformity in finance can also arise when many actors in the financial sector rely on a centralized dataset or model." (p. 17)
- Network interconnectedness: "either the emergence of a dependency on some concentrated infrastructure, data, or operational service provider or an intricate web of firm-to-firm relationships" (p. 17). Cites Haldane (2009) on the financial system as a complex adaptive network "both fragile and robust at the same time".
- Regulatory gaps: the rules themselves fall short.

*The five pathways (pp. 20-27).*
- Data (pp. 20-22): concentrated data providers add herding and interconnectedness. "Models built on the same datasets are likely to generate highly correlated predictions that proceed in lockstep, causing crowding and herding." The risk rises as the provider moves up the value chain from raw data to "analytics and insights". Alternative data have "short sample sizes" that do not cover "even a single, complete financial cycle" (p. 21).
- Model design (pp. 22-24): possible convergence on a few model types ("mono-models"); human factor: few people are trained to build these models, with "fairly similar backgrounds" and an "apprentice effect"; AI-as-a-Service providers (named: BlackRock's Aladdin, Two Sigma's Venn, OpenAI) add interconnectedness. Models may have "fat tails" because of non-linearity and short data (p. 24). "Initially" different initialisations and hyperparameters "may lead to a greater diversity of outcomes", which later consensus erodes (p. 22).
- Regulatory (pp. 24-25): standards for explainability, fairness and robustness "may risk being uniformly internalized"; "Regulatory deep learning models may unknowingly promote uniformity in the agents they regulate"; a supervisory model that "is perturbed or fooled" could cause "outsize risk"; activity may migrate to less regulated actors.
- Algorithmic coordination (pp. 25-27): "by design one firm's models are going to be adapting to the signals from other firm's models"; "Models may add fragility through an invisible, machine-based, form of coordination and possible collusion." Collusion risk depends on number of firms, entry barriers, transparency and frequency of interaction (OECD); regulators "may not be able to discern deep learning coordination until after the fact".
- User interface (p. 27): standardised advice from virtual assistants may cause "herding of client decision making".

*Opacity and humans (pp. 9, 12, 13).*
- "Despite the highly automated nature of neural networks, there is still much human involvement in the modeling process" (p. 9: developers set hyperparameters, which create "inductive bias").
- Many models "automatically rebuild themselves" (continuous learning), adjusting "without any human oversight" (p. 12).
- "Human agency and traditional intervention approaches may be lost as a consequence of lack of model explainability and transparency" (p. 13). Their argument: "if deep learning predictions were explainable, they wouldn’t be used in the first place".

*Flash crashes (p. 22).* "It is hypothesized that herding and crowding in high frequency algorithmic trading is partially responsible for causing flash crashes" (citing Lo and Kirilenko and Lo). See trap 40.

*Policy (pp. 28-32).* Micro-prudential: internal mapping of dependencies; updated model-risk guidance (SR 11-7 of 2011, TRIM 2017, E-23 2017); firm buffers, including back-up non-deep-learning models run in parallel; regulatory diversity (more than one way to comply). Macro-prudential: external mapping of data and AI-as-a-Service dependencies; coordinated stress tests and "war games"; bringing material third-party providers inside the regulatory perimeter; horizontal reviews; network buffers. Ex post: circuit breakers, "kill switches", central bank last-resort roles, recovery and resolution plans for providers (p. 32). Their summary: current tools will "not be sufficient"; "Adequately mitigating such risks will require additional research and discussion" (p. 32).

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

**Instance.** Quant crisis of August 2007 (Khandani and Lo): "highly similar optimization functions" and crowding (p. 22). Credit-rating agencies used "models with similar methodologies" for CDOs (p. 22).

**Careful!**
- Traps 39 and 40. The wording on correlated predictions is "likely to generate", conditional on shared data.
- The paper is a hypothesis about a *future mature stage*, not a finding about 2020.
- It says early-stage technology "often" shows diversity, then "often recedes to more technological uniformity" (p. 4). Do not cite it for present uniformity.
- It names the *checking* job as exposed: a supervisor's own model "may unknowingly promote uniformity" (p. 25). That is a quotable bridge to "who checks the checker".

**Changes vs S2.** E3 (secondary, via MIT Sloan) can be dropped as a source for the paper's content; keep it only for the MIT Sloan article's own gloss. Trap 15 is resolved: the paper is SEEN.

**Toy idea.** The effective-number-of-opinions toy (E8): ten models trained on one dataset; show N_eff near 1 when correlation is high. Say "toy, ours".

---

## V4. Arora, Barak, Brunnermeier and Ge: ICS 2010 extended abstract (the file labelled "cacm") [SEEN, pp. 49-65; the CACM text is UNSEEN]

**Source.** `arora-2011-cacm.pdf` = `arora-ics2010.pdf` (same md5): "Computational Complexity and Information Asymmetry in Financial Products (Extended Abstract)", Innovations in Computer Science 2010, printed pp. 49-65 (offset +48). It says it is "geared to a CS audience" and proves simple cases "for binary CDOs only"; a "companion paper" (economists' version, with tranching) is the 2009 working paper behind S2 units C3 and C4. The 2011 CACM article (54(5): 101-107) is UNSEEN: the one attempt to fetch the Princeton copy returned an HTML error page. Read pp. 49-65; pp. 59 and 63 also viewed as images [img].

**Claims**

- Abstract, p. 49: "Assuming reasonable complexity-theoretic conjectures, we show that derivatives can actually amplify the costs of asymmetric information instead of reducing them." The results are proved "both in the worst-case setting, as well as the more realistic average case setting", with "computational indistinguishability" used to argue the constructions "look like" real derivatives.
- Lemon cost (p. 51): Akerlof's car example ($1000 working car, 20% lemons worth $0, expected $800; the seller's value must be $200 below the buyer's, so "the ‘lemon cost’ of this market is $200"). Defined for derivatives on p. 52: Δ(n) = E[F(X)] minus the minimum over n-subsets S of E[F(X) | X_i = 0 for all i in S]. The seller "positions" the junk assets to his advantage.
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

(The sentence quoted second to last is the conclusion's "faulty models" sentence, which reads in full: "Most analysis of the current financial crisis blames the use of ‘faulty models’ in pricing derivatives rather than computational complexity and we do not dispute that effect." It is 27 words, so it is given as paraphrase plus the 6-word turn.)

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

## V5. Haldane and May (2011), "Systemic risk in banking ecosystems", Nature 469 [SEEN, pp. 351-355]

**Source.** `haldane-may-2011-nature.pdf`: Nature 469, 351-355 (20 January 2011), a Perspective; doi:10.1038/nature09659. Offset +350. Read in full; p. 351 viewed as an image [img]. Authors: Haldane (Bank of England), May (Oxford Zoology). Policy is stated as "explicit aim of minimizing systemic risk".

**Claims**

*May's criterion (p. 351).*
- Background: Hutchinson (1959) thought more links meant more stability, "based on a misunderstanding of MacArthur's paper". "To the direct contrary", model ecosystems showed that "a random assembly of N species, each of which had feedback mechanisms that would ensure the population’s stability were it alone, showed a sharp transition from overall stability to instability as the number and strength of interactions among species increased."
- Exact statement [img]: "for N ≫ 1 this transition occurs once mα² > 1, where m is the average number of links per species, and (±) α their average strength" (ref. 4: May 1972, *Nature* 238, 413-414; UNSEEN).
- Conditions: random assembly; N much greater than 1; each species self-stable when alone; links of random sign (the ± before α). It is an ecology result; Haldane and May do not apply it to banks. In ecology it prompted a search for special structures (modularity, nested hierarchies) that reconcile complexity with persistence; "tentative evidence" is given (p. 351).
- Differences between ecosystems and finance are acknowledged: "There are, of course, major differences between ecosystems and financial systems." (p. 351)

*Derivatives and complexity (pp. 351-352).* About two-thirds of the growth in banks' balance sheets reflected claims within the financial system ("perhaps as much as"). Derivatives outgrew world GDP "by a factor of three" (Fig. 1). Caccioli, Marsili and Vivo (2009): arbitrage pricing theory assumes "perfect competition, market liquidity, no-arbitrage and market completeness", i.e. that trading has no feedback on prices; when feedback is included, "the road to efficient, arbitrage-free, complete markets can be plagued by singularities which arise upon increasing financial complexity". In their model, once n passes a threshold (n* = 4.14), a sharp singularity appears and, once the market is "essentially complete", extra instruments are "essentially redundant" and cost stability "with no welfare gain" (p. 352; Haldane and May's own gloss, "grossly simplified").

*The banking-network model (p. 352-353).*
- A bank has assets (interbank loans l_i, external assets e_i) and liabilities (interbank borrowing b_i, deposits d_i); solvency requires net worth c_i = (e_i + l_i) - (d_i + b_i) ≥ 0. Banks are linked at random (Erdős-Rényi), each pair with probability p; the average number of links is z = p(N - 1).
- Mean-field simplification: all banks the same size (1), each linked to exactly z others, loans of equal size, equal capital c, loans-to-assets ratio h (the text layer shows h and c; the figures show θ and γ). A shock wipes out a fraction f of one bank's external assets; the bank fails if f(1 - h) > c.
- Loan-driven shocks are attenuated, by about the factor z, because a failing bank's losses are split among z creditors. Fragility is greatest for intermediate h. "An increase in the system’s connectivity, z, causes the coloured region of instability to shrink; high connectivity distributes, and thereby attenuates risk. On the other hand, when later-phase failures do occur, they will then involve more banks." (p. 353)
- Liquidity shocks are different: "in sharp contrast to the attenuation in interbank loan shocks, liquidity shocks amplify as more banks fail"; funding-liquidity hoarding "is not subject to the attenuation" (p. 353).
- Real networks are "far from random", with long-tailed degrees; "disassociative" wiring (big banks tied to small) maximises the number infected by a contagion but "can make the network more robust to random losses" (p. 353).

*Homogeneity and diversity (p. 353; policy p. 355).*
- Claim: "excessive homogeneity within a financial system—all the banks doing the same thing—can minimize risk for each individual bank, but maximize the probability of the entire system collapsing". Source cited: earlier work and N. Beale and colleagues, "manuscript in preparation" (UNSEEN).
- Toy: N banks and N distinct, uncorrelated asset classes, each with a very small probability ε of a loss big enough to fail a bank holding only that asset. Inhomogeneous extreme: each bank holds one whole asset; a given bank fails with probability ε and the system with ε^N. Homogeneous extreme: each bank holds 1/N of every asset; one bank fails (and so all N do) with probability N^N ε^N / N!. "This homogeneous, ‘herding behaviour’ limit clearly makes each individual bank safer, but the systemic risk is much larger." "More realistic versions of this scenario consistently show the same unhappy conclusion." (pp. 353-354)
- Evidence: "Tentative evidence" is that the five largest banks became more concentrated while the five largest hedge funds are "less concentrated" (p. 354). Policy: "this systemic diversity objective should probably be given much greater prominence by the regulatory community" (p. 355); "Homogeneity bred fragility" (p. 355, citing Beale et al.).

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

**Numbers.** n* = 4.14 (Caccioli et al.); z = p(N - 1); fail if f(1 - h) > c; loan shocks attenuate by about z. Homogeneity toy (ours, computed): with ε = 0.01 and N = 10, the heterogeneous system fails with probability ε^N = 1e-20 and the homogeneous system with N^N ε^N / N! = 2.76e-17, about 2,756 times larger, while one diversified bank's chance of failing falls from 0.01 to 2.76e-17. For N = 6 the ratio is 64.8; for N = 20, about 4.3e7. The ratio N^N / N! is about e^N / √(2πN).

**Instance.** The 2007-8 crisis as a banking ecosystem; Lehman as a super-spreader (p. 354).

**Careful!**
- Traps 42 and 43.
- The card's lens 2 says "complexity and homogeneity versus stability, by analogy with ecology". Complexity is the ecological and Caccioli et al. result; homogeneity is the banking toy; the paper does NOT show that connectivity always lowers stability (loan shocks attenuate with z, liquidity shocks amplify).
- The homogeneity toy's "each bank is safer" depends on the N asset classes being independent and each bank holding all of them. It is an extreme-case toy with "oversimplified" built in.
- Two of the main supports for homogeneity are manuscripts in preparation in 2011.

**Toy idea.** A new lab widget with two sliders (m and α) showing mα² against 1 for a random web (ecology, labelled as such) and, separately, the N-bank homogeneity toy with the two probabilities above. Say "toy, ours" and keep the ecology widget out of the banking claims.

---

## V6. Harari, *Nexus* (2024) [SEEN: chapters 2, 6, 8, 9 passages, cited by PDF page of the ebook file]

**Source.** `harari-2024-nexus.pdf` (592 PDF pages; text in the scratch dump). Edition from the copyright page (PDF 5): "First edition. | New York: Random House, [2024]"; also Fern Press (UK); "ebook ISBN 9780593734247"; "adapted for ebook". **No printed page numbers.** Cite as chapter, subheading, "PDF n" (this file only). The file carries "OceanofPDF.com" marks (trap 44). Chapter titles (PDF 6): ch. 2 "Stories: Unlimited Connections"; ch. 6 "The New Members: How Computers Are Different from Printing Presses"; ch. 7 "Relentless: The Network Is Always On"; ch. 8 "Fallible: The Network Is Often Wrong"; ch. 9 "Democracies: Can We Still Hold a Conversation?". Read: the passages below in context (a page or more each), plus the Prologue and note 43.

### V6a. Ch. 2, INTERSUBJECTIVE ENTITIES (PDF 50-53): money as story [SEEN]
- Asserts (PDF 50): "stories can even create an entirely new level of reality"; before stories "the universe contained just two levels" (hedged: "As far as we know"). Intersubjective things "like laws, gods, nations, corporations, and currencies exist in the nexus between large numbers of minds". "Intersubjective things exist in the exchange of information." "If people stop talking about them, they disappear."
- Money (PDF 51): "the financial value of money—and pizzas—depends entirely on our beliefs". Bitcoin: 10,000 bitcoins for two pizzas in 2010; a single bitcoin above $69,000 by November 2021; "the financial value of bitcoin is an intersubjective reality that changed dramatically".
- States (PDF 51-52): existence of states is intersubjective: "If enough people agree that a particular state exists, then it does."
- Limit (PDF 53): intersubjective things are "utterly meaningless outside" the network: the billionaire on the island, "his banknotes and bonds immediately become worthless".
- **Quotes.** PDF 50: “stories can even create an entirely new level of reality” | PDF 51: “the financial value of money—and pizzas—depends entirely on our beliefs” | PDF 52: “If enough people agree that a particular state exists, then it does.” | PDF 53: “Intersubjective things like laws, gods, and currencies are extremely powerful within a particular information network and utterly meaningless outside it.”
- **Careful.** Harari's mechanism is "stories people tell one another" and "exchange of information". Searle's is collective acceptance of a status with a function and a constitutive rule (V7). Both say the fact vanishes when the people stop. Harari does not mention deontic powers or "counts as"; the comparison is ours (trap 47).

### V6b. Ch. 6, LINKS IN THE CHAIN (PDF 216-219), WHAT ARE THE IMPLICATIONS? (PDF 226-227): new members and computer-to-computer chains [SEEN]
Sorted by firmness.
- *Asserts.* "computer-to-computer chains can now function without humans in the loop" (PDF 217). Computers "are fully fledged members of the information network, whereas clay tablets, printing presses, and radio sets are merely connections between members" (PDF 217-218). "Humans are excluded from these loops and have difficulty even understanding what’s happening inside them" (PDF 226; the Google Brain Alice, Bob and Eve experiment). "No wonder that computers make a larger and larger percentage of the financial decisions in the world" (PDF 219). "More than 90 percent of this trading is already done by computers talking directly with other computers" (forex, PDF 227; endnote 43: see trap 49). The book's own takeaway is "the emergence of computers capable of pursuing goals and making decisions by themselves changes the fundamental structure of our information network" (PDF 216).
- *Predicts (conditional or hedged).* a conditional: if power depends on how many members cooperate with you, how well you understand law and finance and how capable you are of inventing new laws and financial devices, "then computers are poised to amass far more power than humans" (PDF 219). "For the foreseeable future, the new computer-based network will still include billions of humans, but we might become a minority" (PDF 227).
- *Imagines.* The chain: one computer posts a fake story, a second flags it, a third "might deduce" a political crisis and sell risky stocks, others sell more, "triggering a financial downturn"; "All this could happen within seconds, before any human can notice and decipher what all these computers are doing" (PDF 217; endnote 29 cites the 2016 pound flash crash and a fake Eli Lilly account, not 2010). "We may reach a point when computers dominate the financial markets, and invent completely new financial tools beyond our understanding" (PDF 219).
- *Concedes.* "using this language does not imply that computers have any kind of consciousness" (PDF 216: he uses "goals" and "decisions" for computers without claiming experience). "For at least some time, most of the old information chains will remain" (PDF 226).
- **Quotes (at most 25 words).** PDF 217: “computer-to-computer chains can now function without humans in the loop” | PDF 217: “All this could happen within seconds, before any human can notice and decipher what all these computers are doing.” | PDF 219: “We may reach a point when computers dominate the financial markets, and invent completely new financial tools beyond our understanding.” | PDF 219: “No wonder that computers make a larger and larger percentage of the financial decisions in the world.” | PDF 226: “Humans are excluded from these loops and have difficulty even understanding what’s happening inside them.” | PDF 227: “More than 90 percent of this trading is already done by computers talking directly with other computers.” | PDF 227: “For the foreseeable future, the new computer-based network will still include billions of humans, but we might become a minority.”
- **Careful.** The "chain" is an example Harari constructs ("might", "could"); he gives no case where a chain ran without any human in the 2010 sense. The forex number is his, unverified (trap 49).

### V6c. Ch. 8, COMPUTER MYTHOLOGY (PDF 291-295): inter-computer realities [SEEN]
- *Asserts.* "when a lot of computers communicate with one another, they can create inter-computer realities, analogous to the intersubjective realities produced by networks of humans" (PDF 292). Pokémon: "The Pokémon were inter-computer entities" (PDF 293). Google rank: "The rank itself is an inter-computer reality, existing in a network connecting billions of computers—the internet" (PDF 293), and it "spills over into the physical world". "Cryptocurrencies like bitcoin are midway between intersubjective and inter-computer" (PDF 294).
- *Predicts (hedged).* These realities "may eventually become as powerful—and as dangerous—as human-made intersubjective myths" (PDF 292). "As computers become more intelligent and more creative, they are likely to create new inter-computer financial devices" (PDF 294). "In the twenty-first century, we might see wars fought over inter-computer entities" (PDF 294). "Now computers may acquire comparable abilities" (PDF 295: to create and sustain corporations, currencies, gods and nations).
- *Imagines.* He asks "What if in ten or fifty years computers create a new kind of cryptocurrency" that becomes a vital tool and a source of crises (PDF 295). "Computers may well create financial devices that will be orders of magnitude more complex than CDOs and that will be intelligible only to other computers. The result could be a financial and political crisis even worse than that of 2007–8" (PDF 295). Legal personhood is a question: "What would stop AIs from being incorporated and recognized as legal persons with freedom of speech" (PDF 295), with the Citizens United example.
- *Concedes.* "Of course, they cannot ‘believe’ in any mythology, because they are nonconscious entities that don’t believe in anything" (PDF 292). "This isn’t necessarily bad news" (PDF 295). His CDO lesson is stated as fact: CDOs "were almost unintelligible for most humans, including regulators" (PDF 295).
- **Quotes (at most 25 words).** PDF 292: “when a lot of computers communicate with one another, they can create inter-computer realities, analogous to the intersubjective realities produced by networks of humans” | PDF 292: “Of course, they cannot ‘believe’ in any mythology, because they are nonconscious entities that don’t believe in anything.” | PDF 293: “The rank itself is an inter-computer reality, existing in a network connecting billions of computers—the internet.” | PDF 294: “Cryptocurrencies like bitcoin are midway between intersubjective and inter-computer.” | PDF 295: “Computers may well create financial devices that will be orders of magnitude more complex than CDOs and that will be intelligible only to other computers.” | PDF 295: “The result could be a financial and political crisis even worse than that of 2007–8.”
- **Careful.** Every inter-computer reality Harari gives (Pokémon, Google rank, bitcoin) has its effect through *people* who play, search or trade; none is a status function held by machines for machines. That is our reading (trap 47), and it bears on the card's "machines that treat each other as persons": Harari asks it as a question and says nothing that machines would accept each other as persons. His financial-device claim is "may well ... could": an imagined scenario with no instance (S2 trap 2 and the "ten years" traps 4 and 30 apply).

### V6d. Ch. 9, UNFATHOMABLE, THE RIGHT TO AN EXPLANATION (PDF 329-336): democracy and algorithms [SEEN]
- *Asserts.* "For a democracy, being unfathomable is deadly" (PDF 329): if "citizens, lawmakers, journalists, and judges cannot understand how the state’s bureaucratic system works, they can no longer supervise it". Before computers bureaucrats "always remained human", so there was "at least the hope of identifying and correcting its mistakes" (PDF 329). "The rise of unfathomable alien intelligence undermines democracy" (PDF 335). AlphaGo's move 37: "Even after AlphaGo played it to achieve victory, Suleyman and his team couldn’t explain how AlphaGo decided to play it" (PDF 335). "Even today, only a small fraction of humanity truly understands the financial system" (PDF 335); a 2014 survey found "only 12 percent" of British MPs understood that banks create money when they lend (PDF 336).
- *Reports a demand and a law.* "There is, consequently, a growing demand to enshrine a new human right: the right to an explanation" (PDF 333). The EU's GDPR (2018): the person "is entitled to obtain an explanation of the decision and to challenge that decision in front of some human authority" (PDF 333).
- *Predicts or imagines.* "If more and more decisions about people’s lives are made in a black box, so voters cannot understand and challenge them, democracy ceases to function" (PDF 335; a conditional). The Federal Reserve's rate set by "unfathomable algorithms": "Human voters may keep choosing a human president, but wouldn’t this be just an empty ceremony?" (PDF 335). He asks what happens to democracy when AIs create more complex financial devices and "the number of humans who understand the financial system drops to zero" (PDF 335-336).
- *Concedes (on explanation).* Can the right be met in practice? "when it comes to providing explanations, this creates a potentially insurmountable obstacle" (PDF 338: too many data points and learned patterns). But: "we can use one algorithm to vet another" and a team of experts with "AI sidekicks" can "potentially assess the fairness of algorithmic decisions even more reliably than anyone can assess the fairness of human decisions" (PDF 339).
- **Quotes (at most 25 words).** PDF 329: “For a democracy, being unfathomable is deadly.” | PDF 333: “There is, consequently, a growing demand to enshrine a new human right: the right to an explanation.” | PDF 333: “that human is entitled to obtain an explanation of the decision and to challenge that decision in front of some human authority” | PDF 335: “Even after AlphaGo played it to achieve victory, Suleyman and his team couldn’t explain how AlphaGo decided to play it.” | PDF 335: “Even today, only a small fraction of humanity truly understands the financial system.” | PDF 335: “If more and more decisions about people’s lives are made in a black box, so voters cannot understand and challenge them, democracy ceases to function.”
- **Careful.** The GDPR statement is Harari's description of the law, not his own view. The "empty ceremony" and "drops to zero" lines are rhetorical questions.

### V6e. Harari's remedies (ch. 9, PDF 339-346) [SEEN]
- *Asserts.* "Ultimately, there is no purely technological solution to this recursive problem." The vetting algorithm needs vetting: "we will have to maintain bureaucratic institutions that will audit algorithms and give or refuse them the seal of approval" (PDF 339). Without such institutions, even a right to an explanation has no enforcer (PDF 340). Regulators must "translate their discoveries into stories that humans can understand" (PDF 340).
- *Recommends.* "democracies are not helpless" (PDF 345). Following Dennett, outlaw counterfeit humans as money is protected from counterfeiting: "any attempt by a nonhuman agent to pass itself off as a human" (PDF 345); "banning bots is a simple issue: it doesn’t violate anyone’s rights, because bots don’t have rights" (PDF 345). Bots are welcome "provided they don’t pretend to be humans" (PDF 346). "ban unsupervised algorithms from curating key public debates"; the curation principles "must be vetted by a human institution" (PDF 346).
- *Concedes.* "Naturally, each has its advantages and drawbacks, and none would be easy to implement." "since the technology is developing so rapidly, regulations are likely to become outdated quickly" (PDF 346).
- **Quotes (at most 25 words).** PDF 339: “Ultimately, there is no purely technological solution to this recursive problem.” | PDF 339: “we will have to maintain bureaucratic institutions that will audit algorithms and give or refuse them the seal of approval” | PDF 345: “banning bots is a simple issue: it doesn’t violate anyone’s rights, because bots don’t have rights” | PDF 346: “Digital agents are welcome to join many conversations, provided they don’t pretend to be humans.” | PDF 346: “Naturally, each has its advantages and drawbacks, and none would be easy to implement.”
- **Careful.** The "check" job: Harari concedes algorithms can check algorithms (PDF 339) and then says the regress ends only in human institutions. That is a text-backed statement of the card's "who checks the checker". The "answer" job: his remedies all keep a human authority (a court, a vetting institution, a person with a right to challenge).

**Changes vs S2.** Adds the full Nexus text to A4 (which used the Prologue and the Guardian extract). The Nexus page numbers p. xxii and p. xxxii of trap 7 refer to the paperback sample; do not mix them with the PDF pages here.

---

## V7. Searle (1995), *The Construction of Social Reality* [SEEN, printed pp. 14-58, 68-85, 88-89, 93, 95-97, 99-100, 104, 106-111, 114, 117-124, 140-141; the rest UNSEEN]

**Source.** `searle-1995-construction.pdf` (scan) with OCR in `ocr-searle/p-NNN.txt`; the combined `.txt` is now complete. Offset: see the table above (-9 to printed p. 57, then -8). **Every quote below was checked against the rendered page image [img].** UNSEEN printed pages (not read): 1-13, 59-67 (the opening of ch. 3), 86-87, 90-92, 94, 98, 101-103, 105, 112-113, 115-116, 125-139, 142 onward. A full-text search of the OCR for robot, artificial intelligence, Turing, Chinese room and strong AI finds nothing (trap 48).

### V7a. Collective intentionality and what can have it
- *Asserts.* "Many species of animals, our own especially, have a capacity for collective intentionality" (p. 23): not only cooperation but "that they share intentional states such as beliefs, desires, and intentions". It is "a biologically primitive phenomenon that cannot be reduced to or eliminated in favor of something else" (p. 24). "No set of ‘I Consciousnesses,’ even supplemented with beliefs, adds up to a ‘We Consciousness’" (p. 24); "the individual intentionality that each person has is derived from the collective intentionality that they share" (p. 25). The "we" lives in individual heads: "all my mental life is inside my brain" yet its form is "we intend" (pp. 25-26). A "social fact" is "any fact involving collective intentionality"; institutional facts are a subclass (p. 26).
- *What can have it.* Hyenas hunting a lion are a social fact but not an institutional one (p. 38). For institutions, "only beings that have a language or some more or less language-like system of representation can create most, perhaps all, institutional facts" (p. 37; stated as an "apparent feature", hedged "perhaps all"; defended in ch. 3, p. 69). Ant colonies "have slaves" or hives "have queens" are "harmless metaphors" (p. 37). Animals can "cooperate in the hunt, share their food, and even have pair bonding. But they cannot have marriages, property, or money" (p. 70), because they cannot represent the deontic phenomena: "He still is not buying the food and the bills are not money to him" (p. 70, the dog trained to fetch dollar bills).
- *Hedge.* Searle is "not certain that the ethologists are justified in attributing so much collective intentionality to the animals" (footnote, p. 40).
- *Machines.* Not discussed (trap 48). The nearest passage is pp. 140-141 (V7g).
- **Quotes.** p. 24: “Collective intentionality is a biologically primitive phenomenon that cannot be reduced to or eliminated in favor of something else.” | p. 24: “No set of ‘I Consciousnesses,’ even supplemented with beliefs, adds up to a ‘We Consciousness.’” | p. 25: “the individual intentionality that each person has is derived from the collective intentionality that they share” | p. 37: “only beings that have a language or some more or less language-like system of representation can create most, perhaps all, institutional facts” | p. 70: “He still is not buying the food and the bills are not money to him.”

### V7b. Assignment of function
- *Asserts.* "functions are never intrinsic to the physics of any phenomenon but are assigned from outside by conscious observers and users" (p. 14); "Functions, in short, are never intrinsic but are always observer relative." Examples include "Chairs, bathtubs, and computers" as artefacts built to serve a function (p. 14). Three kinds: nonagentive (the heart pumps blood), agentive (a screwdriver), and a special subclass of agentive functions whose function is to represent or mean something (pp. 20-23).
- *Condition on agentive functions.* "for all cases of agentive function, someone must be capable of understanding what the thing is for, or the function could never be assigned" (p. 22). Money may have "simply evolved without anyone ever thinking, ‘We are now imposing a new function on these objects’" (p. 22).
- *Hedges.* The nonagentive/agentive line has "no sharp dividing line" (p. 20).
- **Quotes.** p. 14: “functions are never intrinsic to the physics of any phenomenon but are assigned from outside by conscious observers and users” | p. 22: “someone must be capable of understanding what the thing is for, or the function could never be assigned” | p. 41: “the collective intentional imposition of function on entities that cannot perform those functions without that imposition”

### V7c. Status functions and "X counts as Y in C"
- *Asserts.* Constitutive rules "create the very possibility of playing chess", and "characteristically have the form ‘X counts as Y’ or ‘X counts as Y in context C.’" (p. 28). "institutional facts exist only within systems of constitutive rules" (p. 28). Rules versus conventions: "constitutive rules in general are not in that sense arbitrary" (p. 28).
- *The step.* The key element in the move from imposed function to institutional facts is "the imposition of a collectively recognized status to which a function is attached" (p. 41), labelled "status functions". The Y term "has to assign a new status that the object does not already have", and "there has to be collective agreement, or at least acceptance" (p. 44). "Collective agreement about the possession of the status is constitutive of having the status" (p. 51), and the status is essential to performing the function.
- *Iteration.* The formula iterates: the X term at a higher level can be the Y term of a lower level (citizen, then President) (p. 80); promise, then contract, then marriage (pp. 82-83).
- *The basic structure.* "We collectively accept, acknowledge, recognize, go along with, etc., that (S has power (S does A))" (p. 111). **Hedge on this very claim:** "There is exactly one primitive logical operation by which institutional reality is created and constituted" is introduced as "the following hypothesis. I do not know if it is true and I certainly have not demonstrated it, but it is worth further exploration" (pp. 110-111).
- *Deontic powers.* Status functions confer "conventional power": "all deontic status-functions are matters of conventional power" (p. 100); "everything turns out to be deontic" (p. 109). Searle also calls the limit on what can be created "perhaps, the most mysterious feature of institutional facts" (p. 47).
- **Quotes.** p. 28: “‘X counts as Y’ or ‘X counts as Y in context C.’” | p. 28: “institutional facts exist only within systems of constitutive rules” | p. 41: “the imposition of a collectively recognized status to which a function is attached” | p. 51: “Collective agreement about the possession of the status is constitutive of having the status” | p. 111: “We collectively accept, acknowledge, recognize, go along with, etc., that (S has power (S does A)).” | p. 100: “let us say that all deontic status-functions are matters of conventional power”

### V7d. Institutional facts: brute and institutional; language
- *Asserts.* "Brute facts exist independently of any human institutions; institutional facts can exist only within human institutions." (p. 27). Institutional facts "exist, so to speak, on top of brute physical facts" (p. 35). "Thus there are no institutional facts without brute facts" (p. 56): the substrate can be "a bit of paper or a blip on a computer disk" (p. 56); "Most money is now in the form of magnetic traces on computer disks" (p. 34).
- *Self-reference.* "for social facts, the attitude that we take toward the phenomenon is partly constitutive of the phenomenon" (p. 33). "Part of being a cocktail party is being thought to be a cocktail party" (p. 34).
- *Language.* The status "exists only if people believe it exists, and the reasons function only if people accept them as reasons" (p. 69); it needs a symbolic vehicle because "empirically speaking, there isn’t anything else there" (p. 69).
- *Declarations.* Many institutional facts are created by performative utterances (p. 34); when the Treasury says a note is legal tender, "they are declaring it to be legal tender, not announcing an empirical fact that it already is legal tender" (p. 55); "You cannot, for example, make a touchdown just by saying you are making it" (p. 55): not all can be declared.
- **Quotes.** p. 27: “Brute facts exist independently of any human institutions; institutional facts can exist only within human institutions.” | p. 33: “the attitude that we take toward the phenomenon is partly constitutive of the phenomenon” | p. 56: “Thus there are no institutional facts without brute facts.” | p. 34: “Most money is now in the form of magnetic traces on computer disks.” | p. 69: “The status exists only if people believe it exists, and the reasons function only if people accept them as reasons.” | p. 55: “they are declaring it to be legal tender, not announcing an empirical fact that it already is legal tender”

### V7e. Money as the central example
- The three kinds (p. 41-42): commodity money, contract money, fiat money; "in the case of fiat money the stuff is valuable because it is a medium of exchange" (p. 42; the first half of the sentence says commodity money is a medium of exchange because it is valuable).
- The medieval story (p. 43), which Searle says he is "using ... only to illustrate certain logical relations": certificates as good as gold; "we can forget about the gold and just have the certificates" (p. 43). A Federal Reserve note redeemed for "another twenty dollar Federal Reserve note" (p. 43).
- The bill: the X term (right material, pattern, issued by the Bureau of Engraving and Printing) counts as Y (legal tender) (pp. 45-46); the label on the bill is a declaration (p. 55).
- Tokens and types (pp. 32-33, 53): a bill that fell into the cracks of the floor and was never used or thought of "would still be money"; a counterfeit that no one knows is counterfeit is not money though all think it is; "where the type of thing is concerned, the belief that the type is a type of money is constitutive of its being money" (p. 33). The reason, by p. 53, is codification: an official, codified institution makes self-reference "a feature of the type".
- Abuses the rule makes possible: "the general rule creates the possibility of abuses that could not exist without the rule, such as counterfeit money" and hyperinflation (p. 48).
- Evolution without awareness: participants "need not think, ‘We are collectively imposing a value’" (p. 47) and "do not in addition have to recognize that they are so recognizing" (p. 47).
- **Quotes.** p. 42: “in the case of fiat money the stuff is valuable because it is a medium of exchange” | p. 43: “we can forget about the gold and just have the certificates” | p. 48: “the general rule creates the possibility of abuses that could not exist without the rule, such as counterfeit money” | p. 47: “They do not in addition have to recognize that they are so recognizing”

### V7f. Continued acceptance, and whether rules can work without it
- *Asserts.* "there must be continued collective acceptance or recognition of the validity of the assigned function; otherwise the function cannot be successfully performed" (p. 45, "continued" in italics). Agreeing with the original assignment is not enough: "we must continue to accept it as money or it will become worthless" (p. 45). "the individuals directly involved and a sufficient number of members of the relevant community must continue to recognize and accept the existence of such facts" (p. 117). "Because institutions survive on acceptance, in many cases an elaborate apparatus of prestige and honor is invoked to secure recognition and maintain acceptance" (p. 118). Property rights "cease to exist" if most members refuse to acknowledge them (p. 117).
- *What acceptance needs.* It need not be aware: "as long as they continue to recognize his authority, he has the status-function of king, regardless of whatever false beliefs they may hold" (p. 96). "Sheer physical power is unaffected by collective agreement" (p. 96).
- *Can force replace it?* No, for the institutional fact: "In fact power grows out of organizations, i.e., systematic arrangements of status-functions" (p. 117), and guns are ineffectual except to those who use them "in cooperation with others and in structures" with recognized lines of authority (p. 117, paraphrase with a short quote). But he concedes that where "consent" is not essential, force can do the work: "Jails find these devices less necessary because they have brute force" (p. 118).
- *Can a rule work without acceptance?* Regulative rules can bind by sanction, but sanction itself needs a status: the criminal law is "regulative, not constitutive", yet to make it work "there must be sanctions, and that requires the imposition of a new status" (p. 50). Constitutive rules cannot: "If you don't follow at least a large subset of the rules, you are not playing chess" (p. 28). An institution can be started by acting "as if it did exist" (the Declaration of Independence), but it succeeded because the founders "created and sustained acceptance" with community support and force (pp. 118-119).
- **Quotes.** p. 45: “there must be continued collective acceptance or recognition of the validity of the assigned function; otherwise the function cannot be successfully performed” | p. 45: “we must continue to accept it as money or it will become worthless” | p. 117: “the individuals directly involved and a sufficient number of members of the relevant community must continue to recognize and accept the existence of such facts” | p. 117: “In fact power grows out of organizations, i.e., systematic arrangements of status-functions.” | p. 118: “Because institutions survive on acceptance, in many cases an elaborate apparatus of prestige and honor is invoked to secure recognition and maintain acceptance.” | p. 118: “One way to create institutional facts in situations where the institution does not exist is simply to act as if it did exist.” | p. 96: “as long as they continue to recognize his authority, he has the status-function of king, regardless of whatever false beliefs they may hold”

### V7g. The nearest Searle comes to machines (printed pp. 140-141, the Background)
- *Asserts.* The Background "can be causally sensitive to the specific forms of the constitutive rules of the institutions" without "actually containing any beliefs or desires or representations of those rules" (p. 141; one 29-word sentence, quoted in two parts). He says the Background is "more in tune with ... the connectionist model of cognition" than with a serial program, and "I think that’s right", **but** he adds that this "still leaves us with the challenge posed by those who oppose connectionism", namely what internal structure gives structured output (p. 141).
- *Hedge.* He says he is "not satisfied" with either way of thinking of the Background (p. 140).
- **Careful.** This is about how humans follow institutional rules without representing them. It does not say a machine can accept a status. Whether a system without consciousness can be part of the "we" is ours.
- **Quotes.** p. 141: “the Background can be causally sensitive to the specific forms of the constitutive rules of the institutions” | p. 141: “without actually containing any beliefs or desires or representations of those rules”

**Numbers.** None. Classifications: Searle's fiat/contract/commodity money; his count "exactly one primitive logical operation" (hypothesis).

**Instance.** Money (the dollar bill, fiat money), the Declaration of Independence, the Korean "police action" versus "war" (pp. 88-89).

**Careful! (Searle overall)**
- Traps 47, 48 and 50.
- Searle's claim that institutional reality needs the "we" is about *human and animal* minds. That a machine cannot be in the "we" is an inference that Searle does not draw.
- Acceptance can be implicit ("go along with", p. 111) and unaware (p. 96); the bar is lower than "belief". That cuts against the card's "no: people's collective acceptance (Searle 1995)" as a flat statement.
- The card's line "Can a token become money with no human accepting it?" has Searle's answer: a *token* yes if the *type* is accepted (and codified); the type, no (trap 50).
- "X counts as Y" on the bill is a declaration by an authority; Searle does not say who or what may declare (a person, an office, a machine) beyond "appropriate circumstances" and "wrong person" (p. 54, not quoted).

**Changes vs S2.** Replaces F1 (Searle via the SEP) with the book itself for status functions, "X counts as Y in C", continued acceptance and the money story. Keep F1 only for the SEP's one-paragraph summary.

**Toy idea.** The "X counts as Y in C" table: three X-terms, a C-term, and a Y-term (a status with a power); then a second table that iterates (citizen, then President). A "who declares?" column makes the card's "declare" job concrete. Say "toy, ours".

---

## V8. What would "fully automated" require, job by job [partly sourced, mostly OURS]

The five-job table is ours (topic card section 2). The sources below support only the cells marked.

| Job | What "no human intervention" would require | Support in the sources | Status |
|---|---|---|---|
| **Run** (carry out the work) | Matching, settlement, execution done by software. | The E-mini is "fully electronic" with "no market maker obligations" (KKST pp. 7, 28). US algorithmic share about 70% of equities, over half of futures (IMF p. 86). Harari: forex trading by computers talking to computers, "more than 90 percent" (his claim; trap 49). | Sourced: largely automated in some markets. |
| **Decide** (choose what to do) | Software chooses the objective and the trades, with no human setting the goal or approving size. | Not yet: the 2010 sale was a person's decision (KKST p. 2). Autonomous AI trading without oversight is "mostly speculative" (IMF p. 78); "all participants" expect a human in the loop "in the near term (three to five years)" (IMF p. 83); AI is mostly a signal into a system where "a human trader may ultimately make the trading decision" (IMF p. 83); 59% of investment managers do not plan to integrate AI into executing investment decisions (IMF Fig 3.5, p. 83). Counter-trend: many deep-learning models retrain "without any human oversight" (G&B p. 12), yet developers still set hyperparameters (G&B p. 9). | Sourced: decision of *what to trade at scale* is not automated; the execution rules are. |
| **Check** (verify and regulate) | Software verifies and halts; and something verifies that software. | A pre-set automated safeguard already ran in 2010 (CME Stop Logic, KKST p. 2). Supervisors use AI tools (SupTech 79% of advanced economies, IMF p. 95) and the IMF asks for circuit-breaker recalibration (p. 96). But a supervisory model "may unknowingly promote uniformity" and can be "perturbed or fooled" (G&B p. 25); Harari: algorithms can vet algorithms but "there is no purely technological solution to this recursive problem" (PDF 339). Arora et al.: under a conjecture, in a simple model, a bounded buyer cannot detect tampering even ex post (pp. 51, 55), and tamper-resistant designs exist only in the simple model (p. 60). | Sourced: part automated already; each step needs a checker; the end of the regress is a human institution in Harari. |
| **Declare** (say what counts: money, law, a person) | Software creates statuses that people (or other software) treat as binding. | Searle: statuses exist through collective acceptance and need language-like representation; the book does not say whether machines can be in the "we" (trap 48). Harari: computers "cannot ‘believe’" but create inter-computer realities that act on the physical world (PDF 292-293). | **OURS** as a verdict. Sources give the criteria (acceptance, representation, continued acceptance), not a ruling on machines. |
| **Answer** (bear losses; be held responsible) | Something that can be fined, jailed, sued or blamed takes the loss. | The IMF: "institutions are responsible for AI systems they deploy" (p. 93); participants want a human in the loop partly for "liability" (p. 78). Harari: a human authority to challenge decisions (PDF 333), and "bots don’t have rights" (PDF 345). G&B: weaker explainability may leave regulators unable to say why (p. 13). | Sourced for the *current* legal position; whether an AI could ever "answer" is OURS. |

**What the sources add to "fully automated".**
- Run: yes, in places. Decide: not by the evidence of 2024. Check: partly, and with a human institution at the end of the regress. Declare and answer: the sources describe the human position and do not test the machine case.
- The post must label as ours: (a) the five-job split; (b) any sentence that a machine "could not" declare or answer.

---

## Challenges to the card's provisional thesis (section 5 of topic-card-v2)

1. **"Run and decide can be automated, and in markets largely are."** "Run" yes. "Decide" no, on the IMF's evidence (pp. 78, 83) and in KKST (a person chose to sell). The IMF's "algorithmic" lumps execution rules with decisions (p. 101), so the card's two rows cannot be filled from one IMF number (traps 35, 36).
2. **"The cost is correlated failure."** One of two IMF scenarios (Table 3.1, p. 89); IMF finds risks "contained" now (p. 92) and credits efficiency and liquidity gains (p. 87). KKST's 2010 event is a sell program meeting thin depth, not shared models (trap 40). G&B's herding is a hypothesis about a future mature stage.
3. **"Check can be partly automated."** Understated: a pre-set automatic check already acted in 2010 (CME Stop Logic) and supervisors already use AI (IMF pp. 83, 95). The truly new point from the sources: the human institution at the end of the regress (Harari PDF 339) and G&B's "regulatory deep learning models may unknowingly promote uniformity" (p. 25).
4. **"Declare ... cannot be handed over ... (Searle 1995)."** Searle says status functions need collective acceptance; he does not say machines cannot join it, and the book never raises the case. Acceptance may be implicit and unaware, so the bar is lower than "belief". The claim is ours, and the post should say so. Harari does not settle it either: his own inter-computer realities all work through people (V6c).
5. **"Machines that treat each other as persons."** Harari asks whether AIs could be incorporated as legal persons (PDF 295), a question about law, and says computers "cannot ‘believe’". No source says machines would accept each other as persons.
6. **Hook: "People had built a pause into the market's own rules, and that pause helped stop the fall."** Fine as "prices stabilised after a five-second pause that a pre-set rule triggered" (KKST p. 2, quoting the CFTC-SEC). The JF paper does not test whether the pause caused the recovery, and the authors' pause recommendation is in the 2014 working paper only (trap 32). "About 36 minutes" is ours (trap 34). "Computer programs ran a market into a crash and back" overstates (trap 35).
7. **Lens 2: "m·a² > 1 ... complexity and homogeneity versus stability, by analogy with ecology."** True of May's random webs only. In Haldane and May's own banking toy, more connectivity *attenuates* loan shocks and *amplifies* liquidity shocks; homogeneity is the stronger result. Keep the widget in the ecology panel (traps 42, 43).
8. **Lens 1: "Arora et al.: some products cannot be checked by any realistic checker."** Overstated: under a conjecture, in a simple model, asymptotically, "only a first step" (V4). The authors also offer designs (tree of majorities) that a checker *can* check in the simple model.
9. **Harari's own limits.** He is firmer on "computer-to-computer chains" (asserts) than on "dominate the financial markets" ("may reach a point") or "financial devices intelligible only to other computers" ("may well ... could"). The card says Harari "asserts" that "anything made of words will be taken over by AI": that line is Davos 2026, not *Nexus*; put the *Nexus* lines in the fold-out in firmness order (V6).
10. **Number tension to keep apart.** IMF FX algorithmic share about 27% (US) versus Harari "more than 90 percent" computer-to-computer forex (global) (trap 49).

## Open items

- The CACM 2011 text (V4) is UNSEEN; ask Kunhao for a copy if the post will cite the published article.
- The JF's journal pagination (V1) is UNSEEN; the page numbers here are the manuscript's.
- Nexus: provenance of the PDF (OceanofPDF); note 43's sources not opened; the Prologue was read only for the passages above.
- IMF figure values are read from images (trap 37).
- Searle: printed pages 1-13, 59-67, 86-87, 90-92, 94, 98, 101-103, 105, 112-113, 115-116, 125-139, 142 onward not read; chapters 6-8 (the Background in full, realism, truth) are UNSEEN.
- Cited but unseen: May (1972), Caccioli et al. (2009), Beale et al. (in preparation), Khandani and Lo, Lo (2012), Kirilenko and Lo.
