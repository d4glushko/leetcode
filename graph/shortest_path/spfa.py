from collections import deque
from typing import List

class Target:
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    # O(E * N), where N - number of vertices, E - number of edges
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i + 1:{} for i in range(n)}

        for source, target, time in times:
            adj_list[source][target] = time

        visited = {k: 0}

        queue = deque()
        queue.append(k)

        while queue:
            cur_el = queue.popleft()
            for target, cost in adj_list[cur_el].items():
                new_cost = visited[cur_el] + cost
                if target not in visited or new_cost < visited[target]:
                    visited[target] = new_cost
                    queue.append(target)

        if len(visited) < n:
            return -1

        res = 0
        for target, cost in visited.items():
            if cost > res:
                res = cost

        return res
