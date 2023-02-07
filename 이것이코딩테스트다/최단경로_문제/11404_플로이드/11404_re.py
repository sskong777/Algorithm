import sys
sys.stdin = open('input.txt', 'r')

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF]*(N+1) for _ in range(N+1)]

for m in range(M):
    a,b,c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for a in range(1, N+1):
    for b in range(1,N+1):
        if a==b:
            graph[a][b] = 0

for k in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()