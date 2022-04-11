import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(T):
    num = list(map(int,input()))
    num_len = len(num)
    mid_len = num_len//2
    if sum(num[:mid_len]) == sum(num[mid_len:]):
        print('LUCKY')
    else:
        print("READY")