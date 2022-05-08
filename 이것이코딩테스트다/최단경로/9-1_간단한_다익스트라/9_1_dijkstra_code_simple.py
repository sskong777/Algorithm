import sys
sys.stdin = open('input.txt')

INF = int(1e9)

# 노드의 개수, 간선의 갯수
n,m  = map(int,input().split())

# 시작노드 번호를 입력받기
start = int(input())
# 인접배열리스트
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
distance = [INF] * (n+1)

# 출발,도착,비용 입력받아 그래프 완성
for _ in range(m):
    begin,end,dist = map(int,input().split())
    graph[begin].append((end,dist))
# print(graph)

def get_smallest_node():
    min_V = INF
    index = 0   # 가장 최단거리가 짧은노드(index)
    for i in range(1,n+1):
        if distance[i] < min_V and not visited[i]:
            min_V = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해 초기화
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = 1
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        # print(distance)

dijkstra(start)
print(distance)


# 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1,n+1):
#     if distance[i]==INF:
#         print('INFINITY')
#     else:
#         print(distance[i])