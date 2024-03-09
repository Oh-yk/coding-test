import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())

neighbors = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

for neighbor in neighbors:
    neighbor.sort()
    
visited = [False] * (N+1)

dfs_list = []

def dfs(start):
    visited[start] = True
    dfs_list.append(start)
    for neighbor in neighbors[start]:
        if visited[neighbor] == False:
            dfs(neighbor)

dfs(V)

visited = [False] * (N+1)

bfs_list = []

def bfs():
    visited[V] = True
    bfs_list.append(V)
    queue = deque([V])
    while queue:
        e = queue.popleft()
        for neighbor in neighbors[e]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                bfs_list.append(neighbor)
                queue.append(neighbor)

bfs()

print(" ".join(list(map(str, dfs_list))))
print(" ".join(list(map(str, bfs_list))))
