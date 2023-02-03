import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


INF = int(1e9)

N,M = map(int,input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1,N+1):
    for b in range(1,N+1):
        if a==b:
            graph[a][b] = 0


for _ in range(M):
    begin, end, cost = map(int,input().split())
    graph[begin][end] = cost


for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,N+1):
    for b in range(1,N+1):
        if graph[a][b] == INF:
            print("INFINITY",end= ' ')
        else:
            print(graph[a][b], end=' ')
    print()