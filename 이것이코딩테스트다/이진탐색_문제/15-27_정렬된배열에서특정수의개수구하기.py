# loop를 이용한 binary_search
def binary_search(arr,target,start,end):
    global cnt
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return

N,x = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0