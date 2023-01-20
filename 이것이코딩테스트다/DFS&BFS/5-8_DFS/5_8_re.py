
def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

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


dfs(1)