import sys
sys.stdin = open('input.txt', 'r')

# 점화식 : arr[i][j] = arr[i][j] + max(arr[i-1][j-1],arr[i-1][j])

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            left = 0
        else:
            left = arr[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = arr[i-1][j]

        arr[i][j] = arr[i][j] + max(left,up)

print(max(arr[N-1]))