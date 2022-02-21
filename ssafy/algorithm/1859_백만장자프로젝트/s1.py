import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    mmax = arr[-1]
    cnt = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > mmax:
            mmax = arr[i]
        else:
            cnt += (mmax-arr[i])
    print("#{} {}".format(tc, cnt))
