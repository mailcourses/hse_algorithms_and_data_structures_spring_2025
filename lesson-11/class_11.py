# n, [(1, 2), (2, 3), (1, 4), (3, 5)], x, y
# V = {1 .. n}
# 1 <= x, y <= n

# n = 6
# 1 <-> 2 -> 3 -> 5
# |     ^
# |     |
# 4  -> 7         6

# x = 1, y = 5 -> 3
# x = 1, y = 6 -> None
from collections import deque

def bfs(x: int, y: int, graph: dict) -> int:
    if x == y:
        return 0

    visited = [0 for i in len(graph)]
    deq = deque([x])
    visited[x] = 1

    while deq:
        current = deq.popleft()
        if current == y:
            return visited[current] - 1
        for i in graph[current]:
            if not visited[i]:
                deq.append(i)
                visited[i] = visited[current] + 1
    
    return None
    

def distance(V: list[int], edges: list, x: int, y: int):
    n = len(V)
    graph = {i: [] for i in V}
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)
    
    
    return bfs(x, y, graph)