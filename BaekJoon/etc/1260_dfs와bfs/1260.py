import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def dfs(v):
    print(v,end=' ')
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        next = q.popleft()
        print(next,end=' ')
        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1,N+1):
    graph[i].sort()

visited = [0] * (N+1)

dfs(V)
print()

visited = [0] * (N + 1)
bfs(V)