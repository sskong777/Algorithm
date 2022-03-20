N = int(input())
arr = []
for n in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))
# print(arr)

rank = [1] * N
for i in range(N):
    for j in range(N):
        if j == i:
            continue
        else:
          # print(arr[j][0])
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                rank[i] += 1

print(' '.join(map(str,rank)))
# print(*rank)