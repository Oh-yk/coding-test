import sys
input = sys.stdin.readline

C, N = map(int, input().split())

info = []
for _ in range(N):
    money, people = map(int, input().split())
    info.append((money, people))
    
min_cost = [0] * (C+1)
for i in range(1, C+1):
    for money, people in info:
        for j in range(people):
            if i+j > C:
                continue
            if min_cost[i+j] == 0:
                min_cost[i+j] = min_cost[i-1] + money
            else:
                min_cost[i+j] = min(min_cost[i+j], min_cost[i-1] + money)
        
print(min_cost[C])
