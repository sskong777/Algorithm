# 런타임에러 -- 아마 시간초과

import sys
sys.stdin = open('input.txt','r')

def dfs(n,i,j,arrays):
    # if i == N-1 and j == N-1:
    if n== 2*(N-1):
        data.append(arrays)
        return

    for di,dj in ((1,0),(0,1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(n+1,ni,nj, arrays + [arr[ni][nj]])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    data = []
    dfs(0,0,0,[arr[0][0]])
    # print(data)
    data_sum = set()
    for i in data:
        data_sum.add(sum(i))
    print(f'#{tc} {min(data_sum)}')