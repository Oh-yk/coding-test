import sys
input = sys.stdin.readline

bingo_map = []
for _ in range(5):
    l = list(map(int, input().split()))
    bingo_map.append(l)
    
nums = []
for _ in range(5):
    l = list(map(int, input().split()))
    nums.extend(l)

cross1 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
cross2 = [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]

bingo = 0
for i, num in enumerate(nums):
    for r in range(5):
        find = False
        for c in range(5):
            if bingo_map[r][c] == num:
                find = True
                bingo_map[r][c] = -1
                target = (r, c)
                break
        if find:
            break
    
    r = target[0]
    c = target[1]
    if bingo_map[r][0] == -1 and bingo_map[r][1] == -1 and bingo_map[r][2] == -1 and bingo_map[r][3] == -1 and bingo_map[r][4] == -1:
        bingo += 1
    
    if bingo_map[0][c] == -1 and bingo_map[1][c] == -1 and bingo_map[2][c] == -1 and bingo_map[3][c] == -1 and bingo_map[4][c] == -1:
        bingo += 1
    
    if target in cross1:
        if bingo_map[0][0] == -1 and bingo_map[1][1] == -1 and bingo_map[2][2] == -1 and bingo_map[3][3] == -1 and bingo_map[4][4] == -1:
            bingo += 1
            
    if target in cross2:
        if bingo_map[0][4] == -1 and bingo_map[1][3] == -1 and bingo_map[2][2] == -1 and bingo_map[3][1] == -1 and bingo_map[4][0] == -1:
            bingo += 1
    
    if bingo >= 3:
        print(i+1)
        break
