def dfs(L,sum):
    global cnt
    if sum > T:
        return

    if L == k:
        if sum == T:
            cnt += 1

    else:
        for i in range(arr[L][1]+1):
            dfs(L+1,sum + (arr[L][0]*i))



T = int(input())
k = int(input())
cnt = 0
arr = []
for i in range(k):
    p,n = map(int,input().split())
    arr.append((p,n))

dfs(0,0)

print(cnt)