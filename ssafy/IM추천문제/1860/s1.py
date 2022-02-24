import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    res = 'Possible'
    for i in range(len(arr)):
        s = (arr[i]//M * K)
        if i+1 <= s:
            continue
        else:
            res = 'Imposible'
            break

    print("#{} {}".format(tc, res))
