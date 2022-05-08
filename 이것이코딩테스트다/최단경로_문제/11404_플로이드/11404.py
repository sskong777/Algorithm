import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for m in range(M):
    start,end,cost = map(int,input().split())
    if cost < graph[start][end]:
        graph[start][end] = cost

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j] = 0

for k in range(1,N+1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()