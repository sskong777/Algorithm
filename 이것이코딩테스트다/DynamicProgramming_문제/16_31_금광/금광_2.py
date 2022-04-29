import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    inputt = list(map(int,input().split()))
    n = 0
    for i in range(N):
        for j in range(M):
            arr[i][j] = inputt[n]
            n += 1
    # print(arr)


    for j in range(1,M):
        for i in range(N):
            # 왼쪽 위에서
            if i == 0:
                left_up = 0
            else:
                left_up = arr[i-1][j-1]
            # 왼쪽 아래서
            if i==N-1:
                left_down = 0
            else:
                left_down = arr[i+1][j-1]
            # 왼쪽 옆에서
            left = arr[i][j-1]

            arr[i][j] = arr[i][j] + max(left,left_down,left_up)

    res = 0
    for i in range(N):
        # print(arr[i][M-1])
        res = max(res,arr[i][M-1])
    print(res)