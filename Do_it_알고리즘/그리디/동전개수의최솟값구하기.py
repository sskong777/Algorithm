# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

n, target = map(int,input().split())
arr = [int(input()) for _ in range(n)]

answer = 0

for i in range(n-1,-1,-1):
    if arr[i] <= target:
        answer += int(target/arr[i])
        target %= arr[i]
print(answer)