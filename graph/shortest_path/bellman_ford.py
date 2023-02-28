from typing import List

import sys

class Target:
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    # O(E * N), where N - number of vertices, E - number of edges
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        inbound_edges = {i + 1:{} for i in range(n)}

        for source, target, time in times:
            inbound_edges[target][source] = time

        cur_distances = [sys.maxsize for i in range(n)]
        cur_distances[k - 1] = 0

        for i in range(1, n):
            stop = True
            prev_distances = cur_distances.copy()
            for j in range(1, n + 1):
                if j == k:
                    continue
                for source, time in inbound_edges[j].items():
                    if prev_distances[source - 1] == sys.maxsize:
                        continue

                    new_time = prev_distances[source - 1] + time
                    if new_time < cur_distances[j - 1]:
                        cur_distances[j - 1] = new_time
                        stop = False

            if stop:
                break

        res = 0
        for distance in cur_distances:
            if distance == sys.maxsize:
                return -1
            if distance > res:
                res = distance

        return res
