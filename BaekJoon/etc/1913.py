# 1913 달팽이 문제.
n = int(input())
arr = [[0] * n  for _ in range(n)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r,c = 0, 0
num = n ** 2
arr[r][c] = num
while num < n**2:
    for dir in range(4):
        next_row = r + dr[dir]
        next_col = c + dc[dir]

        while 0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] ==0:
            r = next_row
            c = next_col
            num -= 1
            arr[r][c] = num

            next_row = r + dr[dir]
            next_col = c + dc[dir]


for i in arr:
    print(*i)