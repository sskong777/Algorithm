import sys
sys.stdin = open('input.txt' , 'r')

N = int(input())
K = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for k in range(K):
    row, col = map(int,input().split())
    arr[row][col] = 1

L = int(input())
for l in range(L):
    time, direc = input().split()
    print(time,direc)

print(arr)

