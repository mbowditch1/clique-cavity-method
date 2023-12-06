import math


def clique_transmission(n, s, T):
    # Base case
    if n < 3:
        return T

    prob = 1 - ((1 - T) ** s)
    sum = 0
    for q in range(1, n - s):
        sum += (
            clique_transmission(n - s, q, T)
            * math.comb(n - s - 1, q) * ((1 - T) ** (s * (n - s - q - 1)))
            * ((1 - ((1 - T) ** s)) ** q)
        )

    prob = prob + (((1 - T) ** s) * sum)
    return prob


def clique_risk_from_node(m, nd_from_cq):
    cq_from_nd = 1 - ((1 - nd_from_cq) ** (m - 1))
    return cq_from_nd


def node_from_clique(n, m, T):
    nd_from_cq = 1
    for N in range(5000):
        cq_from_nd = clique_risk_from_node(m, nd_from_cq)
        sum = 0
        for s in range(1, n):
            sum += (
                ((1 - cq_from_nd) ** (n - 1 - s))
                * (cq_from_nd**s)
                * math.comb(n - 1, s)
                * clique_transmission(n, s, T)
            )

        nd_from_cq = sum

    return nd_from_cq


def node_risk(n, m, T):
    return 1 - ((1 - node_from_clique(n, m, T)) ** m)
