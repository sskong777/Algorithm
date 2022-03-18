N = int(input())
arr = [int(input()) for i in range(N)]

arr.sort()
for i in range(N):
    print(arr[i])