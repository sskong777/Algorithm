import sys
sys.stdin = open('input.txt', 'r')

move = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


N = map(int,input().split())
arr = list(input().split())

x, y = 1, 1

for i in arr:
    for m in range(4):
        if i == move[m]:
            nx, ny = x + dx[m], y + dy[m]

    if 1<=nx<N and 1<=ny<N:
        x,y = nx,ny

print(x,y)