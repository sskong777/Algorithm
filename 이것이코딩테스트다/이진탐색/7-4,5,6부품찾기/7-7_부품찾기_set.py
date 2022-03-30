import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
set_arr = set(arr)

t_N = int(input())
t_arr = list(map(int,sys.stdin.readline().rstrip().split()))

for i in t_arr:
    if i in set_arr:
        print("yes", end=' ')
    else:
        print("no", end=' ')
