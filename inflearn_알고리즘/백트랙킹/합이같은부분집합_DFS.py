import sys


def dfs(L, sum):
    # L : Level(depth) => arr index

    # 가지치기
    if sum > total//2:
        return
    if L == N:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        # 부분집합에 포함했을 경우와 안했을경우
        dfs(L+1,sum+arr[L])
        dfs(L+1,sum)

N = int(input())
arr = list(map(int,input().split()))
total = sum(arr)
dfs(0,0)
print("NO")


# from itertools import permutations,combinations
# N = int(input())
# arr = list(map(int,input().split()))
#
# answer = "NO"
# for i in range(1,N//2+1):
#     combi_arrs = combinations(arr,i)
#     for i in combi_arrs:
#         remain_set = set(arr) - set(i)
#         if sum(remain_set) == sum(i):
#             answer = "YES"
#             break
# print(answer)