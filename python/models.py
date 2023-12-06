import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


# Create NetworkX object of clique graph
def create_simple_clique_graph(clique_size, num_cliques_per_node, N):
    nodes = []
    cliques = []
    num_cliques = int((num_cliques_per_node / clique_size) * N)
    for i in range(N):
        curr_node = {"id": i, "remaining_cliques": num_cliques_per_node, "cliques": []}
        nodes.append(curr_node)

    for i in range(num_cliques):
        curr_clique = {"id": i, "remaining_nodes": clique_size, "nodes": []}
        cliques.append(curr_clique)

    nodes_to_connect = [nd["id"] for nd in nodes if nd["remaining_cliques"] != 0]
    cliques_to_connect = [cq["id"] for cq in cliques if cq["remaining_nodes"] != 0]
    failures = 0
    while True:
        nd = random.sample(nodes_to_connect, 1)[0]
        cq = random.sample(nodes_to_connect, 1)[0]
        # Check if clique already contains node
        if nd in cliques[cq]["nodes"]:
            failures += 1
            if failures > 1000:
                G = create_simple_clique_graph(clique_size, num_cliques_per_node, N)
                return G
            continue

        nodes[nd]["cliques"].append(cq)
        nodes[nd]["remaining_cliques"] -= 1
        cliques[cq]["nodes"].append(nd)
        cliques[cq]["remaining_nodes"] -= 1

        if nodes[nd]["remaining_cliques"] == 0:
            nodes_to_connect.remove(nd)

        if cliques[cq]["remaining_nodes"] == 0:
            cliques_to_connect.remove(cq)

        if len(nodes_to_connect) == 0:
            break

    # Build graph
    A = np.zeros((N, N))
    for cq in cliques:
        for nd1 in cq["nodes"]:
            for nd2 in cq["nodes"]:
                if nd1 != nd2:
                    A[nd1, nd2] = 1

    G = nx.from_numpy_matrix(A)
    return G
