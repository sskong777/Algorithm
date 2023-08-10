# https://www.acmicpc.net/problem/13023
# DFS/ BFS
import time
import sys
input = sys.stdin.readline
# N = 2,000
# M = 2,000
# time :2s => 20,000,000
# 시간 복잡도 : O((V+E)*V)  => 8,000,000
# DFS => O(V+E)
# for문 O(V)
def dfs(start,graph,visited,depth):
    global flag
    if depth == 5:
        flag = True
        return

    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i,graph,visited,depth+1)
    visited[start] = 0

V, E = map(int,input().split())
graph = [[]  for _ in range(V)]
visited = [0] * (V)
flag = False
for e in range(E):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(V):
    dfs(i,graph,visited,1)
    # 속도 약 6배 차이
    if flag:
        break
print(int(flag))