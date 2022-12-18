import sys
sys.setrecursionlimit(10000)

def dfs(n):
    v[n] = 1
    for i in graph[n]:
        if not v[i]:
            dfs(i)

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for e in range(E):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

v = [0] * (V+1)
# print(graph)

cnt = 0
for i in range(1,V+1):
    if not v[i]:
        dfs(i)
        cnt += 1
print(cnt)