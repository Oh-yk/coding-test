import heapq
import sys
input = sys.stdin.readline

N = int(input())

timetable = []
for _ in range(N):
    start, end = map(int, input().split())
    timetable.append((start, end))
    
timetable.sort()

run = []
heapq.heappush(run, timetable[0][1]) # 끝나는 시간만 중요함

for start, end in timetable[1:]:
    if run[0] <= start:
        heapq.heappop(run)
        heapq.heappush(run, end)
    else:
        heapq.heappush(run, end)

print(len(run))
            
    
