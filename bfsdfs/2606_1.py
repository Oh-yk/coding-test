import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
S = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(S):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
    
visited = [False] * (N + 1)           

count = 0

def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                count += 1
                queue.append(w)

bfs(graph, 1, visited)
print(count)

    