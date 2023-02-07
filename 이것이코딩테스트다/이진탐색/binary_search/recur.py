import sys
sys.stdin = open('input.txt', 'r')

def binary_search(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr, target, mid+1, end)



N, target = map(int,input().split())
arr = list(map(int,input().split()))

result = binary_search(arr,target,0,N-1)
if result==None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)