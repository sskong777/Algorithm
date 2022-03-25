import sys
sys.stdin = open('input.txt', 'r')

def dfs(N,si,sj,num):

    if N >= 7:
        sset.add(num)
        return

    for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni,nj = si+di, sj+dj
        if 0<=ni<4 and 0<=nj<4:
            # num += str(arr[ni][nj])
            dfs(N+1,ni,nj,num+str(arr[ni][nj]))


T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]

    sset = set()
    for si in range(4):
        for sj in range(4):
            dfs(0,si,sj,'')


    print(f'#{tc} {len(sset)}')