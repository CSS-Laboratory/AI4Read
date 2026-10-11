---
field: Linear algebra
slug: linear-algebra
layer: foundation
compiled: 2026-10-11
---
# Linear algebra — Canon

## Scope
This catalog covers linear algebra as the shared language of networks, statistics, and machine learning. It is organised in four strands: (1) geometric intuition and on-ramps (3Blue1Brown, Strang's MIT 18.06 and textbooks); (2) the rigorous, basis-free theory of vector spaces and operators (Axler, Halmos, Hoffman & Kunze); (3) numerical and applied linear algebra for data and ML (Boyd & Vandenberghe, Deisenroth et al., Trefethen & Bau, Golub & Van Loan, Strang's 18.065); and (4) classic papers where one matrix idea founded a field: PCA, low-rank approximation, PageRank, latent semantic analysis, eigenvector centrality, eigenfaces, spectral clustering, and word-vector arithmetic. The selection was checked against current syllabi: MIT 18.06 (Strang), MIT 18.065 (*Linear Algebra and Learning from Data*), Stanford ENGR108 (VMLS), and MIT 18.335J (Trefethen & Bau). Out of scope: infinite-dimensional functional analysis, abstract module theory, and tensor decompositions beyond brief mentions. The Kalman filter is also left out. It belongs to estimation and control, and its linear-algebra core (least squares and linear dynamical systems) is already covered by VMLS chs. 9 and 12–16. History has no separate items; it lives in the classic papers.

## Canon

### Strand: Intuition and on-ramps

#### sanderson-2016-essence
- **type:** video
- **citation:** Sanderson, G. (2016). *Essence of Linear Algebra* (video series: preview + Chapters 1–16). 3Blue1Brown, YouTube.
- **tier:** core
- **level:** HS
- **why:** This series treats a matrix as a transformation of space, not a grid of numbers. Determinants become area or volume scaling factors, matrix products become compositions of transformations, and eigenvectors become the directions that stay on their own line. It is the standard geometric warm-up recommended alongside almost every course, and it builds the intuition that formal texts assume and never draw.
- **focus:** Ch. 1 "Vectors"; Ch. 2 "Linear combinations, span, and basis vectors"; Ch. 3 "Linear transformations and matrices"; Ch. 4 "Matrix multiplication as composition"; Ch. 6 "The determinant"; Ch. 7 "Inverse matrices, column space and null space"; Ch. 9 "Dot products and duality"; Ch. 13 "Change of basis"; Ch. 14 "Eigenvectors and eigenvalues"; Ch. 16 "Abstract vector spaces".
- **access:** free: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **verified:** https://www.3blue1brown.com/lessons/eola-preview (series dated Aug 2016); chapter titles from the YouTube playlist above.

#### strang-2010-mit1806
- **type:** course
- **citation:** Strang, G. (2010). *18.06 Linear Algebra, Spring 2010* [video lectures and course materials]. MIT OpenCourseWare.
- **tier:** core
- **level:** UG
- **why:** These are the most widely watched linear algebra lectures in the world. Strang organises the subject around the "four fundamental subspaces" and the column picture of Ax = b. The course reaches graphs and incidence matrices, Markov matrices, and the SVD early, which is exactly what a network scientist needs.
- **focus:** Lecture 1 "The geometry of linear equations"; L10 "The four fundamental subspaces"; L11 "Matrix spaces; rank 1; small world graphs"; L12 "Graphs, networks, incidence matrices"; L14–16 (orthogonality, projections, least squares); L21–22 (eigenvalues, diagonalization and powers of A); L24 "Markov matrices; fourier series"; L25 and L27 (positive definite matrices); L29 "Singular value decomposition"; L31 "Change of basis; image compression".
- **access:** free: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- **verified:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/

#### strang-2023-introduction
- **type:** book
- **citation:** Strang, G. (2023). *Introduction to Linear Algebra* (6th ed.). Wellesley-Cambridge Press. ISBN 978-1-7331466-7-8.
- **tier:** core
- **level:** UG
- **why:** This is the textbook behind 18.06. The 6th edition rebuilds the subject around the factorizations A = CR, LU, QR, QΛQᵀ, and UΣVᵀ, so every topic becomes a way of factoring data. New chapters connect directly to optimization and learning from data.
- **focus:** 1.3 "Matrices and Their Column Spaces"; 1.4 "Matrix Multiplication AB and CR"; 3.5 "Dimensions of the Four Subspaces"; 4.2 "Projections onto Lines and Subspaces"; 4.3 "Least Squares Approximations"; 6.1–6.3 (eigenvalues, diagonalizing, symmetric positive definite); Ch. 7 "The Singular Value Decomposition (SVD)" (7.1–7.3, including PCA by the SVD); 9.4 "Linear Programming, Game Theory, and Duality".
- **access:** need-copy (free sample sections 1.4, 2.2, 3.5, 6.1 and the outline are on the author's site: https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html)
- **verified:** https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html; TOC from https://math.mit.edu/~gs/linearalgebra/ila6/ila6outline.pdf

#### strang-2020-everyone
- **type:** book
- **citation:** Strang, G. (2020). *Linear Algebra for Everyone*. Wellesley-Cambridge Press. ISBN 978-1-7331466-3-0.
- **tier:** deep
- **level:** UG
- **why:** This is Strang's shorter, data-oriented version of the subject. It opens with column-times-row thinking (A = CR) and moves quickly to the SVD and to learning from data. It suits a working scientist who wants Strang's viewpoint without the full 18.06 syllabus.
- **focus:** whole (Sections 1.3 and 1.4 and an SVD image-compression note are free samples on the author's site)
- **access:** need-copy
- **verified:** https://math.mit.edu/~gs/everyone

#### hiranabe-2021-artoflinearalgebra
- **type:** website
- **citation:** Hiranabe, K. (with the help of G. Strang) (2021; updated 2025). *The Art of Linear Algebra: Graphic Notes on "Linear Algebra for Everyone"*. GitHub repository, 12 pp. PDF.
- **tier:** deep
- **level:** UG
- **why:** These are visual "cheat-sheet" diagrams of the five matrix factorizations (CR, LU, QR, QΛQᵀ, UΣVᵀ), plus a "Map of Eigenvalues" and a "Matrix World" diagram, made with Strang's blessing. Each factorization becomes a picture of how columns and rows combine, which makes it a good compact review. It is written by a Japanese engineer and has a Japanese version.
- **focus:** whole (12 pages); also "MapofEigenvalues.pdf" and "MatrixWorld.pdf" in the same repository.
- **access:** free: https://raw.githubusercontent.com/kenjihiranabe/The-Art-of-Linear-Algebra/main/The-Art-of-Linear-Algebra.pdf
- **translation:** Japanese version (The-Art-of-Linear-Algebra-j.pdf) and Chinese version (The-Art-of-Linear-Algebra-zh-CN.pdf) in the same repository.
- **verified:** https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra

### Strand: Rigorous and abstract

#### axler-2024-ladr
- **type:** book
- **citation:** Axler, S. (2024). *Linear Algebra Done Right* (4th ed.). Springer, Undergraduate Texts in Mathematics. Open Access (CC BY-NC). https://doi.org/10.1007/978-3-031-41026-0
- **tier:** core
- **level:** UG
- **why:** Axler develops the theory through linear maps and operators, with determinants postponed to the end, so eigenvalues, the spectral theorem, and the SVD are proved from structure rather than computation. It is the standard proof-based text (adopted at 375+ universities). It is the place to learn *why* symmetric matrices have orthonormal eigenbases and *why* the SVD exists.
- **focus:** 3B "Null Spaces and Ranges" (Fundamental Theorem of Linear Maps); 3D "Invertibility and Isomorphisms"; 3F "Duality"; 5A–5D (invariant subspaces, minimal polynomial, upper-triangular matrices, diagonalizable operators); 6B "Orthonormal Bases"; 6C "Orthogonal Complements and Minimization Problems"; 7B "Spectral Theorem"; 7C "Positive Operators"; 7E "Singular Value Decomposition"; 7F "Consequences of Singular Value Decomposition".
- **access:** free: https://linear.axler.net/LADR4e.pdf
- **translation:** Chinese: 《线性代数应该这样学（第四版）》, trans. 吴俊达, 何阳, free PDF at https://linear.axler.net/LADR4eChinese.pdf (a print Chinese translation of the 3rd ed., 《线性代数应该这样学（第3版）》, also exists).
- **verified:** https://linear.axler.net/ ; https://api.crossref.org/works/10.1007/978-3-031-41026-0

#### halmos-1958-finitedimensional
- **type:** book
- **citation:** Halmos, P. R. (1958). *Finite-Dimensional Vector Spaces* (2nd ed.). Van Nostrand. Reprinted 1974, Springer-Verlag, Undergraduate Texts in Mathematics, viii + 200 pp. ISBN 0-387-90093-4.
- **tier:** deep
- **level:** UG
- **why:** Halmos wrote this classic to treat finite-dimensional spaces with the methods of Hilbert-space operator theory. It teaches linear algebra as a theory of transformations and inner products that carries over to infinite dimensions. Its short numbered sections are a model of mathematical exposition.
- **focus:** Part I "Spaces"; Part II "Transformations"; Part III "Orthogonality".
- **access:** need-copy
- **verified:** https://ci.nii.ac.jp/ncid/BA01145705?l=en ; https://proofwiki.org/wiki/Book:Paul_R._Halmos/Finite-Dimensional_Vector_Spaces

#### hoffman-1971-linearalgebra
- **type:** book
- **citation:** Hoffman, K., & Kunze, R. (1971). *Linear Algebra* (2nd ed.). Prentice-Hall, viii + 407 pp.
- **tier:** reference
- **level:** UG
- **why:** This is the traditional rigorous honors text, covering canonical forms (rational and Jordan), bilinear forms, and modules over polynomial rings. Use it as the reference when you need the full algebraic structure theory that Axler deliberately streamlines.
- **focus:** whole (consult as reference)
- **access:** need-copy
- **verified:** https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/linear-algebra-2nd-edition-by-k-hoffman-and-r-kunze-pp-viii-407-1971-prenticehall/59E7125693C27C9B0FFE033691712306

### Strand: Numerical, applied, and ML

#### boyd-2018-vmls
- **type:** book
- **citation:** Boyd, S., & Vandenberghe, L. (2018). *Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares*. Cambridge University Press. https://doi.org/10.1017/9781108583664
- **tier:** core
- **level:** UG
- **why:** This book uses only vectors, matrices, and least squares, and from that small toolkit it gets clustering (k-means), regression, classification, linear dynamical systems, and constrained fitting. It is the textbook for Stanford ENGR108. It shows how far plain linear algebra goes in data work, and it has Julia and Python companions.
- **focus:** Ch. 3 "Norm and distance"; Ch. 4 "Clustering"; Ch. 7 "Matrix examples"; Ch. 9 "Linear dynamical systems"; Ch. 12 "Least squares"; Ch. 13 "Least squares data fitting"; Ch. 14 "Least squares classification"; Ch. 15 "Multi-objective least squares".
- **access:** free: https://web.stanford.edu/~boyd/vmls/vmls.pdf
- **verified:** https://web.stanford.edu/~boyd/vmls/ ; https://web.stanford.edu/class/engr108/ ; https://api.crossref.org/works/10.1017/9781108583664

#### deisenroth-2020-mml
- **type:** book
- **citation:** Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press. https://doi.org/10.1017/9781108679930
- **tier:** core
- **level:** UG
- **why:** This book is a bridge from linear algebra and analytic geometry to ML. Inner products, projections, and matrix decompositions are developed specifically to explain regression, PCA, GMMs, and SVMs. Its "projection perspective" on PCA and its reading of maximum likelihood as orthogonal projection are especially good for intuition.
- **focus:** Ch. 2 "Linear Algebra"; Ch. 3 "Analytic Geometry" (3.8 "Orthogonal Projections", 3.9 "Rotations"); Ch. 4 "Matrix Decompositions" (4.2, 4.4, 4.5 "Singular Value Decomposition", 4.6 "Matrix Approximation", 4.7 "Matrix Phylogeny"); 9.4 "Maximum Likelihood as Orthogonal Projection"; Ch. 10 "Dimensionality Reduction with Principal Component Analysis".
- **access:** free: https://mml-book.github.io/book/mml-book.pdf
- **verified:** https://mml-book.com ; https://api.crossref.org/works/10.1017/9781108679930

#### strang-2018-matrixmethods
- **type:** course
- **citation:** Strang, G. (2018). *18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning, Spring 2018* [video lectures]. MIT OpenCourseWare. Textbook: Strang, G. (2019). *Linear Algebra and Learning from Data*. Wellesley-Cambridge Press. ISBN 978-0-692-19638-0.
- **tier:** core
- **level:** UG
- **why:** This is Strang's sequel to 18.06, aimed at data science. It covers the SVD and the Eckart–Young theorem, the four ways to solve least squares, randomized linear algebra, graph Laplacians and clustering, and the linear algebra of deep learning. The course videos are free; the book is the course text.
- **focus:** Lectures 6 "Singular Value Decomposition (SVD)", 7 "Eckart-Young: The Closest Rank k Matrix to A", 9 "Four Ways to Solve Least Squares Problems", 13 "Randomized Matrix Multiplication", 35 "Finding Clusters in Graphs". Book: Part I (I.1–I.9, ending with "Principal Components and the Best Low Rank Matrix"); II.4 "Randomized Linear Algebra"; IV.6 "Graphs and Laplacians and Kirchhoff's Laws"; IV.7 "Clustering by Spectral Methods and k-means"; V.6 "Markov Chains".
- **access:** free: https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/ (book: need-copy; TOC and sample sections at https://math.mit.edu/~gs/learningfromdata/)
- **verified:** https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/pages/syllabus/ ; https://math.mit.edu/~gs/learningfromdata/dsla_toc.pdf

#### trefethen-1997-numerical
- **type:** book
- **citation:** Trefethen, L. N., & Bau, D., III (1997). *Numerical Linear Algebra*. SIAM. ISBN 978-0-89871-361-9. 25th Anniversary ed., SIAM, 2022, https://doi.org/10.1137/1.9781611977165
- **tier:** deep
- **level:** grad
- **why:** This is the graduate standard (required text for MIT 18.335J). It is written as 40 short lectures that put the SVD at the centre from Lecture 4 onward. It explains what numpy/LAPACK actually do (QR, Householder, eigenvalue algorithms, Krylov methods) and why conditioning and stability decide whether a computed answer can be trusted.
- **focus:** Part I "Fundamentals" (Lectures 1–5, incl. 4 "The Singular Value Decomposition", 5 "More on the SVD"); Part II "QR Factorization and Least Squares" (6–11); Lectures 12 "Conditioning and Condition Numbers", 14 "Stability"; 27 "Rayleigh Quotient, Inverse Iteration"; 33 "The Arnoldi Iteration"; 36 "The Lanczos Iteration"; 38 "Conjugate Gradients".
- **access:** need-copy
- **verified:** https://www.iri.upc.edu/people/thomas/Collection/details/5350.html (TOC) ; https://api.crossref.org/works/10.1137/1.9781611977165 ; https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/syllabus/

#### golub-2013-matrixcomputations
- **type:** book
- **citation:** Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.). Johns Hopkins University Press, Johns Hopkins Studies in the Mathematical Sciences, xxi + 756 pp. ISBN 978-1-4214-0794-4.
- **tier:** reference
- **level:** grad
- **why:** This is the reference work of numerical linear algebra, the book to check for the algorithm, its cost, and its error bounds. The 4th edition adds large-scale SVD, fast transforms, multigrid, and tensor computations.
- **focus:** whole (consult as reference)
- **access:** need-copy
- **verified:** https://libwebservice.biblio.tuat.ac.jp/opac/opac_link/bibid/1000235666 ; https://nhigham.com/2013/05/31/fourth-edition-of-matrix-computations/

### Strand: Classic papers and applications

#### pearson-1901-closestfit
- **type:** paper
- **citation:** Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 559–572. https://doi.org/10.1080/14786440109462720
- **tier:** deep
- **level:** UG
- **why:** This is the geometric origin of PCA. Pearson asks for the line or plane that minimizes *perpendicular* distances to a point cloud, not vertical ones as in regression. The answer is the principal axes of the correlation ellipsoid, and this "best-fitting subspace" picture is still the clearest intuition for PCA.
- **focus:** whole (short)
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1080/14786440109462720

#### hotelling-1933-principalcomponents
- **type:** paper
- **citation:** Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. *Journal of Educational Psychology*, 24(6), 417–441. https://doi.org/10.1037/h0071325
- **tier:** reference
- **level:** UG
- **why:** Hotelling named "principal components" and framed them as the variance-maximizing eigenvectors of a correlation matrix, computed by iteration. This gives the statistical (maximum-variance) view that complements Pearson's geometric one. It came out of psychometrics, like much of early multivariate linear algebra.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1037/h0071325

#### eckart-1936-lowrank
- **type:** paper
- **citation:** Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika*, 1(3), 211–218. https://doi.org/10.1007/BF02288367
- **tier:** core
- **level:** UG
- **why:** This paper proves that truncating the SVD gives the best rank-k approximation of a matrix in least squares. It is the theorem underneath PCA, LSA, image compression, recommender systems, and LoRA-style low-rank adaptation. Strang devotes a full 18.065 lecture to it.
- **focus:** whole (8 pages)
- **access:** need-copy
- **verified:** https://link.springer.com/article/10.1007/BF02288367 ; https://api.crossref.org/works/10.1007/BF02288367

#### brin-1998-anatomy
- **type:** paper
- **citation:** Brin, S., & Page, L. (1998). The anatomy of a large-scale hypertextual Web search engine. *Computer Networks and ISDN Systems*, 30(1–7), 107–117. https://doi.org/10.1016/S0169-7552(98)00110-X
- **tier:** deep
- **level:** UG
- **why:** This is the founding Google paper. It introduces PageRank as the stationary distribution of a "random surfer" with damping, which turns link structure into importance scores. Read it for the original framing and Section 2.1; read Bryan & Leise for the linear algebra.
- **focus:** 2.1 "PageRank: Bringing Order to the Web"
- **access:** free: http://infolab.stanford.edu/pub/papers/google.pdf
- **verified:** https://api.crossref.org/works/10.1016/S0169-7552(98)00110-X

#### bryan-2006-eigenvector
- **type:** paper
- **citation:** Bryan, K., & Leise, T. (2006). The $25,000,000,000 eigenvector: The linear algebra behind Google. *SIAM Review*, 48(3), 569–581. https://doi.org/10.1137/050623280
- **tier:** core
- **level:** UG
- **why:** This is the canonical teaching exposition of PageRank as an eigenvector problem. It shows why the raw link matrix can have a non-unique dominant eigenvector, how the damping/teleportation fix guarantees uniqueness (Perron–Frobenius), and why the power method converges at a rate set by the second eigenvalue. It is one of the best single examples of eigenvectors applied to networks.
- **focus:** 2 "Developing a formula to rank pages"; 3 "A remedy for dim(V1(A)) > 1"; 4 "Computing the Importance Score Eigenvector".
- **access:** free: https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf
- **verified:** https://scholar.rose-hulman.edu/math_fac/117 ; https://www.rose-hulman.edu/~bryan/google.html

#### deerwester-1990-lsa
- **type:** paper
- **citation:** Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). Indexing by latent semantic analysis. *Journal of the American Society for Information Science*, 41(6), 391–407. https://doi.org/10.1002/(SICI)1097-4571(199009)41:6<391::AID-ASI1>3.0.CO;2-9
- **tier:** deep
- **level:** UG
- **why:** LSA applies a truncated SVD to a term–document matrix so that words and documents live in one low-dimensional "semantic" space where synonyms end up near each other. It is the direct ancestor of word embeddings and of topic-style text analysis in computational social science.
- **focus:** 3.2 "The choice of method for uncovering latent semantic structure"; 4 "SVD or two-mode factor analysis".
- **access:** free: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/JASIS90.pdf
- **verified:** https://api.crossref.org/works/10.1002/(SICI)1097-4571(199009)41:6%3C391::AID-ASI1%3E3.0.CO;2-9

#### bonacich-1987-power
- **type:** paper
- **citation:** Bonacich, P. (1987). Power and centrality: A family of measures. *American Journal of Sociology*, 92(5), 1170–1182. https://doi.org/10.1086/228631
- **tier:** core
- **level:** grad
- **why:** Bonacich defines c(β) = α(I − βA)⁻¹A1, a family of centralities indexed by β. Positive β gives eigenvector-like centrality (being connected to the well-connected); negative β gives "power" in exchange networks (being connected to the *poorly* connected). It is the sociological anchor for the claim that network centralities are matrix functions.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1086/228631

#### turk-1991-eigenfaces
- **type:** paper
- **citation:** Turk, M., & Pentland, A. (1991). Eigenfaces for recognition. *Journal of Cognitive Neuroscience*, 3(1), 71–86. https://doi.org/10.1162/jocn.1991.3.1.71
- **tier:** deep
- **level:** UG
- **why:** PCA applied to face images gives "eigenfaces": a few basis images whose combinations reconstruct and recognize faces. It is the most famous visual demonstration that high-dimensional data often lies near a low-dimensional subspace.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1162/jocn.1991.3.1.71

#### vonluxburg-2007-spectralclustering
- **type:** paper
- **citation:** von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing*, 17(4), 395–416. https://doi.org/10.1007/s11222-007-9033-z
- **tier:** deep
- **level:** grad
- **why:** This is the standard tutorial on graph Laplacians (unnormalized and normalized) and on why their bottom eigenvectors reveal clusters. It derives the result from three viewpoints: relaxed graph cuts, random walks, and perturbation theory. It is the most direct link from linear algebra to community detection.
- **focus:** sections "Graph Laplacians and their basic properties", "Spectral Clustering Algorithms", "Graph cut point of view", "Random walks point of view", "Practical details".
- **access:** free: https://arxiv.org/pdf/0711.0189
- **verified:** https://arxiv.org/abs/0711.0189 ; https://api.crossref.org/works/10.1007/s11222-007-9033-z

#### spielman-2025-sagt
- **type:** book
- **citation:** Spielman, D. A. (2025). *Spectral and Algebraic Graph Theory* (incomplete draft, dated April 2, 2025). Yale University, author's website.
- **tier:** deep
- **level:** grad
- **why:** This book grew out of Spielman's Yale spectral graph theory lecture notes. It teaches graphs through their matrices, using physical metaphors (springs, resistor networks, random walks) and theorems such as Courant–Fischer, Perron–Frobenius, and Cheeger's inequality. It is the deepest free text connecting eigenvalues to network structure, partitioning, and fast Laplacian solvers.
- **focus:** Part I chs. 1–4 (incl. 2 "Eigenvalues and Optimization: The Courant-Fischer Theorem", 3 "The Laplacian and Graph Drawing", 4 "Adjacency matrices, Eigenvalue Interlacing, and the Perron-Frobenius Theorem"); 10 "Random Walks on Graphs"; 11 "Walks, Springs, and Resistor Networks"; 20 "Graph Partitioning"; 21 "Cheeger's Inequality"; 23 "Spectral Partitioning in a Stochastic Block Model".
- **access:** free: https://www.cs.yale.edu/homes/spielman/sagt/sagt.pdf
- **verified:** https://www.cs.yale.edu/homes/spielman/sagt/

#### mikolov-2013-regularities
- **type:** paper
- **citation:** Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic regularities in continuous space word representations. In *Proceedings of NAACL-HLT 2013* (pp. 746–751). Association for Computational Linguistics.
- **tier:** deep
- **level:** UG
- **why:** This paper shows that learned word vectors encode relations as roughly constant *offsets*, so analogies can be solved by vector arithmetic (king − man + woman ≈ queen) and cosine similarity. It is the founding demonstration of "meaning as geometry" behind the linear-representation ideas in LLM interpretability. It cross-references the LLM field.
- **focus:** whole (6 pages)
- **access:** free: https://aclanthology.org/N13-1090.pdf
- **verified:** https://aclanthology.org/N13-1090/

## Concept spine
- **vector** — an arrow or a list of numbers; anything you can add and scale (HS)
- **linear combination** — a weighted sum of vectors; every Ax is a linear combination of the columns of A (HS)
- **span** — all linear combinations of a set of vectors; the "reachable" subspace (HS)
- **linear independence** — no vector in the set is a combination of the others; nothing is redundant (UG)
- **basis** — an independent set that spans; a coordinate system (UG)
- **dimension** — the number of vectors in any basis; degrees of freedom (UG)
- **linear map / transformation** — a function that preserves addition and scaling; grid lines stay parallel and evenly spaced (HS)
- **matrix as transformation** — the columns of A are where the basis vectors land (HS)
- **matrix multiplication as composition** — AB means "do B, then A" (HS)
- **determinant** — the signed factor by which a map scales area or volume; zero means space is flattened (HS)
- **inverse matrix** — the map that undoes A; exists iff det ≠ 0 (UG)
- **column space (range)** — all outputs Ax; where the map can reach (UG)
- **null space (kernel)** — all inputs sent to zero; what the map destroys (UG)
- **rank** — the dimension of the column space; how many independent directions survive (UG)
- **rank–nullity (Fundamental Theorem of Linear Maps)** — dim V = dim null T + dim range T (UG)
- **four fundamental subspaces** — column space, null space, row space, and left null space, which come in orthogonal pairs (UG)
- **rank-one matrix / outer product** — uvᵀ, a single column pattern times a single row pattern; the building block of low-rank structure (UG)
- **dot (inner) product** — Σxᵢyᵢ; measures alignment and induces length and angle (HS)
- **cosine similarity** — the inner product of normalized vectors; the angle between them, the standard similarity in embeddings (UG)
- **norm** — a size of a vector or matrix (ℓ2, ℓ1, Frobenius, spectral) (UG)
- **orthogonality** — inner product zero; independent directions that do not interfere (UG)
- **orthonormal basis / orthogonal matrix** — perpendicular unit vectors; QᵀQ = I, rotations and reflections that preserve length (UG)
- **Gram–Schmidt and QR** — turning any basis into an orthonormal one; A = QR (UG)
- **projection** — the closest point in a subspace; P = A(AᵀA)⁻¹Aᵀ (UG)
- **least squares** — solving an overdetermined Ax ≈ b by projecting b onto the column space (normal equations AᵀAx = Aᵀb) (UG)
- **change of basis** — the same vector or map described in different coordinates; A ↦ P⁻¹AP (UG)
- **eigenvector / eigenvalue** — a direction the map only stretches, Av = λv (UG)
- **diagonalization** — A = XΛX⁻¹; in the eigenbasis the map is just independent scalings, so Aᵏ is easy (UG)
- **characteristic polynomial** — det(A − λI); its roots are the eigenvalues (UG)
- **spectral theorem** — real symmetric (self-adjoint) matrices have real eigenvalues and an orthonormal eigenbasis, S = QΛQᵀ (UG)
- **positive (semi)definite matrix** — xᵀSx ≥ 0; covariance matrices, Gram matrices, and Laplacians are all of this kind (UG)
- **quadratic form** — xᵀSx; its level sets are ellipsoids whose axes are eigenvectors (UG)
- **singular value decomposition (SVD)** — A = UΣVᵀ; every matrix is rotate, then scale, then rotate (UG)
- **Eckart–Young theorem** — the truncated SVD is the best rank-k approximation (UG)
- **pseudoinverse** — A⁺ = VΣ⁺Uᵀ; the minimum-norm least-squares solution (UG)
- **principal component analysis** — the SVD of centred data; directions of maximal variance and best-fitting subspaces (UG)
- **covariance matrix** — XᵀX/(n−1) for centred X; second-order structure of the data (UG)
- **Rayleigh quotient** — xᵀSx / xᵀx; its max and min are the extreme eigenvalues (Courant–Fischer) (grad)
- **power iteration** — repeatedly applying A to find the dominant eigenvector; how PageRank is computed (UG)
- **Markov (stochastic) matrix** — non-negative columns summing to 1; the steady state is the eigenvector for eigenvalue 1 (UG)
- **Perron–Frobenius theorem** — positive matrices have a unique positive dominant eigenvector; guarantees well-defined PageRank and eigenvector centrality (grad)
- **adjacency matrix** — Aᵢⱼ = 1 if i links to j; (Aᵏ)ᵢⱼ counts walks of length k (UG)
- **incidence matrix** — edges × nodes with ±1 entries; a graph as a difference operator (UG)
- **graph Laplacian** — L = D − A = BᵀB; its quadratic form Σ(xᵢ − xⱼ)² measures how "unsmooth" a signal is on a network (grad)
- **Fiedler vector / algebraic connectivity** — the eigenvector of the second-smallest Laplacian eigenvalue; splits a graph into communities (grad)
- **eigenvector centrality** — a node's importance is proportional to the sum of its neighbours' importance; the dominant eigenvector of A (grad)
- **Katz–Bonacich centrality** — (I − βA)⁻¹ counts all walks with decay β (grad)
- **condition number** — σ_max/σ_min; how much input errors are amplified in solving Ax = b (grad)
- **numerical stability** — whether an algorithm's rounding errors stay small (e.g., Householder QR vs. classical Gram–Schmidt) (grad)
- **Krylov subspace methods** — Arnoldi, Lanczos, and conjugate gradients; solving huge sparse problems using only matrix–vector products (grad)

## Canonical instances
- **PageRank as an eigenvector** — Web importance is the eigenvalue-1 eigenvector of the damped Google matrix, found by power iteration — bryan-2006-eigenvector, brin-1998-anatomy
- **Rotation vs shear vs projection** — a rotation preserves lengths (det 1), a shear preserves area but tilts the grid (det 1, one eigen-direction), and a projection flattens space (det 0) — sanderson-2016-essence
- **Determinant as area scaling** — det = 0 exactly when the transformation squashes the plane onto a line — sanderson-2016-essence
- **Least squares as orthogonal projection** — the fitted values are the shadow of y on the column space, and the residual is perpendicular to it — strang-2023-introduction, deisenroth-2020-mml
- **Pearson's line of closest fit** — perpendicular-distance fitting (PCA) vs vertical-distance fitting (regression) gives different lines through the same cloud — pearson-1901-closestfit
- **SVD image compression** — keeping the top k singular triplets of an image matrix gives the best rank-k picture — eckart-1936-lowrank, strang-2010-mit1806
- **Eigenfaces** — a handful of principal-component "ghost faces" reconstructs and recognizes thousands of faces — turk-1991-eigenfaces
- **Latent semantic analysis** — truncated SVD of a term–document matrix places "car" and "automobile" near each other without either word co-occurring with the other — deerwester-1990-lsa
- **king − man + woman ≈ queen** — semantic relations appear as roughly parallel vector offsets in embedding space — mikolov-2013-regularities
- **Fibonacci via eigenvalues** — diagonalizing the Fibonacci step matrix gives the closed form with powers of the golden ratio (the book's cover equation; Exercise 21 in Section 5D) — axler-2024-ladr
- **Markov chain steady state** — powers of a Markov matrix converge to the eigenvalue-1 eigenvector; the second eigenvalue sets the speed — strang-2010-mit1806, strang-2018-matrixmethods
- **Incidence matrices and Kirchhoff's laws** — a network's incidence matrix encodes conservation laws, and BᵀB is the graph Laplacian — strang-2010-mit1806, strang-2018-matrixmethods
- **Spectral graph partitioning** — the sign pattern of the Fiedler vector cuts a graph into two communities, including planted partitions in a stochastic block model — vonluxburg-2007-spectralclustering, spielman-2025-sagt
- **Bonacich's sign of β** — the same formula ranks central brokers (β > 0) or powerful exchangers with weak partners (β < 0) — bonacich-1987-power

## Bridges
- [same-math] Katz–Bonacich centrality (I − βA)⁻¹ ↔ economics & finance: Leontief input–output inverse (I − A)⁻¹ — both are the Neumann series Σβᵏ Aᵏ, summing effects that propagate along chains of links.
- [same-math] Markov matrix steady state / power iteration ↔ complex systems: random walks and stationary distributions on networks — PageRank is literally the stationary distribution of a damped random walk.
- [same-math] graph Laplacian and powers of a row-stochastic matrix ↔ communication theory: DeGroot consensus model x(t+1) = Wx(t) — whether and how fast opinions converge is set by the eigenvalues of W.
- [same-math] least squares with an ℓ2 penalty (ridge) ↔ Bayesian theory & causal inference: MAP estimate under a Gaussian prior — identical normal equations (AᵀA + λI)x = Aᵀb; OLS is projection onto the column space.
- [same-math] covariance eigendecomposition and determinant ↔ information theory: differential entropy of a multivariate Gaussian, ½ log det(2πeΣ) — the log-volume of the covariance ellipsoid.
- [same-math] linear programming duality ↔ decision & game theory: two-person zero-sum games solved by LP (minimax = LP duality; Strang ILA6 §9.4; 18.065 Lecture 24).
- [same-math] inner products, cosine similarity and vector offsets ↔ LLMs: attention scores QKᵀ and the linear-representation hypothesis — attention scores literally are matrix products, but the claim that concepts are linear directions is an empirical finding, not a theorem.
- [structural-analogy] low-rank factorization / PCA of a votes matrix ↔ political science: ideal-point scaling of roll calls — legislators embedded in a few latent dimensions, though NOMINATE-type models are not plain SVD.
- [metaphor] change of basis (same object, different coordinates) ↔ analytic philosophy: sense vs reference — one invariant thing, many descriptions. This is a helpful metaphor, not shared mathematics.
