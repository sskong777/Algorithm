N = int(input())
arr = []
for n in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])
# print(arr)
arr.sort()
arr.sort(key=lambda x: (x[1],x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])