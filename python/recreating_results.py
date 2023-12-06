import matplotlib.pyplot as plt
from simulate import SIR
from models import create_simple_clique_graph
import networkx as nx
import numpy as np
import tqdm
from theoretical import node_risk


def main():
    # N = 20
    # k = 20
    # # erdos renyi network
    # G = nx.erdos_renyi_graph(N, k / N)
    n = 3
    m = 3
    N = 900
    iterations = 1000
    T = np.arange(0.1, 0.4, 0.1)
    empirical_node_risk = np.zeros(len(T))
    for i, t in tqdm.tqdm(enumerate(T), total=len(T)):
        num_epidemics = 0
        for k in range(iterations):
            G = create_simple_clique_graph(n, m, N)
            sup, inf, rec = SIR(G, 1, t, N)
            if rec[-1] <= 100:
                continue
            else:
                num_epidemics += 1
                empirical_node_risk[i] += rec[-1]/N
        empirical_node_risk[i] /= num_epidemics

    theoretical_risk = []
    for t in T:
        theoretical_risk.append(node_risk(n, m, t))

    plt.plot(T, theoretical_risk)
    plt.plot(T, empirical_node_risk)
    plt.show()
    # T = np.arange(len(sup))
    # plt.plot(T, sup, label="susceptible")
    # plt.plot(T, inf, label="infected")
    # plt.plot(T, rec, label="recovered")
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
