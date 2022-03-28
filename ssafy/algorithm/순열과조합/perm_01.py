def perm():
    for i in range(N):
        for j in range(N):
            if i != j:
                print(a[i],a[j])

a = [1,2,3]
N = len(a)
perm()