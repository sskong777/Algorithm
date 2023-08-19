import heapq

N = int(input())

arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

if len(arr) == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        temp1 = heapq.heappop(arr)
        temp2 = heapq.heappop(arr)
        answer += temp1 + temp2
        heapq.heappush(arr, temp1+temp2)
    print(answer)