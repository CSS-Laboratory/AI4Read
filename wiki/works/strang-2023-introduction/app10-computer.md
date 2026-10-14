---
id: strang-2023-introduction/app10-computer
work: strang-2023-introduction
unit: Appendix 10 — Computer Graphics
pages: 413–418
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Computer Graphics: 4 by 4 matrices and homogeneous coordinates

## L0 — One line
Adding a fourth coordinate equal to 1 turns shifts, which are not linear in R³, into 4 by 4 matrix multiplication, so translation, scaling, rotation and projection can all be chained as matrices.

## L1 — The gist (≤ 120 words)
Graphics must move, rescale, rotate and project images. A translation adds a fixed vector to every point. This is not linear, so no 3 by 3 matrix can do it. Strang writes the point (x, y, z) as the row vector (x, y, z, 1), called homogeneous coordinates. Every operation then becomes a 4 by 4 matrix with last column (0, 0, 0, 1). Because the matrices have the same size, they can be multiplied. Rotation about an arbitrary point, or projection onto a plane that misses the origin, becomes "translate, act, translate back". The order matters. The appendix also has a short note on pixels, a review of key ideas, and exercises.

**Prerequisites:** matrix–vector and matrix–matrix products; orthogonal matrices; projection I − nnᵀ; row versus column vectors.

## L2 — Key ideas
- A shift v → v + v₀ is not linear, so no 3 by 3 matrix does it. Four key operations are listed: translation, rescaling, rotation, projection. (p. 413)
- Homogeneous coordinates (x, y, z, 1) with row vectors give a 4 by 4 translation matrix T. (p. 413)
- Scaling matrices keep a 1 in the corner; (cx, cy, cz, c) is the same point as (x, y, z, 1). Translate-then-scale differs from scale-then-translate. (p. 414)
- Affine transformations (linear plus shift) are 4 by 4 matrices with last column (0, 0, 0, 1). The bottom row is the image of the origin. (p. 414)
- Rotation about a point P is T₋ R T₊: shift P to the origin, rotate, shift back. (p. 415)
- Rotation about a unit axis a has the three-part formula (1). The axis is fixed because aQ = a. (p. 415)
- Projection onto a plane through the origin is I − nnᵀ. Projection onto a flat (a plane not through the origin) is T₋PT₊. Reflection uses I − 2nnᵀ. (pp. 415–416)
- Perspective projection includes foreshortening (an object looks larger as it moves closer), which is why it is more popular; the parallel projection P moves points parallel to n. (p. 416)

## L3 — Walkthrough

**Intro (p. 413).** Operations: translation (shift origin to P₀ = (x₀, y₀, z₀)), rescaling, rotation, projection. Translation is "not linear! No 3 by 3 matrix can move the origin." Fix: use homogeneous coordinates, so (x, y, z) becomes (x, y, z, 1) and the origin becomes (0, 0, 0, 1).

**1. Translation (p. 413).** Computer graphics uses **row vectors**: row times matrix.
$$T=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\x_0&y_0&z_0&1\end{bmatrix},\qquad [x\;y\;z\;1]\,T=[x+x_0\;\;y+y_0\;\;z+z_0\;\;1].$$
Check: $[0\;0\;0\;1]T=[x_0\;y_0\;z_0\;1]$. Every v moves to v + v₀.

*Intuition note:* The extra 1 acts as a "constant" slot. Multiplying it by the bottom row of T adds the shift.

**2. Scaling (pp. 413–414).** The plane uses a 3 by 3 matrix S = diag(.9, .9, 1). A solid uses S = diag(c, c, c, 1). Important: S is not cI. The origin stays fixed because $[0\;0\;1]S=[0\;0\;1]$.
- If the 1 is changed to c, then (cx, cy, cz, c) is the same point as (x, y, z, 1). Multiplying by cI does not move the point. This is the reason for the word "homogeneous".
- Different factors per direction: S = diag(¾, ½, 1) in the plane (full page onto half page; margin), and S = diag(c₁, c₂, c₃, 1) for a solid.
- S and T are the same size, so they multiply. Translate then rescale is vTS. Rescale then translate is vST. These differ. (p. 414)
- Projective space P³: the point (x, y, z, 1) represents (cx, cy, cz, c). These points are lines through the origin in R⁴. P³ is still three-dimensional. (p. 414)

**Affine transformations (p. 414).** Affine means linear plus shift. It is executed by
$$A=\begin{bmatrix}a_{11}&a_{12}&a_{13}&0\\a_{21}&a_{22}&a_{23}&0\\a_{31}&a_{32}&a_{33}&0\\a_{41}&a_{42}&a_{43}&1\end{bmatrix}=\begin{bmatrix}T(1,0,0)&0\\T(0,1,0)&0\\T(0,0,1)&0\\T(0,0,0)&1\end{bmatrix}.$$
A linear map is fixed by three outputs. An affine map also needs T(0,0,0), which gives the shift.

**3. Rotation (pp. 414–415).** A rotation in R² or R³ is an orthogonal matrix Q with determinant +1. Determinant −1 gives an extra reflection. Plane rotation becomes
$$R=\begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}.$$
- *Rotation about the point (4, 5):* translate (4, 5) to (0, 0), rotate, translate back:
$$vT_-RT_+=[x\;y\;1]\begin{bmatrix}1&0&0\\0&1&0\\-4&-5&1\end{bmatrix}R\begin{bmatrix}1&0&0\\0&1&0\\4&5&1\end{bmatrix}.$$
- Apply the matrices one at a time, left to right, because the points are row vectors. T₋ acts first. The centre (4, 5, 1) goes to (0, 0, 1), is unchanged by R, and returns to (4, 5, 1). The point (4, 6, 1) goes to (0, 1, 1), turns by θ, then moves back. (p. 415)
- In 3D, a rotation turns around an axis. The axis is a line of eigenvectors with λ = 1. For the z axis, Q is the 3 by 3 block above and $R=\begin{bmatrix}Q&0\\0\;0\;0&1\end{bmatrix}$, with a zero column beside Q.
- Rotation about a unit vector $a=(a_1,a_2,a_3)$:
$$Q=(\cos\theta)I+(1-\cos\theta)\begin{bmatrix}a_1^2&a_1a_2&a_1a_3\\a_1a_2&a_2^2&a_2a_3\\a_1a_3&a_2a_3&a_3^2\end{bmatrix}-\sin\theta\begin{bmatrix}0&a_3&-a_2\\-a_3&0&a_1\\a_2&-a_1&0\end{bmatrix}\tag{1}$$
The axis does not move because $aQ=a$. For a = (0, 0, 1), (1) becomes the z-axis Q above.
- Q goes in the upper left block of R. The zeros below it keep the origin fixed. If they are not zeros, the map is affine and the origin moves. (p. 415)

*Intuition note:* In the (4, 5) example, "move the centre to the origin, turn, move back" is the pattern; the same three steps appear for a flat on p. 416. Each step is a matrix, and the product is the whole motion.

**4. Projection (pp. 415–416).** A plane through the origin is a vector space. Other planes are affine spaces ("flats"), obtained by translating a vector space.
- Plane through the origin with unit normal column n: vectors satisfy nᵀv = 0. The projection is I − nnᵀ. It sends n to 0: $(I-nn^T)n=n-n(n^Tn)=0$. It leaves in-plane v unchanged: $(I-nn^T)v=v-n(n^Tv)=v$. (p. 415)
- Homogeneous form: $P=\begin{bmatrix}I-nn^T&0\\0&1\end{bmatrix}$, with a zero column beside I − nnᵀ and bottom row (0 0 0 1). (p. 416)
- Flat nᵀ(v − v₀) = 0, with v₀ a point on it. It resembles solutions of Av = b: one particular solution plus the nullspace. Three steps: translate v₀ to the origin, project along n, translate back:
$$T_-PT_+=\begin{bmatrix}I&0\\-v_0&1\end{bmatrix}\begin{bmatrix}I-nn^T&0\\0&1\end{bmatrix}\begin{bmatrix}I&0\\v_0&1\end{bmatrix}.$$
T₋ and T₊ are inverses, like the elementary matrices of Chapter 2. (p. 416)
- Reflection (mirror matrix) is the fifth type. It moves each point twice as far as the projection does, so replace I − nnᵀ by I − 2nnᵀ. (p. 416)
- P is a *parallel* projection: points move parallel to n. *Perspective* projection is "more popular" because it includes foreshortening, so an object looks larger when closer. The projection lines go toward the eye, the centre of projection. (p. 416)

**Pixels (p. 416).** Strang's closing note: a pixel is a small picture element. One bit per pixel gives black and white. In practice each of three colours gets shading levels, 8 bits each, so 8 × 3 = 24 bits per pixel. The quality depends on the number of pixels and bits per pixel. A raster frame buffer directs the electron beam, scanning like a television set; Strang names a standard text, *Computer Graphics: Principles and Practice*, for this area.

**Review (p. 417).** (1) Graphics needs shifts v + v₀ as well as linear maps Av. (2) A shift in Rⁿ is a matrix of order n + 1 in homogeneous coordinates. (3) The extra 1 is preserved when all matrices have last column 0, 0, 0, 1.

## Toy example (ours)
Plane, row vectors, homogeneous 3-vectors. Let $T=\begin{bmatrix}1&0&0\\0&1&0\\1&2&1\end{bmatrix}$ (shift by (1, 2)), $S=\text{diag}(2,2,1)$, and $v=[3\;1\;1]$.
- Translate then scale (vTS): $vT=[3+1,\;1+2,\;1]=[4\;3\;1]$. Then $[4\cdot2,\;3\cdot2,\;1]=[8\;6\;1]$.
- Scale then translate (vST): $vS=[6\;2\;1]$. Then $[6+1,\;2+2,\;1]=[7\;4\;1]$.
- Since $[8\;6\;1]\ne[7\;4\;1]$, order matters.
- Check: $[16\;12\;2]$ is the same point as $[8\;6\;1]$, since both divide down to $(8,6,1)$ (the homogeneous rule).

## Concepts
- [[homogeneous-coordinates]] (new) — (x, y, z) written as (x, y, z, 1); (cx, cy, cz, c) is the same point (pp. 413–414)
- [[affine-transformation]] (new) — linear plus shift; a 4 by 4 matrix with last column (0, 0, 0, 1) (p. 414)
- [[projective-space]] (new) — P³: points are lines through the origin in R⁴ (p. 414)
- [[row-vector-convention]] (new) — vectors are rows and act on the left; the first matrix in the product acts first (pp. 413, 415)
- [[reflection-matrix]] (new) — I − 2nnᵀ; moves points twice as far as projection (p. 416)
- [[matrix as transformation]] — here T, S, R, P are all 4 by 4 maps (pp. 413–416)
- [[matrix multiplication as composition]] — order of products is order of operations (pp. 414–415)
- [[orthonormal basis / orthogonal matrix]] — an orthogonal matrix Q with determinant +1 gives a rotation (p. 414)
- [[projection]] — I − nnᵀ onto a plane with unit normal n (p. 415)
- [[eigenvector / eigenvalue]] — the rotation axis is a line of eigenvectors with λ = 1 (p. 415)
- [[inverse matrix]] — T₋ and T₊ undo each other (p. 416)

## Canonical instances
- [[rotation-about-point-4-5]] — T₋RT₊ with centre (4, 5) (p. 415)
- [[axis-angle-rotation-matrix]] — formula (1), unit axis a (p. 415)
- [[projection-onto-a-flat]] — T₋PT₊ (p. 416)
- [[pixel-24-bit-colour]] — 8 × 3 = 24 bits per pixel (p. 416)

## Bridges (candidates)
- [structural-analogy] translate–act–translate back, T₋PT₊ ↔ change of basis: A ↦ P⁻¹AP — conjugating by an invertible map.
- [same-math] projection onto a flat, "v₀ + nullspace" ↔ solutions of Av = b — the author says a flat is like the solutions of Av = b: one particular solution added to the nullspace (p. 416).
- [metaphor] projective points as lines through the origin of R⁴ ↔ scale-free ratios (ratios as the same data under a scale factor).

## Questions this raises
- How does perspective projection fit into a 4 by 4 matrix? The text only describes it verbally.
- Since rotations and scalings fix the 1, what operation changes the last coordinate, and how is it turned back into 1?
- How are the many steps of a long chain of T, S, R, P matrices combined into one matrix?

## Exercises worth doing
- Ex. 3 (p. 417) — multiply two translation matrices and read off what the product does — easy
- Ex. 4 (p. 417) — ST versus TS; which blows up around the centre (1, 4, 3) — medium
- Ex. 6 (p. 417) — one 4 by 4 matrix: move a corner to the origin, then double lengths — medium
- Ex. 7–8 (p. 417) — verify that formula (1) fixes the axis and rotates a perpendicular b by θ — hard
- Ex. 10 (p. 418) — build T₋PT₊ for the plane ⅔x + ⅔y + ⅓z = 1 — medium
- Ex. 15 (p. 418) — reflect (3, 3, 3) in a plane not through the origin — medium

## Reading notes
- Printed page = pdf page − 10. The text layer is garbled for the matrices; they were checked against the page images.
- The problem set is labelled "Problem Set 10.3" in an appendix chapter A10 (as printed).
- Exercise 14's plane is garbled in the text layer; the image shows ⅔x + ⅔y + ⅓z = 0.
- Ex. 6 has the printed typo "multply".
- Shading levels are printed as "between 0 and 2⁸".
