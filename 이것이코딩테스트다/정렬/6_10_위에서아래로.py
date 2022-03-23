N = int(input())
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(input())
# print(arr)
arr = [int(input()) for _ in range(N)]

arr.sort()
print(*arr)