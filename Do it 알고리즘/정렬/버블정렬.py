# https://www.acmicpc.net/problem/
# 버블정렬
import time
import sys
input = sys.stdin.readline
# N = 1,000
# time : 2s => 20,000,000
# 시간 복잡도 : O(n^2)

N = int(input())
arr = [int(input()) for _ in range(N)]
# print(arr)

for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)


# 5
# 2
# 3
# 4
# 1