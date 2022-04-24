import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(si,sj,c):
    q = deque()
    q.append((si,sj,c))
    v[si][sj][0] = 1

    while q:
        ci,cj,c = q.popleft()

        if ci == N-1 and cj == M-1:
            return v[ci][cj][c]

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            # 다음 이동할 좌표가 벽이 아니고 아직 방문을 하지 않았다면
            if 0<=ni<N and 0<=nj<M and v[ni][nj][c]==0 and arr[ni][nj]==0:
                q.append((ni,nj,c))
                v[ni][nj][c] = v[ci][cj][c] + 1
            # 다음 이동할 좌표가 벽이고, 벽을 아직 부수지 않았다면
            elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and c==0:
                v[ni][nj][1] = v [ci][cj][0] +1
                q.append((ni,nj,1))


    return -1




N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
v = [[[0]*2 for _ in range(M)] for _ in range(N)]

res = bfs(0,0,0)
print(res)
