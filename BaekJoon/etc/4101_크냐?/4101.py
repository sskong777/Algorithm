import sys
sys.stdin = open('input.txt', 'r')

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        exit(0)
    if a > b:
        print("Yes")
    else:
        print("No")