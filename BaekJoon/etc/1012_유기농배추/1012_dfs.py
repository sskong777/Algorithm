import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()

        for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                stack.append((ni,nj))
                v[ni][nj] = 1

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        col,row = map(int,input().split())
        arr[row][col] = 1

    v = [[0]*M for _ in range(N)]
    cnt = 0

    for si in range(N):
        for sj in range(M):
            if v[si][sj] == 0 and arr[si][sj] == 1:
                dfs(si,sj)
                cnt += 1

    print(cnt)