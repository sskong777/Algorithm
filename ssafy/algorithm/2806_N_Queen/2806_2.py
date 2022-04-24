# dfs로 풀이

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = 0
    # v1 세로, v2:좌대각선, V3:우대각선
    v1,v2,v3 = [0]*30, [0]*30, [0]*30

    dfs(0)
    print(f'#{tc} {ans}')