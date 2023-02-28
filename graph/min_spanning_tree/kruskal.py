from typing import List

class DisjSet:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, el):
        if el == self.roots[el]:
            return el

        self.roots[el] = self.find(self.roots[el])
        return self.roots[el]

    def union(self, el1, el2):
        root1 = self.find(el1)
        root2 = self.find(el2)

        if root1 == root2:
            return False

        if self.ranks[root1] > self.ranks[root2]:
            self.roots[root2] = root1
        elif self.ranks[root2] > self.ranks[root1]:
            self.roots[root1] = root2
        else:
            self.roots[root1] = root2
            self.ranks[root2] += 1
        return True

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return f"{self.point1}-{self.point2}:{self.cost}"

    def __repr__(self):
        return f"{self.point1}-{self.point2}:{self.cost}"

class Solution:
    def distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    # O(ElogE), where E - number of edges
    def min_cost_connect_points_kruskal(self, points: List[List[int]]) -> int:
        res = 0

        vertices_count = len(points)
        edges = []
        for i, point_1 in enumerate(points):
            for j in range(i + 1, len(points)):
                point_2 = points[j]
                new_edge = Edge(i, j, self.distance(point_1[0], point_1[1], point_2[0], point_2[1]))
                edges.append(new_edge)

        edges.sort(key = lambda edge: edge.cost)
        disj_set = DisjSet(vertices_count)
        used = 0
        for edge in edges:
            if disj_set.union(edge.point1, edge.point2):
                res += edge.cost
                used += 1

            if used == vertices_count - 1:
                break

        return res
        