import networkx as nx
import numpy as np
import random


def SIR(G, Nb_inf_init, HM, N):
    """function that runs a simulation of an SIR model on a network.
    INPUT:
        G(networkx) : Graph
        Nb_inf_init : Initial number of infected people (nodes)
        HM(float) : Infection probability before recovering
        N(int): number of nodes (or people)
    """
    # setting initial conditions
    inf = [Nb_inf_init]
    sup = [N - Nb_inf_init]
    rec = [0]

    for u in G.nodes():
        G.nodes[u]["state"] = 0
        G.nodes[u]["neighbours"] = [n for n in G.neighbors(u)]
    init = random.sample(G.nodes(), Nb_inf_init)
    for u in init:
        G.nodes[u]["state"] = 1

    while True:
        sup.append(sup[-1])
        inf.append(inf[-1])
        rec.append(rec[-1])
        new_infected = []
        for u in G.nodes:
            # if not infected
            if G.nodes[u]["state"] == 0:
                # find infected neighbours
                for n in G.nodes[u]["neighbours"]:
                    if G.nodes[n]["state"] == 1:
                        if np.random.rand() < HM:
                            new_infected.append(u)
                            break

        for u in G.nodes:
            if G.nodes[u]["state"] == 1:
                # recover nodes
                G.nodes[u]["state"] = 2
                rec[-1] += 1

        inf[-1] += len(new_infected)
        inf[-1] -= inf[-2]
        sup[-1] -= len(new_infected)
        for n in new_infected:
            G.nodes[n]["state"] = 1

        if inf[-1] == 0:
            break

    return sup, inf, rec
