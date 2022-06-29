import sys
sys.stdin = open('input.txt' ,'r')

N = int(input())
cards = set(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

for c in check:
    if c in cards:
        print(1,end=' ')
    else:
        print(0, end=' ')