# https://www.acmicpc.net/problem/1260
# DFS/ BFS
import time
import sys
input = sys.stdin.readline
# N = 1,000
# M = 10,000
# time :2s => 40,000,000
# 시간 복잡도 : O((V+E)*V)  => 8,000,000
# DFS => O(V+E)
# for문 O(V)

def dfs(start):

    print(start,end=' ')

    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q  = [start]
    visited[start] = 1

    while q:
        now = q.pop(0)
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

N, M, V = map(int,input().split())
graph = [[]  for _ in range(N+1)]

for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1,N+1):
    graph[i].sort()

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)

