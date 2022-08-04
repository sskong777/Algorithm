import sys
sys.stdin = open('input.txt', 'r')

import heapq

V, E = map(int,input().split())
start = int(input())

INF = int(1e9)
graph = [[]  for _ in range(V+1)]
distance = [INF] * (V+1)


for m in range(V):
    begin, end, cost = map(int,input().split())
    graph[begin].append((end,cost))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

# print(distance)
for i in range(1,V+1):
    if distance[i] ==INF:
        print("INF")
    else:
        print(distance[i])