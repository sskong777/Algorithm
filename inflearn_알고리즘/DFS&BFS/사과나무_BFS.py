import sys
from collections import deque

def bfs(si,sj):
    global res, L
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    res += arr[si][sj]

    while q:
        if L == N//2:
            break
        for i in range(len(q)):
            ci,cj = q.popleft()

            for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                    q.append((ni,nj))
                    visited[ni][nj] = 1
                    res += arr[ni][nj]
        L += 1

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

si,sj = N//2, N//2
L = 0
res  = 0
bfs(si,sj)
print(res)
print(visited)