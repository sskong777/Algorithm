import sys
sys.stdin = open('input.txt', 'r')
def binary_search(arr,target,start,end):
    if start > end:
        return

    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

def binary_search_loop(arr,target,start,end):

    while start <= end:
        mid = (start+end)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


def solution(arr,start,end):
    while start <= end:
        mid = (start+end)//2
        currnet = arr[0]
        cnt = 1

        # 공유기 설치
        for i in range(1,len(arr)):
            if arr[i] >= currnet + mid:
                cnt += 1
                currnet = arr[i]
        # 공유기 수가 초과 되면 더 넓게 설치할 수 있다는 얘기 -> mid+1
        if cnt >= C:
            start = mid + 1
            res = mid

        # 공유기가 C개를 넘어가지 않는다면 더 좁게 설치해야함
        else:
            end = mid - 1

    return res


N, C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
start, end = 1,(arr[-1] - arr[0])

res = solution(arr,start,end)
print(res)