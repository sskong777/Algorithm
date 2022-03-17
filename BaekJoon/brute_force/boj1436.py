N = int(input())
cnt = 0
num = 666   # 첫번째 숫자
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
