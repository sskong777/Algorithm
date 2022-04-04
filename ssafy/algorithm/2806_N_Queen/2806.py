# dfs로 풀이

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if check(n,j):
            v[n][j] = 1
            dfs(n+1)
            v[n][j] = 0


def check(si,sj):
    # 1. 위쪽 방향
    for i in range(si-1,-1,-1):
        if v[i][sj] == 1:
            return 0

    # 2. 좌측 대각선 위
    i,j = si-1, sj-1
    while i>=0 and j>=0:
        if v[i][j]==1:
            return 0
        i,j = i-1,j-1

    # 3. 우측 대각선 위
    i,j = si-1, sj+1
    while i>=0 and j<N:
        if v[i][j]==1:
            return 0
        i,j = i-1,j+1
    # 3방향 퀸 없음: 성공
    return 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    v= [[0]*N for _ in range(N)]
    ans = 0
    dfs(0)
    print(f'#{tc} {ans}')