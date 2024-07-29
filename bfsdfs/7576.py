import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split()) # M: 가로, N: 세로
m = []
for _ in range(N):
    l = list(map(int, input().split()))
    m.append(l)

visited = [ [False] * M for _ in range(N)]
queues = []
for y in range(N):
    for x in range(M):
        if m[y][x] == 1:
            visited[y][x] = True
            queues.append(deque([(y, x)]))

print(queues)
def is_end():
    for queue in queues:
        if len(queue) != 0:
            return False
    return True

round = 0      
while not is_end():
    round += 1
    print(round)
    for queue in queues:
        if len(queue) == 0:
            continue
        
        y, x = queue.popleft()
        dist = m[y][x]
        
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if ny >= N or ny < 0 or nx >= M or nx < 0: # out of range
                continue
            if visited[ny][nx]:
                continue
            if m[ny][nx] == -1: # no way
                continue
            
            m[ny][nx] = dist + 1
            
            visited[ny][nx] = True
            queue.append((ny, nx))

no = False
for row in m:
    if 0 in row:
        no = True
        print("-1")
        break

if not no:
    max_value = max([max(row) for row in m])
    print(max_value - 1)
