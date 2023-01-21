import sys
sys.stdin = open('input.txt', 'r')

def bfs(i,j):
    q = []
    q.append((i,j))
    visited[i][j] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = 1

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # print(arr)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)