# https://www.acmicpc.net/problem/11659
import time

# N = 100,000
# M = 100,000
# time : 0.5s => 20,000,000
# O(n2)하면 터짐

# 시간 복잡도 : O(N+M)
start_time = time.time()
N,M = map(int,input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

# 합 배열 만들어주기    #O(N)
for num in arr:
    temp += num
    prefix_sum.append(temp)
print(prefix_sum)

# 합 배열을 통해 구간 합 구하기 #O(N)
for _ in range(M):
    i,j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
print(time.time() - start_time)
# 0.7523326873779297




# 시간초과
# 시간 복잡도 : O(n2)
# sum() : O(n)
# for 문 : O(n)
# time complex : O(n2) => 10,000,000,000
# start_time = time.time()
# N,M = map(int,input().split())
# arr = list(map(int,input().split()))
#
# for _ in range(M):
#     i,j = map(int,input().split())
#     print(sum(arr[i-1:j]))
# print(time.time() - start_time)
# 0.8168659210205078
