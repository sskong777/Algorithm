import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,ssum):
    global ans
    # 1년을 넘어가면 중단
    if n > 12:
        # 정답 갱신
        if ans > ssum:
            ans = ssum
        return
    dfs(n+1,ssum+arr[n]*day)
    dfs(n+1,ssum + month)
    dfs(n+3,ssum+month_3)
    dfs(n+12,ssum+year)


T = int(input())
for tc in range(1,T+1):
    day, month, month_3,year = map(int,input().split())
    arr = [0] + list(map(int,input().split()))

    ans = 12345678
    dfs(1,0)
    print(f'#{tc} {ans}')