import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and not visited[ni][nj] and arr[ni][nj]==1:
                q.append((ni,nj))
                visited[ni][nj] = 1


while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(M)]
    visited = [[0]*N for _ in range(M)]

    cnt = 0

    for si in range(M):
        for sj in range(N):
            if not visited[si][sj] and arr[si][sj] == 1:
                bfs(si,sj)
                cnt += 1
    print(cnt)
