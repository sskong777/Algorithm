def dfs(v):

    if v==N+1:
        for i in range(1,N+1):
            if visited[i]:
                print(i,end=' ')
        print()
    else:

        # 방문처리
        visited[v] = 1
        dfs(v+1)

        # 방문 처리 해제
        visited[v] = 0
        dfs(v+1)

N = int(input())
visited = [0] * (N+1)
dfs(1)
