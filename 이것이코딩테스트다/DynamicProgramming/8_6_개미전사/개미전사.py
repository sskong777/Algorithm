import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int,input().split()))

d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,N):
    print(d[i-1])
    print(d[i-2],arr[i])
    d[i] = max(d[i-1],d[i-2]+arr[i])

print(d[N-1])
print(d)