import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj,color):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==color:
                stack.append((ni,nj))
                v[ni][nj] = 1



def GtoR():
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='G':
                arr[i][j] = 'R'

N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)]
cnt = 0
for si in range(N):
    for sj in range(N):
        if not v[si][sj]:
            dfs(si,sj,arr[si][sj])
            cnt += 1

GtoR()
v = [[0]*N for _ in range(N)]
cnt2 = 0
for si in range(N):
    for sj in range(N):
        if not v[si][sj]:
            dfs(si,sj,arr[si][sj])
            cnt2 += 1

print(cnt,cnt2)