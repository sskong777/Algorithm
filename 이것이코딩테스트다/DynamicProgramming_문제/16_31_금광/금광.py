# 실패코드 - 문제 잘못 이해함

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
    d = [0]*M

    for i in range(M):
        for j in range(N):
            d[i] = max(d[i],arr[j][i])
    print(sum(d))