N = int(input())
dp = [0] * (N+2)
T = [0] * (N+1)
P = [0] * (N+1)
for i in range(1,N+1):
    t, p = map(int,input().split())
    T[i] = t
    P[i] = p

for i in range(N,0,-1):
    if i + T[i] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[1])