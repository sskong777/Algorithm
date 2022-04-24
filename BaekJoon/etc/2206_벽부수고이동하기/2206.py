# 실패코드

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

    return v[N-1][M-1]




N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

res = bfs(0,0)

for si in range(N):
    for sj in range(M):
        if arr[si][sj] == 1:
            arr[si][sj] = 0
            d = bfs(0,0)
            arr[si][sj] = 1

            if res == 0 and d > 0:
                res = d

            if res > 0 and d > 0:
                res = min(res,d)

if res == 0:
    print(-1)
else:
    print(res)