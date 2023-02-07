import sys
sys.stdin = open('input.txt', 'r')

INF = int(1e9)
N, M = map(int,input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for m in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

for a in range(1,N+1):
    for b in range(1,N+1):
        if a==b:
            graph[a][b] = 0

for k in range(1,N+1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for i in range(1,N+1):
    count = 0
    for j in range(1,N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == N:
        result += 1

print(result)
