arr = [0, 4, 1, 3 ,1, 2, 4, 1]
N = len(arr)
# 1~4
counts = [0] * 5
temp = [0] * N

for i in range(N):
    counts[arr[i]] += 1
print(counts)

for i in range(1, len(counts)):
    counts[i] += counts[i-1]
print(counts)

for j in range(N-1, -1, -1):
    counts[arr[j]] -= 1
    temp[counts[arr[j]]] = arr[j]

print(temp)