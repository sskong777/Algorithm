def bfs(si,sj):
    q =[]
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1


while True:
    W, H = map(int, input().split())
    if W==0 and H == 0:
        exit(0)
    arr = [list(map(int,input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and arr[i][j]==1:
                bfs(i,j)
                ans += 1
    print(ans)


