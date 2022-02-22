import sys
sys.stdin = open('input.txt', 'r')

# 이진탐색 함수.
def binarySearch(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    # return False


T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int,input().split())
    count_A = binarySearch(p,a)
    count_B = binarySearch(p,b)
    if count_A < count_B :
        res = 'A'
    elif count_A > count_B:
        res = 'B'
    elif count_A == count_B:
        res = '0'
    print("#{} {}".format(tc, res))




