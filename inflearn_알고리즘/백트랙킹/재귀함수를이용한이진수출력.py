N = int(input())


def dfs(N):
    if N == 0:
        return
    dfs(N//2)
    print(N%2,end='')

dfs(N)
