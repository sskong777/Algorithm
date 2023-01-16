import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int,input().split()))
# print(arr)

arr.sort()
cnt = 0
for i in arr:
    if len(arr) >= i:
        cnt += 1
        for i in range(i):
            arr.remove(arr[-1])
    else:
        break

print(cnt)