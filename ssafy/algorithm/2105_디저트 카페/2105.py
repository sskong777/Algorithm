import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,ci,cj,v,cnt):
    global si,sj,ans

    if n == 2 and ans >= cnt*2:
        return

    if n > 3:
        return

    # 정답 갱신
    if n==3 and ci == si and cj == sj and ans < cnt:
        ans = cnt
        return

    for k in range(n, n+2):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            dfs(k, ni, nj,v+[arr[ni][nj]], cnt+1)


# 중요 -상 하 좌 우
di,dj = (1,1,-1,-1,1) , (-1,1,1,-1,-1)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = -1
    for si in range(0,N-2):
        for sj in range(1,N-1):
            dfs(0,si,sj,[],0)

    print(f'#{tc} {ans}')