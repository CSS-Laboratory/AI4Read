---
id: brin-1998-anatomy/main
work: brin-1998-anatomy
unit: paper
pages: pdf 1–20
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# The Anatomy of a Large-Scale Hypertextual Web Search Engine (Brin & Page, 1998)

## L0 — One line
Google ranks web pages by combining a link-based importance score (PageRank, said to be the principal eigenvector of the normalized link matrix) with text, anchor and proximity evidence, inside an architecture built to scale with the Web.

## L1 — The gist (≤ 120 words)
The authors ask how to build a practical search engine that gives high-precision results on the huge, uncontrolled Web. Their answer is Google. It uses the link graph to compute PageRank, a citation-importance score. It indexes anchor text (the text of links) under the page the link points to. It uses word proximity and font information. Rank is built from dot products of hit-count weights with type weights, then combined with PageRank. Compact data structures and a distributed crawl/index/sort pipeline handle 24 million pages. The paper is an early public description of a full search engine. Linear algebra appears in dot products of weight vectors and in a stated (not derived) eigenvector link.

**Prerequisites:** vectors and the dot product; sums over neighbours in a graph; the idea of an eigenvector; basic ideas of files, indexes and sorting.

## L2 — Key ideas (5–10 bullets)
- Index completeness is not the only factor in search quality. Users read only the first few tens of results, so the authors want very high precision (relevant documents among the top results), even at the cost of recall (the total number of relevant documents returned) (pdf 2–3).
- PageRank gives each page a score from its in-links (links pointing to it). Each linking page's score is divided by its out-degree (its number of outgoing links), and a damping factor d is used. The authors say it corresponds to the principal eigenvector of the normalized link matrix of the web; they do not explain this further (pdf 4).
- The "random surfer" model (an imagined user who keeps clicking links and sometimes restarts at a random page) gives an intuitive reading: a page's PageRank is the probability that the surfer visits it (pdf 4).
- Anchor text (the text of a link) is also attached to the page the link points to. This makes it possible to return pages that were not crawled, and non-text objects (pdf 5).
- A document's IR (information retrieval) score is a dot product (multiply matching entries, then add) of a vector of count-weights (numbers derived from how many hits of each type the document has; a hit is one occurrence of a word) with a vector of type (or type–proximity) weights. It is then combined with PageRank (pdf 12).
- The architecture is designed to avoid disk seeks (about 10 ms each) whenever possible. It uses a compressed repository, barrels (partly sorted buckets of word data), a forward index (document → words), an inverted index (word → documents) and compact 2-byte hits (pdf 7–10).
- Reported results: 24 million pages fetched, 147.8 GB raw, 108.7 GB of data stored in total, most queries answered in 1–10 s. Quality evidence is subjective (pdf 13–15).
- Appendix A says the authors expect advertising-funded engines to be inherently biased toward advertisers. They believe this makes a competitive, transparent, academic engine crucial (pdf 18–19).

## L3 — Walkthrough

### Abstract and 1 Introduction
- Google is a prototype that uses hypertext structure. It had a full-text and link database of at least 24 million pages (pdf 1).
- Problems of the 1997 Web: rapid growth, inexperienced users, and keyword engines returning many low-quality matches. Human-maintained lists cover popular topics effectively but are subjective, expensive to build and maintain, slow to improve, and cannot cover all esoteric topics. Some advertisers also try to mislead engines (pdf 1).
- The name comes from "googol", 10^100 (pdf 1).

### 1.1–1.2 Scaling
- The World Wide Web Worm indexed 110,000 pages in 1994 and handled about 1,500 queries/day. By November 1997 the top engines claimed 2–100 million documents. AltaVista claimed about 20 million queries/day (pdf 2).
- They say a comprehensive index of over a billion documents is foreseeable by 2000, and that top engines will likely handle hundreds of millions of queries per day by then (pdf 2).
- Hardware improves, but disk seek time and operating-system robustness are exceptions (pdf 2).

### 1.3 Design goals
- **Quality.** Completeness of the index is not the only factor. "Junk results" wash out useful ones. As of November 1997 only one of the top four commercial engines returned its own search page in the top ten results for its own name (pdf 2).
  - *1994 view* (reported): some people believed a complete index would make anything easy to find; Best of the Web 1994 said the best navigation service should make it easy to find almost anything "once all the data is entered". The authors say the 1997 Web is different (pdf 2).
  - Users look only at the first few tens of results, so the authors want high **precision** (relevant documents among the top results). They say they want "relevant" to mean only the very best documents. They accept lower **recall** (total relevant documents returned) for it (pdf 3).
- **Academic research.** The share of web servers on .com rose from 1.5% (1993) to over 60% (1997). Commercial engines publish little, so the technology stays "largely a black art" and advertising-oriented (pdf 3).
- Google stores all crawled documents in compressed form so other researchers can process large chunks of the Web. The authors want usable systems and a "Spacelab-like" experimental environment (pdf 3).

### 2 System features
Two features help produce high-precision results: PageRank, and the use of link text (pdf 3).

#### 2.1 PageRank
- The authors built maps with up to 518 million hyperlinks. PageRank is an "objective measure" of citation importance that corresponds well with people's subjective idea of importance (pdf 3–4).
- For most popular subjects, a simple text-matching search restricted to page titles performs admirably when PageRank prioritizes the results (pdf 4).

#### 2.1.1 Definition
Counting citations (backlinks) approximates importance. PageRank does not count all links equally, and it normalizes by the number of links on the linking page (pdf 4).

Let page $A$ have pages $T_1,\dots,T_n$ pointing to it. Let $C(T_i)$ be the number of links going out of $T_i$. Let $d\in(0,1)$ be the damping factor, usually $0.85$. Then

$$PR(A) = (1-d) + d\left(\frac{PR(T_1)}{C(T_1)} + \dots + \frac{PR(T_n)}{C(T_n)}\right). \tag{PR}$$

(Equation unnumbered in the source; tag ours.) The authors state that the PageRanks form a probability distribution over pages, so they sum to one. They say PR can be computed by "a simple iterative algorithm" and "corresponds to the principal eigenvector of the normalized link matrix of the web". PageRank for 26 million pages takes a few hours on a medium workstation. Other details are beyond the paper's scope (pdf 4).

*Intuition note:* each page splits its own score equally among the pages it links to. A page's score is the base amount $(1-d)$ plus $d$ times the shares it receives from its in-linkers. The authors say this can be computed by a simple iterative algorithm; they do not discuss convergence here.

#### 2.1.2 Intuitive justification
- **Random surfer.** The surfer starts at a random page, keeps clicking links, never presses "back", and eventually gets bored and restarts at a random page. The probability of visiting a page is its PageRank. The authors describe d as the probability of getting bored at each page (pdf 4). (See Reading notes: this conflicts with the formula's use of d.)
- Adding the damping term to only one page or a group of pages allows personalization. The authors say this can make it "nearly impossible" to mislead the system on purpose (pdf 4).
- A page can have a high PageRank if many pages point to it, or if some pages that point to it have a high PageRank (e.g. even one citation from the Yahoo! homepage is generally a good sign). PageRank handles both cases by "recursively propagating weights" through the link structure (pdf 4).

#### 2.2 Anchor text
Anchor text is associated with the page it is on, and also with the page it points to. Reasons: anchors often describe a page better than the page itself, and they exist for non-text items (images, programs, databases). So pages that were not actually crawled can be returned. They are never checked for validity, so a page that never existed could be returned; the authors say it is possible to sort the results so that this rarely happens. The crawl of 24 million pages had over 259 million indexed anchors (pdf 5). The WWWW already propagated anchor text; Google uses it mostly because it can help give better-quality results, and it is technically hard because of the data volume (pdf 5).

#### 2.3 Other features
Hits carry location, so proximity is used. Font size is tracked, and larger or bolder words weigh more. Raw HTML is kept in the repository (pdf 5).

### 3 Related work
- Few documents describe recent search engines. Quote from Mauldin (Lycos): services "closely guard the details" (pdf 5).
- **3.1 Information retrieval.** IR research mostly uses small, controlled collections. The TREC "Very Large Corpus" benchmark is 20 GB, against 147 GB for the authors' crawl (pdf 5–6).
  - The standard vector space model returns the document closest to the query, with both seen as word-occurrence vectors. On the web this often returns very short documents that are the query plus a few words (e.g. a major search engine returned a page containing only "Bill Clinton Sucks" and a picture for the query "Bill Clinton") (pdf 6).
  - **Opponents' view:** users should type more specific queries. **Authors:** "We disagree vehemently with this position" (pdf 6).
- **3.2 Web vs controlled collections.** Web documents vary internally (language, format, machine-generated) and in external meta-information (reputation, update frequency, usage, citations). Usage varies by orders of magnitude. Anyone can publish anything, so manipulation of engines for profit is a serious problem. Metadata efforts largely failed because unseen page text is abused (pdf 6).

### 4 System anatomy
#### 4.1 Architecture (Figure 1)
- Distributed crawlers fetch URLs from a URLserver. The storeserver compresses pages into the repository. Each page gets a docID (pdf 7).
- The indexer parses documents into **hits** (word, position, approximate font size, capitalization). It distributes hits into barrels, giving a partially sorted forward index. It also writes an anchors file (pdf 7).
- The URLresolver turns relative URLs into absolute URLs and then docIDs. It puts anchor text into the forward index under the target docID, and writes a links database of docID pairs. The links database is used to compute PageRank (pdf 7).
- The sorter re-sorts barrels by wordID to make the inverted index, in place. The searcher uses the lexicon, the inverted index and the PageRanks (pdf 7).
- A disk seek takes about 10 ms, so Google is designed to avoid disk seeks whenever possible (pdf 7).

#### 4.2 Data structures
- **BigFiles:** virtual files across file systems, addressed by 64-bit integers (pdf 8).
- **Repository:** full HTML compressed with zlib (about 3:1). zlib was chosen for speed over bzip (about 4:1). Other structures can be rebuilt from it plus a crawler-error file (pdf 8).
- **Document index:** fixed-width ISAM index ordered by docID, with a one-seek record fetch. A checksum-sorted URL→docID file is used, and batch merge is crucial: one seek per link would take over a month for 322 million links (pdf 8).
- **Lexicon:** 14 million words, fits in 256 MB of memory (word list plus hash table) (pdf 8–9).
- **Hit lists:** most of the index space, so each hit is 2 bytes (pdf 9).
  - Plain hit: 1 capitalization bit, 3 font bits, 12 position bits (positions above 4095 are labelled 4096).
  - Fancy hit (URL, title, anchor, meta tag): font field = 7 (binary 111) as flag, 4 bits for hit type, 8 bits for position. Anchor hits split these 8 bits into 4 for position and 4 for a docID hash.
  - Font size is relative to the rest of the document, so otherwise identical documents are not ranked differently.
  - Hit-list length is packed with the wordID (forward) or docID (inverted), with an escape code for long lists.
- **Forward index:** 64 barrels, each covering a range of wordIDs. wordIDs are stored relative to the barrel minimum, so 24 bits suffice (pdf 9–10).
- **Inverted index:** the lexicon points into barrels of doclists. Sorting docIDs by ID allows fast merging. Sorting by rank makes one-word queries easy but merging hard, and a ranking change forces a rebuild. Compromise: two sets of barrels, one for title/anchor hits and one for all hits. The first set is searched first (pdf 10).

#### 4.3 Crawling
- A URLserver feeds about 3 crawlers. Each keeps about 300 connections. Peak is over 100 pages/s (about 600K/s). DNS lookup is a major stress, so each crawler keeps its own DNS cache (pdf 10).
- Crawling is the most fragile part and involves social issues: emails from site owners, the robots exclusion protocol, and bugs that only appear at scale (e.g. garbage messages in an online game). The authors say a crawler is "virtually impossible" to test without running on a large part of the Internet (pdf 10–11).

#### 4.4 Indexing
- **Parsing:** a flex-generated lexical analyzer with its own stack, robust to many HTML errors (pdf 11).
- **Barrels:** words become wordIDs via the in-memory lexicon. For parallel indexers, a base lexicon of 14 million words is fixed. Extra words go to a log processed by one final indexer (pdf 11).
- **Sorting:** one barrel at a time, in parallel across machines. Barrels are subdivided into memory-sized baskets (pdf 11).

#### 4.5 Searching
- Query steps (Figure 4, query evaluation): parse; convert words to wordIDs; seek in the short barrels; scan doclists for documents matching all terms; compute the rank of each match; if in the short barrels and at the end of any doclist, seek in the full barrels and keep scanning, otherwise keep scanning; finally sort the matched documents by rank and return the top $k$ (pdf 12).
- Once 40,000 matching documents are found, the searcher stops. Results may be sub-optimal (pdf 12).

**4.5.1 Ranking**
- The ranking is designed so no single factor has too much influence (pdf 12).
- **Single-word query.** Each hit has a type (title, anchor, URL, large plain, small plain, …) with a type-weight. The type-weights form a vector indexed by type. Counts per type are converted to count-weights, which rise linearly at first and then taper off. The IR score is the dot product of the count-weight vector with the type-weight vector. It is then combined with PageRank (pdf 12).
- **Multi-word query.** Nearby hits are matched, and a proximity is computed in one of 10 bins from "phrase match" to "not even close". Counts are kept per (type, proximity) pair, each with a type-prox-weight. The IR score is again a dot product of count-weights with weights (pdf 12). The shapes are one weight per type, or per (type, bin) pair, i.e. $10\times$ the number of types if flattened (added step).

*Intuition note:* ranking is a weighted sum of evidence. Count-weights taper off, so counts above a certain level do not help. The weights are hard to choose ("something of a black art"), so the authors use user feedback to see how a change affects earlier searches.

**4.5.2 Feedback.** The weights are "something of a black art". A trusted user may rate all results of a query. Ratings are saved, so the effect of a ranking change on earlier queries can be checked. The authors call this far from perfect (pdf 12–13).

### 5 Results and performance
- The authors claim only subjectively that Google beats major commercial engines for most searches. A full user study is out of scope (pdf 13).
- In the "bill clinton" example (Figure 4, sample results), results are clustered by server. A page with no title was ranked via anchor text because it was not crawled, and an email address was also found through anchor text. The results are reasonably high-quality pages and, at last check, none were broken links; the authors say this is largely because they all have high PageRank. No results about another Bill or another Clinton appear, which they attribute to the weight on proximity (pdf 13).
- **Storage (Table 1):** fetched pages 147.8 GB; compressed repository 53.5 GB; short inverted index 4.1 GB; full inverted index 37.2 GB; lexicon 293 MB; document index with variable-width data 9.7 GB; links database 3.9 GB. Total without repository 55.2 GB; with repository 108.7 GB (pdf 14). Web statistics: 24 million pages fetched, 76.5 million URLs seen, 1.7 million email addresses, 1.6 million 404s (pdf 14).
- Most queries can be answered with the short inverted index alone. With better compression of the document index, an engine "may fit onto a 7GB drive" (pdf 14).
- **Performance:** about 9 days to download 26 million pages. The last 11 million took 63 hours, about 48.5 pages/s. The indexer runs at about 54 pages/s. Sorting with four machines takes about 24 hours (pdf 14).
- **Search time:** most queries 1–10 s, dominated by disk IO over NFS. No caching or subindices. Table 2 shows initial vs repeated query times, e.g. "al gore" 2.13 s total at first and 0.06 s repeated. The target is several hundred queries per second (pdf 14–15).

### 6 Conclusions
- **Future work:** query caching, subindices and smart disk allocation. Update policy: which pages to recrawl. Boolean operators, negation, stemming. Relevance feedback, clustering, user context, summarization. PageRank personalization by increasing the weight of a user's home page or bookmarks ("simple experiments indicate") (pdf 15).
- **Quality:** the authors say they "subjectively" find better results. They credit PageRank (page quality), link text (relevance and some quality) and proximity (pdf 15).
- **Scalability:** the bottlenecks seen were CPU, memory, disk and network. They indexed 24 million pages in under a week and expect 100 million in under a month (pdf 16).
- **Research tool:** the stored data has already produced papers. Abiteboul 97 is cited for limits on answering Web queries without local Web data (pdf 16).

### Appendix A: advertising and mixed motives
- The authors expect advertising-funded search engines to be inherently biased toward advertisers and away from consumers' needs (pdf 18). The PageRank-ranked top result for "cellular phone" was a study on the risks of phone use while driving, which would be hard to justify to advertisers (pdf 18).
- OpenText was reported (Marchiori 97) to sell top positions, which the authors call more insidious than ads. Subtler bias may be hard to detect, and ad income can create an incentive to give poor results, e.g. a major engine not returning an airline's own page when the airline had paid for an ad (pdf 18–19).
- The authors argue a competitive, transparent, academic engine is crucial (pdf 19).

### Appendix B: scalability
- Target is 100 million pages. Crawlers, indexers and sorters are parallel and roughly linear in time. Beyond about 100 million pages, operating-system limits would greatly raise complexity (pdf 19).
- Illustration: 250 million people × 10k/day ≈ 850 terabytes for a year. Assuming a terabyte can be indexed at reasonable cost now, that indexing is linear or nearly linear in complexity, and that Moore's law (doubling every 18 months) keeps holding, 10 more doublings (15 years) would make this affordable for a small company. The authors note hardware experts are somewhat concerned Moore's law may not hold for 15 years (pdf 19). Distributed systems (Gloss, Harvest) may be technically elegant but have high administration costs (pdf 20).

## Toy example (ours, not from the text)
Three pages: A→B, A→C, B→C, C→A. So $C(A)=2$, $C(B)=1$, $C(C)=1$, with $d=0.85$. Equations from (PR):
- $PR(A)=0.15+0.85\,PR(C)$
- $PR(B)=0.15+0.85\,(PR(A)/2)$
- $PR(C)=0.15+0.85\,(PR(A)/2+PR(B))$

Start with all values 1 and update all pages at once from the old values.
- Iteration 1: $A=0.15+0.85\cdot1=1.0$; $B=0.15+0.85\cdot0.5=0.575$; $C=0.15+0.85\,(0.5+1)=1.425$. Sum = 3.0.
- Iteration 2: $A=0.15+0.85\cdot1.425=1.36125$; $B=0.15+0.85\cdot0.5=0.575$; $C=0.15+0.85\,(0.5+0.575)=1.06375$. Sum = 3.0.

C has two in-links, including one from A, and is highest after iteration 1; after iteration 2 A is highest. The scores have not settled yet, and the paper does not discuss convergence. The sum stays at 3 (the number of pages) under this formula. Dividing by 3 gives probabilities (0.454, 0.192, 0.355), which sum to 1. That division is our normalization, not stated in the paper.

## Concepts
- [[pagerank]] (new) — a page's score: base amount plus damped sum of in-linkers' scores divided by their out-degrees (pdf 4)
- [[damping-factor]] (new) — parameter $d\in(0,1)$, usually 0.85; also described as the "bored" probability (pdf 4)
- [[random-surfer]] (new) — a model user who follows links and restarts randomly; visit probability is PageRank (pdf 4)
- [[eigenvector / eigenvalue]] — the paper only states that PageRank "corresponds to the principal eigenvector of the normalized link matrix" and does not derive this (pdf 4)
- [[dot (inner) product]] — used to combine count-weights with type or type–proximity weights into an IR score (pdf 12)
- [[vector]] — type-weights and count-weights are vectors indexed by hit type; documents and queries in the vector space model are word-occurrence vectors (pdf 6, 12)
- [[vector-space-model]] (new) — IR model returning the document closest to the query vector. The authors say it often returns very short documents on the web (pdf 6)
- [[anchor-text]] (new) — link text, indexed under the page the link points to (pdf 5)
- [[inverted-index]] (new) — word → list of documents (doclist) with hit lists, built by sorting the forward index by wordID (pdf 10)
- [[precision-recall]] (new) — precision: relevant results among the top returned. Recall: total relevant documents returned. The authors favour precision (pdf 3)

## Canonical instances
- [[pagerank-formula]] — recursive link-weight definition with $d=0.85$ (pdf 4)
- [[random-surfer-model]] — behavioural justification of PageRank (pdf 4)
- [[bill-clinton-query]] — failure of the vector space model on the web, and Google's results via anchor text and proximity (pdf 6, 13)
- [[cellular-phone-query]] — PageRank returns a result an advertiser would not want (pdf 18)

## Bridges (candidates)
- [structural-analogy] random surfer with restarts ↔ linear-algebra: Markov chain, steady-state eigenvector — the paper ties PageRank to a principal eigenvector but gives no derivation.
- [structural-analogy] PageRank ↔ network science: eigenvector centrality — importance depends on importance of in-neighbours; the paper adds a constant term and a division by out-degree.
- [structural-analogy] inverted index ↔ sparse term–document matrix, transposed — sorting by wordID instead of docID acts like transposing.
- [same-math] IR score = count-weights · type-weights ↔ linear models: weighted sum of features — literally a dot product (pdf 12).

## Questions this raises
- How exactly does the iterative PageRank update converge, and why does it reach the principal eigenvector?
- What happens to pages with no outgoing links, which the (PR) formula does not address?
- How should the hand-set type-weights be learned from the user feedback the authors mention?
- How well does the claimed resistance to manipulation (adding $d$ to a single page) hold up?

## Reading notes
- The metadata says printed pages are unknown, so all references use (pdf N). The page labels show printed numbers for pdf 4–20, apparently counting from the first body page. Some are inconsistent: pdf 18 and 19 are labelled 8 and 9, but pdf 17 is labelled 14. Pages 1–3 have no label.
- The source states there are two versions (full and shorter printed).
- Figure 1 (architecture) is not visible in the images given. Only the Repository, Hit and Table 1 images were checked. Figure numbering is duplicated: "Figure 4" labels both the query-evaluation steps (pdf 12) and the sample results (pdf 13).
- The text says 322 million links in the 4.2.3 batch-merge sentence (pdf 8), but 518 million links in the maps (pdf 3). It gives 26 million pages in some places and 24 million in others (pdf 14). The source does not reconcile these. It also says crawling took "roughly 9 days" for 26 million pages (pdf 14) but later says 24 million pages in "less than one week" (pdf 16).
- Formula inconsistencies. (1) The paper says PageRanks sum to one. With $(1-d)$ added for each of $N$ pages, and ignoring pages with no outgoing links, the sum would be $N$ (added step: $\sum_A PR(A)=N(1-d)+d\sum PR$, so $\sum PR=N$). (added step: probabilities summing to one would need $(1-d)/N$ in place of $(1-d)$.) (2) The surfer text calls $d$ the bored probability, but in the formula the constant (random-jump) term is $(1-d)$ and $d$ multiplies the sum over in-linkers.
- The sentence "Second, Google utilizes link to improve search results" (pdf 3) appears to be missing the word "text". The Bagdikian citation reads "83" in Appendix A and "97" in the references.
