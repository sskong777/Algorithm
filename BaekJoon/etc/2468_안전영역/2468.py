import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj,n):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>n:
                stack.append((ni,nj))
                v[ni][nj] = 1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
mmax = max(max(arr))
res = 0
for n in range(mmax):
    v = [[0]*N for _ in range(N)]
    cnt = 0

    for si in range(N):
        for sj in range(N):
            if arr[si][sj]>n and v[si][sj]==0:
                dfs(si,sj,n)
                cnt += 1
    res = max(res,cnt)

print(res)