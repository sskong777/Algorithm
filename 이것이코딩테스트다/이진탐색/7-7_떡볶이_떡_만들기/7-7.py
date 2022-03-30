import sys
sys.stdin = open('input.txt','r')

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2

        ssum = 0

        for i in arr:
            if mid >= i:
                ssum += 0
            else:
                ssum += i-mid

        if ssum > target:
            # res = mid
            start = mid + 1
        elif ssum < target:
            end = mid - 1
        else:
            return mid

N,target = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

res = binary_search(arr,target,0,max(arr))
print(res)