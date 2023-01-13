import sys
sys.stdin = open('input.txt', 'r')

def check_seperate():
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for si in range(N):
        for sj in range(M):
            if arr[si][sj] != 0 and not visited[si][sj]:
                bfs(si,sj,visited)
                cnt += 1
    return cnt



def bfs(si,sj,visited):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] != 0:
                q.append((ni,nj))
                visited[ni][nj] = 1




N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = check_seperate()
print(ans)