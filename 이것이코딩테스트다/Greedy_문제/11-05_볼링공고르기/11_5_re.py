import sys
sys.stdin = open('input.txt', 'r')

N,M = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(N-1):
    for j in range(i,N):
        if arr[i] != arr[j]:
            cnt += 1
print(cnt)