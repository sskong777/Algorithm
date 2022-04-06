# D : 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P : 최단 경로 트리 저장
def Dijkstra(G, r): # r: 시작 정점
    D = [float('inf')] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min = float('inf')
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True

        for v, val in G[minIndex]:
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex