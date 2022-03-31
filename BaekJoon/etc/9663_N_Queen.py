def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            dfs(n+1)
            v[i] = 0




N = int(input())
arr = [[0]*N for _ in range(N)]
v = [0] * N
cnt = 0

dfs(0)

print(cnt)
