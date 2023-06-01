def sol(per):
    print(1-((1-V)*(1-per)))


N = int(input())
arr = list(map(int,input().split()))

v = 0
for i in range(N):
    v = 1 - (1 - v) * (1 - arr[i] / 100)

    print(round(v*100,6))