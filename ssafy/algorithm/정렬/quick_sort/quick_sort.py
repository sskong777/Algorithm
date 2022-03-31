import sys
sys.stdin = open('input.txt', 'r')

# Hoare-Partition 알고리즘
def partition(arr,start,end):
    pivot = (start+end)//2
    L = start
    R = end
    while L < R:
        while (L<R and arr[L] < arr[pivot]):
            L += 1
        while (L<R and arr[R] >= arr[pivot]):
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L],arr[R] = arr[R],arr[L]
    arr[pivot], arr[R] = arr[R],arr[pivot]
    return R

def quick_sort(arr,start,end):
    if start < end:
        p = partition(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    start = 0
    end = len(arr)-1
    quick_sort(arr,start,end)
    print(*arr)