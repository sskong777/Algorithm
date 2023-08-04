def dfs(L):
    print(money)
    global res
    if L == N:
        cha = max(money)-min(money)
        if cha < res:
            temp = set()
            for x in money:
                temp.add(x)
            if len(temp) == 3:
                res = cha

    else:
        for i in range(3):
            money[i] += arr[L]
            dfs(L+1)
            money[i] -= arr[L]

N = int(input())
arr = [int(input()) for _ in range(N)]
res = int(1e9)
money = [0] * 3
dfs(0)
print(res)