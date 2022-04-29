import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
d = [0] * (10**6+1)
# print(d)

for i in range(2,N+1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    print(i, d[i])
print(d[N])