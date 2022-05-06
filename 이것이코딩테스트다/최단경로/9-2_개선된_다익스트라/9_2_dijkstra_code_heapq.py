import sys
sys.stdin = open('input.txt', 'r')

import heapq
INF = int(1e9)

# 노드의 개수, 간선의 갯수
n,m  = map(int,input().split())

# 시작노드 번호를 입력받기
start = int(input())
# 인접배열리스트
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 출발,도착,비용 입력받아 그래프 완성
for _ in range(m):
    begin,end,dist = map(int,input().split())
    graph[begin].append((end,dist))

def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0

    # 큐가 비어있을 때 까지 반복
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
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


# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])