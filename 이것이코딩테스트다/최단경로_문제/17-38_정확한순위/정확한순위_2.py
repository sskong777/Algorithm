import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint

INF = int(1e9)
N,M = map(int,input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(M):
    start, end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j] = 0


for k in range(1,N+1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

pprint(graph)
result = 0
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if graph[i][j] != INF:
            cnt += 1

    if cnt == N:
        result += 1
print(result)