def dfs(V):
    global cnt
    if V == M:
        for i in range(M):
            print(visited[i],end=' ')
        print()
        cnt += 1

    else:
        for i in range(1,N+1):
            visited[V] = i
            dfs(V+1)

N ,M = map(int,input().split())
visited = [0] *N
cnt = 0
dfs(0)

