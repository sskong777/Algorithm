import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,cost):
    global res
    if n > 12:
        if res > cost:
            res = cost
        return
    if res < cost:
        return

    dfs(n+1,cost + day*plan[n])
    dfs(n+1,cost + month)
    dfs(n+3,cost + month3)
    dfs(n+12,cost + year)

T = int(input())
for tc in range(1,T+1):
    day,month,month3,year = map(int,input().split())
    plan = [0] + list(map(int,input().split()))

    res = 9999999
    dfs(1,0)
    print(res)