import heapq
import sys

N = int(sys.stdin.readline().rstrip())
# arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

heap = []   # 힙 생성
for n in range(N):
    data = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap,data)   # heap으로 push

# print(heap)
res = 0
while len(heap) != 1:    # heap이 2개 이상 남아있을 때까지 반복
    # 가장 작은 카드 2개 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    ssum = one+two
    res += ssum
    heapq.heappush(heap,ssum)
print(res)