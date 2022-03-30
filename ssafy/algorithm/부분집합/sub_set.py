arr = [3, 6, 7, 1, 5, 4]

n = len(arr)
sub_set_arr = []
for i in range(1 << n):
    sub_set = []
    for j in range(n):
        if i & (1<<j):
            sub_set.append(arr[j])
    sub_set_arr.append(sub_set)
print(sub_set_arr)
print(len(sub_set_arr))