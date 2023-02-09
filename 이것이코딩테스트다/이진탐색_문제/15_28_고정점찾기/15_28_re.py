import sys
sys.stdin = open('input.txt', 'r')


def binary_search(array,target,start,end):
    if start > end:
        return
    mid = (start+end)//2

    if array[mid] == target:
        return mid

    #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    res = -1
    for i in range(N):
        if i == binary_search(arr,i,0,N-1):
            res = i

    print(res)


