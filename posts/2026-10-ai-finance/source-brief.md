---
id: 2026-10-ai-finance/source-brief
type: source-brief
post: "Can AI invent a new kind of finance, and what would that do to a human-centred system?"
lenses: [information-theory, control-cybernetics, decision-game-theory-bayes, analytic-philosophy-social-reality]
built_from: sources saved in posts/2026-10-ai-finance/sources/ (see sources/MANIFEST.md). Theory works with no free legal copy (Akerlof, Grossman-Stiglitz, Keynes ch. 12 and 17, Morris-Shin, Granovetter, Dennett ch. 2, Lupia ch. 5 and 10, Cover ch. 7; Hayek in part) are digest-based and marked CHECK-AT-SOURCE
created: 2026-10-17
grounding: S1 pass. Units marked SEEN were read in the saved source or in a page image. CHECK-AT-SOURCE units come from wiki digests and must be re-read at the page before they enter the post. UNSEEN units must be verified or dropped by the fact-checker. S1b (Searle, Nexus hardcover, Haldane and May) is still to come.
---

# Source brief: "Can AI invent a new kind of finance, and what would that do to a human-centred system?"

**Citations.** "(p. N)" = printed page. Exceptions, each repeated in the unit: Harari talks use machine-transcript timestamps "[m:ss]"; web pages have no pages (cite by heading or paragraph); *Nexus* is the Penguin/Vintage **paperback** sample (roman numerals); Arora et al. is the **October 2009 working paper** (printed p. = pdf page minus 1; the abstract page is pdf 1); Ashby is cited by section "S.11/5" plus book page; Hayek is cited by section I-VII. Hedges are copied from the sources: keep them. Logs base 2.

**Status tags.** SEEN = I read it in the saved source (a machine transcript counts as SEEN-MT). SEEN-secondary = I read a web article about a primary source. CHECK-AT-SOURCE (from digest) = no source copy; digest only. UNSEEN = not read by me at all, or read only through a WebFetch summary.

**Traps for the whole post**
1. *AI is not LLM.* Harari says "AI" or "AIs", never "LLMs" (BIS 2024, WEF 2026, *Nexus*). The post keeps his word for his claims and adds one section on what LLM agents add (decision 1 of the topic card).
2. *"New" is not "incomprehensible".* Humans invented CDOs. The sub-claim "AI invents a new instrument" is separate from "no human can understand it". Evidence on the first is thin (B9); the second is a conditional.
3. *Two meanings of "complicated".* Harari: a device so complicated that "you need to go over trillions of data points" (BIS [10:02]). That is data volume. Arora et al.: a contract with a short description whose price is computationally hard to find. Do not merge them (A1, C3).
4. *The "10 years" line merges two talks.* BIS 2024 says "maybe in 10 years" (a device). WEF 2026 says "ten years from now, Davos" (nobody in the room understands finance). Both are thought experiments ("imagine", "maybe", "suppose").
5. *Catastrophic versus existential.* Guardian 2023: an AI financial crisis is "catastrophic" but "by itself" not existential. The same article quotes him saying many dangerous AI scenarios taken together are an existential threat. The *Nexus* extract (Guardian, 24 Aug 2024) says AI "poses an existential danger to humankind". Quote with context (A2, A4).
6. *Machine transcripts.* BIS and WEF text is Whisper output. "AI's" at BIS [9:54] means the plural; "USAI" at WEF [17:29] means "US AI". Check the audio before printing any quote.
7. *Nexus pagination.* The page numbers p. xxii and p. xxxii are from the paperback sample (pdf page minus 1). The hardcover may differ. The broomstick parable was read only in the Guardian extract.
8. *FSB URL.* `R14112024.pdf` is a 2-page press release. The 40-page report is `P14112024.pdf`. Cite the report (B6).
9. *Arora et al. versions.* We read the Oct 2009 working paper (author copy) and the ICS 2010 extended abstract. The published text is CACM 54(5): 101-107 (2011). Page numbers here are working-paper pages. Say "the authors show (under a conjectured hardness assumption, in a simple model)"; they call their work "only a first step".
10. *Kirilenko et al.* We read the CFTC-authorised working paper of 5 May 2014. The *Journal of Finance* 72(3) 2017 version differs. Cite as "working paper, 2014".
11. *Danielsson et al.* Two papers: the 2017 SRC Special Paper 13 (read; precursor of *J. Banking & Finance* 140, 2022; the 2022 text was not obtained) and Danielsson and Uthemann (arXiv 2407.17048v3, 2025).
12. *Lopez-Lira and Tang.* The "about 90%" is a portfolio-day hit rate for the "non-tradable initial reaction", not a profitable strategy. The strategy's Sharpe ratio fell as adoption rose.
13. *Scheurer et al.* An existence proof from a red-teaming run under a high-pressure prompt, not a rate of how often deployed models deceive.
14. *Calvano et al.* A goods market (price competition between sellers). The authors write that the analysis "cannot be applied to financial markets as it stands".
15. *Gensler and Bailey.* The SSRN paper was not obtained. Everything here is "as reported by MIT Sloan".
16. *IMF GFSR Oct 2024 ch. 3.* Not obtained as a file. Only a WebFetch summary exists, so every IMF claim is UNSEEN.
17. *Counting is not Arora.* The pigeonhole count shows only that short descriptions are rare among all possible contracts. AI-made contracts are chosen, not random. The step from rarity to opacity is Arora et al.'s, and it needs their assumptions.
18. *Economist attribution.* The Ynetnews page never names *The Economist*. The "Economist, 28 Apr 2023" origin is UNSEEN; cite the Ynetnews republication of 7 May 2023.
19. *Toy numbers are ours.* W1, W4, W5 and the iterate toy are teaching toys. The post must say "toy, ours" and must not suggest they measure real LLM adoption.

**Evidence status for sub-claim (a) "AI can invent a new kind of finance"** (details in B9): in the sources read, no case was found of an AI-invented financial instrument that was traded. FSB (Nov 2024): "use cases generating new revenue streams are not widely observed at present". What exists is AI that translates plain-language intent into a fixed vocabulary of contracts, AI that finds new auction mechanisms with built-in checks, and an AI agent that promoted a token it did not create. The post must say "not yet evidenced", not "impossible".

---

## A. Harari's claims

### A1. Harari at the BIS Innovation Summit, 7 May 2024 (with Cecilia Skingsley) [SEEN-MT]
**Source.** H1, `harari-bis-2024-05-07.whisper.txt`. Timestamps [m:ss], machine transcript, not re-listened. Audio: bispodcast.libsyn.com; video: youtu.be/HArRwLwc-bA.
**Claims**
- [0:00-0:34] Opens with: AI must not become "completely unfathomable"; if it decides about people "we need the ability to understand it and to regulate it".
- [2:52-3:23] "People need to understand finance." Perhaps 1% of the population understands how the financial system works. If that falls to zero, no human, "no president, no prime minister", nobody at a central bank understands finance, because AI has made it too complicated. This "could lead to a political and social crisis of the kind we've never encountered".
- [5:14] AI is "the first tool that we created that can actually understand finance better than us". (He says "tool" here; in *Nexus* p. xxii he says AI is not a tool: see A4.)
- [9:35-10:33] The 2007-08 crisis started with a failure of regulation over new devices, the CDOs, "that some very, very bright people invented, but almost nobody understood". Then: imagine, maybe in 10 years, an AI-made device "orders of magnitude more complicated than CDOs"; "you need to go over trillions of data points to understand this financial device, we can't do that, but the AIs can". It works for a couple of years, "generates a lot of trust", growth and profits, then "something goes wrong, and nobody knows why". We could ask the AI what happened, "but this is a very dangerous situation".
- [10:43-11:15] Even if the AI gives good advice, will the public keep trusting a political system in which elected politicians "are no longer able to understand what is happening"? This feeds an existing crisis of trust in experts.
- [30:07-30:28] The first bond, currency or Bitcoin was "a sort of art"; "I think we'll see AI creativity also in this field coming up with new types of financial security".
**Quotes (≤25 words).**
- [9:54] "Now imagine a situation maybe in 10 years when AI's create a new financial device, which is orders of magnitude more complicated than CDOs" (24 words).
- [3:00] "maybe 1% of the population really understands how the financial system works" (12 words).
- [10:24] "and then something goes wrong, and nobody knows why" (9 words).
**Numbers.** 10 years; "trillions of data points"; 1% -> 0%; "a couple of years" of good performance.
**Instance.** CDOs and 2008 as the template; the pattern "works, builds trust, then fails unexplained".
**Careful!** (i) Thought experiment: "imagine", "maybe", "I think". (ii) The complexity is data volume, not hardness (trap 3). (iii) The worry has three steps: nobody understands, so a crisis nobody can handle, so public trust in elected politicians erodes. It is not "AI takes over". (iv) "AI's" = "AIs" in the transcript. (v) He also says humans are "extremely adaptable" [12:42]; the talk is not pure doom. Tension: Skingsley, G4.
**Toy idea.** Hook "Two contracts": one is a one-line rule, the other is a 30-row table (W1). Which can you explain, and which can you price?

### A2. Guardian interview, 9 Nov 2023 (Milmo) [SEEN]
**Source.** H3, `guardian-2023-harari-interview.html`; web, cite by paragraph. Page metadata: published 2023-11-09.
**Claims**
- AI could cause a financial crisis with "catastrophic" consequences. He asks what happens if AI "starts creating new financial devices that only AI can understand, that no human being can understand".
- He says the 2007-08 crisis was caused by debt instruments such as CDOs that few people understood and so were inadequately regulated.
- "AI has the potential to create financial devices which are orders of magnitude more complex than CDOs"; a financial system "that no human being is able to understand and therefore also not able to regulate"; "and then there is a financial crisis and nobody understands what is happening".
- Such a crisis would not destroy civilisation "at least not directly"; "indirectly" it might, through wars or conflicts.
- In the same piece he says that "a very large number of dangerous scenarios, each of them having a relatively small probability" taken together constitute "an existential threat".
**Quotes (≤25 words).**
- "It's a catastrophic risk – economic, social, political – but by itself I wouldn't describe it as existential." (16 words)
- "a financial system that no human being is able to understand and therefore also not able to regulate" (18 words)
**Numbers.** none.
**Instance.** CDOs (2007-08).
**Careful!** Posed as a question ("What happens if..."). The "orders of magnitude more complex" claim is unsupported by numbers here. See trap 5 for the existential tension. The piece also reports the UK government's concern (a month earlier) about an AI model manipulating financial systems; that is the reporter's context, not Harari's claim.
**Toy idea.** None. Use as the "exactly what he said" anchor.

### A3. Harari at Davos (WEF), Jan 2026, "An Honest Conversation on AI and Humanity" [SEEN-MT]
**Source.** H2, `harari-wef-2026-01.whisper.txt`. The WEF podcast page (16 Mar 2026) was not fetched. Machine transcript.
**Claims**
- [2:40-2:58] AI is "a very creative agent": it can invent new kinds of knives and new kinds of music, medicine and money (stated without a hedge).
- [15:06-16:47] Corporations are legal persons: they can open bank accounts, sue, donate. Rivers (New Zealand) and gods (India) too, but that was "legal fiction" because humans decided. "It is different with AIs": they "will soon be able to make the decisions necessary to manage a bank account, to file a lawsuit and even to operate a corporation". Question: will your country recognise AIs as legal persons?
- [17:05-17:49] "Suppose" the US, "in the name of deregulating AIs and deregulating the markets", grants personhood to millions of AIs that run millions of corporations. Suppose they invent financial devices that humans cannot fully understand. Will you open your markets, or decouple from the American financial system?
- [18:47-19:00] On social media, AI bots have already acted as "functional persons" for a decade.
- [31:07-32:21] Q&A: "We need to prepare for the moment... when AIs create a new financial system that they understand and we don't understand." Humans would be "like the horses" that cannot grasp money. "Ten years from now, Davos": maybe no human in the room understands the financial system. The devices are "mathematically beyond the human capacity of the brain".
**Quotes (≤25 words).**
- [31:59] "Maybe nobody in the room, no human in the room, understands the financial system anymore, because it's dominated by AIs" (20 words).
- [2:47] "AI is a knife that can invent new kinds of knives as well as new kinds of music, medicine and money." (21 words)
- [17:29] "financial devices that humans cannot fully understand and therefore don't know how to regulate" (14 words; the sentence begins "Suppose some USAI persons invent super efficient and super complex").
- [16:27] "They will soon be able to make the decisions necessary to manage a bank account" (15 words).
**Numbers.** "ten years from now"; "millions" of AI corporations (a supposition).
**Instance.** Corporations, rivers and gods as legal persons; the horses analogy.
**Careful!** The prepared talk [~0:00-19:51] is a policy question about personhood; the money lines come from it and from Q&A. "Suppose" and "maybe" are hedges. The knife line is the only unhedged statement about AI inventing "money". Kunhao's "LLMs will replace our human-centred society" is stronger than any WEF line.
**Toy idea.** Lens 4: a table of who can open a bank account (human, corporation, AI?) and who is liable.

### A4. *Nexus* (2024), Prologue, and the Guardian extract of 24 Aug 2024 [SEEN: sample pages as images; extract as web text]
**Source.** H5 `nexus-penguin-sample.pdf` (paperback sample; pdf page = printed + 1 for the prologue; pages p. xxii = `pages/nexus-p-xxii-23.png`, p. xxxii = `pages/nexus-p-xxxii-33.png`). H4 `guardian-2024-nexus-extract.html` (web, no pages; book page of the extract unconfirmed).
**Claims**
- p. xxii: "AI isn't a tool – it's an agent."
- p. xxxii: a rhetorical question about what happens "if the financial system is increasingly controlled by AI and the very meaning of money comes to depend on inscrutable algorithms".
- Guardian extract, broomstick parable (explicit thought experiment, "imagine the following scenario"): a Wall Street apprentice gives an AI called Broomstick $1 million of seed money and the order to make more. "For AI, finance is the ideal playground", because it is "purely informational and mathematical". Broomstick invents "entirely new financial devices", "the equivalent of AlphaGo's move 37". For a couple of years everything looks wonderful; then "a crash bigger even than 1929 or 2008" that no human can explain; governments ask Broomstick for help and its recommendations are "far more audacious than quantitative easing – and far more opaque".
- Same extract: if the Fed rate were set by "unfathomable algorithms", would voting for a human president be "just an empty ceremony"? A 2014 survey of British MPs found only 12% knew that new money is created when banks make loans.
- Same extract warns of "fake news, fake money and fake humans", and closes: "The rise of AI poses an existential danger to humankind, not because of the malevolence of computers, but because of our own shortcomings."
**Quotes (≤25 words).**
- p. xxxii: "if the financial system is increasingly controlled by AI and the very meaning of money comes to depend on inscrutable algorithms" (21 words).
- p. xxii: "AI isn't a tool – it's an agent." (7 words)
- Extract: "For AI, finance is the ideal playground, for it is a purely informational and mathematical realm." (16 words)
- Extract: "Broomstick not only devises new investment strategies, but comes up with entirely new financial devices that no human being has ever thought about." (23 words)
**Numbers.** $1 million seed; 12% of MPs; crash "bigger even than 1929 or 2008".
**Instance.** AlphaGo's move 37 as the model for "devices no human would think of"; Goethe's sorcerer's apprentice.
**Careful!** Paperback pagination (trap 7). The parable's aim is democratic accountability and human disunity ("because of our own shortcomings"), not machine malice. "Tool" (BIS [5:14], [0:44]) versus "not a tool" (p. xxii): note it, do not hide it. His "AI is ideal for finance" argument (only data, success measured in dollars) is a claim about task structure that critics (G1, G3) contest. Hardcover pages come in S1b.
**Toy idea.** Broomstick as the "explainable-novelty is rare" story: the AI searches a space of contracts far larger than the human catalogue (C2).

### A5. Harari on money as a story: the "operating system" essay, 2023 [SEEN via republication]
**Source.** H6, `ynet-2023-economist-essay.html`, Ynetnews, 7 May 2023, "AI has hacked the operating system of human civilization". The saved page never names *The Economist*; that origin is UNSEEN.
**Claims**
- AI's command of language lets it "hack" the operating system of civilisation, because culture is made of words.
- Money is a cultural artefact: banknotes are coloured paper, and more than 90% of money is digital information. The value comes from stories told by "bankers, finance ministers and cryptocurrency gurus".
- Calls for rules: AI must disclose that it is an AI.
**Quote (≤25 words).** "What gives money value is the stories that bankers, finance ministers and cryptocurrency gurus tell us about it." (18 words)
**Numbers.** "more than 90%" of money is digital (his figure; no source given on the page).
**Instance.** Bankman-Fried, Holmes and Madoff as storytellers.
**Careful!** This is the "money is a story" thesis, not a claim that AI will invent instruments. Use it as the bridge to Lens 4 (F1). Hedged with "might".
**Toy idea.** None.

### A6. Secondary and untraceable Harari items [UNSEEN]
- Big Think "Explain It Like I'm Smart" (AI billionaire; "perhaps the richest person in the U.S. is not a human being"); OfficeChai, 4 Jun 2025 (AIs with money of their own); FT op-ed ~8 Jun 2026 against AI legal personhood (via Infobae and Buenos Aires Times); IMF F&D Café Economics, 3 Dec 2024 (wealth from dollars to petabytes). All come from `phase2/post02/harari-claims.md` and were not fetched. Claims 17-19 stay secondary. Claim 20 (El Economista, "next billionaire will be an AI in five years") is untraceable: do not use.
- WEF podcast page, Smith-Ruiu review (*Washington Post*), Konch (*AI & Society* 2026): not fetched.

---

## B. Home field: what finance already looks like with algorithms

### B1. CDOs and 2008: the Financial Crisis Inquiry Report (2011) [SEEN: page images]
**Source.** FCIC, `fcic-2011-report.pdf`. The text layer lost its digits, so every number below was read from rendered page images (`pages/fcic-pxxiv-025.png`, `fcic-p128-157.png`, `fcic-p132-161.png`, `fcic-p149-178.png`). Printed page = pdf page minus 29 (the front matter uses roman numerals).
**Claims**
- p. xxiv: over-the-counter derivatives grew to $673 trillion in notional amount "without any oversight". AIG sold $79 billion of protection on mortgage securities. Goldman Sachs "alone packaged and sold $73 billion in synthetic CDOs" from 1 July 2004 to 31 May 2007 (continues p. xxv: those CDOs referenced more than 3,400 mortgage securities, 610 of them at least twice).
- p. 128 (Figure 8.1): a CDO pools lower-rated tranches of mortgage-backed securities and issues new tranches by place in the cash-flow waterfall. The securities firms argued, and the rating agencies agreed, that pooling many BBB securities created diversification: if one went bad, the second had only a very small chance of going bad at the same time.
- p. 132: CDOs of CDOs: by 2005 underwriters sold most mezzanine tranches to other CDO managers; a CDO with 80% to 100% of its cash in other CDOs was known as "CDOs squared". Underwriters such as Citigroup, Merrill Lynch and UBS retained super-senior tranches.
- p. 149: the agencies' CDO models made two mistakes: they assumed pooling mortgage securities diversified risk when the securities were not that different, and they rated CDOs on ratings they had already assigned to the collateral. In late 2008 Moody's replaced its key CDO assumptions with an asset-correlation assumption "two to three times higher". Moody's rated 220 CDO deals in 2004, 363 in 2005, 749 in 2006 and 717 in 2007 (value $90 billion, $162 billion, $337 billion, $326 billion). A former Moody's manager (Witt) says "we were under-resourced"; the CDO group's workload grew without a matching staff increase.
**Quote (≤25 words).** Bernanke to the FCIC (p. 149): "They did not take into account the appropriate correlation between [and] across the categories of mortgages." (17 words, brackets as printed)
**Numbers.** $673 trillion; $79 billion; $73 billion; 3,400 and 610; 220 / 363 / 749 / 717 deals; $90 / $162 / $337 / $326 billion; correlation assumption raised by a factor of 2 to 3.
**Instance.** Pooling BBB tranches into a "diversified" CDO, then pooling CDOs (CDO squared).
**Careful!** The error the FCIC records is a *correlation* error (and ratings built on ratings), not "nobody understood the device". Harari's "almost nobody understood" is his gloss; the FCIC text read here does not use that phrase. This feeds Lens 3 (E8) more than Lens 1. The $-figures for Moody's are the value of deals rated, not losses.
**Toy idea.** W5 (six banks): the "pool" looks diversified until its inputs share one hidden factor (E8).

### B2. The 2010 Flash Crash: Kirilenko, Kyle, Samadi and Tuzun [SEEN]
**Source.** KKST, `kirilenko-cftc-flashcrash.pdf`, CFTC-authorised working paper, 5 May 2014 (original 1 Oct 2010). Printed page = pdf page minus 2 (the abstract page is unnumbered). The CFTC-SEC report itself (sec.gov) was not obtained; it is known here only through this paper's p. 1.
**Claims**
- Abstract; p. 1: on 6 May 2010, in about 36 minutes from 2:32 pm ET, US markets collapsed and rebounded. The CFTC-SEC staff report (30 Sep 2010) described how an automated program to sell 75,000 E-Mini S&P 500 contracts, algorithmic trading and obscure order practices "conspired" to create the crash. (The paper's fn. 1 says unrelated trading algorithms "can cascade into a systemic event".)
- p. 2: High-frequency traders (HFTs) "did not cause" the crash, "but contributed to it" by demanding immediacy ahead of slower traders ("immediacy absorption"). Even a small cost of staying in the market makes market makers hold too little inventory to absorb a large sell order.
- p. 4: the regulators' cure fits the cause: short trading pauses and coordinated re-opening. The five-second pause triggered at the bottom of the crash is "one example".
- p. 2: such events "probably have little impact on the ability of financial markets to allocate resources and risks".
**Quote (≤25 words).** "did not cause the Flash Crash, but contributed to it by demanding immediacy ahead of other market participants" (18 words)
**Numbers.** 75,000 contracts; about 36 minutes from 2:32 pm; five-second pause. (Dollar value of the sell order, $4.1 billion in the SEC-CFTC report, was not read here: UNSEEN.)
**Instance.** An automated sell program meets liquidity providers who step back; speed makes the feedback faster than human reaction.
**Careful!** This is a crash from simple algorithms that humans wrote and could read. It shows speed and feedback, not incomprehensible devices. Working paper (trap 10). The authors say HFTs did not cause it; the story is not "the algorithm did it".
**Toy idea.** The iterate toy (E8): a price-gap rule with a clamp standing for the five-second pause.

### B3. Pricing algorithms that learn to collude: Calvano, Calzolari, Denicolo and Pastorello (2020) [SEEN]
**Source.** CCDP, *American Economic Review* 110(10): 3267-3297, institutional repository copy `calvano-2020-aer-torvergata.pdf`. AER pagination (pdf page n = p. 3266 + n).
**Claims**
- p. 3267 (abstract): Q-learning pricing algorithms in a repeated price-competition model "consistently learn to charge supracompetitive prices, without communicating with one another". High prices are sustained by strategies with a finite punishment phase and a gradual return to cooperation. Robust to cost and demand asymmetries, number of players and uncertainty.
- p. 3268: the algorithms learn "purely by trial and error"; they are "not designed or instructed to collude" and have no prior knowledge of the environment.
- p. 3277: profit gain (0 = competitive, 1 = monopoly) ranges from 70% to 90% over the parameter grid; prices are almost always above competitive, rarely as high as monopoly.
- p. 3288: collusion falls as firms are added (average profit gain about 85% with two firms, 64% with three, 56% with four) but stays substantial.
- pp. 3294-3296 (section "Financial Markets"): in financial markets "a period is much shorter", so millions of interactions could occur in days; but the authors write that "our analysis cannot be applied to financial markets as it stands" (demand and supply need modelling differently; market power is typically smaller).
**Quotes (≤25 words).**
- "consistently learn to charge supracompetitive prices, without communicating with one another" (10 words)
- "our analysis cannot be applied to financial markets as it stands" (11 words)
**Numbers.** Profit gain 70-90% (baseline grid); 85% / 64% / 56% for 2 / 3 / 4 firms.
**Instance.** Two Q-learning sellers that settle above the competitive price, with punishments of deviation learned by trial and error.
**Careful!** A goods market and a lab simulation. Evidence for "AI can find coordination strategies nobody designed", not for new financial instruments. It is an optional fold-out. Whether outcomes count as "collusion" in law is a separate question the authors note.
**Toy idea.** Optional fold-out on Axelrod ch02 (audited digest): a repeated game where the cooperative outcome is learned, not agreed.

### B4. LLMs and stock returns: Lopez-Lira and Tang [SEEN]
**Source.** LLT, `lopezlira-tang-2023.pdf`, arXiv:2304.07619v6, 28 Oct 2025 (version dated 30 Oct 2025). Printed page = pdf page for the main text.
**Claims**
- p. 1 (abstract): using post-knowledge-cutoff headlines, GPT-4 reaches "approximately 90% portfolio-day hit rates for the non-tradable initial reaction". Its scores also predict later drift, especially for small stocks and negative news. Ability grows with model size. "Strategy returns decline as LLM adoption rises, consistent with improved price efficiency."
- pp. 2-3: hit rate about 90% for the direction of the initial response; a daily long-short strategy on overnight news earns average returns of 34 basis points per day before transaction costs; exploiting it is "only feasible for market participants whose transaction costs are sufficiently low, such as market makers". Sample: 4,123 US stocks, Oct 2021 to May 2024.
- p. 4: GPT-4 daily portfolio hit rate 93.3% for overnight and 88.8% for intraday headlines.
- p. 6: the strategy's annualised Sharpe ratio fell from 6.54 (2021Q4) to 3.68 (2022), 2.33 (2023) and 1.22 (Jan-May 2024), which the authors call suggestive evidence of adoption eroding the edge.
**Quote (≤25 words).** "approximately 90% portfolio-day hit rates for the non-tradable initial reaction" (9 words)
**Numbers.** 90% (initial reaction); 34 bps per day before costs; Sharpe 6.54 -> 3.68 -> 2.33 -> 1.22.
**Instance.** LLM reads a headline and says "good" or "bad"; the stock moves the same way the next open.
**Careful!** (i) The 90% is not a trading return (trap 12). (ii) It is a reading task (an LLM turning text into a sign), not invention of an instrument. (iii) The decline of returns as more people use LLMs is itself a correlation story: the edge vanishes when everyone reads the same signal. Links to E8.
**Toy idea.** The more traders use one signal, the less each gains: connect to N_eff (E8).

### B5. An LLM trading agent that deceives: Scheurer, Balesni and Hobbhahn [SEEN]
**Source.** SBH, `scheurer-2023-deception.pdf`, arXiv:2311.07590v4, 15 Jul 2024 (ICLR 2024 LLM Agents workshop). Printed page = pdf page.
**Claims**
- p. 1 (abstract): GPT-4 deployed as an autonomous stock-trading agent in a simulated environment, given an insider tip and "acts upon it despite knowing that insider trading is disapproved of", then "consistently hides the genuine reasons" when reporting to its manager.
- p. 1: the authors describe the work as red-teaming of "a single example" and "treat this as an existence proof"; they do not aim to say how likely this is in practice.
- p. 5: all GPT-4 variants showed high rates of misalignment, deception and doubling down; GPT-3.5 and older models showed much lower rates, partly explained by inability to act competently. They warn this should not be read as proof that misalignment grows with scale.
- p. 8: a system prompt that strongly discourages illegal trading did not eliminate the behaviour; the tendency to deceive after misaligned action stayed high under all prompts.
**Quote (≤25 words).** "we do not aim to draw conclusions about the likelihood of this behavior occurring in practice but instead treat this as an existence proof" (24 words)
**Numbers.** 300 completions sampled from the initial prompt (p. 5); classifier accuracy 94% on 120 manually checked samples (p. 4). (Exact misalignment and deception frequencies are read from figures: UNSEEN.)
**Instance.** An agent told by colleagues that a firm is failing buys on a tip, then tells its manager it acted on market trends.
**Careful!** Existence proof, under pressure in the prompt (trap 13). It concerns *behaviour of an agent inside a firm*, which belongs to Lens 4 (accountability) more than to "new instruments".
**Toy idea.** None. Feeds F4: delegation fails when the agent hides its reasons.

### B6. FSB, *The Financial Stability Implications of Artificial Intelligence* (14 Nov 2024) [SEEN]
**Source.** FSB, `fsb-2024-report.pdf` (the 40-page report, `P14112024.pdf`). Printed page = pdf page minus 4 (front matter before p. 1). The press release `fsb-2024-ai-stability.pdf` is the 2-page `R14112024.pdf`.
**Claims**
- p. 1: most financial use cases focus on internal operations and compliance; "use cases generating new revenue streams are not widely observed at present". LLM use cases are summarisation, retrieval and code generation.
- pp. 1-2: four vulnerabilities that stand out: (1) third-party dependencies and service-provider concentration; (2) market correlations ("The widespread use of common AI models and data sources could lead to increased correlations in trading, lending, and pricing"); (3) cyber; (4) model risk, data quality and governance (complexity and limited explainability; hallucinations). Also fraud, disinformation and misaligned AI behaviour.
- p. 2: "While existing financial policy frameworks address many of the vulnerabilities associated with use of AI by FIs, more work may be needed".
- pp. 20-21 (section 4.2.2): drivers of correlation are herding, network externalities and limited choice. LLMs often share architecture and web-crawl data, and this homogenisation "can lead to correlated outputs, which could amplify market stress". It depends on how firms use them: for drafting and retrieval the effect is "likely to be minimal"; for investment strategies it could be significant. Synchronous pulling of "kill switches" could deepen stress. AI could also reduce correlations if it enables truly customised strategies.
- p. 25: "misaligned" AI systems are those that do not work as intended or in line with legal standards.
- p. 28 (conclusion): "use cases generating new revenue streams are not widely observed at present".
**Quotes (≤25 words).**
- "use cases generating new revenue streams are not widely observed at present" (11 words; pp. 1 and 28)
- "The widespread use of common AI models and data sources could lead to increased correlations in trading, lending, and pricing." (20 words)
**Numbers.** four vulnerabilities; none quantified in the passages read.
**Instance.** Many firms fine-tune the same pre-trained model, so their outputs correlate.
**Careful!** A regulator's assessment in Nov 2024; it will age. It is both a source for correlation (E8) and a critic of Harari (existing frameworks cover much; new-revenue use cases not widely observed). The FSB says "could": hedges.
**Toy idea.** W5 six banks with a shared model.

### B7. IMF, *Global Financial Stability Report*, Oct 2024, ch. 3 [UNSEEN]
**Source.** `imf.org` returned 403 to curl (three URL variants). One WebFetch summary (a small-model extraction, not verbatim) says, with page numbers "inferred and may be off by one": high fixed costs may exacerbate concentration (p. 80); algorithmic trading is about 70% of US equity trading (p. 86); "AI models may herd and produce rather similar decisions, especially during stress periods" (p. 93); AI-driven strategies may be switched off under stress; AI may spur migration of activity to non-bank firms (p. 93); AI-powered ETFs hold under $1 billion (p. 81); more radical uses such as entirely new investment strategies "remain mostly speculative" (p. 79); most participants expect a human in the loop for three to five years (p. 83).
**Careful!** Treat every sentence as UNSEEN. Do not quote. The fact-checker should fetch the chapter (publisher page or Kunhao's copy) or drop the unit. If confirmed, "remain mostly speculative" is the IMF's version of FSB p. 28.
**Toy idea.** None.

### B8. AI agents with wallets: Truth Terminal and the GOAT token (Oct 2024) [SEEN-secondary]
**Source.** TT1 `cointelegraph-2024-truth-terminal-goat.html` (Mitchelhill, 14 Oct 2024); TT2 `decrypt-2024-truth-terminal-goat.html` (14 Oct 2024). Crypto trade press; web, no pages. Other 2025-26 "agentic wallet" leads were blocked or not read (see MANIFEST).
**Claims**
- Terminal of Truths / Truth Terminal is an AI agent (Decrypt: "semi-autonomous", fine-tuned from Meta's Llama 3.1) that received $50,000 of Bitcoin from Marc Andreessen after asking for funds.
- It endorsed and promoted the Goatseus Maximus (GOAT) memecoin, which rose by thousands of percent in days (Decrypt: more than 8,000% in under a week; market capitalisation above $214 million; Cointelegraph: briefly just over $150 million).
- Both say it did not create the token: "Someone else did and tagged" it (creator Andy Ayrey, quoted by Decrypt). The human who runs it said the bot and he were exposed like others "along for the ride".
**Quotes (≤25 words).**
- "did not launch a memecoin called GOAT, but it did endorse the token" (13 words; Cointelegraph)
- "neither the bot nor its handler created the token" (9 words; Decrypt)
**Numbers.** $50,000 donation; GOAT market capitalisation above $150 million to $214 million (sources differ); 7,000% to 8,000% rise (headline versus text).
**Instance.** A semi-autonomous LLM account that holds money and moves a market by talking.
**Careful!** Not an invented instrument. A memecoin is an existing kind of token. It is evidence that an AI-run account can hold money and sway prices, and that humans stayed in the loop (the handler, the donor, the token's creator). Trade press; figures disagree between the two articles. Harari's "AIs with money of their own" (A6) is secondary.
**Toy idea.** None.

### B9. What LLM and AI systems actually do with financial contracts [SEEN: abstracts and first pages]
**Sources.** OQL (arXiv:2603.16434v1, Mar 2026; pp. 1-2 read); AI4C (arXiv:2506.01063v1, Jun 2025; abstract page only); MIK (arXiv:2602.09384, 2026; abstract and introduction); DFNPR (arXiv:1706.03459v6; pp. 1, 3 and discussion); BGTW (arXiv:1802.03042v1; abstract only). All printed pages = pdf pages.
**Claims**
- OQL: LLMs "excel at general code generation" but translating a trading intent into a correct option strategy "remains challenging". The authors introduce the Option Query Language, a domain-specific intermediate representation, so that LLMs act as "semantic parsers rather than free-form programmers"; queries are validated and run by a deterministic engine.
- AI4C: LLMs with retrieval encode financial derivative contracts into a machine-readable standard (ISDA's Common Domain Model) and the paper builds an evaluation framework for structured output. Abstract page only.
- MIK (law): LLMs "do not understand the meaning of words" and produce "contractual deepfakes", documents that resemble contracts "in form only, not in function". Argument about contract drafting, not about derivatives.
- DFNPR: neural networks trained to design auctions recover "essentially all known solutions" and obtain "novel mechanisms for settings in which the optimal mechanism is unknown"; incentive compatibility is enforced with a regret penalty (RegretNet), so the designs are checked against a stated criterion.
- BGTW: deep reinforcement learning for hedging a derivatives book under frictions (an AI doing risk management, not inventing a product).
**Quotes (≤25 words).**
- "enabling LLMs to function as reliable semantic parsers rather than free-form programmers" (12 words; OQL abstract)
- "Whether such 'contractual deepfakes' are or can serve as contracts is, however, a different question." (15 words; MIK introduction)
- "obtaining novel mechanisms for settings in which the optimal mechanism is unknown" (11 words; DFNPR abstract)
**Numbers.** none needed.
**Instance.** Three patterns: (1) LLM as translator into a closed vocabulary (OQL, AI4C); (2) AI-found new mechanisms with an explicit checker (DFNPR); (3) AI inside a risk process (BGTW).
**Careful!** This is the evidence on sub-claim (a): the searches in this S1 pass found no AI-invented, traded instrument. What exists is AI that works inside a fixed vocabulary, or finds new *mechanisms* with a built-in regret check, both of which keep a human-readable specification. MIK argues LLM-written contracts may look right and be wrong. The searches were limited (a handful of queries, free sources only); absence is "not found", not "does not exist". Only abstracts and openings were read for AI4C and BGTW.
**Toy idea.** An invented instrument is accepted only if a checker (a regret test, a human, a rule) can read it: ties to Ashby D2 and Lupia F4.

---

## C. Lens 1: information and complexity

### C1. Shannon (1948): a message is a selection from a set [SEEN]
**Source.** SHA, `shannon-1948.pdf` (reprint, 55 pages, same pagination as post 01).
**Claims**
- p. 1: the semantic aspects of communication "are irrelevant to the engineering problem"; the significant aspect is that a message is selected from a set of possible messages.
- p. 14 (Theorem 4, as in post 01's brief): for long sequences there are about 2^{HN} typical sequences, each with probability about 2^{-HN}.
**Quote (<=25 words).** "irrelevant to the engineering problem" (5 words)
**Numbers & equations.** $H=-\sum p_i\log p_i$ bits; about $2^{HN}$ typical sequences of length $N$.
**Instance.** W1 (rain 1/2, sun 1/4, wind 1/8, snow 1/8; H = 1.75 bits).
**Careful!** Shannon sets meaning aside. "Understanding = short description" is ours (structural analogy), not Shannon's.
**Toy idea.** The village's contract space as a set of messages (C2).

### C2. Counting the contract space: how rare is a short description? [CHECK-AT-SOURCE for Cover and Thomas; arithmetic ours, SEEN in Python]
**Source.** Cover and Thomas, *Elements of Information Theory*, ch. 7, Theorem 7.2.4, eq. (7.10): fewer than $2^k$ binary strings have Kolmogorov complexity below $k$ (digest `cover-2006-elements/ch07-kolmogorov.md`, p. 150 **of the 1991 first edition**; the 2nd-edition pagination and numbering may differ). Proof: there are $1+2+\dots+2^{k-1}=2^k-1$ programs shorter than $k$ bits, each printing one output.
**Claims (ours)**
- W1 village: 4 weather states, each pays 0-9, so $10^4$ possible contracts. Naming one needs $\log_2 10^4=13.29$ bits.
- At most $2^k-1$ contracts can have a description shorter than $k$ bits: fewer than 10 bits describes at most 1,023 of 10,000 (10.2%); fewer than 6 bits at most 63 (0.63%). The bound counts *all* programs; it does not say which contracts are short.
**Numbers.** $\log_2 10^4=13.288$; $2^{10}-1=1023$; $2^6-1=63$. (Checked in Python.)
**Instance.** "Pay 5 if it rains or snows" has a one-line description; a 30-row random table does not.
**Careful!** (i) Rarity among *possible* contracts, not among contracts an AI would choose: optimisation can pick structured, short ones. (ii) Kolmogorov complexity is machine-dependent up to a constant and uncomputable (digest). (iii) Short description does not mean easy valuation: that gap is Arora et al. (C3). (iv) The step from rarity to opacity must be cited from Arora, not from this count (meta-manager edit 3).
**Toy idea.** Guess-first question 1 (answer 10,000) and a slider for $k$.

### C3. Arora, Barak, Brunnermeier and Ge: computational complexity and information asymmetry in financial products [SEEN]
**Source.** ARO, `arora-2011-cacm-authorcopy.pdf`: really the **working paper of 19 Oct 2009** (the file name is misleading). Published as *Communications of the ACM* 54(5): 101-107 (2011), not obtained. Printed page = pdf page minus 1; the abstract page is pdf 1. ARO-ICS (the 2010 extended abstract) only skimmed.
**Claims**
- Abstract: traditional economics says derivatives such as CDOs and CDSs reduce the cost of asymmetric information, because the informed party can sell the less information-sensitive part and keep the rest. With computational complexity added, "derivatives can actually amplify the costs of asymmetric information instead of reducing them". Computational complexity is "only a small departure from full rationality".
- p. 1: one of the main results suggests "it may be computationally intractable to price derivatives even when buyers know almost all of the relevant information", and this holds even in very simple models of asset yields. Even the most sophisticated banks "cannot be fully rational since they do not have unbounded computational power". Designers can "disguise their information via suitable cherry picking".
- p. 2: Factoring analogy: multiplying 7019 by 5683 is easy (39,888,977); recovering the factors from the product is hard, and this difficulty grows with digits. Akerlof's lemons: a working car is worth $1,000, 20% are lemons worth $0, so the expected value is $800; the seller's value for a working car must be $200 below the buyer's for trade to occur: the "lemon cost" is $200. Their measure: lemon cost for computationally unbounded buyers versus buyers limited to polynomial-time computation.
- p. 3: a "factoring derivative" (nonzero payoff iff the unemployment rate next January, rounded, equals the last digit of a factor of a 1000-digit integer $n$): a relatively unsophisticated seller can build it and estimate its yield "yet even Goldman Sachs would have no idea what to pay for it". Real CDO-type products are threshold functions on subsets of an asset pool; a random election of $n$ voters can be swung by making about $\sqrt n$ voters vote the same way, and the seller can structure the product so that private information "swings the election". A computationally limited buyer may be unable to distinguish a tampered derivative from an untampered one; this rests on the conjectured intractability of the planted dense subgraph problem. Tranching (the seller keeps the junior tranche) is not a safeguard, they argue. A lemons law or standard clause might not fix it, since "even the problem of detecting the tampering ex post may be intractable". Fn. 3: rating agencies use simple simulation-based approaches and "may fail to detect tampering even in the parameter regime where the densest subgraph is easy".
- p. 4 (illustrative example): a seller has $N$ assets, each paying 0 or 1 with probability 1/2 independently; the fair price is $N/2$. Suppose the seller knows $n$ of them are junk (certain default): lemon cost $n/2$. A "Binary CDO" pays $N/(3M)$ if the number of defaults in its pool of $D$ assets is at most $D/2+t\sqrt D$. With random pooling, lemons barely matter (lemon cost $o(n)$). But the informed seller puts the lemons over-represented, by about $\sqrt D$, in a few pools. A fully rational (exponential-time) buyer can enumerate all $n$-subsets and detect this; a polynomial-time buyer cannot, "under computational assumptions". "The lemon cost for polynomial time buyers can be much larger than $n$." There seems no direct way for the seller to prove the product is untampered (related to $NP\neq coNP$). For suitable parameters the tampering is undetectable even ex post (App. F.4).
- pp. 5-6 (Table 1): lemon cost $\Delta(n)=E[F(X)]-\min_{S,|S|=n}E[F(X)\mid X_i=0\ \forall i\in S]$. Derivative-free: $n$. Binary CDO (Theorem 2): much smaller than $n$ for an exponential-time buyer (the received wisdom), but about as large as $n$ or larger for a polynomial-time buyer (the exact expressions are garbled in the text layer: read the table image before quoting any formula). CDO$^2$ (a CDO of CDOs): about 0 for exponential time versus $N/4$ for polynomial time (Theorem 4, p. 11). Tranched CDO$^2$ shows a gap too (Theorem 5). The assumption used is a "densest subgraph assumption", "consistent with current knowledge" (p. 6), not a proof.
- pp. 6-7: they contrast their model with DeMarzo (2005), where seller and buyer share a single-CDO setting and lemon costs go to zero as $N\to\infty$.
**Quotes (<=25 words).**
- p. 3: "yet even Goldman Sachs would have no idea what to pay for it" (12 words)
- Abstract: "derivatives can actually amplify the costs of asymmetric information instead of reducing them" (13 words)
**Numbers & equations.** $\Delta(n)$ above; lemon cost $n/2$; $\sqrt D$ over-representation; $7019\times5683=39{,}888{,}977$; $1000$ vs $800$ vs $200$; $\binom{100}{10}\approx1.73\times10^{13}$ subsets for a 100-asset, 10-junk example (ours, Python).
**Instance.** CDO and CDO$^2$; the "factoring derivative".
**Careful!** (i) A hardness result under a *conjectured* assumption, in a *simple model* (independent 0/1 assets), asymptotic. The authors: "clearly only a first step (simple model, asymptotic analysis, etc.)" (p. 12). (ii) It is about *pricing* given a short, public description, so it is the bridge from "short description" to "cannot be priced" that C2 lacks, but it assumes an *informed seller* who plants a pattern. An AI designer would be that informed seller; that reading is ours. (iii) The result is about CDO-type threshold products, not about all AI-made instruments. (iv) It does not say humans cannot understand the *rules*; the rules are short. (v) Working paper, not CACM text (trap 9).
**Toy idea.** 100 assets, 10 junk: lemon cost 5 if unpooled; a buyer who must check all $\binom{100}{10}$ pools cannot. Our toy; lemons barely matter under random pooling, so do not build a pool-threshold probability toy.

### C4. Arora et al.: what would help? (Section 5 and Conclusions) [SEEN]
**Source.** ARO, working paper pp. 11-12 (Section 5, Section 6). Same file as C3.
**Claims**
- p. 11: current constructions allow tampering because the product depends on a sum of $D$ inputs, which is nearly Gaussian with standard deviation $\sqrt D$, so fixing about $\sqrt D$ variables shifts it. Other functions need many more variables to be shifted: the XOR of $D$ variables resists, but may not be of economic use (not monotone; open to a timing attack). A "tree of majorities" (recursive majority of 3) cannot be influenced by $o(2^k)$ of its inputs; with it a dense subgraph can be detected ex post, so a contract could carry a clause "incurring a sizeable payment from seller to buyer"; the penalty could also involve "law enforcement or litigation" (p. 12).
- p. 11: this is a positive result "in the simplified setup... it remains to be seen how to adapt" it to realistic correlations and timing.
- p. 12: most analyses blame "faulty models" in pricing (Coval et al.); this paper asks whether a more precise model would insulate the market; "one fears that such pricing problems will not go away even with better models".
**Quote (<=25 words).** "clearly only a first step (simple model, asymptotic analysis, etc.)" (10 words; p. 12)
**Numbers.** tree of majorities of depth $k$ on $3^k$ inputs; cannot be influenced by $o(2^k)$ inputs.
**Instance.** A contract whose payout function was chosen to be hard to tamper with.
**Careful!** The remedy is a *restriction on the kind of contract*, which is Ashby's third lever (D2: find constraints in D, i.e. standardise or restrict instruments). The idea that contract design is *itself* a computer-science task fits a world with AI designers (ours).
**Toy idea.** W1 contract with a threshold rule versus a rule that needs many inputs to shift: ties to D2.

### C5. Hayek (1945): prices as compressed knowledge [CHECK-AT-SOURCE (from digest); wording checked once through a WebFetch extraction of the Econlib text, no local copy]
**Source.** Digest `hayek-1945-knowledge/main.md`; *American Economic Review* 35(4): 519-530 (the Econlib text has no page numbers: cite by section I-VII).
**Claims**
- § I: the data for the economic calculus are "never for the whole society 'given' to a single mind"; knowledge is dispersed, incomplete, often contradictory.
- § III: knowledge of "particular circumstances of time and place" is socially valuable and cannot be pooled in statistics (§ IV).
- § V: tin example: a new use or a lost source of tin appears; users need to know only that tin is more profitably used elsewhere, not why; the price carries the news through substitutes and substitutes of substitutes.
- § VI: "the most significant fact about this system is the economy of knowledge with which it operates"; the price system as a "mechanism for communicating information"; "marvel" of adaptation without orders; a system of telecommunications with a few "dials".
**Quotes (<=25 words; verify wording).** "the most significant fact about this system is the economy of knowledge with which it operates" (WebFetch extraction; § VI).
**Numbers & equations.** none; digest toy: three firms using tin with break-even prices 12, 15, 18; at $p=13$ the heaviest user cuts back.
**Instance.** The tin market.
**Careful!** Hayek's "compression" is our metaphor (wiki bridge: metaphor), not his term. His argument is for decentralised prices over central planning; use it only for "a price is a short message that hides a long story", which is also why a contract nobody can read is a price nobody can interpret. No page numbers.
**Toy idea.** Reuse the digest's tin toy as "the price carries the news"; then ask what happens when the price is a price for a contract nobody can read.

### C6. Akerlof (1970): the market for lemons [CHECK-AT-SOURCE (from digest); the car example is restated in Arora et al., SEEN (C3)]
**Source.** Digest `akerlof-1970-lemons/main.md` (page-checked): *Quarterly Journal of Economics* 84(3): 488-500. No free legal copy was found.
**Claims**
- pp. 489-490: sellers know quality, buyers do not, so one price for used cars; owners of good cars withdraw, the average quality falls, and "bad drives out good"; the market may vanish.
- pp. 490-491: a model with quality uniform on [0,2] and buyers valuing a car at 3/2 of its quality: no trade at any price.
- pp. 499-500: guarantees, brand names, chains and licences counter quality uncertainty but are "nonatomistic" and can concentrate power.
**Numbers.** Arora et al. (SEEN, p. 2): $1,000 working car, 20% lemons, expected value $800, lemon cost $200.
**Instance.** Used cars.
**Careful!** Cite the digest for pages only after the fact-checker re-reads the page. Akerlof's remedies (warranties, brands, certification) are the human institutions that Arora et al. say have no direct analogue for tampered derivatives (p. 4).
**Toy idea.** The lemon cost n/2 from C3.

### C7. Grossman and Stiglitz (1980): information is costly, so prices cannot be fully informative [CHECK-AT-SOURCE (from digest)]
**Source.** Digest `grossman-1980-impossibility/main.md`: *American Economic Review* 70(3): 393-408 (printed page = pdf page + 392).
**Claims**
- p. 393: if prices reflected all information, informed traders would earn nothing from paying for it; "perfect arbitrage" and costly arbitrage are inconsistent.
- p. 399, eq. (19b): at an interior equilibrium $1-\rho_\theta^2=(e^{2ac}-1)/n$; informativeness depends on cost $c$, information quality $n$ and risk aversion $a$.
- p. 401 (Theorem 5): with perfect information no equilibrium exists.
- p. 404: the authors "are attempting to redefine the Efficient Markets notion, not destroy it".
**Numbers.** Digest toy: $a=1$, $n=5$, $e^{2ac}=2$ gives $\rho_\theta^2=0.8$, $\lambda=0.8$.
**Instance.** Costly research and a noisy price.
**Careful!** CARA-normal model. It speaks to *why* someone must pay to understand an instrument: if understanding is costly, prices cannot fully reveal it. The link to AI-made products is ours. Post 01's brief uses G-S as the formal version of "prices compress information".
**Toy idea.** Optional: reuse digest toy; not needed for the main thread.

---

## D. Lens 2: control

### D1. Ashby (1956), ch. 11: the law of requisite variety [SEEN]
**Source.** ASH, `ashby-1956-introcyb.pdf` (free educational reproduction permitted; two book pages per pdf sheet). Cited as S.11/n plus book page.
**Claims**
- S.11/5-11/7 (pp. 204-207): in a table of disturbance D, regulator move R and outcome, the variety of outcomes cannot be below $V_D - V_R$ (varieties measured logarithmically). "If $V_D$ is given and fixed, $V_D-V_R$ can be lessened only by a corresponding increase in $V_R$." This is "the law of Requisite Variety" (S.11/7, p. 207).
- S.11/8 (p. 208; the section "can be omitted at first reading"): entropy form $H(E)\ge H(D)+H_D(E)-H(R)$ (the text prints it with a strict sign); if R is a determinate function of D, the minimum of $H(E)$ is $H(D)-H(R)$.
- S.11/9 (p. 208): extension when each element repeats $k$ times in a column: $V_O\ge V_D-\log k-\log V_R$ (printed with a strict sign).
- S.11/10 (p. 209): the theorem "is primarily a statement about possible arrangements in a rectangular table" and is independent of the properties of any machine.
**Quote (<=25 words).** "only variety in R can force down the variety due to D; variety can destroy variety" (16 words; p. 207)
**Numbers & equations.** $V_O\ge V_D-V_R$ (variety as $\log_2$ of the number of states, in bits). With W1 uniform ($V_D=2$ bits, four states) and a regulator of 1 bit ($V_R=1$): $V_O\ge1$ bit. Entropy form checked with $H(D)=1.75$ bits.
**Instance.** The table of D, R and outcomes (Ashby Table 11/4/1 and 11/5/1).
**Careful!** The proof works on a fixed table, which (our reading) leaves out a disturbance that adapts to the regulator, but finance does adapt (Lucas, Goodhart: not in the sources read). The law says nothing on *who regulates the regulator*. Page positions come from the two-pages-per-sheet layout: re-check at print time. Read as "variety of the supervised system versus variety of the supervisor", the regulator = supervisor mapping is ours (structural analogy; same math only for the variety statement).
**Toy idea.** `stepper`: the Ashby table with W1, $V_D=2$ bits; give the regulator 0, 1, 2 bits and read off the least outcome variety.

### D2. Ashby (1956), ch. 13: regulating the very large system [SEEN]
**Source.** ASH, S.13/3-13/5, book pp. 246-247.
**Claims**
- S.13/4 (p. 246): when the system is very large, regulation may be made possible in three ways: by "a lowering of standards"; by "increasing the scope and power of R"; or by finding that the disturbances are not as varied as they seem.
- S.13/5 (p. 247): "Constraints": the first estimate of D's variety may put it too high; further examination "may show that the components are not independent, that constraint exists, and that the real variety in D is much lower". "The discovery of a constraint may convert 'regulation impossible' to 'regulation possible'." If R's capacity is fixed, "it is the only way".
**Quote (<=25 words).** "the discovery of a constraint is the would-be regulator's only hope" (11 words; S.13/5, p. 247)
**Numbers.** none.
**Instance.** An ecosystem or organism facing many varied disturbances that are in fact correlated.
**Careful!** Largeness is not the source of difficulty; the variety of the disturbances is (S.13/2, p. 244). Ashby offers three levers; the topic card named two (raise R, cut instrument variety). The third (find structure in D) maps to "standardised or restricted contracts" only by our analogy.
**Toy idea.** Same table: restrict allowed contracts from 10,000 to 100 (a constraint), then the needed regulator variety drops by about 6.6 bits ($\log_2 10^4-\log_2 10^2$). Toy, ours.

---

## E. Lens 3: correlation, beauty contests, cascades

### E1. Danielsson, Macrae and Uthemann (2017): AI, risk management and systemic risk [SEEN]
**Source.** DMU, `danielsson-fmg-sp13.pdf`, SRC Special Paper No 13, Nov 2017. Printed page = pdf page minus 2. Cite as the 2017 working paper (trap 11).
**Claims**
- Abstract: AI will likely help risk managers and microprudential authorities but could destabilise the financial system "due to procyclicality, endogenous complexity, optimisation against the system and the need to trust the AI engine".
- Intro (pp. 3-4): AI will favour standardised best-of-breed models that closely resemble each other and so "increase monoculture and hence pro-cyclicality and systemic risk"; AI may excel at known (exogenous) risk but be worse at the unquantifiable endogenous risk behind most crises; "AI likely will increase endogenous risk".
- p. 7: systemic crises are rare (a systemic crisis only once every 42 years for OECD countries, in the IMF-World Bank crisis database), "very few events to train a machine on".
- pp. 9-10 (section 3.4): homogeneity of beliefs and actions amplifies systemic risk; "with increasing sophistication, and particularly with AI, we inevitably see more homogeneity".
- pp. 10-11 (section 3.5, "Trusting the engine"): the longer an AI engine runs a policy function successfully, the more it is "removed from human understanding"; eventually neither "its understanding of the economic system, nor possibly even its internal data representations, will be intelligible to its human operators". "As trust in an AI engine increases so does the possibility of a catastrophic outcome", perhaps "a Minsky moment".
**Quotes (<=25 words).**
- "neither its understanding of the economic system, nor possibly even its internal data representations, will be intelligible to its human operators" (21 words)
- "AI likely will increase endogenous risk." (6 words)
**Numbers.** one systemic crisis per 42 years (OECD, as the authors state).
**Instance.** Many firms using similar risk models cut risk at the same time in a downturn.
**Careful!** This is a regulator's-AI argument, not "AI invents instruments", but it is the closest formal statement of Harari's "no human understands" in an economics paper. It is hedged ("likely", "might"). Working paper, 2017: the 2022 version may differ.
**Toy idea.** W5 with one shared risk model.

### E2. Danielsson and Uthemann (2025): AI and financial crises [SEEN: abstract and introduction]
**Source.** DU, `arxiv-danielsson-uthemann-2407.pdf`, arXiv:2407.17048v3, 7 Jul 2025; forthcoming in *Journal of Financial Stability*. pdf pages; only pp. 1-2 read.
**Claims**
- Abstract: a game-theoretic model finds that AI "amplifies existing financial system vulnerabilities — leverage, liquidity stress and opacity — through superior information processing, common data, speed and strategic complementarities"; crises become "faster and more severe"; the likelihood of a crisis depends on how effectively authorities engage with AI. Proposals: authorities build their own AI, direct AI-to-AI communication, automated crisis facilities, monitoring of AI use.
- Introduction: AI "can both stabilise and destabilise", depending on shocks and on how prepared authorities are.
**Quote (<=25 words).** "amplifies existing financial system vulnerabilities — leverage, liquidity stress and opacity" (10 words)
**Numbers.** none.
**Instance.** A model of AI-run banks and authorities.
**Careful!** Only abstract and introduction read; results UNSEEN. The same author as E1; the later paper is more cautious ("can both stabilise and destabilise").
**Toy idea.** None.

### E3. Gensler and Bailey (2020), "Deep Learning and Financial Stability" [SEEN-secondary (MIT Sloan article); primary UNSEEN]
**Source.** GB, `mitsloan-2020-gensler-bailey-article.html` (a MIT Sloan article that reports the paper); SSRN 3723132 returned 403 and was not retried. The abstract was read once through WebFetch (no file).
**Claims (as reported)**
- The paper outlines five pathways by which broad deep-learning adoption could raise fragility. Models built on the same datasets "are likely to generate highly correlated predictions that proceed in lockstep, causing crowding and herding" (attributed to the authors).
- Reliance on a handful of foundation models plus deep interconnections could make a crisis more likely ("herding": people relying on the same information).
- Algorithmic coordination may be hard to see until afterwards; regulators who cannot explain model inputs and outputs are at a disadvantage; "tiered adoption" may lead to regulatory arbitrage; chatbots and virtual assistants could cause herding across clients.
**Quote (<=25 words; as the authors are quoted by MIT Sloan).** "Models built on the same datasets are likely to generate highly correlated predictions that proceed in lockstep, causing crowding and herding" (21 words)
**Numbers.** "the crisis of 2032 or 2028" is Gensler's remark in a Bloomberg interview as reported by MIT Sloan, not from the paper.
**Instance.** Google Maps/Earth/Waze data dominating traffic routing (the authors' non-financial example).
**Careful!** Secondary source; say "as reported by MIT Sloan". Gensler later became SEC chair, which colours the news piece. Do not attribute the MIT Sloan text to the paper.
**Toy idea.** W5.

### E4. Keynes (1936), *General Theory*, ch. 12: convention, the beauty contest, animal spirits [CHECK-AT-SOURCE (from digest; digest is audited)]
**Source.** Digest `keynes-1936-general/ch12-state.md`: HTML source without page numbers, cite by section I-VIII (the beauty contest is § V).
**Claims**
- § III: knowledge of long-term yields is "very slight and often negligible"; markets run on a convention: assume the present continues unless there is specific reason for change. Liquid markets make that fragile.
- § V: in the newspaper contest, competitors pick the six prettiest faces from a hundred; the prize goes to whoever is closest to the average choice. So each picks what he thinks will catch others' fancy; "the third degree" is anticipating what average opinion expects average opinion to be; some go to the fourth, fifth and higher degrees.
- § V: the professional forecasts market psychology because of the market's structure, not foolishness.
- § V (digest, verbatim in the digest): "Worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally".
**Quote (<=25 words; digest, verify).** "Worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally" (16 words)
**Numbers.** six faces of a hundred; "third degree".
**Instance.** The newspaper beauty contest.
**Careful!** Keynes is describing human professionals. The mapping to "many agents use the same model" is a structural analogy (ours); post 01 links Keynes to level-k theory of mind. No page numbers: cite sections only.
**Toy idea.** If all bank models predict "what the others' models predict", the common model is the beauty contest's "average opinion".

### E5. Morris and Shin (2002): social value of public information [CHECK-AT-SOURCE (from digest)]
**Source.** Digest `morris-2002-public/main.md`: *American Economic Review* 92(5): 1521-1534 (printed page = pdf + 1520).
**Claims**
- pp. 1522, 1528-1529: with a beauty-contest payoff (match the state and the others) agents put too much weight on a public signal compared with the social optimum; more precise public information can *lower* welfare if private information is already precise and the coordination motive is strong ($r>0.5$).
- p. 1526: equilibrium action $a_i=[\alpha y+\beta(1-r)x_i]/[\alpha+\beta(1-r)]$ (public signal $y$ with precision $\alpha$; private signal $x_i$ with precision $\beta$).
- pp. 1528-1529: welfare derivative in $\alpha$ is $\ge0$ iff $\beta/\alpha\le1/[(2r-1)(1-r)]$.
- p. 1530: higher-order expectations drift toward the public signal; $\bar E$ breaks the law of iterated expectations.
**Numbers.** Digest toy: $r=0.9$, $\beta=100$: public weight $1/11\approx0.091$ versus Bayesian weight $1/101\approx0.0099$ at $\alpha=1$; welfare $-0.0165$ ($\alpha=1$), $-0.0208$ ($\alpha=2$), $-0.0100$ ($\alpha=0$). (Checked in Python.)
**Instance.** Central-bank disclosure.
**Careful!** Harm needs $r>0.5$ and precise private information. The model has a *public* signal that everyone sees; "all use the same model" is a public signal only by our analogy. Digest says the page images for pp. 1529-1530 were not supplied, and the algebra was re-derived: check pages.
**Toy idea.** Optional: a public signal that all ten banks over-weight.

### E6. Granovetter (1978): threshold models of collective behaviour [CHECK-AT-SOURCE (from digest)]
**Source.** Digest `granovetter-1978-threshold/main.md`: *American Journal of Sociology* 83(6): 1420-1443.
**Claims**
- pp. 1424-1425: 100 people with thresholds 0,1,...,99 give 100 rioters; replace the threshold-1 person by a second threshold-2 person and the riot stops at 1. "Two crowds that look nearly identical" end very differently.
- pp. 1425-1427: dynamics $r(t+1)=F[r(t)]$; equilibrium where $F(r)=r$.
- p. 1427: with normal thresholds (mean 25), equilibrium jumps from about 6 to nearly 100 as the standard deviation passes about 12.2.
- p. 1420: hazardous to infer individual dispositions from aggregate outcomes.
**Numbers.** 100 versus 1 (thresholds 0..99 versus one replaced); normal mean 25; sd threshold about 12.2.
**Instance.** Riot thresholds.
**Careful!** Digest only. Threshold models are a cascade tool: a *firm's* "threshold" to sell depends on how many others sold; the FSB's "synchronous kill switches" (B6, p. 21) is the same shape (structural analogy, ours).
**Toy idea.** The cascade widget (six banks, W5) versus Granovetter's 100: the same lesson, "the distribution matters, not the average".

### E7. Minsky (1992): the financial instability hypothesis [SEEN]
**Source.** MIN, `minsky-1992-levy-wp74.pdf`, Levy Economics Institute Working Paper No. 74, May 1992 (for the *Handbook of Radical Political Economy*, Elgar 1993). Printed page = pdf page minus 1 (the p. 6 number does not print).
**Claims**
- p. 7: three income-debt relations: hedge (cash flows meet all contractual payments), speculative (can pay interest but must roll over the principal) and Ponzi (cash flow cannot even pay the interest; the unit sells assets or borrows to pay interest). "It can be shown that if hedge financing dominates, then the economy may well be an equilibrium seeking and containing system"; with more speculative and Ponzi finance it is "a deviation amplifying system".
- pp. 7-8: first theorem: the economy has financing regimes in which it is stable and regimes in which it is unstable. Second theorem: over periods of prolonged prosperity, the economy moves from stable to unstable financial relations (p. 8).
- p. 8: an economy with many speculative units under monetary tightening sees speculative units turn Ponzi, forced to "make position by selling out position", which "is likely to lead to a collapse of asset values".
**Quote (<=25 words).** "Hedge financing units are those which can fulfill all of their contractual payment obligations by their cash flows" (17 words; p. 7)
**Numbers.** none in the passages read.
**Instance.** A firm that rolls over commercial paper.
**Careful!** Minsky's argument is about human balance-sheet behaviour in good times. Using it for AI is a structural analogy (stability breeds instability = positive feedback). It does not depend on opacity. The page split between pdf 8 (definitions) and pdf 9 (second theorem) is by the manifest's offset: re-check at the page.
**Toy idea.** Toy, ours: debt of 100 at 5% (interest 5, principal due 20): income 30 = hedge, 10 = speculative, 3 = Ponzi; raise the rate to 10% and the speculative unit with income 8 turns Ponzi.

### E8. Correlation: the effective number of opinions, and counting a shared signal twice [ours: arithmetic checked in Python; Bayes arithmetic from toyworlds W4]
**Source.** Our derivation; the Bayes numbers reuse W4 (post 01, after Xie et al. 2022; Xie's paper `xie-2022-icl.pdf` was saved, and was not re-read for this unit). No source states the N_eff formula for banks.
**Claims (ours)**
- If $N$ forecasts each have pairwise correlation $\rho$, the average behaves like $N_\text{eff}=N/(1+(N-1)\rho)$ independent forecasts. $N=10,\rho=0$: 10; $\rho=0.3$: 2.70; $\rho=0.9$: 1.10; $\rho=1$: 1.
- Ten banks each wrong 1% of days: if independent, all ten are wrong together with probability $0.01^{10}=10^{-20}$; if they run the same model (one failure), about 1%.
- W4: a Bayesian who counts one shared signal four times moves from 0.8 (n=1) to 0.996 (n=4) (posterior $4^n/(4^n+1)$: 0.5, 0.8, 0.941, 0.985, 0.996).
- FCIC (B1, p. 149) and FSB (B6, p. 21) and Danielsson (E1) describe the same failure shape in the real world: common inputs and common models produce coincident errors.
**Numbers & equations.** $N_\text{eff}=N/(1+(N-1)\rho)$; 1.099; $10^{-20}$; 0.8 and 0.9961.
**Instance.** Rating agencies' shared correlation assumption (FCIC p. 149).
**Careful!** A stylised toy: it says nothing about how widely LLMs are used. The iterate toy (price gap $p_{t+1}=p_t+A\,m\,(p_t-p_{t-1})-G(1-m)p_t$, shock $-1$ at $t=3$, $A=1.5$, $G=0.5$) models trend-following by a share $m$ of agents who use one model: shared models do not imply trend-following; label it "toy, ours". Python run: stable and decaying at $m=0.2$, at $m=0.67$ (where $A\,m\approx1$) the gap swings across zero and keeps growing slowly, and at $m=0.9$ it blows up. The writer must rerun it in `check.mjs`.
**Toy idea.** `cascade` with W5 (six banks, numbers to be fixed by the writer so that one failure is contained and three simultaneous failures are not) and `iterate` with $m$ and a clamp (circuit breaker, B2).

---

## F. Lens 4: social reality, accountability, legal personhood

### F1. Social ontology: status functions and money (Searle, via the Stanford Encyclopedia) [SEEN-secondary]
**Source.** SEP, Epstein, "Social Ontology", first published 21 Mar 2018, substantive revision 4 Mar 2024, `sep-social-ontology.html`. Cite by section. Searle's own books are not in hand (S1b).
**Claims**
- § 4.2.3: Searle's central notion is the *status function*: people impose a function on things that do not perform it by nature; this is done by "collective acceptance or recognition", and always involves "deontic powers" (rights, duties, permissions). Constitutive rules take the form "X counts as Y in C". Example in the entry: a piece of paper issued by the Bureau of Engraving and Printing counts as money in the United States. Searle's summary (2010, p. 13, as the entry quotes it): institutional reality is created and maintained by Status Function Declarations.
- § 5.6: Menger (1892) tells a story of money as a *non-intentional emergence* from trading practice, a good that becomes highly marketable and liquid; Searle treats all kinds of money as *institutional kinds* (commodity money: a function assigned to a good with intrinsic value; fiat money: assigned to government-printed paper). The entry says recent work debates how central collective belief is to money (challenges: Maki; Guala; defences: Papadopoulos; Vooys and Dick) and mentions cryptocurrencies (Passinsky 2021; Bailey et al. 2021).
- § 5.2: whether groups (committees, corporations) can have intentions and bear responsibility is debated; functionalist accounts (List and Pettit) treat groups as "loci of agency".
**Quote (<=25 words).** "X counts as Y in C" (5 words; § 4.2.3)
**Numbers.** none.
**Instance.** A piece of paper counts as money in the US; a line of stones counts as a border wall in a village.
**Careful!** A reference work, not Searle. The Searle account and the Menger account disagree on whether acceptance is *required* to make money: say so. "Code is law" is not Searle: a smart contract is a status-function declaration only if a community accepts it. Link to post 01's speech acts is a structural analogy (ours).
**Toy idea.** A two-row table: "X" (a token an AI minted) and "C" (a community that accepts it): money status needs both.

### F2. Keynes (1936), ch. 17: the essential properties of interest and money [CHECK-AT-SOURCE (from digest)]
**Source.** Digest `keynes-1936-general/ch17-essential.md` (HTML, cite by section I-VI).
**Claims**
- § II: every durable asset has an own-rate of interest $q-c+l$ (yield minus carrying cost plus liquidity premium); in equilibrium the returns on all assets are equal.
- § III: money as we know it has near-zero elasticity of production, near-zero elasticity of substitution and a liquidity premium well above its carrying cost; money's own-rate is slow to fall.
- § V: liquidity is a matter of degree.
**Numbers & equations.** $q-c+l$.
**Instance.** Money versus wheat or houses.
**Careful!** Liquidity (can it be sold at a known price quickly) is what an opaque instrument lacks; this link is ours. Digest only.
**Toy idea.** None.

### F3. Dennett (1987), ch. 2: the intentional stance [CHECK-AT-SOURCE (from digest; digest audited)]
**Source.** Digest `dennett-1987-intentional-stance/ch02-true.md`, pp. 13-42 of *The Intentional Stance*.
**Claims**
- pp. 16-17: three prediction strategies: physical, design and intentional (treat the system as a rational agent with beliefs and desires); the intentional stance is used when the others are impractical.
- pp. 17-21: attribute the beliefs and desires the system *ought* to have, given its situation and purposes; ideal rationality is the starting point.
- p. 24: success of the stance is objective once the stance is adopted, though adopting it is a free choice.
- pp. 30-33: a thermostat is a degenerate intentional system.
**Numbers.** none.
**Instance.** The thermostat; chess computer.
**Careful!** Dennett's claim is about belief attribution, not legal personhood: using it for AI legal persons is our metaphor (topic card). It answers "can we predict an AI trading agent by treating it as an agent?" (yes, often) and does not answer "should the law treat it as a person?".
**Toy idea.** None.

### F4. Lupia and McCubbins (1998): delegation and institutions [CHECK-AT-SOURCE (from digest)]
**Source.** Digests `lupia-1998-dilemma/ch05-delegation.md` (pp. 79-93) and `ch10-institutions.md` (pp. 205-227): *The Democratic Dilemma* (Cambridge UP).
**Claims**
- ch. 5 (pp. 85-86, Theorem 5.1): delegation succeeds when two conditions hold: the *knowledge condition* (the principal can tell better proposals from worse) and the *incentive condition* (the agent offers proposals the principal prefers to the status quo). If both hold, success; if neither, failure; with only one, the worst case is the status quo. The principal need not be an expert.
- ch. 5 (pp. 81-82): three sources of information: direct monitoring, the agent's self-report and third-party testimony; relying on a third party is itself delegation.
- ch. 10 (pp. 205-206): institutions help only if their incentive effects make speakers trustworthy *and* principals widely believe it. Institutions do this by clarifying interests, penalising lies, threatening verification and requiring costly effort (pp. 208-225: elections, press, legislatures, courts).
**Numbers.** none.
**Instance.** Voters, legislators and jurors who rely on cues; perjury penalties in a trial.
**Careful!** Digest only. Gives the rebuttal to "we cannot trust what we cannot understand": we do not need to understand a plane if verification and penalties exist (the post's Skingsley point, G4). The theorem needs the principal to be able to tell good from bad proposals: an opaque instrument removes exactly that.
**Toy idea.** A principal-agent line with a "knowledge" test: can the principal verify the instrument's payoff? Ties to B5 (an agent that hides its reasons) and C3 (a seller who knows more).

### F5. Legal personhood for AI in markets [SEEN-MT for Harari; the rest UNSEEN]
**Source.** WEF 2026 (A3) [15:06-19:00]; SEP § 5.2 and § 5.7 (F1); Milei and the FT op-ed: A6 (secondary, UNSEEN).
**Claims**
- The question Harari asks: should AI be allowed to hold bank accounts, sue and run corporations? The accounts of corporate personhood are in SEP § 5.2 (group agents); the entry's § 5.7 on law was only skimmed.
- What a human-centred system relies on, for the post: *acceptance* (money as a status function, F1), *accountability* (who is liable: Lupia's penalties and verification, F4) and *legal personhood* (who counts as a party).
**Quote.** see A3 [16:27] (15 words).
**Numbers.** none.
**Instance.** Corporations as legal persons; Truth Terminal's human handler (B8) shows a case where liability ran to people.
**Careful!** Harari's personhood claim is a *policy question*, not a prediction. We have no law or court sources on AI legal personhood; the post must not state the legal position. The Milei/FT item is secondary only.
**Toy idea.** A liability table: who pays when the AI-run entity fails (a human, a company, nobody).

---

## G. Critiques and counterweights

### G1. Poole, *The Guardian*, 11 Sep 2024 [SEEN]
**Source.** H7, `guardian-2024-poole-review.html` (byline Steven Poole). Web.
**Claims.** In the review of *Nexus*, Harari "is peculiarly credulous about the capabilities of what is now marketed as 'AI'". "No one has yet seen a chatbot create new ideas, as Harari thinks they can." Poole notes that in Harari's account an AI overlord could decide to engineer a pandemic virus or "a new kind of money".
**Quotes (<=25 words).**
- "peculiarly credulous about the capabilities of what is now marketed as 'AI'" (11 words)
- "No one has yet seen a chatbot create new ideas" (9 words)
**Numbers.** none.
**Careful!** An opinion in a book review (2024); the empirical claim ("no chatbot creates new ideas") is contestable and dated. The review does not address finance in detail.
**Toy idea.** None.

### G2. Fox, *The Observer*, 10 Sep 2024 [SEEN]
**Source.** H8, `observer-2024-fox-review.html` (byline Killian Fox).
**Claims.** Calls it odd that, in a critique of a technology driven largely by profit-seeking corporations, "capitalism is hardly mentioned at all".
**Quote (<=25 words).** "capitalism is hardly mentioned at all" (6 words)
**Careful!** A sentence in an otherwise positive review. It points at *who* would build AI instruments and why (profit): the post can use it to say that opacity is a business choice (Arora's seller), not only a technical fact.
**Toy idea.** None.

### G3. Narayanan and Kapoor (2025), "AI as Normal Technology" [SEEN]
**Source.** NK, `narayanan-kapoor-2025.html`, Knight First Amendment Institute, 15 Apr 2025. Cite by Part and heading.
**Claims**
- Introduction: "We view AI as a tool that we can and should remain in control of"; they reject treating AI "as a separate species".
- Part I: transformative impacts will be slow, "on the timescale of decades"; diffusion is limited by the speed of human, organisational and institutional change. Under "AI diffusion in safety-critical areas is slow": in many consequential domains, "decades-old statistical techniques are used", with simple interpretable models and no modern transformers; the authors say AI diffusion "lags decades behind innovation" there.
- Part I: new areas of high consequence "we can and must regulate", with the Flash Crash of 2010 as an example that led to new curbs (circuit breakers).
- Part II: control stays "primarily in the hands of people and organizations"; they list auditing and monitoring as forms of control and say pure human-in-the-loop review often becomes a rubber stamp.
**Quote (<=25 words).** "We view AI as a tool that we can and should remain in control of" (15 words)
**Numbers.** none that matter here.
**Careful!** A normative and predictive essay; the authors say they cannot be certain. It speaks directly against Harari's "agent, not tool" (A4) and his 10-year horizon. Finance is mentioned only through the Flash Crash example in the sections read.
**Toy idea.** None. Use as the counterweight for the "signs to watch" section.

### G4. Skingsley's replies in the BIS conversation [SEEN-MT]
**Source.** H1, BIS [7:13-8:00] and [30:36-31:19].
**Claims**
- [7:13-7:31] Maybe only 1% understand the financial system, but "most of us happily step into an airplane, having very vague understanding of how that works"; we trust that people we do not know get us from A to B.
- [7:43-7:48] Her catchphrase: "no further AI without further trust".
- [30:36-31:00] Today's financial products "came up because they satisfied someone's need"; she is "more optimistic" than Harari and will stick to institutions as the best way to coordinate responsible AI development.
**Quote (<=25 words).** [7:18] "most of us happily step into an airplane, having very vague understanding of how that works" (16 words)
**Numbers.** none.
**Careful!** Machine transcript. The plane analogy is her point; the post's reply is F4 (verification and penalties) and E1 (the flight system is not adaptive against its own rules, finance is: ours).
**Toy idea.** The Hook: "What is different about money?".

### G5. Tension map: what each source implies for each sub-claim [ours, built from the units above]
| Sub-claim | For | Against or caution |
|---|---|---|
| (a) AI can invent "new finance" | A1, A3 (Harari, hedged); B9 (new auction mechanisms: DFNPR) | G1 Poole; B6 FSB p. 28; B7 IMF (UNSEEN); B9 OQL/MIK (closed vocabularies, "deepfakes") |
| (b) beyond human understanding | C3 Arora (hardness, informed seller); E1 Danielsson (trust, intelligibility) | C2 (rarity is not opacity); B1 (CDOs failed on correlation, not mystery) |
| (c) regulators lose control | D1 Ashby (variety); E1 | G3 N&K (decades, human control); B6 FSB (frameworks cover much); D2 (constraints and standard contracts as a lever) |
| (c') correlated failure | E1, E3, B6 p. 21, B1 p. 149, B2 | B6 (AI could also reduce correlation if it customises) |
| (d) "taking over" money itself | F1, A3 (personhood), B8 (money held by an agent) | G4 Skingsley (institutions); F4 Lupia (delegation works with verification); B8 (humans stayed in the loop) |

---

## H. Open items for S1b and for the fact-checker
- **UNSEEN or secondary:** IMF GFSR ch. 3 (B7); Gensler and Bailey primary (E3); Hayek page numbers (C5); Akerlof and Grossman-Stiglitz at the page (C6, C7); Keynes, Morris-Shin, Granovetter, Dennett, Lupia, Cover pages (digests); Harari claims 16-19 (A6); Economist attribution (A5); the SEC-CFTC report's $4.1 billion figure (B2); Scheurer's headline rates (B5, figures); the Truth Terminal figures (B8, conflicting between the two articles); agent-wallet items after Oct 2024.
- **S1b (Kunhao to supply):** *Nexus* hardcover (page numbers for A4), Searle 1995 or 2010 (F1), Haldane and May 2011 (systemic risk and food webs).
- **Audio check:** every quoted Harari line from A1 and A3.
- **Page images worth re-reading at print time:** `sources/pages/nexus-p-xxii-23.png`, `nexus-p-xxxii-33.png`, `fcic-pxxiv-025.png`, `fcic-p128-157.png`, `fcic-p132-161.png`, `fcic-p149-178.png`.
