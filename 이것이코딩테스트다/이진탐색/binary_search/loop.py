import sys
sys.stdin = open('input.txt', 'r')

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

N,target = map(int,input().split())
arr = list(map(int,input().split()))

result = binary_search(arr,target,0,N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)