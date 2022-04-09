import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    data = []
    data += combinations(arr,2)

    cnt = 0
    for i in data:
        if i[0] == i[1]:
            continue
        else:
            cnt += 1

    print(cnt)
