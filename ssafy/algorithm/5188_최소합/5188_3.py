# 가지치기, 방문 표시
import sys
sys.stdin = open('input.txt','r')

def dfs(n,i,j,ssum):
    v = [[0]*N for _ in range(N)]
    v[0][0] = 1
    global res
    if n== 2*(N-1):
        if res > ssum:
            res = ssum
        return

    for di,dj in ((1,0),(0,1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 :
            v[ni][nj] = 1
            dfs(n+1,ni,nj, ssum + arr[ni][nj])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # v = [[0]*N for _ in range(N)]
    # v[0][0] = 1
    res = 10000
    dfs(0,0,0,arr[0][0])
    print(f'#{tc} {res}')