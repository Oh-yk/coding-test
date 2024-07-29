import sys
from collections import deque

input = sys.stdin.readline

EMPTY = "."
OBSTACLE = "#"

move = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    m = [] # index: L, R, C
    start_idx = [0, 0, 0]
    end_idx = [0, 0, 0]
    
    for l in range(L):
        level = []
        for r in range(R):
            line = list(input().strip())
            level.append(line)
            if "S" in line:
                c = line.index("S")
                start_idx = [l, r, c, 0]
            elif "E" in line:
                c = line.index("E")
                end_idx = [l, r, c]
        m.append(level)
        input()
            
    
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[start_idx[0]][start_idx[1]][start_idx[2]] = True
    
    
    queue = deque([start_idx])
    next_queue = deque()
    
    dist = start_idx[3]
    found = False
    
    while queue:
        p_curr = queue.popleft()

        dist = p_curr[3] + 1
        for dl, dr, dc in move:
            p_next = [p_curr[0] + dl, p_curr[1] + dr, p_curr[2] + dc]
            
            if p_next[0] < 0 or p_next[0] >= L or p_next[1] < 0 or p_next[1] >= R or p_next[2] < 0 or p_next[2] >= C:
                continue
            
            if visited[p_next[0]][p_next[1]][p_next[2]]:
                continue
            
            if m[p_next[0]][p_next[1]][p_next[2]] == OBSTACLE:
                continue
                
            if p_next == end_idx:
                found = True
                break
        
            
            visited[p_next[0]][p_next[1]][p_next[2]] = True
            p_next.append(dist)
            queue.append(p_next)
            
        if found:
            break

        
    if not found:
        print("Trapped!")
    else:
        print("Escaped in {0} minute(s).".format(dist))
    
    