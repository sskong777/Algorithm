import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1

    while stack:
        ci,cj = stack.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w and arr[ni][nj]==1 and v[ni][nj]==0:
                stack.append((ni,nj))
                v[ni][nj] = 1


while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break

    arr = [list(map(int,input().split())) for _ in range(h)]
    v = [[0]*w for _ in range(h)]

    cnt = 0
    for si in range(h):
        for sj in range(w):
            if v[si][sj]==0 and arr[si][sj]==1:
                dfs(si,sj)
                cnt += 1


    print(cnt)