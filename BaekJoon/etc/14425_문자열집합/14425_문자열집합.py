import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
S = []
check = []
for n in range(N):
    S.append(input())

for m in range(M):
    check.append(input())

print(S)
print('=--====')
print(check)