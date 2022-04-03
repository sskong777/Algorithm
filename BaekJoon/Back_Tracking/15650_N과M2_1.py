from itertools import combinations


N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
data = []
data += combinations(arr,M)

for ans in data:
    print(*ans)