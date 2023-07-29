import sys

input=sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

# 합 배열 만들어주기    #O(N)
for num in arr:
    temp += num
    prefix_sum.append(temp)

# 합 배열을 통해 구간 합 구하기 #O(N)
for _ in range(M):
    i,j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i-1])