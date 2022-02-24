search = int(input())
# arr = []
# arr.append([1])
num = 2
i = 1
size = 6
cnt = 1
while num <= search:
    # row = []
    for s in range(size):
        # row.append(num)
        num += 1
    # arr.append(row)
    i += 1
    size += 6
    cnt +=1

print(cnt)