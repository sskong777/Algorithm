import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
# print(arr)

ans = 0
cnt = 0
for i in range(M):
    if cnt >= K:
        ans += arr[1]
        cnt = 0
    else :
        ans += arr[0]
        cnt += 1

print(ans)