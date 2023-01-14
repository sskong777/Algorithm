import sys
sys.stdin = open('input.txt' ,'r')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
for i in arr:
    i.sort()
mmin = 100
print(min(arr[0]))
for i in arr:
    if mmin > i[0]:
        mmin = i[0]
print(mmin)