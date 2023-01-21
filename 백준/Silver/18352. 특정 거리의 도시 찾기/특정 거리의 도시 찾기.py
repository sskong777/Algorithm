
from collections import deque

def bfs(v):
    q = deque([v])

    visitied[v] = 1

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visitied[i]:
                q.append(i)
                visitied[i] = visitied[now]+1

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
visitied = [0]* (N+1)

for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
bfs(X)

for i in range(1,len(visitied)):
    if i == X:
        continue
    if visitied[i]-1 == K:
        print(i)
if K+1 not in visitied:
    print(-1)

