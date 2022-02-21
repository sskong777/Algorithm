import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = []
    N, M = map(int, input().split())
    for n in range(N):
        arr.append(list(map(int,input().split())))
    sol = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    cnt += arr[i][j]
            if sol < cnt:
                sol = cnt
    print("#{} {}".format(tc, sol))