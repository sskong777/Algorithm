import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,per):
    global res
    if n ==N:
        if res < per:
            res = per
        return
    # 가지치기
    # 100보다 작은수면 곱할 수록 작아진다.
    if res >= per or per == 0:
        return

    for i in range(N):
        if not v[i]:
            v[i] = 1
            dfs(n+1,per*arr[n][i]*0.01)
            v[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [0] * N
    res = 0
    dfs(0,1)
    print(f'#{tc} {res*100:.6f}')