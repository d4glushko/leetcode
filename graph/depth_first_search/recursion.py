from typing import List, Dict

# O(N + M). N - number of vertices, M - number of edges
visited = set()
def dfs(graph: Dict[int, List[int]], root):
    if not graph:
        return

    for next_el in graph[root]:
        if next_el not in visited:
            visited.add(next_el)
            dfs(graph, next_el)
