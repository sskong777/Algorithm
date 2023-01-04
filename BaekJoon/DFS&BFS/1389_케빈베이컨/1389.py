import sys
sys.stdin = open('input.txt', 'r')

def bfs(user):
    q = []
    visited = [0] * (N + 1)

    q.append(user)
    visited[user] = 1

    while q:
        next = q.pop(0)
        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[next] + 1
    return sum(visited)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for m in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

res = []
for i in range(1,N+1):
    v = bfs(i)
    res.append(v)

print(res.index(min(res))+1)

