
n = int(input())
plan = list(input().split())

x,y = 1,1

move = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in plan:
    for j in range(len(move)):
        if i == move[j] :
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)

# 0120