import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(si,sj):
    while q:
        ci,cj = q.popleft()

        if arr[si][sj] =='S':
            return v[si][sj]

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if (arr[ni][nj] =='D' or arr[ni][nj]=='.') and arr[ci][cj]=='S':
                    arr[ni][nj] = 'S'
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni,nj))
                elif (arr[ni][nj] =='S' or arr[ni][nj]=='.') and arr[ci][cj]=='*':
                    q.append((ni,nj))
                    # v[ni][nj] = 1
                    arr[ni][nj] = '*'

    return 'KAKTUS'


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

q = deque()
v = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if arr[n][m] =='S':
            q.append((n,m))
        elif arr[n][m] =='D':
            si,sj = n,m

for n in range(N):
    for m in range(M):
        if arr[n][m] == '*':
            q.append((n,m))

print(bfs(si,sj))

