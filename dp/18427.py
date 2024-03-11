import sys
input = sys.stdin.readline

import copy

N, M, H = map(int, input().split())
students_blocks = []
for _ in range(N):
    students_blocks.append(list(map(int, input().split())))

count = [0] * (H+1)
for student_blocks in students_blocks:
    prev_count = copy.deepcopy(count)
    for block in student_blocks:
        for i in range(block, H+1):
            if i == block:
                count[block] += 1
            elif prev_count[i-block] != 0:
                count[i] += prev_count[i-block]

print(count[H] % 10007)