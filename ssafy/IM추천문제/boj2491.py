length = int(input())
arr = list(map(int, input().split()))
# count_arr = []
count = 1
max = 2
for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        count+= 1
    else:
        count = 1
    if max < count:
        max = count

# count2 = 1
for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
        count+= 1
    else:
        count = 1
    if max < count:
        max = count
print(max)