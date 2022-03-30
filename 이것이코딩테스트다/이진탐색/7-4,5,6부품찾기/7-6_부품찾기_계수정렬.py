import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
count = [0] * 1000001
for i in range(N):
    count[arr[i]] = 1

t_N = int(input())
t_arr = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(t_N):
    if count[t_arr[i]] == 1:
        print("yes", end= ' ')
    else:
        print("no", end=' ')