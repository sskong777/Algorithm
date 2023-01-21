import sys
sys.stdin = open('input.txt' ,'r')

def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        # if ci==N-1 and cj==M-1:
        #     return visited[ci][cj]
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited[N-1][M-1]


N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

ans  = bfs(0,0)
print(ans)
