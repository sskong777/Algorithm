import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
stack = [i for i in range(1,N+1)]
arr = [int(input()) for i in range(N)]
print(arr)