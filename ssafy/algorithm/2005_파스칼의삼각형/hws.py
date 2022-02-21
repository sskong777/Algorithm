T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for i in range(N)]

    arr[0][0] = 1
    for n in range(1,N):
        for i in range(n+1):
            if i == 0 or i == n:
                arr[n][i] = 1
            else:
                arr[n][i] = arr[n-1][i-1] + arr[n-1][i]
    print("#{}".format(tc))
    for a in arr:
        for i in a:
            if i != 0:
                print(i,end=' ')
        print()

