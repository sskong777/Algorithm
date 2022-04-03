import sys
sys.stdin = open('input.txt', 'r')

def dfs(start,si,sj,ans):
    if start == 7:
        sset.add(ans)
        return

    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni,nj = si+di, sj+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(start+1,ni,nj,ans+arr[ni][nj])

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]

    sset = set()
    for si in range(4):
        for sj in range(4):
            dfs(0,si,sj,'')

    print(len(sset))