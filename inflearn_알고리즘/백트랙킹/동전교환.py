def dfs(L,sum):
    global mmin
    if mmin <= L:
        return
    if sum > M:
        return
    if sum == M:
        if L < mmin:
            mmin = L

    else:
        for i in range(N):
            dfs(L+1,sum+arr[i])

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
mmin = int(1e9)
arr.sort(reverse=True)

dfs(0,0)
print(mmin)