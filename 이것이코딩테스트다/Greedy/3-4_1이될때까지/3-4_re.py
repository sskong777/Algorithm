import sys
sys.stdin = open('input.txt', 'r')

N,K = map(int,input().split())

cnt = 0
while N >= K:
    while not N % K:
        N -= 1
        cnt += 1
    N //= K
    cnt += 1

while N == 1:
    N -= 1
    cnt += 1
print(cnt)
