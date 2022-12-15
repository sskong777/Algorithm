import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(0,-1),(1,0),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1


T = int(input())

for tc in range(T):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    ans = 0

    for k in range(K):
        j,i = map(int,input().split())
        arr[i][j] = 1

    for si in range(N):
        for sj in range(M):
            if visited[si][sj] == 0 and arr[si][sj] == 1:
                bfs(si,sj)
                ans += 1
    print(ans)