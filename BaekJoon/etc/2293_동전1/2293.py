import sys
sys.stdin = open('input.txt', 'r')

N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

d = [0] * (M+1)
d[0] = 1

for i in range(N):
    for j in range(1,M+1):
        if j-arr[i] >= 0:
            d[j] += d[j-arr[i]]

print(d)