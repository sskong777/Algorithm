# 점화식 : D[i] = D[i-1] + D[i-2]

def dfs(N):
    if dp[N] != 0:
        return dp[N]
    if N == 1 or N == 2:
        return N
    else:
        dp[N] = dfs(N-1)+dfs(N-2)
        return dp[N]
N = int(input())
dp = [0] * (N+1)

dfs(N)
print(dp[N])

