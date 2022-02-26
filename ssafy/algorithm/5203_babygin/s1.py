arr = list(map(int, input().split()))
N = len(arr)
counts = [0] * 10

for i in range(N):
    counts[arr[i]] += 1
# print(counts)

i = 0
run = tri = 0
while i < 10:
    if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    if counts[i] >= 3:
        counts[i] -= 3
        tri += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("NO")
# for i in range(1, N):
#     counts[i] += counts[i-1]
# print(counts)
