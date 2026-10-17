# Exercise 2: The six-bank network (W5) in 20 lines, then a random experiment (ours).
import numpy as np

def cascade(capital, edges, seeds, lgd=0.8, kappa=1.0):
    """edges: {(j, i): w} means bank j is exposed to bank i (j lent w to i).
    Rule: bank j fails when the sum of lgd * w over its failed borrowers i reaches kappa * capital[j].
    Returns {bank: round in which it failed}; seeds fail in round 0."""
    failed = {b: 0 for b in seeds}
    frontier = list(seeds)
    loss = {b: 0.0 for b in capital}
    r = 0
    while frontier:
        r += 1
        for (j, i), w in edges.items():
            if i in frontier and j not in failed:
                loss[j] += lgd * w
        frontier = [b for b in capital if b not in failed and loss[b] >= kappa * capital[b] - 1e-12]
        for b in frontier:
            failed[b] = r
    return failed

# W5 as in the post: (exposed bank, failing bank): size
cap = {"X1": 10, "X2": 10, "X3": 10, "Y1": 10, "Y2": 9, "Y3": 11}
edg = {("Y1", "X1"): 5, ("Y1", "X2"): 5, ("Y1", "X3"): 5, ("Y2", "X3"): 5,
       ("Y2", "Y1"): 10, ("Y3", "Y1"): 5, ("Y3", "Y2"): 10}

if __name__ == "__main__":
    print("one bank:", len(cascade(cap, edg, ["X1"])), "of 6")             # expect 1
    print("two X banks:", len(cascade(cap, edg, ["X1", "X2"])), "of 6")      # expect 2
    print("three X banks:", len(cascade(cap, edg, ["X1", "X2", "X3"])), "of 6")  # expect 6
    print("three, capital x1.5:", len(cascade(cap, edg, ["X1", "X2", "X3"], kappa=1.5)), "of 6")  # expect 3

    # Random experiment (ours, a toy): 30 banks, each lent to 3 random others (size 5).
    # Compare ONE random bank failing with THREE random "same-model" banks failing together.
    rng = np.random.default_rng(1)
    def random_net(n=30):
        capital = {k: rng.uniform(6, 14) for k in range(n)}
        edges = {}
        for j in range(n):
            for i in rng.choice([k for k in range(n) if k != j], 3, replace=False):
                edges[(j, int(i))] = 5.0
        return capital, edges
    def mean_size(k_seeds, kappa, nets=300):
        sizes = []
        for _ in range(nets):
            capital, edges = random_net()
            seeds = [int(s) for s in rng.choice(30, k_seeds, replace=False)]
            sizes.append(len(cascade(capital, edges, seeds, kappa=kappa)))
        return np.mean(sizes)
    for kappa in (1.0, 1.25, 1.5, 2.0):
        print(f"kappa={kappa}: mean failures with 1 seed = {mean_size(1, kappa):.2f}, with 3 seeds = {mean_size(3, kappa):.2f}")
    # TODO for you: find the kappa that halves the mean cascade of the 3-seed case. Label the result "toy, ours".
