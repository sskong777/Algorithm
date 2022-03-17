arr = list(map(int,input().split()))
# print(arr)
a_cnt, d_cnt = 0, 0
for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
        a_cnt += 1
    if arr[i-1] > arr[i]:
        d_cnt += 1

if a_cnt == len(arr)-1:
    print("ascending")
elif d_cnt == len(arr)-1:
    print("descending")
else:
    print("mixed")
