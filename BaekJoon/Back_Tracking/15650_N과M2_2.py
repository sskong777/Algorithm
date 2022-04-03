def dfs(idx):
    if idx == M:
        print(subset)
        return


    for i in range(N):
        if not v[i]:
            v[i] = 1
            subset.append(arr[i])
            dfs(idx+1)
            subset.pop()
            v[i] = 0

N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]

v = [0] * N
subset = []
dfs(0)