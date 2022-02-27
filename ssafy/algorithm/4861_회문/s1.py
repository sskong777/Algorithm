import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 회귀문으로 판별
def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))

    # arr = [input() for _ in range(N)]

    str_row = []
    str_col = [''] * N
    for idx in range(N):
        in_str = input()
        str_row.append(in_str) # 가로 문장
        for i in range(N):
            str_col[i] += in_str[i] # 세로 문장만들기

    # str_col = [''.join(list(zip(*str_row))[i]) for i in range(N)]
    # print(str_col)
    # 전체 문장 만들기 (빼고 각각 돌리는게 효율이 좋을듯)
    arr = str_row + str_col   # 가로문장리스트 + 세로 문장 리스트

    # 회문 판별
    res = ''
    for idx in range(len(arr)):
        # M 개 만큼 회문 판별
        for dt in range(N-M+1):
            target = arr[idx][dt:M+dt]
            if palindrome(target):
                res = target
                break

        if res:
            break
    #
    print('#{} {}'.format(test_case, res))