import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    if si < 0 or si >=N or sj < 0 or sj>=M:
        return False

    if arr[si][sj]==1:
        # 방문 표시
        arr[si][sj] = 0

        dfs(si-1,sj)
        dfs(si+1,sj)
        dfs(si,sj+1)
        dfs(si,sj-1)
        return True
    return False


T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        col,row = map(int,input().split())
        arr[row][col] = 1

    cnt = 0

    for si in range(N):
        for sj in range(M):
            if dfs(si,sj):
                cnt += 1

    print(cnt)