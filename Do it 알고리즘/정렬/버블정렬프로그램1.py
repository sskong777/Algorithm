# https://www.acmicpc.net/problem/
import time
import sys
input = sys.stdin.readline
# N = 500,000
# time : 2s => 20,000,000
# 버블 정렬 O(n^2)로 풀면 터짐
# 시간 복잡도 : O(?)

N = int(input())
arr = [int(input()) for _ in range(N)]
