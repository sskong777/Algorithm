import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
N, M = map(int,input().split()) # 노드와 간선 입력 받기
start = int(input())            # 출발 노드 입력 받기

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    begin, end, cost = map(int,input().split())
    graph[begin].append((end,cost))

dijkstra(start)

for i in range(1,N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])



def dikjstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


