N = int(input())
arr = []
for n in range(N):
    x ,y = map(int,input().split())
    arr.append([x,y])
arr.sort()
# print(arr)
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
arr2 = []
arr2.append(arr[0])

max = arr[0][1]
for i in range(1,len(arr)-1):
    if arr[i][1] > max:
        max = arr[i][1]
        arr2.append(arr[i])
arr2.append(arr[-1])

# print(arr2)
# [[2, 4], [4, 6], [8, 10], [15, 8]]
