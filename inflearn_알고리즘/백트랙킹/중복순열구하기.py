def dfs(V):
    print(arr)
    global cnt
    if V == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1,N+1):
            arr[V] = i
            dfs(V+1)

N ,M = map(int,input().split())
arr = [0] * N
cnt = 0
dfs(0)
print(cnt)

# from itertools import product
# N ,M = map(int,input().split())
#
# # 중복순열을 구할 원소들
# elements = [i for i in range(1,N+1)]
#
# # 원소들로 중복순열 구하기
# result = list(product(elements, repeat=M))
# for i in result:
#     print(*i)
# print(len(result))