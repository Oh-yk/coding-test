import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

gaps = []
for i in range(N - 1):
    gaps.append(sensors[i+1] - sensors[i])
gaps.sort()

if K != 1:
    gaps = gaps[:-(K - 1)]
print(sum(gaps))