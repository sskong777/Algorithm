N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
# print(arr)

for m in range(M):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
