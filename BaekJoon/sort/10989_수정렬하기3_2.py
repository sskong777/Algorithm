import sys

N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]

counts = [0] * 10001

for i in range(N):
    counts[int(sys.stdin.readline())] += 1

for i in range(10001):
    if counts[i] != 0:
        for j in range(counts[i]):
            print(i)