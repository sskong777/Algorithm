import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(input().split())

move = ['L','R','U','D']

x,y = 1,1
for i in arr:
    if i == 'L':
        nx = x
        ny = y-1
    elif i == 'R':
        nx = x
        ny = y+1
    elif i == 'U':
        nx = x-1
        ny = y
    else:
        nx = x+1
        ny = y
    if 1<=nx<N and 1<=ny<N:
        x,y = nx,ny
print(x,y)