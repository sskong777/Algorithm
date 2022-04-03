def dfs(idx):
    if idx == M:
        print(*subset)
        return

    for i in range(N):
            subset.append(arr[i])
            visited[i] = 1
            dfs(idx+1)
            subset.pop()
            visited[i] = 0


N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
visited = [0] * N
subset = []
dfs(0)