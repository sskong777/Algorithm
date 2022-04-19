import sys
sys.stdin = open('input.txt', 'r')

def bfs(arr,n,visited):
    visited[n] = 1
    q = []
    q.append(n)

    while q:
        x = q.pop(0)
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
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

bfs(arr,1,visited)
for i in range(2,V+1):
    print(par[i])