import sys
sys.stdin = open('input.txt', 'r')

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0,  1, 0,-1]

def maze():
    pass

T = int(input())
for tc in range(1,T+1):

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

    stack = []
    res = 0
    while res == 0:
        for d in range(4):
            arr[row][col] = 1
            if 0 <= row+dr[d] <N and 0 <= col+dc[d] < N:
                if arr[row+dr[d]][col+dc[d]] == 0:
                    stack.append([row,col])
                    row += dr[d]
                    col += dc[d]
                    break
                elif arr[row+dr[d]][col+dc[d]] == 3:
                    res = 1
                    break
        else:
            if stack:
                row, col = stack.pop()
            else:
                break
    print("#{} {}".format(tc, res))
    # print(stack)