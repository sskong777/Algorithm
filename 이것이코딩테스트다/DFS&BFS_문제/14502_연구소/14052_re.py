import sys
sys.stdin = open('input.txt', 'r')

N,M = map(int,input().split())

# 지도 입력받기
arr = [(list(map(int,input().split()))) for _ in range(N)]
virus = []
empty = []
walls = 0
safe = 0

