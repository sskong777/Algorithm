import sys
sys.stdin = open('input.txt','r')
import time

K = int(input())

# 소인수 분해 최적화(logN)
def prime(k):
    x = k
    arr = []
    for i in range(2, k):
        if i * i > k:
            break

        while x % i == 0:
            arr.append(i)
            x //= i
    if x != 1:  # 만약 제곱수가 아니라면
        arr.append(x)  # 마지막 남은 수를 추가해준다.
    return arr


# 처음에 수박을 2개반드시 이상 서리해야한다.
first = True
s1 = time.time()
print()
while True:
    arr = prime(K)  # 훔친 수박의 정보

    if first and len(arr) == 1:  # 그 길이가 1이면 탈출
        K -= 1
        arr = prime(K)
        first = False
    elif not first and len(arr) == 1:
        break
    K = sum(arr)  # 수박의합

s2 = time.time()
print(*arr)
print(s2 - s1)