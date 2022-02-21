import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = []
    for i in range(5):
        arr.append(list(input()))
    res = []
    for c in range(15):
        for r in range(5):
            if c < len(arr[r]):
                res.append(arr[r][c])
    print("#{}".format(tc), ''.join(res))



# ABCDE
# abcde
# 01234
# FGHIJ
# fghij


# AABCDD
# afzz
# 0
# 9121
# a8EWg6
# P5h3kx