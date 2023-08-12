def dfs(V, answer):
    global cnt
    if V == N:
        cnt += 1
        print(answer)
        return

    else:
        if answer[-1] != '1':
            dfs(V+1, answer +str(1))
        dfs(V+1, answer + str(0))

N = int(input())
cnt = 0
dfs(1, '1')
print(cnt)


