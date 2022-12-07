import sys
sys.stdin = open('input.txt', 'r')

C = int(input())

for tc in range (C):
    array  = list(map(int,input().split()))
    N  = array[0]
    sum_score = sum(array[1:])
    avg = sum_score / N
    # print(avg)
    cnt = 0
    for score in array[1:]:
        if score > avg:
            cnt += 1
    print("{:.3f}%".format(cnt / N * 100))
