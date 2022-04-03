import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,ci,cj,v,cnt):
    global ans
    # 종료조건
    if n > 3:
        return

    # 시작지점 복귀
    if n == 3 and ci==si and cj==sj and ans < cnt:
        ans = cnt
        return

    # 직진 or 방향전환
    for k in range(n,n+2):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            dfs(k,ni,nj,v+[arr[ni][nj]],cnt+1)

# 중요 -
di,dj = (1,1,-1,-1,1) , (-1,1,1,-1,-1)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = -1
    for si in range(N):
        for sj in range(N):
            dfs(0,si,sj,[],0)

    print(f'#{tc} {ans}')