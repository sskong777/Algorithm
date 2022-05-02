import sys
sys.stdin = open('input.txt')

d = [0]*100

def fibo(x):
    # 종료 조건
    if x==1 or x==2:
        return 1
    # 이미 구한 값이라면(메모제이션에 저장되어있는 값이라면)
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-2) + fibo(x-1)
    return d[x]


T = int(input())
for tc in range(T):
    N = int(input())
    fibo(N)
