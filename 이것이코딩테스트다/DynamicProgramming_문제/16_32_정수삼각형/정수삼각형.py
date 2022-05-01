# 실패코드
import sys
sys.stdin = open('input.txt', 'r')

# 점화식 : arr[i][j] = arr[i][j] + max(arr[i-1][j-1],arr[i-1][j])

N = int(input())
# arr = [[0]*N for _ in range(N)]
arr = []
for i in range(N):
    arr.append([0] + list(map(int,input().split())))
# print(arr)

for i in range(1,N):
    for j in range(1,i+1):
        arr[i][j] = arr[i][j] + max(arr[i-1][j-1],arr[i-1][j])

# print(arr)
print(max(arr[N-1]))