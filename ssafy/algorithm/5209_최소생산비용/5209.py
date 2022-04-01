import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,ssum):
    global res

    # 종료조건
    if n == N:
        # 최소값 갱신
        res = min(res,ssum)
        # if res > ssum:
        #     res = ssum
        return

    # 가지치기 조건
    # 넣어주지 않으면 시간초과.
    if ssum > res:      # SSUM을 더하는중에 이미 res값을 넘어섰다면 최소 비용이 나올 수 없다.
        return

    for i in range(N):
        # 이전 깊이에서 방문하지 않은 인덱스라면
        # dfs 실행
        if not v[i]:
            v[i] = 1        #방문표시
            dfs(n+1,ssum+arr[n][i])
            v[i] = 0        # DFS실행 후 다시 방문표시 초기화

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]

    v = [0]*N
    res = 1500

    dfs(0,0)
    print(f'#{tc} {res}')

