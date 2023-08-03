# 구간 합
N, M = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0] * (N+1)
answer = 0
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + arr[i]

for i in range(1,N+1):
    for j in range(1,i):
        if prefix[i]-prefix[j-1] == M:
            answer += 1
print(answer)