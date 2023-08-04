def dfs(L,price):
    global res

    if L == N+1:
        res = max(res,price)

    else:
        if L+arr[L][0] <= N+1:
            dfs(L+arr[L][0], price+arr[L][1])
        dfs(L+1,price)

N = int(input())
arr = [(0,0)]
for i in range(1,N+1):
    t,p = map(int,input().split())
    arr.append((t,p))

res = 0
dfs(1,0)
print(res)