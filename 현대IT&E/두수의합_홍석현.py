def two_sum(arr, target):
    count = 0
    left, right = 0, len(arr)-1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            left += 1
            count += 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return count

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()

ans = two_sum(arr,x)

print(ans)

