import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
S = set()
# check = []
count = 0
for n in range(N):
    S.add(input())

for m in range(M):
    str_m = input()
    if str_m in S:
        count += 1

print(count)
