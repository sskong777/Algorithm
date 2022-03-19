import sys

def counting_sort(N,arr):
    counts = [0] * 10001
    temp = [0] * N

    for i in range(N):
        counts[arr[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # print(counts)

    for i in range(N - 1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]
    return temp


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

sorted_arr = counting_sort(N,arr)
for i in sorted_arr:
    print(i)