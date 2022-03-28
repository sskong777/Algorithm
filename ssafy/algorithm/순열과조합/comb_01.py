def comb():
    for i in range(N-1):
        for j in range(i+1,N):
            print(a[i],a[j])

a = [1,2,3]
N = len(a)
comb()