---
id: grimmer-2022-textasdata/ch10-principles
work: grimmer-2022-textasdata
unit: Chapter 10. Principles of Discovery
pages: 174-187
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Principles of Discovery

## L0 — One line
Discovering a new way to organize data is judged by how useful the resulting concept is, not by how it was found, but ideally it should be tested on fresh data, and discovery still needs deep substantive knowledge.

## L1 — The gist (≤ 120 words)
Chapter 10 asks how researchers should treat discovery (finding new ways to organize text data) now that data are plentiful. It gives four principles: discovery needs substantive knowledge; no conceptualization (way of organizing data) is the true one; a concept is judged by its usefulness, not by the method that produced it; and, ideally, discovery data should be replaced by fresh data for testing. The VoteView/DW-NOMINATE case shows how one organization of legislators found inductively (from the data, not set in advance) reshaped a whole literature. The authors conclude that discovery is part of every project and should be discussed openly, so readers know which evidence is credible.

**Prerequisites:** the idea of a measurement or hypothesis test on data; the spatial model of voting (ideal points); a rough idea of overfitting.

## L2 — Key ideas
- Data-driven discovery on one set of documents, followed by measurement and testing on a different set, avoids the standard critiques of data mining (circularity, overfitting, meaninglessness) (p. 174).
- Principle 1: computational discovery complements theory. Choosing data, interpreting output and revising theory all need substantive knowledge (pp. 175–176).
- Principle 2: there is no ground-truth conceptualization. Organizations are more or less useful for a task, and "right/wrong" applies only after a concept is fixed (p. 177).
- Principle 3: judge the concept by its utility, not its origin. So discovery methods cannot be ranked by proofs or simulations, and researchers should try many methods (pp. 178–179).
- Principle 4: ideally discard the discovery data and use new or held-out data for testing. Failing to do so risks violating core causal inference assumptions (p. 180).
- The VoteView case: a statistically derived, low-dimensional organization of legislators became the default conceptualization of Congress and spread to other actors, fields and data types (pp. 181–183).
- A conceptualization makes some questions askable and others nonsensical, yet little quantitative work develops new ones (pp. 184–185).
- Discussing discovery openly helps method development, teaching, and clarity about where results are credible (pp. 186–187).

## L3 — Walkthrough

### Opening (p. 174)
- The authors say conventional research rules come from a time when data were sparse but thinking was cheap. Then one should theorize before looking at the data, to save information for testing theories (p. 174).
- Now data are plentiful. So we can discover on one set of documents and develop measures and evaluate claims on a different set (p. 174).
- This approach avoids the common critiques of data mining: that it is circular, overfits, or is meaningless (p. 174).
- **Origin-independence:** once we hold a concept, it is ours and how it was developed is irrelevant. What matters is that it gives an insightful view and that we use fresh data afterwards. So any technique that gives good insight may be used, without worrying about its underlying assumptions (p. 174).

### 10.1 Principle 1: Context relevance (pp. 175–176)
- Text-as-data models complement theory and substantive knowledge. Contextual knowledge amplifies our ability to make computational discoveries (p. 175).
- **Target of criticism (Anderson, 2008, "The End of Theory"):** optimistic futurists claim the data deluge makes the scientific method obsolete. The authors say such claims overstate machine learning and understate qualitative human analysis (p. 175).
- Three reasons: choosing interesting data needs substantive knowledge; interpreting output needs deep knowledge of the case; deciding what findings mean and how they revise our understanding needs an organizing theory and case knowledge (p. 175).
- Example: abductive analysis (identifying a surprising category, pattern or concept). Karell and Freedman (2019, Afghan radical groups; Chapter 13) show it requires knowing existing theoretical organizations of radical rhetoric. Nelson (2020, feminist organizations; Chapter 11) used her knowledge of the organizations' geographic structure to find distinctions existing frameworks cannot (p. 175).
- The methods are complements to traditional theory building. They serve the iterative process whose goal is theory development, with deep substantive knowledge a prerequisite for inference. They can support discovery and highlight tensions in earlier theories (pp. 175–176).

*Intuition note:* The computer proposes ways to organize documents. Interpreting the output and recognizing a surprising category need knowledge of the case and of existing theory.

### 10.2 Principle 2: No ground truth (p. 177)
- There is no ground-truth conceptualization. Only after a concept is fixed can we say it is right or wrong (p. 177).
- Texts can be organized by topic, tone or author. These are different views of the world, more or less useful for different questions (p. 177).
- Not all organizations are equally useful for all tasks. Examples: the book's index is alphabetical, which would be a poor order for presenting topics. The book's methods are organized by research task rather than by statistical foundations, which suits this book but might not suit another audience (p. 177).
- After the concept is fixed, methods can be more or less accurate at measuring it (Part IV). We can and should validate how accurately a method finds "criticism". Whether to use "criticism/praise" or "effusive/curt" depends entirely on the research question (p. 177).

*Intuition note:* Validation asks "does this tool find my category?" It cannot ask "is my category the true one?"

### 10.3 Principle 3: Judge the concept, not the method (pp. 178–179)
- Value comes from what the concept helps the researcher do (measure, test hypotheses, update theory), not from the method that generated it. So there is no "best" discovery method (p. 178).
- The only meaningful way to evaluate a conceptualization is by its usefulness for a particular application. Examples: understanding censors' goals, radical groups' rhetoric, or how advocacy groups shape the media landscape. No application-independent claim says topics are better than sentiment (p. 178).
- Consequence 1: the researcher may explore freely (p. 178).
- Consequence 2: evaluating discovery methods is very hard. There are no proofs that some methods discover better, and no simulations showing one does better on average. A method's producing insight once gives no guarantee it will do so later or for other teams (p. 178).
- So researchers should try many methods and many organizations. Methods with precise assumptions can help, but so can "going for a walk in the woods". Varying the properties of the organization is essential. In a real sense, model properties do not matter other than in their ability to produce useful organizations. Once a conceptualization exists it may be applied to any new dataset (p. 179).

*Intuition note:* A discovery method is like a source of ideas. Its pedigree does not matter, because the idea is ideally tested on fresh data afterwards.

### 10.4 Principle 4: Separate data is best (p. 180)
- Ideally, data used for discovery is discarded in favor of new or previously held-out data for measurement and inference (p. 180).
- External data ensures that categories are not artifacts of the discovery dataset and that labels mean what we claim (p. 180).
- This matters especially for causal inference. Without two distinct datasets we risk violating core causal inference assumptions (discussed later in the book) (p. 180).
- The authors admit much text-as-data research (including their own) has not separated the data. In certain projects data is highly limited, and the value of separation has not always been recognized. Such work can still be compelling through careful validation. Still, when possible, "it is difficult to understate the value" of separate data, especially when many techniques are tried (p. 180).

### 10.5 Conceptualizing the US Congress (pp. 181–185)
- **Aim:** show how a conceptualization from a statistical model led to new insights, theories and questions. The data, roll call votes, are high-dimensional, like the bag-of-words representation of Chapter 5 (p. 181).
- **Competing conceptualizations:** MacRae (1965) argues six to eight voting blocs underlie roll calls, depending on legislative content. Others stress ephemeral coalitions, such as the 1960s "conservative coalition" on civil rights. Another tradition places politicians on an ideological spectrum from "far-left liberal" to "far-right conservative" (p. 181).
- **VoteView (Poole and Rosenthal):** from the early 1980s they developed DW-NOMINATE (Dynamic Weighted Nominal Three-Step Estimation), which compresses voting data. Each legislator gets a two-dimensional score; the first dimension, often the only one used, is said to correspond to ideology (p. 181).
- **Link to spatial models:** actors have an "ideal point", the policy location they prefer to any other. DW-NOMINATE supposes legislators vote for proposals closer to their ideal point than the status quo, so its estimates can be read as ideal points (p. 182).
- **Figure 10.1** (first dimension by session of Congress, 87–117, by party): in the image, Democratic density lies mostly left of 0 and Republican density mostly right of 0, in every session shown (p. 183).
- **Reception:** at first it was seen as audacious. Skeptics doubted two dimensions could capture the conflict, and even those who accepted low dimensionality disagreed on why. Critics called it too simplistic, since it suppressed many features of conflict (p. 182).
- **Later influence:** after over 30 years it is the default conceptualization of members of Congress. It is used in nearly every quantitative paper on Congress, and has provoked theory about why voting is so low-dimensional. It inspired work on other legislatures (Snyder Jr., 1992). The same core techniques measure ideal points of candidates, donors, social media users and voters, and spread to computer science, which combines votes with bill text (p. 182).
- **Inductive yet useful for deduction:** the dimensions were not specified a priori, but DW-NOMINATE is used to assess theories of congressional organization, inter-branch bargaining and representation. This pushed scholars of other legislatures to build analogous measures from other data, including political speech (p. 183).
- **Other organizations suggest other questions:** leadership, committees and party caucuses. For example, Berry and Fowler (2016) ask whether Appropriations Committee members deliver more money to their districts. Fenno (1978) organized legislators by the issues they engaged in with constituents. Grimmer (2013b) places senators on a spectrum from broad national issues to claiming credit for money delivered (pork versus policy) (pp. 183–184).
- **Main point:** inferences depend on the conceptualization. It makes some hypotheses possible and others impossible or nonsensical, so all conclusions depend on how we first organize the world (p. 184).
- **Problem:** very little quantitative work develops new conceptualizations. Use of DW-NOMINATE has far outpaced attempts to find new organizations of congressional conflict. Reasons given: lack of methods, time cost, anxiety about new schemas. Shared conceptualizations are valuable, but focusing on only one will limit questions and inferences (pp. 184–185).

*Intuition note:* A map decides what you can see. VoteView's map was found by data analysis, yet it became the base for theory-driven work, which fits the point that a concept's origin does not decide its value (our reading, not the authors' wording).

### 10.6 Conclusion (pp. 186–187)
- The authors say we do not talk about discovery enough, even though it is an implicit part of every research project. **Duneier (1999, p. 341):** he did not know his research question at the start. Quantitative researchers also often form designs after seeing data. The authors add that discovery is usually invisible in published work (p. 186).
- Three benefits of discussing discovery:
  1. We can develop methods designed for it. Qualitative design literature has done this (Strauss, 1952; Tavory and Timmermans, 2014), and computational scholars import it (Baumer et al., 2017; Nelson, 2020; Karell and Freedman, 2019). This needs frank discussion of how discovery works, its barriers, and how to recognize a good discovery (p. 186).
  2. It gives students a more accurate picture of science. Concepts are too often shown as springing "unbidden" from brilliant minds, which can discourage new entrants (p. 187).
  3. It clarifies the nature of evidence. Readers should know whether a discovery was validated on external data or hypothesized from the same evidence used to confirm it. Chapter 21 returns to using discovery methods for measurement, which requires separating the two tasks (p. 187).
- Next chapter: discriminating words (p. 187).

## Toy example (ours, not from the text)
A researcher reads 6 senators' press releases (discovery set) and notices the word "grant" in 3 of them. She defines a category "credit claiming" = releases containing "grant".
- Discovery set share: 3/6 = 0.50. This number cannot validly test her hypothesis, because the category was chosen after seeing these documents.
- Fresh set of 8 releases: "grant" appears in 2, so the share is 2/8 = 0.25.
- Under Principles 3 and 4, how she came up with "grant" is irrelevant. The reportable estimate is the 0.25 from fresh data. Whether "credit claiming" is a useful concept is judged by what it helps explain.

## Concepts
- [[discovery-vs-measurement-separation]] (new) — find a concept on one dataset; measure and test it on new or held-out data (pp. 174, 180)
- [[origin-independence-of-concepts]] (new) — a concept's value does not depend on how it was developed (pp. 174, 178)
- [[conceptualization]] (new) — an organization of data (by topic, tone, author, etc.) that is more or less useful, never "true" (p. 177)
- [[abductive-analysis]] (new) — identifying a surprising category, pattern or concept, often needing theory knowledge (p. 175)
- [[ideal-point]] (new) — the policy-space location a legislator prefers to all others (p. 182)
- [[spatial-model-of-voting]] — actors and policies sit in a policy space, with each politician at an ideal point; DW-NOMINATE adds the supposition that legislators vote for proposals closer to their ideal point than the status quo (p. 182)
- [[text-as-data-validation]] — after a concept is fixed, one can check how accurately a method measures it (p. 177)

## Canonical instances
- [[dw-nominate-voteview]] — inductive low-dimensional scoring of legislators that became the default Congress conceptualization (pp. 181–183)
- [[karell-freedman-radical-rhetoric]] — abductive discovery needing theory of radical rhetoric (p. 175)
- [[nelson-computational-grounded-theory]] — computational distinctions among feminist organizations' strategies (p. 175)
- [[pork-policy-spectrum-grimmer]] — senators ordered from national-issue rhetoric to credit claiming (p. 184)

## Bridges (candidates)
- [structural-analogy] Discovery data vs test data ↔ machine learning: training vs held-out data — both keep fresh data for evaluating what was fit.
- [same-math] DW-NOMINATE ideal points ↔ spatial model of voting: ideal points in policy space (p. 182) — the chapter states this link directly.
- [metaphor] "Going for a walk in the woods" as discovery method ↔ the origin-independence of ideas.

## Questions this raises
- How can a research team show readers which evidence came from discovery and which from testing, when data are small?
- If discovery methods cannot be ranked by proofs or simulation, what practical signs show a discovery is worth pursuing?
- How much does one dominant conceptualization (like DW-NOMINATE) narrow the questions a field asks?
- What does a held-out split cost when data are very limited?

## Reading notes
- Printed page = pdf page (174–187). No offset.
- The text layer was clean. Figure 10.1 was checked in the image. Its description above is my reading of the image, not the authors' text.
- The chapter has no equations and no exercises. Several citations (e.g., Powell, N.d.) are printed as given.
