import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    global cnt
    stack = []
    stack.append((si,sj))
    v = [[0]*N for _ in range(M)]
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()

        if ci==M-1 and cj==N-1:
            cnt += 1
            # return

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ci][cj]>arr[ni][nj]:
                stack.append((ni,nj))
                v[ni][nj] = 1



M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

cnt = 0
dfs(0,0)

print(cnt)