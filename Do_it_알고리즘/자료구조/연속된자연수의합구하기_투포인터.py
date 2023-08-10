# https://www.acmicpc.net/problem/2018
import math
import time
import sys
input = sys.stdin.readline
# N = 10,000,000
# time : 2s => 40,000,000
# 시간 복잡도 : O(?) => O(n)으로 풀어야함
N = int(input())
cnt = 1
start_index = 1
end_index = 1
sum = 1

while end_index != N:
    if sum == N:
        cnt += 1
        end_index +=1
        sum += end_index

    elif sum > N:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(cnt)