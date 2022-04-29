#실패코드

import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]
res = []
while arr:
    if len(arr) < K:
        rem = arr.pop(0)
    else:
        rem = arr.pop(K-1)
        arr = arr[K-1:] + arr[:K-1]
    res.append(rem)
print('<',end='')
for i in range(len(res)-1):
    print("%d, "%res[i], end='')
print(res[-1], end='')
print(">")
