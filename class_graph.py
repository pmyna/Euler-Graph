import numpy as np
import random as rd
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, k):
        self.knots = k
        self.edges = []
        self.backup = []

    def addEdge(self, u, v):
        self.edges.append([u, v])
        self.edges.sort()
        self.backup.append([u, v])
        self.backup.sort()

    def reset(self):
        self.edges = self.backup[:]

    def checkCircle(self):
        k = self.knots
        edges_count = np.array(self.edges).flatten()
        count = 0
        for x in range(1, (k + 1)):
            for y in range(len(edges_count)):
                if x == edges_count[y]:
                    count += 1
            if count % 2 != 0:
                return False
            count = 0
        return True

    def isUnique(self, np_cedges):
        *y, = map(list, {*map(tuple, np_cedges)})
        if len(np_cedges) == len(y):
            return True
        return False

    def findCircle(self, cpath):
        cedges = []
        if cpath[0] is None:
            cpath = []
        while cpath[-1] is not cpath[0] or len(cpath) <= 1:
            next_knot = rd.choice(range(self.knots + 1))
            knots = [cpath[-1], next_knot]
            for elem in self.edges:
                if set(knots) == set(elem):
                    cedges.append(elem)
                    cpath.append(next_knot)
                if cpath[-1] is cpath[0] and len(cpath) > 1:
                    break

        np_cedges = np.array(cedges)
        for i in np_cedges:
            i.sort()

        if self.isUnique(np_cedges):
            return cpath, cedges
        knot = [cpath[0]]
        return knot, None

    def checkKnot(self, cpath):
        np_edges = np.array(self.edges)
        available_knots = np.unique(np_edges)
        for i in range(1, len(cpath)):
            for j in range(len(available_knots)):
                if cpath[-i] == available_knots[j]:
                    knot = cpath[-i]
                    return knot, i
        return None, None

    def findEuler(self):
        start = rd.choice(range(1, self.knots))
        cpath = [start]  # current path
        epath = ["x"] # final euler path

        if self.checkCircle():
            position = 1
            while True:
                if not self.edges:
                    epath.insert(0, start)
                    epath.remove("x")
                    if epath[-1] != start:
                        epath.append(start)
                    self.reset()
                    return epath
                else:
                    while True:
                        if not self.edges:
                            break
                        cpath, cedges = self.findCircle(cpath)  # try a circle
                        if len(cpath) > 1 and cedges is not None:
                            # delete used edges
                            self.edges = [elem for elem in self.edges if elem not in cedges]
                            # append to euler pathway
                            cpath.pop(0)
                            for elem in cpath:
                                epath.insert(-position, elem)
                            # check for next knot
                            knot, position = self.checkKnot(cpath)
                            cpath = [knot]
        else:
            return "No Euler Circle found"

    def drawGraph(self):
        plot = nx.Graph()
        plot.add_edges_from(self.edges)
        nx.draw_networkx(plot, with_labels=True, node_color = "#ffffff", node_size=350, edge_color="#5f95ed", width=1.5)
        return plt.plot()
        plot.clear()