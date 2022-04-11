import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    global v, cnt
    q = []
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = 1



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input())) for _ in range(N)]

    cnt = 0
    v = [[0]*M for _ in range(N)]
    for si in range(N):
        for sj in range(M):
            if v[si][sj] == 0:
                bfs(si,sj)
                cnt += 1

    print(f'#{tc} {cnt}')