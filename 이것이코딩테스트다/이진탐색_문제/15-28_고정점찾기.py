def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return

# arr = [-15,6,1,3,7]
arr = [-15,-4,3,8,9,13,15]

res = -1
for i in range(len(arr)):
    if i == binary_search(arr,i,0,len(arr)-1):
        res = i

print(res)