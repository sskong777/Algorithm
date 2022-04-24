import sys
sys.stdin = open('input.txt', 'r')

def dfs(a):

    for i in graph[a]:
        if not v[i]:
            v[i] = v[a] + 1
            dfs(i)

V = int(input())
a,b = map(int,input().split())
E = int(input())
graph = [[]*(V+1) for _ in range(V+1)]
v = [0] * (V + 1)

for e in range(E):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a)

if v[b] ==0:
    print(-1)
else:
    print(v[b])