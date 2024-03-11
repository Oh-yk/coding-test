# Not solved

import sys
input = sys.stdin.readline

import math

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
info.sort()
move = info[0][0]
if move < 0:
    for i in range(N):
        info[i][0] += -move
else:
    move = 0
    
weight = 0
count = 0
for x, population in info:
    weight += x * population
    count += population

weight_center = weight / count
left = math.floor(weight_center)
right = math.floor(weight_center) + 1

if weight_center - left <= right - weight_center:
    print(left + move)
else:
    print(right + move)