import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr,n,visited):
    visited[n] = 1
    stack = []
    stack.append(n)

    while stack:
        x = stack.pop()
        for i in arr[x]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                par[i] = x

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