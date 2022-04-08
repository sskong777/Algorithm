import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = sorted(list(map(int,input().split())))
# print(arr)
res = 0
cnt = 0
for i in arr:
    cnt += 1
    if cnt >=i:
        res += 1
        cnt = 0

print(res)