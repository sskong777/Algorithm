for tc in range(1,11):
    n = int(input())
    arr = []
    arr = [list(map(int,input().split())) for _ in range(100)]
    res = []
    # 1. 각 행의 합
    r_total_arr= []
    for c in range(100):
        r_total_arr.append(sum(arr[c]))
    res.append(max(r_total_arr))
    # print(max(r_total_arr))

    # 2. 각 열의 합
    c_total_arr = []
    for r in range(100):
        c_total = 0
        for c in range(100):
            c_total += arr[c][r]
            # print(arr[c][r], end= ' ')
        c_total_arr.append(c_total)
    res.append(max(c_total_arr))
    # print(max(c_total_arr))

    # 3. 각 대각선의 합
    d_total = 0
    for c in range(100):
        for r in range(100):
            if c == r:
                d_total += arr[c][r]
    res.append(d_total)
    # print(d_total)

    r_d_total = 0
    for c in range(100):
        for r in range(100):
            if c + r == 99:
                r_d_total += arr[c][r]
    res.append(r_d_total)
    # print(r_d_total)
    # print(max(res))

    print("#{} {}".format(tc, max(res)))
# 1
# 4 4 3 2 1
# 2 2 1 6 5
# 3 5 4 6 7
# 4 2 5 9 7
# 8 1 9 5 6