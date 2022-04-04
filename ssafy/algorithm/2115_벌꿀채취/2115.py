import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,cnt,ssum,lst):
    global sol
    if n==M:
        if cnt<=C and sol<ssum:
            sol = ssum
        return
    dfs(n+1,cnt,ssum,lst)   #포함 시키지 않는 경우
    dfs(n+1,cnt+lst[n], ssum+lst[n]**2,lst)

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0

    for i1 in range(N):
        for j1 in range(N-M+1):
            sol = 0
            dfs(0,0,0,arr[i1][j1:j1+M])
            t1 = sol
            for i2 in range(i1,N):
                sj = 0
                if i1==i2:
                    sj = j1+M
                for j2 in range(sj,N-M+1):
                    sol = 0
                    dfs(0,0,0,arr[i2][j2:j2+M])
                    ans = max(ans,t1+sol)


    print(f'#{tc} {ans}')

