# 실패코드

import sys
sys.stdin = open('input.txt', 'r')

def run(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
def tri(arr):
    if arr[0]+2 == arr[1]+1 == arr[2]:
        return True

def permu(n,k):
    if n==k:
        arr.append(p)

    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                p[n] = num[i]
                permu(n+1,k)
                used[i] = 0


T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input()))
    p = [0] * 6
    used = [0] * 6
    arr = []

    permu(0,6)

    print(arr)
    # for i in arr:
    #     if run(i[:3]) or tri(i[:3]):
    #         if run(i[3:]) or tri(i[3:]):
    #             print("Ture!!")

