# Exercise 3: Where does the share-m toy tip?  (post 02, Rung 5)
# gap(t+1) = gap(t) + A*m*(gap(t) - gap(t-1)) - G*(1-m)*gap(t), shock -1 after step 3.
import numpy as np

A, G = 1.5, 0.5

def run(m, steps=40, brk=None):
    p, q = 0.0, 0.0
    out = [0.0]
    for t in range(1, steps + 1):
        new = p + A * m * (p - q) - G * (1 - m) * p
        if brk: new = max(-brk, min(brk, new))     # circuit breaker: clamp the gap
        q, p = p, new
        if t == 3: p -= 1.0                          # the shock, applied after step 3
        out.append(p)
    return np.array(out)

def root_size(m):
    b, c = 1 + A * m - G * (1 - m), A * m           # x^2 - b x + c = 0
    return np.abs(np.roots([1, -b, c])).max()

if __name__ == "__main__":
    for m in (0.2, 0.67, 0.9):
        g = run(m)
        print(f"m={m}: root size {root_size(m):.3f}, largest up {g.max():.2f}, down {g.min():.2f}, final {g[-1]:.3f}")
    print("m=0.9 with breaker 3:", run(0.9, brk=3).round(2)[-6:])
    ms = np.linspace(0, 1, 101)
    sizes = np.array([root_size(m) for m in ms])
    print("first m with root size > 1:", ms[np.argmax(sizes > 1)], "  (theory: 1/A = %.3f)" % (1 / A))
    # TODO for you: plot sizes against m (matplotlib); change G and see if the tipping point moves.
