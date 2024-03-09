import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())

box = []
for _ in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    
def is_done(box):
    for row in box:
        for apple in row:
            if apple == 0:
                return False
    return True

visited = [[False] * M for _ in range(N)]

neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

count = 1
while not is_done(box):
    for r in range(N):
        for c in range(M):
            if box[r][c] == count:
                for dr, dc in neighbors:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r >= N or new_r < 0 or new_c >= M or new_c < 0:
                        continue
                    if box[new_r][new_c] == 0:
                        box[new_r][new_c] = count + 1
    count += 1
    
print(count - 1)