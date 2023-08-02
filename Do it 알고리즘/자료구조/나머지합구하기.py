# https://www.acmicpc.net/problem/11660
import math
import time
import sys
input = sys.stdin.readline
# N = 1,000,000
# M = 1,000
# time : 1s => 20,000,000
# 시간 복잡도 : O(?)
N, M = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0] * N
prefix[0] = arr[0]
answer = 0
C = [0] * M # 나머지가 같은 인덱스 담아줄 배열
for i in range(1,N):
    prefix[i] = prefix[i-1] + arr[i]


for i in range(N):
    remainder = prefix[i] % M
    if remainder == 0:
        answer += 1

    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        # 나머지가 같은 인덱스중 2개를 뽑는 경우의 수
        # nC2
        # answer += (C[i] * (C[i]-1) //2)
        answer += math.comb(C[i],2)

print(answer)