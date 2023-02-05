# import sys
#
# sys.stdin = open('input.txt', 'r')
#
# import heapq
#
#
# def dijkstra(start, end):
#     distance = [INF] * (N + 1)
#
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#     return distance[end]
#
#
# INF = int(1e9)
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#     graph[b].append((a, 1))
#
# K, X = map(int, input().split())
#
# answer = dijkstra(1, K) + dijkstra(K, X)
#
# if answer >= INF :
#     print(-1)
# else :
#     print(answer)


import sys
sys.stdin = open('input.txt', 'r')
import heapq

# 무한대를 나타내는 변수
INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())

# 인접한 회사들 정보를 담기 위한 인접리스트
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, sys.stdin.readline().rstrip().split())


# 다익스트라 알고리즘을 위한 함수
def dijkstra(start, end):
    # 최단 거리 테이블 무한대로 초기화
    distance = [INF] * (n + 1)

    # 우선순위 큐 만들고 시작점 push
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        # 이미 처리한 회사이면 무시
        if distance[cur] < dist:
            continue

        # 현재 회사와 인접한 회사들 확인
        for i in graph[cur]:
            cost = dist + i[1]
            # 현재 회사를 거쳐서 가는 것이 더 최단 거리이면 최단 거리 테이블 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 출발점 ~ 도착점 최단 거리 리턴
    return distance[end]


# 1번 ~ k번 회사 최단 거리 + k번 ~ x번 회사 최단 거리
answer = dijkstra(1, k) + dijkstra(k, x)

if answer < INF:
    print(answer)
else:
    print(-1)
