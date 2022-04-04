import sys
sys.stdin =open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        minV = min(arr[i])
        res = max(res,minV)

    print(res)