from itertools import permutations

N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
data = []
data += permutations(arr,M)
for i in data:
    print(*i)