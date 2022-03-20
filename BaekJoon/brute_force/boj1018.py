from pprint import pprint
# def check_board(arr, M, N):
#     B_arr = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
#     W_arr = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
#     for i in range(M):

N, M = map(int,input().split())
# arr = [input() for _ in range(N)]
arr = []
for i in range(N):
    arr.append(input())
# pprint(arr)

count = []
for i in range(N-8+1):
    for j in range(M-7):
        w_count = 0     # w가 먼저 시작하는 경우
        b_count = 0     # b가 먼저 시작하는 경우
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if arr[k][l] != 'W':
                        w_count += 1
                    if arr[k][l] != 'B':
                        b_count += 1
                else:
                    if arr[k][l] != 'B':
                        w_count += 1
                    if arr[k][l] != 'W':
                        b_count += 1
        count.append(min(w_count,b_count))
print(min(count))

