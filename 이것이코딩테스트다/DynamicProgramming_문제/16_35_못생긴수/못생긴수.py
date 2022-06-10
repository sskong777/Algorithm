import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

ugly = [0] * N
ugly[0] = 1

# 2,3,5배를 위한 인덱스
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

# 1부터 N까지의 못생긴 수를 찾기
for x in range(1,N):
    ugly[x] = min(next2,next3,next5)
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    if ugly[x] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[x] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[x] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[N-1])
