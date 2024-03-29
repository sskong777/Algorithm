
def bfs(si,sj):
    q = []
    q.append((si,sj))

    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = 1



T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        col,row = map(int,input().split())
        arr[row][col] = 1

    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for si in range(N):
        for sj in range(M):
            if visited[si][sj] == 0 and arr[si][sj] == 1:
                bfs(si,sj)
                cnt += 1

    print(cnt)