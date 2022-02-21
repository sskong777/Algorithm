def isline(arr):
    x = arr[0][0]
    y = arr[0][1]
    flag_x = True
    flag_y = True
    for dup in arr:
        if dup[0] != x:
            flag_x = False
        if dup[1] != y:
            flag_y = False
    return (flag_y or flag_x)


for n in range(4):
    line = list(map(int, input().split()))
    rec1 = line[:4]
    # rec2 = line[4:8]
    point1 = set()
    point2 = set()
    for i in range(rec1[0], rec1[2] + 1):
        for j in range(rec1[1], rec1[3] + 1):
            point1.add((i, j))

    for i in range(rec1[4], rec1[6] + 1):
        for j in range(rec1[5], rec1[7] + 1):
            point2.add((i, j))

    # print(type(point2 & point1))
    # duplicated = list(point1 & point2)
    duplicated = point1 & point2
    if len(duplicated) == 0:
        print('d')
    elif len(duplicated) == 1:
        print('c')
    elif len(duplicated) > 1:
        if isline(duplicated):
            print('b')
        else:
            print('a')

# print(duplicated)
# x = duplicated[0][0]
# y = duplicated[0][1]
# flag_x = True
# flag_y = True
# for dup in duplicated:
#     if dup[0] != x:
#         flag_x = False
#     if dup[1] != y:
#         flag_y = False
# print(flag_x ,flag_y)