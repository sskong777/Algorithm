import sys
sys.stdin = open('input.txt' ,'r')

N = int(input())
arr = []
for i in range(N):
    start, end = map(int,input().split())
    arr.append((start,end))

print(arr)
