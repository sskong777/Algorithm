import sys
sys.stdin = open('input.txt', 'r')

N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
print(arr)
# 정렬 후 가장 큰 수와 그 다음으로 큰 수 변수에 담아주기
mmax = arr[0]
mmmax = arr[1]

ans = 0
while M:
    for i in range(K):
        ans += mmax
        M -= 1
    ans += mmmax
    M -= 1
print(ans)