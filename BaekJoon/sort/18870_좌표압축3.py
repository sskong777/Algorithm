import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

sorted_set = sorted(list(set(arr)))

dict = {sorted_set[i] : i for i in range(len(sorted_set))}


for i in arr:
    print(dict[i], end=' ')
