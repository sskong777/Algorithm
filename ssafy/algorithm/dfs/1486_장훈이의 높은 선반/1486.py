import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,ssum):
    global ans
    if n == N:
        if ssum >= B and \
            ans > ssum -B:
            ans = ssum - B
        return

    dfs(n+1,ssum + arr[n])
    dfs(n+1,ssum)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))

    ans = 12345678
    dfs(0,0)
    print(f'#{tc} {ans}')