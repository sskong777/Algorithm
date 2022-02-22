import sys
sys.stdin = open('input.txt', 'r')

# 1부터 12까지 숫자를 담아줄 배열 생성
arr = [i for i in range(1,13)]
T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    # 조건을 만족하는 부분집합의 갯수를 담아줄 변수
    count = 0
    for i in range(1 << 12):
        # 부분집합을 담아줄 배열 선언
        sub_set = []
        for j in range(12):
            if i & (1 << j):
                sub_set.append(arr[j])
        # 조건에 맞으면 count수 증가
        if len(sub_set) == n :
            if sum(sub_set) == k:
                count += 1
    print("#{} {}".format(tc,count))


