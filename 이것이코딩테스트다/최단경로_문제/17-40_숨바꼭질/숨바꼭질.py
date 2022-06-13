import sys
sys.stdin = open('input.txt', 'r')

import heapq
INF = int(1e9)

N, M = map(int,input().split())
start = 1

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int,input().split())
    # 양방향 이동 비용이 1
    graph[a].append((b,1))
    graph[b].append((a,1))


def dijkstra(start):
    q = []
    # 시작노드로 가기 위한 최단 경로 : 0
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인

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
print(distance)
# 최단 거리가 가장 먼 노드 번호
max_node = 0

# 도달할 수 있는 노드 중에서, 최단거리가 가장 먼 노드와의 최단거리
max_distance = 0

# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단거리를 가지는 노드들의 리스트
result = []

for i in range(1, N+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))