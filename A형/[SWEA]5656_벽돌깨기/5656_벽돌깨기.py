import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # print(arr)
    