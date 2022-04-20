import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global cnt
    v[n] = 1
    for i in graph[n]:
        if not v[i]:
            dfs(i)
            cnt += 1


V = int(input())
E = int(input())
graph = [[]*(V+1) for _ in range(V+1)]
for e in range(E):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)
cnt = 0
v = [0]*(V+1)
dfs(1)

print(cnt)