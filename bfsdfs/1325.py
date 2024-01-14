import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    c1, c2 = map(int, input().split())
    graph[c2].append(c1)

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    
    count = 0
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if not visited[child]:
                count += 1
                visited[child] = True
                queue.append(child)
    return count

count_list = [0]
for i in range(1, N + 1):
    count_list.append(bfs(i))

max_count = max(count_list)
answer = []
for i, count in enumerate(count_list):
    if i == 0:
        continue
    if count == max_count:
        answer.append(i)

print(" ".join(list(map(str, answer))))

    
    
    
    