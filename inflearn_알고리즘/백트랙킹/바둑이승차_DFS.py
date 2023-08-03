
# def DFS(L, sum, tsum):
#     global result
#     if sum+(total-tsum)<result:
#         return
#     if sum>C:
#         return
#     if L==N:
#         if sum>result:
#             result=sum
#     else:
#         DFS(L+1, sum+arr[L], tsum+arr[L])
#         DFS(L+1, sum, tsum+arr[L])
#
#
# C, N = map(int,input().split())
# arr = [int(input()) for _ in range(N)]
# total = sum(arr)
# DFS(0, 0, 0)
# print(result)


def dfs(L,sum):
    if sum > C:
        return

    global result
    if L==N:
        if sum > result:
            result = sum
    else:
        dfs(L + 1, sum + arr[L])
        dfs(L + 1, sum)


C, N = map(int,input().split())
arr = [int(input()) for _ in range(N)]
total = sum(arr)
result = 0
dfs(0, 0)
print(result)