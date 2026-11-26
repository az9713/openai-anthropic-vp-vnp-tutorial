"""Numeric check of the hub-shift step used in both proofs (tutorial Part B, step 5).

Layout from the Anthropic paper, Section 2.3: complete graph on k nodes, one wire
per edge. For a < b the end (a,b) sits at +e_a/2 and the end (b,a) at -e_a/2, so
each wire has length 1. For a balanced node set S, every end at a node of S is
routed to hub o_S, every other end to hub o_S'. With both hubs at the origin the
routing costs k(k-1)/2, the same as the wires. Shifting the hubs by eta along the
sum vector of the S-side ends makes the routing shorter.
"""
import itertools
import math


def check(k, eta):
    worst = None
    for size in range(math.ceil(k / 3), (2 * k) // 3 + 1):
        for S in itertools.combinations(range(k), size):
            S = set(S)
            ends = []  # (position vector, True if the end is at a node of S)
            for a in range(k):
                for b in range(a + 1, k):
                    pos = [0.0] * k
                    neg = [0.0] * k
                    pos[a], neg[a] = 0.5, -0.5
                    ends.append((pos, a in S))   # end (a,b) at node a
                    ends.append((neg, b in S))   # end (b,a) at node b
            total = [sum(p[i] for p, in_s in ends if in_s) for i in range(k)]
            norm = math.sqrt(sum(x * x for x in total))
            hub = [eta * x / norm for x in total]
            routed = 0.0
            for p, in_s in ends:
                sign = 1 if in_s else -1
                routed += math.dist(p, [sign * h for h in hub])
            saving = k * (k - 1) / 2 - routed
            if worst is None or saving < worst[0]:
                worst = (saving, norm, sorted(S))
    return worst


if __name__ == "__main__":
    for k in (6, 9, 12):
        wires = k * (k - 1) / 2
        best = None
        for t in (0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
            eta = t / math.sqrt(k)
            saving, norm, S = check(k, eta)
            if best is None or saving > best[0]:
                best = (saving, t, eta, norm, S)
        saving, t, eta, norm, S = best
        print(f"k={k} wires={wires:.0f} best eta={t}/sqrt(k)={eta:.3f} "
              f"worst balanced S={S} sum-norm={norm:.3f} "
              f"(paper bound k^1.5/9={k**1.5/9:.3f}) "
              f"saving={saving:.3f} = {saving/k:.3f}*k, hub gap={2*eta:.3f}")
        assert norm >= k ** 1.5 / 9, "sum vector shorter than the paper's bound"
        assert saving > 0, "shifted hubs must be cheaper than hubs at the origin"
