import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**9)

def dfs(arr,n,visited):
    visited[n] = 1
    for i in arr[n]:
        if not visited[i]:
            par[i] = n
            dfs(arr,i,visited)

V = int(input())
E = V-1

visited = [0]*(V+1)
par = [0]*(V+1)

arr = [[] for _ in range(V+1)]

for i in range(E):
    start,end = map(int,input().split())
    arr[start].append(end)
    arr[end].append(start)

dfs(arr,1,visited)
for i in range(2,V+1):
    print(par[i])