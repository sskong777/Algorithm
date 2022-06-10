import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int,input().split()))

arr.reverse()

dp = [1] * N

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘

# 점화식 : D[i] = max(D[i], D[j] + 1) if array[j] < arrary[i]
for i in range(1,N):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(N - max(dp))