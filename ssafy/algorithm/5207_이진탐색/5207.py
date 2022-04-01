import sys
sys.stdin = open('input.txt', 'r')

def binary_search_loop(arr, target, start, end, r_cnt, l_cnt):
    global cnt
    while start <= end:
        mid = (start + end) // 2

        if r_cnt==2 or l_cnt ==2:
            return
        if arr[mid] == target:
            cnt += 1
            return
        elif arr[mid] > target:
            end = mid -1
            l_cnt += 1
            r_cnt = 0
        else:
            start = mid + 1
            r_cnt += 1
            l_cnt = 0
    return False

# def binary_search(arr,target,start,end):
#     if start > end:
#         return
#     mid = (start+end)//2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr,target,start,mid-1)
#     else:
#         return binary_search(arr,target,mid+1,end)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))

    cnt = 0

    for i in B:
        binary_search_loop(A,i,0,N-1,0,0)

    print(f'#{tc} {cnt}')