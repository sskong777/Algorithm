from heapq import *
def solution(scoville, K):
    count = 0
    # list = []
    # for num in scoville:
    #     pass

    heapify(scoville)

    print(scoville)
    while scoville[0] < K : # scovile의 가장 작은 수가 기준보다 낮다면
        if len(scoville) > 1:
            count += 1
            first = heappop(scoville)
            second = heappop(scoville)
            print(first,second)

            heappush(scoville, first + second * 2)
        else:
            return -1

    return count


# solution([5,3,213,34,12,64,2],6)