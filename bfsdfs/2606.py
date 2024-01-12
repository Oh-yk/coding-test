import sys
input = sys.stdin.readline

N = int(input())
S = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(S):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

count = 0
visited = [False] * (N + 1)

def dfs(graph, v, visited):
    global count
    visited[v] = True
    count += 1
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)

dfs(graph, 1, visited)
print(count - 1)