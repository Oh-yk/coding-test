import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())

graph = [ [] for _ in range(N + 1) ]
visited = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for l in graph:
    l.sort()
    
dfs_list = []
bfs_list = []

def dfs(graph, v, visited):
    visited[v] = True
    dfs_list.append(v)
    for w in graph[v]:
        if  not visited[w]:
            dfs(graph, w, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    bfs_list.append(start)
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                bfs_list.append(w)
dfs(graph, V, [False] * (N + 1))
bfs(graph, V, [False] * (N + 1))

print(" ".join(list(map(str, dfs_list))))
print(" ".join(list(map(str, bfs_list))))
print(dfs_list.reverse())
print(dfs_list)