from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in (-1,0),(1,0),(0,1),(0,-1):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited[N-1][N-1]

N = 7
arr = [list(map(int,input().split())) for _ in range(N)]

visited= [[0]*N for _ in range(N)]
res = bfs(0,0)
print(res-1)