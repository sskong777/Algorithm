import sys
sys.stdin = open('input.txt', 'r')

N = map(int,input().split())
arr = list(map(int,input().split()))
# print(arr)
arr.sort()

minV = 1
for i in arr:
    if minV < i:
        break
    minV += i

print(minV)