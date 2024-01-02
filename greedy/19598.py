import heapq
import sys
input =  sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort()

rooms = []
heapq.heappush(rooms, meetings[0][1])

for meeting in meetings[1:]:
    if rooms[0] <= meeting[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, meeting[1])
    
print(len(rooms))
