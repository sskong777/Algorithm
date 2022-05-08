import sys
sys.stdin = open('input.txt')

INF = int(1e9)

N,M = map(int,input().split())  # 노드와 간선
start = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))

def get_smallest_node():
    minV = INF
    index = 0
    for i in range(1,N+1):
        if distance[i] < minV and not visited[i]:
            minV = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = 1

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost



dijkstra(start)
print(distance)