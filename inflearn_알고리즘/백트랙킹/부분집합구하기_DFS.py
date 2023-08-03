def dfs(v):

    if v==N+1:
        for i in range(1,N+1):
            if visited[i]:
                print(i,end=' ')
        print()
    else:

        visited[v] = 1
        dfs(v+1)
        visited[v] = 0
        dfs(v+1)

N = int(input())
visited = [0] * (N+1)
dfs(1)
#
#
# def DFS(v):
#     if v == n + 1:
#         for i in range(1, n + 1):
#             if ch[i] == 1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v] = 1
#         DFS(v + 1)
#         ch[v] = 0
#         DFS(v + 1)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     ch = [0] * (n + 1)
#     DFS(1)
