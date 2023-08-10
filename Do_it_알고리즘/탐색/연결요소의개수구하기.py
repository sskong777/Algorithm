# https://www.acmicpc.net/problem/11724
# DFS/ BFS
import time
import sys
input = sys.stdin.readline
# N = 1,000
# time : 3s => 30,000,000
# 시간 복잡도 : O(?)
def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


V, E = map(int,input().split())
graph = [[]  for _ in range(V+1)]
visited = [0] *(V+1)
answer = 0

for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,V+1):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)