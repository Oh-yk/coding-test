import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (N + 1)
parent = [0] * (N + 1)

def dfs(graph, v, visited):
    visited[v] = True
    for child in graph[v]:
        if not visited[child]:
            parent[child] = v
            dfs(graph, child, visited)

# dfs(graph, 1, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if not visited[child]:
                parent[child] = v
                visited[child] = True
                queue.append(child)

bfs(graph, 1, visited)

print("\n".join(list(map(str, parent[2:]))))