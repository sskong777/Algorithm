arr = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i],arr[i][j]

print(arr)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 두번째 방법 - zip함수 사용
transpose_matix = list(zip(*arr))
print(transpose_matix)