# 실패 코드

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
for i in range(len(arr2)-1):
    if arr2[i][1] > arr2[i+1][1]:
        arr2.append([arr2[i][0]+1,arr2[i+1][1]])
arr2.sort()
arr2.append([arr2[-1][0]+1, arr2[-1][1]])
# print(arr2)

# [[2, 4], [4, 6], [8, 10], [9, 8], [15, 8]]
area = 0
for i in range(len(arr2)-1):
    area += (arr2[i+1][0]-arr2[i][0]) * arr2[i][1]
print(area)