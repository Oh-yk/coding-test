import sys
input = sys.stdin.readline

import heapq

INF = int(1e9)

N = int(input()) # 도시
M = int(input()) # 버스

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, goal = map(int, input().split())

def dijkstra(start):
    q = []
    
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # q가 비어있지 않다면
    while q:
        # 최소 비용 노드 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue
        
        # 현재 노드와 인접한 노드 업데이트
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳤을 때 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

print(distance[goal])
    
