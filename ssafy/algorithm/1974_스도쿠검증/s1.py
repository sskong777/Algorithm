import sys
sys.stdin = open('input.txt', 'r')

# 행, 열 검사 함수
def check_r_c(arr):
    cnt = 0
    flag = False
    # 행 검사
    for r in range(9):
        check = set()
        for c in range(9):
            check.add(arr[r][c])
        if len(check) == 9:
            cnt += 1
    if cnt == 9:
        flag = True
    else:
        flag = False
    return flag

def check_3x3(arr):
    flag2 = False
    set2 = []
    cnt = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            set1 = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    set1.add(arr[r][c])
            if len(set1) ==9:
                cnt += 1
    if cnt == 9:
        flag2 = True
    else:
        flag2 = False
    return flag2



T = int(input())
for tc in range(1,T+1):
    arr = []
    for n in range(9):
        arr.append(list(map(int, input().split())))
    arr_T = list(zip(*arr))

    res1 = check_r_c(arr)
    res2 = check_r_c(arr_T)
    res3 = check_3x3(arr)

    print("#{} {}".format(tc, int(res1 & res2 & res3)))











    # # 3x3 검사
    # r = c = 0
    # plus = 3
    # flag2 = False
    # cnt2 = 0
    # while True:
    #     check2 = set()
    #     for i in range(r, r+plus):
    #         for j in range(c, c+plus):
    #            check2.add(arr[i][j])
    #     if len(check2) == 9:
    #         cnt2 += 1
    #
    #     c += plus
    #
    #     if c > 6:
    #         c = 0
    #         r += plus
    #
    #     if r > 6:
    #         break
    #
    #     if cnt2 == 9:
    #         flag2 = True
    #     else:
    #         flag2 = False


    # res = check_r_c(arr)
    # res = check_r_c(arr_T)
    # print(int(res))




    # cnt = 0
    # flag = False
    # # 행 검사
    # for r in range(9):
    #     check = set()
    #     for c in range(9):
    #         check.add(arr[r][c])
    #     if len(check) == 9:
    #         cnt += 1
    #
    # if cnt == 9:
    #     flag = True
    # else:
    #     flag = False
    #
    # # 열 검사
    # cnt = 0
    # for r in range(9):
    #     check = set()
    #     for c in range(9):
    #         check.add(arr_T[r][c])
    #     if len(check) == 9:
    #         cnt += 1
    #
    # if cnt == 9:
    #     flag = True
    # else:
    #     flag = False