dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1 ,-1, 1, -1]

arr = [[1,2,3], [4,5,6], [7,8,9]]
total_arr = []
for r in range(3):
    for c in range(3):
        total = arr[r][c]
        for dir in range(8):
            row = r + (dr[dir])
            col = c + (dc[dir])
            if 0 <= row <= 3 - 1 and 0 <= col <= 3 - 1:
                total += arr[row][col]
        total_arr.append(total)
print(total_arr)