def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        now = q.pop(0)
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

N = 8
visited = [0] * (N+1)
bfs(1)