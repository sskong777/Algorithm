# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1

# arr = [list(map(int, input().split())) for _ in range(10)]
#
# # 하 우 하 좌
# dr = [1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# nr,nc = 0, 0
# while nc == 10:
#     for d in range(4):
#         if arr[nr+dr[d]][nc+dc[d]] == 1:
#             nr = nr + dr[d]
#             nc = nc + dc[d]


# 교수님 풀이!
# delta 풀이법
import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]
    # 좌 우 상
    dr = [0, 0, -1]
    dc = [-1 ,1, 0]
