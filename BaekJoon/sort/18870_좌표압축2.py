N = int(input())
arr = list(map(int,input().split()))

sorted_set = sorted(list(set(arr)))

for i in range(N):
    if arr[i] in sorted_set:
        print(sorted_set.index(arr[i]), end=' ')