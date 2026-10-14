---
id: bonacich-1987-power/main
work: bonacich-1987-power
unit: paper
pages: 1170–1182
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Power and Centrality: A Family of Measures

## L0 — One line
Bonacich proposes the centrality family c(α,β) = α(I−βR)⁻¹R1, in which the sign of β decides whether being tied to high-status others raises or lowers a unit's status, so that it can cover both conventional centrality and Cook et al.'s exceptional bargaining results.

## L1 — The gist (≤ 120 words)
Cook et al. (1983) found that the most central positions in some exchange networks did not get the best bargaining profits. This seems to contradict network research that treats centrality as power. Bonacich offers c(α,β): the sign of β says whether ties to high-status others help (β>0) or hurt (β<0); its size says how far indirect ties count. For moderately positive β it ranks positions conventionally. For negative β its rankings fit Cook et al.'s profits in networks 1c and 1e. In 1f this holds only for small β, and in 1d only after an ad hoc change. He concludes the measure accentuates an ambiguity already present in the concept of centrality.

**Prerequisites:** matrix inverse; eigenvalues (largest eigenvalue); geometric series and its convergence; adjacency matrix and walks.

## L2 — Key ideas (5–10 bullets)
- Cook et al. found that the most central positions were not the most successful bargainers. The author says this "seems to contradict" network research that equates centrality with power (p. 1170).
- c(α,β) = α(I−βR)⁻¹R1 generalises the eigenvector measure. β sets the sign and degree of dependence on others' scores; α only rescales (pp. 1172–1173).
- For |β| < 1/(largest eigenvalue of R), c is a weighted count of walks of every length; a walk of length k+1 gets weight βᵏ (p. 1173). For β>0, read as a transmission probability and with α=1, c(1,β) is an expected number of communications or influences (p. 1174).
- The size of β acts as a "radius": β=0 gives degree (number of contacts), and larger |β| gives more weight to the whole structure (pp. 1171, 1174).
- For β<0, odd-length walks add and even-length walks subtract. Being tied to the powerless then raises centrality, which matches bargaining where partners with few options are an advantage (pp. 1171, 1176).
- In Cook et al.'s networks, conventional measures give D>E>F. This is also the order of c(α,β) for moderately positive β (p. 1177, fn. 9). Negative β makes E exceed D in 1c and 1e (pp. 1178–1179). In 1f this holds for β ≤ .2 (p. 1179).
- Network 1d cannot separate the β's: R²1 ∝ R1 makes c ∝ degree. The author makes R asymmetric (F feeds E, not the reverse), an ad hoc fix (pp. 1178–1179).
- The measure is limited to network-derived importance and may mislead unless members are equal on other relevant factors (pp. 1171–1172).

## L3 — Walkthrough

### Introduction (pp. 1170–1172)
- **Problem.** Cook et al. (1983) found, in experiments and simulations, that the most central positions were not the most successful bargainers (p. 1170). The author says this "seems to contradict" network research, especially on interlocking directorates, that assumes centrality is equivalent to power. The author adds that a social-psychological literature on experimentally restricted communication networks shows that leadership typically devolves on the individual in the most central position (p. 1170).
- **Proposal.** A family c(α,β). β reflects how far a unit's status depends on the statuses of those it is connected to (p. 1170).
  - β>0: status rises with the status of contacts. This suits communication networks and power hierarchies, where one's power depends on the power of those one has power over (pp. 1170–1171).
  - β<0 (the "major innovation"): in bargaining, being connected to those with few options is advantageous, and powerful partners with many options reduce one's power (p. 1171). Footnote 3 notes that Caplow's and Gamson's coalition theories also assume this, because powerful actors tend to be avoided as partners (p. 1171).
- The sign of β matches Cook et al.'s distinction, slightly modified to apply to whole systems (p. 1171):
  - Positive system: exchange in one relation is contingent on exchange in others (communication).
  - Negative system: exchange in one relation precludes exchange in others (e.g. exchanging a commodity).
- **Size of β.** If β=0, c_i is proportional to degree (number of contacts), whatever their centralities. A larger |β| takes indirect ties more into account, so c becomes more global (p. 1171).
- Footnote 2: for the four networks analysed, nearness and betweenness orderings equal those of c(α,β) for moderately positive β. At β=0, c correlates perfectly with degree (pp. 1170–1171).
- **Limitation.** c measures only network-derived importance. It ignores ties outside the system, quality of information, rights and duties, and the value of goods. It may mislead unless members are equal on these factors (pp. 1171–1172).

### The measure (pp. 1172–1173)
- Earlier measure e (Bonacich 1972a,b), the standard in interlocking-directorate research. R is a relations matrix, usually but not necessarily symmetric, with zero diagonal (p. 1172):
$$\lambda e_i=\sum_j R_{ij}e_j \tag{1}$$
$$\lambda e = Re \tag{2}$$
  So e is an eigenvector of R, and the largest eigenvalue is usually preferred (p. 1172). Footnote 4: all eigenvectors solve (1)–(2). If R is symmetric, each is a factor of R, and its eigenvalue measures how accurately it reproduces R (p. 1172).
- New measure (p. 1173):
$$c_i(\alpha,\beta)=\sum_j(\alpha+\beta c_j)R_{ij} \tag{3}$$
$$c(\alpha,\beta)=\alpha(I-\beta R)^{-1}R\mathbf 1 \tag{4}$$
  Shapes: R is n×n, **1** and c are n×1.
- α changes only the length of c. It is chosen so that $\sum_i c_i(\alpha,\beta)^2=n$. Then $c_i=1$ means, approximately, that position i is not unusually central or peripheral (p. 1173).
- Footnote 6: c(α,β) approaches e as β approaches 1/(largest eigenvalue of R) (p. 1173).
- Footnote 5: the β>0 versus β<0 distinction is not Knoke and Burt's centrality versus prestige distinction. c(α,β) suits symmetric and asymmetric relations. With asymmetric relations, as in Fig. 1, c with β>0 measures prestige, and with symmetric relations it measures centrality (pp. 1172–1173).

### Mathematical interpretations (pp. 1173–1176)
- If |β| is less than the reciprocal of the largest eigenvalue of R, (4) is an infinite sum (p. 1173):
$$c(\alpha,\beta)=\alpha\sum_{k=0}^{\infty}\beta^kR^{k+1}\mathbf 1=\alpha(R\mathbf 1+\beta R^2\mathbf 1+\beta^2R^3\mathbf 1+\dots) \tag{5}$$
  So c_i counts direct and indirect paths from i, weighted by β^(length−1). A path may revisit a point (p. 1173, fn. 7). This is a closeness measure in Freeman's (1979) sense (p. 1174).
- Footnote 7 relates c to Katz's status t = Σ_{i≥1} βⁱRⁱ**1**. The source prints t = β⁻¹c(1,β) (see Reading notes). Footnote 7 says t and c are perfectly correlated for β>0 and perfectly negatively correlated for β<0. For Katz, β was only an "attenuation factor" that made the sum converge (p. 1174, fn. 7).
- **β>0, probabilities.** Each individual communicates with all contacts; β is the probability that a received message is passed on to any contact. R**1** counts direct communications, βR²**1** the expected number passed on, and β^(k−1)Rᵏ**1** the expected number at the kth remove (p. 1174):
$$\sum_{k=1}^{\infty}\beta^{k-1}R^k\mathbf 1=\sum_{k=0}^{\infty}\beta^kR^{k+1}\mathbf 1=c(1,\beta) \tag{6}$$
  In an asymmetric power structure, β is the probability that a command is transmitted to subordinates (p. 1174).
- **β as radius.** The expected length of a path is (1−β)⁻¹, which can be read as a radius of concern. Small β weights local structure heavily. Large β takes more account of the whole structure (p. 1174). A low β suits mostly local communication. In power hierarchies β should depend on how transitive power relations are: near zero if power is only dyadic, larger in a formal hierarchy where orders are likely to be passed on (pp. 1174–1175).
- **Example (Fig. 1, p. 1175).** A has one subordinate, B; B has two, C and D. Taylor (1969) objected that Katz's index "would probably attribute higher status to the head of the secretarial pool than to the president". The author replies that this is true only when status is measured by number of subordinates (β=0). Table 1 (p. 1176; C and D are .00 throughout):

| β | A | B |
|---|---|---|
| 0 | .89 | 1.79 |
| .2 | 1.15 | 1.64 |
| .4 | 1.34 | 1.49 |
| .6 | 1.48 | 1.35 |
| .8 | 1.59 | 1.22 |

  B leads for small β. The text says A is more central at β=.50 and increases its lead as β grows (p. 1175).
- **β<0.** The probability interpretations are not valid. From (4) (p. 1175):
$$c(\alpha,\beta)=\alpha R\mathbf 1+\beta Rc(\alpha,\beta) \tag{7a}$$
$$\phantom{c(\alpha,\beta)}=\alpha R\mathbf 1+\alpha\beta R^2\mathbf 1+\beta^2R^2c(\alpha,\beta) \tag{7b}$$
  (Added step: (7a) is (3) in matrix form. (7b) substitutes (7a) into its own right side.) In (5) even powers get negative weight and odd powers positive. Many direct ties raise centrality, but many length-two paths lower it. By (7a), c is reduced when one's connections are central. By (7b), it is increased by the centrality of those at distance two (p. 1176).

*Intuition note.* With β>0, ties to well-placed others help, and longer walks count with shrinking weight. With β<0, a well-placed partner hurts, and that partner's own well-placed partners help you again. That is why being linked to powerless partners can pay in bargaining.

### The Cook et al. data: a negative β (pp. 1176–1181)
- Cook et al. praise centrality for covering the whole network, and call for "a more general conception of centrality". The author says this is precisely what the article tries to supply (p. 1176). Networks 1a and 1b are omitted because they are uninteresting (p. 1176, fn. 8).
- **Setup (Fig. 2).** Each position can make one negotiation per trial. Solid lines offer 24 points to divide and broken lines 8. Only solid lines are used for centrality: r_ij=1 if a relation exists, otherwise 0, with zero diagonal. The author keeps |β| below 1/(largest eigenvalue of R). This is "not strictly necessary in formula (3)", but without it the series (5) does not converge and c loses some of its interpretations (pp. 1177–1178, fn. 10).
- **Conventional prediction.** In all four networks conventional measures rank D>E>F; so do c(α,β) for moderately positive β (p. 1177, fn. 9). Yet E got the highest profit in all four networks, not D (p. 1178). Table 2 gives E's mean profit per exchange:

| E's exchange with | Exp. 1c | Sim. 1c | 1d | 1e | 1f |
|---|---|---|---|---|---|
| D | 13.97 | 16.96 | 15.21 | 18.60 | 19.34 |
| F | 15.43 | 17.94 | 16.97 | 19.22 | 20.00 |

- **1c (Table 3, p. 1180).** At β=0, D=E (proportional to degree). For β>0 it ranks D>E>F. For β<0, E exceeds D, and the gap grows as β falls (p. 1178). F has one tie and no alternatives, so it is powerless. E is powerful because its F partners are powerless. D is relatively powerless because it is tied to two powerful E's (p. 1178).
- **1d.** Since R²**1** ∝ R**1**, by (5) c ∝ R**1** for all β. Table 3 shows D 1.62, E 1.08, F .54 in every row given (β from −.4 to .4). The same holds for e (pp. 1178–1179, fns. 10–11). The author suggests an ad hoc fix: make R asymmetric so that F contributes to E's centrality but not vice versa. This removes the proportionality and gives F zero centrality. In Table 4, for β=−.4 and −.5 E is more central than D (pp. 1179, 1181).
- **1e.** Similar to 1c: D=E at β=0, D>E for β>0, D<E for β<0 (p. 1179).
- **1f.** D is more central than E for β>.2, even though D has smaller degree. For β ≤ .2, E is more central (p. 1179).
- **Cook et al.'s hypothesis.** In one way, the author says, c predicts the empirical results better than Cook et al.'s own hypotheses. They hypothesise (their p. 285, cited on p. 1181) that D and F are equally powerful in relation to the more powerful E. In the experiment and all four simulations E gains less with D than with F, "which indicates" that D has more exchange power than F. The author calls this unexplained consistency compatible with the centrality orderings in Tables 3 and 4 when β is sufficiently negative (pp. 1179–1181).

*Intuition note.* In these trade networks a position gains by having partners with no alternatives. Negative β builds that into the score. The fit is good for 1c and 1e, only partial for 1f, and in 1d needs an ad hoc change.

### Conclusions (pp. 1181–1182)
- **Objection.** "To some" the measure may seem hopelessly ambiguous because rankings change with β. **Author:** the measure accentuates an inherent ambiguity in the concept of centrality (p. 1181).
- There are different types of centrality, depending on how much local versus global structure is weighted and on whether the weight is positive or negative. There is no point in subsuming all these situations under one measure. A common core remains: one's status is a function of the status of those one is connected to (p. 1181).
- **Further use.** Best-fitting β could characterise structures, with variation in optimal β corresponding to differences in system integration. Roy and Bonacich (1985) found that central railroads in interlocking directorates were not particularly important in the late 19th and early 20th centuries, because power lay in separate, balkanized communities of interest. They used a completely different measure. The author says their results correspond to a situation where negative rather than positive β predicts power. If communities of interest declined in significance and the system became better integrated later in the 20th century, the optimal value becomes more positive (p. 1182).

## Toy example (ours)
The solid-line graph of network 1c, as I read Fig. 2, is a path F–E–D–E–F. Take α=1 and use symmetry: D = d, both E's = e, both F's = f. Equation (3) in matrix form is c = R**1** + βRc (this is (7a) with α=1), so:
- d = 2 + β(2e)
- e = 2 + β(d+f)
- f = 1 + βe

The largest eigenvalue of this 5-node path is 2cos(π/6)=√3≈1.73 (added fact), so we need |β|<0.577.

**β=0:** d=2, e=2, f=1. This is the degree vector, and D=E.

**β=+0.25:** d=2+0.5e and f=1+0.25e, so d+f=3+0.75e. Then e=2+0.25(3+0.75e)=2.75+0.1875e, so e=2.75/0.8125≈3.385. Then d=2+0.5(3.385)≈3.692 and f=1+0.25(3.385)≈1.846. Check: e=2+0.25(3.692+1.846)=3.385 ✓. The order is D>E>F.

**β=−0.5:** d=2−e and f=1−0.5e, so d+f=3−1.5e. Then e=2−0.5(3−1.5e)=0.5+0.75e, so e=2. Then d=0 and f=1−1=0. Only E is non-zero, so E is the most central, as in Cook et al.'s 1c data. Rescaling to Σc²=5 gives e=√2.5≈1.58, matching Table 3's row for β=−.5 (D .00, E 1.58, F .00).

## Concepts
- [[katz-bonacich-centrality]] — c(α,β)=α(I−βR)⁻¹R1, a walk count weighted by βᵏ; here β may also be negative (pp. 1173, 1174, fn. 7)
- [[eigenvector-centrality]] — e: centrality equals summed ties weighted by neighbours' centralities, Re=λe; the limit of c as β→1/λ_max (pp. 1172–1173)
- [[adjacency-matrix]] — R, with R_ij=1 if a relation exists and zero diagonal; powers Rᵏ count paths (pp. 1172, 1174, 1178)
- [[neumann-series]] (new) — the expansion of (I−βR)⁻¹ as Σβᵏ(R)ᵏ; converges when |β|<1/λ_max (p. 1173)
- [[negative-exchange-system]] (new) — exchange in one relation precludes exchange in others; modelled with β<0 (p. 1171)
- [[beta-as-radius]] (new) — β sets how far indirect ties count; β=0 is degree, larger |β| is more global (pp. 1171, 1174)

## Canonical instances
- [[cook-exchange-networks]] — networks 1c–1f where position E out-earns the most central D; the central test case for β<0 (pp. 1177–1181)
- [[fig1-power-hierarchy]] (new) — the three-level hierarchy, where B leads A for small β and A leads from about β=.5 (pp. 1175–1176)
- [[roy-bonacich-railroads]] — central firms peripheral to all power centres, while powerful firms sat at the centres of separate communities of interest, which the author says corresponds to negative β predicting power, though a different measure was used (p. 1182)

## Bridges (candidates)
- [same-math] c(α,β) as a walk-weighted sum ↔ linear algebra: the geometric (Neumann) series (I−βR)⁻¹=ΣβᵏRᵏ — the same expansion, valid under the stated eigenvalue bound.
- [structural-analogy] β as probability of passing a message on ↔ damping in PageRank-style iteration — both attenuate longer paths geometrically.
- [structural-analogy] Negative β (alternating signs by walk length) ↔ signed-network or balance-type weighting — odd and even steps carry opposite sign.

## Questions this raises
- How should β be chosen in practice? The author only suggests best-fitting β, or matching it to how transitive or local the process is (pp. 1174–1175, 1182).
- What happens for β beyond ±1/λ_max, where the series diverges, although the limit is "not strictly necessary in formula (3)" (p. 1178, fn. 10)?
- Is the asymmetric repair of 1d principled, or only ad hoc, as the author calls it (p. 1179)?
- Can the sign of β be estimated from data rather than assumed from the type of exchange?

## Reading notes
- Page offset: printed = pdf + 1169 (e.g. pdf 4 = p. 1173). Pdf 11 shows no printed number, as it is a rotated table page. I cite it as p. 1180 by position between pp. 1179 and 1181. The title shows the 1987 *AJS* 92(5) printing.
- The text layer of pdf 11 (Table 3) is garbled. I read the values from the rotated image.
- Footnote 7 prints t = β⁻¹c(1,β). From the series as printed, t = βΣ_{k≥0}β^kR^{k+1}**1** = βc(1,β). This looks like a misprint.
- On p. 1179 the text layer prints "a = − .5" in "(β = −.4 and a = −.5 in table 4)", but the page image reads "β = − .4 and β = − .5"; this is an OCR error, not a misprint in the source.
- In Table 4 the entry for β=−.1, E=1.84 breaks the sequence 1.23, 1.84, 1.16. It is probably a misprint.
- Text and Table 3 for 1f: the text says E is more central for β ≤ .2. As I read the rotated image, at β=.2 D=1.65 and E=1.59, so the table suggests the crossing lies between .1 and .2.
- The text layers print "a/ot" and "1/3" for α and β. On p. 1182 (text layer only, no image supplied) the optimal-value passages read "a"; context indicates β.
