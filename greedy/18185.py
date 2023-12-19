N = int(input())
A = [int(a) for a in input().split()]

cost = 0
for i in range(N):
    if i < N - 2:
        min_num = min(A[i:i+3])
        if min_num > 0:
            A[i] -= min_num
            A[i+1] -= min_num
            A[i+2] -= min_num
            cost += min_num * 7
    if i < N - 1:
        min_num = min(A[i:i+2])
        if min_num > 0:
            A[i] -= min_num
            A[i+1] -= min_num
            cost += min_num * 5
    min_num = min(A[i:i+1])
    if min_num > 0:
        A[i] -= min_num
        cost += min_num *3

print(cost)