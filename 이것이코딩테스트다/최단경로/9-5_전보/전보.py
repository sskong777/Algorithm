import sys
sys.stdin = open('input.txt', 'r')

import heapq
INF = int(1e9)

# 도시의 개수, 통로의 개수, 메시지를 보내야하고자 하는 도시
N,M,start = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

# 출발,도착,비용 입력 => 그래프 완성
for i in range(M):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))

def dijstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(start)
# print(distance)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서 , 가장 멀리 있는 노드와의 최단거리
max_distance = 0
for d in distance:
    if d !=INF:
        count += 1
        max_distance = max(d,max_distance)
print(count-1,max_distance)