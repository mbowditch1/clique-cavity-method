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


def write_simple_clique_graph_to_rust(n=3, m=3, N=900):
    G = create_simple_clique_graph(n, m, N)
    file_name = f"simple_clique_graph_{n}_{m}_{N}.el"
    file_path = "../rust/resources/" + file_name
    print("mean degree: ", np.mean([G.degree(n) for n in G.nodes()]))
    nx.write_edgelist(G, file_path, data=False)


def write_erdos_to_rust(N=900, p=0.1, mean_degree=None):
    if mean_degree is not None:
        p = mean_degree / N
    G = nx.erdos_renyi_graph(N, p)
    print("mean degree: ", np.mean([G.degree(n) for n in G.nodes()]))
    file_name = f"erdos_renyi_{N}_{mean_degree}.el"
    file_path = "../rust/resources/" + file_name
    nx.write_edgelist(G, file_path, data=False)


if __name__ == "__main__":
    # main()
    # write_erdos_to_rust(N=900, mean_degree=3)
    write_simple_clique_graph_to_rust(n=6, m=4, N=900)
