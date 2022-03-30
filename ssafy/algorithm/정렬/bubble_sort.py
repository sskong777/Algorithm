arr = [55 ,7, 78, 12, 42]
N = len(arr)
# 구간의 마지막 값을 고정시키면서 시작
for i in range(N-1, -1 , -1):
    for j in range(0, i):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
print(arr)