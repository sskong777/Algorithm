import sys
sys.stdin = open('input.txt' ,'r')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
for i in arr:
    i.sort()
mmax = 0

for i in arr:
    if mmax < i[0]:
        mmax = i[0]
print(mmax)