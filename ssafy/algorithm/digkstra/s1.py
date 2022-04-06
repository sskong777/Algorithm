import sys
sys.stdin = open('input.txt', 'r')

def digkstra():
    while Q:
        now, dist = Q.pop()

        if D[now] < dist:    # 주어진 거리보다 이미 저장된 거리가 더 작으면 skip
            continue

        visited[now] = True
        # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
        for v in range(len(adj[now])):
            n_v, n_dist = adj[now][v]
            if not visited[n_v]:
                if dist + n_dist < D[n_v]:
                    D[n_v]= dist + n_dist
                    Q.append((n_v, D[n_v]))



V, E = map(int, input().split())
# 인접 리스트
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    adj[s].append((e, d))

INF = 987654321
D = [INF] * (V+1)
D[0] = 0
# 시작 정점에서 인접한 정점 거리를 저장
for v, d in adj[0]:
    D[v] = d

visited = [False] * (V+1)
visited[0] = True

Q = [*adj[0]]
digkstra()
print(D)