---
id: popper-1959-logic/appvii-untitled
work: popper-1959-logic
unit: "Appendix vii — Remarks Concerning an Imaginary Experiment (cf. section 77)"
pages: 305-308
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Appendix vii: Remarks Concerning an Imaginary Experiment

## L0 — One line
Popper argues that, in his imaginary experiment, each factor of the product (ΔP)y·(Δb₂)y can be made as small as we like, independently of the other. He adds that showing one factor can be made small without the other growing beyond all bounds would already suffice to refute Heisenberg's assertion about the limits of attainable precision.

## L1 — The gist (≤ 120 words)
Popper offers remarks on the imaginary experiment of section 77. In it, an [A]-particle arrives at X from direction PX, and a [B]-particle leaves P. Δ marks an indeterminacy (uncertainty) of a quantity. Using diffraction at a slit at X and relations (1)–(8), he argues that the y-components (ΔP)y and (Δb₂)y can each be made as small as we like, independently. He adds that it would have been enough to show one of the two factors can be made small without the other growing beyond all bounds. He concludes that, as regards precision, the measurement of the [A]-particle at X and the prediction of the [B]-particle's path are symmetrical.

**Prerequisites:** vectors and magnitudes; momentum and its conservation; angle ≈ error/size; reading "≅" as "approximately equal"; Appendix vi and section 77 (not reproduced here).

## L2 — Key ideas
- Popper assumes a₁ and |b₁| are measured or selected with arbitrary precision. Only the indeterminacies Δa₂, Δb₂ and ΔP then remain to be examined (p. 305).
- Slit diffraction gives a directional indeterminacy φ ≅ h/(r·|a₂|). It shrinks as |a₂| grows (p. 306).
- |Δa₂| ≅ h/r does not depend on |a₂|. Popper says it cannot be lowered by this method (raising |a₂|); it would decrease only by increasing r, which would increase |ΔP| (p. 306).
- The same reasoning applies to the [B]-particle: ψ ≅ h/(r·|b₂|). So (Δb₂)y can be made small by large |b₂|, without harming the precision of the position of P (p. 307).
- Hence each factor of (ΔP)y·(Δb₂)y can be made small independently. Popper says showing one factor small without the other growing beyond all bounds would suffice against Heisenberg's assertion (p. 307).
- For an appropriate choice of the PX-direction, ΔP and Δb₂ are parallel and, for sufficiently small φ, normal to PY. Precision of momentum and position in that direction then becomes independent of the precision of the measurement of the position of P (p. 307).
- Popper concludes that the measurement of the [A]-particle and the prediction for the [B]-particle are completely symmetrical in precision (p. 308).

## L3 — Walkthrough

**Starting assumptions (p. 305).** a₁ and |b₁| are measured or selected with arbitrary precision. By the result of appendix vi, we may assume |a₂| (the particle arriving at X from direction PX) can be measured with arbitrary precision. Then |b₂| may also be determined as precisely as we choose, using conservation of energy. The position of Sl and X, and the arrival instants of the [A]-particles at X, can be measured with arbitrary precision. So only these remain: Δa₂ and Δb₂, which arise from indeterminacies of "the corresponding directions", and the vector ΔP. ΔP is tied to the indeterminacy of the position of P, which also arises from an indeterminacy of a direction, namely PX. Footnote *1 refers to note *1 to appendix vi, which criticises some assumptions of section 77 and this appendix (p. 305).

**The [A]-side (p. 306).** A beam through a slit of width r at X gets a directional indeterminacy φ from diffraction. h is not defined on these pages.
$$\varphi \cong \frac{h}{r\,|\mathbf a_2|}\tag{1}$$
$$|\Delta \mathbf a_2| \cong \varphi\,|\mathbf a_2|\tag{2}$$
$$|\Delta \mathbf a_2| \cong \frac{h}{r}\tag{3}$$
By (3), |Δa₂| does not depend on |a₂|. By this method (raising |a₂|) it cannot be decreased; it would decrease only by increasing r, and that would increase |ΔP| (p. 306). For any chosen r, φ can be made as small as we like by raising |a₂|. So the PX-component (Δa₂)ₓ can also be made as small as we like. This does not interfere with the precision of the position of P, which also becomes more precise with increasing |a₂| and decreasing r (p. 306).

*Intuition note:* A larger momentum |a₂| narrows the angular spread φ, and with it the PX-component (Δa₂)ₓ. The total indeterminacy |Δa₂| stays at h/r; by this method it cannot be lowered, and it would decrease only by increasing r.

**The [B]-side (pp. 306–307).** Goal: show a corresponding result for (Δb₂)y, the PY-component of Δb₂. Since Δa₁ = 0 by assumption, conservation of momenta gives
$$\Delta \mathbf b_2 = \Delta \mathbf b_1 - \Delta \mathbf a_2\tag{4}$$
For given a₁, |b₁|, |a₂|, Δb₁ depends directly on φ. So an arrangement is possible with
$$|\Delta \mathbf b_1| \cong |\Delta \mathbf a_2| \cong \frac{h}{r}\tag{5}$$
$$|\Delta \mathbf b_1| - |\Delta \mathbf a_2| \cong \frac{h}{r}\tag{6}$$
In analogy to (2), with ψ the indeterminacy of the direction of b₂:
$$|\Delta \mathbf b_2| \cong \psi\,|\mathbf b_2|\tag{7}$$
By (4) and (5):
$$\psi \cong \frac{|\Delta \mathbf b_1 - \Delta \mathbf a_2|}{\mathbf b_2} \cong \frac{h}{r\,|\mathbf b_2|}\tag{8}$$
However small r is, ψ and with it (Δb₂)y can be made as small as we like by sufficiently large |b₂|. This again does not interfere with the precision of the position of P (p. 307).

*Intuition note:* The position side improves by shrinking r and raising |a₂|. The momentum side improves by raising |b₂|. Shrinking r raises ψ for a given |b₂|, but ψ can still be made small "however small we make r" by taking |b₂| large enough (p. 307). So each factor of (ΔP)y·(Δb₂)y can be made small independently of the other.

**Conclusion on Heisenberg (p. 307).** Each factor of (ΔP)y·(Δb₂)y can be made as small as we like, independently of the other. For refuting Heisenberg's assertion about the limits of attainable precision, it would have been sufficient to show that one factor can be made as small as we like without the other growing beyond all bounds.

**Addition (pp. 307–308).** By an appropriate choice of the PX-direction, the distance PX can be fixed so that ΔP and Δb₂ are parallel. For sufficiently small φ they are then normal to PY. The precision of momentum in this direction, and of position in the same direction, both become independent of the precision of the measurement of the position of P. The latter depends mainly on the smallness of r if |a₂| is high (pp. 307–308). Both depend only on the precision of the measured position and momentum of the particle arriving at X from PX, and on the smallness of ψ. This matches the dependence of (Δa₂)ₓ on the smallness of φ (p. 308). Footnote: Schiff pointed out that examining exactness in a direction perpendicular to Δs can be relevant. Popper thanks Dr. K. Schiff for collaborating through the better part of a year (p. 307).

**Final remark (p. 308).** With respect to precision, the apparently non-predictive measurement of the [A]-particle arriving at X and the prediction of the path of the [B]-particle leaving P are completely symmetrical.

## Toy example (ours)
Take units with h = 1 and slit width r = 0.5, using (1)–(3) as equalities.
- |a₂| = 10: φ = 1/(0.5·10) = 0.2, and |Δa₂| = 0.2·10 = 2.
- |a₂| = 100: φ = 1/(0.5·100) = 0.02, and |Δa₂| = 0.02·100 = 2. φ fell tenfold, |Δa₂| = h/r = 2 did not change.
- For the [B]-side with (8): |b₂| = 20 gives ψ = 1/(0.5·20) = 0.1. |b₂| = 200 gives ψ = 1/(0.5·200) = 0.01. The directional indeterminacy ψ falls as |b₂| grows, at the same r.

## Concepts
- [[imaginary-experiment]] (new) — Popper's thought-experiment of section 77, here examined to refute Heisenberg's assertion on attainable precision (pp. 305, 307)
- [[directional-indeterminacy]] (new) — uncertainty in a beam's direction: φ for the beam through the slit, ψ for the direction of b₂ (pp. 306–307)
- [[slit-diffraction-relation]] (new) — φ ≅ h/(r·|a₂|); |Δa₂| ≅ h/r, independent of |a₂| (p. 306)
- [[sufficient-counterexample-to-limit-claim]] (new) — Popper: one factor made small without the other growing beyond all bounds would suffice to refute (p. 307)

## Canonical instances
- [[section-77-imaginary-experiment]] — the setting: [A]-particle at X, [B]-particle leaving P (pp. 305, 308)

## Bridges (candidates)
- [structural-analogy] "One factor small without the other unbounded suffices" ↔ falsifiability: one counter-case can refute a universal claim.

## Questions this raises
- What exactly does Heisenberg's assertion claim, and which assumptions of section 77 does note *1 to appendix vi criticise?
- Why does Popper stress that a perpendicular direction matters?
- Are the "≅" relations accurate enough for the "as small as we like" conclusions?

## Reading notes
- Printed pages 305–308 (pdf 334–337); printed = pdf − 29.
- Equation (6) is printed as |Δb₁| − |Δa₂| ≅ h/r. I could not reconcile this with the equal magnitudes in (5), but (8) uses |Δb₁ − Δa₂|, so I reproduce it as the image shows.
- The unit relies on appendix vi, section 77 and unexplained notation (Sl, Δs, h, [A], [B]), none defined here.
- In (8) the denominator of the middle term is printed as bold b₂ without absolute-value bars (p. 307); the digest reproduces it as printed.
