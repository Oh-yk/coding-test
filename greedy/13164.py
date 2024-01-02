N, K = map(int, input().split())
heights = list(map(int, input().split()))

gap = [heights[i+1] - heights[i] for i in range(N-1)]
gap.sort()

if K != 1:
    gap = gap[:-(K-1)]

cost = sum(gap)
print(cost)