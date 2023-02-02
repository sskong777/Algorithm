import sys
sys.stdin = open('input.txt', 'r')

# 0) 총 비교한 횟수(answer)를 0으로 둔다.
#
# 1) 현재의카드 묶음(card_deck) 중 가장 작은 2개의 카드 묶음을 꺼낸다.
#
# 2) 두 개를 더한 값 = 현재 단계에서 비교한 횟수
#
# 3) 두 개를 더한 값을 총 비교한 횟수에 더해준다.
#
# 4) 두 개를 더한 값을 다시 카드 더미 안에 넣는다.
#
# 5) 1 ~ 4 과정을 힙에 하나의 덱만 남을 때 까지 반복한다.

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