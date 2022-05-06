import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def waterpool(water_list):
    q = deque(water_list)
    v = [[0] * M for _ in range(N)]

    for water in water_list:
        v[water[0]][water[1]] = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]=='.':
                q.append((ni,nj))
                v[ni][nj] = 1
                arr[ni][nj] = '*'

def waterpool(water_list):
    q = deque(water_list)
    v = [[0] * M for _ in range(N)]

    for water in water_list:
        v[water[0]][water[1]] = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]=='.':
                q.append((ni,nj))
                v[ni][nj] = 1
                arr[ni][nj] = '*'


def bfs(si,sj):
    visited = [[0] * M for _ in range(N)]
    q = deque((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
water_list = []
for n in range(N):
    for m in range(M):
        if arr[n][m] == '*':
            water_list.append((n,m))
        # if arr[n][m] =='S':


waterpool(water_list)
print(arr)