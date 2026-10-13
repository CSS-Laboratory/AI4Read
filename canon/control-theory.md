---
field: Control theory & cybernetics
slug: control-theory
layer: foundation
compiled: 2026-10-13
---
# Control theory & cybernetics — Canon

## Scope
This catalog covers the science of steering: how a system that senses its own output and acts on the error (feedback) can hold a goal against disturbances, how it can estimate a hidden state from noisy measurements, and how it can choose actions that are optimal over time. It has five strands: (1) feedback and cybernetics, from Maxwell's governor through Wiener and Ashby to a modern textbook; (2) state-space models, controllability/observability and estimation, with the Kalman filter as the bridge to Bayesian inference; (3) optimal control and dynamic programming (Bellman, the maximum principle, LQR); (4) reinforcement learning read as control when the model is unknown; and (5) control ideas in biology, cognition and society (homeostasis, motor control, the thermostatic public, monetary-policy rules, time inconsistency, the "control revolution"). The boundary with the complex-systems canon is deliberate: there (Strogatz) the dynamics are taken as given and we ask how they behave; here the focus is on the *input*: feedback, estimation and optimal action. Robust and H-infinity control, nonlinear and adaptive control theory, and deep-RL engineering are left out. The selection was triangulated against Caltech CDS 110 (Spring 2024; textbook Åström & Murray, weekly topics from state feedback and Kalman filtering to PID), Stanford AA 203 *Optimal and Learning-Based Control* (Spring 2026; calculus of variations, Pontryagin, DP/LQR, HJB, MPC, RL), Berkeley CS 285 *Deep Reinforcement Learning* (Spring 2026; policy gradients, model-based RL, IRL, control as inference), and Boyd's archived Stanford EE263. Wiener also appears in the communication-theory canon; Bayesian inverse planning (Baker et al. 2009) lives in the theory-of-mind canon.

## Canon

### Strand: Feedback & cybernetics

#### maxwell-1868-governors
- **type:** paper
- **citation:** Maxwell, J. C. (1868). *On Governors*. Proceedings of the Royal Society of London, 16, 270–283. https://doi.org/10.1098/rspl.1867.0055
- **tier:** deep
- **level:** UG
- **why:** The founding paper of control theory. Maxwell takes the steam-engine governor, a device that seemed to be pure engineering craft, linearizes its motion, and shows that whether it settles down or "hunts" (oscillates) depends on the roots of a polynomial. That move, stability as a property of characteristic roots, is still the core of the field.
- **focus:** whole (14 pages; the opening classification of governors and the stability conditions are the essentials)
- **access:** free: https://archive.org/download/paper-doi-10_1098_rspl_1867_0055/paper-doi-10_1098_rspl_1867_0055.pdf
- **verified:** https://api.crossref.org/works/10.1098/rspl.1867.0055 ; https://archive.org/metadata/paper-doi-10_1098_rspl_1867_0055 (public-domain mark)

#### wiener-1948-cybernetics
- **type:** book
- **citation:** Wiener, N. (1948). *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press (2nd ed. 1961; MIT Press reissue 2019, ISBN 9780262537841).
- **tier:** deep
- **level:** grad
- **why:** The book that named the field and claimed that control and communication are one subject across machines, animals and societies. Its central idea is that purposeful behavior is negative feedback driven by information about error. Much of it is heavy, dated mathematics, so read it for the framing and the history (anti-aircraft prediction, the nervous system, society) rather than for technique.
- **focus:** whole, skimming the mathematics (read for the framing)
- **access:** need-copy
- **translation:** 『サイバネティックス――動物と機械における制御と通信』池原止戈夫ほか訳, 岩波書店（岩波文庫）, 2011
- **verified:** https://openlibrary.org/isbn/9780262537841 ; https://ci.nii.ac.jp/ncid/BB05947863

#### ashby-1956-cybernetics
- **type:** book
- **citation:** Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall, London.
- **tier:** core
- **level:** HS
- **why:** The clearest textbook of cybernetics ever written. It needs only high-school mathematics, yet it states the deepest principles: systems as transformations, the black box, variety (number of possible states), and the law of requisite variety, which says that only variety in the regulator can absorb variety in the disturbances. It is the conceptual root of the "good regulator" theorem and of much systems thinking in the social sciences.
- **focus:** Ch. 4 The Machine with Input (incl. "Feedback"); Ch. 6 The Black Box; Ch. 7 Quantity of Variety; Ch. 10 Regulation in Biological Systems; Ch. 11 Requisite Variety; Ch. 12 The Error-Controlled Regulator
- **access:** free: http://pespmc1.vub.ac.be/books/IntroCyb.pdf (electronic edition published by Principia Cybernetica with permission of the Ashby estate)
- **translation:** 『サイバネティクス入門』篠崎武・山崎英三・銀林浩訳, 宇野書店, 1967
- **verified:** http://pespmc1.vub.ac.be/ASHBBOOK.html ; https://ci.nii.ac.jp/ncid/BN02212140

#### conant-1970-goodregulator
- **type:** paper
- **citation:** Conant, R. C., & Ashby, W. R. (1970). *Every good regulator of a system must be a model of that system*. International Journal of Systems Science, 1(2), 89–97. https://doi.org/10.1080/00207727008920220
- **tier:** deep
- **level:** grad
- **why:** A short theorem with a famous title: the simplest optimal regulator of a system must contain (be isomorphic to) a model of that system. It is the formal ancestor of the idea that brains, organizations and AI agents must carry internal models of what they control. Read it alongside Ashby's Ch. 11, and be careful: the theorem is narrower than its title suggests.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1080/00207727008920220

#### meadows-2008-thinking
- **type:** book
- **citation:** Meadows, D. H. (2008). *Thinking in Systems: A Primer* (D. Wright, Ed.). Chelsea Green Publishing, White River Junction, VT.
- **tier:** core
- **level:** HS
- **why:** The best non-mathematical on-ramp: stocks, flows, balancing (negative) and reinforcing (positive) feedback loops, and delays, explained with everyday examples. It also gives the vocabulary that policy and sustainability researchers use (system traps, leverage points). Use it to build intuition before the equations, and as a check on whether you can explain a model in plain words.
- **focus:** Ch. 1 The Basics; Ch. 2 A Brief Visit to the Systems Zoo; Ch. 5 System Traps . . . and Opportunities; Ch. 6 Leverage Points—Places to Intervene in a System
- **access:** need-copy
- **translation:** 『世界はシステムで動く――いま起きていることの本質をつかむ考え方』枝廣淳子訳, 英治出版, 2015
- **verified:** https://libcat.mcphs.edu/Record/p2360990/TOC ; https://www.obalkyknih.cz/file/toc/302307/pdf ; https://ci.nii.ac.jp/ncid/BB17880023

#### astrom-2021-feedbacksystems
- **type:** book
- **citation:** Åström, K. J., & Murray, R. M. (2021). *Feedback Systems: An Introduction for Scientists and Engineers* (2nd ed.). Princeton University Press. ISBN 9780691193984.
- **tier:** core
- **level:** UG
- **why:** The standard modern introduction, written for scientists rather than only engineers, and the textbook of Caltech CDS 110. It covers why feedback works (disturbance rejection, robustness, tracking), state-space models, stability, reachability and observability, LQR, the Kalman filter, transfer functions, Bode/Nyquist, and PID, with examples from cruise control and bicycles to drug dosing and population dynamics. The figures are reproducible in Python with the `python-control` package.
- **focus:** Ch. 1 Introduction; Ch. 2 Feedback Principles (incl. 2.6 Positive Feedback); Ch. 4 Examples (4.1 Cruise Control, 4.2 Bicycle Dynamics); Ch. 5 Dynamic Behavior (5.3 Stability); Ch. 7 State Feedback (7.1 Reachability, 7.5 Linear Quadratic Regulators); Ch. 8 Output Feedback (8.1 Observability, 8.4 Kalman Filtering); Ch. 11 PID Control
- **access:** free: http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf
- **verified:** https://fbswiki.org/wiki/index.php/Main_Page ; https://openlibrary.org/search.json?q=feedback+systems+astrom+murray ; https://murray.cds.caltech.edu/Cds110

#### douglas-nd-classicalcontrol
- **type:** video
- **citation:** Douglas, B. (n.d.). *Classical Control Theory* [YouTube playlist, "Control Systems Lectures"]. https://www.youtube.com/playlist?list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk
- **tier:** reference
- **level:** HS
- **why:** Short (5–15 minute) whiteboard lectures by a practicing control engineer that build intuition for closed-loop control, transfer functions and Bode plots without heavy notation. They are a good audio-visual companion to Åström & Murray Ch. 1–2 and 9–11 for a learner starting from high-school math.
- **focus:** "Why Learn Control Theory"; "Closed Loop Control"; "Transfer Functions"; "Bode Plots, Introduction"; "Final Value Theorem and Steady State Error"
- **access:** free: https://www.youtube.com/playlist?list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk
- **verified:** https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk&format=json

### Strand: State space, estimation & controllability

#### kalman-1960-filtering
- **type:** paper
- **citation:** Kalman, R. E. (1960). *A New Approach to Linear Filtering and Prediction Problems*. Journal of Basic Engineering, 82(1), 35–45. https://doi.org/10.1115/1.3662552
- **tier:** core
- **level:** grad
- **why:** Introduces the Kalman filter: a recursive algorithm that keeps a running best estimate of a hidden state and its uncertainty, predicting forward with a model and correcting with each new noisy measurement. It replaced Wiener's frequency-domain filtering with a state-space formulation that computers could run, and it went on to guide Apollo, GPS and almost every tracking system. Read it after Welch & Bishop.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1115/1.3662552

#### kalman-1960-generaltheory
- **type:** paper
- **citation:** Kalman, R. E. (1960). *On the general theory of control systems*. IFAC Proceedings Volumes, 1(1), 491–502 (First IFAC World Congress, Moscow). https://doi.org/10.1016/S1474-6670(17)70094-8
- **tier:** reference
- **level:** grad
- **why:** The paper that introduced controllability and observability and showed their duality: whether inputs can steer every state, and whether outputs reveal every state, are mirror-image questions. These two concepts organize all of modern state-space control. Read the textbook treatments (Åström & Murray Ch. 7–8, Boyd's EE263 lectures) first; this is the historical source.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1016/S1474-6670(17)70094-8

#### welch-2004-kalmanintro
- **type:** paper
- **citation:** Welch, G., & Bishop, G. (1995; updated 2004). *An Introduction to the Kalman Filter*. Technical Report TR 95-041, Department of Computer Science, University of North Carolina at Chapel Hill.
- **tier:** core
- **level:** UG
- **why:** The most-used practical tutorial on the Kalman filter: 16 pages giving the predict–correct equations, the extended Kalman filter for nonlinear systems, and a worked example with real numbers. It is the fastest way to get the filter running in Python before reading Kalman or Särkkä.
- **focus:** The Discrete Kalman Filter; A Kalman Filter in Action: Estimating a Random Constant
- **access:** free: https://techreports.cs.unc.edu/papers/95-041.pdf
- **verified:** https://techreports.cs.unc.edu/papers/95-041.pdf (title page: TR 95-041, updated April 5, 2004)

#### sarkka-2023-bayesianfiltering
- **type:** book
- **citation:** Särkkä, S., & Svensson, L. (2023). *Bayesian Filtering and Smoothing* (2nd ed.). Cambridge University Press. ISBN 9781108926645.
- **tier:** deep
- **level:** grad
- **why:** Rebuilds the Kalman filter from Bayes' rule: filtering is just recursive Bayesian updating of a belief about a hidden state, and the Kalman filter is the exact answer when everything is linear and Gaussian. From there it climbs to extended/unscented filters, particle filters and smoothers. This is the bridge between control and the Bayesian canon, and the natural tool for tracking latent opinion or attention over time.
- **focus:** Ch. 1 What Are Bayesian Filtering and Smoothing?; Ch. 3 Batch and Recursive Bayesian Estimation; Ch. 6 Bayesian Filtering Equations and Exact Solutions; Ch. 7 Extended Kalman Filtering; Ch. 11 Particle Filtering; Ch. 12 Bayesian Smoothing Equations and Exact Solutions
- **access:** free: https://users.aalto.fi/~ssarkka/pub/bfs_book_2023_online.pdf (author pre-publication version, personal use)
- **verified:** https://users.aalto.fi/~ssarkka/ ; https://users.aalto.fi/~ssarkka/pub/bfs_book_2023_online.pdf (title and copyright pages)

#### boyd-2007-ee263
- **type:** course
- **citation:** Boyd, S. (2007–08). *EE263: Introduction to Linear Dynamical Systems* [lecture notes, homework and videos]. Stanford Engineering Everywhere, Stanford University.
- **tier:** reference
- **level:** UG
- **why:** The classic applied course connecting linear algebra to dynamics: eigenvalues as modes of motion, the matrix exponential, inputs and outputs, controllability as a least-norm problem, and observability as a least-squares problem. It shows that state estimation and control are linear algebra with a time index. (Stanford has since split it into a new EE263 and EE363; this archived version is the classic.)
- **focus:** Lectures "Autonomous linear dynamical systems"; "Eigenvectors and diagonalization"; "Linear dynamical systems with inputs and outputs"; "Controllability and state transfer"; "Observability and state estimation"
- **access:** free: https://see.stanford.edu/Course/EE263
- **verified:** https://see.stanford.edu/Course/EE263 ; https://see.stanford.edu/materials/lsoeldsee263/00-coverpage.pdf ; https://ee263.stanford.edu/

#### brunton-2017-controlbootcamp
- **type:** video
- **citation:** Brunton, S. L. (2017–). *Control Bootcamp* [YouTube playlist]. University of Washington. https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- **tier:** core
- **level:** UG
- **why:** A compact, code-along lecture series on modern state-space control: linear systems, stability and eigenvalues, controllability, pole placement, LQR, observability, and the Kalman filter, all worked on the inverted pendulum on a cart. It is the best single video path from "what is feedback" to "I can design an LQG controller", and it pairs naturally with Åström & Murray Ch. 5–8.
- **focus:** "Control Bootcamp: Overview"; "Linear Systems"; "Stability and Eigenvalues"; "Controllability"; "Inverted Pendulum on a Cart"; "Kalman Filter Example in Matlab"; "Cruise Control Example with Proportional-Integral (PI) control"
- **access:** free: https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- **verified:** https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m&format=json (first video dated Jan 23, 2017)

### Strand: Optimal control & dynamic programming

#### bellman-1957-dp
- **type:** book
- **citation:** Bellman, R. (1957). *Dynamic Programming*. Princeton University Press (Dover reprint 2003, ISBN 9780486428093).
- **tier:** core
- **level:** grad
- **why:** States the principle of optimality: an optimal plan has the property that, whatever the first decision, the remaining decisions must be optimal for the situation that results. This turns long-horizon decisions into a recursion on a "value function" (the Bellman equation), which underlies optimal control, economics' dynamic models, and all of reinforcement learning.
- **focus:** Book TOC not verified here. Start with Bellman's free 4-page precursor, "On the Theory of Dynamic Programming", PNAS 38(8), 716–719 (1952), https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/ (doi:10.1073/pnas.38.8.716), then read the book's opening chapters.
- **access:** need-copy
- **verified:** https://www.abebooks.com/9780486428093/Dynamic-Programming-Bellman-Richard-Ernest-0486428095/plp ; https://api.crossref.org/works/10.1073/pnas.38.8.716

#### liberzon-2012-calculus
- **type:** book
- **citation:** Liberzon, D. (2012). *Calculus of Variations and Optimal Control Theory: A Concise Introduction*. Princeton University Press. ISBN 9780691151878.
- **tier:** deep
- **level:** grad
- **why:** The cleanest path through the three classical routes to optimal control: calculus of variations, Pontryagin's maximum principle (optimality via "costates" or shadow prices), and the Hamilton–Jacobi–Bellman equation (optimality via a value function), ending with the linear-quadratic regulator. It replaces the hard-to-read original Pontryagin et al. (1962) and Kirk (1970) for a modern reader.
- **focus:** Ch. 2 Calculus of Variations; Ch. 3 From Calculus of Variations to Optimal Control; Ch. 4 The Maximum Principle; Ch. 5 The Hamilton-Jacobi-Bellman equation; Ch. 6 The Linear Quadratic Regulator
- **access:** free: https://liberzon.csl.illinois.edu/teaching/cvoc.pdf (author's 2011 pre-publication draft)
- **verified:** https://press.princeton.edu/titles/9760.html ; https://ci.nii.ac.jp/ncid/BB08140059

### Strand: Reinforcement learning as control

#### sutton-2018-rl
- **type:** book
- **citation:** Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. ISBN 9780262039246.
- **tier:** core
- **level:** UG
- **why:** The defining textbook of reinforcement learning: an agent learns to act by trial and error from a reward signal, without a known model of its world. It frames RL as approximate dynamic programming (Markov decision processes, value functions, Bellman equations) and adds the learning ideas (temporal-difference learning, Q-learning, policy gradients). The psychology and neuroscience chapters connect RL to conditioning and dopamine.
- **focus:** Ch. 1 Introduction (incl. 1.5 Tic-Tac-Toe, 1.7 Early History of Reinforcement Learning); Ch. 2 Multi-armed Bandits; Ch. 3 Finite Markov Decision Processes; Ch. 4 Dynamic Programming; Ch. 6 Temporal-Difference Learning; Ch. 13 Policy Gradient Methods; Ch. 14 Psychology; Ch. 15 Neuroscience
- **access:** free: http://incompleteideas.net/book/RLbook2020.pdf (CC BY-NC-ND 2.0, authors' site)
- **translation:** 『強化学習（第2版）』今井翔太ほか訳, 森北出版, 2022
- **verified:** https://opac.lib.gifu-u.ac.jp/opc/recordID/catalog.bib/BB27095177 ; https://ci.nii.ac.jp/ncid/BC17652365

#### recht-2019-tour
- **type:** paper
- **citation:** Recht, B. (2019). *A Tour of Reinforcement Learning: The View from Continuous Control*. Annual Review of Control, Robotics, and Autonomous Systems, 2, 253–279. https://doi.org/10.1146/annurev-control-053018-023825
- **tier:** core
- **level:** grad
- **why:** A control theorist's review of RL, written to give the control and RL communities a shared language. Its key move is to test RL methods on the simplest control problem with a known answer (LQR with unknown dynamics), and it finds that model-based approaches (estimate the model, then control) are often far more data-efficient than model-free ones. It is the best antidote to hype and the best bridge between strands 3 and 4.
- **focus:** sections "What is reinforcement learning?"; "Strategies for solving reinforcement learning problems"; "Model-based reinforcement learning"; "Approximate Dynamic Programming"; "Direct Policy Search"
- **access:** free: https://arxiv.org/pdf/1806.09460
- **verified:** https://api.crossref.org/works/10.1146/annurev-control-053018-023825 ; https://arxiv.org/abs/1806.09460

#### bertsekas-2026-rlcourse
- **type:** book
- **citation:** Bertsekas, D. P. (2026). *A Course in Reinforcement Learning* (2nd ed.). Athena Scientific, Belmont, MA. ISBN 978-1-886529-29-8.
- **tier:** reference
- **level:** grad
- **why:** The optimal-control view of RL from the author of the standard dynamic-programming texts. It reads AlphaZero-style systems as approximation in value space plus online lookahead (rollout), and links RL to Newton's method and model predictive control. It is a free substitute for his paid *Reinforcement Learning and Optimal Control* (2019) and *Dynamic Programming and Optimal Control* (Vol. I, 4th ed., 2017).
- **focus:** Ch. 1 Exact and Approximate Dynamic Programming (1.1 AlphaZero, Off-Line Training, and On-Line Play; 1.2 Deterministic Dynamic Programming; 1.5 Newton's Method - Linear Quadratic Problems; 1.7 Reinforcement Learning and Decision/Control); Ch. 2 Approximation in Value Space - Rollout Algorithms
- **access:** free: https://www.mit.edu/~dimitrib/RLCOURSECOMPLETE%202ndEDITION.pdf (author's site, free for instructional use)
- **verified:** https://www.mit.edu/~dimitrib/RLbook.html ; https://www.mit.edu/~dimitrib/dpbook.html

#### ng-2000-irl
- **type:** paper
- **citation:** Ng, A. Y., & Russell, S. (2000). *Algorithms for Inverse Reinforcement Learning*. Proceedings of the 17th International Conference on Machine Learning (ICML 2000), 663–670.
- **tier:** deep
- **level:** grad
- **why:** Turns RL around: given an agent's (presumed optimal) behavior, infer the reward function it is optimizing. It also shows the problem is ill-posed (many rewards, including zero reward, explain any behavior) and proposes margin-based fixes. This is the computational core shared with Bayesian inverse planning in theory of mind and with preference learning in LLM alignment.
- **focus:** whole
- **access:** free: https://ai.stanford.edu/~ang/papers/icml00-irl.pdf
- **verified:** https://mlanthology.org/icml/2000/ng2000icml-algorithms ; https://dblp.dagstuhl.de/rec/conf/icml/NgR00.html

### Strand: Control in biology, cognition & society

#### cannon-1932-wisdom
- **type:** book
- **citation:** Cannon, W. B. (1932). *The Wisdom of the Body*. W. W. Norton, New York.
- **tier:** deep
- **level:** HS
- **why:** Coins and popularizes "homeostasis": the body actively holds temperature, blood sugar, water and salt within narrow ranges through automatic corrective mechanisms. It is the biological template for every later "system that defends a set point". Its epilogue speculates on homeostasis in society, which anticipates cybernetic social science by fifteen years.
- **focus:** Epilogue "Relations of Biological and Social Homeostasis" (pp. 305–324 of the 1932 edition) plus the opening chapters
- **access:** need-copy
- **translation:** 『からだの知恵――この不思議なはたらき』舘鄰・舘澄江訳, 講談社学術文庫, 1981
- **verified:** https://wellcomecollection.org/works/aqyvkktu ; https://ndlsearch.ndl.go.jp/en/books/R100000038-I1127259 ; https://www.kodansha.co.jp/book/products/0000149938

#### powers-1973-behavior
- **type:** book
- **citation:** Powers, W. T. (1973). *Behavior: The Control of Perception*. Aldine, Chicago. (Revised text with added chapter "Emotion", 2005.)
- **tier:** reference
- **level:** UG
- **why:** Perceptual Control Theory: organisms do not control their actions, they act in order to keep their *perceptions* at reference values, and behavior is organized as a hierarchy of such control loops. The thesis reverses the stimulus–response picture and gives a concrete control-theoretic model of purpose. It is outside the mainstream, but it is a sharp lens for agent-based models of goal-directed actors.
- **focus:** Chapters "Feedback and Behavior"; "The Control-System Unit of Organization"; "A Hierarchy of Control Systems"; "Conflict and Control" (titles as in the revised text)
- **access:** need-copy
- **verified:** https://bemis.marmot.org/Record/.b17344773 ; https://livingcontrolsystems.com/bcp/content_bcp.html

#### todorov-2002-ofc
- **type:** paper
- **citation:** Todorov, E., & Jordan, M. I. (2002). *Optimal feedback control as a theory of motor coordination*. Nature Neuroscience, 5(11), 1226–1235. https://doi.org/10.1038/nn963
- **tier:** deep
- **level:** grad
- **why:** Shows that the brain's movement control looks like stochastic optimal feedback control (LQG-style estimation plus control), not like replaying a fixed planned trajectory. Its "minimal intervention principle" says that a good controller corrects only the deviations that hurt the task and lets harmless variability be. This is the landmark case of optimal control as a theory of cognition.
- **focus:** whole (the minimal intervention principle section is the payoff)
- **access:** free: https://roboti.us/lab/papers/TodorovNatNeurosci02.pdf (author's lab site)
- **verified:** https://api.crossref.org/works/10.1038/nn963

#### wlezien-1995-thermostat
- **type:** paper
- **citation:** Wlezien, C. (1995). *The Public as Thermostat: Dynamics of Preferences for Spending*. American Journal of Political Science, 39(4), 981 ff. https://doi.org/10.2307/2111666
- **tier:** core
- **level:** UG
- **why:** Models public opinion as a thermostat: the public's *relative* preference ("spend more" vs "spend less") falls when policy moves up and rises when it moves down, so opinion acts as negative feedback on policy. This made feedback a measurable, time-series idea in political science, and was extended in Soroka & Wlezien's *Degrees of Democracy* (Cambridge UP, 2010) into a theory of how media and institutions shape responsiveness. It is a direct template for studying opinion dynamics around crisis and climate policy.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works?query.bibliographic=Wlezien+The+Public+as+Thermostat ; https://www.icpsr.umich.edu/web/ICPSR/studies/1104 ; https://api.crossref.org/works/10.1017/cbo9780511804908

#### beniger-1986-controlrevolution
- **type:** book
- **citation:** Beniger, J. R. (1986). *The Control Revolution: Technological and Economic Origins of the Information Society*. Harvard University Press, Cambridge, MA.
- **tier:** deep
- **level:** UG
- **why:** A communication scholar's grand history: the "information society" arose because industrialization sped up material flows faster than anyone could steer them, and a "crisis of control" was answered by bureaucracy, telecommunications, mass media and computing. It reframes media and information technology as control technology, which is the most direct link from cybernetics to communication research.
- **focus:** whole
- **access:** need-copy
- **verified:** https://ci.nii.ac.jp/ncid/BA00705327 ; https://en.wikipedia.org/wiki/The_Control_Revolution

#### kydland-1977-rules
- **type:** paper
- **citation:** Kydland, F. E., & Prescott, E. C. (1977). *Rules Rather than Discretion: The Inconsistency of Optimal Plans*. Journal of Political Economy, 85(3), 473–491. https://doi.org/10.1086/260580
- **tier:** deep
- **level:** grad
- **why:** Argues that optimal control theory "is not the appropriate tool" for economic policy when people form expectations about future policy: a plan that is optimal today becomes tempting to abandon tomorrow (time inconsistency), so binding rules can beat case-by-case optimization. It marks the limit of control theory when the "plant" is a population of strategic agents, and it was cited in the 2004 Nobel prize.
- **focus:** whole (the introduction and the patent and flood-plain examples are the essentials)
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1086/260580

#### taylor-1993-discretion
- **type:** paper
- **citation:** Taylor, J. B. (1993). *Discretion versus policy rules in practice*. Carnegie-Rochester Conference Series on Public Policy, 39, 195–214. https://doi.org/10.1016/0167-2231(93)90009-L
- **tier:** deep
- **level:** UG
- **why:** Proposes the Taylor rule: set the short-term interest rate as a simple linear function of inflation's gap from target and output's gap from potential. In control terms, it is a feedback law for the economy, and it became the benchmark central banks are judged against. Read it as the practical answer to Kydland & Prescott: a simple, transparent rule rather than discretion.
- **focus:** whole
- **access:** free: https://web.stanford.edu/~johntayl/Papers/Discretion.PDF (scan on author's Stanford page)
- **verified:** https://api.crossref.org/works/10.1016/0167-2231(93)90009-L

## Concept spine
- **feedback** — using a measurement of a system's output to adjust its input (HS)
- **negative (balancing) feedback** — the correction opposes the deviation, pulling the system toward a goal (HS)
- **positive (reinforcing) feedback** — the correction amplifies the deviation, producing growth, runaway or switching (HS)
- **open loop vs closed loop** — acting on a fixed plan versus acting on measured results (HS)
- **feedforward** — acting on a measured disturbance before it affects the output (UG)
- **reference (set point)** — the target value the controller tries to hold (HS)
- **error signal** — the difference between the reference and the measured output (HS)
- **plant** — the system being controlled, as distinct from the controller (HS)
- **disturbance and noise** — unwanted inputs to the plant, and errors in the measurements (HS)
- **delay (dead time)** — lag between action and effect, the main cause of overshoot and oscillation (HS)
- **gain** — how strongly the controller reacts to a given error (HS)
- **stability** — small disturbances die out rather than grow (UG)
- **PID control** — proportional (react to error), integral (remove lasting offset), derivative (anticipate trend) (UG)
- **integral action** — accumulating past error so that steady-state error goes to zero (UG)
- **robustness** — feedback keeps performance good even when the plant model is wrong (UG)
- **transfer function** — input-to-output relation of a linear system in the frequency (Laplace) domain (UG)
- **Bode plot** — gain and phase of a system plotted against frequency (UG)
- **Nyquist criterion** — a graphical test of closed-loop stability from the open-loop frequency response (grad)
- **state** — the minimal set of numbers that, with future inputs, determines future behavior (UG)
- **state-space model** — dx/dt = Ax + Bu, y = Cx: dynamics, input and measurement as matrices (UG)
- **eigenvalues and modes** — a linear system is stable when every eigenvalue of A has negative real part (UG)
- **linearization** — approximating a nonlinear system near an equilibrium by its Jacobian (UG)
- **controllability (reachability)** — whether inputs can drive the system to any state (UG)
- **observability** — whether outputs reveal the entire internal state (UG)
- **duality** — controllability and observability are mathematically mirror images (grad)
- **state feedback / pole placement** — u = −Kx chosen to put the closed-loop eigenvalues where you want them (UG)
- **observer (state estimator)** — a model run in parallel and corrected by measurements to reconstruct hidden state (UG)
- **Kalman filter** — the optimal recursive estimator for linear systems with Gaussian noise: predict, then correct (UG)
- **Kalman gain** — the weight on a new measurement, set by how uncertain the prediction is relative to the sensor (UG)
- **LQR** — linear-quadratic regulator: the optimal state feedback for a quadratic cost on state and effort (grad)
- **separation principle (LQG)** — for linear-Gaussian problems you can design the estimator and the controller separately (grad)
- **model predictive control** — repeatedly solve a finite-horizon optimal control problem and apply only the first step (grad)
- **homeostasis** — active maintenance of internal variables within viable ranges (HS)
- **black box** — a system known only through its input–output behavior (HS)
- **variety** — the number of distinguishable states a system can take (HS)
- **law of requisite variety** — only variety in the regulator can absorb variety in the disturbances (UG)
- **good regulator theorem** — the simplest optimal regulator must contain a model of the system it regulates (grad)
- **perceptual control** — behavior is the means by which organisms keep perceptions at reference values (UG)
- **principle of optimality** — the tail of an optimal plan is optimal for the state it starts from (UG)
- **Bellman equation / value function** — the value of a state equals the best immediate payoff plus the value of where you land (UG)
- **Hamilton–Jacobi–Bellman equation** — the continuous-time Bellman equation, a PDE for the value function (grad)
- **Pontryagin maximum principle** — necessary conditions for optimality using costates (shadow prices) along the trajectory (grad)
- **Markov decision process** — states, actions, transition probabilities and rewards: the formal RL problem (UG)
- **policy** — a rule mapping states (or beliefs) to actions (UG)
- **exploration vs exploitation** — trying new actions to learn versus using the best-known action (HS)
- **temporal-difference learning / reward prediction error** — learn values from the gap between predicted and received reward plus next-step value (UG)
- **model-based vs model-free RL** — learn a model and plan with it, versus learn values or policies directly (UG)
- **inverse reinforcement learning (inverse optimal control)** — infer the reward that makes observed behavior optimal (grad)
- **minimal intervention principle** — an optimal controller corrects only deviations that matter for the task (grad)
- **time inconsistency** — a plan optimal today is not optimal to follow later, because expectations already responded to it (grad)

## Canonical instances
- **Watt's centrifugal governor** — spinning flyballs throttle the steam valve; Maxwell's analysis of when it "hunts" founded stability theory — maxwell-1868-governors
- **Black's negative-feedback amplifier** — trading raw gain for precision lets imperfect components build excellent telephone amplifiers — astrom-2021-feedbacksystems
- **Cruise control (PI)** — a car holds speed up and down hills; integral action removes the steady-state error that pure proportional control leaves — astrom-2021-feedbacksystems
- **Inverted pendulum on a cart** — an unstable system made stable by fast state feedback; the standard demonstration of controllability, LQR and Kalman filtering — brunton-2017-controlbootcamp
- **The bicycle** — the tilting bicycle behaves like an inverted pendulum that is kept upright by steering into the fall — astrom-2021-feedbacksystems
- **Kalman filter in Apollo 11** — the lunar module's guidance system fused a model with noisy measurements to estimate position — sarkka-2023-bayesianfiltering
- **The thermostatic water-bath** — Ashby's running example of a regulator: the bath holds temperature E inside the desired range despite room disturbances — ashby-1956-cybernetics
- **Homeostasis of temperature and blood sugar** — the body as a set of automatic regulators defending set points — cannon-1932-wisdom
- **The thermostatic public** — opinion asks for "less" after spending rises and "more" after it falls, a negative feedback loop on policy — wlezien-1995-thermostat
- **The Taylor rule** — interest rate = neutral rate + inflation + ½(inflation gap) + ½(output gap): a feedback law for the economy — taylor-1993-discretion
- **The flood plain** — government would like to forbid building on a flood plain, but once houses exist it is optimal to build dams, so people build anyway — kydland-1977-rules
- **Minimal-intervention reaching** — variability in arm movement is left uncorrected along task-irrelevant directions — todorov-2002-ofc
- **The k-armed bandit** — the cleanest exploration vs exploitation dilemma — sutton-2018-rl
- **Gridworld and pole-balancing** — toy MDPs where value iteration and TD learning can be watched step by step — sutton-2018-rl
- **LQR with unknown dynamics** — the simplest control problem used as a benchmark to compare model-based and model-free RL — recht-2019-tour

## Bridges
- [same-math] Kalman filter ↔ Bayesian theory & modeling: conjugate Gaussian updating — the predict–update cycle is Bayes' rule applied recursively to a linear-Gaussian state-space model (Särkkä Ch. 6).
- [same-math] stability of x' = Ax ↔ linear algebra: eigenvalues — a linear system is stable exactly when all eigenvalues of A have negative real part, and controllability is the rank of [B, AB, A²B, …].
- [same-math] linearization & stability of equilibria ↔ complex systems: linear stability analysis (Strogatz) — the same Jacobian-eigenvalue test; control adds the input u that can move those eigenvalues.
- [same-math] law of requisite variety ↔ information theory: entropy — Ashby states the law with Shannon entropy: outcome entropy cannot fall below disturbance entropy minus regulator entropy.
- [same-math] Bellman's principle of optimality ↔ decision & game theory: backward induction — finite-horizon dynamic programming is backward induction; with several agents it becomes subgame perfection.
- [same-math] inverse RL / inverse optimal control ↔ theory of mind: Bayesian inverse planning — inferring goals from actions by inverting an MDP planner; Baker et al. (2009) is the Bayesian version of the problem Ng & Russell pose.
- [same-math] policy-gradient RL ↔ large language models: RLHF — fine-tuning an LLM against a learned reward model is policy-gradient RL (Sutton & Barto Ch. 13 family) with a KL penalty, and the reward model is preference-based inverse RL.
- [structural-analogy] time inconsistency & policy rules ↔ economics & finance: central-bank credibility — the Taylor rule has the form of a proportional feedback law, but the "plant" reacts through expectations, which is why Kydland & Prescott limit what optimal control can do.
- [structural-analogy] thermostatic public ↔ political science: policy responsiveness and representation — opinion and policy form a negative feedback loop that can be estimated with time-series models.
- [metaphor] feedback, homeostasis, control ↔ communication theory: Craig's cybernetic tradition, Luhmann's systems theory, Beniger's control revolution — the vocabulary transfers to communication and society, but the equations usually do not.
