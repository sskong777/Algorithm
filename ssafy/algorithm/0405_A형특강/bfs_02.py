def bfs(si,sj):
    q = []

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

N = 10
v = [[0] * N for _ in range(N)]

bfs(1,1)
print(v)