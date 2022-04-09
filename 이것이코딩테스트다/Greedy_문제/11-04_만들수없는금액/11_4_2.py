import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

minV = 1

for i in arr:
    if minV < i:
        break
    minV += i


print(minV)
