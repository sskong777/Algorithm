# 시간 초과

import sys
sys.stdin = open('input.txt','r')

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))

# print(cards)
# print(arr)

dic = dict()
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)

for i in arr:
    if i not in dic:
        print(0, end=' ')
    else:
        print(dic[i],end=' ')