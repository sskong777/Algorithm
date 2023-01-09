import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = map(int,input().split())
    for i in range(1,A*B+1):
        if i % A ==0 and i % B == 0:
            print(i)
            break