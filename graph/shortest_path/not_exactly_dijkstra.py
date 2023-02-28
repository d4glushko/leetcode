from typing import List
import heapq

class Target:
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    #O (N + ElogN), where N - number of vertices, E - number of edges
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i + 1:{} for i in range(n)}

        for source, target, time in times:
            adj_list[source][target] = time

        visited = {k: (0, k)}
        pq = [Target(k, 0)]
        heapq.heapify(pq)
        while pq:
            cur_el = heapq.heappop(pq)
            # for dijkstra: visited[cur_el] = True
            for target, cost in adj_list[cur_el.target].items():
                new_cost = cur_el.cost + cost
                if target not in visited or new_cost < visited[target][0]: # for dijkstra no need to revisit by new_cost < visited...
                    visited[target] = (new_cost, cur_el.target)
                    heapq.heappush(pq, Target(target, new_cost))

        if len(visited) < n:
            return -1

        res = 0
        for target, visited_item in visited.items():
            if visited_item[0] > res:
                res = visited_item[0]

        return res
