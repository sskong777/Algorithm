
def dfs(L,sum,time):
    global res

    if M < time:
        return

    if L == N:
        res = max(res,sum)

    else:
        dfs(L+1,sum + arr[L][0], time+arr[L][1])
        dfs(L+1,sum,time)

N, M = map(int,input().split())

arr = []
for i in range(N):
    score,time = map(int,input().split())
    arr.append((score,time))
visited = [0] *(N)
res = 0
dfs(0,0,0)

print(res)