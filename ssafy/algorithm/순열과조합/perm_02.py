# 순열 함수
def perm(arr, n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]


arr = [1, 2, 4, 7, 8, 3]
perm(arr, len(arr), 0)