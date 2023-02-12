import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

d = [10001] * (M+1)

d[0] = 0
