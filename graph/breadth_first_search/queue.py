from typing import List, Dict
from collections import deque

# O(N + M). N - number of vertices, M - number of edges
def bfs(graph: Dict[int, List[int]], root):
    if not graph:
        return

    visited = set()
    queue = deque()

    queue.append(root)

    # O(N + M). N - number of vertices, M - number of edges
    while queue:
        cur_el = queue.popleft()
        if cur_el not in visited:
            visited.add(cur_el)
            for next_el in graph[cur_el]:
                queue.append(next_el)
