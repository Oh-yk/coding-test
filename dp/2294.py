import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = [-1] * (K+1)
count[0] = 0
for i in range(0, K+1):
    if i != 0 and count[i] == -1:
        continue
    for coin in coins:
        if i+coin > K:
            continue
        if count[i+coin] == -1:
            count[i+coin] = count[i] + 1
        else:
            count[i+coin] = min(count[i] + 1, count[i+coin])

if count[K] == 0:
    print(-1)
else:
    print(count[K])