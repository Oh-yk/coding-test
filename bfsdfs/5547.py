import sys
input = sys.stdin.readline

from collections import deque
import copy

W, H = map(int, input().split())
my_map = [[]]
for _ in range(H):
    my_map.append([0] + list(map(int, input().split())))

odd_y_neighbors = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]
even_y_neighbors = [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

visited = [[False] * (W+1) for _ in range(H+1)]

count = 0
for y in range(1, H+1):
    for x in range(1, W+1):
        if my_map[y][x] == 1 and visited[y][x] == False:
            # start bfs
            buildings = [(x, y)]
            visited[y][x] = True
            count += 6
            queue = deque([(x, y)])
            while (queue):
                curr_x, curr_y = queue.popleft()
                if (curr_y % 2 == 1):
                    neighbors = copy.deepcopy(odd_y_neighbors)
                else:
                    neighbors = copy.deepcopy(even_y_neighbors)

                for dx, dy in neighbors:
                    new_x = curr_x + dx
                    new_y = curr_y + dy
                    if new_x > W or new_x < 1 or new_y > H or new_y < 1:
                        continue
                    if my_map[new_y][new_x] == 1:
                        count -= 1
                    if visited[new_y][new_x] == False and my_map[new_y][new_x] == 1:
                        visited[new_y][new_x] = True
                        count += 6
                        buildings.append((new_x, new_y))
                        queue.append((new_x, new_y))

            buildings.sort()
            hole = []
            init = buildings[0]
            

print(count)
                    
        