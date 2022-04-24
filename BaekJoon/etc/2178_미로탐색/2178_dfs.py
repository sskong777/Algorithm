import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    v = [[0]*M for _ in range(N)]
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()
        if ci==N-1 and cj==M-1:
            return v[N-1][M-1]

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                stack.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

    # return v[N-1][M-1]


N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

ans = dfs(0,0)
print(ans)