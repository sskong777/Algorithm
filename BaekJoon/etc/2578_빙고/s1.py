import sys
sys.stdin = open('input.txt', 'r')

# 행과 열은 전치행렬을 통해 함수 하나로 구한다.
# 대각선과 역대각선도 하나의 함수로 구한다.

def line_check(arr):
    count = 0
    arr_T = list(zip(*arr))

    for i in range(5):
        if sum(arr[i]) == 5:
            count += 1

    for i in range(5):
        if sum(arr_T[i]) == 5:
            count += 1

    sum_diag = 0
    for i in range(5):
        sum_diag += arr[i][i]
    if sum_diag == 5:
        count += 1

    reverse_arr = arr[:][::-1]
    sum_re_diag = 0
    for i in range(5):
        sum_re_diag += reverse_arr[i][i]
    if sum_re_diag == 5:
        count += 1

    return count

def ans(pick, bingo):
    cnt = 0
    for pi in range(5):
        for pj in range(5):

            for bi in range(5):
                for bj in range(5):

                    if pick[pi][pj] == bingo[bi][bj]:
                        bingo_chk[bi][bj] = 1
                        cnt += 1
                        # check
                        count = line_check(bingo_chk)
                        if count >= 3:
                            # res = cnt
                            # ans = 1
                            return cnt


bingo = []
bingo_chk = [[0]*5 for _ in range(5)]
pick = []

for i in range(5):
    bingo.append(list(map(int, input().split())))

for i in range(5):
    pick.append(list(map(int, input().split())))


res = ans(pick,bingo)
print(res)









# cnt = 0 # 뽑은 횟수

# for pi in range(5):
#     for pj in range(5):
#
#         for bi in range(5):
#             for bj in range(5):
#
#                 if pick[pi][pj] == bingo[bi][bj]:
#                     bingo_chk[bi][bj] = 1
#                     cnt += 1
#                     # check
#                     count = line_check(bingo_chk)
#                     if count >= 3:
#                         # res = cnt
#                         # ans = 1
#                         print(cnt)
#                         break

