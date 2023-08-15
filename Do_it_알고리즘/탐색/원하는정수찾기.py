# 이진 탐색

N = int(input())
arr = list(map(int,input().split()))
find_N = int(input())
find_arr = list(map(int,input().split()))

# 이진 탐색을 위해 정렬
arr.sort()

for find in find_arr:
    isfind = False

    target = find
    start, end = 0, N-1
    while start <= end:
        mid_index = int((start+end) / 2)
        min_val = arr[mid_index]
        if min_val > target:
            end = mid_index - 1
        elif min_val < target:
            start = mid_index + 1
        else:
            isfind = True
            break

    if isfind:
        print(1)
    else:
        print(0)