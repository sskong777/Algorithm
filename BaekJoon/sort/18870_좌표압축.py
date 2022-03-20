import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
ans = [0] * N


for i in range(N):
    count = 0
    num = []
    for j in range(N):
        if i==j or arr[j] in num:
            continue
        if arr[i]>arr[j]:
            count += 1
            num.append(arr[j])
    ans[i] = count
print(*ans)