# import sys
# sys.stdin = open('input.txt', 'r')

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0,  1, 0,-1]

# T = int(input())
# for tc in range(1,T+1):

N = int(input())
arr = []
# 배열에 넣기.
for n in range(N):
    arr.append(list(map(int,input())))

# 번호가 2인 출발 지점 찾기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            row = r
            col = c
# stack = [[0]*N for _ in range(N)]
stack = []
visited = [[0]*N for _ in range(N)]
# print(visited)
visited[row][col] = 1
stack.append(row)
stack.append(col)

while stack:
    # if row == 0:
    #     break
    for d in range(4):
        n_row = row + dr[d]
        n_col = col + dc[d]

        if (0 <= n_row < N and 0 <= n_col < N) and arr[n_row][n_col] == 0 and visited[n_row][n_col] == 0:
            row = n_row
            col = n_col
            stack.append(row)
            stack.append(col)
            visited[row][col] = 4

    else:
        visited[row][col] = 0
        col = stack.pop()
        row = stack.pop()

    # if row == 0 and arr[row][col] == 3:
    #     res = 1
print(visited)
print(stack)


