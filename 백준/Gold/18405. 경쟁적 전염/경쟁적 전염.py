from collections import deque

def bfs(start):
    q = deque(start)
    for s,i,j in start:
        visited[i][j] = 1

    while q:
        v, ci, cj = q.popleft()
        if visited[ci][cj]-1 == S:
            return

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((v,ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
                arr[ni][nj] = v

N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())

start = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            start.append((arr[i][j], i, j))

start.sort()
visited = [[0]*N for _ in range(N)]
ans = bfs(start)
print(arr[X-1][Y-1])
