# https://www.acmicpc.net/problem/11660
import time
import sys
input = sys.stdin.readline
# N = 1,000
# M = 100,000
# time : 1s => 20,000,000
# 시간 복잡도 : O(?)
start_time = time.time()
N,M = map(int,input().split())
arr = [[0]* (N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
pre_fix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        pre_fix[i][j] = pre_fix[i][j-1] + pre_fix[i-1][j] - pre_fix[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1,y1, x2,y2 = map(int,input().split())
    answer = pre_fix[x2][y2] - pre_fix[x1-1][y2] - pre_fix[x2][y1-1] + pre_fix[x1-1][y1-1]

    print(answer)


# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4