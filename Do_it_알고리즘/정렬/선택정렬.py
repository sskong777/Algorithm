# https://www.acmicpc.net/problem/1427
# 버블정렬
import time
import sys
input = sys.stdin.readline
# N = 1,000
# time : 2s => 20,000,000
# 시간 복잡도 : O(n^2)

arr = list(map(int,list(input())))
print(arr)
N = int(input())

for i in range(N):
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)


# 5
# 2
# 3
# 4
# 1