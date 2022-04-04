import sys
sys.stdin = open('input.txt', 'r')
from collections import  deque

def bfs(si,sj):
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        if ci == N-1 and cj == N-1:
            return v[ci][cj]
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = bfs(0,0)
    print(ans)