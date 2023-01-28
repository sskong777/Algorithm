import sys
sys.stdin = open('input.txt', 'r')


mmax = -1000000000
mmin = 1000000000

T = int(input())
for tc in range(T):

    N = int(input())
    arr = list(map(int, input().split()))
    operator = list(map(int, input().split()))

    def dfs(i, ssum, plus, minus, multiply, divide):
        global mmax, mmin

        if i == N:
            mmax = max(ssum, mmax)
            mmin = min(ssum, mmin)
            return
        if plus:
            dfs(i+1,ssum + arr[i],plus-1, minus, multiply, divide)

        if minus:
            dfs(i+1,ssum - arr[i], plus, minus-1, multiply, divide)

        if multiply:
            dfs(i+1, ssum * arr[i], plus, minus, multiply-1, divide)

        if divide:
            dfs(i+1, int(ssum/arr[i]), plus, minus, multiply, divide-1)


    dfs(1, arr[0], operator[0], operator[1], operator[2], operator[3])

    print(mmax)
    print(mmin)
