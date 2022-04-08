import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input()))

    ssum = arr[0]
    for i in range(1,len(arr)):
        if arr[i-1] != 0:
            ssum *= arr[i]
        else:
            ssum += arr[i]
    print(ssum)