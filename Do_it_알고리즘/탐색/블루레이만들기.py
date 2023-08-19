def binary_search(start,end, arr, target):
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return

