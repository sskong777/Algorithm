import sys
sys.stdin = open('input.txt')
def binary_search(arr,target,start,end):
    if start > end:
        return

    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-2)



N = int(input())
# arr = list(map(int,input().split()))
arr = list(map(int,sys.stdin.readline().rstrip().split()))

t_N = int(input())
t_arr = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(t_N):
    if binary_search(arr,t_arr[i],0,N-1):
        print("yes",end=' ')
    else:
        print("no", end=' ')

