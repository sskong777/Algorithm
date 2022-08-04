import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1
    apt = [(si,sj)]
    while stack:
        ci,cj = stack.pop()
        for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                stack.append((ni,nj))
                v[ni][nj] = 1
                apt.append((ni,nj))
    return apt

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

v = [[0]*N for _ in range(N)]
apts = []
cnt = 0
for si in range(N):
    for sj in range(N):
        if arr[si][sj]==1 and v[si][sj]==0:
            apt = dfs(si,sj)
            cnt += 1
            apts.append(len(apt))
            
apts.sort()
print(cnt)
for apt in apts:
    print(apt)

