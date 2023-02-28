from collections import deque
from typing import List

class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        outbound_vertices = [[] for _ in range(num_courses)]
        inbound_count = [0 for _ in range(num_courses)]
        res = []

        for second, first in prerequisites:
            outbound_vertices[first].append(second)
            inbound_count[second] += 1

        queue = deque()

        # O(V)
        for i in range(num_courses):
            if inbound_count[i] == 0:
                inbound_count[i] -= 1
                queue.append(i)
                res.append(i)

        # O(V + E)
        while queue:
            cur_el = queue.popleft()
            for next_el in outbound_vertices[cur_el]:
                inbound_count[next_el] -= 1
                if inbound_count[next_el] == 0:
                    queue.append(next_el)
                    res.append(next_el)
                    inbound_count[next_el] -= 1

        return res if len(res) == num_courses else []
