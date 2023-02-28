from typing import List, Dict
from collections import deque

# O(N + M). N - number of vertices, M - number of edges
def dfs(graph: Dict[int, List[int]], root):
    if not graph:
        return

    stack = deque()
    visited = set()

    stack.append(root)

    # O(N + M). N - number of vertices, M - number of edges
    while stack:
        cur_el = stack.pop()
        if cur_el not in visited:
            visited.add(cur_el)
            for next_el in graph[cur_el]:
                stack.append(next_el)
