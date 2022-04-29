# 백준 14501
import sys
sys.stdin = open('input.txt', 'r')


N  = int(input())
dp = [0] * N
T = []
P = []
for n in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

print(T)
print(P)

for i in range(N):
    # i일에 상담을 잡을 수 있다면
    if T[i]+i <= N+1:
        t = 0
        while t <= N:
            dp[i] += P[t]
            t += T[t]
print(dp)
