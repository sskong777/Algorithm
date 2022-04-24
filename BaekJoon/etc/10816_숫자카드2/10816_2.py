import sys
sys.stdin = open('input.txt','r')

N = int(input())
cards = list(map(int,input().split()))

M = int(input())
arr = list(map(int,input().split()))

# print(cards)
# print(arr)

dic = {}
for i in cards:
    dic[i] = cards.count(i)
# print(dic)

for i in arr:
    if i not in dic:
        print(0, end=' ')
    else:
        print(dic[i],end=' ')