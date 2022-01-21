N = int(input())

cnt = 0
num = N

while True:
    a = num //10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    # num = ((N // 10 + N % 10) % 10) + ((N % 10) * 10)
    cnt += 1

    if num == N:
        break
        

print(cnt)