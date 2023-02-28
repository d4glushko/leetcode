import heapq
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
        visited = [False for _ in range(vertices_count)]

        edges = []
        for i in range(1, vertices_count):
            new_edge = Edge(
                0,
                i,
                self.distance(
                    points[0][0],
                    points[0][1],
                    points[i][0],
                    points[i][1]
                )
            )
            edges.append(new_edge)

        heapq.heapify(edges)
        left = vertices_count - 1
        visited[0] = True
        while edges and left > 0:
            edge = heapq.heappop(edges)
            if not visited[edge.point2]:
                visited[edge.point2] = True
                res += edge.cost
                left -= 1

                for j in range(vertices_count):
                    if not visited[j]:
                        new_edge = Edge(
                            edge.point2,
                            j,
                            self.distance(
                                points[edge.point2][0],
                                points[edge.point2][1],
                                points[j][0],
                                points[j][1]
                            )
                        )
                        heapq.heappush(edges, new_edge)

        return res
        