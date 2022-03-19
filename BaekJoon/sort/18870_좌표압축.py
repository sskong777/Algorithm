N = int(input())
arr = list(map(int,input().split()))
ans = []


for i in range(N):
    count = 0
    num = []
    for j in range(N):
        if i==j or arr[j] in num:
            continue
        if arr[i]>arr[j]:
            count += 1
            num.append(arr[j])

    ans.append(count)
print(*ans)