N, K = map(int, input().split())
arr = list(map(int, input().split()))

maxV = -10000
for i in range(len(arr)-K+1):
    sum_K = sum(arr[i:i+K])
    if maxV < sum_K:
        maxV = sum_K
print(maxV)
